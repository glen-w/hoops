# League income sources

**Research cut-off:** 2026-09-19 (Europe/Paris). **Purpose:** public source map for NBA TV deals, salary totals, attendance, licensing, and arena revenue. Kaggle is excluded. Amounts below are reported by the linked sources; no unlinked estimates are introduced.

## Source register

| Topic | Source | Label | What it supports / limits |
|---|---|---|---|
| Current national media rights | [NBA, "NBA signs new 11-year media agreements with Disney, NBCUniversal and Amazon Prime Video through 2035-36 season," 24 Jul 2024](https://www.nba.com/news/nba-media-agreements-2024) | **OFFICIAL** | Primary announcement for the 2025-26 through 2035-36 package, partners, distribution and game-volume terms. It does not publish a team-by-team revenue allocation or audited annual league revenue. |
| Previous national media rights | [Forbes, 2016 NBA valuation release](https://www.forbes.com/sites/forbespr/2016/01/20/forbes-releases-18th-annual-nba-team-valuations/) | **SECONDARY** | Reports the nine-year, $24bn ESPN/ABC–TNT agreement discussed in the 2016 valuation context. Treat the figure as a published secondary report and preserve the contract-period wording. |
| Previous national media rights, primary announcement | [NBA Communications, "NBA extends partnerships with The Walt Disney Company and Turner Broadcasting System through 2024-25 season"](https://pr.nba.com/nba-partnerships-walt-disney-company-turner-broadcasting-system/) | **OFFICIAL** | Primary announcement for the nine-year extension covering 2016-17 through 2024-25, naming Disney/ABC/ESPN and Turner/TNT. The official release is the safer source for partners and term; use Forbes or other secondary reporting only for the dollar estimate. |
| CBA revenue definition | [2023 NBA–NBPA Collective Bargaining Agreement, Article VII](https://imgix.cosmicjs.com/25da5eb0-15eb-11ee-b5b3-fbd321202bdf-Final-2023-NBA-Collective-Bargaining-Agreement-6-28-23.pdf) | **OFFICIAL** | Primary rulebook for Basketball Related Income (BRI), salary-cap calculations, designated share, accounting treatment, and relevant revenue categories. Use the PDF page/article/section, not a blog paraphrase. |
| CBA-readable index | [CBA Guide, League Finances](https://cbaguide.com/finances/) | **SECONDARY** | Navigable explanation of Article VII. Useful for locating tickets, concessions, parking, licensed products, suites and naming-rights provisions; cite the CBA itself for final prose. |
| Historical salary-cap / team-floor totals | [NBA Communications salary-cap archive](https://pr.nba.com/tag/salary-cap/) | **OFFICIAL** | Official season-by-season cap, tax level, and minimum-team-salary announcements (including 2015-16 onward). These are league rules/thresholds, **not** actual total player payroll or total salaries paid. |
| 2016-17 salary cap | [NBA, 2016-17 salary-cap release](https://pr.nba.com/nba-salary-cap-2016-17-season/) | **OFFICIAL** | Primary season release; useful anchor for the 2016-era book material. |
| 2025-26 salary cap | [NBA, 2025-26 salary-cap release](https://pr.nba.com/nba-salary-cap-2025-26-season/) | **OFFICIAL** | Primary current-season cap, tax level, minimum team salary and apron levels. |
| Attendance | [NBA Communications, 2023-24 attendance records](https://pr.nba.com/nba-attendance-records-2023-24-regular-season/) | **OFFICIAL** | Primary release with 2023-24 total attendance, average attendance, capacity, sellouts, and historical comparison including 2015-16, 2016-17 and 2017-18. Use as the cleanest public league series. |
| Team/game attendance cross-check | [Basketball-Reference NBA standings/team pages](https://www.basketball-reference.com/leagues/NBA_2024.html) | **SECONDARY** | Cross-check for games and team season context. Do not substitute its attendance presentation for the NBA release without recording the definition. |
| Player-level salaries | [ESPN NBA salaries, 2016](https://www.espn.com/nba/salaries/_/year/2016) | **SECONDARY** | Public player-level salary list; can be summed only after defining season, guaranteed salary, options, retained salary and whether injured/released players remain in the total. |
| Team payroll accounting | [Spotrac, 2015-16 cap tracker](https://www.spotrac.com/nba/cap/_/year/2015) | **SECONDARY** | Public historical cap-accounting dataset with multiple total definitions. Good for a derived payroll table, but not an audited league total. |
| Team revenue categories / arena economics | [SEC filing: Madison Square Garden Sports FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1636519/000163651925000027/R51.htm) | **OFFICIAL** | Primary public company filing. Shows the kinds of event-related, media-rights, sponsorship/signage, suite-license and league-distribution categories disclosed by a team owner; it does not isolate Knicks-only revenue or provide a league-wide NBA total. |
| Team revenue estimates | [Forbes 2016 team valuation release](https://www.forbes.com/sites/forbespr/2016/01/20/forbes-releases-18th-annual-nba-team-valuations/) | **SECONDARY** | Historical comparable estimates for franchise value, revenue and operating income. Keep estimates separate from SEC figures and note the financial season used by Forbes. |
| Licensing structure | [NBA Properties license agreement (public PDF)](https://ipmall.info/sites/default/files/hosted_resources/SportsEntLaw_Institute/Sports%20License%20Agreements/NBA%20Properties,%20Inc._License%20Agreement.pdf) | **SECONDARY** | Public example of NBA Properties licensing terms and royalty mechanics. It is not a league-wide licensing-revenue report. |
| NBA licensing disclosure gap | [SEC EDGAR company filings search](https://www.sec.gov/edgar/search/) | **OFFICIAL** | Use filings from public team owners (for example MSG Sports) for disclosed local categories. The NBA is not a public company with a comprehensive audited annual report, so league-wide licensing and arena revenue are generally not available as one official table. |

**Access date for every URL above:** 2026-09-19 (Europe/Paris).

## What can become a derived table later

A defensible workbook can have separate tabs, rather than forcing unlike values into one "income" number:

### `media_rights_contracts`

```text
announcement_date | rights_period_start | rights_period_end | partner | package_type | territories | annual_value_usd | total_value_usd | games_or_windows | source_url | label | notes
```

Use contract values as contract facts; do not turn them into annual league revenue without a stated recognition/allocation assumption.

### `salary_cap_and_payroll`

```text
season | cap | tax_level | minimum_team_salary | first_apron | second_apron | team | payroll_definition | payroll_usd | source_url | label | notes
```

Keep official thresholds separate from player/team payroll estimates. If summing player salaries, preserve the player list and inclusion rules.

### `attendance`

```text
season | team_or_league | regular_or_postseason | games | attendance_total | average_attendance | capacity_pct | sellouts | source_url | label | notes
```

Attendance is a volume measure, not ticket revenue. A later revenue proxy must disclose ticket-price and premium-seat assumptions.

### `team_revenue_categories`

```text
fiscal_or_season_year | owner_or_team | event_revenue | media_rights | sponsorship_signage | suite_licenses | league_distributions | food_beverage_merchandise | licensing | arena_scope | currency | source_url | label | notes
```

Only populate categories explicitly disclosed by the filing/source. "Arena revenue" can include non-NBA events and shared rights; do not infer a Knicks/Celtics/Blazers team number from a whole arena or parent company.

### `licensing`

```text
season_or_fiscal_year | licensor | product_or_right | territory | royalty_or_revenue_field | amount | currency | inclusion_in_BRI | source_url | label | notes
```

The 2023 CBA changed the treatment of licensed products; record the CBA version and effective season before comparing across eras.

## Interpretation guardrails

- A media-rights contract, BRI, salary cap, player payroll, attendance, ticket revenue, sponsorship rights fees, and parent-company revenue are different measures.
- Use **OFFICIAL** only for NBA/NBPA/team-owner filings or releases; **SECONDARY** for Forbes, Sportico, Spotrac, ESPN, CBA Guide and similar; **UNCONFIRMED** for an estimate whose methodology or primary document cannot be inspected.
- No comprehensive official NBA table for league-wide licensing, arena, or team revenue was located in this pass. Mark those fields unavailable rather than backfilling with invented numbers.
