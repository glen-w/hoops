# Chapter Map

Maps Scrivener binder sections to repository data products. Tracks readiness state for each dataset referenced in the draft manuscript.

This is the research tooling manifest. Prose stays in Scrivener, citations in Zotero. The sidecar holds derived tables we are licensed to redistribute, source documentation, and methodology notes.

---

## Data Products

| Binder / section | Data product (repo path) | Status | Notes |
|------------------|--------------------------|--------|-------|
| PLAYERS / height | `data/derived/height-series/nba_height_series.csv` | READY | 607 rows; RunRepeat through 2021; includes slim `nba_height_league_by_season.csv` (75 rows) |
| Officiating / referee stats table | `data/derived/nba-referees-2023-24/nba_referees_2023_24.csv` | READY | 175 rows (125 RS + 50 playoffs); NBAstuffer; 2 MEDIUM confidence anomalies (foul_% >1) |
| Disputes / BAT | `data/derived/fiba-bat-2022/fiba_bat_arbitration_by_year.csv` | READY | 21 rows (2007–2025); FIBA official PDF; includes `fiba_bat_2022_key_metrics.csv` (8 rows) and footnotes |
