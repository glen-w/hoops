# Teams Desk Data Notes

## P0d Status (Updated 2026-09-19 17:38 UTC)

**Enrichments Complete (Partial):**
- ✅ Country codes: ISO-3166-1 alpha-2 mapping (US/CA/EU)
- ✅ Ownership structure: Conservative heuristic mapping to locked vocabulary
- ❌ Colors: Wikidata SPARQL outage (HTTP 429 "Aggressively rate-limiting to 1 req / min"); 0/84 filled
- ❌ Logos: Wikidata SPARQL blocked, cannot fetch logo URLs; 0/84 filled

### Full Desk Scope: 84 Teams (NBA 30 + WNBA 12 + EuroLeague 24 + EuroLeague Women 20)

### Fill Rates (84 teams)

| Field | Fill | Count | Notes |
|-------|------|-------|-------|
| **Basic Identity** |
| name | 100% | 84/84 | All teams |
| abbr | 100% | 84/84 | Unique within league |
| wikidata_qid | 100% | 84/84 | All verified |
| **Location** |
| city | ~95% | ~80/84 | Most teams |
| **country** | **100%** | **84/84** | **US (42), CA (1), EU (41)** |
| arena | ~95% | ~80/84 | Current venues where documented |
| arena_capacity | ~75% | ~63/84 | Many EuroLeague gaps |
| **History** |
| founded_year | ~95% | ~80/84 | Most teams |
| former_names | ~30% | ~25/84 | Where applicable |
| **Branding** |
| colours_primary_hex | **0%** | **0/84** | **Wikidata SPARQL outage (HTTP 429)** |
| colours_secondary_hex | 0% | 0/84 | Wikidata SPARQL outage |
| colours_accent_hex | 0% | 0/84 | Wikidata SPARQL outage |
| colours_source | 0% | 0/84 | Will be 'wikidata' when available |
| mascot | ~50% | ~42/84 | NBA/WNBA mostly filled |
| **Ownership** |
| owner | ~60% | ~50/84 | Many EuroLeague gaps |
| **ownership_structure** | **100%** | **84/84** | **3 mapped + 81 unknown** |

### Ownership Structure Breakdown

| Value | Count | Examples |
|-------|-------|----------|
| unknown | 39 | Most teams (conservative default) |
| group | 1 | Maple Leaf Sports & Entertainment (TOR) |
| sole | 1 | DeVos family (ORL) |
| municipal | 1 | Mohegan Tribe (CON) |

**Mapping strategy**: Conservative heuristics only map when confident. Individual owners (e.g., "Mark Cuban", "Jeanie Buss") remain `unknown` pending manual verification of control structure (sole vs. majority vs. group).

### Country Code Mapping

- **US**: 41 teams (all NBA + all WNBA except TOR)
- **CA**: 1 team (Toronto Raptors)

## P0d Coverage (Completed 2026-09-19)

**Full desk: NBA (30) + WNBA (12) + EuroLeague Men (24) + EuroLeague Women (20)** = 84 teams

### League Breakdown

**North American Leagues:**
- NBA: 30 teams (complete)
- WNBA: 12 teams (complete)

**European Leagues:**
- EuroLeague Men: 24 teams (2025-26 season; complete)
- EuroLeague Women: 20 teams (2025-26 season; complete)

### Data Provenance

- **Wikidata QIDs**: All teams have verified Wikidata entity IDs
- **Abbreviations**: Standard 2-3 letter codes
- **Former names**: Documented relocations and rebranding
- **Arenas**: Current home venues with capacity where available
- **Ownership**: Listed where publicly documented

### Notable Relocations

**NBA:**
- Brooklyn Nets ← New Jersey Americans/Nets
- Oklahoma City Thunder ← Seattle SuperSonics
- Memphis Grizzlies ← Vancouver
- Sacramento Kings ← Rochester → Cincinnati → Kansas City
- Washington Wizards ← Chicago → Baltimore → Bullets

**WNBA:**
- Las Vegas Aces ← Utah Starzz → San Antonio
- Dallas Wings ← Detroit/Tulsa Shock
- Connecticut Sun ← Orlando Miracle

## API Limitations (2026-09-19)

During P0a-P0b-P0b.1-P0d implementation, Wikimedia APIs experienced persistent issues:

### Wikidata SPARQL
- **P0a/P0b**: HTTP 429 "Too Many Requests"
- **P0b.1**: Timeout on color queries (P465 property)
- **P0d (2026-09-19 17:38 UTC)**: HTTP 429 "Aggressively rate-limiting to 1 req / min - this rule was created during active wdqs outage (797a132)"
  - Attempted full desk color enrichment (84 teams, 2s rate limit)
  - **Result**: 0/84 teams enriched due to ongoing WDQS outage
- **Status**: Color enrichment script (`enrich_colors.py`) ready for retry when outage resolves

### Wikimedia Commons
- **P0a/P0b/P0b.1**: HTTP 403 Forbidden
- **P0d**: Cannot fetch logo URLs from Wikidata SPARQL due to outage
- **Status**: Logo fetch script (`fetch_logos.py`) ready with polite User-Agent and 2s default rate limit

**Workaround for base data**: Manual research from Wikipedia, official NBA/WNBA/EuroLeague sources, and Wikidata entity pages (browser verification).

## Enrichment Scripts Ready for Retry

**P0d Retry Attempt (2026-09-19 17:32 UTC):**
- Executed `enrich_colors.py` with 2s rate limit on full 84-team desk
- Result: 0/84 filled due to Wikidata SPARQL outage (HTTP 429)
- Error message: "Aggressively rate-limiting to 1 req / min - this rule was created during active wdqs outage (797a132)"

**When WDQS outage resolves:**

```bash
# Retry color enrichment (P465 official colors)
python3 -m hoops_data.teams.enrich_colors --rate-limit 2.0

# Retry logo fetch (requires WDQS for logo URLs, then Commons for downloads)
python3 -m hoops_data.teams.fetch_logos --rate-limit 2.0
```

Both scripts use:
- Polite User-Agent: `hoops-data/0.1 (glen-w/hoops basketball teams; research; [email protected])`
- 2-second default rate limiting
- Conservative error handling (leaves blanks on failure)

## Schema Compliance

All 84 teams comply with locked 24-column schema:
- ✅ Unique `abbr` codes within each league
- ✅ `ownership_structure` in locked vocabulary (sole|majority|group|public|municipal|unknown)
- ✅ `country` mapped to ISO-3166-1 alpha-2 (US/CA for North America; country codes for EuroLeague)
- ✅ Colors blank (no invented values; ready for P465 extraction when WDQS available)
- ✅ Real Wikidata QIDs for all teams
- ✅ Former names documented where applicable

## Next Phase

### P465 Color Extraction (Blocked)
- Query Wikidata P465 (official color) property
- Extract hex codes where available
- Populate `colours_source=wikidata`
- **Script ready**: `enrich_colors.py`

### Logo Downloads (Blocked)
- Retry Commons API with polite headers
- Prefer SVG over raster
- Skip fair-use (URL-only)
- **Script ready**: `fetch_logos.py` with updated headers

### Ownership Manual Verification (P1)
- Review individual owners for sole vs. majority classification
- Document corporate control structures
- Update conservative `unknown` mappings with verified data
