# Decade analysis: next steps (coder, tick after 2026-10-19)

Status: nothing fetched this tick. No new figures. Prior figures in decade_summary_confirmed.md remain summary-level only.

## Order of work
1. Run `python3 -I analysis/br_league_fetch.py analysis/out/br_league_per_game.csv`. Cite BR (WNKIH56T) with URL and access date from the .access sidecar. Fallback: nba_api (9FJZPDKM) league dashboard.
2. Run decade_means.py on the CSV. Report `mean_of_means` and `games_weighted` as two separate values; never merge them.
3. Check BR 3PA share (3PA/FGA) against Wang's 22% to 39% range. Mismatch in span or season window must be stated, not smoothed.
4. Open the Foteinakis PDF. Resolve nine seasons vs 2012-13 to 2022-23 (that span is eleven seasons). Quote no season count until resolved.
5. Open the Wang PDF or abstract. Confirm Limitations text and how the 1.85 per year slope was computed.

## Caveats
- BR terms: scrape politely, cite only, no raw redistribution.
- Per-game league rows are per-team-game averages; games-weighting needs games per season, so confirm the column exists before claiming a weighted value.
