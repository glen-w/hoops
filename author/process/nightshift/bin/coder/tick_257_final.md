# Tick 257 final: Foteinakis and Wang vs Basketball-Reference

## Status
- No scripts were run. The bib searches returned nothing usable. The two summaries came back, but both were cut off.
- Nothing here is a computed result. Every number below is quoted from a paper summary and still needs checking against the PDF.

## Foteinakis and Pavlidou (2025): NBA vs EuroLeague
Quoted from the summary:
- Window: 2012-13 to 2022-23, with 2019-20 excluded.
- Data: 12,150 NBA games and 2,538 EuroLeague games, 14,688 in total.
- Source: stats.nba.com and euroleague.net.
- NBA 3PA/FGA: 32.44%. EuroLeague: 37.59%. These are pooled values over the window.
- NBA 3PA per 100 possessions: 27.94. EuroLeague: 32.79.
- NBA 2PA per 100 possessions: 58.29. EuroLeague: 54.50.
- 2P%: NBA 51.11, EuroLeague 52.90. 3P%: NBA 35.62, EuroLeague 36.38. eFG%: NBA 52.14, EuroLeague 53.95.
- Method: Mann-Whitney U, because Shapiro-Wilk found non-normal data. Analysis in JASP 0.19.

### Conflict to resolve: nine seasons or ten
- The summary says "nine seasons". The stated window, 2012-13 to 2022-23, is 11 seasons. Dropping 2019-20 leaves 10.
- 12,150 games = 9 x 1,230 + 1,080, which also fits 10 seasons, if one of them is the shortened 2020-21 season.
- Both readings point to ten seasons, so "nine" is probably a summary error or a paper typo. Confirm in the PDF methods.
- Check the per-season NBA game counts against BR. Do not assume the 1,230 and 1,080 figures.
- Check whether the paper also drops 2020-21 or any other season. The summary does not say.
- The 3PA/FGA values are pooled over the window. They are not season values. Table A below needs the paper's per-season table or figure.

## Wang and Zheng (2022): NBA shot chart patterns
Quoted from the summary:
- Window: 2011-12 to 2020-21, ten regular seasons, 1,059 to 1,230 games per season.
- Source: the NBA shot chart API, pulled with Python.
- Method: Mann-Kendall trend test, p < 0.05, in Matlab 2020a.
- FG per game: about 163 rising to 177 (p < 0.001).
- Share of attempts from 24 ft and above: 22% rising to 39%, about 1.85 percentage points per year (p < 0.001).
- Share from 16-24 ft: 21% falling to about 7.2%.
- 3P accuracy was flat (p = 0.150), staying in the 35-36% range. Restricted-area accuracy was above 60% in every season.

### Cautions
- Wang's bin is distance-based: 24 ft and above. The corner three is 22 ft, so this bin is not the same as 3PA/FGA. Corner threes fall into the 16-24 ft bin. Do not put Wang's 22% and 39% next to BR 3PA/FGA as if they were the same quantity. Confirm the bin edges and any court-zone handling in the PDF.
- The summary does not name the estimator behind 1.85 per year. Arithmetic: (39 - 22) / 9 = 1.89, which is close to 1.85. That is consistent with a Sen slope or a regression slope, but it does not identify either. Read the methods before citing it as one.
- The limitations section was cut off again. Read it from the PDF.

## Table A: BR vs Foteinakis, NBA 3PA/FGA
| season | BR 3PA/FGA | Foteinakis | diff |
|---|---|---|---|
| fill from br_league_fetch.py output | | fill from the paper's per-season table | |

Rules:
- Cite the BR URL and the access date.
- Use only the seasons the paper covers. Settle the nine-vs-ten question first.
- Pooled-window check: the paper's 32.44% is one pooled number. Compare it to the BR games-weighted value over the same seasons, not the unweighted mean of season rates. Report `mean_of_means` and `games_weighted` from decade_means.py separately.

## Table B: BR vs Wang, shot-chart share
| quantity | BR | Wang | note |
|---|---|---|---|
| first season | | 22% (24 ft and above) | definition differs from 3PA/FGA |
| last season | | 39% (24 ft and above) | definition differs from 3PA/FGA |

Rules:
- Keep Table B separate from Table A.
- Wang's trend is the ten seasons 2011-12 to 2020-21.
- Only compare the endpoints after the bin definition is confirmed. The difference may be real, because corner threes are excluded from Wang's 24 ft and above bin.

## Next
1. Read the Foteinakis PDF methods for the season list and per-season counts.
2. Read the Wang PDF for the bin edges, the slope estimator, and the limitations.
3. Run `python3 -I analysis/br_league_fetch.py` and record the URL and access date.
4. Run decade_means.py and report the two means separately.
5. Fill Tables A and B.
