# Input spec: season CSV for decade_table.py

Status: proposal. Column names are my guess and must be matched against the real export. I have not seen the file.

## Source
Basketball-Reference season rows. The abs for WNKIH56T says they are the primary source for glen-w/hoops avg_game_by_decade. The CSV must be supplied by the researcher or Glen. Coder does not scrape.

## Minimum columns
- season (year or season label)
- one row per league-season
- per-game or total counting stats the chapter averages. The researcher picks the stats.

## Rules
- Decade bucket = floor(season end year / 10) * 10. State this in the output so readers can check the convention.
- Compute averages only from rows present in the CSV. Report n seasons per decade.
- Do not impute missing seasons. Leave them blank and list them.
- Output header must cite the CSV path and the ds path WNKIH56T.

## Open question for researcher
Is the intended average a mean of per-season league averages, or a games-weighted mean? The two can differ. Pick one before the table goes in the book.