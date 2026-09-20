# Methodology — Average Desk Phase 1

**Access:** 2026-09-20 (Europe/Paris)  
**Pack:** `hoops-average-desk-2026-09-20`

## Design principle

Every “average” product is a **summary of observed distributions** (mode / median / mean where numeric and defined), never a fabricated entity. Hooks may personify carefully, but data files stay composite.

## 1. Average team

### Inputs

| Input | Path / URL | Use |
|-------|------------|-----|
| Teams desk | `/workspace/hoops-swatches-work/data/derived/teams/teams.csv` (NBA `league_id=nba`, n=30) | city, arena, capacity, ownership_structure, colours_* , founded_year |
| US metro pop | Census Bureau `cbsa-est2023-alldata.csv` (CBSA MSA, POPESTIMATE2023) | metro_pop for US homes |
| Toronto | Wikipedia *Greater Toronto Area* reporting StatCan **2021** census (6,712,341) | CA market only; flagged non-comparable vintage |
| Conference/division | Wikipedia *National Basketball Association* (access 2026-09-20) | current 6×5 alignment |

### Aggregations

- **Arena capacity:** min / median / mean / max over 30 non-null capacities (public figures as stored in teams desk).
- **Ownership:** mode of `ownership_structure` + full Counter.
- **Metro band:** cut US+Toronto pops into bands (`megacity_10M+`, `large_5_10M`, `mid_large_2.5_5M`, `mid_1_2.5M`, `under_1M`); report mode + distribution. Shared markets (NYC, LA) counted **per team** (duplicate market rows intentional).
- **Colours:** count filled `colours_primary_hex`. If 0 → **GAP**. If >0 in a later pass → **modal** hex among filled only — **never** channel-wise mean of hex.
- **Conference/division:** empirical mix (expect 15/15 and 5 per division under current rules).

### Explicit non-actions

- No invented franchise name, mascot, or owner.
- No averaged hex string.
- No silent coercion of StatCan 2021 into “Census 2023.”

## 2. Average / historical player universe

### Primary dump (v1)

- File: `player_data.csv` via [msyamkumar/cs220-projects](https://raw.githubusercontent.com/msyamkumar/cs220-projects/master/spring20/final/player_data.csv) (identical twin mirrored as Graham-Dom CSPB dump).
- Schema: name, year_start, year_end, position, height, weight, birth_date, college.
- **Coverage:** year_start/year_end span **1947–2018** in this file; **4550** rows after empty-name drop.
- **Draft:** not present → blank columns reserved for Phase 2.
- Attribution: teaching/public BRef-class dump; **not** NBA.com Stats API republication.

### Statistics computed

- Height (inches, parsed from `ft-in`), weight (lb): mean + median; mean height by **debut decade**.
- Career span years inclusive.
- Position Counter as coded (G/F/C mixes).
- **Names:** `Counter` on first token and last token; report modes + top-10. Composite “John Williams” = modal-first **juxtaposed with** modal-last — **not** asserted as a single historical person’s full name frequency.

### Staged but not merged

ESPN sportsdataverse `player_core_{2002,2010,2015,2020,2024,2025,2026}.csv` sit in `data/raw/` for Phase 2 dedup (adds draft_* and post-2018 players). Merging deferred so v1 remains one clear citation.

### Non-actions

- No Basketball-Reference HTML scrape this pass (ToS/etiquette; prefer dumps).
- No claim of “every NBA player ever through 2026.”

## 3. Videogame ratings seed

### Method

1. Download HoopsHype player history HTML + 2K27 rankings HTML (access 2026-09-20).
2. Parse embedded `__NEXT_DATA__` → `VideoGameRatings` objects (`videoGameDisplayName`, `rating`, optional `season`, `sortName`).
3. Emit CSV with certainty tags; attribute URL + access date.
4. Dedup on (game_title, player_name, overall_rating, source_url).

### Certainty

- **HIGH:** history entry with season field.
- **MEDIUM:** rankings snapshot or missing season (patch drift).
- No row without a sourced rating integer.

### Non-actions

- No fabricated overalls for missing years.
- No NBA Live / early 2K rows until Archive/wiki tables are transcribed with URLs.
- Not an official 2K Sports dataset.

## Reproducibility

Rebuild script logic lives in this pack’s generation notes; raw HTML/CSV retained under `data/raw/`. Derived outputs under `data/derived/average/`.
