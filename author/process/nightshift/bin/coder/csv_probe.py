#!/usr/bin/env python3
"""Probe a B-Ref season CSV before decade_compare.py. Reports facts only.

Usage: python3 -I csv_probe.py PATH [--expect COL ...]
Exit 1 if any --expect column is missing. Compare the header with decade_csv_spec.md.
"""
import argparse
import csv
import sys


def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path")
    ap.add_argument("--expect", nargs="*", default=[])
    a = ap.parse_args()

    with open(a.path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("empty csv")

    cols = list(rows[0].keys())
    print(f"rows: {len(rows)}")
    print(f"cols: {cols}")
    for c in cols:
        vals = [r[c] for r in rows if r[c] not in ("", None)]
        kind = "numeric" if vals and all(is_num(v) for v in vals) else "text"
        print(f"  {c}: {kind}, blank={len(rows) - len(vals)}")

    missing = [c for c in a.expect if c not in cols]
    if missing:
        print(f"MISSING: {missing}")
        sys.exit(1)


if __name__ == "__main__":
    main()
