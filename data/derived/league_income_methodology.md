# League income ingredients — methodology

**Pack:** `hoops-league-income-2026-09-19`  
**Target:** `glen-w/hoops` sidecar only (`data/derived/` candidate)  
**Access / as_of date:** 2026-09-19 (Europe/Paris)  
**Scope:** first **derived** table of publicly responsible “income ingredients” for recent seasons — not a BRI audit, not a full P&L.

## What this pack is

A long CSV of **sourced facts** that feed a writer-facing “where does the money come from?” stack:

| Ingredient family | Status in this pack |
|-------------------|---------------------|
| National media / TV rights (partners, term, published dollars) | Tabulated |
| Salary cap / tax / apron thresholds (BRI-*related* public rules) | Tabulated |
| Industry-reported BRI / gross revenue (Sportico) | Tabulated with MEDIUM confidence |
| League regular-season attendance | Tabulated (official where available) |
| Licensing, arena/gate dollars, local media, sponsorship rollups | Explicit **GAP** rows |

**Skipped by brief:** gambling; Kaggle; invented numbers; Scrivener edits.

## Source allow-list (used)

| Source | Role |
|--------|------|
| [NBA.com / NBA Communications](https://pr.nba.com/) | OFFICIAL partners/terms for media deals; OFFICIAL salary-cap releases; OFFICIAL attendance records |
| [CNBC](https://www.cnbc.com/2024/07/24/nba-picks-amazon-for-media-rights-over-warner-bros-discovery.html) | SECONDARY partner annual fees and ~$77B package framing |
| [Sportico](https://www.sportico.com/leagues/basketball/2025/nba-revenue-projected-2025-26-season-1234876505/) | SECONDARY BRI, projected gross revenue, per-team national TV payouts |
| [Sports Illustrated](https://www.si.com/nba/2014/10/06/new-nba-tv-deal-worth-24-billion) | SECONDARY ~$24B / ~$2.6B AAV for 2016–25 cycle |
| [Spotrac CBA / Cap History](https://www.spotrac.com/nba/cba/) | Cross-check only for published cap maxima (not a primary dollar claim here) |
| [Sports Business Journal](https://www.sportsbusinessjournal.com/Articles/2025/04/15/nba-has-second-highest-season-attendance-mark-ever/) | SECONDARY 2024–25 attendance average |

## Confidence labels

| Label | Meaning |
|-------|---------|
| **HIGH** | Number or partner/term text taken from an official NBA release (or unambiguous historical table inside one). |
| **MEDIUM** | Credible secondary journalism (CNBC, Sportico, SI, SBJ) citing unnamed sources, people familiar, or industry tallies. Preserve published wording; do not invent reconciliations. |
| **GAP** | No responsible public figure located this pass; value left blank. |

## Non-negotiable interpretation rules

1. **Contract value ≠ recognized annual league revenue ≠ BRI.**  
   Rights fees are contract facts. BRI is a CBA accounting construct (Article VII). Cap is a rule threshold derived from BRI projections/smoothing — **not** “what the league earned.”
2. **Attendance ≠ ticket revenue.** Volume only. Gate dollars need price/mix assumptions or private disclosures.
3. **$76B vs ~$77B.** Both appear in secondary coverage of the 2025–36 media cycle. CNBC uses “about $77 billion”; Sportico uses “$76 billion.” Rows cite their source; **do not average**.
4. **Partner splits** (Disney $2.62B / NBCU $2.45B / Amazon ~$1.8B per year) are CNBC “people familiar” figures, **not** in the official NBA announcement.
5. **Escalators.** New-deal annual averages mask year-to-year steps (Sportico notes ~7%/yr average per-team TV growth). Early-season receipts ≠ AAV.
6. **WNBA bundling.** Some secondary tallies may include concurrent WNBA rights in a combined package figure. Flag when using totals in prose.
7. **No invented arithmetic.** Example: 2024–25 total attendance is *not* filled as `18147 × 1230` because the source only said the total “exceeded 22.3 million.”

## How rows were chosen

- **Media rights:** Official PR for *who* and *when*; secondary press for *how much* when the league does not publish dollars.
- **Cap / tax / aprons:** Official season announcements for 2022–23 through 2025–26 (recent seasons anchoring the new-media transition).
- **BRI / revenue:** Only Sportico figures that are explicitly labeled BRI or gross/projected revenue in the cited article — one source chain, clearly MEDIUM.
- **Attendance:** Official 2023–24 release (includes multi-year comparison table) plus SBJ for 2024–25 average only.
- **Gaps:** Explicit empty-value rows for licensing, arena gate dollars, local media, and sponsorship/patch leaguewide totals.

## What is still missing (by design)

- Audited BRI Audit Report line items  
- League-wide licensing / merchandising receipts  
- League-wide ticket, suite, concessions, parking (arena) dollars  
- Team-by-team local media rights fees  
- Current sponsorship / jersey-patch league rollup  
- International media beyond the domestic national packages cited  
- Actual player payroll sums (cap thresholds only; Spotrac/ESPN payrolls are a separate derived job)

## Relationship to earlier sidecar notes

This pack **implements** the empty schema sketched in `hoops-thicken-efficiency-income-2026-09-19/SCHEMA-sketch.md` (`league_income_component.csv`) and the source map in `hoops-thicken-2026-09-19/league-income-sources.md`. It does not replace those notes; it is the first populated ingredients CSV. Column names follow the brief (`season,category,value,unit,currency,source_url,as_of,confidence,notes`).


## Suggested repo landing path

`data/derived/league_income_ingredients.csv`  
with this `methodology.md` (or a slim `SOURCES.md`) beside it.
