#!/usr/bin/env python3
"""
Legacy rebuild helper for average-game-by-decade.

Canonical artifact (cite this):
  data/derived/avg_game_by_decade/
    - avg_game_by_decade.csv
    - nba_league_averages_by_season.csv
    - sample_seasons_landmarks.csv
    - methodology.md

This script still aggregates the older committed reference file
`data/reference/nba_league_averages_by_season.csv` for comparison only.
It writes beside the pack as `avg_game_by_decade_from_reference.csv` and
does **not** overwrite the cite-backed pack CSV (schemas differ; see
pack methodology).

Usage:
    uv run python scripts/build_avg_game_by_decade.py
"""

import sys
from pathlib import Path
import pandas as pd


def load_season_data() -> pd.DataFrame:
    """Load season-level league averages from committed source CSV."""
    source_path = Path('data/reference/nba_league_averages_by_season.csv')

    if not source_path.exists():
        print(f"Error: Source data not found at {source_path}", file=sys.stderr)
        print("Expected season-level league averages CSV.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(source_path)

    # Extract start year from season string (e.g., "1985-86" → 1985)
    df['season_start_year'] = df['season'].str.split('-').str[0].astype(int)

    # Assign decade (e.g., 1985 → 1980s)
    df['decade'] = (df['season_start_year'] // 10) * 10

    return df


def aggregate_by_decade(season_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate season-level stats by decade."""
    stat_cols = [
        col for col in season_df.columns
        if col not in ['season', 'season_start_year', 'decade']
    ]

    decade_df = season_df.groupby('decade')[stat_cols].mean().reset_index()

    for col in stat_cols:
        if col.endswith('_pct'):
            decade_df[col] = decade_df[col].round(3)
        else:
            decade_df[col] = decade_df[col].round(1)

    decade_df['decade_label'] = decade_df['decade'].apply(lambda d: f"{d}s")
    cols = ['decade', 'decade_label'] + stat_cols
    return decade_df[cols]


def main():
    print("=== NBA Average Game by Decade (reference rebuild) ===\n")
    print("Cite the pack under data/derived/avg_game_by_decade/ — not this rebuild.\n")

    print("Step 1: Load season-level source data")
    season_df = load_season_data()
    print(
        f"✓ Loaded {len(season_df)} seasons "
        f"({season_df['season'].iloc[0]} to {season_df['season'].iloc[-1]})"
    )

    print("\nStep 2: Aggregate by decade")
    decade_df = aggregate_by_decade(season_df)
    print(f"✓ Aggregated into {len(decade_df)} decades")
    print("\nDecade summary:")
    print(decade_df[['decade_label', 'fga', 'fg_pct', 'fg3a', 'pts']].to_string(index=False))

    print("\nStep 3: Write comparison rebuild (does not overwrite pack CSV)")
    output_dir = Path('data/derived/avg_game_by_decade')
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / 'avg_game_by_decade_from_reference.csv'
    decade_df.to_csv(output_path, index=False, float_format='%.3f')
    print(f"✓ Wrote {output_path}")
    print("   Canonical cite path: data/derived/avg_game_by_decade/avg_game_by_decade.csv")


if __name__ == '__main__':
    main()
