# Teams Desk Data Notes

## P0b.1 Status (Updated 2026-09-19 15:17 UTC)

**Enrichments Complete (Partial):**
- ✅ Country codes: ISO-3166-1 alpha-2 mapping (US/CA)
- ✅ Ownership structure: Conservative heuristic mapping to locked vocabulary
- ⚠️  Colors: API blocked (SPARQL timeout); enrichment script ready for retry
- ⚠️  Logos: API blocked (Commons 403); enrichment script ready with polite User-Agent

### Fill Rates (42 teams)

| Field | Fill | Count | Notes |
|-------|------|-------|-------|
| **Basic Identity** |
| name | 100% | 42/42 | All teams |
| abbr | 100% | 42/42 | Unique within league |
| wikidata_qid | 100% | 42/42 | All verified |
| **Location** |
| city | 100% | 42/42 | All teams |
| **country** | **100%** | **42/42** | **US (41), CA (1)** |
| arena | 100% | 42/42 | Current venues |
| arena_capacity | ~95% | ~40/42 | Most documented |
| **History** |
| founded_year | 100% | 42/42 | All teams |
| former_names | ~40% | ~17/42 | Where applicable |
| **Branding** |
| colours_primary_hex | **0%** | **0/42** | **API blocked (ready for retry)** |
| colours_secondary_hex | 0% | 0/42 | API blocked |
| colours_accent_hex | 0% | 0/42 | API blocked |
| colours_source | 0% | 0/42 | Will be 'wikidata' when filled |
| mascot | ~70% | ~29/42 | Where applicable |
| **Ownership** |
| owner | ~95% | ~40/42 | Where publicly documented |
| **ownership_structure** | **100%** | **42/42** | **3 mapped + 39 unknown** |

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

## P0b Coverage (Completed 2026-09-19)

**Full NBA (30 teams) + WNBA (12 teams)** = 42 teams

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

During P0a-P0b-P0b.1 implementation, Wikimedia APIs experienced persistent issues:

### Wikidata SPARQL
- **P0a/P0b**: HTTP 429 "Too Many Requests"
- **P0b.1**: Timeout on color queries (P465 property)
- **Status**: Color enrichment script (`enrich_colors.py`) ready for retry with 2s rate limit

### Wikimedia Commons
- **P0a/P0b/P0b.1**: HTTP 403 Forbidden
- **Status**: Logo fetch script updated with polite User-Agent and 2s default rate limit

**Workaround for base data**: Manual research from Wikipedia, official NBA/WNBA sources, and Wikidata entity pages (browser verification).

## Enrichment Scripts Ready for Retry

When APIs become available:

```bash
# Retry color enrichment (P465 official colors)
python3 -m hoops_data.teams.enrich_colors --rate-limit 2.0

# Retry logo fetch (prefers SVG, skips fair-use)
python3 -m hoops_data.teams.fetch_logos --rate-limit 2.0
```

Both scripts now use:
- Polite User-Agent with contact info
- 2-second default rate limiting
- Conservative retry logic

## Schema Compliance

All 42 teams comply with locked schema:
- ✅ Unique `abbr` codes within each league
- ✅ `ownership_structure` in locked vocabulary (sole|majority|group|public|municipal|unknown)
- ✅ `country` mapped to ISO-3166-1 (US/CA)
- ✅ Colors blank (no invented values; ready for P465 extraction)
- ✅ Real Wikidata QIDs
- ✅ Former names documented where applicable

## Ownership Enrichment (2026-09-19)

**Status:** Complete for NBA (30) + WNBA (12) = 42 teams

Researcher's ownership patch applied with high-confidence sources:
- **Patch date:** 2026-09-19
- **Coverage:** All NBA and WNBA teams
- **Methodology:** See `ownership_methodology.md` in this directory
- **Not included:** EuroLeague and EuroLeague Women (deferred; multi-jurisdiction corporate structures)

### Ownership Structure Distribution

| Structure | NBA | WNBA | Total |
|-----------|-----|------|-------|
| sole      | 5   | 1    | 6     |
| majority  | 20  | 5    | 25    |
| group     | 4   | 6    | 10    |
| public    | 1   | 0    | 1     |
| **Total** | **30** | **12** | **42** |

**High confidence (37):** Standard ownership cites (team FO pages, Wikipedia List of NBA team owners, closing PRs)  
**Medium confidence (5):** Controlling role clear; stake % or named individual differs by source (DEN, GSW, SAC, WNBA CHI, WNBA DAL)

### Notable Ownership Details

- **Connecticut Sun:** Mohegan → Fertitta family (closed 2026-05-14); structure changed from `municipal` to `sole`
- **Trail Blazers:** Allen Trust → Tom Dundon (2026 sale)
- **Celtics:** Grousbeck → William Chisholm majority (closed 2025)
- **Lakers:** Mark Walter majority; Jeanie Buss remains governor/CEO
- **Knicks:** Classified as `public` (MSG Sports Corp, NYSE:MSGS) despite Dolan family voting control
- **Timberwolves/Lynx:** Taylor → Lore & Rodriguez (closed 2025)

See `ownership_methodology.md` for decision rules and source hierarchy.

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
