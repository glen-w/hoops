# Franchise efficiency sources

**Research cut-off:** 2026-09-19 (Europe/Paris). **Purpose:** source the still-open franchise-efficiency item without altering Scrivener. Kaggle is intentionally excluded.

## Finding on the "Forbes, 22 Apr 2016" sketch

I could not verify a Forbes article published on 22 April 2016 that presents a Portland–Boston efficiency comparison. The closest public, date-matched material is a cluster of Forbes valuation/brand pages and a contemporaneous secondary payroll-versus-wins comparison. Treat the 22-April attribution as **UNCONFIRMED** until the original clipping, URL, or screenshot is supplied. Do not cite it as a verified Forbes article in the book.

The likely source family is:

1. Forbes' 20-Jan-2016 valuation release and team valuation table.
2. Forbes' 02-Apr-2016 "Visual Brand Snapshots" page, which exposes team value and revenue-per-fan fields.
3. Forbes' 20-Jan-2016 "Best and Worst GMs: Wins vs. Payroll" page.
4. Austin Vitelli's 2015-16 dollars-per-win calculation and the contemporaneous OregonLive version of the payroll/wins comparison.

## Source register

| ID | Source and what it can support | Label | Caveat / use |
|---|---|---|---|
| FE-01 | [Forbes, "Forbes Releases 18th Annual NBA Team Valuations," 20 Jan 2016](https://www.forbes.com/sites/forbespr/2016/01/20/forbes-releases-18th-annual-nba-team-valuations/) | **SECONDARY** | Forbes is the original publisher of its own estimates, but these are not audited NBA disclosures. Use for team value, estimated revenue, estimated operating income, and valuation-year context. |
| FE-02 | [Forbes, "Visual Brand Snapshots For All 30 NBA Teams," 2 Apr 2016](https://www.forbes.com/sites/baileybrautigan/2016/04/02/visual-brand-snapshots-for-all-30-nba-teams/) | **SECONDARY** | Public page includes team value and revenue-per-fan fields, including Boston and Portland. It is a brand/valuation feature, not a payroll-efficiency study. |
| FE-03 | [Forbes, "The NBA's Best And Worst GMs: Wins vs. Payroll," 20 Jan 2016](https://www.forbes.com/sites/chrissmith/2016/01/20/the-nbas-best-and-worst-gms-wins-vs-payroll/) | **SECONDARY** | Candidate source for the "wins versus payroll" framing. Preserve the page's season definition and payroll definition before extracting. |
| FE-04 | [Austin Vitelli, "Measuring the spending of NBA teams in 2015-16: dollars per win"](https://austinvitelli.com/around-the-league/measuring-the-spending-of-nba-teams-in-2015-16-dollars-per-win/) | **SECONDARY** | Candidate source for a reproducible 2015-16 payroll/wins table. The article reports Portland at 44 wins, $61.69m payroll, and $1.40m per win; Boston at 48 wins, $77.14m payroll, and $1.61m per win. Verify the payroll field before treating these as book data. |
| FE-05 | [OregonLive, "Payroll vs. wins: Which NBA teams got the biggest bang for the buck this season?"](https://www.oregonlive.com/nba/2016/05/payroll_vs_wins_which_nba_team.html) | **SECONDARY** | Contemporaneous journalistic comparison; useful cross-check against FE-04. Publication is May 2016, not 22 April. |
| FE-06 | [Spotrac, 2015-16 NBA Team Salary Cap Tracker](https://www.spotrac.com/nba/cap/_/year/2015) | **SECONDARY** | Public cap-accounting dataset. "Cap allocations," cash payroll, dead money, and active salary are not interchangeable; record the selected field verbatim. |
| FE-07 | [Spotrac, Portland Trail Blazers 2015-16 financial summary](https://www.spotrac.com/nba/portland-trail-blazers/overview/_/year/2015) and [Boston Celtics 2015-16 financial summary](https://www.spotrac.com/nba/boston-celtics/overview/_/year/2015) | **SECONDARY** | Team-level audit trail for the two clubs. Pages may change presentation or require interaction; save an access date and an export/screenshot if used. |
| FE-08 | [Peter Bender, NBA salaries 2015-16](https://www.eskimo.com/~pbender/misc/salaries16.txt) | **UNCONFIRMED** | Useful historical text compilation, not an NBA or team filing. Cross-check every total with Spotrac or player-level records; do not use as sole authority. |
| FE-09 | [NBA Stats](https://www.nba.com/stats/teams) | **OFFICIAL** | Primary public source for team wins and team efficiency fields where the selected season and stat table are available. Capture query parameters/export date because the site is dynamic. |
| FE-10 | [Basketball-Reference, Portland 2015-16 team page](https://www.basketball-reference.com/teams/POR/2016.html) and [Boston 2015-16 team page](https://www.basketball-reference.com/teams/BOS/2016.html) | **SECONDARY** | Stable cross-check for games, wins, losses, pace, ratings, and roster context. It is not a payroll source. |

**Access date for every URL above:** 2026-09-19 (Europe/Paris). "OFFICIAL" means league/team primary data; "SECONDARY" means published estimate or independent compilation; "UNCONFIRMED" means a lead requiring verification.

## Safe reconstruction plan

Do not divide unlike concepts. Build one row per `team-season` and retain the source field names:

```text
season | team | wins | losses | payroll_definition | payroll_usd | revenue_definition | revenue_usd | valuation_usd | operating_income_usd | efficiency_metric | formula | source_url | accessed_on | confidence | notes
```

Recommended derived fields, calculated only after the source fields are frozen:

- `payroll_per_win = payroll_usd / wins`
- `revenue_per_win = revenue_usd / wins`
- `operating_income_per_win = operating_income_usd / wins`
- `revenue_to_payroll = revenue_usd / payroll_usd`

These are **derived**, not reported facts. Keep regular-season win totals separate from payroll season labels and from Forbes' valuation/revenue year. Never mix Forbes estimated revenue with a team's audited filing without labeling the change in definition.

## What to archive for reproducibility

- The original Forbes URL, page title, publication date, and any chart/table label.
- A local citation note or screenshot for dynamic/paywalled pages; do not silently transcribe a changed page.
- The exact Spotrac field selected and whether it includes dead money, retained salary, or tax charges.
- NBA Stats/Basketball-Reference season and stat-table names.
- A calculation sheet that shows formulas and leaves source and derived columns distinct.
