# Schema sketch (empty tables)

Do not invent rows. When a licensed or hand-verified figure exists, use:

## `franchise_year.csv` (optional later)

`season,team,forbes_value_usd_m,forbes_revenue_usd_m,forbes_op_income_usd_m,source_url,access_date,notes`

## `league_income_component.csv`

`season,component,amount_usd_m,definition_note,source_url,access_date,confidence`

`component` enum sketch: `national_rights_fee | local_media | gate | team_sponsorship | league_sponsorship | jersey_patch | other | bri_total_reported`

## `national_ads_booking.csv`

`season,partner,window,ad_sales_usd_m,source_url,access_date,confidence`

## Join to CBA (future)

`cba_edition,clause_id,topic` with topics like `bri_definition | salary_cap | apron | escrow | audit_report`
