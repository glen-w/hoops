# Pack A — Chinese NBA team-name renderings (2026-09-20)

Cite-backed Simplified (Mainland) and Traditional (Taiwan-primary, HK noted) renderings for all **30** current NBA franchises.

## Deliverables

| Path | Description |
|------|-------------|
| `data/derived/teams/nba_team_names_zh.csv` | Main dataset (30 rows) |
| `data/raw/` | Wikidata API JSON (QIDs, labels, city labels) |
| `methodology.md` | Sources, variant rules, honesty locks |
| `CHAPTER-MAP-append.md` | 4-cell binder rows |
| `PR-BODY.md` | Suggested PR text for glen-w/hoops |

## Quick stats

- **30/30** `zh_hans` and `zh_hant` filled (0 GAP)
- Traditional primary = Wikidata **zh-tw** when present
- HK variants retained in `zh_hk_label` + notes
- City/nickname split cite-backed; Golden State city = prefix `金州` from team label

## Honesty

No invented characters. QIDs re-resolved via enwiki (do not copy colliding QIDs from `teams.csv`).
