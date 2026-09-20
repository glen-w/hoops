# Relocation Graph Methodology

**Version:** 1.0  
**Date:** 2026-09-20  
**Source:** `data/derived/teams/teams.csv` (441 teams, as of 2026-09-19)

## Purpose

Infer franchise relocation and name-change edges from the `former_names` field in the teams desk. This is a *derived interpretation* of the landed data—no relocations are invented.

## Methodology

### Edge inference

1. Parse the pipe-delimited `former_names` field for each team.
2. Create one edge per former name pointing to the current team's city.
3. Classify edge type using heuristic city-name matching:
   - If the former name contains a known city string (Fort Wayne, Syracuse, Seattle, etc.) → likely **relocation**.
   - Otherwise → **name change** (same market unclear without additional sources).

### Node construction

- **City nodes**: Current city of each team.
- **Franchise nodes**: Current team name.
- **AKA nodes**: Each former name.

Node IDs are deterministic hashes of `label + team_id`.

### Confidence

- All edges: **MEDIUM** — inferred from textual parsing; no year or ownership transfer data.
- **GAP** when unclear: Year is left blank; notes flag ambiguity.

### Limitations

- **Year unknown**: The `former_names` field provides no temporal data. Relocation years would require external sources (e.g., Basketball-Reference, team histories).
- **City inference is heuristic**: The city-name matching is keyword-based. A name like "Charlotte Bobcats" → "Charlotte Hornets" is flagged as a name change, but may also represent franchise continuity questions (2004 expansion vs. 2014 rebranding).
- **No validation of intermediate cities**: Multi-hop relocations (e.g., Tri-Cities → Milwaukee → St. Louis → Atlanta) are represented as parallel edges, not a directed chain.

### Examples

#### Clear relocation
- **Seattle SuperSonics** → Oklahoma City Thunder (city change)
- **Vancouver Grizzlies** → Memphis Grizzlies (city change)

#### Name change
- **Charlotte Bobcats** → Charlotte Hornets (same city, rebrand)
- **New Jersey Nets** → Brooklyn Nets (metro area shift)

#### Ambiguous
- **New York Nets** in the `former_names` of Brooklyn Nets: was this ABA Long Island → ABA New York → NBA New Jersey → NBA Brooklyn? The current graph does not model this temporal sequence.

## Output

### `relocation_edges.csv`

| Column | Description |
|--------|-------------|
| `edge_id` | Sequential identifier (`edge_0001`, ...) |
| `from_label` | Former name (from `former_names` field) |
| `to_team_id` | Current team identifier |
| `to_city` | Current city of the team |
| `year_approx` | Relocation year (blank—data unavailable) |
| `source_field` | Always `former_names` |
| `source_url` | Wikidata QID URL from teams.csv |
| `confidence` | Always `MEDIUM` |
| `notes` | Interpretation note |

### `relocation_nodes.csv`

| Column | Description |
|--------|-------------|
| `node_id` | Hashed node identifier |
| `label` | City, team name, or former name |
| `kind` | `city`, `franchise`, or `aka` |
| `team_id` | Associated team (may be blank for city nodes) |
| `as_of` | Snapshot date (2026-09-19) |

## Future enhancements

- Add relocation years from Basketball-Reference team histories.
- Validate city assignments with historical market data.
- Link to ownership transfer events (see `ownership_events.csv`).
- Distinguish ABA/BAA/NBL pre-merger lineages.

## Honest limitations

This graph is a *reading aid*, not authoritative franchise genealogy. When year or intermediate cities are unclear, the field is left blank rather than inventing data. Always cross-reference with primary sources for publication-grade claims.
