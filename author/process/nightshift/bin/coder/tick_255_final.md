# Tick 255 final (coder)

Source for every item below: the hr summaries (qwen3.8 mirrored notes). The PDFs were not read this tick.

## Foteinakis and Pavlidou 2025 (E7QXTIF7)
- Scope: NBA vs EuroLeague, 2012-2013 to 2022-2023.
- Games: 14,688 total. That is 12,150 NBA regular-season games and 2,538 EuroLeague games (regular season plus top-16 rounds).
- Stated as nine seasons, with 2019-2020 excluded for the pandemic.
- **Conflict still open.** An 11-season span minus the one excluded season gives 10, not nine. The summary does not list the seasons. Another season may also have been dropped, or the span or count may be misstated. Read the PDF methods and list the exact seasons before citing a season count.
- Data: stats.nba.com and euroleague.net box scores.
- Tests: Shapiro-Wilk showed non-normal distributions, so Mann-Whitney U was used (p < 0.05), in JASP 0.19.
- Reported league means:
  - 3PA/FGA: EuroLeague 37.59%, NBA 32.44%.
  - 3PA per 100 possessions: EuroLeague 32.79, NBA 27.94.
  - 2PA per 100 possessions: NBA 58.29, EuroLeague 54.50.
  - 2P%: EuroLeague 52.90, NBA 51.11.
  - 3P%: EuroLeague 36.38, NBA 35.62.
  - eFG%: EuroLeague 53.95, NBA 52.14.
- The summary says effect sizes were small for some metrics.
- The summary text was cut off mid-sentence in the contextual-factors passage, so limitations are not captured.

## Wang and Zheng 2022 (NCQ6GJND)
- Scope: NBA regular seasons 2011-2012 to 2020-2021, which is ten seasons.
- Data: NBA shot chart API via Python, with 1,059 to 1,230 games per season.
- Shot distance bins: restricted area; less than 8 ft outside the restricted area; 8-16 ft; 16-24 ft; 24 ft and above.
- Trend test: Mann-Kendall, p < 0.05, in Matlab 2020a.
- Reported results:
  - FG per game rose from about 163 to 177 (p < 0.001).
  - 24 ft and above rose from 22% to 39%, described as about 1.85 percentage points per year (p < 0.001).
  - 16-24 ft fell from 21% to about 7.2%.
  - 3-point accuracy was flat (p = 0.150) and stayed in the 35-36% range.
  - Restricted-area accuracy was above 60% in every season.
- **Slope estimator unconfirmed.** The summary names Mann-Kendall, which is a trend test and gives no slope. The 1.85/yr figure may come from Sen's slope, OLS or a simple endpoint calculation.
  - Check: (39 - 22) / 9 intervals = 1.89 pp/yr, not exactly 1.85, so 1.85 probably comes from a fitted slope.
  - Do not cite 1.85/yr as a Theil-Sen or OLS slope until the PDF confirms which.
- Limitations were cut off in the summary text. Read the PDF.

## Definition caveat
Wang's 24 ft and above share comes from shot-chart distance bins. BR 3PA/FGA counts three-point attempts. These differ, so do not compare them as like for like. Foteinakis uses 3PA/FGA, the same definition as BR. The NBA 3PA/FGA of 32.44% there is a multi-season mean, not an end-point value.

## Not done this tick
- `br_league_fetch.py` not run, so no BR URL or access date is recorded.
- `decade_means.py` not run, so `mean_of_means` and `games_weighted` are not reported.
- `hoops_bib` returned no output, so Foteinakis and Wang bib entries are not checked.

## Next tick
1. Read the Foteinakis PDF methods and list the seasons.
2. Read the Wang PDF for the limitations and the slope estimator.
3. Run `br_league_fetch.py` and record the URL and date.
4. Run `decade_means.py` and report both columns.
5. Put BR 3PA/FGA against Foteinakis's NBA 3PA/FGA, then separately against Wang's 22%-39%, labelling the definitions.
