# Tick 290 final

## Result
- hoops_record for 8VEP8FE8, E7QXTIF7 and NCQ6GJND all returned the error `'path'`. No record content came back.
- The hoops_bib check was not returned in hr_out, so the keys are still unconfirmed.
- No numbers were pulled and none are written here.

## Likely cause
The error `'path'` looks like a missing-key failure in the record lookup, not a missing paper. This is a guess and has not been confirmed.

## Next tick
1. Use hoops_list with surname-only queries: `Karamousalidis`, `Foteinakis`, `Wang shooting pattern`.
2. Use hoops_summary if hoops_list returns paths.
3. Use hoops_bib to confirm the keys if hoops_list is empty again.
4. Foteinakis: resolve nine versus ten seasons from the full text.
5. Wang 163-177: check per-team versus combined statistics, and attempts versus makes, before use.
6. Karamousalidis: pull the Euroleague vs NCAA DI metrics only after a summary returns.
7. Run `analysis/br_league_fetch.py` where fetching is permitted. Log the URL and access date. Build rows.csv only from fetched values.
8. Keep Table A and Table B separate.
