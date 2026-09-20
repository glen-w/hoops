# NBA videogame ratings — seed sources (Phase 1)

**Access:** 2026-09-20 (Europe/Paris / PT)  
**Schema:** `game_title, year, season_field_hoopshype, player_name, overall_rating, certainty, source_url, access_date, notes`  
**Rows:** **97**  
**Rule:** no invented ratings; mark MEDIUM/UNCERTAIN where snapshot drift or missing season field.

## What was ingested

- 2k_stephen-curry.html: extracted 18 rating objs; url=https://www.hoopshype.com/nba-2k/players/stephen-curry/338365/
- 2k_giannis-antetokounmpo.html: extracted 14 rating objs; url=https://www.hoopshype.com/nba-2k/players/giannis-antetokounmpo/739957/
- 2k_kevin-durant.html: extracted 20 rating objs; url=https://www.hoopshype.com/nba-2k/players/kevin-durant/329525/
- 2k_lebron-james.html: extracted 24 rating objs; url=https://www.hoopshype.com/nba-2k/players/lebron-james/214152/
- 2k27_rankings.html: 21 unique player rows; url=https://www.hoopshype.com/nba-2k/players/?game=nba-2k27

## Primary sources

| Source | Role | URL |
|--------|------|-----|
| HoopsHype player 2K history pages | Multi-year overalls per star | e.g. https://www.hoopshype.com/nba-2k/players/lebron-james/214152/ |
| HoopsHype 2K27 rankings | Cross-sectional seed for one title | https://www.hoopshype.com/nba-2k/players/?game=nba-2k27 |
| HoopsHype “best average ratings” feature | Context only (averages not row-expanded here) | https://www.hoopshype.com/story/sports/nba/2026/08/23/players-best-average-ratings-nba-2k-history/82889930007/ |

Data parsed from publicly rendered `__NEXT_DATA__` JSON embedded in HoopsHype pages (access 2026-09-20). **Not affiliated with 2K Sports.** Community / media ratings databases can disagree with in-game patches.

## Certainty legend

| Tag | Meaning |
|-----|---------|
| HIGH | Player history page entry with season field present |
| MEDIUM | Rankings snapshot or history entry without season; subject to weekly patch drift |
| UNCERTAIN | Reserved for conflicting sources / Archive-only OCR (none in v1 seed beyond notes) |

## Expansion path (Phase 2+)

1. Walk HoopsHype `/nba-2k/players/` directory for full current roster history pages (respect rate limits; cache HTML).
2. Add archived title years (2K / Live / NBA Live) via Internet Archive + fandom wikis where tables are stable — tag UNCERTAIN.
3. Optional: nba2kapi.com (third-party; requires key) for bulk weekly snapshots — attribute 2kratings.com lineage.
4. Join keys later: normalize `player_name` → BRef slug / NBA person_id for real-life vs rating panels.
5. Do **not** scrape 2K Sports ToS-blocked surfaces; prefer published media tables + Archive.

## Live / older titles

**Not in v1 seed.** Expansion should add `game_franchise` column (`2K` vs `Live`) when those rows arrive.
