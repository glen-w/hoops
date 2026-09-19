# Basketball Numbers Landscape: Baseline Understanding

**Purpose:** One-page orientation for the open basketball data ecosystem. For comprehensive source details, see [DATA-REPOS.md](DATA-REPOS.md).

---

## The Lay of the Land

Basketball analytics sits at the intersection of **historical box-score abundance** (Basketball-Reference back to 1946), **modern league APIs** (NBA Stats ~1996–present for play-by-play), **tracking proprietary islands** (SportVU/Second Spectrum/Hawk-Eye—cite, don't redistribute), and a **thriving open-source tooling layer** (`nba_api`, `hoopR`, `nbastatR`).

**Hard rules for this repository:** Kaggle warehouses are **later/parked**. Client MIT license ≠ data redistribution rights. SportVU GitHub dumps are **legal caution—do not vendor**.

### What We Have

**Season aggregates are solved.** Basketball-Reference covers decades of team/player box scores and advanced metrics (pace, eFG%, TOV%, BPM, WS, VORP, etc.). NBA Stats API adds modern endpoints (prefer V3 PBP/scoreboard). Both are scrapable for research with etiquette (Sports Reference: ~20 req/min); neither licenses wholesale commercial database redistribution or AI training without written permission.

**Play-by-play is recent but rich.** ESPN-derived feeds (via `hoopR`/sportsdataverse) go back to ~2002 (through 2026). NBA Stats PBP reaches ~1996 for some endpoints. Convenient GitHub mirrors exist (`shufinskiy/nba_data`, `hoopR-data`) but inherit upstream NBA ToS—**use for local analysis; do NOT vendor the full mirror into this repo's `data/` directory** (violates NBA comprehensive DB restriction).

**College and international are spottier.** Barttorvik offers free public efficiency CSVs (`{year}_team_results.csv`) for NCAA D1—best open college metric. KenPom is paywall (subscription + paid API; `hoopR` supports with active sub). EuroLeague has an unofficial but widely-used API (`py-euroleague`). FIBA GDAP is mostly paywalled (auth subscription).

**Tracking is proprietary with legal caution.** SportVU (2013–16 era), Second Spectrum (~2017–2023), and Hawk-Eye (~2023–present) are league/vendor products. Public "dumps" of SportVU 2015–16 data exist on GitHub (`neilmj/BasketballData` and mirrors) but carry **legal gray area / proprietary caution**—briefly public then withdrawn. MIT license on parsing *code* ≠ data redistribution rights. **Cite papers and methods only; do NOT commit tracking data to this repo or vendor it.** Safe alternative: NBA Stats tracking *aggregates* (LeagueDashPtStats, hustle, speed/distance summaries) and ShotChartDetail coordinates.

**Packages are excellent.** Python's `nba_api` (prefer V3 endpoints) and `basketball_reference_scraper` are P0. R's `hoopR` is a Swiss Army knife (127+ NBA wrappers: ESPN PBP, NBA Stats, Basketball-Reference `bref_*` scrapers, KenPom with subscription, WNBA via `wehoop`, college Torvik). `nbastatR` is R front-office oriented. `BasketballAnalyzeR` is in our Zotero analytics collection (BB4SV25F) and aligns with the Zuccolotto/Manisera *Basketball Data Science* textbook.

### What We Don't Have (Yet)

- **Standardized front-office efficiency tables.** Forbes payroll/wins/attendance are cited in the draft (`efficiency / table` placeholder); we need to pull and commit our own derived series.
- **Open gambling odds.** Narrative in the fans chapter; no dataset per ROADMAP "out of scope."
- **Gender-comparative depth.** WNBA PBP exists (`wehoop`); we haven't pulled it yet.
- **Salaries cleanly versioned.** Basketball-Reference contracts are scrapable but need periodic snapshots committed to `data/` with date stamps.

### What's Parked

- **Wyatt Walsh Kaggle basketball SQLite/nbadb** (claims 1946–present; star-schema warehouse)—later/auth required + ToS considerations per ROADMAP section 6.
- **Nathan Lauga Kaggle nba-games** (~2004–present)—parked per project policy.
- **Other Kaggle NBA warehouses**—parked per project policy.
- **Spotrac bulk scrape**—ToS explicitly bans scraping/data mining; cite individual HTML pages only.
- **KenPom**—cite-only unless active subscription available.
- **BigDataBall / NBAstuffer data shop**—commercial; cite-only.
- **Cleaning the Glass**—subscription required (~$5/mo); cite-only.

---

## How to Use This Landscape

1. **For quick reference:** See [open_datasets.csv](open_datasets.csv) (~30 rows: name, URL, grain, coverage, access, priority).
2. **For detail:** Read [DATA-REPOS.md](DATA-REPOS.md) (full source descriptions, packages, ToS notes, P0 list).
3. **For provenance:** Check [ZOTERO-DATASET-MENTIONS.md](../uploads/ZOTERO-DATASET-MENTIONS_bb21.md) (gap analysis: our Zotero `hoops/⭐analytics` is method-heavy, tooling-thin; new `data sources` subfolder seeded).

---

## P0 for This Repo (Quick List)

**Priority 0 (baseline for manuscript tables & reproducibility):**

1. **Basketball-Reference season aggregates**—already feeding `avg_game_by_decade`; BPM/WS/VORP; Sports Reference etiquette (~20 req/min)
2. **`nba_api` (Python)** — [github.com/swar/nba_api](https://github.com/swar/nba_api) — live stats.nba.com; prefer V3 PBP/scoreboard; document NBA ToS (no full DB publish)
3. **`hoopR` (R)** — [hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/) — R parity; 127+ NBA wrappers; ESPN + NBA Stats + `bref_*`
4. **`basketball_reference_scraper` / `ballr` / `hoopR bref_*`**—advanced metrics & historical depth; SR etiquette
5. **`hoopR-data` or `shufinskiy/nba_data`**—PBP research lane; **local analysis only; don't vendor the mirror** (flag NBA ToS)
6. **Barttorvik CSVs** — [barttorvik.com](https://barttorvik.com/) — public `{year}_team_results.csv`; college without KenPom paywall
7. **EuroLeague API / `py-euroleague`**—international grain beyond NBA/FIBA GDAP; unofficial but widely used
8. **`wehoop` / `sportsdataverse-py` WNBA**—gender/league comparison chapters
9. **Basketball-Reference contracts + NBA Draft Combine**—FO payroll tables & anthropometrics; combine via `hoopR` `nba_draftcombinestats` or `nba_api`
10. **awesome-nba-data** — [github.com/JovaniPink/awesome-nba-data](https://github.com/JovaniPink/awesome-nba-data) — living index + ToS matrix

**Key constraints:**
- **NBA ToS:** Personal/research/news use OK; **no comprehensive regularly-updated public database mirrors** or commercial/gambling redistribution without consent.
- **Sports Reference:** ~20 req/min polite scraping; no competing DB or AI training without written permission.
- **SportVU dumps:** Legal gray area—**do not vendor**; cite papers/methods only.
- **Derive tables locally, cite the source, commit only what's allowed.**

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

- [DATA-REPOS.md](DATA-REPOS.md)—comprehensive source catalog (season aggregates, PBP, packages, college/intl, salaries, tracking, GitHub, paywalled, P0 list)
- [open_datasets.csv](open_datasets.csv)—structured table (35 sources)
- [ROADMAP.md](../ROADMAP.md)—repo priorities and out-of-scope items
- [Open Data Landscape Brief](../uploads/OPEN-DATA-LANDSCAPE_14b2.md)—2026-09-19 (CEST) baseline with access flags and P0 recommendations
- [Zotero Dataset Mentions](../uploads/ZOTERO-DATASET-MENTIONS_819c.md)—library gap analysis (analytics method-heavy, tooling thin; `hoops → data sources` subfolder seeded)
