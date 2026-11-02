# Tick 265 final

Source: HR hoops_summary + hoops_record outputs only (qwen3.8 mirrored summaries). No page refs in them. The PDFs have not been checked.

## Foteinakis & Pavlidou 2025 (E7QXTIF7), NBA vs EuroLeague
- Games: 14,688 total = 12,150 NBA + 2,538 EuroLeague.
- Data: stats.nba.com and euroleague.net box scores. 2019-20 excluded (pandemic).
- Stats: Shapiro-Wilk, then Mann-Whitney U, p < 0.05, JASP 0.19.

### Season count: OPEN CONFLICT
- The summary says "nine seasons" and "2012-2013 to 2022-2023".
- That span is 11 seasons. Excluding 2019-20 leaves 10, not 9.
- Either the summary is wrong, or another season is also dropped (2020-21?).
- Do not write "ten" or "nine" in the chapter until the PDF methods section is read.

### Pooled league comparisons (EuroLeague vs NBA)
| Metric | EuroLeague | NBA |
|---|---|---|
| 3PA/FGA % | 37.59 | 32.44 |
| 3PA per 100 poss | 32.79 | 27.94 |
| 2PA per 100 poss | 54.50 | 58.29 |
| 2P% | 52.90 | 51.11 |
| 3P% | 36.38 | 35.62 |
| eFG% | 53.95 | 52.14 |

- Trend (qualitative): NBA 3-point frequency grew faster and nearly closed the gap. eFG% rose in both leagues. 2PA per 100 fell in both.
- Per-season 3PA/FGA values are NOT in the summary. They are still needed, with page or table refs.
- Some effect sizes were reported as small.

## Wang & Zheng 2022 (NCQ6GJND), NBA 2011-12 to 2020-21
- Ten regular seasons. Source: NBA shot chart API via Python. Games per season: 1,059 to 1,230.
- Distance bins: restricted area; <8 ft outside the restricted area; 8-16 ft; 16-24 ft; 24+ ft. Game split into 16 three-minute segments. Mann-Kendall trend test, Matlab 2020a.
- Field goals per game: about 163 (2011-12) to 177 (2020-21), p < 0.001.
- Share of attempts at 24+ ft: 22% to 39%, about +1.85 pp per year, p < 0.001.
- Share at 16-24 ft: 21% to about 7.2%, p < 0.001.
- Accuracy rose at all distances except 3PT (flat, p = 0.150). Restricted area > 60% every season. Long range 35-36%.
- Q1 had the highest accuracy. The last segment of each quarter had the lowest.

### pp.163-177: FGA or FGM?
- The summary only says "field goals per game".
- About 163-177 per game cannot be makes by one team. A typical NBA game has about 80-85 makes per team, and the summary frames the data as attempts by distance.
- The counts are therefore probably FGA, probably both teams combined. This is inference only. Confirm in the Wang PDF before citing.

## Caveats for Table A / Table B
- Foteinakis gives pooled means across seasons, not a per-season series (in the summary).
- Wang gives start and end endpoints only. Do not interpolate.
- Keep Table B (cross-league, from Foteinakis) apart from Table A (NBA by decade, from Basketball-Reference).

## Next
1. Read PDF methods and tables for Foteinakis (season list, per-season 3PA/FGA, page refs).
2. Read Wang for the FGA/FGM definition and the exact page.
3. Run analysis/br_league_fetch.py, then decade_means.py. Cite https://www.basketball-reference.com/ and the access date. Keep mean_of_means and games_weighted as separate columns.
