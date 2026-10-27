#!/usr/bin/env python3
"""Validate and normalize figures transcribed from official Indian exchange filings.

The input CSV must contain source URLs and period/basis metadata. This tool deliberately
does not scrape NSE/BSE pages or invent values; use it after reviewing an official filing.
"""
from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "data" / "india-results.json"
FIELDS = [
    "symbol", "company_name", "period_end", "period_type", "basis", "units",
    "revenue", "operating_profit", "profit_after_tax", "eps", "total_assets",
    "total_debt", "cash_and_equivalents", "operating_cash_flow",
    "filing_date", "source_title", "source_url",
]
NUMERIC = {
    "revenue", "operating_profit", "profit_after_tax", "eps", "total_assets",
    "total_debt", "cash_and_equivalents", "operating_cash_flow",
}
ALLOWED_BASIS = {"consolidated", "standalone"}
ALLOWED_PERIOD = {"quarterly", "annual", "half-yearly", "nine-month"}
ALLOWED_SCHEMES = {"https"}

def clean_number(value: str, field: str, row_num: int):
    value = (value or "").strip()
    if not value:
        return None
    value = value.replace(",", "")
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError(f"Row {row_num}: {field} must be numeric, got {value!r}") from exc
    if number != number or abs(number) == float("inf"):
        raise ValueError(f"Row {row_num}: {field} must be a finite number")
    return number

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/import_india_results.py path/to/india-results.csv", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"Input CSV not found: {input_path}", file=sys.stderr)
        return 2

    normalized = []
    seen = set()
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            print("CSV is missing required columns: " + ", ".join(missing), file=sys.stderr)
            return 2
        for row_num, raw in enumerate(reader, start=2):
            row = {key: (raw.get(key) or "").strip() for key in FIELDS}
            if not any(row.values()):
                continue
            for required in ("symbol", "company_name", "period_end", "period_type", "basis", "units", "source_title", "source_url"):
                if not row[required]:
                    raise ValueError(f"Row {row_num}: {required} is required")
            row["symbol"] = row["symbol"].upper()
            row["period_type"] = row["period_type"].lower()
            row["basis"] = row["basis"].lower()
            if row["basis"] not in ALLOWED_BASIS:
                raise ValueError(f"Row {row_num}: basis must be consolidated or standalone")
            if row["period_type"] not in ALLOWED_PERIOD:
                raise ValueError(f"Row {row_num}: period_type must be one of {', '.join(sorted(ALLOWED_PERIOD))}")
            try:
                datetime.strptime(row["period_end"], "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError(f"Row {row_num}: period_end must use YYYY-MM-DD") from exc
            if row["filing_date"]:
                try:
                    datetime.strptime(row["filing_date"], "%Y-%m-%d")
                except ValueError as exc:
                    raise ValueError(f"Row {row_num}: filing_date must use YYYY-MM-DD") from exc
            parsed_url = urlparse(row["source_url"])
            if parsed_url.scheme not in ALLOWED_SCHEMES or not parsed_url.netloc:
                raise ValueError(f"Row {row_num}: source_url must be a full HTTPS URL")
            key = (row["symbol"], row["period_end"], row["basis"], row["period_type"])
            if key in seen:
                raise ValueError(f"Row {row_num}: duplicate symbol/period/basis/period_type: {key}")
            seen.add(key)
            item = {key: row[key] for key in ("symbol", "company_name", "period_end", "period_type", "basis", "units", "filing_date", "source_title", "source_url")}
            item.update({field: clean_number(row[field], field, row_num) for field in NUMERIC})
            normalized.append(item)

    normalized.sort(key=lambda item: (item["symbol"], item["period_end"], item["basis"], item["period_type"]), reverse=False)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_policy": "Values entered from reviewed official exchange filings; source URL and period metadata required.",
        "record_count": len(normalized),
        "results": normalized,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(normalized)} normalized result records to {OUTPUT.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"Import failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
