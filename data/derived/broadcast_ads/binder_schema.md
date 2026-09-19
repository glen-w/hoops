# Binder schema — proposed `data/derived/broadcast_ads/`

**Access date:** 2026-09-19 (Europe/Paris)  
**Rule:** empty cells preferred to zeros; never invent. Always keep `source_url` + `as_of` + `confidence`.

Suggested landing: `data/derived/broadcast_ads/` in `glen-w/hoops` (sidecar copy first).

---

## 1. `national_media_rights.csv`

Contract / partner facts (rights fees — **not** ad sales).

```text
season_start,season_end,partners,package_scope,total_contract_usd,annual_avg_usd,partner_annual_usd,value_kind,source_url,as_of,confidence,notes
```

| Column | Notes |
|--------|-------|
| `value_kind` | `official_partners_term` \| `secondary_contract_total` \| `secondary_aav` \| `secondary_partner_split` \| `secondary_per_team_payout` |
| `confidence` | `HIGH` \| `MEDIUM` \| `GAP` |
| Money fields | Blank when unknown; do not fill from invented arithmetic |

Aligns with rows already populated in `hoops-league-income-2026-09-19/league_income_ingredients.csv` (media categories).

---

## 2. `national_ads_booking.csv`

Advertiser → network/streamer spend estimates (measurement vendors / trade press).

```text
season,window,partner_or_platform,metric,value,unit,currency,vendor,source_url,as_of,confidence,methodology_note,notes
```

| Column | Notes |
|--------|-------|
| `window` | `regular_season` \| `playoffs` \| `finals` \| `full_season` \| `unspecified` |
| `metric` | `ad_sales_usd` \| `airings` \| `impressions` \| `cpm` \| `yoy_pct` |
| `vendor` | e.g. `iSpot` \| `Guideline` \| `unknown` |
| Rule | Do not compute CPM unless spend + impressions share platform, geography, period |

Sketch ancestor: `hoops-thicken-efficiency-income-2026-09-19/SCHEMA-sketch.md` → `national_ads_booking.csv`.

---

## 3. `local_media.csv`

```text
season,team,market,distributor,fee_usd,fee_kind,source_url,as_of,confidence,notes
```

| `fee_kind` | `rights_fee` \| `equity_income` \| `hybrid` \| `unspecified` |
| Expectation | Mostly empty; rare SECONDARY team anecdotes only |

---

## 4. `in_game_inventory.csv`

Courtside LED, apron, stanchion, floor, stair LED, augmented overlay, etc.

```text
record_id,season,team_or_league,asset_type,asset_description,broadcast_visible,national_blackout_note,sponsor_brand,term_note,fee_usd,inventory_units,unit_definition,source_url,as_of,confidence,notes
```

| `asset_type` enum sketch | `courtside_led` \| `apron` \| `stanchion_led` \| `floor` \| `stair_led` \| `centerhung` \| `augmented_broadcast` \| `other` |
| Money / unit counts | Blank unless source states them |

---

## 5. `sponsored_moments.csv`

Writer taxonomy for entitlement of named moments (not a published NBA product catalog).

```text
deal_id,season,brand,moment_name,scope,announcement_date,fee_usd,source_url,as_of,confidence,notes
```

| `scope` | `league` \| `team` \| `network_show` \| `event` |
| `fee_usd` | Almost always blank |

---

## 6. `sponsor_deals.csv` (optional wider sheet)

From thicken BA schema — keep rights fees separate from media buys:

```text
deal_id,season_start,season_end,announcement_date,league_team_venue,rights_holder,brand,category,asset_type,jersey_patch,naming_rights,in_arena,digital_social,annual_fee_usd,total_fee_usd,fee_type,source_url,as_of,confidence,notes
```

---

## 7. `inventory_dictionary.csv`

```text
asset_type,definition,inclusion_rule,exclusion_rule,source_or_owner,notes
```

Seed rows (definitions only — no dollars):

| asset_type | definition sketch |
|------------|-------------------|
| `rights_fee` | Network/streamer payment to league for windows |
| `media_buy` | Advertiser payment to network/streamer for spots / impressions |
| `sponsorship_rights` | Brand payment to league/team for association / assets |
| `activation` | Brand spend to execute the sponsorship (often excluded from rights tallies) |
| `courtside_led` | Rotating LED ribbon / boards in camera sightlines |
| `sponsored_moment` | Entitlement of a named program moment or data-triggered overlay |

---

## 8. `source_log.csv`

```text
source_id,url,publisher,publication_date,accessed_on,data_vintage,label,paywall_or_gate,saved_copy,extraction_notes,verification_status
```

---

## Join / non-join rules

1. Do **not** sum `national_media_rights.total_contract_usd` with `national_ads_booking.ad_sales_usd`.  
2. Do **not** treat IEG sponsorship rights totals as ad spend (IEG excludes media buys).  
3. Cap / BRI rows stay in `league_income_ingredients.csv` — link by `season` only.  
4. Prefer one vendor chain per metric; if two vendors disagree, two rows — never average.
