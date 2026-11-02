#!/usr/bin/env python3
"""Derive cap growth, tax/cap ratio and apron gaps from the canonical Hoops cap table.

Input: glen-w/hoops main, data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv
(columns: season, salary_cap_usd, tax_level_usd, first_apron_usd, second_apron_usd, ...).

Usage: python3 -I cap_growth.py path/to/nba_salary_cap_apron_history.csv

Blank cells stay blank: a missing figure is never filled or estimated.
Output: markdown tables on stdout, every value labeled DERIVED from the input file.
"""
import csv
import sys

M = 1_000_000


def num(row, col):
    v = (row.get(col) or "").strip()
    return float(v) if v else None


def fmt_m(v):
    return "" if v is None else f"{v / M:.3f}"


def pct(new, old):
    if new is None or old is None:
        return ""
    return f"{(new / old - 1) * 100:.2f}%"


def ratio(a, b):
    if a is None or b is None:
        return ""
    return f"{a / b:.3f}"


def gap(a, b):
    if a is None or b is None:
        return ""
    return f"{(a - b) / M:.3f}"


def main(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = sorted(csv.DictReader(f), key=lambda r: r["season"])

    print("## Cap growth and tax/cap (DERIVED)\n")
    print("| season | cap $M | YoY cap | tax $M | tax/cap |")
    print("|---|---|---|---|---|")
    prev = None
    for r in rows:
        cap = num(r, "salary_cap_usd")
        tax = num(r, "tax_level_usd")
        print(f"| {r['season']} | {fmt_m(cap)} | {pct(cap, prev)} | {fmt_m(tax)} | {ratio(tax, cap)} |")
        prev = cap

    first, last = num(rows[0], "salary_cap_usd"), num(rows[-1], "salary_cap_usd")
    steps = len(rows) - 1
    if first and last and steps:
        cagr = (last / first) ** (1 / steps) - 1
        print(
            f"\n{rows[0]['season']} -> {rows[-1]['season']}: "
            f"cumulative {pct(last, first)}, CAGR {cagr * 100:.2f}% over {steps} steps\n"
        )

    print("## Apron gaps above tax line (DERIVED, $M)\n")
    print("| season | first apron - tax | second apron - tax |")
    print("|---|---|---|")
    for r in rows:
        tax = num(r, "tax_level_usd")
        a1, a2 = num(r, "first_apron_usd"), num(r, "second_apron_usd")
        if a1 is None and a2 is None:
            continue
        print(f"| {r['season']} | {gap(a1, tax)} | {gap(a2, tax)} |")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: cap_growth.py path/to/nba_salary_cap_apron_history.csv")
    main(sys.argv[1])
