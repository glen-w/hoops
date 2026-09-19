# Basketball Numbers Landscape: Baseline Understanding

**Purpose:** One-page orientation for the open basketball data ecosystem. For comprehensive source details, see [DATA-REPOS.md](DATA-REPOS.md).

---

## The Lay of the Land

Basketball analytics sits at the intersection of **historical box-score abundance** (Basketball-Reference back to 1946), **modern league APIs** (NBA Stats ~1996–present for play-by-play), **tracking proprietary islands** (SportVU/Second Spectrum—cite, don't redistribute), and a **thriving open-source tooling layer** (`nba_api`, `hoopR`, `nbastatR`).

### What We Have

**Season aggregates are solved.** Basketball-Reference covers decades of team/player box scores and advanced metrics (pace, eFG%, TOV%, etc.). NBA Stats API adds modern endpoints. Both are scrapable for research; neither licenses wholesale commercial database redistribution.

**Play-by-play is recent but rich.** ESPN-derived feeds (via `hoopR`/sportsdataverse) go back to ~2002. NBA Stats PBP reaches ~1996 for some data types. Convenient GitHub mirrors exist (`shufinskiy/nba_data`, `hoopR-data`) but inherit upstream NBA ToS—use for local analysis, not commercial products.

**College and international are spottier.** Barttorvik offers free efficiency CSVs for NCAA D1. KenPom is paywall. EuroLeague has an unofficial but functional API. FIBA is mostly paywalled.

**Tracking is proprietary.** SportVU (2013–16 era) and Second Spectrum (current NBA vendor) are league/vendor products. Public "dumps" of SportVU from that era exist in the wild but carry legal/ToS ambiguity—**cite papers, don't commit tracking data to this repo.**

**Packages are excellent.** Python's `nba_api` and `basketball_reference_scraper` are P0. R's `hoopR` is a Swiss Army knife (ESPN PBP, NBA Stats, Basketball-Reference scrapers, KenPom with subscription, WNBA via `wehoop`, college). `BasketballAnalyzeR` is in our Zotero analytics collection and aligns with the Zuccolotto/Manisera *Basketball Data Science* textbook.

### What We Don't Have (Yet)

- **Standardized front-office efficiency tables.** Forbes payroll/wins/attendance are cited in the draft (`efficiency / table` placeholder); we need to pull and commit our own derived series.
- **Open gambling odds.** Narrative in the fans chapter; no dataset per ROADMAP "out of scope."
- **Gender-comparative depth.** WNBA PBP exists (`wehoop`); we haven't pulled it yet.
- **Salaries cleanly versioned.** Basketball-Reference contracts are scrapable but need periodic snapshots committed to `data/` with date stamps.

### What's Parked

- **Wyatt Walsh Kaggle basketball SQLite** (~1946–2024, huge)—later/auth required per ROADMAP.
- **Spotrac bulk scrape**—ToS explicitly forbids it; cite individual HTML pages only.

---

## How to Use This Landscape

1. **For quick reference:** See [open_datasets.csv](open_datasets.csv) (~30 rows: name, URL, grain, coverage, access, priority).
2. **For detail:** Read [DATA-REPOS.md](DATA-REPOS.md) (full source descriptions, packages, ToS notes, P0 list).
3. **For provenance:** Check [ZOTERO-DATASET-MENTIONS.md](../uploads/ZOTERO-DATASET-MENTIONS_bb21.md) (gap analysis: our Zotero `hoops/⭐analytics` is method-heavy, tooling-thin; new `data sources` subfolder seeded).

---

## P0 for This Repo (Quick List)

1. Basketball-Reference season aggregates (already feeding `avg_game_by_decade`)
2. `nba_api` or `hoopR` for modern NBA Stats pulls
3. Basketball-Reference scrapers (`basketball_reference_scraper`, `ballr`, `hoopR bref_*`)
4. `hoopR-data` or `shufinskiy/nba_data` for PBP research
5. Barttorvik CSVs (college without KenPom paywall)
6. EuroLeague API / `py-euroleague` (international)
7. `wehoop` / `sportsdataverse-py` WNBA
8. Basketball-Reference contracts (payroll/FO efficiency)
9. NBA Draft Combine via NBA Stats (anthropometrics)
10. `awesome-nba-data` (living index)

**Key constraint:** NBA ToS allows personal/research/news use but prohibits comprehensive database mirrors for commercial/gambling redistribution. **Derive tables locally, cite the source, commit only what's allowed.**

---

## Access Philosophy

| Flag | Meaning |
|------|---------|
| **open-tool** | Package/API usable; upstream may still limit republication |
| **cite-scrape** | Public HTML/tables; polite scrape OK for research; no bulk commercial redistribution |
| **bulk-mirror** | Third-party GitHub/Kaggle dump; check inherited ToS |
| **paywall** | Subscription required |
| **proprietary** | Tracking/vendor; cite narrative only |
| **later** | Parked per ROADMAP (e.g., Kaggle auth) |

**P0** = baseline for manuscript reproducibility. **P1** = thicken next. **cite-only** = map but don't use yet.

---

## Next Steps

- **Expand `data/` with committed snapshots:** salaries, draft combine anthro, Barttorvik college ratings, WNBA box scores.
- **Document each committed dataset** with source URL, scrape/download date, license, and any transformations applied.
- **Cross-reference DATA-REPOS.md from the analytics chapter** when drafting "state of the data" narrative (ROADMAP section 5).
- **Maintain Zotero `data sources` subfolder** (`I5MN75D8`) as the tooling bibliography; tag new finds `hoops-data-landscape`.

---

## Cross-References

- [DATA-REPOS.md](DATA-REPOS.md)—comprehensive source catalog
- [open_datasets.csv](open_datasets.csv)—structured table
- [ROADMAP.md](../ROADMAP.md)—repo priorities and out-of-scope items
- [Open Data Landscape Brief](../uploads/OPEN-DATA-LANDSCAPE_7cbd.md)—2026-09-19 baseline with P0 recommendations
- [Zotero Dataset Mentions](../uploads/ZOTERO-DATASET-MENTIONS_bb21.md)—library gap analysis
