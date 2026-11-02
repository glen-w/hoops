# Tick 268 final

Source caveat: every figure below comes from the mirrored paperful summaries (qwen3.8). They are not read from the papers. Both excerpts were cut off mid-sentence. Check each figure against the PDF before it goes in the chapter.

## Foteinakis & Pavlidou 2025 (E7QXTIF7)
Summary-level figures (NBA vs EuroLeague, pooled over the study period):

| Metric | NBA | EuroLeague |
|---|---|---|
| 3PA/FGA % | 32.44 | 37.59 |
| 3PA per 100 poss | 27.94 | 32.79 |
| 2PA per 100 poss | 58.29 | 54.50 |
| 2P% | 51.11 | 52.90 |
| 3P% | 35.62 | 36.38 |
| eFG% | 52.14 | 53.95 |

- Games: 14,688 total = 12,150 NBA + 2,538 EuroLeague. NBA: regular season. EuroLeague: regular season plus top-16.
- Sources: stats.nba.com and euroleague.net. Tests: Mann-Whitney U, JASP 0.19.
- Per-season 3PA and FGA are NOT in the excerpt. Open the PDF and record the page and table number for each.

### Season count discrepancy: nine vs ten
- The summary says 'nine seasons'. It also gives the span as 2012-13 to 2022-23 with 2019-20 excluded.
- That span is 11 seasons. Minus 2019-20 leaves 10.
- Cross-check on the NBA game count (my arithmetic, not from the paper): 12,150 = 9 x 1,230 + 1,080. That fits ten seasons, with one shortened season of 1,080 games. Nine full seasons would be 11,070.
- Working position: ten seasons, and 'nine' is probably a summary error. Confirm from the paper's methods section and tables. Do not publish either count until then.

## Wang & Zheng 2022 (NCQ6GJND)
- Ten regular seasons, 2011-12 to 2020-21. Source: NBA shot chart API via Python. Test: Mann-Kendall, Matlab 2020a.
- 'Field goals per game' rises from about 163 to about 177 (p < 0.001).
- 163-177 is almost certainly FGA, not FGM. It is a per-game league total, and I infer it covers both teams. FGM per game would be far lower. Confirm the paper's wording, the unit (per game or per team) and the table or figure.
- Share of attempts from 24 ft and above: 22% to 39%, about +1.85 percentage points per year.
- Share from 16-24 ft: 21% to about 7.2%.
- Accuracy: rises at every distance except 3-pointers (flat, p = 0.150). Restricted area is above 60% in every season. Long range stays at 35-36%.
- Quarter pattern: Q1 is the most accurate. The last 3-minute segment of each quarter is the least accurate.
- Per-season games: 1,059 to 1,230 (from summary).

## Next tick
1. Run analysis/br_league_fetch.py, then decade_means.py. Cite https://www.basketball-reference.com/ and the access date.
2. Keep mean_of_means and games_weighted separate. Keep Table B apart from Table A.
3. Do not merge Wang's 3PA share (shot-chart distance, 24 ft+) with Foteinakis's 3PA/FGA (box score) without a definition note.