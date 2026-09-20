#!/usr/bin/env python3
"""
Generate three derived datasets from teams.csv:
1. Relocation graph (edges & nodes)
2. Mascot bestiary
3. Abbreviation phonology
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

# =============================================================================
# 2. MASCOT BESTIARY
# =============================================================================

mascot_rows = []

# Taxonomy keywords for classification
ANIMAL_KEYWORDS = {
    'animal': ['bull', 'bear', 'hawk', 'raptor', 'grizzl', 'wolf', 'cat', 
               'dog', 'horse', 'lion', 'tiger', 'panther', 'jaguar', 'eagle',
               'pelican', 'hornet', 'bee', 'dragon', 'bison', 'coyote',
               'gorilla', 'snake', 'falcon', 'leopard', 'rabbit', 'deer'],
    'human': ['wizard', 'king', 'knight', 'warrior', 'giant', 'thunder',
              'buccaneer', 'bandit', 'ninja'],
    'abstract': ['heat', 'magic', 'storm', 'thunder', 'lightning', 'fire',
                 'energy', 'spirit', 'force'],
    'object': ['rocket', 'sun', 'moon', 'star', 'wheel']
}

def classify_mascot(mascot_name: str) -> tuple[str, str]:
    """Classify mascot into taxonomy."""
    if not mascot_name:
        return 'unknown', ''
    
    mascot_lower = mascot_name.lower()
    
    # Check animal
    for keyword in ANIMAL_KEYWORDS['animal']:
        if keyword in mascot_lower:
            # Try to get more specific
            if 'bull' in mascot_lower:
                return 'animal', 'bovine'
            elif 'bear' in mascot_lower:
                return 'animal', 'ursine'
            elif any(bird in mascot_lower for bird in ['hawk', 'eagle', 'raptor', 'falcon']):
                return 'animal', 'avian'
            elif 'cat' in mascot_lower or 'panther' in mascot_lower or 'leopard' in mascot_lower:
                return 'animal', 'feline'
            elif 'dog' in mascot_lower:
                return 'animal', 'canine'
            elif 'wolf' in mascot_lower or 'coyote' in mascot_lower:
                return 'animal', 'canine'
            elif 'horse' in mascot_lower:
                return 'animal', 'equine'
            elif 'lion' in mascot_lower or 'tiger' in mascot_lower:
                return 'animal', 'feline'
            elif 'bison' in mascot_lower:
                return 'animal', 'bovine'
            elif 'dragon' in mascot_lower:
                return 'animal', 'mythical'
            elif 'gorilla' in mascot_lower:
                return 'animal', 'primate'
            elif 'hornet' in mascot_lower or 'bee' in mascot_lower:
                return 'animal', 'insect'
            elif 'pelican' in mascot_lower:
                return 'animal', 'avian'
            elif 'rabbit' in mascot_lower:
                return 'animal', 'lagomorph'
            return 'animal', 'general'
    
    # Check human
    for keyword in ANIMAL_KEYWORDS['human']:
        if keyword in mascot_lower:
            return 'human', 'anthropomorphic'
    
    # Check abstract
    for keyword in ANIMAL_KEYWORDS['abstract']:
        if keyword in mascot_lower:
            return 'abstract', 'elemental'
    
    # Check object
    for keyword in ANIMAL_KEYWORDS['object']:
        if keyword in mascot_lower:
            return 'object', 'inanimate'
    
    # Default
    if 'leprechaun' in mascot_lower:
        return 'human', 'mythological'
    
    return 'unknown', 'unclassified'

for team in teams:
    mascot = team.get('mascot', '').strip()
    
    # Only include teams with mascots or create GAP rows for teams without
    if mascot or True:  # Include all for completeness
        taxon, taxon_detail = classify_mascot(mascot)
        
        mascot_rows.append({
            'team_id': team['team_id'],
            'mascot': mascot if mascot else '',
            'taxon': taxon,
            'taxon_detail': taxon_detail,
            'league_id': team['league_id'],
            'source_url': team.get('source_url', ''),
            'confidence': 'HIGH' if mascot else 'GAP'
        })

# Write mascot bestiary
bestiary_path = OUTPUT_DIR / "mascot_bestiary.csv"
with open(bestiary_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'team_id', 'mascot', 'taxon', 'taxon_detail', 'league_id', 
        'source_url', 'confidence'
    ])
    writer.writeheader()
    writer.writerows(mascot_rows)

print(f"✓ Created {bestiary_path} ({len(mascot_rows)} entries)")

# =============================================================================
# 3. ABBREVIATION PHONOLOGY
# =============================================================================

abbr_rows = []

def analyze_abbreviation(abbr: str, team_name: str, city: str) -> tuple[list, str]:
    """Analyze abbreviation pattern."""
    patterns = []
    notes = []
    
    if not abbr:
        return ['unknown'], 'No abbreviation provided'
    
    abbr_upper = abbr.upper()
    
    # Check if it's city initials
    if city:
        city_initials = ''.join([word[0] for word in city.split() if word])
        if abbr_upper == city_initials.upper():
            patterns.append('city_initials')
            notes.append(f"Initials of {city}")
    
    # Check if it's team nickname clip
    name_parts = team_name.split()
    if len(name_parts) >= 2:
        nickname = name_parts[-1]
        if abbr_upper.startswith(nickname[:3].upper()):
            patterns.append('nickname_clip')
            notes.append(f"Clip of {nickname}")
        
        # Check for full city + nickname initials
        if len(abbr) == 3:
            city_part = name_parts[0] if len(name_parts) > 1 else ''
            if city_part and abbr[0].upper() == city_part[0].upper():
                patterns.append('city_plus_nickname')
    
    # Check for state abbreviations
    state_abbrs = ['LA', 'NY', 'TX', 'CA', 'MA', 'IL', 'FL', 'PA', 'OH', 
                   'MI', 'WA', 'CO', 'UT', 'AZ', 'OR', 'IN', 'TN', 'NC',
                   'MN', 'OK', 'DC']
    if abbr_upper in state_abbrs or abbr_upper.startswith(tuple(state_abbrs)):
        patterns.append('state')
        notes.append('Contains state code')
    
    # Phonetic patterns
    if len(abbr) <= 3:
        patterns.append('trigram')
    elif len(abbr) == 4:
        patterns.append('tetragram')
    else:
        patterns.append('long_form')
    
    if not patterns or patterns == ['trigram']:
        patterns.append('other')
    
    return patterns, '; '.join(notes) if notes else ''

for team in teams:
    abbr = team.get('abbr', '').strip()
    patterns, analysis_notes = analyze_abbreviation(
        abbr, team['name'], team.get('city', '')
    )
    
    abbr_rows.append({
        'team_id': team['team_id'],
        'abbr': abbr,
        'pattern_tags': '|'.join(patterns),
        'letter_count': len(abbr) if abbr else 0,
        'league_id': team['league_id'],
        'notes': analysis_notes
    })

# Write abbreviation phonology
phonology_path = OUTPUT_DIR / "abbr_phonology.csv"
with open(phonology_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'team_id', 'abbr', 'pattern_tags', 'letter_count', 'league_id', 'notes'
    ])
    writer.writeheader()
    writer.writerows(abbr_rows)

print(f"✓ Created {phonology_path} ({len(abbr_rows)} entries)")

print("\n✓ All three derived datasets created successfully")
