# Method — average game by decade (light pin)

**Pack:** `hoops-avg-game-by-decade`  
**Access / as_of:** 2026-09-19 (Europe/Paris)  
**Mode:** light pin only (not a full research pack). **Not blocked.**

## Verdict

**Basketball-Reference publishes free, login-free league-average tables by season** that can back a by-decade chapter table for PPG, pace, FG%, and 3PA rate.

Primary URL (Per Game):  
https://www.basketball-reference.com/leagues/NBA_stats_per_game.html

Companions (same site, free):  
- Totals: https://www.basketball-reference.com/leagues/NBA_stats_totals.html  
- Per 100 possessions: https://www.basketball-reference.com/leagues/NBA_stats_per_poss.html  
- Glossary (Pace definition): https://www.basketball-reference.com/about/glossary.html

## How to build the decade table

1. **Pull season rows** from the Per Game league-averages table (one row per season, NBA/BAA).  
2. **Map seasons to decades** with an explicit rule, e.g. decade label = calendar year of season *end* floored to decade (`1985-86` → 1980s), or use landmark single seasons as chapter pins (this pack’s sample).  
3. **Metrics:**
   | Wanted | BRef column | Notes |
   |--------|-------------|-------|
   | PPG | `PTS` | League average points per game (team) |
   | Pace | `Pace` | Possessions per 48; **published from 1973-74 onward only** |
   | FG% | `FG%` | `FG / FGA` |
   | 3PA rate | derive `3PA / FGA` | Both on the same row; 3P columns empty before **1979-80** |
4. **Decade aggregation (later full job, not done here):** mean or median of season values inside the decade window — document which, and whether lockout / shortened seasons are excluded. This light pin only cites **landmark seasons**, not decade means.  
5. **Cite** the BRef league-averages URL + access date on every row. Prefer archive/snapshot if the live page updates mid-season (e.g. 2025-26 row is in-progress on the live page).

## Caveats (writer-facing)

- **Pace gap:** blank before 1973-74 — do not invent pace from modern formulas for early eras unless a separate sourced method is documented.  
- **3P gap:** no three-point line before 1979-80 — leave 3PA / 3PA rate blank.  
- **In-progress seasons:** live BRef rows for the current season change; prefer completed seasons for manuscript pins.  
- **Playoffs vs regular season:** the main league-averages table is **regular season**; BRef also shows a separate playoffs block on the same page — do not mix.  
- **ABA:** out of scope unless chapter explicitly merges leagues; this pin uses NBA/BAA rows only.  
- **Terms of use:** hand transcription or documented scrape for research sidecar; do not republish BRef’s full historical table into a public repo as a dump — cite and sample.

## Status

| Item | Status |
|------|--------|
| Free public source exists? | **Yes** |
| Login / paywall? | **No** (page fetched 2026-09-19 without auth) |
| Sample landmark seasons CSV | **Populated** (`sample_seasons.csv`) |
| Full by-decade aggregated table | **Not built** (out of light-pin scope) |
