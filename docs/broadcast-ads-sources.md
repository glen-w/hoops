# Broadcast advertising and sponsor inventory sources

**Research cut-off:** 2026-09-19 (Europe/Paris). **Question:** is there public NBA ad-spend or sponsor-inventory data, and if not, what should the binder capture? Kaggle is excluded.

## Short answer

**Partial public data exists, but not a single official, historical inventory ledger.** Public sources cover different things:

- Sponsor-rights estimates: deal counts, categories, jersey patches, naming rights and estimated rights fees.
- Media ad-spend estimates: advertiser spend, impressions, airings, CPM or network/platform totals, usually from commercial measurement vendors.
- Public announcements: individual team/league sponsorships and media agreements, often without price, inventory quantity or make-good terms.

Do not equate sponsorship rights fees with broadcast media buys, and do not treat a vendor estimate as an NBA audited total.

## Source register

| ID | Source and data | Label | What to do with it |
|---|---|---|---|
| BA-01 | [IEG / Sponsorship.com, NBA Sponsorship Snapshot 2024-25](https://sponsorship.com/wp-content/uploads/2025/07/IEG_NBA_Sponsorship_Snapshot_2024-25_Season.pdf) | **SECONDARY** | Public snapshot sourced to IEG's Sponsorship Intelligence Database. It reports estimated sponsorship rights fees, deal counts, brands/categories and asset mix such as jersey patches and naming rights. It explicitly excludes commercial advertising media buys, player endorsements and brand activation expenses. Use as a rights-fee benchmark, not ad spend. |
| BA-02 | [SponsorUnited, NBA Sponsorship Intelligence Report 2025-26](https://www.sponsorunited.com/insights/nba-sponsorship-intelligence-report-2025-26) | **SECONDARY** | Public summary of team sponsorship revenue, category activity, jersey-patch coverage and brands. Underlying intelligence may be gated; retain the public page and mark any extracted value as vendor-estimated. |
| BA-03 | [MediaPost, "NBA Regular Season Ad Spend Hits $760M," 22 Apr 2026](https://www.mediapost.com/publications/article/414480/nba-2025-26-video-ad-revenue-hits-760m-viewing-u.html?edition=142360) | **SECONDARY** | Public trade-press report of iSpot.tv estimates for 2025-26 regular-season national TV/streaming ad revenue, airings, impressions and leading advertisers. It is an estimate, not an NBA filing; retain iSpot's methodology and platform scope. |
| BA-04 | [Sportico, "NBA Ad Sales Soar to $2.1 Billion in First Season of New Rights Deals"](https://www.sportico.com/business/media/2026/nba-ad-sales-media-rights-deal-tv-1234942133/) | **SECONDARY** | Trade report using Guideline data for national ad sales, network/platform split, audience delivery and CPM context. Treat all totals as measurement-vendor estimates and preserve the season definition. |
| BA-05 | [NBA 2024 media-agreement announcement](https://www.nba.com/news/nba-media-agreements-2024) | **OFFICIAL** | Primary source for rights partners, package structure, distribution and game windows beginning 2025-26. It does not disclose sellable commercial units, rate cards, advertiser spend or inventory sold. |
| BA-06 | [NBA Partner/Corporate Partnerships hub](https://www.nba.com/partners) | **OFFICIAL** | Official public landing point for named league partners, but not a complete historical inventory or price list. Use individual team/league announcements to document an asset, term and announcement date. |
| BA-07 | [iSpot.tv NBA advertising insights](https://www.ispot.tv/brands/0m/nba) | **SECONDARY** | Measurement-vendor lead for advertiser, creative, airing and estimated-spend observations. Verify whether the page exposes the required season/platform detail before relying on it. |
| BA-08 | [EDO Sports advertising analytics](https://www.edo.com/sports/) | **SECONDARY** | Measurement/analytics lead for sports advertising exposure and response. Public pages may describe methodology without releasing a complete NBA inventory file. |

**Access date for every URL above:** 2026-09-19 (Europe/Paris).

## What is and is not publicly available

### Public enough to cite

- League/team sponsor announcements and the asset named in the announcement.
- Vendor or trade-press estimates of rights fees and ad spend, with season and methodology.
- Media-rights partner and package information in official NBA releases.
- Historical sponsor/category snapshots where the vendor publishes a PDF or summary.

### Usually not public as a complete series

- Network/streamer sellable-unit inventory, unsold units, make-goods and rate cards.
- Contract-level fee schedules for every team sponsor.
- A league-owned, audited annual table separating broadcast ad revenue, sponsorship rights fees, activations, endorsements and licensing.
- Comparable 2015-16 team-by-team sponsor inventory with consistent definitions.

The correct status for an unpriced announcement is **UNCONFIRMED** for amount, while the existence of the announced partnership can be **OFFICIAL** if the announcement is from the NBA/team/brand.

## Binder spreadsheet schema if hand-built

Use one normalized workbook with separate sheets. Leave unknown values blank; do not enter zero unless the source says zero.

### `sponsor_deals`

```text
deal_id | season_start | season_end | announcement_date | league_team_venue | rights_holder | brand | parent_company | category | asset_type | asset_description | jersey_patch | naming_rights | in_arena | digital_social | content | hospitality_suite | exclusivity | territory | term_years | annual_fee_usd | total_fee_usd | fee_type | source_url | source_accessed_on | source_label | amount_confidence | notes
```

### `broadcast_inventory`

```text
record_id | season | game_type | network_platform | package | market | game_or_window | spot_length_seconds | unit_count | sellable_or_aired | advertiser | category | gross_spend_usd | net_spend_usd | impressions | audience_source | cpm | makegood_flag | source_url | source_accessed_on | source_label | methodology | confidence | notes
```

### `inventory_dictionary`

```text
asset_type | definition | inclusion_rule | exclusion_rule | source_or_owner | notes
```

### `source_log`

```text
source_id | url | publisher | publication_date | accessed_on | data_vintage | label | paywall_or_gate | saved_copy | extraction_notes | reviewer | verification_status
```

## Calculation rules for a later chapter table

- Keep `rights_fee`, `media_buy`, `activation`, `endorsement`, and `licensing_royalty` as separate monetary fields.
- Store the original currency and reported period; only then add a documented conversion field.
- Do not calculate CPM unless both spend and impressions use the same platform, geography, and period.
- Do not infer annual fee from total contract value unless the term and escalation schedule are known.
- A vendor estimate is not an official number: label the row **SECONDARY** or **UNCONFIRMED**, even when it is the best available public observation.
