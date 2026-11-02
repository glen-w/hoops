# Tick 274 final

## Done
- Wrote `analysis/decade_means.py`. It reads a rows CSV (season, games, metric_value, source) and prints mean_of_means and games_weighted separately. It has no embedded data and refuses rows with no source.
- Not run: no rows CSV exists yet.

## hr result
- `hoops_summary` (Foteinakis per-season 3PA/FGA): error `'path'`. No data returned.
- `hoops_record` (Wang 2022): error `'path'`. No data returned.
- Both failed the same way. The queries probably did not resolve to a record with a `path`. Next time, query by exact title or Zotero key instead (Foteinakis `E7QXTIF7`, Wang `NCQ6GJND`).

## Not done
- `br_league_fetch.py` has not been run. No URL or access date is logged, so there is no rows CSV.
- No Foteinakis per-season values, no Wang content, no computed numbers.

## Open
- Foteinakis season count conflict: the summary says 9 seasons, but 2012-13 to 2022-23 minus 2019-20 gives 10. Unverified until the paper text is read.
- Wang 163-177 stays unusable until the full text or notes are read.
- Table A and Table B stay separate. mean_of_means stays separate from games_weighted.

## Next
1. Retry hr with exact title or key for Foteinakis and Wang.
2. Run `br_league_fetch.py` and log the URL and access date.
3. Build rows.csv only from fetched or quoted values, then run `python3 -I decade_means.py rows.csv`.
