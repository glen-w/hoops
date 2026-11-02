# Tick 276 final

## hr results
- hoops_record (Foteinakis title query): error `'path'`. Same error as hoops_summary in ticks 274 and 275. The record call seems to need a `p` path, not a title query `q`.
- hoops_list (Wang title query): 0 items. The full-title query matched nothing. Try a shorter query such as `Wang 2022 shooting` or `NCQ6GJND`.
- hoops_bib (Foteinakis): no entry in hr_out. Result unknown.

## Computed
- Nothing. No source was read. No numbers were produced.

## Open items
1. Foteinakis 2025 gives 9 seasons in one place and 10 in another. Unresolved. Quote the passage with its location before using either number.
2. Wang 2022, pp. 163-177. Unresolved. Do not use until the full text or notes are read.
3. analysis/br_league_fetch.py has not been run. When it runs, log the URL and access date and build rows.csv from fetched values only.
4. Keep Table A and Table B separate. Keep mean_of_means separate from games_weighted.

## Next pass
- Call hoops_record with `p` set to the exact pc path, for example `hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7`. Do not use `q`.
- Call hoops_list with a short query or the key to get the Wang path. Then call hoops_summary with `p`.
- Call hoops_bib with a short author query, `Foteinakis` or `Wang`, and check that it returns.
- If hr keeps failing, run br_league_fetch.py, which does not depend on hr.
