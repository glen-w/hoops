# Team Logos — Coverage Gaps

**As of**: 2026-09-19  
**Scope**: EuroLeague (men) + EuroLeague Women

## Summary

| League | Teams | Logos Populated | Coverage |
|--------|------:|----------------:|---------:|
| EuroLeague (men) | 20 | 0 | 0% |
| EuroLeague Women | 22 | 0 | 0% |
| **Total** | **42** | **0** | **0%** |

## Status

Logo population is **deferred** to a follow-up task. The initial P0c implementation focuses on:
1. ✅ Seed data with Wikidata QIDs
2. ✅ Fetch and normalize team metadata (country, founding year, etc.)
3. ✅ Schema lock for teams.csv
4. ⏸️ Logo URLs (to be populated)

## Next Steps

1. Create `scripts/teams/fetch_logos_from_commons.py` script to:
   - Query Wikidata P154 (logo image) for each team
   - Resolve Wikimedia Commons URLs
   - Verify SVG availability
   - Write to `logos.csv`

2. Manual verification:
   - Check licensing for each logo
   - Document fair-use references where Commons is unavailable
   - Prioritize SVG over raster formats

3. Update coverage statistics in this file

## Known Challenges

- **Wikimedia Commons coverage**: Not all basketball team logos are available on Commons
- **Licensing**: Many team logos are copyrighted with no open license
- **Format preference**: SVG preferred, but not always available
- **Name variations**: Team names may differ across Wikidata and Commons

## Policy Reminder

We **do not** download or host copyrighted logos in this repository. `logos.csv` contains **URL references only** for fair-use purposes.
