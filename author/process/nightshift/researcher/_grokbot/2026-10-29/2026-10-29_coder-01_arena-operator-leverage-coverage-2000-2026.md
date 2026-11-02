# Arena operators and REITs: debt-to-equity, leverage and interest coverage, 2000–2026 (source documentation)

Request: 2026-10-28-watch-r1-coder-01 · Night 2026-10-29 · Supports `arena_financing_post2010.csv`
**Extends** `2026-10-28/out/2026-10-28_coder-03_*`. That covers the instrument-level debt table and the raw XBRL debt/capex series (273 rows). This file adds **ratios, interest coverage, VICI, and EPR for 2000–2008 (pre-XBRL)**.
Data: `2026-10-29_coder-01_arena-operator-leverage-coverage-2000-2026.csv` / `.parquet`. There are 98 entity-year rows; scripts are in `work/c1.py` and `work/c1b.py`.

## Method
- **Source.** SEC XBRL companyfacts at `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, fetched with a declared User-Agent. VICI was fetched 2026-10-29; the other CIKs reuse the 2026-10-28 cache. Only 10-K facts are used, taking the latest-filed value for each period end. Duration facts need a 350–380-day window.
- **Debt.** `LongTermDebt`, falling back to `LongTermDebtAndCapitalLeaseObligations`, then `DebtInstrumentCarryingAmount`, then `LongTermDebtNoncurrent` plus `LongTermDebtCurrent`. The tag actually used is recorded in `debt_tag`. Operating-lease liabilities are excluded.
- **Equity.** `StockholdersEquity` (parent), falling back to equity including NCI.
- **Ratios:**
  - `debt_to_equity` = debt / equity. It is negative when equity is negative; see the `equity_negative` flag.
  - `debt_to_assets` = debt / `Assets`.
  - `interest_coverage_ebit` = `OperatingIncomeLoss` / `InterestExpense` (falling back to `InterestExpenseNonoperating` or `InterestExpenseDebt`).
  - `interest_coverage_ni_plus_int` = (`NetIncomeLoss` + interest) / interest. This is the better metric for REITs, which don't report operating income consistently.
- **Pre-XBRL EPR (2000–2008).** Hand-keyed from Item 6 Selected Financial Data:
  - 2000–03 from the FY2004 10-K: https://www.sec.gov/Archives/edgar/data/1045450/000095013705002690/c92844e10vk.txt
  - 2004–08 from the FY2008 10-K (restated): https://www.sec.gov/Archives/edgar/data/1045450/000095013709001267/c49499e10vk.htm
  - The EBIT proxy is income before minority interests, JVs and gains, plus interest expense, net.

## Entities and SEC URLs
| Entity | CIK | Years in file | Filing index root |
|---|---|---|---|
| Madison Square Garden Company 2010–15 (CIK now MSG Networks; rows after 2015 relabelled as **not an arena operator**) | 1469372 | 2008–2020 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1469372&type=10-K |
| MSG Sports (EDGAR: MSG Knickerbockers Corp.) | 1636519 | FY2013–FY2026 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1636519&type=10-K |
| Sphere Entertainment (MSG Entertainment 2020–23) | 1795250 | FY2018–2025 | …CIK=1795250 |
| MSG Entertainment (2023 spin; owns MSG arena) | 1952073 | FY2021–FY2026 | …CIK=1952073 |
| Live Nation | 1335258 | 2009–2025 | …CIK=1335258 |
| EPR Properties (REIT) | 1045450 | 2000–2025 | …CIK=1045450 |
| VICI Properties (REIT) | 1705696 | 2017–2025 | …CIK=1705696 |
| Atlanta Braves Holdings | 1958140 | 2022–2025 | …CIK=1958140 |
Each row's `filing_index_url` and `accessions` point to the exact 10-K(s).

## Headline readings (as tagged)
- **The MSG family runs negative equity after the spins.** MSGS has had negative equity since FY2020 (D/E about −0.9 to −1.7) while debt/assets is only 0.16–0.28. Its coverage fell from 7.3× (FY2022) to 0.7× (FY2025) and 1.4× (FY2026). MSG Entertainment (2023 spin) has thin or negative equity (D/E swings from −444 to +11.8) and coverage of about 2–3.5×. **For these entities, debt/assets is the meaningful leverage measure.**
- **Live Nation.** D/E rose from 1.3 to 2.9 (2010–19), equity turned negative in 2020–23, and coverage was about 2.5–4× in 2022–25 after negative years in 2020–21.
- **EPR.** D/E 0.94–1.40 and debt/assets 0.41–0.55 over 2000–2025. NI-plus-interest coverage was mostly 2.1–3.4×, collapsing to 0.16× in COVID 2020.
- **VICI.** D/E about 0.6 and debt/assets about 0.36, with NI-plus-interest coverage of 3.1–4.3× (2018–25).
- **Braves Holdings.** D/E 1.1–1.8 and debt/assets 0.36–0.46; operating income does not cover interest (−0.3 to −1.2×).

## Caveats and gaps
- **VICI's `OperatingIncomeLoss`** (2017–20 only) looks segment-level and implausible against revenue, so it is excluded. Use `interest_coverage_ni_plus_int`.
- Sphere's FY changed to Dec in 2024, giving a transition row. FY2023 has no interest tag.
- **2000–2008 gap for non-REITs (GAP).** MSG was inside Cablevision until 2010, consolidated with cable, so it is not separable. Live Nation's predecessors (SFX Entertainment 1998–2000, then Clear Channel) were not pulled. Other pre-2009 listed team or arena entities (Ascent Entertainment/Pepsi Center to 2000, Boston Celtics LP, Florida Panthers Holdings) were not pulled. CIKs not verified tonight.
- These are company-level ratios, not arena-project leverage. Team, arena and media debts are mixed, especially at MSG and Live Nation.
- Treat these figures as accurate only to the extent that the companies tagged them correctly in XBRL. Spot-check against the 10-K before quoting any single figure.
