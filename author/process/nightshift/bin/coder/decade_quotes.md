# Decade quotes (summary-sourced, unverified)

Source of every figure below: the qwen3.8 mirrored summary note, returned by hr hoops_summary. Both summaries are cut off mid-sentence. Nothing here is computed, fetched, or checked against full text. Do not cite in the manuscript until checked.

The two papers use different windows and leagues. Do not merge or average them.

## Wang and Zheng (2022): NBA only

Path: hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND

- Window: 2011-12 to 2020-21 regular seasons, ten seasons.
- Games per season: 1,059 to 1,230, depending on shortened schedules.
- Data: NBA shot chart API, pulled with Python. Trend test: Mann-Kendall, p < 0.05, run in Matlab 2020a.
- Field goals per game: about 163 (2011-12) to 177 (2020-21), upward trend, p < 0.001.
- Share of attempts from 24 ft and above: 22% to 39%, about +1.85 percentage points per year, p < 0.001.
- Share of attempts from 16-24 ft: 21% to about 7.2%, p < 0.001.
- Accuracy: rose significantly at every distance except 3-pointers, which stayed flat (p = 0.150).
- Restricted-area accuracy was above 60% in every season. Long-range accuracy stayed at 35-36%.
- Game flow: Q1 had the highest accuracy, and the last 3-minute segment of each quarter had the lowest. The 2nd and 4th segments of each quarter had the most attempts, and the 1st had the fewest.
- Authors' attributions: rule changes (clear-path foul), fatigue, and coaching emphasis.
- Limitations section: cut off in the summary, unread.

## Foteinakis and Pavlidou (2025): NBA vs EuroLeague

Path: hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7

- Window stated: 2012-13 to 2022-23, with 2019-20 excluded (pandemic).
- Sample: 14,688 games, made up of 12,150 NBA regular-season games and 2,538 EuroLeague games (regular season plus top-16).
- Sources: stats.nba.com and euroleague.net. Methods: Shapiro-Wilk, Mann-Whitney U, p < 0.05, run in JASP 0.19.
- Figures are shown as NBA vs EuroLeague.

| Metric | NBA | EuroLeague |
|---|---|---|
| 3PA/FGA % | 32.44 | 37.59 |
| 3PA per 100 poss | 27.94 | 32.79 |
| 2PA per 100 poss | 58.29 | 54.50 |
| 2P% | 51.11 | 52.90 |
| 3P% | 35.62 | 36.38 |
| eFG% | 52.14 | 53.95 |

- Trends: both leagues rose in efficiency and fell in 2PA per 100 possessions. The NBA's 3-point frequency grew faster and nearly closed the gap. The NBA's eFG% rise was steeper recently, and the EuroLeague was higher but more stable.
- The summary says some effect sizes were small. The effect-size values themselves were not returned.
- Authors' attributions (court dimensions and others): cut off in the summary.

## Flags

- Season count mismatch. The summary says nine seasons. 2012-13 to 2022-23 minus 2019-20 is ten seasons. 12,150 NBA games is not a multiple of 1,230, and it is not 9 or 10 full 1,230-game seasons. Check the full text for the real window and any exclusions.
- The Foteinakis figures are pooled across seasons, not per season. They cannot feed a per-season decade mean.
- The Wang figures are endpoints and trends only. They give no per-season table.

## Still needed (not done)

- Basketball-Reference season table (WNKIH56T), with URL and access date. The alternative is nba_api (9FJZPDKM).
- decade_means.py has not been run, so mean_of_means and games_weighted are still unreported.
- Read both full texts, then confirm the figures and read the limitations.
- Both hoops_bib queries from the previous pass returned nothing here. Retry with different terms.
