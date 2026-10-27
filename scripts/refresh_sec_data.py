#!/usr/bin/env python3
"""Refresh static company, filing and financial data from public SEC EDGAR endpoints."""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
WATCHLIST = ROOT / "config" / "watchlist.json"
OUTPUT = ROOT / "site" / "data"
UA = os.environ.get("SEC_USER_AGENT", "").strip()
if not UA or "@" not in UA:
    raise SystemExit("Set SEC_USER_AGENT to an app name and monitored contact email (GitHub Actions variable).")

HEADERS = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate", "Accept": "application/json"}
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
CONCEPTS = {
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "Revenues"],
    "net_income": ["NetIncomeLoss"],
    "total_assets": ["Assets"],
    "total_liabilities": ["Liabilities"],
    "cash_and_equivalents": ["CashAndCashEquivalentsAtCarryingValue"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
}

def get_json(url: str):
    request = Request(url, headers=HEADERS)
    try:
        with urlopen(request, timeout=30) as response:
            payload = response.read()
        # SEC responses are usually uncompressed by urllib unless requested; decode safely.
        import gzip
        if payload[:2] == b"\x1f\x8b":
            payload = gzip.decompress(payload)
        return json.loads(payload.decode("utf-8"))
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"SEC request failed for {url}: {exc}") from exc

def newest_fact(companyfacts: dict, candidates: list[str]):
    us_gaap = companyfacts.get("facts", {}).get("us-gaap", {})
    for concept in candidates:
        item = us_gaap.get(concept)
        if not item:
            continue
        units = item.get("units", {})
        preferred = units.get("USD") or units.get("shares") or next(iter(units.values()), [])
        annual = [row for row in preferred if row.get("form") in ("10-K", "20-F") and row.get("fp") == "FY"]
        if not annual:
            annual = [row for row in preferred if row.get("form") in ("10-K", "20-F")]
        if annual:
            row = max(annual, key=lambda r: (r.get("end", ""), r.get("filed", "")))
            return {"concept": concept, "label": item.get("label", concept), "unit": next((u for u, rows in units.items() if row in rows), None),
                    "value": row.get("val"), "period_end": row.get("end"), "filed": row.get("filed"),
                    "form": row.get("form"), "accession_number": row.get("accn")}
    return None

def main():
    config = json.loads(WATCHLIST.read_text(encoding="utf-8"))
    wanted = [str(t).strip().upper() for t in config.get("tickers", []) if str(t).strip()]
    if not wanted:
        raise SystemExit("config/watchlist.json has no tickers.")
    ticker_payload = get_json(TICKERS_URL)
    ticker_rows = ticker_payload.values() if isinstance(ticker_payload, dict) else []
    by_ticker = {str(row.get("ticker", "")).upper(): row for row in ticker_rows}
    companies = []
    for ticker in wanted:
        row = by_ticker.get(ticker)
        if not row:
            print(f"WARNING: ticker not found in SEC company ticker file: {ticker}")
            continue
        cik = str(row["cik_str"]).zfill(10)
        time.sleep(0.15)
        submissions = get_json(SUBMISSIONS_URL.format(cik=cik))
        recent = submissions.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        filings = []
        for i, form in enumerate(forms):
            if form not in ("10-K", "10-Q", "8-K", "DEF 14A", "4", "S-1"):
                continue
            accession_raw = recent.get("accessionNumber", [""])[i]
            accession = accession_raw.replace("-", "")
            primary = recent.get("primaryDocument", [""])[i]
            filings.append({
                "form": form,
                "filing_date": recent.get("filingDate", [""])[i],
                "report_date": recent.get("reportDate", [""])[i],
                "description": recent.get("primaryDocDescription", [""])[i],
                "accession_number": accession_raw,
                "url": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/{quote(primary)}" if accession and primary else f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            })
            if len(filings) >= 12:
                break
        time.sleep(0.15)
        facts = get_json(FACTS_URL.format(cik=cik))
        metrics = {name: newest_fact(facts, names) for name, names in CONCEPTS.items()}
        companies.append({
            "ticker": ticker,
            "name": row.get("title", submissions.get("name", ticker)),
            "cik": cik,
            "sic": submissions.get("sic"),
            "sic_description": submissions.get("sicDescription"),
            "fiscal_year_end": submissions.get("fiscalYearEnd"),
            "website": submissions.get("website"),
            "sec_url": f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            "filings": filings,
            "metrics": metrics,
        })
        print(f"Refreshed {ticker} ({cik})")
    if not companies:
        raise SystemExit("No companies were refreshed; refusing to write an empty dataset.")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    data = {"generated_at": datetime.now(timezone.utc).isoformat(), "source": "U.S. SEC EDGAR public submissions and XBRL companyfacts", "companies": companies}
    (OUTPUT / "research.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(companies)} companies to {OUTPUT / 'research.json'}")

if __name__ == "__main__":
    main()
