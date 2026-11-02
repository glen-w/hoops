# Tick 284 final

Status: no fetch, no compute. All three hoops_record calls (E7QXTIF7, NCQ6GJND, 8VEP8FE8) returned the error 'path'. No record text was received.

## Still unverified
- Foteinakis E7QXTIF7: the summary says 9 seasons, but the range implies 10. It is also unclear whether the league figures are per-game or per-season averages.
- Wang NCQ6GJND, pp. 163-177: unclear whether the 163-177 figure is for one team or both, and what its basis is. Treat any such inference as unverified.
- Karamousalidis 8VEP8FE8: the excerpt after CHAID has not been read. Do not cite the trees yet.

## Next
- Retry hoops_record using hoops_summary or a title query instead of the bare key, since the key lookup raised 'path'.
- If the retry fails again, flag the hoops_record tool for Glen. Do not ask for data.
- Run analysis/br_league_fetch.py. Log the URL and access date. Build rows.csv only from fetched values.
- Keep Table A (mean_of_means) and Table B (games_weighted) separate.

## Sources
- hoops/data sources/Unknown - n.d. - Basketball-Reference -- WNKIH56T
