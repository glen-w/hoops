#!/usr/bin/env python3
"""
Generate average game statistics by decade from NBA season data.

Reads season-level league averages from data/reference/, aggregates by decade,
and writes derived table to data/derived/avg_game_by_decade.csv.

Source: Basketball-Reference.com league averages (via data/reference/nba_league_averages_by_season.csv)
License: Public NBA statistics, freely redistributable with attribution
No Kaggle credentials or API calls required.

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
    """
    Aggregate season-level stats by decade.
    
    Returns DataFrame with decade-level averages.
    """
    # Columns to aggregate
    stat_cols = [col for col in season_df.columns 
                 if col not in ['season', 'season_start_year', 'decade']]
    
    # Group by decade and calculate mean
    decade_df = season_df.groupby('decade')[stat_cols].mean().reset_index()
    
    # Round for readability
    for col in stat_cols:
        if col.endswith('_pct'):
            decade_df[col] = decade_df[col].round(3)
        else:
            decade_df[col] = decade_df[col].round(1)
    
    # Add decade label
    decade_df['decade_label'] = decade_df['decade'].apply(lambda d: f"{d}s")
    
    # Reorder columns: decade, decade_label, then all stats
    cols = ['decade', 'decade_label'] + stat_cols
    decade_df = decade_df[cols]
    
    return decade_df


def main():
    """Main pipeline: load → aggregate → write."""
    
    print("=== NBA Average Game by Decade Builder ===\n")
    
    # Load source data
    print("Step 1: Load season-level source data")
    season_df = load_season_data()
    print(f"✓ Loaded {len(season_df)} seasons ({season_df['season'].iloc[0]} to {season_df['season'].iloc[-1]})")
    
    # Aggregate by decade
    print("\nStep 2: Aggregate by decade")
    decade_df = aggregate_by_decade(season_df)
    print(f"✓ Aggregated into {len(decade_df)} decades")
    print("\nDecade summary:")
    print(decade_df[['decade_label', 'fga', 'fg_pct', 'fg3a', 'pts']].to_string(index=False))
    
    # Write output
    print("\nStep 3: Write derived table")
    output_dir = Path('data/derived')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / 'avg_game_by_decade.csv'
    decade_df.to_csv(output_path, index=False, float_format='%.3f')
    print(f"✓ Wrote {output_path}")
    
    print("\n✅ Done! The derived table is ready for use in the manuscript.")
    print(f"   View: cat {output_path}")


if __name__ == '__main__':
    main()
