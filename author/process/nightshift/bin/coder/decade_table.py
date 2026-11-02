#!/usr/bin/env python3
"""Per-decade means from a season-level CSV.

No data is bundled. Supply a CSV exported from Basketball-Reference season rows.
Column names are arguments, so nothing is assumed about the file's schema.

Usage:
  python3 -I decade_table.py seasons.csv --season-col Season --cols PTS,FGA

--season-col holds a year (e.g. 1987) or a string like 1986-87. For the
string form the ending year is used. Rows with non-numeric values are
skipped and counted.
"""
import argparse
import csv
import sys
from collections import defaultdict


def season_year(raw):
    raw = raw.strip()
    if "-" in raw:
        start, end = raw.split("-", 1)
        century = int(start) // 100 * 100
        year = century + int(end)
        return year + 100 if year < int(start) else year
    return int(raw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--season-col", required=True)
    ap.add_argument("--cols", required=True, help="comma-separated numeric columns")
    args = ap.parse_args()
    cols = [c.strip() for c in args.cols.split(",") if c.strip()]

    sums = defaultdict(lambda: defaultdict(float))
    counts = defaultdict(lambda: defaultdict(int))
    skipped = 0
    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in [args.season_col, *cols] if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"missing columns: {missing}; have: {reader.fieldnames}")
        for row in reader:
            try:
                decade = season_year(row[args.season_col]) // 10 * 10
            except ValueError:
                skipped += 1
                continue
            for c in cols:
                try:
                    v = float(row[c])
                except ValueError:
                    skipped += 1
                    continue
                sums[decade][c] += v
                counts[decade][c] += 1

    print("decade," + ",".join(f"{c}_mean,{c}_n" for c in cols))
    for d in sorted(sums):
        cells = []
        for c in cols:
            n = counts[d][c]
            cells += [f"{sums[d][c] / n:.3f}" if n else "", str(n)]
        print(f"{d}s," + ",".join(cells))
    if skipped:
        print(f"# skipped {skipped} unparseable cells", file=sys.stderr)


if __name__ == "__main__":
    main()
