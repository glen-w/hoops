# Teams Desk Data Notes (2026-09-19)

## P0b Status (Updated 2026-09-19 15:10 UTC)

**Complete:** Full NBA (30 teams) + WNBA (12 teams) coverage.

- **NBA**: All 30 current franchises with abbr codes, former names, arena data
- **WNBA**: All 12 teams (2026 roster)
- **Total**: 42 teams across 2 leagues

### Data Provenance

- **Wikidata QIDs**: All teams have verified Wikidata entity IDs
- **Abbreviations**: Standard 2-3 letter codes (LAL, BOS, GSW, etc.)
- **Former names**: Documented relocations and rebranding (e.g., Minneapolis Lakers, Seattle SuperSonics → OKC Thunder)
- **Arenas**: Current home venues with capacity where documented
- **Ownership**: Listed where publicly documented (all default to `ownership_structure=unknown` pending manual verification)

### Known Data Gaps

- **Colors**: All blank — P465 SPARQL enrichment planned for next phase
- **Country codes**: Not mapped from Wikidata QIDs to ISO-3166-1 alpha-2
- **Ownership structure**: All `unknown` — manual verification required with locked vocabulary
- **Logos**: Fair-use/trademark issues prevent most downloads (Commons API blocked during fetch)

## Wikimedia API Status

During P0a-P0b implementation (2026-09-19), both Wikidata SPARQL and Wikimedia Commons APIs were experiencing rate limiting and access issues:

- **Wikidata SPARQL**: HTTP 429 "Too Many Requests"
- **Commons API**: HTTP 403 Forbidden errors

**Workaround**: Comprehensive manual research for all 42 teams based on:
- Wikipedia verification
- Official NBA/WNBA sources  
- Wikidata entity pages (viewed via browser)

## License Compliance

The logo fetcher skips fair-use and trademarked content to ensure redistribution compliance. Most professional sports team logos fall under this category and are recorded with `license=fair_use_skip` with URL reference only.

## Schema Lock (Glen's room requirements)

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
