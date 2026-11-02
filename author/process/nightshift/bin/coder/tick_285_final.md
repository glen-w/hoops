# Tick 285 final

## Status
- Tick 284: hoops_record by key raised a 'path' error on all 3 keys.
- Tick 285: hoops_summary by title query raised the same 'path' error on all 3 queries (Foteinakis, Wang, Karamousalidis).
- Both hr routes fail the same way, so the fault is probably in the hr path lookup and not in the query form. This is unconfirmed.
- No paper text was read, so nothing is verified. No numbers invented.

## Not yet checked
1. Foteinakis: whether the season count is nine or ten, and whether the metric is per-game or per-season.
2. Wang pp.163-177: whether it covers one team or both, and what basis it uses.
3. Karamousalidis: the excerpt after CHAID, before any tree citation.
4. `analysis/br_league_fetch.py`: not run. Run it, log the URL and access date, and build `rows.csv` from fetched values only. Source: Basketball-Reference (ds WNKIH56T), scrape politely.
5. Keep Table A (mean_of_means) and Table B (games_weighted) separate.

## Next tick
- Try hoops_bib (local private/hoops_data/hoops_data.bib) or hoops_list. These are different routes and may avoid the 'path' error.
- If they also fail, report the hr 'path' fault to Glen and work on item 4. That needs no hr.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
- hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 -- E7QXTIF7
- hoops/_inbox/Wang - 2022 -- NCQ6GJND
- hoops/⭐game 🏀/offense 💥/Karamousalidis - 2025 -- 8VEP8FE8
