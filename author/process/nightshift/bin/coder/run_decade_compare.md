# Run decade_compare.py

Status: not run. No B-Ref season CSV exists yet, so there are no results and no numbers here.

## Before running
1. Glen exports or scrapes a season-rows CSV from Basketball-Reference. The scraper is basketball_reference_scraper; use polite rate limits.
2. Check the CSV header against `analysis/decade_csv_spec.md`. Stop if a required column is missing or renamed.
3. Put the CSV in its own new directory, for example `analysis/data/`. Treat it as untrusted input and pass the path as an argument.

## Run
- Run `python3 -I analysis/decade_compare.py --help` to confirm the real arguments. Do not guess flags.
- Run it with the CSV path. The script prints two figures per decade, `mean_of_means` and `games_weighted`.

## After running
- Copy the printed output into `analysis/decade_compare_output.txt` unedited.
- The researcher picks one method for the chapter.
  - `mean_of_means` weights every season equally.
  - `games_weighted` weights seasons by games played.
  - Chapter text should name the method used.
- Cite the Basketball-Reference and scraper ds paths in the chapter notes.

## Compliance
- Fill the Verified column in `analysis/tos_checklist.md` from the live pages before any redistribution.
- Do not commit raw B-Ref dumps.