# Tick 283 final

## Status
- hoops_summary results received for Foteinakis E7QXTIF7 and Wang NCQ6GJND. Both are summary excerpts (qwen3.8), not full text.
- br_league_fetch.py was NOT run. No URL or access date logged. No rows.csv built. No numbers computed.

## Foteinakis & Pavlidou 2025 (E7QXTIF7)
Quoted from the summary:
- Period: "a decade (2012-2013 to 2022-2023)".
- Data: "14,688 professional games: 12,150 NBA regular-season games and 2,538 EuroLeague games (regular season plus top-16 rounds) across nine seasons (2019-2020 was excluded due to pandemic disruptions)".
- Sources: stats.nba.com and euroleague.net.
- Tests: Shapiro-Wilk, then Mann-Whitney U, in JASP v0.19.

Checks:
- 12,150 + 2,538 = 14,688. The game counts are internally consistent.
- Season count is NOT resolved. The range 2012-13 to 2022-23 is 11 seasons. Excluding 2019-20 leaves 10. The summary says nine.
- Possible explanation, UNVERIFIED: the summary may have miscounted, or the paper may exclude a second season. Check the paper's methods section before citing a season count.
- Do not state "nine seasons" or "ten seasons" in the chapter until the paper text is checked.

League-level figures stated in the summary (pooled over the study period, as the summary reports them):
- 3PA/FGA%: EuroLeague 37.59 vs NBA 32.44
- 3PA per 100 poss: EuroLeague 32.79 vs NBA 27.94
- 2PA per 100 poss: NBA 58.29 vs EuroLeague 54.50
- 2P%: EuroLeague 52.90 vs NBA 51.11
- 3P%: EuroLeague 36.38 vs NBA 35.62
- eFG%: EuroLeague 53.95 vs NBA 52.14
- Summary notes some effect sizes were small. The excerpt is cut mid-sentence at "court dimensions, t".
- Whether these are means of per-game values or of per-season values is not stated in the excerpt. Check before labeling as Table A or Table B.

## Wang & Zheng 2022 (NCQ6GJND)
Quoted from the summary:
- Period: ten regular seasons, 2011-12 to 2020-21. Games per season "ranged from 1,059 to 1,230 ... depending on shortened schedules".
- Source: NBA shot chart API via Python. Trend test: Mann-Kendall, p < 0.05, Matlab 2020a.
- "The number of field goals per game increased from approximately 163 (2011-2012) to 177 (2020-2021), a statistically significant upward trend (p < 0.001)."
- 3-pointers (24 ft and above): 22% to 39%, about 1.85 percentage points per year.
- 16-24 ft share: 21% to about 7.2%.
- 3P accuracy flat (p = 0.150). Restricted-area accuracy above 60% every season. Long-range accuracy 35-36%.

Open on the 163-177 figure:
- The summary says "field goals per game". It does not say attempts or makes, and does not say one team or both teams.
- Inference, UNVERIFIED: a figure near 170 per game is too large for one team's makes and is more consistent with both teams' attempts combined. Confirm in the paper before using it.
- Until confirmed, write "field goals per game (basis not stated in summary)" and do not compare it with per-team numbers.

## Karamousalidis 8VEP8FE8
- Excerpt still truncated at CHAID. No tree results may be cited yet. Notes file analysis/karamousalidis_notes.md stays summary-only.

## Table rules
- Table A = mean_of_means. Table B = games_weighted. Keep separate and labeled.
- Foteinakis and Wang are literature figures, not our computed tables. Do not merge them into rows.csv.

## Next, in order
1. Run hoops_record or full-text check on E7QXTIF7: season count, and whether the league figures are per-game or per-season means.
2. Run hoops_record or full-text check on NCQ6GJND: attempts vs makes, and one team vs both teams for 163-177.
3. Pull the Karamousalidis excerpt past CHAID.
4. Run br_league_fetch.py. Log URL and access date. Build rows.csv from fetched values only.

## Rule
No invented basketball facts. Anything not in an hr output stays marked unverified.
