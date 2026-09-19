> Folded into `main` alongside the NBA and WNBA desk. `teams.csv` now has 84 rows in the shared 24-column schema (30 NBA, 12 WNBA, 20 EuroLeague, 22 EuroLeague Women). The fetch script refreshes only the EuroLeague leagues and leaves the others in place. Partizan's abbreviation is `PTZ` so it does not collide with Paris (`PAR`).

# Teams P0c Status — EuroLeague + EuroLeague Women

**Completed**: 2026-09-19  
**PR**: [#24](https://github.com/glen-w/hoops/pull/24)  
**Branch**: `cursor/teams-p0c-euroleague-105f`

## ✅ Deliverables Complete

### 1. Seed Data
- ✅ `scripts/teams/leagues_seed.yaml` created
  - 2 leagues: EuroLeague (men) + EuroLeague Women
  - 44 teams total (20 men + 24 women)
  - 42 teams with Wikidata QIDs (status: `ready_for_p0c`)
  - 2 gap teams documented (status: `gap`)

### 2. Data Pipeline
- ✅ `scripts/teams/fetch_and_normalize_teams.py` created
  - Reads seed YAML
  - Fetches Wikidata metadata (country, founded year, former names)
  - Derives abbreviations
  - Outputs normalized CSV with locked 14-column schema

### 3. Output Data
- ✅ `data/derived/teams/teams.csv` generated (42 teams)
  - EuroLeague: 20 men's teams
  - EuroLeague Women: 22 teams (with QIDs)
  - Schema locks: abbr, country (ISO), colors_hex, former_names
  - No invented QIDs or colors
  - Official hex only / blank if unknown ✅

### 4. Logo Infrastructure
- ✅ `data/derived/teams/logos.csv` (sparse, header only)
- ✅ `LOGOS-README.md` (fair-use URL-only policy, SVG preferred)
- ✅ `LOGOS-GAPS.md` (0% coverage documented)
- ✅ No copyrighted logos downloaded
- ✅ Commons-blocked logos left sparse ✅

### 5. Tests
- ✅ `scripts/teams/test_teams_data.py` created (7 validation tests)
  - Schema lock enforcement
  - Row counts match seed (20 men, 22 women)
  - Gap teams documented and excluded
  - Required fields populated
  - Data integrity checks
  - League IDs correct
- ✅ **All tests passing (7/7)** ✅

### 6. Documentation
- ✅ `data/derived/teams/README.md` (comprehensive)
- ✅ `LOGOS-README.md` (fair-use policy)
- ✅ `LOGOS-GAPS.md` (coverage gaps)
- ✅ `docs/CHAPTER-MAP.md` updated with EuroLeague entries
- ✅ Gap teams documented (2) ✅

## Coverage Summary

| League | Teams in Seed | Teams with QIDs | Teams in CSV | Gaps |
|--------|-------------:|----------------:|-------------:|-----:|
| EuroLeague (men) | 20 | 20 | 20 | 0 |
| EuroLeague Women | 24 | 22 | 22 | 2 |
| **Total** | **44** | **42** | **42** | **2** |

**Gap teams** (no Wikidata QID):
1. Kangoeroes Basket Mechelen (EuroLeague Women)
2. KP Brno (EuroLeague Women)

## Schema Compliance

✅ **Locked 14-column schema** (same as NBA/WNBA pattern):
- `team_id`, `league_id`, `name`, `short_name`, `abbr`
- `gender` (men/women)
- `country` (ISO 3166-1 alpha-2)
- `founded_year`
- `colors_hex` (blank if unknown) ✅
- `former_names` (from Wikidata)
- `wikidata_qid`, `wikipedia_en`, `as_of`, `confidence`

## Data Sources

| Source | Purpose | Method | As of |
|--------|---------|--------|-------|
| English Wikipedia | Team verification, QID lookup | `pageprops wikibase_item` API | 2026-09-19 |
| Wikidata | QIDs, country (P17), founded year (P571), former names (P1448) | Entity API | 2026-09-19 |
| Uploaded `qid_map.md` | QID audit trail | Manual curation | 2026-09-19 |

## Scope Compliance

✅ **EuroLeague M/W only** — no expansion to ACB/LNB/etc.  
✅ **No invented QIDs** — all from Wikidata  
✅ **No invented colors** — blank where unknown  
✅ **Fair-use logos** — URL-only, no downloads  
✅ **2026-27 season** — current as of access date

## Files Changed

| Path | Type | Lines |
|------|------|------:|
| `scripts/teams/leagues_seed.yaml` | new | 463 |
| `scripts/teams/fetch_and_normalize_teams.py` | new | 300 |
| `scripts/teams/test_teams_data.py` | new | 242 |
| `data/derived/teams/teams.csv` | new | 43 |
| `data/derived/teams/logos.csv` | new | 1 |
| `data/derived/teams/README.md` | new | 170 |
| `data/derived/teams/LOGOS-README.md` | new | 77 |
| `data/derived/teams/LOGOS-GAPS.md` | new | 48 |
| `docs/CHAPTER-MAP.md` | modified | +5 |

**Total**: 9 files, 1,381 insertions

## Testing Results

```
✓ teams.csv exists
✓ Schema locked (14 columns)
✓ Row counts match seed:
  - EuroLeague (men): 20 teams
  - EuroLeague Women: 22 teams
  - Total: 42 teams
✓ Gap teams documented: euroleague_women_kangoeroes, euroleague_women_kp_brno
✓ Required fields populated for all teams
✓ Data integrity checks passed
✓ League IDs correct

✓ All 7 tests passed!
```

## Follow-Up Work (Out of Scope for P0c)

- [ ] Populate `colors_hex` from Wikidata P462 (requires color item resolution)
- [ ] Fetch logo URLs from Wikimedia Commons (via Wikidata P154)
- [ ] Expand to other leagues (ACB, LNB, etc.)
- [ ] Add Kangoeroes and KP Brno QIDs when available
- [ ] Populate enwiki for Casademont Zaragoza and AZS UMCS Lublin

## Git Details

- **Branch**: `cursor/teams-p0c-euroleague-105f`
- **Commit**: `92c30f6` (feat(teams): P0c EuroLeague + EuroLeague Women)
- **PR**: [#24](https://github.com/glen-w/hoops/pull/24)
- **Status**: Draft PR open, ready for review

## Sign-Off

All P0c requirements met:
- ✅ Merge fragment into seed (no "todo" placeholders)
- ✅ Run/extend fetch+normalize → teams.csv
- ✅ Schema locks (abbr, former_names, ownership vocab, official hex/blank, country ISO)
- ✅ Logos: URL-only + SVG prefer; Commons blocked → sparse + documented
- ✅ Tests: row counts match seed (men 20; women 22 with QIDs; gaps documented)
- ✅ CHAPTER-MAP: updated with EuroLeague M/W entries
- ✅ PR opened (new branch off main)

**Ready for review.**
