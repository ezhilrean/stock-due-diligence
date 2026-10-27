"""SEC EDGAR MCP server for Stock Due Diligence.

Public SEC endpoints only; no API key is required. Set SEC_USER_AGENT to a
descriptive contact string such as "StockDueDiligence contact@example.com".
"""
from __future__ import annotations

import json
import os
import re
import time
from typing import Any
from urllib.parse import quote

import httpx
from mcp.server.fastmcp import FastMCP

APP_NAME = "Stock Due Diligence — SEC EDGAR"
SEC_USER_AGENT = os.environ.get("SEC_USER_AGENT", "").strip()
if not SEC_USER_AGENT:
    raise RuntimeError(
        "Set SEC_USER_AGENT to a descriptive app name and contact email before starting."
    )

mcp = FastMCP(
    APP_NAME,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "8000")),
)

TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
TIMEOUT = httpx.Timeout(20.0, connect=10.0)
_HEADERS = {
    "User-Agent": SEC_USER_AGENT,
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
}
_cache: dict[str, tuple[float, Any]] = {}
_CACHE_SECONDS = 300


def _get_json(url: str) -> Any:
    now = time.time()
    cached = _cache.get(url)
    if cached and now - cached[0] < _CACHE_SECONDS:
        return cached[1]
    with httpx.Client(headers=_HEADERS, timeout=TIMEOUT, follow_redirects=True) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
    _cache[url] = (now, data)
    return data


def _json_result(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _normalize_ticker(value: str) -> str:
    return value.strip().upper().replace(".", "-")


def _find_company(query: str) -> dict[str, Any]:
    q = query.strip().casefold()
    if not q:
        raise ValueError("Enter a company name or ticker.")
    entries = _get_json(TICKERS_URL)
    rows = entries.values() if isinstance(entries, dict) else []
    candidates = []
    for row in rows:
        ticker = str(row.get("ticker", "")).upper()
        title = str(row.get("title", ""))
        if ticker.casefold() == q or title.casefold() == q:
            candidates.insert(0, row)
        elif q in ticker.casefold() or q in title.casefold():
            candidates.append(row)
    # Exact matches first, then stable alphabetical partial matches.
    seen = set()
    out = []
    for row in candidates:
        cik = str(row.get("cik_str", "")).zfill(10)
        if cik and cik not in seen:
            seen.add(cik)
            out.append({
                "company_name": row.get("title"),
                "ticker": row.get("ticker"),
                "cik": cik,
                "sec_company_page": f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            })
        if len(out) >= 10:
            break
    return {"query": query, "matches": out, "source": TICKERS_URL}


def _resolve_cik(ticker_or_cik: str) -> tuple[str, dict[str, Any] | None]:
    value = ticker_or_cik.strip()
    if not value:
        raise ValueError("Enter a stock ticker or SEC CIK.")
    digits = re.sub(r"^CIK", "", value, flags=re.IGNORECASE)
    if digits.isdigit():
        return digits.zfill(10), None
    matches = _find_company(value)["matches"]
    exact = [m for m in matches if str(m.get("ticker", "")).upper() == _normalize_ticker(value)]
    selected = exact[0] if exact else (matches[0] if len(matches) == 1 else None)
    if selected is None:
        raise ValueError(
            "Ticker could not be resolved unambiguously. Use sec_search_company first, "
            "then call this tool with the exact SEC CIK."
        )
    return selected["cik"], selected


@mcp.tool()
def sec_search_company(query: str) -> str:
    """Find SEC-listed companies by ticker or company name. Returns candidate CIKs and SEC links."""
    try:
        return _json_result(_find_company(query))
    except httpx.HTTPError as exc:
        return _json_result({"error": "SEC request failed", "detail": str(exc), "retryable": True})


@mcp.tool()
def sec_get_recent_filings(ticker_or_cik: str, form_types: str = "10-K,10-Q,8-K,DEF 14A,4,S-1") -> str:
    """Retrieve recent SEC filing metadata for a ticker or CIK. form_types is a comma-separated list."""
    try:
        cik, company = _resolve_cik(ticker_or_cik)
        data = _get_json(SUBMISSIONS_URL.format(cik=cik))
        recent = data.get("filings", {}).get("recent", {})
        allowed = {x.strip().upper() for x in form_types.split(",") if x.strip()}
        forms = recent.get("form", [])
        rows = []
        for i, form in enumerate(forms):
            if form.upper() not in allowed:
                continue
            accession = recent.get("accessionNumber", [""])[i].replace("-", "")
            primary = recent.get("primaryDocument", [""])[i]
            rows.append({
                "form": form,
                "filing_date": recent.get("filingDate", [""])[i],
                "report_date": recent.get("reportDate", [""])[i],
                "accession_number": recent.get("accessionNumber", [""])[i],
                "description": recent.get("primaryDocDescription", [""])[i],
                "filing_url": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/{quote(primary)}" if accession and primary else None,
            })
            if len(rows) >= 30:
                break
        return _json_result({
            "company": company or {"cik": cik, "name": data.get("name")},
            "cik": cik,
            "filings": rows,
            "source": f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            "note": "Filing metadata is from SEC submissions data; read the linked filing before drawing conclusions.",
        })
    except (ValueError, httpx.HTTPError, KeyError, IndexError) as exc:
        return _json_result({"error": "Unable to retrieve filings", "detail": str(exc)})


@mcp.tool()
def sec_get_company_facts(ticker_or_cik: str, metric_names: str = "Revenue,NetIncome,CashAndCashEquivalentsAtCarryingValue,LongTermDebtCurrent,LongTermDebtNoncurrent,Assets,StockholdersEquity") -> str:
    """Retrieve selected XBRL financial facts reported to the SEC. metric_names accepts comma-separated standard US-GAAP concept names."""
    try:
        cik, company = _resolve_cik(ticker_or_cik)
        data = _get_json(FACTS_URL.format(cik=cik))
        usgaap = data.get("facts", {}).get("us-gaap", {})
        wanted = [x.strip() for x in metric_names.split(",") if x.strip()]
        results = []
        for requested in wanted:
            # Match exact concept first; otherwise a case-insensitive concept-name match.
            concept = usgaap.get(requested)
            concept_name = requested
            if concept is None:
                match = next(
                    ((k, v) for k, v in usgaap.items() if k.casefold() == requested.casefold()),
                    None,
                )
                if match:
                    concept_name, concept = match
            if not concept:
                results.append({"requested_metric": requested, "status": "not_found_in_companyfacts"})
                continue
            units = concept.get("units", {})
            unit_results = []
            for unit, observations in units.items():
                # Prefer annual 10-K observations and latest fiscal years; avoid pretending
                # quarterly and annual values are directly comparable.
                annual = [
                    o for o in observations
                    if o.get("form") == "10-K" and o.get("filed") and o.get("fy") is not None
                ]
                annual.sort(key=lambda o: (str(o.get("end", "")), str(o.get("filed", ""))), reverse=True)
                dedup, seen = [], set()
                for obs in annual:
                    key = (obs.get("fy"), obs.get("fp"), obs.get("end"))
                    if key in seen:
                        continue
                    seen.add(key)
                    dedup.append({
                        "fiscal_year": obs.get("fy"),
                        "fiscal_period": obs.get("fp"),
                        "period_end": obs.get("end"),
                        "filed": obs.get("filed"),
                        "form": obs.get("form"),
                        "value": obs.get("val"),
                        "unit": unit,
                        "accession_number": obs.get("accn"),
                    })
                    if len(dedup) >= 5:
                        break
                if dedup:
                    unit_results.append({"unit": unit, "annual_observations": dedup})
            results.append({
                "requested_metric": requested,
                "concept": concept_name,
                "label": concept.get("label"),
                "description": concept.get("description"),
                "data": unit_results,
            })
        return _json_result({
            "company": company or {"cik": cik, "name": data.get("entityName")},
            "cik": cik,
            "facts": results,
            "source": f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",
            "filing_search": f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            "limitations": [
                "Values are company-reported XBRL facts, not independently audited by this tool.",
                "Metric concepts and reporting units differ across issuers; verify the source filing and concept.",
                "Absence of a requested concept does not mean the company has no such item.",
                "Market prices, enterprise value, valuation multiples, and forward estimates are not provided.",
            ],
        })
    except (ValueError, httpx.HTTPError, KeyError, IndexError) as exc:
        return _json_result({"error": "Unable to retrieve company facts", "detail": str(exc)})


@mcp.tool()
def sec_get_company_profile(ticker_or_cik: str) -> str:
    """Get the SEC submissions profile and official company identifiers for a ticker or CIK."""
    try:
        cik, company = _resolve_cik(ticker_or_cik)
        data = _get_json(SUBMISSIONS_URL.format(cik=cik))
        addresses = data.get("addresses", {})
        business = addresses.get("business", {})
        mailing = addresses.get("mailing", {})
        return _json_result({
            "company": company or {"cik": cik, "name": data.get("name")},
            "cik": cik,
            "name": data.get("name"),
            "entity_type": data.get("entityType"),
            "sic": data.get("sic"),
            "sic_description": data.get("sicDescription"),
            "fiscal_year_end": data.get("fiscalYearEnd"),
            "state_of_incorporation": data.get("stateOfIncorporation"),
            "business_address": business,
            "mailing_address": mailing,
            "website": f"https://www.sec.gov/edgar/browse/?CIK={cik}",
            "source": f"https://data.sec.gov/submissions/CIK{cik}.json",
        })
    except (ValueError, httpx.HTTPError, KeyError) as exc:
        return _json_result({"error": "Unable to retrieve company profile", "detail": str(exc)})


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
