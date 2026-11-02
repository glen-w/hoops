#!/usr/bin/env python3
"""Per-decade average of one stat column, computed two ways.

Usage: decade_compare.py SEASON_CSV SEASON_COL GAMES_COL STAT_COL

SEASON_COL holds the ending year (e.g. 1985 or 1984-85). STAT_COL is a per-game
value. Prints CSV: decade,seasons,mean_of_means,games_weighted.
No data is bundled; all numbers come from the input file.
"""
import csv
import sys
from collections import defaultdict


def season_year(s):
    s = s.strip()
    if "-" in s:
        start, end = s.split("-", 1)
        century = int(start[:2]) * 100
        year = century + int(end[-2:])
        return year + 100 if year < int(start) else year
    return int(s)


def main(path, season_col, games_col, stat_col):
    by_dec = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                y = season_year(row[season_col])
                g = float(row[games_col])
                v = float(row[stat_col])
            except (KeyError, ValueError):
                continue
            by_dec[y // 10 * 10].append((g, v))
    print("decade,seasons,mean_of_means,games_weighted")
    for dec in sorted(by_dec):
        rows = by_dec[dec]
        n = len(rows)
        mom = sum(v for _, v in rows) / n
        tg = sum(g for g, _ in rows)
        gw = sum(g * v for g, v in rows) / tg if tg else float("nan")
        print(f"{dec}s,{n},{mom:.4f},{gw:.4f}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])
