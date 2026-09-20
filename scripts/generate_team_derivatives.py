#!/usr/bin/env python3
"""
Generate relocation graph (edges & nodes) from teams.csv.

Note: Mascot bestiary and abbreviation phonology generation removed.
Those interpretive packs live under author/derived-creative/teams/ (committed
author workspace per SCOPE — not citeable artifacts).
"""

import csv
import hashlib
from pathlib import Path

# Paths
TEAMS_CSV = Path("data/derived/teams/teams.csv")
OUTPUT_DIR = Path("data/derived/teams")

# Read teams data
teams = []
with open(TEAMS_CSV, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    teams = list(reader)

print(f"Loaded {len(teams)} teams")

# =============================================================================
# 1. RELOCATION GRAPH
# =============================================================================

relocation_edges = []
relocation_nodes = []
node_ids = set()
edge_counter = 1

def make_node_id(label: str, team_id: str = None) -> str:
    """Create consistent node ID from label."""
    if team_id:
        return f"node_{team_id}_{hashlib.md5(label.encode()).hexdigest()[:8]}"
    return f"node_{hashlib.md5(label.encode()).hexdigest()[:8]}"

def add_node(node_id: str, label: str, kind: str, team_id: str = "", as_of: str = "2026-09-19"):
    """Add node if not already present."""
    if node_id not in node_ids:
        node_ids.add(node_id)
        relocation_nodes.append({
            'node_id': node_id,
            'label': label,
            'kind': kind,
            'team_id': team_id,
            'as_of': as_of
        })

for team in teams:
    team_id = team['team_id']
    current_city = team['city']
    current_name = team['name']
    former_names = team.get('former_names', '').strip()
    league_id = team['league_id']
    source_url = team.get('source_url', '')
    
    # Add current city node
    if current_city:
        current_city_node = make_node_id(current_city, team_id)
        add_node(current_city_node, current_city, 'city', team_id)
    
    # Add current franchise node
    current_franchise_node = make_node_id(current_name, team_id)
    add_node(current_franchise_node, current_name, 'franchise', team_id)
    
    # Parse former names for relocations
    if former_names:
        former_list = [fn.strip() for fn in former_names.split('|') if fn.strip()]
        
        for former_name in former_list:
            # Infer if this is a city relocation or just a name change
            # Simple heuristic: check if city name appears in former name
            from_label = former_name
            from_node = make_node_id(former_name, team_id)
            
            # Try to detect if it's a city vs name change
            # This is interpretive - we note confidence
            if any(city_word in former_name.lower() for city_word in 
                   ['fort wayne', 'syracuse', 'new jersey', 'minneapolis', 
                    'seattle', 'new orleans', 'san diego', 'vancouver', 
                    'rochester', 'tri-cities', 'milwaukee', 'st. louis',
                    'baltimore', 'kansas city', 'omaha', 'charlotte',
                    'chicago', 'san antonio', 'dallas', 'texas', 'utah',
                    'orleans', 'oklahoma city', 'tulsa', 'detroit',
                    'orlando']):
                # Likely a city relocation
                add_node(from_node, former_name, 'aka', team_id)
                
                # Create edge from former to current
                relocation_edges.append({
                    'edge_id': f'edge_{edge_counter:04d}',
                    'from_label': former_name,
                    'to_team_id': team_id,
                    'to_city': current_city,
                    'year_approx': '',  # Would need additional data
                    'source_field': 'former_names',
                    'source_url': source_url,
                    'confidence': 'MEDIUM',
                    'notes': 'Inferred from former_names field; year unknown'
                })
                edge_counter += 1
            else:
                # Name change without clear city signal
                add_node(from_node, former_name, 'aka', team_id)
                
                relocation_edges.append({
                    'edge_id': f'edge_{edge_counter:04d}',
                    'from_label': former_name,
                    'to_team_id': team_id,
                    'to_city': current_city,
                    'year_approx': '',
                    'source_field': 'former_names',
                    'source_url': source_url,
                    'confidence': 'MEDIUM',
                    'notes': 'Name change; same market unclear without additional sources'
                })
                edge_counter += 1

# Write relocation edges
edges_path = OUTPUT_DIR / "relocation_edges.csv"
with open(edges_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'edge_id', 'from_label', 'to_team_id', 'to_city', 
        'year_approx', 'source_field', 'source_url', 'confidence', 'notes'
    ])
    writer.writeheader()
    writer.writerows(relocation_edges)

print(f"✓ Created {edges_path} ({len(relocation_edges)} edges)")

# Write relocation nodes
nodes_path = OUTPUT_DIR / "relocation_nodes.csv"
with open(nodes_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'node_id', 'label', 'kind', 'team_id', 'as_of'
    ])
    writer.writeheader()
    writer.writerows(sorted(relocation_nodes, key=lambda x: x['node_id']))

print(f"✓ Created {nodes_path} ({len(relocation_nodes)} nodes)")

print("\n✓ Relocation graph created successfully")
