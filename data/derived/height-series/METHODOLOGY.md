# NBA height series — methodology

**As of:** 2026-09-19  
**Primary source:** [https://runrepeat.com/height-evolution-in-the-nba](https://runrepeat.com/height-evolution-in-the-nba)  
**Author / page:** Dimitrije Curcic, RunRepeat — “70 Years of Height Evolution in the NBA [4,504 players analyzed]” (published Aug 31, 2021; page updated Apr 8, 2024).  
**Confidence:** **HIGH** for transcribed seasonal tables; **HIGH-MEDIUM** for position splits (era position labels).  
**Label:** SECONDARY (independent analysis of public roster/box data; not an NBA.com official publication).

## What we extracted

| File | Contents |
|------|----------|
| `nba_height_series.csv` | Long-form: league avg height, league avg weight, rookie avg height, position avg height (PG/SG/SF/PF/C), plus decade means |
| `nba_height_league_by_season.csv` | Slim: league average height only (one row per season) |

## Source scope (per RunRepeat)

- 4,504 NBA players; 24,841 player-season records; 69 seasons.
- Season label on the page is a single year (e.g. `2021`); we treat it as **season-end calendar year** and add `season_label` as `YYYY-YY` (e.g. `2020-21`).
- RunRepeat notes incomplete data for seasons before 1951/52 for some series; weight blanks for 1950–51 are omitted (not invented).
- Heights are published as feet/inches strings; we also provide `value_numeric` in inches (parsed, not remeasured).

## What we did **not** do

- No recomputation from Basketball-Reference player lists this pass (RunRepeat already cites BRef-class public data; BRef scrape deferred).
- No invented post-2021 seasons — series ends at season_end_year **2021** as published.
- Decade rows (`avg_height_league_decade_mean`) are **DERIVED** means of the published seasonal averages; marked in `notes`.

## Citation

Curcic, D. (2021/2024). *70 Years of Height Evolution in the NBA.* RunRepeat. https://runrepeat.com/height-evolution-in-the-nba (accessed 2026-09-19).
