# Methodology — Chinese NBA team-name renderings (Pack A)

**Pack date:** 2026-09-20 (Europe/Paris)  
**Access date for all cited fetches:** 2026-09-20  
**Artifact:** `data/derived/teams/nba_team_names_zh.csv` (30 current NBA franchises)

## Honesty locks

- **No invented Chinese characters or phonetic spellings.** Every `zh_hans` / `zh_hant` value comes from Wikidata language labels (and, where used, zh.wikipedia sitelink titles that match those labels).
- **GAP over guesses.** City/nickname fields are filled only when a cite-backed city label (or documented common prefix such as 金州 for Golden State) can be aligned to the full team label; otherwise they would be `GAP` (this build: 0 nickname GAPs after documented prefix-form alignment).
- **Primary over blogs.** Prefer Wikidata + zh.wikipedia over fan blogs / NetEase listicles (those may be mentioned only as secondary awareness, never as sole authority for a cell).
- **Script identity noted.** When Simplified and Traditional use the same codepoints, notes say so; Traditional primary prefers Wikidata `zh-tw` (Taiwan media convention) over generic `zh-hant` when both exist.

## Sources used

| Source | Role | URL pattern |
|--------|------|-------------|
| Wikidata entity labels | Primary for `zh-hans`, `zh-cn`, `zh-hant`, `zh-tw`, `zh-hk` | `https://www.wikidata.org/wiki/Q…` |
| Wikidata sitelinks | Resolve correct QID via `enwiki` title; `zhwiki` title for Mainland page | same API |
| Chinese Wikipedia | Full-name cross-check / `source_url_hans` | `https://zh.wikipedia.org/wiki/…` |
| Wikidata city entities | Separable `city_zh_*` | e.g. Boston `Q100`, Oklahoma City `Q34863` |
| glen-w/hoops `teams.csv` | English names + abbr scaffolding only (QIDs in that file are **not** trusted — several collisions observed) | `https://github.com/glen-w/hoops` |

### How QIDs were chosen

`teams.csv` on `main` has incorrect / colliding `wikidata_qid` values for multiple NBA rows (e.g. shared QIDs across franchises). This pack **re-resolved** each franchise via Wikidata `wbgetentities` with `sites=enwiki` + English team title, then stored the resolved QID in `wikidata_qid`.

### How Simplified vs Traditional were chosen

1. **`zh_hans`:** Wikidata `zh-hans`, else `zh-cn`, else `zh`, else zhwiki title.  
2. **`zh_hant`:** Prefer Wikidata **`zh-tw`** (Taiwan broadcast/print convention for NBA nicknames such as 塞爾提克 / 暴龍 / 溜馬), else `zh-hant`, else `zh-hk`.  
3. **HK variants** recorded in `zh_hk_label` and `notes` when they differ (e.g. Celtics 塞爾特人, Knicks 紐約人, Kings 帝王, Raptors 速龍).

### City / nickname separation

- City labels from Wikidata municipality/state QIDs (cited per row in `city_source_url` / notes).  
- Nickname = remainder of full team label after a documented city prefix form.  
- When Wikidata city label uses a geo suffix (州/区/市) or an alternate transliteration (克利夫兰 vs 克里夫兰; 休斯敦 vs 休斯顿; 奧克拉荷馬市 vs 奧克拉荷馬 in TW team label), notes record the **prefix form used for the split** — the `city_zh_*` columns still hold the Wikidata city label, not an invented shorter form (except **Golden State → 金州**, which is the prefix of the cite-backed team label itself, not a municipality QID).

### Not used as authorities (awareness only)

Mainland↔Taiwan comparison blogs (e.g. xianote.com, 163.com listicles) agree with Wikidata on major nickname splits but were **not** written into cells without Wikidata corroboration.

## Coverage

| Field | Non-GAP / 30 |
|-------|----------------|
| zh_hans | 30/30 |
| zh_hant | 30/30 |
| city_zh_hans / city_zh_hant | 30/30 |
| nickname_zh_hans / nickname_zh_hant | 30/30 |

Former franchise names: **not** included (optional `former_names_zh.csv` omitted — no extra cite pass this pack).

## Expansion path

- Add Tencent NBA / NBA China official glossary pages if publicly listable without login.  
- Add zh-yue (Cantonese Wikipedia) titles as an explicit HK column.  
- Former names CSV from Wikidata aliases + historical zhwiki redirects.
