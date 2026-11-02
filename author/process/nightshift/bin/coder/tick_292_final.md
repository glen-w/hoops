# Tick 292 final

## Result
hoops_summary returned error `'path'` for all three keys. No summary text came back, so no numbers were read, used or invented.

- 8VEP8FE8 (Karamousalidis 2025, Euroleague vs NCAA DI three-point shooting): error 'path'
- E7QXTIF7 (Foteinakis 2025, A Decade of Evolution): error 'path'
- NCQ6GJND (Wang 2022, NBA shooting pattern and accuracy changes): error 'path'

## Likely cause
The error looks like a missing `path` field in the summary lookup. This is a guess, not confirmed. The earlier hoops_list found the keys and their summaries, so the failure is probably in how the query was passed (`q` with a bare key).

## Next tick
- Retry hoops_summary with `p` set to the exact pc path for each key instead of `q`.
- If that fails, use hoops_record per key, then hoops_bib.
- After a summary returns:
  - Foteinakis: resolve the 9 vs 10 season discrepancy and check per-team vs combined stats.
  - Wang pp. 163-177: check attempts vs makes.
  - Karamousalidis: extract Euroleague vs NCAA DI metrics from the summary only.

## Still open
- Run analysis/br_league_fetch.py where fetching is permitted. Log URL and access date. Build rows.csv from fetched values only.
- Keep Table A and Table B separate.
