# Tick 260 final

## hr results
- hoops_list q=Foteinakis: 3 items (E7QXTIF7 decade paper; LXB3FHHR EuroLeague ML; SX6EB6GD home advantage). Only E7QXTIF7 is relevant to Table A.
- hoops_list q=Wang 2022: 0 items again. Wang is in hoops/_inbox, NCQ6GJND.
- hoops_summary E7QXTIF7: returned, but the excerpt is truncated mid-sentence ("court dimensions, t...").
- hoops_record NCQ6GJND: returned title and year 2022 only. abs is empty, so no Wang numbers are available.
- hoops_bib: no result returned this tick. Retry.

## Foteinakis & Pavlidou 2025 (E7QXTIF7): pooled figures from the summary excerpt
Source: mirrored paperful-summary note (qwen3.8 summary), not the PDF. Verify against the paper before quoting.

- Scope: NBA vs EuroLeague, 2012-13 to 2022-23, 14,688 games (12,150 NBA regular season; 2,538 EuroLeague regular season plus top-16).
- Season count: the summary says nine seasons, with 2019-20 excluded. The 2012-13 to 2022-23 span is 11 seasons, so excluding only 2019-20 would leave 10. This conflicts and is unresolved. Check the paper for which seasons were dropped (possibly 2020-21 as well).
- Test: Mann-Whitney U, p < 0.05, JASP 0.19.

| metric | NBA | EuroLeague |
|---|---|---|
| 3PA/FGA % | 32.44 | 37.59 |
| 3PA per 100 poss | 27.94 | 32.79 |
| 2PA per 100 poss | 58.29 | 54.50 |
| 2P% | 51.11 | 52.90 |
| 3P% | 35.62 | 36.38 |
| eFG% | 52.14 | 53.95 |

These are decade-pooled league values. The excerpt gives no per-season values. Table A needs per-season 3PA/FGA from the paper's figures or tables.

## Table A (BR vs Foteinakis)
Still blank. Only pooled NBA 3PA/FGA 32.44% is available. Per-season BR values cannot be compared until the Foteinakis per-season series is read. Keep BR mean_of_means separate from games_weighted. The pooled value is likely closer to a games-weighted figure, but the paper does not say, so do not assume it.

## Table B (BR vs Wang)
Blank. No numbers retrieved. Bin edges, the slope estimator behind 1.85/yr, and limitations are all unread. The 24ft+ bin is not 3PA/FGA.

## Next
1. Retry hoops_bib q=Foteinakis.
2. Call hoops_summary on NCQ6GJND. Wang is in _inbox and may have no summary note. If none exists, find the Zotero attachment path.
3. Resolve the Foteinakis season count.
4. Run br_league_fetch.py, then decade_means.py. Cite the BR URL and access date.
