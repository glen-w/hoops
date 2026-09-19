# Teams Data — Global Basketball

**Scope**: International basketball teams with Wikidata integration  
**Status**: P0c complete (EuroLeague + EuroLeague Women)  
**As of**: 2026-09-19

## Files

| File | Description | Rows |
|------|-------------|-----:|
| `teams.csv` | Normalized team metadata | 42 data rows |
| `logos.csv` | Logo URL references (sparse) | 0 populated |
| `leagues_seed.yaml` | Curated source of truth (in `scripts/teams/`) | 2 leagues, 44 teams |

## Coverage

| League | Teams in Seed | Teams with QIDs | Teams in CSV | Gap Teams |
|--------|-------------:|----------------:|-------------:|----------:|
| EuroLeague (men) | 20 | 20 | 20 | 0 |
| EuroLeague Women | 24 | 22 | 22 | 2 |
| **Total** | **44** | **42** | **42** | **2** |

### Gap Teams (No Wikidata QID)

1. **Kangoeroes Basket Mechelen** (EuroLeague Women) — No women-specific Wikidata item found
2. **KP Brno** (EuroLeague Women) — No Wikidata item found

These teams are documented in `scripts/teams/leagues_seed.yaml` with `status: gap` and are excluded from `teams.csv`.

## Schema: teams.csv

| Column | Type | Description | Populated |
|--------|------|-------------|-----------|
| `team_id` | string | Unique identifier (e.g., `euroleague_barcelona`) | 100% |
| `league_id` | string | Parent league (e.g., `euroleague`, `euroleague_women`) | 100% |
| `name` | string | Full team name (e.g., "FC Barcelona") | 100% |
| `short_name` | string | Common short name (e.g., "Barcelona") | 100% |
| `abbr` | string | Abbreviation (derived, e.g., "BAR") | 100% |
| `gender` | enum | `men` or `women` | 100% |
| `country` | string | ISO 3166-1 alpha-2 country code (from Wikidata P17) | ~95% |
| `founded_year` | string | Year founded (from Wikidata P571) | ~90% |
| `colors_hex` | string | Official team colors as hex codes (comma-separated) | 0% |
| `former_names` | string | Semicolon-separated list of former names (Wikidata P1448) | ~15% |
| `wikidata_qid` | string | Wikidata item ID (e.g., Q54893) | 100% |
| `wikipedia_en` | string | English Wikipedia page title | ~95% |
| `as_of` | date | Data collection date (YYYY-MM-DD) | 100% |
| `confidence` | enum | Confidence level: `high`, `medium`, `low` | 100% |

### Schema Lock

The schema is **locked** and validated by `scripts/teams/test_teams_data.py`. Do not add, remove, or reorder columns without updating the test suite.

## Data Sources

1. **Seed data**: Hand-curated in `scripts/teams/leagues_seed.yaml`
   - Team names and QIDs verified from English Wikipedia and Wikidata (2026-09-19)
   - See uploaded `qid_map.md` for audit trail

2. **Wikidata enrichment**: Fetched via Wikidata API
   - Country (P17)
   - Founded year (P571)
   - Official colors (P462) — deferred
   - Former names (P1448)

3. **Logos**: URL references only (fair-use policy)
   - See `LOGOS-README.md` for details
   - No logo files are hosted in this repository

## Pipeline

```
scripts/teams/leagues_seed.yaml
           ↓
scripts/teams/fetch_and_normalize_teams.py
           ↓
data/derived/teams/teams.csv
```

### Running the Pipeline

```bash
# Fetch and normalize teams from seed
python3 scripts/teams/fetch_and_normalize_teams.py

# Validate output
python3 scripts/teams/test_teams_data.py
```

## Maintenance

### Adding New Leagues

1. Edit `scripts/teams/leagues_seed.yaml` to add league and teams
2. Verify Wikidata QIDs and Wikipedia page titles
3. Run `fetch_and_normalize_teams.py`
4. Run `test_teams_data.py` and update expected counts
5. Update this README with new coverage statistics

### Updating Existing Teams

1. Edit the seed YAML (do not edit `teams.csv` directly)
2. Re-run the pipeline
3. Commit both seed and derived CSV

## Known Limitations

1. **Colors**: `colors_hex` column is blank (requires additional Wikidata resolution)
2. **Logos**: Sparse coverage (0% as of 2026-09-19)
3. **Country codes**: Some teams missing country (e.g., Dubai Basketball)
4. **Former names**: Limited coverage (~15%)

## Future Work

- [ ] Populate `colors_hex` from Wikidata P462 (requires color item resolution)
- [ ] Fetch logo URLs from Wikimedia Commons (via Wikidata P154)
- [ ] Expand to other leagues (ACB, LNB, etc.) — see roadmap
- [ ] Add team venue/arena data
- [ ] Add historical rosters or season records

## Related Documentation

- `LOGOS-README.md` — Logo fair-use policy
- `LOGOS-GAPS.md` — Logo coverage gaps
- `../../CHAPTER-MAP.md` — Connection to book manuscript
- `../../../scripts/teams/` — Pipeline scripts and seed data

## License

Team metadata is derived from Wikidata (CC0) and Wikipedia (CC-BY-SA). Team names, logos, and trademarks are property of their respective owners. Use of this data must comply with applicable trademark and copyright law.
