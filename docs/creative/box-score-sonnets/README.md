# Box-Score Sonnets

A creative micro-pack blending the fixed form of the English sonnet (14 lines, iambic pentameter) with statistical narratives drawn from NBA history.

## Form

Each sonnet follows the traditional structure:
- 14 lines
- Iambic pentameter (10 syllables per line, alternating unstressed/stressed)
- ABAB CDCD EFEF GG rhyme scheme

## Data Discipline

**Hard constraint**: All numbers, percentages, and historical claims cite landed derived CSVs in this repository. No invented statistics. Each sonnet includes a citation footer pointing to:
- CSV path
- Row keys or cell references
- Date accessed

## Motifs

Common themes include:
- **arc** — The three-point revolution
- **height** — Physical evolution of players
- **pace** — Game tempo across eras
- **drought** — Scoring slumps and defensive dominance

See `motif_tags.csv` for the full mapping.

## Sources

All numbers drawn from:
- `data/derived/avg_game_by_decade.csv` — Decade-level league averages (1970s–2020s)
- `data/derived/avg_game_by_decade/sample_seasons.csv` — Landmark seasons
- `data/derived/height-series/nba_height_league_by_season.csv` — Player height evolution (1946–2021)
- `data/reference/nba_league_averages_by_season.csv` — Annual league stats (1979–2024)

## Background

These sonnets were created as a creative drop for the *Hoops* manuscript data sandbox. The form honors both the precision of box scores and the constraint-driven elegance of traditional poetry.
