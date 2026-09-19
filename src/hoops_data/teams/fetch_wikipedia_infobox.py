#!/usr/bin/env python3
"""
Fetch Wikipedia infobox data for gap-filling.

STUB: Placeholder for Wikipedia API integration to extract infobox
data (colors, arena capacity, ownership) when Wikidata is incomplete.

Future implementation will use MediaWiki API action=parse to extract
infobox templates and parse structured fields.

Usage:
    uv run python -m hoops_data.teams.fetch_wikipedia_infobox
"""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Wikipedia infobox data (STUB)"
    )
    parser.add_argument(
        "--teams-csv",
        type=Path,
        default=Path("data/derived/teams/teams.csv"),
        help="Path to teams.csv",
    )
    
    args = parser.parse_args()
    
    print("Wikipedia infobox gap-filling is not yet implemented.")
    print("Future implementation will:")
    print("  - Query MediaWiki API for each team's Wikipedia article")
    print("  - Extract infobox template fields")
    print("  - Fill gaps in colours, arena_capacity, owner fields")
    print("  - Update teams.csv with confidence=MEDIUM for wiki-sourced data")
    
    return 0


if __name__ == "__main__":
    exit(main())
