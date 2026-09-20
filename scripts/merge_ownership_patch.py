#!/usr/bin/env python3
"""Merge ownership patch into teams.csv for NBA and WNBA teams only."""

import csv
import sys
from pathlib import Path

def read_csv_as_dicts(filepath):
    """Read a CSV file into a list of dictionaries."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv_from_dicts(filepath, rows, fieldnames):
    """Write a list of dictionaries to a CSV file."""
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    # Paths
    patch_path = Path('/home/ubuntu/.cursor/projects/workspace/uploads/ownership_patch_5211.csv')
    teams_path = Path('/workspace/data/derived/teams/teams.csv')
    
    print(f"Reading patch from: {patch_path}")
    print(f"Reading teams from: {teams_path}")
    
    # Read the patch and teams data
    patch_rows = read_csv_as_dicts(patch_path)
    teams_rows = read_csv_as_dicts(teams_path)
    
    # Store original fieldnames
    teams_fieldnames = list(teams_rows[0].keys())
    
    print(f"\nPatch has {len(patch_rows)} rows")
    print(f"Teams has {len(teams_rows)} rows")
    
    # Create a lookup dictionary for patch data by (league_id, abbr)
    # Handle abbreviation mismatches between patch and teams.csv
    abbr_mapping = {
        'LV': 'LVA',   # Las Vegas Aces
        'LA': 'LAS',   # Los Angeles Sparks
        'NY': 'NYL',   # New York Liberty
        'PHX': 'PHO',  # Phoenix Mercury
    }
    
    patch_lookup = {}
    for patch_row in patch_rows:
        key = (patch_row['league_id'], patch_row['abbr'])
        patch_lookup[key] = patch_row
    
    print(f"\nPatch lookup has {len(patch_lookup)} entries")
    
    # Track updates
    updates = []
    not_matched = []
    
    # Update teams data
    for team_row in teams_rows:
        league_id = team_row['league_id']
        abbr = team_row['abbr']
        
        # Only process NBA and WNBA teams
        if league_id not in ['nba', 'wnba']:
            continue
        
        # Look up patch data, using abbr mapping if needed
        patch_abbr = abbr_mapping.get(abbr, abbr)
        key = (league_id, patch_abbr)
        if key in patch_lookup:
            patch = patch_lookup[key]
            
            # Store original values for reporting
            old_owner = team_row['owner']
            old_structure = team_row['ownership_structure']
            
            # Update owner and ownership_structure
            team_row['owner'] = patch['owner']
            team_row['ownership_structure'] = patch['ownership_structure']
            
            # Update provenance fields carefully
            # The patch has ownership-specific source_url, as_of, confidence
            # Current teams.csv has general team source_url (Wikidata)
            # We should NOT overwrite the general source_url with ownership source
            # Instead, we'll update as_of and confidence since they're at team level
            team_row['as_of'] = patch['as_of']
            team_row['confidence'] = patch['confidence']
            # Note: source_url in teams.csv should stay as Wikidata provenance
            # The ownership source_url is documented in the patch notes
            
            updates.append({
                'team_id': team_row['team_id'],
                'abbr': abbr,
                'league': league_id,
                'old_owner': old_owner,
                'new_owner': patch['owner'],
                'old_structure': old_structure,
                'new_structure': patch['ownership_structure'],
                'confidence': patch['confidence']
            })
        else:
            not_matched.append(f"{league_id}_{abbr}")
    
    # Write updated teams data
    write_csv_from_dicts(teams_path, teams_rows, teams_fieldnames)
    
    # Report results
    print(f"\n{'='*70}")
    print(f"MERGE RESULTS")
    print(f"{'='*70}")
    print(f"\nUpdated {len(updates)} teams:")
    print(f"{'Team':<20} {'Old Owner':<25} → {'New Owner':<25} {'Structure':<12} {'Conf'}")
    print(f"{'-'*110}")
    
    for update in updates:
        print(f"{update['league'].upper()} {update['abbr']:<16} "
              f"{update['old_owner']:<25} → "
              f"{update['new_owner']:<25} "
              f"{update['new_structure']:<12} "
              f"{update['confidence']}")
    
    if not_matched:
        print(f"\n⚠️  WARNING: {len(not_matched)} NBA/WNBA teams not matched in patch:")
        for team in not_matched:
            print(f"  - {team}")
    
    print(f"\n✅ Updated teams.csv written to: {teams_path}")
    print(f"{'='*70}\n")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
