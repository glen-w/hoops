# hoops_data.teams — Global Basketball Teams Desk

Reproducible pipeline for scraping Wikidata/Wikipedia/Commons for top-tier men's and women's basketball clubs worldwide.

## Overview

This package provides structured data for basketball teams across major leagues:

- **`leagues_seed.yaml`** — Curated P0 league inventory with Wikidata QIDs
- **`fetch_wikidata_teams.py`** — SPARQL queries to Wikidata for team metadata
- **`normalize_teams.py`** — Converts raw JSONL to derived CSV tables
- **`fetch_logos.py`** — Downloads free-license logos from Wikimedia Commons
- **`fetch_wikipedia_infobox.py`** — (Stub) Gap-fill from Wikipedia infoboxes

## Output Schema

### `data/derived/teams/leagues.csv`

| Column | Description |
|--------|-------------|
| league_id | Slug identifier (e.g., `nba`, `wnba`) |
| name | Official English display name |
| gender | `men` \| `women` \| `mixed` |
| tier | `1` for top domestic/continental |
| country_or_region | ISO-3166-1 alpha-2 or `INT` |
| governing_body | FIBA / NBA / league organization |
| wikidata_qid | Wikidata entity QID |
| wikipedia_en | English Wikipedia article title |
| season_label | e.g., `2025-26` |
| as_of | ISO date of data snapshot |
| source_url | Wikidata URL |
| confidence | HIGH / MEDIUM / LOW / GAP |

### `data/derived/teams/teams.csv`

| Column | Description |
|--------|-------------|
| team_id | Stable slug `{league_id}_{short}_{qid}` |
| league_id | Foreign key to leagues.csv |
| name | Full team name |
| short_name | Short identifier |
| city | Home city |
| country | ISO-3166-1 alpha-2 |
| arena | Current home venue name |
| arena_capacity | Integer capacity or blank |
| founded_year | Year established |
| colours_primary_hex | `#RRGGBB` or blank |
| colours_secondary_hex | `#RRGGBB` or blank |
| colours_source | wikidata / wiki / official |
| mascot | Mascot name or blank |
| owner | Owner person/entity string |
| ownership_structure | Free text (manual enrichment) |
| wikidata_qid | Wikidata entity QID |
| wikipedia_en | English Wikipedia article title |
| official_url | Official team website |
| as_of | ISO date of data snapshot |
| source_url | Wikidata URL |
| confidence | HIGH / MEDIUM / LOW / GAP |

### `data/derived/teams/logos.csv`

| Column | Description |
|--------|-------------|
| team_id | Foreign key to teams.csv |
| logo_kind | `current` \| `historical` |
| year_start | Optional year range start |
| year_end | Optional year range end |
| commons_title | Wikimedia Commons file title |
| commons_url | Commons description page URL |
| local_path | Relative path to downloaded file |
| mime | MIME type (e.g., `image/svg+xml`) |
| sha256 | SHA-256 hash of file |
| license | Commons license shortname or `fair_use_skip` |
| attribution | Author/attribution string |
| as_of | ISO date of data snapshot |
| confidence | HIGH / MEDIUM / GAP |

## Usage

### 1. Fetch team data from Wikidata

```bash
# Fetch NBA teams
uv run python -m hoops_data.teams.fetch_wikidata_teams --league nba

# Fetch WNBA teams
uv run python -m hoops_data.teams.fetch_wikidata_teams --league wnba

# Fetch all active leagues (P0a)
uv run python -m hoops_data.teams.fetch_wikidata_teams --all-active
```

Writes raw JSONL to `data/raw/wikidata/{league_id}_teams.jsonl`.

### 2. Normalize into derived CSVs

```bash
uv run python -m hoops_data.teams.normalize_teams
```

Reads `leagues_seed.yaml` and raw JSONL, writes:
- `data/derived/teams/leagues.csv`
- `data/derived/teams/teams.csv`
- `data/derived/teams/logos.csv` (schema only)

### 3. Fetch logos from Commons

```bash
# Dry-run to check licenses
uv run python -m hoops_data.teams.fetch_logos --dry-run

# Download free-license logos
uv run python -m hoops_data.teams.fetch_logos
```

Downloads logo files to `data/raw/logos/{team_id}/` and populates `logos.csv`.

**Important**: Fair-use and trademarked logos are skipped to ensure redistribution compliance. These are recorded with `license=fair_use_skip` and URL-only.

### 4. (Future) Gap-fill from Wikipedia

```bash
uv run python -m hoops_data.teams.fetch_wikipedia_infobox
```

Currently a stub. Future implementation will extract infobox data for colors, arena capacity, and ownership when Wikidata is incomplete.

## Rate Limits & Etiquette

- **Wikidata SPARQL**: ~60 req/min; script includes User-Agent header
- **Wikimedia Commons API**: No hard limit; default 1s delay between requests
- Adjust `--rate-limit` for `fetch_logos.py` if needed

## License Caveats

This pipeline respects intellectual property:

- **Free licenses only**: CC-BY, CC-BY-SA, PD, etc. are downloaded
- **Fair-use skipped**: Trademarked team logos under fair-use are recorded but not redistributed
- **Attribution**: `logos.csv` includes attribution and license for each file

Do not commit copyrighted binaries to git. Consider:
- `.gitignore` for `data/raw/logos/` + checksum manifest in git
- Git LFS if repo already uses it

Current implementation: logos are gitignored; checksums in CSV.

## Dependencies

See `pyproject.toml`:
- pandas
- pyyaml
- requests
- SPARQLWrapper

Install with:

```bash
uv pip install -e .
```

## Development Status

- **P0a (this PR)**: NBA + WNBA end-to-end
- **P0b (next)**: Expand to all tier-1 leagues in seed
- **P1 (future)**: Historical logos, ownership graphs, color hex extraction

## See Also

- [Plan document](../../../uploads/PLAN-2026-09-19_7896.md) — Full P0 specification
- [CHAPTER-MAP](../../../docs/CHAPTER-MAP.md) — Manuscript data map
- [tests/teams/](../../../tests/teams/) — Pytest suite
