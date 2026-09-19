#!/usr/bin/env python3
"""
Fetch basketball team data from Wikidata via SPARQL.

Queries Wikidata for teams in specified leagues and writes
raw JSONL to data/raw/wikidata/.

Usage:
    uv run python -m hoops_data.teams.fetch_wikidata_teams --league nba
    uv run python -m hoops_data.teams.fetch_wikidata_teams --league wnba
    uv run python -m hoops_data.teams.fetch_wikidata_teams --all-active
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from SPARQLWrapper import JSON, SPARQLWrapper


def get_sparql_endpoint() -> SPARQLWrapper:
    """Initialize Wikidata SPARQL endpoint."""
    endpoint = SPARQLWrapper("https://query.wikidata.org/sparql")
    endpoint.setReturnFormat(JSON)
    endpoint.addCustomHttpHeader(
        "User-Agent",
        "hoops-data/0.1 (glen-w/hoops basketball teams desk; research project)",
    )
    return endpoint


def build_teams_query(league_qid: str) -> str:
    """
    Build SPARQL query for teams in a given league.
    
    Retrieves:
    - Team QID, label, Wikipedia title
    - Home venue (P115), headquarters location (P159)
    - Country (P17)
    - Logo image (P154)
    - Official color (P462)
    - Owner (P127)
    - Inception (P571)
    
    Uses flexible matching: P118 (league) OR P463 (member of) OR P361 (part of)
    """
    return f"""
    SELECT DISTINCT ?team ?teamLabel ?country ?countryLabel 
           ?venue ?venueLabel ?venueCapacity
           ?hq ?hqLabel ?logo ?color ?colorLabel 
           ?owner ?ownerLabel ?inception ?mascot ?mascotLabel
           ?officialWebsite ?wikipediaEn
    WHERE {{
      # Teams that participate in, are members of, or are part of the league
      {{
        ?team wdt:P118 wd:{league_qid} .
      }}
      UNION
      {{
        ?team wdt:P463 wd:{league_qid} .
      }}
      UNION
      {{
        ?team wdt:P361 wd:{league_qid} .
      }}
      
      # Must be a basketball team or sports club
      {{ ?team wdt:P31 wd:Q476028 . }}  # basketball team
      UNION
      {{ ?team wdt:P31 wd:Q4498974 . }}  # sports club
      
      # Optional: country
      OPTIONAL {{ ?team wdt:P17 ?country . }}
      
      # Optional: home venue
      OPTIONAL {{ 
        ?team wdt:P115 ?venue .
        OPTIONAL {{ ?venue wdt:P1083 ?venueCapacity . }}
      }}
      
      # Optional: headquarters location (city)
      OPTIONAL {{ ?team wdt:P159 ?hq . }}
      
      # Optional: logo
      OPTIONAL {{ ?team wdt:P154 ?logo . }}
      
      # Optional: official color
      OPTIONAL {{ ?team wdt:P462 ?color . }}
      
      # Optional: owner
      OPTIONAL {{ ?team wdt:P127 ?owner . }}
      
      # Optional: inception date
      OPTIONAL {{ ?team wdt:P571 ?inception . }}
      
      # Optional: mascot
      OPTIONAL {{ ?team wdt:P822 ?mascot . }}
      
      # Optional: official website
      OPTIONAL {{ ?team wdt:P856 ?officialWebsite . }}
      
      # Optional: English Wikipedia article
      OPTIONAL {{
        ?wikipediaEn schema:about ?team .
        ?wikipediaEn schema:isPartOf <https://en.wikipedia.org/> .
      }}
      
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}
    ORDER BY ?teamLabel
    """


def fetch_teams_for_league(league_id: str, league_qid: str) -> list[dict[str, Any]]:
    """
    Fetch all teams for a given league from Wikidata.
    
    Args:
        league_id: Internal league identifier (e.g., 'nba')
        league_qid: Wikidata QID for the league (e.g., 'Q155223')
        
    Returns:
        List of team data dictionaries
    """
    print(f"Fetching teams for {league_id} (Wikidata {league_qid})...")
    
    endpoint = get_sparql_endpoint()
    query = build_teams_query(league_qid)
    endpoint.setQuery(query)
    
    try:
        results = endpoint.query().convert()
        bindings = results.get("results", {}).get("bindings", [])
        
        teams = []
        for binding in bindings:
            team_data = {
                "team_qid": binding["team"]["value"].split("/")[-1],
                "team_label": binding.get("teamLabel", {}).get("value"),
                "country_qid": binding.get("country", {}).get("value", "").split("/")[-1] or None,
                "country_label": binding.get("countryLabel", {}).get("value"),
                "venue_qid": binding.get("venue", {}).get("value", "").split("/")[-1] or None,
                "venue_label": binding.get("venueLabel", {}).get("value"),
                "venue_capacity": binding.get("venueCapacity", {}).get("value"),
                "hq_qid": binding.get("hq", {}).get("value", "").split("/")[-1] or None,
                "hq_label": binding.get("hqLabel", {}).get("value"),
                "logo_url": binding.get("logo", {}).get("value"),
                "color_qid": binding.get("color", {}).get("value", "").split("/")[-1] or None,
                "color_label": binding.get("colorLabel", {}).get("value"),
                "owner_qid": binding.get("owner", {}).get("value", "").split("/")[-1] or None,
                "owner_label": binding.get("ownerLabel", {}).get("value"),
                "inception": binding.get("inception", {}).get("value"),
                "mascot_qid": binding.get("mascot", {}).get("value", "").split("/")[-1] or None,
                "mascot_label": binding.get("mascotLabel", {}).get("value"),
                "official_website": binding.get("officialWebsite", {}).get("value"),
                "wikipedia_en": binding.get("wikipediaEn", {}).get("value", "").split("/")[-1] or None,
                "league_id": league_id,
                "league_qid": league_qid,
                "fetched_at": datetime.utcnow().isoformat() + "Z",
            }
            teams.append(team_data)
        
        print(f"  ✓ Found {len(teams)} teams")
        return teams
        
    except Exception as e:
        print(f"  ✗ Error fetching teams: {e}")
        return []


def load_leagues_seed(seed_path: Path) -> dict[str, Any]:
    """Load leagues seed YAML."""
    with open(seed_path) as f:
        return yaml.safe_load(f)


def save_raw_teams(teams: list[dict[str, Any]], output_path: Path) -> None:
    """Save raw team data as JSONL."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        for team in teams:
            f.write(json.dumps(team) + "\n")
    
    print(f"  ✓ Saved {len(teams)} teams to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch basketball team data from Wikidata"
    )
    parser.add_argument(
        "--league",
        help="Fetch teams for specific league (e.g., nba, wnba)",
    )
    parser.add_argument(
        "--all-active",
        action="store_true",
        help="Fetch teams for all active leagues (priority=P0a)",
    )
    parser.add_argument(
        "--seed",
        type=Path,
        default=Path("src/hoops_data/teams/leagues_seed.yaml"),
        help="Path to leagues seed YAML",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/raw/wikidata"),
        help="Output directory for raw JSONL",
    )
    
    args = parser.parse_args()
    
    # Load leagues seed
    seed_data = load_leagues_seed(args.seed)
    leagues = {league["league_id"]: league for league in seed_data["leagues"]}
    
    # Determine which leagues to fetch
    target_leagues = []
    if args.league:
        if args.league not in leagues:
            print(f"Error: League '{args.league}' not found in seed")
            return 1
        target_leagues = [leagues[args.league]]
    elif args.all_active:
        target_leagues = [
            league for league in seed_data["leagues"]
            if league.get("status") == "active"
        ]
    else:
        print("Error: Specify --league or --all-active")
        return 1
    
    # Fetch teams for each league
    all_teams = []
    for league in target_leagues:
        league_id = league["league_id"]
        league_qid = league["wikidata_qid"]
        
        teams = fetch_teams_for_league(league_id, league_qid)
        all_teams.extend(teams)
        
        # Save per-league JSONL
        output_path = args.output_dir / f"{league_id}_teams.jsonl"
        save_raw_teams(teams, output_path)
    
    print(f"\n✓ Complete. Fetched {len(all_teams)} total teams.")
    return 0


if __name__ == "__main__":
    exit(main())
