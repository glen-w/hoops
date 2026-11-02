# coder-03 — Arena / venue-operator debt & equity financing, 2000–2026

Night: 2026-10-28 (Grok Bot nightshift). Fetched 2026-10-28 from SEC EDGAR (10-Ks and XBRL companyfacts) plus company and law-firm releases.
Files:
- `2026-10-28_coder-03_arena-operator-debt-equity.csv`: 25 instrument-level rows (facility, outstanding, dates, maturity, security, source, confidence).
- `2026-10-28_coder-03_sec-xbrl-debt-capex-series.csv`: 273 rows of XBRL year-end series (LongTermDebt, DebtInstrumentCarryingAmount, PP&E capex, debt proceeds/repayments) for MSGS, Sphere, MSGE, the old MSG Co., Live Nation, Braves Holdings and EPR. The accession shown is the latest 10-K reporting that period.
- `.parquet` versions of both.

## Bottom line

1. **Only the MSG family gives you a listed NBA-arena balance sheet**, and since 2020/2023 it is split three ways.
   - **MSG Entertainment (MSGE)** owns the Garden and carries **arena-level debt**: the National Properties term loan, **$609.4M** refinanced Jun 2025 to 2030, ~$548M outstanding at 30 Jun 2026, plus a $150M revolver.
   - **MSG Sports (MSGS)** owns the Knicks/Rangers and borrows at **team level** against league media money: a Knicks $425M revolver ($242M drawn) and a Rangers $250M revolver (undrawn). The teams rent the arena under **35-year license agreements to 2055**.
   - **Sphere Entertainment** carries the Las Vegas Sphere and the distressed MSG Networks loan. The latter was restructured Jun 2025 from ~$829M to ~$159M principal, after cutting the Knicks/Rangers TV fees.
   - The **2011–13 Garden Transformation (~$1B)** was cash-funded with no project debt (MSG 10-K FY2013).
2. **Live Nation is the debt-heavy venue operator**: **$8.27B** principal at end-2025, up from $6.49B. It leans on convertibles ($1.0B 2029, $1.1B 2030, $1.4B 2031) and a $1.3B TLB. Capex hit **$1.06B** in 2025. These are mainly amphitheatres, clubs and new venues, not NBA arenas.
3. **Atlanta Braves Holdings** is the clean public comparator for "team + surrounding real estate". It has $739M of debt, about two-thirds in the Battery mixed-use development, while the ballpark itself is publicly owned (Cobb County). MLB, not NBA.
4. **The REITs are not in arenas.** The EPR and VICI FY2025 10-Ks contain **zero** mentions of "arena". Arena real estate is not a listed asset class; it sits with municipalities, teams or private operators.
5. **The private operators are a disclosure black hole**:
   - **Legends + ASM Global** (Sixth Street-controlled) runs on a **$1.85B private-credit package** (Ares/KKR-led unitranche, Aug 2024).
   - **Oak View Group** used a ~$500M construction loan, later refinanced into a private investment-grade bond, for Climate Pledge Arena, plus a **$100M Silver Lake** equity stake (2018).
   - **AEG** and **Comcast Spectacor** disclose nothing at arena level.
   - Those figures come from law-firm/company releases and trade press, not filings. Treat them as MEDIUM at best.

## Being honest about what is private

| Entity | Status | What we can say |
|---|---|---|
| AEG | private (Anschutz) | Nothing on arena debt/equity; only that it sold its ASM stake (2024) |
| Legends / ASM Global | private | Deal-level debt package from the lenders' counsel release; no ongoing balances |
| OVG | private | Investor and construction-loan headlines only; "$5.5B for five venues" is press [unverified] |
| Comcast Spectacor | inside Comcast | Wells Fargo Center spending not broken out |
| Most NBA team arena companies | private | Debt is visible only when it's municipal (EMMA) or reported in press. See coder-01 and researcher-01 (AAC's ~$215M private placement). |

## Next steps

- EMMA (municipal) for team-side conduit debt: Barclays PILOT 2016 refi, Chase Center (none), Fiserv (WCD bonds).
- Pull Sphere's total Sphere construction cost (~$2.3B reported [unverified]) from 10-K capex history; FY2020–22 capex is in the XBRL series CSV ($455M / $456M / $757M).
- If useful for *Hoops*: MSGS spin-off of the Rangers (authorised Feb 2026) will split team-level debt again. Watch the Form 10.
