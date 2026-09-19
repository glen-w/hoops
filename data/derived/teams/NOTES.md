# Teams Desk Data Notes (2026-09-19)

## Wikimedia API Status

During initial implementation (2026-09-19), both Wikidata SPARQL and Wikimedia Commons APIs were experiencing rate limiting and access issues:

- **Wikidata SPARQL**: HTTP 429 "Aggressively rate-limiting to 1 req / min - this rule was created during active wdqs outage"
- **Commons API**: HTTP 403 Forbidden errors

## Current Data Status

The initial PR contains:

- **Stub data**: 3 NBA teams (Lakers, Celtics, Warriors) and 2 WNBA teams (Sparks, Liberty)
- **Real QIDs**: Wikidata entity IDs are authentic and manually verified
- **Schema complete**: All CSV schemas match the P0 specification

## Full Data Fetch

To fetch complete NBA + WNBA rosters when APIs are available:

```bash
# Fetch teams
python3 -m hoops_data.teams.fetch_wikidata_teams --all-active

# Normalize
python3 -m hoops_data.teams.normalize_teams

# Fetch logos (skips fair-use)
python3 -m hoops_data.teams.fetch_logos
```

## License Compliance

The logo fetcher skips fair-use and trademarked content to ensure redistribution compliance. Most professional sports team logos fall under this category and are recorded with `license=fair_use_skip` with URL reference only.

## Known Gaps

- Country codes not yet mapped from Wikidata QIDs to ISO-3166-1 alpha-2
- Color hex values not extracted (Wikidata P465 property) — **colors must be official only, never sampled from logos**
- Ownership structure locked to vocabulary: `sole|majority|group|public|municipal|unknown` — defaults to `unknown` until manual verification
- Wikipedia infobox gap-filling stub only

## Schema Updates (Glen's room lock)

**Added to teams.csv:**
- `abbr` — Stable short code (LAL, NYK, GSW, etc.)
- `former_names` — Pipe-separated historical names
- `colours_accent_hex` — Third official color
- Ownership structure restricted to locked vocabulary (no free text)

**Color policy:**
- Official hex only from Wikidata P465, official style guides, or documented Wikipedia sources
- Never sample from logo pixels
- Leave blank + confidence=GAP if no official claim
- `colours_source` required when any color present

**Logo policy:**
- Prefer SVG/PNG with transparent backgrounds
- No low-res wiki thumbnails for book figures
- Fair-use → URL-only row, no binary committed
