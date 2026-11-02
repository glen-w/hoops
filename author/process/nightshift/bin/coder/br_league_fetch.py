"""Fetch Basketball-Reference NBA league per-game table (WNKIH56T) to CSV.

Source: https://www.basketball-reference.com/leagues/NBA_stats_per_game.html
Run: python3 -I analysis/br_league_fetch.py analysis/out/br_league_per_game.csv
Writes the CSV plus a .access sidecar holding URL and UTC access date for citation.
Politeness: one request, custom UA. Do not redistribute raw dump; cite only.
"""
import sys
import datetime
import urllib.request
from io import StringIO
from pathlib import Path

import pandas as pd

URL = "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"


def main(out_path):
    req = urllib.request.Request(URL, headers={"User-Agent": "hoops-book-research/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read().decode("utf-8")
    tables = pd.read_html(StringIO(html))
    if not tables:
        raise SystemExit("no tables parsed; page layout changed or blocked")
    df = tables[0]
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(-1)
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    out.with_suffix(".access").write_text(f"{URL}\naccessed {stamp} UTC\n")
    print(f"rows={len(df)} cols={list(df.columns)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: br_league_fetch.py OUT.csv")
    main(sys.argv[1])
