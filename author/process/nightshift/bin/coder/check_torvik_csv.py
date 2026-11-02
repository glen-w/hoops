#!/usr/bin/env python3
"""Structural gate for Barttorvik team results CSVs (ds NVTWTCHG).

Checks barttorvik/{year}_team_results.csv for 2024 and 2025:
- file exists and is non-empty
- header present with at least one column
- at least one data row
Prints header + row count only. No statistics. Exits 1 on any failure.
Usage: python3 -I analysis/check_torvik_csv.py [--data-dir DIR] [--years 2024 2025]
Env: HOOPS_DATA_DIR overrides the data directory.
"""
import argparse
import csv
import os
import sys
from pathlib import Path

DEFAULT_YEARS = (2024, 2025)


def candidate_roots(data_dir):
    roots = []
    if data_dir:
        roots.append(Path(data_dir))
    env = os.environ.get("HOOPS_DATA_DIR")
    if env:
        roots.append(Path(env))
    roots += [Path("analysis/data"), Path("data"), Path(".")]
    seen = set()
    out = []
    for r in roots:
        key = str(r)
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def find_file(year, roots):
    name = f"{year}_team_results.csv"
    for root in roots:
        direct = root / name
        if direct.is_file():
            return direct
        nested = root / "barttorvik" / name
        if nested.is_file():
            return nested
    return None


def check(year, roots):
    path = find_file(year, roots)
    if path is None:
        print(f"{year}: MISSING (searched {', '.join(str(r) for r in roots)})")
        return 1
    try:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            rows = sum(1 for _ in reader)
    except (OSError, UnicodeError) as e:
        print(f"{year}: READ ERROR {e} ({path})")
        return 1
    if not header:
        print(f"{year}: EMPTY HEADER ({path})")
        return 1
    if rows < 1:
        print(f"{year}: NO DATA ROWS ({path})")
        return 1
    print(f"{year}: rows={rows} cols={len(header)} path={path}")
    print(f"  header: {header}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default=None)
    ap.add_argument("--years", nargs="*", type=int, default=list(DEFAULT_YEARS))
    args = ap.parse_args()
    roots = candidate_roots(args.data_dir)
    rc = 0
    for y in args.years:
        rc |= check(y, roots)
    sys.exit(rc)


if __name__ == "__main__":
    main()
