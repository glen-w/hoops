# Analysis roadmap: MEDIA, FIN, STADIUM (biggest holes)

**Status:** 2026-10-23. Hoops status: MEDIA 7%, FIN 10%, STADIUM 20%.  
**Approach:** Library first (Zotero + hoops_reads), then structured nightshift requests for gaps.

---

## MEDIA (7% complete)

### What's in library
- 2016-24 national media deals: ABC/ESPN/TNT nine-year agreements (pr.nba.com 2014-10-06, confirmed via league_income_sources.md)
- Pre-2020 context: jersey patch program launch 2017-18, Warriors-Rakuten $60M (cite from existing Zotero)
- RSN structure pre-2023 (fragmentary; Sinclair, Diamond Sports context partial)

### Library gap (confirmed 2026-10-23)
- **2024-25 streaming split:** Amazon Prime, Apple TV+, ESPN+ carriage. Paperful_ask 0 results. Researcher must source from pr.nba.com releases, SEC filings (Disney 10-K, Amazon Q4), trade press (Variety, Sports Business Journal).
- **Sponsorship inventory:** Current arena naming rights by team + values. Current jersey patch contracts by team. Pre-2020 only in library. Researcher must source from team websites, Spotrac, league PRs, or mark out-of-scope.
- **RSN bankruptcy:** Sinclair/Diamond/Bally post-2023. No academic literature. Gray sources (SEC, Bloomberg, trade press) acceptable if researcher sourced.

### Coder next steps
1. After researcher sources 2024-25 streaming split: build media_income_ingredients.csv (parallel to league_income_ingredients.csv). Columns: year, category (national TV, streaming, sponsorship, licensing), partner, value, currency, source_url, as_of, confidence.
2. Build arena_naming_rights.csv (by team, contract start/end, value, source).
3. Summarize MEDIA chapter structure: [National TV deals] → [Streaming split] → [Sponsorship (naming + jersey patch)] → [Local licensing].

---

## FIN (10% complete)

### What's in library
- Salary cap / tax / apron history 2016-17 to 2026-27 (hoops_derived, pr.nba.com official, corrected 2026-10-23)
- League income ingredients (BRI, media, attendance, licensing) 2016-17 to 2024-25 (league_income_sources.md, source graded)
- Pre-2010 arena financing patterns (Propheter, Groothuis, Humphreys/Nowak, Irizarry cited in existing Zotero)
- Gate, licensing, sponsorship macro context (partial; values dated)

### Library gap (confirmed 2026-10-23)
- **Post-2010 arena subsidy cases:** Vegas Allegiant (2020), SoFi (2020), Crypto.com (2019), Intuit (2024). 9 Zotero keys pending researcher validation. Need: public subsidy %, total cost, financing breakdown. Fallback: paperful_ask per venue for architectural/financing context.
- **Post-2010 sponsorship detail:** Patch program ROI by team 2017-24. Naming rights by franchise historical trend 2010-25. Library pre-2020 only.
- **Local revenue splits:** Market-by-market gate, suites, club revenue (proprietary; may be out-of-scope).

### Coder next steps
1. After researcher validates 9 Zotero arena keys: extract subsidy %, total cost, public vs. private split. Build arena_financing.csv (venue, year, total cost, public subsidy $, subsidy %, financing structure, source_url).
2. Cross-check with hoops_record arena path outputs (debug 2026-10-24).
3. Build FIN chapter spine: [Salary cap history & mechanics] → [League income ingredients 2016-24] → [Arena financing pre-2010 patterns] → [Post-2010 case studies (if library sources)] → [Sponsorship trends].

---

## STADIUM (20% complete)

### What's in library
- Pre-2010 arena design & capacity trends (Irwin & Sandvoss, Humphreys/Nowak cited)
- Capacity by era (pre-1960s, 1960s-1990s, post-2000)
- Amenity categories (suites, club seating, concourse, premium)

### Library gap (confirmed 2026-10-23)
- **Post-2010 new builds:** Architectural features, seating inventory, design philosophy. SoFi (2020), Crypto.com (2019), Intuit (2024), Vegas Allegiant (2020), Milwaukee/Fiserv (2018). Researcher must source from venue whitepapers, architectural firms (Manica, Populous), team/city press releases, or trade press (Architect Magazine, venue trade journals).
- **Design cost per seat:** Modern builds ($500–800k per seat typical, not in library). Researcher to source from construction data, consulting reports, or academic analyses.
- **Crowd experience literature:** Post-COVID venue management, crowd density, wayfinding. Sparse in academic library; gray sources acceptable.

### Coder next steps
1. After researcher sources post-2010 builds: extract key data (year, capacity, signature feature, cost per seat, primary architect). Build stadium_features.csv (venue, year, capacity, suites, club, signature_feature, design_philosophy, cost_total, cost_per_seat, source_url).
2. Build STADIUM chapter spine: [Pre-2010 evolution: capacity, amenity categories] → [Design philosophy by era] → [Post-2010 new builds (if sourced)] → [Crowd experience elements].

---

## Consolidated Next Actions

### Researcher (2026-10-24+)
- [ ] Validate 9 Zotero arena subsidy keys (Vegas, SoFi, Crypto.com, Intuit); extract subsidy %, costs
- [ ] Source 2024-25 MEDIA streaming split (pr.nba.com, SEC filings)
- [ ] Source MEDIA sponsorship inventory (naming rights + jersey patch by team, current)
- [ ] Source STADIUM post-2010 new builds (architecture, cost, design feature by venue)
- [ ] Update hoops/nightshift_requests.json with findings

### Coder (after researcher sources)
- [ ] Debug hoops_record arena path (test Vegas case 2026-10-24)
- [ ] Build media_income_ingredients.csv (parallel structure to league_income_ingredients.csv)
- [ ] Build arena_financing.csv from Zotero + hoops_record validation
- [ ] Build arena_naming_rights.csv from researcher sourcing
- [ ] Build stadium_features.csv from researcher sourcing
- [ ] Summarize chapter spines in analysis/ for researcher integration into Scrivener

---

## Library-First Rule

**No invented numbers or sources.** If researcher cannot source from library or verified gray sources:
- Mark as "out-of-scope" in chapter notes
- Cite what IS available (pre-2010 patterns, macro trends, illustrative cases)
- Flag the gap in endnotes

Example: "Modern arena financing (post-2010) remains largely proprietary; this section draws on published subsidies for [Vegas, SoFi, Crypto.com] and pre-2010 patterns [Propheter, Humphreys/Nowak]."
