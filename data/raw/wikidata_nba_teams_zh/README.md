# Wikidata NBA Teams — Chinese Labels (Raw Data)

**Access date:** 2026-09-20  
**Pack:** hoops-cn-team-names-2026-09-20

Supporting raw JSON from Wikidata API for Chinese NBA team-name renderings.

## Files

| File | Description | Size |
|------|-------------|------|
| `qid_map.json` | Re-resolved NBA franchise QIDs via enwiki sitelinks | 1 KB |
| `wd_batch1.json` | Initial Wikidata batch fetch (QIDs, labels) | 73 KB |
| `wd_resolve_0.json` | Wikidata entity labels batch 0 | 107 KB |
| `wd_resolve_10.json` | Wikidata entity labels batch 10 | 102 KB |
| `wd_resolve_20.json` | Wikidata entity labels batch 20 | 109 KB |
| `city_labels.json` | City entity labels (zh-hans, zh-tw, zh-hk) | 5.3 KB |
| `city_resolve_fix.json` | City entity resolution fixup | 221 KB |

## Purpose

These JSON files preserve the raw Wikidata API responses used to derive `data/derived/teams/nba_team_names_zh.csv`. They support reproducibility and allow verification of label sourcing without re-fetching from Wikidata.

## Honesty

No invented QIDs. All QIDs were re-resolved via Wikidata `wbgetentities` API with `sites=enwiki` parameter (do not trust colliding QIDs from `teams.csv`).

## Derived Artifact

See `data/derived/teams/nba_team_names_zh.csv` and `docs/teams/nba_team_names_zh_methodology.md` for the processed dataset and methodology.
