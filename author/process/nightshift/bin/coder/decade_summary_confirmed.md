# Decade figures confirmed against hoops_summary (2026-10-20)

Source level: mirrored paperful summaries (qwen3.8), NOT the PDFs. Both excerpts were cut off mid-sentence (Wang at Limitations, Foteinakis at contextual factors). Quote as 'per summary' until checked against the PDF.

## Wang and Zheng 2022 (NCQ6GJND)
Path: hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND

- Scope: NBA regular seasons 2011-12 to 2020-21. Data from the NBA shot chart API via Python. Games per season ranged 1,059 to 1,230.
- Shot distance categories: restricted area; <8 ft outside restricted area; 8-16 ft; 16-24 ft; 24 ft and above.
- Method: Mann-Kendall trend test, p < 0.05. Matlab 2020a. League-wide aggregates, not players.
- Field goals per game: about 163 (2011-12) to 177 (2020-21), p < 0.001.
- 3-pointer share (24 ft+): 22% to 39%, about +1.85 percentage points per year, p < 0.001.
- 16-24 ft share: 21% to about 7.2%, p < 0.001.
- Accuracy rose significantly at all distances except 3-pointers (p = 0.150, flat).
- Restricted-area accuracy above 60% every season. Long-range accuracy stayed at 35-36%.
- Q1 had the highest accuracy. The last 3-minute segment of each quarter had the lowest.
- Within each quarter, segments 2 and 4 had the most attempts and segment 1 the fewest.

Status of decade_quotes.md: the Wang entries match this summary where they overlap. Still unconfirmed as direct quotes, because there is no abstract and no PDF check. Use paraphrase with 'per summary'.

Check needed: 22% to 39% over 9 yearly steps is about 1.9 points per year. The summary says 1.85, probably a fitted slope (Sen's). Do not recompute it as an endpoint difference.

## Foteinakis and Pavlidou 2025 (E7QXTIF7)
Path: hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution Comparative Analysis of Shooting Trends and Offensive Efficiency in -- E7QXTIF7

- Scope: NBA vs EuroLeague, 2012-13 to 2022-23, 2019-20 excluded (pandemic).
- Games: 14,688 = 12,150 NBA regular season + 2,538 EuroLeague (regular season plus top-16). The sum checks.
- Sources: stats.nba.com and euroleague.net. Test: Mann-Whitney U (Shapiro-Wilk showed non-normality), JASP 0.19.
- 3PA/FGA%: EuroLeague 37.59 vs NBA 32.44.
- 3PA per 100 possessions: 32.79 vs 27.94.
- 2PA per 100 possessions: NBA 58.29 vs EuroLeague 54.50.
- 2P%: EuroLeague 52.90 vs NBA 51.11.
- 3P%: EuroLeague 36.38 vs NBA 35.62.
- eFG%: EuroLeague 53.95 vs NBA 52.14.
- Trends: NBA 3-point frequency grew faster and nearly closed the gap. NBA eFG% rose more steeply recently. Both leagues' 2PA per 100 possessions declined.

Inconsistency to resolve in the PDF: the summary says 'nine seasons', but 2012-13 through 2022-23 is eleven seasons, or ten after dropping 2019-20. Check the season count and whether 2020-21 and 2021-22 were handled differently before quoting the number of seasons.

The summary gives pooled means, not season-by-season values. Do not use them as a per-season series.

Status of foteinakis_summary_figures.md: the figures above match what that file should hold. Diff the file against this list before quoting.
