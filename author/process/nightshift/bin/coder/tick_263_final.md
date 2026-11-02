# Tick 263 final

## Sources
- Foteinakis and Pavlidou 2025, hoops/⭐game 🏀/offense 💥/Foteinakis - 2025 - A Decade of Evolution ... -- E7QXTIF7. Figures below come from the hoops_summary excerpt (qwen3.8 mirrored note), not the PDF. The excerpt is truncated after "Contextual factors".
- Wang 2022, hoops/_inbox/Wang - 2022 - ... -- NCQ6GJND. hoops_record returned an empty abstract and no attachment path. Nothing was verified.
- Basketball-Reference (https://www.basketball-reference.com/). Not fetched this tick.

## Table A: Foteinakis pooled NBA vs EuroLeague (2012-13 to 2022-23, 2019-20 excluded)

These are pooled values for the whole period. The excerpt has no per-season values.

| Metric | NBA | EuroLeague |
|---|---|---|
| Games | 12,150 | 2,538 |
| 3PA/FGA % | 32.44 | 37.59 |
| 3PA per 100 poss | 27.94 | 32.79 |
| 2PA per 100 poss | 58.29 | 54.50 |
| 2P% | 51.11 | 52.90 |
| 3P% | 35.62 | 36.38 |
| eFG% | 52.14 | 53.95 |

Other items from the summary:
- Total games: 14,688.
- Source pages: stats.nba.com and euroleague.net.
- Test: Mann-Whitney U, p < 0.05, in JASP 0.19.
- Trend claims: the NBA 3-point frequency grew faster, and both leagues' 2PA per 100 possessions declined.
- Per-season 3PA and FGA: TBD.
- Cells not listed in the excerpt (2PM, 3PM, 3PM/FGM%): TBD.

## Season count dispute (nine vs ten)
- The summary text says "nine seasons".
- The span 2012-13 to 2022-23 has 11 seasons. Excluding 2019-20 leaves 10.
- NBA games: 12,150 = 9 x 1,230 + 1,080. That matches ten seasons if the one 1,080-game season is 2020-21.
- I derived this by arithmetic. It is not stated in the excerpt.
- Provisional reading: ten seasons, and the summary's "nine" looks like a summarizer error.
- Settle it from the PDF's per-season table.

## Wang 163-177 FG per game (FGA or FGM?)
- Open. The Wang record has no abstract or attachment path, so I could not check it.
- Reference points: 163-177 is far above any NBA team's makes per game, which are roughly 38-42 per team and so about 80 combined. That is my background knowledge, not a cited figure. It is only a hint that the number may be a different quantity, such as combined or per-100 values.
- Do not cite Wang's number until it is read from the PDF with a page reference.

## Table B: Basketball-Reference decade means
All cells are TBD. Nothing was fetched.
- Run `analysis/br_league_fetch.py`, then `decade_means.py`.
- Cite the URL and the access date.
- Keep `mean_of_means` separate from `games_weighted`.

## Do not
- Do not merge Table A and Table B.
- Do not put any number in a table without a cited source.
