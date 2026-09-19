#!/usr/bin/env python3
"""
Enrich teams with official colors from Wikidata P465.

Queries Wikidata for P465 (official color) property and extracts
hex values where available. Updates teams.csv with official colors only.

Usage:
    python3 -m hoops_data.teams.enrich_colors
"""

import argparse
import time
from pathlib import Path

import pandas as pd
from SPARQLWrapper import JSON, SPARQLWrapper


def get_sparql_endpoint() -> SPARQLWrapper:
    """Initialize Wikidata SPARQL endpoint with polite User-Agent."""
    endpoint = SPARQLWrapper("https://query.wikidata.org/sparql")
    endpoint.setReturnFormat(JSON)
    endpoint.addCustomHttpHeader(
        "User-Agent",
        "hoops-data/0.1 (glen-w/hoops basketball teams; research; [email protected])",
    )
    return endpoint


def build_colors_query(team_qid: str) -> str:
    """
    Build SPARQL query for team colors.
    
    Queries P465 (official color) with P462 (color) fallback.
    Extracts hex codes when available.
    """
    return f"""
    SELECT DISTINCT ?color ?colorLabel ?hexCode
    WHERE {{
      # Primary: P465 (official color)
      {{
        wd:{team_qid} wdt:P465 ?color .
      }}
      UNION
      {{
        # Fallback: P462 (color)
        wd:{team_qid} wdt:P462 ?color .
      }}
      
      # Try to get hex code (P465 qualifier or direct property)
      OPTIONAL {{
        wd:{team_qid} p:P465 ?statement .
        ?statement ps:P465 ?color .
        ?statement pq:P462 ?hexCodeEntity .
        ?hexCodeEntity wdt:P465 ?hexCode .
      }}
      
      # Or direct on color entity
      OPTIONAL {{
        ?color wdt:P465 ?hexCode .
      }}
      
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}
    LIMIT 5
    """


def extract_colors_for_team(team_qid: str) -> dict[str, str | None]:
    """
    Fetch official colors for a team from Wikidata.
    
    Returns dict with primary_hex, secondary_hex, accent_hex, source.
    """
    endpoint = get_sparql_endpoint()
    query = build_colors_query(team_qid)
    endpoint.setQuery(query)
    
    try:
        results = endpoint.query().convert()
        bindings = results.get("results", {}).get("bindings", [])
        
        hex_codes = []
        color_labels = []
        
        for binding in bindings:
            hex_code = binding.get("hexCode", {}).get("value")
            color_label = binding.get("colorLabel", {}).get("value")
            
            if hex_code:
                # Ensure proper format
                if not hex_code.startswith("#"):
                    hex_code = f"#{hex_code}"
                hex_codes.append(hex_code.upper())
                color_labels.append(color_label)
        
        # Deduplicate
        hex_codes = list(dict.fromkeys(hex_codes))
        
        if not hex_codes:
            return {
                "colours_primary_hex": None,
                "colours_secondary_hex": None,
                "colours_accent_hex": None,
                "colours_source": None,
            }
        
        return {
            "colours_primary_hex": hex_codes[0] if len(hex_codes) > 0 else None,
            "colours_secondary_hex": hex_codes[1] if len(hex_codes) > 1 else None,
            "colours_accent_hex": hex_codes[2] if len(hex_codes) > 2 else None,
            "colours_source": "wikidata" if hex_codes else None,
        }
        
    except Exception as e:
        print(f"  ✗ Error fetching colors for {team_qid}: {e}")
        return {
            "colours_primary_hex": None,
            "colours_secondary_hex": None,
            "colours_accent_hex": None,
            "colours_source": None,
        }


def enrich_teams_with_colors(
    teams_csv: Path,
    rate_limit: float = 2.0,
) -> tuple[int, int]:
    """
    Enrich teams.csv with official colors from Wikidata.
    
    Returns (enriched_count, total_count).
    """
    df = pd.read_csv(teams_csv)
    enriched_count = 0
    
    for idx, row in df.iterrows():
        team_qid = row["wikidata_qid"]
        team_name = row["name"]
        
        # Skip if already has colors
        if pd.notna(row["colours_primary_hex"]):
            print(f"  ⊙ {team_name}: Colors already present, skipping")
            continue
        
        print(f"  Fetching colors for {team_name} ({team_qid})...")
        
        colors = extract_colors_for_team(team_qid)
        
        if colors["colours_primary_hex"]:
            df.at[idx, "colours_primary_hex"] = colors["colours_primary_hex"]
            df.at[idx, "colours_secondary_hex"] = colors["colours_secondary_hex"]
            df.at[idx, "colours_accent_hex"] = colors["colours_accent_hex"]
            df.at[idx, "colours_source"] = colors["colours_source"]
            enriched_count += 1
            print(f"    ✓ Found colors: {colors['colours_primary_hex']}")
        else:
            print(f"    ○ No colors found (leaving blank)")
        
        # Rate limiting
        time.sleep(rate_limit)
    
    # Save back
    df.to_csv(teams_csv, index=False)
    
    return enriched_count, len(df)


def main():
    parser = argparse.ArgumentParser(
        description="Enrich teams with official colors from Wikidata P465"
    )
    parser.add_argument(
        "--teams-csv",
        type=Path,
        default=Path("data/derived/teams/teams.csv"),
        help="Path to teams.csv",
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=2.0,
        help="Seconds to wait between requests (default: 2s)",
    )
    
    args = parser.parse_args()
    
    if not args.teams_csv.exists():
        print(f"Error: {args.teams_csv} not found")
        return 1
    
    print(f"Enriching teams with official colors from Wikidata...")
    print(f"Rate limit: {args.rate_limit}s between requests")
    
    enriched, total = enrich_teams_with_colors(args.teams_csv, args.rate_limit)
    
    print(f"\n✓ Complete: Enriched {enriched}/{total} teams with colors")
    print(f"  Fill rate: {enriched/total*100:.1f}%")
    
    return 0


if __name__ == "__main__":
    exit(main())
