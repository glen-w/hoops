# NBA League Averages by Season: Source Citation

## File

`nba_league_averages_by_season.csv`

## Source

**Basketball-Reference.com**  
https://www.basketball-reference.com/

**Owner:** Sports Reference LLC

## Description

League-wide per-game averages for NBA regular seasons from 1979-80 through 2023-24. Each row represents the mean statistics across all NBA teams for a given season.

## Coverage

- **Seasons:** 1979-80 through 2023-24 (45 seasons)
- **Start year:** 1979-80 (first season with three-point line)
- **Statistics:** Field goals, three-pointers, free throws, rebounds, assists, steals, blocks, turnovers, fouls, points

## License and Redistribution

**License:** Public NBA statistics  
**Redistribution:** Permitted with attribution to Basketball-Reference.com  
**Commercial Use:** Permitted (public statistics)

Basketball-Reference.com makes season-level aggregate statistics freely available for public use. This CSV compiles publicly available data and may be redistributed with proper attribution.

## Compilation Method

Data was compiled from Basketball-Reference.com's league average pages. Each season's statistics represent:

1. **Per-game averages:** Team statistics divided by games played
2. **League-wide means:** Average across all NBA teams
3. **Regular season only:** Playoff games excluded

## Data Quality

- **Accuracy:** Direct transcription from Basketball-Reference.com
- **Completeness:** All regular seasons from 1979-80 through 2023-24
- **Validation:** 2023-24 values match published Basketball-Reference.com league averages

## Attribution Requirements

When using or redistributing this data, please credit:

> NBA season statistics from Basketball-Reference.com  
> Sports Reference LLC

## Related Files

- **Derived table:** `data/derived/avg_game_by_decade.csv`
- **Methodology:** `data/derived/avg_game_by_decade_methodology.md`
- **Transform script:** `scripts/build_avg_game_by_decade.py`

## Notes

- Three-point statistics only available from 1979-80 onward (introduction of three-point line)
- 2020-21 season shortened to 72 games (COVID-19) - included without adjustment
- All statistics are per-game averages, not season totals

---

**Compiled:** 2026-09-19  
**Compiler:** Hoops data sidecar repository  
**For:** *Hoops: An Uncommon Field Guide to Basketball*
