#!/usr/bin/env python3
"""Fetch Barttorvik T-Rank season-end team results CSVs (ds NVTWTCHG, 7FHGENDV).

Source: https://barttorvik.com/ (season-end CSVs named {year}_team_results.csv).
Writes barttorvik/{year}_team_results.csv plus a .access sidecar (URL + UTC date).
Fetch only; no stats computed. Verify ToS before redistributing.
Usage: python3 -I analysis/fetch_torvik_csv.py [YEAR ...] [--out-dir DIR]
Default years: 2024 2025
"""
import argparse
import datetime
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://barttorvik.com"
DEFAULT_YEARS = (2024, 2025)


def fetch(year, out_dir):
    url = f"{BASE}/{year}_team_results.csv"
    req = urllib.request.Request(url, headers={"User-Agent": "hoops-book-research/1.0"})
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{year}_team_results.csv"
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        print(f"year={year} HTTP {e.code}: {url}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"year={year} URL error: {e}", file=sys.stderr)
        return 1
    if not data.strip():
        print(f"year={year} empty response: {url}", file=sys.stderr)
        return 1
    dest.write_bytes(data)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    dest.with_suffix(".access").write_text(f"{url}\naccessed {stamp} UTC\n")
    lines = data.decode("utf-8", errors="replace").splitlines()
    print(f"year={year} rows~={max(len(lines) - 1, 0)} bytes={len(data)} -> {dest}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("years", nargs="*", type=int, default=list(DEFAULT_YEARS))
    ap.add_argument("--out-dir", default="analysis/data/barttorvik")
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    rc = 0
    for y in args.years:
        rc |= fetch(y, out_dir)
    sys.exit(rc)


if __name__ == "__main__":
    main()
