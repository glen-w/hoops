# Tasks 2–3: League Income Audit — Attendance & TV Revenue

**Status**: Scaffolding for researcher. Gaps: attendance 2018-19–2021-22 and per-team national TV revenue 2016-17–2023-24.

## Filing Convention

Use the same structure as `league_income_ingredients.csv`:
- **season**: e.g., 2018-19
- **category**: attendance_league_total | attendance_avg_per_game | local_media_revenue
- **value**: numeric
- **unit**: persons (attendance) | games (denominator) | USD (media revenue)
- **currency**: USD for media; blank for attendance
- **source_url**: direct link to source data or methodology
- **as_of**: access date (YYYY-MM-DD)
- **confidence**: HIGH (official/primary) | MEDIUM (secondary) | GAP
- **notes**: caveats, season disruptions (COVID), availability constraints

## Task 2: League Attendance 2018-19–2021-22

### Sources

| Season | Source | Notes |
|--------|--------|-------|
| 2018-19 | [ESPN NBA Attendance Report 2019](https://www.espn.com/nba/attendance/_/year/2019) | Per-team totals and averages available; 2018-19 was ticket-revenue record (~$1.67B) |
| 2019-20 | Basketball-Reference or ESPN 2020 | COVID-shortened season (72 games); check availability |
| 2020-21 | [ESPN NBA Attendance Report 2021](https://www.espn.com/nba/attendance/_/year/2021) | Pandemic restrictions; many teams had no or limited home attendance |
| 2021-22 | ESPN 2022 or Basketball-Reference | Likely available but not yet retrieved; verify full season data |

**Filing steps**:
1. Visit ESPN attendance pages for each season; record league total and average per game
2. Cross-check with Basketball-Reference (cite-scrape permitted; ~20 req/min; see hoopR::bref_* for package)
3. Note COVID impact in 2019-20 and 2020-21; distinguish "games played" from "games scheduled"
4. Add per-team breakdowns if chapter requires team-grain analysis

## Task 3: Per-Team National TV Revenue 2016-17–2023-24

### Sources

| Vintage | Source | Notes |
|---------|--------|-------|
| 2024 & 2023 | [Sportico NBA Valuation 2024](https://d3data.sportico.com/NBAValuations/NBAVal2024.html) | Includes media revenue (local TV/radio) by franchise; verify availability for 2016-17 start |
| 2023 | [Sportico NBA Valuation 2023](https://d3data.sportico.com/NBAValuations2023/NBAVal.html) | Franchise revenue mix; methodology documented |
| 2016-17–2022-23 | TBD | May require secondary sources (media reports, Bloomberg, sports business archives) |

**Filing steps**:
1. Access Sportico 2024 and 2023 valuations; extract per-team media revenue figures
2. Document methodology: Sportico defines "media" as local TV + radio (e.g., YES Network for Nets, WFAN)
3. For years before 2023, search:
   - Sports Business Journal / Bloomberg (subscription or library access)
   - Forbes annual NBA team valuations (cite-backed)
   - Team investor reports (if public)
4. Mark confidence MEDIUM if secondary-sourced; HIGH if from official broadcast partners

**Note**: National media (ABC/ESPN/TNT) is already in `league_income_ingredients.csv`. This task focuses on *local* media revenue only.

## Open Questions for Researcher

- Does the chapter require per-team TV revenue, or only league total?
- Should 2019-20 and 2020-21 attendance be listed separately from full-season averages (to show pandemic impact)?
- Are there prior Scrivener notes on Sportico access (subscription required)?

## Dependency

Both tasks can run in parallel. Task 4 (franchise efficiency source selection) is independent; awaiting researcher decision on Austin Vitelli, OregonLive, or component-build approach.
