# Methodology — average NBA game by decade

**Artifact:** `data/derived/avg_game_by_decade/`  
**Access date:** 2026-09-20  
**Status:** thickened cite-backed table (not landmark-only)

## Sources

- Basketball-Reference, *League Average Per Game* (NBA/BAA):  
  https://www.basketball-reference.com/leagues/NBA_stats_per_game.html  
- Companion landmark sample retained from prior light pin (`sample_seasons_landmarks.csv`) for chapter storytelling only.

## Schema

### `nba_league_averages_by_season.csv`
One row per completed season with non-empty FGA on the BRef table (pull includes history through the newest completed-looking row at access date; in-progress empty rows dropped).

Columns: `season,fga,fg_pct,fg3a,fg3_pct,fta,ft_pct,orb,drb,trb,ast,stl,blk,tov,pf,pts,pace,source_url,access_date,notes`

### `avg_game_by_decade.csv`
Unweighted arithmetic mean of season rows with **start year** in the decade window, restricted to **1979-80 through 2023-24** (3PT era start through last fully settled season used for the book draft line).

Columns include `n_seasons`, `season_from`, `season_to`, counting stats, `pace`, method/source fields, `notes`.

### `draft_2023_24_line_check.csv`
Compares the ROADMAP/mentions drafted 2023-24 line (88.9 FGA, ~47% FG, 35.1 3PA, 21.7 FTA, 33 DRB, 10.6 ORB, 26.7 AST) to the BRef 2023-24 league-average row.

## Blank / GAP rules

- Pre-1979-80 seasons in the season file leave **3PA/3P% blank** (no line).
- Pace blank when BRef cell empty → do not invent.
- 1970s decade row is **one season only** (1979-80) — noted in `notes` (not a full decade).
- 2020s decade row is **partial** (2020-21…2023-24).
- Prefer `GAP` / blank over invented cells. Cite BRef; do not rehost proprietary tracking.

## Confidence

- Season cells transcribed from public BRef HTML: **HIGH** for the accessed snapshot.
- Decade means: **HIGH** as arithmetic transforms; interpretation of partial decades is a writer hedge.
- Existing `data/reference/nba_league_averages_by_season.csv` on main **diverges** from this live BRef pull for many pre-2018 seasons (FGA/PTS). Treat that file as stale pending refresh; this pack’s season CSV is the cite-backed refresh candidate.

## Regenerate

1. Fetch the BRef league-average Per Game page (no login).
2. Parse `table#stats-Regular-Season` rows with `data-stat` fields (`fga_per_g`, `pace`, …).
3. Drop rows with empty FGA.
4. Mean season rows by `floor(start_year/10)*10` for 1979-80…2023-24 → decade CSV.
5. Diff draft line vs 2023-24 row → check CSV.

## Non-goals

No Kaggle dump (credentials still blocked per ROADMAP). No playoff-only mix. No invented pace for early eras.
