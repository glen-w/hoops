# Tick 258 final (coder)

## Status
- No scripts run this tick. No numbers added.
- Both `hoops_summary` requests (Foteinakis and Wang) failed. hr_out returned the error `'path'` for each, so there are no summaries and no PDF text.
- Likely cause: the query form did not resolve to a summary path. This is unconfirmed. Next tick, retry with `hoops_record` or `hoops_list` first to get the exact item path, then call `hoops_summary` with `p` set to that path.
- `analysis/br_league_fetch.py` and `decade_means.py` are still unrun. When run, cite the URL and access date.

## Open conflicts (unchanged)
1. Foteinakis season count: the window 2012-13 to 2022-23 minus 2019-20 gives 10 seasons, but the earlier summary says 9. Check the PDF methods for the exact season list before using either figure.
2. Foteinakis gives only pooled 3PA/FGA, with no per-season values. Table A can only compare pooled values until per-season data is found.
3. Wang's 24ft+ bin is not 3PA/FGA. Do not equate the two. Read the bin edges, the slope estimator behind 1.85/yr, and the limitations in the PDF.

## Table A: Basketball-Reference vs Foteinakis (blank until BR fetch is run)
| metric | BR value | BR season span | Foteinakis value | Foteinakis span | diff | note |
|---|---|---|---|---|---|---|
| 3PA/FGA (pooled) | TBD | TBD | TBD | TBD | TBD | report mean_of_means and games_weighted separately |
| FGA/game | TBD | TBD | TBD | TBD | TBD | |
| eFG% | TBD | TBD | TBD | TBD | TBD | |

## Table B: Basketball-Reference vs Wang (blank until BR fetch is run)
| metric | BR value | Wang value | bin or definition match? | note |
|---|---|---|---|---|
| 3PA share | TBD | TBD | no: Wang uses a 24ft+ distance bin | do not compare directly unless Wang reports 3P-line shots |
| yearly slope | TBD | 1.85/yr (estimator unconfirmed) | TBD | confirm the estimator in the PDF |

## Run order
1. `python3 -I analysis/br_league_fetch.py`: record the URL and access date.
2. `python3 -I analysis/decade_means.py`: report mean_of_means and games_weighted separately.
3. Retry the PDF reads with exact paths (see Status).
4. Fill tables A and B from the outputs and the PDF reads.
