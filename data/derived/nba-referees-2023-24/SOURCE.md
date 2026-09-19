# NBA referees 2023-24 — source note

**As of:** 2026-09-19  
**Source URL (canonical):** [https://www.nbastuffer.com/2023-2024-nba-referee-stats/](https://www.nbastuffer.com/2023-2024-nba-referee-stats/)  
**Also cited / redirects:** https://www.nbastuffer.com/2023-2024-nba-referee-stats/ (same site; path used in ROADMAP)  
**Label:** SECONDARY (NBAstuffer TablePress aggregates). Not an NBA Official redistribution.  
**Confidence:** **HIGH** for HTML table transcription (2026-09-19). Two rows flagged MEDIUM for foul_% scale anomaly.

## Files

| File | Rows | Notes |
|------|------|-------|
| `nba_referees_2023_24.csv` | 175 | Flat union of regular season + playoffs |
| `page.html` | — | Cached HTML snapshot for audit (do not commit if repo policy prefers URL-only) |

Row split: regular_season=125; playoffs=50.

## Extraction

- HTML contains embedded TablePress tables (`tablepress-114` = regular season; `tablepress-119` = playoffs). **Not JS-blocked** on curl fetch 2026-09-19.
- Empty RANK column dropped.
- Same person may appear as both CHIEF and CREW (separate rows).

## Gaps / anomalies

- **JD Ralls**, **Biniam Maru** (regular season): `foul_pct_against_*` published as values >1 (e.g. tens). Left as-is with `confidence=MEDIUM`.
- Playoff game counts are small for many officials — descriptive only.
- Paid Excel game-by-game product on the page was **not** scraped.
- Official daily assignments: http://official.nba.com/referee-assignments/ — no season aggregate table located.

## Citation

NBAstuffer. *2023-2024 NBA Referee Stats.* https://www.nbastuffer.com/2023-2024-nba-referee-stats/ (accessed 2026-09-19).
