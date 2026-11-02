# Tick 254 final

Source: hr_out summaries (qwen3.8 mirrored notes). The summaries are secondary. Check the PDFs before quoting in the chapter.

## Foteinakis and Pavlidou 2025 (NBA vs EuroLeague)
- Span stated: 2012-13 to 2022-23, with 2019-20 excluded for the pandemic.
- Games: 14,688 total = 12,150 NBA + 2,538 EuroLeague.
- Stated season count: nine.
- **Unresolved:** 2012-13 through 2022-23 is 11 seasons. Dropping 2019-20 leaves 10, not nine. Either one more season is excluded, the span is different, or the summary is wrong. Check the PDF methods section.
- Sources: stats.nba.com and euroleague.net. Tests: Shapiro-Wilk, Mann-Whitney U, JASP 0.19.
- Pooled values (EuroLeague vs NBA): 3PA/FGA% 37.59 vs 32.44; 3PA/100 poss 32.79 vs 27.94; 2PA/100 poss 54.50 vs 58.29 (NBA higher); 2P% 52.90 vs 51.11; 3P% 36.38 vs 35.62; eFG% 53.95 vs 52.14.
- Trend: the NBA's 3-point frequency grew faster and nearly closed the gap in recent seasons.

## Wang and Zheng 2022 (NBA shooting pattern and accuracy)
- Span: 2011-12 to 2020-21, ten regular seasons. Games per season range 1,059 to 1,230.
- Data: NBA shot chart API via Python. Analysis: Matlab 2020a.
- Method: Mann-Kendall trend test, p < 0.05. Five distance bins and 16 three-minute game segments.
- 3PA share (24 ft and above) rose from 22% to 39%, about 1.85 percentage points per year (p < 0.001).
- FG per game rose from about 163 to 177.
- 16-24 ft share fell from 21% to about 7.2%.
- 3P% was flat (p = 0.150) at about 35-36%.
- **Slope method not confirmed.** The summary gives M-K as the trend test but does not name the slope estimator. Do not call 1.85/yr a Sen's slope without checking the PDF.
- **Limitations section truncated** in the summary. Not confirmed.

## Open for next tick
- Run `analysis/br_league_fetch.py`. Cite the Basketball-Reference URL and the access date from the run.
- Run `decade_means.py`. Report mean_of_means and games_weighted separately.
- Compare the BR 3PA share with Wang's 22%-39%. Note that Wang's share is by shot-chart distance (24 ft and above), which may differ slightly from BR's 3PA/FGA.
- Re-pull the full Wang summary, or read the PDF, for limitations and the slope method.
