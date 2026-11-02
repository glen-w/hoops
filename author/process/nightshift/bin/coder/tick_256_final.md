# Tick 256 final (coder)

All figures below come from the hr_out summaries. Nothing was run this tick.

## Foteinakis & Pavlidou 2025 (E7QXTIF7)
- Span: 2012-13 to 2022-23. 2019-20 excluded for the pandemic.
- The paper states nine seasons. Span minus 2019-20 gives 10.
- Games: 12,150 NBA and 2,538 EuroLeague, 14,688 total.
- **Inference, not from the paper:** 12,150 = 9 x 1,230 + 1,080. That equals nine full 82-game seasons plus the shortened 2020-21 season. The game count therefore fits 10 NBA seasons, not nine. This assumes 1,230 games per full season and 1,080 for 2020-21, both from my memory of the NBA schedule, so check them against BR. The summary does not list the seasons. Confirm in the PDF methods before citing "nine".
- Reported means, NBA vs EuroLeague:
  - 3PA/FGA%: 32.44 vs 37.59
  - 3PA per 100 possessions: 27.94 vs 32.79
  - 2PA per 100 possessions: 58.29 vs 54.50
  - 2P%: 51.11 vs 52.90
  - 3P%: 35.62 vs 36.38
  - eFG%: 52.14 vs 53.95
- Method: Shapiro-Wilk, then Mann-Whitney U, in JASP 0.19. Data from stats.nba.com and euroleague.net.

## Wang & Zheng 2022 (NCQ6GJND)
- Span: ten regular seasons, 2011-12 to 2020-21. Data from the NBA shot chart API, 1,059 to 1,230 games per season.
- Field goals per game: about 163 to 177 (p < 0.001).
- 3-pointers (24 ft and above), as a share of FGA: 22% to 39%, about 1.85 pp per year (p < 0.001). The share is shot-chart based, so its definition differs from BR 3PA/FGA.
- 16-24 ft share: 21% to about 7.2%.
- 3P accuracy flat at 35-36% (p = 0.150).
- Test: Mann-Kendall, a trend test. **The summary does not name the estimator behind 1.85/yr.** A rough check, (39-22)/9 = 1.89, is close but proves nothing about the method. The excerpt is cut off again at Limitations.

## Still open
1. Foteinakis: read the PDF methods for the exact season list.
2. Wang: read the PDF for the slope estimator and the limitations.
3. hoops_bib returned no entries. Retry with narrower queries, e.g. a DOI or a title fragment.
4. Run br_league_fetch.py and record the URL and access date.
5. Run decade_means.py. Report mean_of_means and games_weighted as separate columns.
6. Make two comparisons in separate tables: BR 3PA/FGA vs Foteinakis NBA 3PA/FGA, and BR 3PA/FGA vs Wang's 22-39% shot-chart share.

## Sources (pc)
- Foteinakis 2025, E7QXTIF7
- Wang 2022, NCQ6GJND
- Basketball-Reference, WNKIH56T
