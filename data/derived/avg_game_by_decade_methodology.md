# Average Game by Decade: Methodology

## Overview

This dataset provides average per-game NBA statistics aggregated by decade, from the 1970s (1979-80 season) through the 2020s (through 2023-24 season).

## Source Data

**Primary Source:** Basketball-Reference.com league-wide per-game averages  
**Coverage:** 1979-80 through 2023-24 seasons (45 seasons total)  
**License:** Public NBA statistics, freely redistributable with attribution

Season-level source data committed to: `data/reference/nba_league_averages_by_season.csv`

## Methodology

### 1. Season-Level Data Collection

League-wide per-game averages were compiled from Basketball-Reference.com, representing the mean statistics across all NBA teams for each season. Each season row represents:

- **Per-game averages:** Team statistics divided by games played
- **League-wide:** Mean across all teams (not per-player)
- **Regular season only:** Playoff games excluded

### 2. Decade Assignment

Seasons are assigned to decades based on their **start year**:

- 1979-80 → 1970s
- 1980-81 through 1989-90 → 1980s  
- 1990-91 through 1999-00 → 1990s
- 2000-01 through 2009-10 → 2000s
- 2010-11 through 2019-20 → 2010s
- 2020-21 through 2023-24 → 2020s

**Note:** The 1970s contains only one season (1979-80) as three-point data is unavailable for earlier years. The 2020s is incomplete (4 seasons as of 2024).

### 3. Decade-Level Aggregation

For each decade, statistics are computed as the **arithmetic mean** of all seasons within that decade.

Example:
```
1980s FGA = mean(1980-81 FGA, 1981-82 FGA, ..., 1989-90 FGA)
```

This produces decade-level averages representing typical per-game statistics for that era.

### 4. Rounding

- **Counting stats** (FGA, FG3A, FTA, rebounds, assists, etc.): Rounded to 1 decimal place
- **Percentages** (FG%, FG3%, FT%): Rounded to 3 decimal places

## Statistics Included

| Stat | Description |
|------|-------------|
| `fga` | Field goal attempts per game |
| `fg_pct` | Field goal percentage |
| `fg3a` | Three-point attempts per game |
| `fg3_pct` | Three-point percentage |
| `fta` | Free throw attempts per game |
| `ft_pct` | Free throw percentage |
| `oreb` | Offensive rebounds per game |
| `dreb` | Defensive rebounds per game |
| `reb` | Total rebounds per game |
| `ast` | Assists per game |
| `stl` | Steals per game |
| `blk` | Blocks per game |
| `tov` | Turnovers per game |
| `pf` | Personal fouls per game |
| `pts` | Points per game |

## Key Observations

- **Three-point evolution:** FG3A increased from 2.8 (1970s) to 35.0 (2020s)
- **Pace changes:** Points per game ranged from 99.8 (2000s) to 109.1 (1980s)
- **Free throws decline:** FTA decreased from 29.2 (1980s) to 21.9 (2020s)
- **Shooting efficiency:** FG% relatively stable (~0.45-0.49) despite style changes

## Reproducibility

Regenerate the derived table at any time:

```bash
uv run python scripts/build_avg_game_by_decade.py
```

The script reads `data/reference/nba_league_averages_by_season.csv` and writes `data/derived/avg_game_by_decade.csv`.

## Attribution

**Data Source:** Basketball-Reference.com  
**Compiler:** Sports Reference LLC  
**Availability:** Public NBA statistics  

When citing this derived table, credit:
- Basketball-Reference.com for season-level data
- This repository for decade-level aggregation

## Limitations

1. **1970s incomplete:** Only 1979-80 season included (three-point line introduction)
2. **2020s incomplete:** Only 4 seasons (2020-21 through 2023-24) as of dataset compilation
3. **Team-level averages:** Not player-level or game-level detail
4. **Regular season only:** Playoff statistics excluded
5. **COVID-19 impact:** 2020-21 season (72 games) included without adjustment

## Version History

- **2026-09-19:** Initial compilation covering 1979-80 through 2023-24

---

**Last Updated:** 2026-09-19  
**Script:** `scripts/build_avg_game_by_decade.py`  
**Output:** `data/derived/avg_game_by_decade.csv`
