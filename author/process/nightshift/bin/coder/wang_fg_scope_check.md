# Wang 2022 FG/game scope check

Status: open, blocked.

Question: is the 163 to 177 field goals per game figure per team or a per-game league total?

Known: coverage is league-wide, all NBA games, 2011-12 to 2020-21. The earlier summary gives no per-team breakdown.

Not known: the unit of the 163 to 177 figure.

Blocker: the hoops_summary call for Wang returned error 'path' on final_tick. No summary text came back, so the unit is still unconfirmed. The hoops_record call for Foteinakis failed the same way.

Next: retry hoops_summary with the exact ds path as q, `hoops/_inbox/Wang - 2022 - What are the changes in basketball shooting pattern and accuracy in National Basketball -- NCQ6GJND`. If it fails again, try hoops_bib. Do not use the 163 to 177 figure in any table until the unit is confirmed from the text.

Related: Table A (mean_of_means) and Table B (games_weighted) stay separate. br_league_fetch.py is still unrun. rows.csv is built only from fetched values, with the URL and access date logged.
