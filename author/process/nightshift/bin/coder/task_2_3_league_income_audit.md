# League Income Audit — Tasks 2-3 Scaffolding

## Current Data State (league_income_ingredients.csv)

Present:
- National media rights: 2016-17–2024-25 and 2025-26–2035-36 deals (partners, totals, annual splits)
- Per-team national TV revenue: 2024-25 ($103M), 2025-26 ($143M) from Sportico
- Salary cap structure: 2022-23–2025-26 from pr.nba.com
- Basketball-related income (BRI): 2024-25 ($10.25B) secondary source
- Attendance: 2015-16, 2016-17, 2017-18, 2022-23, 2023-24 (mostly official)

Gaps (must source or cite explicitly if not filled):
- Attendance: 2018-19, 2019-20, 2020-21, 2021-22 (totals and averages)
- 2024-25 regular-season attendance total (only "exceeded 22.3M" cited)
- Salary cap/tax before 2022-23 (now available: see analysis/nba_salary_cap_apron_history.csv)
- Per-team national TV revenue for 2016-17–2023-24
- Local media revenue (by season and team, if trackable)
- Arena gate revenue / ticket revenue
- Licensing revenue
- Sponsorship and jersey patch revenue

## Data Sources for Missing Pieces

1. **Attendance 2018-19 through 2021-22:**
   - Primary: Basketball-Reference (cite-scrape, stable cross-check)
   - Secondary: Spotrac, HoopsHype archives
   - Sport-Reference data-use: ~20 req/min, no competing DB (per hoops/docs/open_datasets.csv)

2. **Per-team national TV revenue 2016-17–2023-24:**
   - Search Sportico archives (2024-25 available; backfill strategy TBD)
   - Fallback: Estimate from annual total + 30-team split if primary unavailable
   - Note: 10% growth cap limits projections per CBA (Sportico 2025-26 report)

3. **Local media and arena revenue:**
   - Individual team disclosures (sparse; may require FOIA for public teams)
   - Spotrac team financial summaries (use with caution: estimates, not audited)
   - Forbes valuations (Jan 2016, etc.; secondary, not audited)

## Recommended Task Flow

1. **Task 2:** Fill attendance gaps (2018-19–2021-22) using Basketball-Reference or Spotrac
2. **Task 3:** Build per-team national TV revenue table for 2016-17–2025-26 by:
   - Searching Sportico archives or pr.nba.com team earnings reports
   - If unavailable: document assumption (equal split of annual media total ÷ 30)
   - Cross-check against known recent figures (2024-25, 2025-26)

## Filing Convention

All cells with data must include a source URL or citation. Empty cells signal "searched, not found" or "not published." Do not invent.
