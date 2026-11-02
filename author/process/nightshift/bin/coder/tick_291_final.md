# Tick 291 final

## Result
- hoops_record error from tick 290 is avoided: hoops_list found all 3 target keys, and each has a summary (sm=true).
- 8VEP8FE8 Karamousalidis 2025 (Euroleague vs NCAA DI three-point shooting): 1 list hit, path matches.
- E7QXTIF7 Foteinakis 2025 (A Decade of Evolution): found. The surname query also returned LXB3FHHR (2025, explainable ML for EuroLeague) and SX6EB6GD (2026, home advantage). Neither is a target, so ignore them for the shooting-trend work.
- NCQ6GJND Wang 2022 (NBA shooting pattern and accuracy): found in hoops/_inbox. The surname query returned 11 hits, and the other 10 are unrelated.
- hoops_bib was queued but not returned this pass. Key existence is already confirmed by hoops_list, so it is not needed.
- No stats were read this tick, so none are used here.

## Next tick
1. Call hoops_summary for 8VEP8FE8, E7QXTIF7 and NCQ6GJND.
2. Write analysis notes only from the returned summary text.

## Open checks before use
- Foteinakis: the full text mentions both 9 and 10 seasons. Resolve this.
- Wang 163-177: check per-team vs combined stats, and attempts vs makes.
- Karamousalidis: Euroleague vs NCAA DI metrics only after a summary is returned.
- br_league_fetch.py: run where fetching is allowed. Log the URL and access date. Build rows.csv only from fetched values.
- Keep Table A and Table B separate.
