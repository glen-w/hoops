# Basketball Data Repositories & Sources

**Last updated:** 2026-09-19

This document maps the open basketball numbers landscape: datasets, APIs, Python/R packages, and key resources for reproducible basketball analytics. Access flags are practical guidance, not legal advice—always re-check terms of service before redistributing data.

**Hard rules for this repository:** Kaggle warehouses are **later/parked**. Client MIT license ≠ data redistribution rights. SportVU GitHub dumps are **legal caution—do not vendor**.

---

## Access Legend

| Flag | Meaning |
|------|---------|
| **open-tool** | Package/API usable for analysis; upstream may still restrict republication |
| **cite-scrape** | Public HTML/tables; polite scrape OK for research; weak redistribution rights |
| **bulk-mirror** | Third-party dump (GitHub/Kaggle); convenient; provenance/ToS inherited from origin |
| **paywall** | Subscription or commercial feed |
| **proprietary** | League/vendor tracking; cite narrative only |
| **later** | Useful but parked (e.g. Kaggle auth) per [ROADMAP](../ROADMAP.md) policy |

**Priority codes:**
- **P0** = baseline for manuscript tables and reproducibility in this repo
- **P1** = thicken next
- **later/cite-only** = map only; not for immediate use

---

## Season Aggregates (Box Scores, Advanced Stats, Pace)

### Basketball-Reference
- **URL:** [basketball-reference.com](https://www.basketball-reference.com/)
- **Access:** cite-scrape
- **Grain:** season/player/game/draft
- **Coverage:** BAA/NBA 1946–present
- **Priority:** P0
- **Notes:** Canonical historical source for season and advanced tables. **Already in use** for decade/avg-game tables (BPM/WS/VORP). Sports Reference [data-use page](https://www.sports-reference.com/data_use.html) and [bot-traffic policy](https://www.sports-reference.com/bot-traffic.html) apply—approximately 20 requests/minute; polite scraping for research is acceptable; **no competing database** or AI training without written permission. **Cite, don't dump full mirrors.**
- **Packages:** `basketball_reference_scraper` (Python), `ballr` (R), `hoopR` `bref_*` family (R)

### NBA Stats API (stats.nba.com)
- **URL:** [nba.com/stats](https://www.nba.com/stats)
- **Access:** open-tool
- **Grain:** season/game/player; hustle; tracking summaries; combine
- **Coverage:** Modern era; endpoint-dependent history (~1996–present for most)
- **Priority:** P0
- **Notes:** Official public endpoints. Canonical official definitions. **NBA Terms of Service:** allowed for news/private noncommercial use; **no comprehensive regularly-updated public database mirrors** or commercial gambling redistribution without consent. **Derive tables, cite the source, and don't ship full mirrors.**
- **Packages:** `nba_api` (Python), `hoopR` (R), `nbastatR` (R)
- **Best practice:** Prefer V3 endpoints (PlayByPlayV3, ScoreboardV3) over deprecated V2 where available.

### ESPN NBA Stats / Site API
- **URL:** [espn.com/nba/stats](https://www.espn.com/nba/stats) · `site.api.espn.com`
- **Access:** open-tool (unofficial ToS)
- **Grain:** leaders/box/scoreboard
- **Coverage:** Current + recent seasons
- **Priority:** P1
- **Notes:** Live leaderboards and scoreboards. Upstream of many `hoopR` loads. ESPN ToS apply; unofficial API endpoints.
- **Packages:** `hoopR` `espn_*` functions, `sportsdataverse-py`

### BALLDONTLIE
- **URL:** [docs.balldontlie.io](https://docs.balldontlie.io/)
- **Access:** freemium API
- **Grain:** teams/players/games (+ paid stats tier)
- **Coverage:** Modern NBA, thinner historical depth than Basketball-Reference
- **Priority:** P1
- **Notes:** Free tier approximately 5 requests/minute (API key recommended). Good teaching API for basic queries; **not a Basketball-Reference replacement**.

### Dunks & Threes EPM
- **URL:** [dunksandthrees.com/epm](https://dunksandthrees.com/epm)
- **Access:** cite-scrape
- **Grain:** player-season impact estimates
- **Coverage:** Modern era
- **Priority:** P1
- **Notes:** Estimated Plus-Minus (EPM) for plus-minus chapters without building RAPM from scratch.

### Nathan Lauga: nba-games (Kaggle) — PARKED
- **URL:** [kaggle.com/datasets/nathanlauga/nba-games](https://www.kaggle.com/datasets/nathanlauga/nba-games)
- **Access:** later/parked
- **Grain:** games + player box details
- **Coverage:** approximately 2004–present
- **Priority:** later
- **Notes:** **Parked per project policy** (ROADMAP section 6)—Kaggle authentication.

### Wyatt Walsh: basketball (nbadb) — PARKED
- **URL:** [kaggle.com/datasets/wyattowalsh/basketball](https://www.kaggle.com/datasets/wyattowalsh/basketball)
- **Access:** later/parked
- **Grain:** Star-schema warehouse (SQLite/DuckDB)
- **Coverage:** Claims 1946–present
- **Priority:** later
- **Notes:** **Intentionally parked** per [ROADMAP](../ROADMAP.md) section 6—large SQLite/DuckDB, Kaggle authentication, ToS considerations. Built from `nba_api`. GitHub ETL pipeline companion at [wyattowalsh/nbadb](https://github.com/wyattowalsh/nbadb).

---

## Play-by-Play & Shot Data

### NBA PlayByPlayV3 (via nba_api / hoopR)
- **Access:** open-tool (NBA ToS)
- **Grain:** event-level PBP with shot coordinates
- **Coverage:** V3 current; V2 deprecated on many seasons
- **Priority:** P0
- **Notes:** Prefer V3 endpoints. **Fetch for notebooks; don't vendor full season archives** (violates NBA ToS comprehensive DB restriction). Use for local analysis, derive tables, cite.
- **Packages:** `nba_api.live.nba.endpoints` (Python), `hoopR` NBA Stats wrappers (R)

### hoopR & hoopR-data
- **URL:** [github.com/sportsdataverse/hoopR](https://github.com/sportsdataverse/hoopR)  
  [github.com/sportsdataverse/hoopR-data](https://github.com/sportsdataverse/hoopR-data)
- **Access:** open-tool / bulk-mirror
- **Grain:** PBP/box parquet/CSV/RDS
- **Coverage:** ESPN-derived NBA play-by-play approximately **2002–2026**
- **Priority:** P0
- **Notes:** MIT license package; upstream ESPN ToS apply. Static PBP parquet/CSV/RDS archive in `hoopR-data` for research (**P0 PBP research lane**). Convenience dump—**cite ESPN/NBA upstream sources; do not treat as open license grant for wholesale redistribution**. Dynamic loads via `hoopR` package. Also covers WNBA (via `wehoop`), men's/women's college basketball, and integrates Basketball-Reference scrapers.

### shufinskiy/nba_data
- **URL:** [github.com/shufinskiy/nba_data](https://github.com/shufinskiy/nba_data)
- **Access:** bulk-mirror
- **Grain:** PBP and shot detail, multi-source
- **Coverage:** stats.nba.com approximately 1996/97–present; pbpstats.com approximately 2000/01–present; data.nba.net approximately 2016/17–present
- **Priority:** P0
- **Notes:** Apache-2.0 licensed **repository** (code); data sourced from NBA endpoints and inherit NBA ToS. Convenient PBP/shots archive. **P0 offline PBP for local research—analyze locally; do NOT redistribute into glen-w/hoops data/ or vendor the full mirror as a commercial product.**

### pbpstats (Python package)
- **URL:** [github.com/dblackrun/pbpstats](https://github.com/dblackrun/pbpstats)
- **Access:** open-tool
- **Grain:** possession/lineup/shot-zone enrichment
- **Coverage:** NBA/WNBA/G League (stats.nba / data.nba dependent)
- **Priority:** P1
- **Notes:** Open-source parser; upstream NBA ToS apply. Enriches PBP with possession/lineup/on-off analysis. Useful for deriving advanced lineup metrics.

### pbpstats.com API
- **URL:** [api.pbpstats.com/docs](https://api.pbpstats.com/docs)
- **Access:** paywall (site browse + paid API)
- **Grain:** on/off WOWY lineups
- **Coverage:** Modern era
- **Priority:** cite-only
- **Notes:** Cite derived views from the public website; full API requires subscription.

### ESPN Live PBP
- **Access:** open-tool (unofficial ToS)
- **Grain:** live events + shots when present
- **Coverage:** Current season strong
- **Priority:** P1
- **Notes:** Accessed via `hoopR` `espn_*` functions or `sportsdataverse-py`. Good for live-game chapters. ESPN ToS apply.

### BigDataBall
- **URL:** [bigdataball.com/datasets/nba-data](https://www.bigdataball.com/datasets/nba-data/)
- **Access:** paywall
- **Grain:** Cleaned PBP with lineups/coordinates
- **Coverage:** Historical + in-season
- **Priority:** cite-only
- **Notes:** Commercial product. Budget-friendly cleaned PBP Excel exports.

### NBAstuffer Data Shop
- **URL:** [nbastuffer.com/sports-data](https://www.nbastuffer.com/sports-data/)
- **Access:** paywall
- **Grain:** box/PBP Excel (product-dependent)
- **Priority:** cite-only
- **Notes:** Commercial spreadsheets; not open.

---

## Tracking, Pose, Video (Proprietary / Cite-Only)

### NBA Tracking Aggregates (Public)
- **Source:** stats.nba.com (LeagueDashPtStats, hustle, speed/distance endpoints)
- **Access:** open-tool / cite
- **Grain:** player/team summaries (not raw xy coordinates)
- **Coverage:** SportVU → Second Spectrum → Hawk-Eye eras
- **Priority:** P1
- **Notes:** **Safe public substitute for raw tracking data.** Aggregate statistics (e.g., player speed, distance traveled, touches) accessible via `nba_api` / `hoopR` / `nbastatR`. Use these instead of attempting to redistribute raw tracking dumps.

### ShotChartDetail / PBP V3 Coordinates
- **Source:** nba_api / hoopR
- **Access:** open-tool / cite
- **Grain:** shot x/y coordinates
- **Coverage:** Multi-season modern era
- **Priority:** P1
- **Notes:** Shot charts without SportVU risk. NBA Stats ShotChartDetail endpoint provides shot locations. Safe for analysis and visualization.

### SportVU Raw Dumps — LEGAL CAUTION
- **URL (historical):** [github.com/neilmj/BasketballData](https://github.com/neilmj/BasketballData) · mirrors `sealneaward/nba-movement-data`, `linouk23/NBA-Player-Movements`
- **Access:** proprietary / legal gray area
- **Grain:** approximately 25 Hz x/y/(z) tracking
- **Coverage:** Primarily **2015–16 season**
- **Priority:** later / methods-only
- **Notes:** **LEGAL CAUTION—DO NOT REDISTRIBUTE.** Briefly public then withdrawn; used in academic papers. SportVU data carries legal/ToS ambiguity. **Cite papers and methods only; do NOT commit tracking data to this repo or vendor it.** MIT license on parsing *code* ≠ data redistribution rights.

### Second Spectrum
- **Access:** proprietary
- **Grain:** approximately 25 Hz optical tracking
- **Coverage:** approximately 2017–2023 (NBA vendor era)
- **Priority:** cite-only
- **Notes:** Teams and licensees only. No public raw API. Describe in narrative; cite Sloan SSAC papers.

### Hawk-Eye (NBA)
- **Access:** proprietary
- **Grain:** skeletal / high-Hz pose estimation
- **Coverage:** approximately 2023–present (current NBA vendor)
- **Priority:** cite-only
- **Notes:** Teams only. No public API. Approximately 1 million tracking entries per game (narrative). Describe tracking evolution in analytics chapter.

**Zotero Context:** The `hoops → ⭐analytics` collection (B5IYL479) is **rich in tracking and PBP method papers** (SportVU-era, player tracking, play-by-play modeling), but thin on package citations. Tracking is **research literature + proprietary**—not an open dump for repo redistribution. See [ZOTERO-DATASET-MENTIONS.md](../uploads/ZOTERO-DATASET-MENTIONS_819c.md) for gap analysis.

---

## College & International Basketball

### Barttorvik T-Rank (College)
- **URL:** [barttorvik.com](https://barttorvik.com/)
- **Access:** cite-scrape / open CSV
- **Grain:** team ratings / four factors
- **Coverage:** approximately 2008–present (season-end year format)
- **Priority:** P0
- **Notes:** **Best free college efficiency metric.** Public CSVs available in `{YYYY}_team_results.csv` format (YYYY = season-end year). Use this for college chapters without requiring a KenPom paywall subscription. Wrapped by `hoopR`/`sportsdataverse` `torvik_*` functions.
- **Packages:** `hoopR` Torvik functions, `sportsdataverse-py`

### KenPom (College)
- **URL:** [kenpom.com](https://kenpom.com/)
- **Access:** paywall
- **Grain:** ratings / four factors
- **Coverage:** Long Division I history
- **Priority:** later / cite-only
- **Notes:** Subscription required for full tables. Paid API available (`register-api.php`). `hoopR` supports KenPom scraping (`kenpom_*` / `kp_*` functions) with an active subscription. Use Barttorvik for open alternative.

### hoopR NCAA / NET
- **URL:** [hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/)
- **Access:** open-tool
- **Grain:** NET ratings + ESPN men's college basketball
- **Coverage:** Current + recent seasons
- **Priority:** P1
- **Notes:** College play-by-play via ESPN helpers. NET (NCAA Evaluation Tool) ratings accessible.

### EuroLeague Live API / py-euroleague
- **URL:** `api-live.euroleague.net` · [github.com/sfendourakis/py-euroleague](https://github.com/sfendourakis/py-euroleague)
- **Access:** open-tool (unofficial)
- **Grain:** box/PBP/shots
- **Coverage:** approximately 2000s–present; PBP and shots stronger post-approximately 2007
- **Priority:** P1
- **Notes:** Unofficial API but widely used. ToS unclear for redistribution. Use for international comparison chapters without requiring FIBA paywall. **International grain beyond NBA.**
- **Packages:** `py-euroleague` (Python)

### FIBA GDAP
- **URL:** [gdap-portal.fiba.basketball](https://gdap-portal.fiba.basketball/)
- **Access:** paywall / auth
- **Grain:** official competitions box/PBP
- **Coverage:** World Cup, Olympics, FIBA competitions
- **Priority:** later / cite-only
- **Notes:** Subscription and authentication required—**not open**. Public event HTML leaderboards available but limited. **Cite public HTML only.** For FIBA scale estimates (e.g., approximately 450 million players globally), cite official FIBA publications.

### wehoop / sportsdataverse-py WNBA
- **URL:** [wehoop.sportsdataverse.org](https://wehoop.sportsdataverse.org/)
- **Access:** open-tool
- **Grain:** WNBA/WBB PBP/box
- **Coverage:** Multi-season ESPN-derived
- **Priority:** P1
- **Notes:** MIT-family license. WNBA companion to `hoopR`. Use for gender/league comparison chapters.
- **Packages:** `wehoop` (R), `sportsdataverse-py` (Python)

---

## Salaries & Front Office

### Basketball-Reference Contracts
- **URL:** [basketball-reference.com/contracts](https://www.basketball-reference.com/contracts/)
- **Access:** cite-scrape
- **Grain:** multi-year deals / payrolls
- **Coverage:** Team and player salary tables, multi-year historical
- **Priority:** P0
- **Notes:** **P0 for front-office payroll tables.** Use for payroll/front-office efficiency tables (e.g., Forbes-derived FO efficiency in ROADMAP section 4). Sports Reference data-use terms apply (approximately 20 req/min; polite scraping).

### HoopsHype Salaries
- **URL:** [hoopshype.com/salaries](https://hoopshype.com/salaries/)
- **Access:** cite-scrape
- **Grain:** player salaries
- **Coverage:** Current NBA salaries
- **Priority:** P1
- **Notes:** GraphQL API shifts have broken some scrapers; scraper fragility. **Cite carefully.** `hoopR` includes `hoopshype_*` scrapers; ESPN contracts are fallback option.

### Spotrac NBA
- **URL:** [spotrac.com/nba](https://www.spotrac.com/nba/)
- **Access:** cite-only (ToS anti-scrape)
- **Grain:** contracts/guarantees/cap
- **Coverage:** Current contracts and salary cap details
- **Priority:** later / cite-only
- **Notes:** **Explicit anti-scrape Terms of Service—ToS bans scraping/data mining.** Cite individual HTML pages only; **do not bulk harvest**.

### Capology
- **URL:** [capology.com](https://capology.com/)
- **Access:** n/a (wrong sport)
- **Priority:** later
- **Notes:** **Soccer only—not an NBA source.**

### NBA Draft Combine
- **URL:** [nba.com/stats/draft/combine](https://www.nba.com/stats/draft/combine)
- **Access:** open-tool (via NBA Stats wrappers / ToS)
- **Grain:** anthropometrics + athletic measurements
- **Coverage:** Combine years
- **Priority:** P1
- **Notes:** Anthropometrics for skills/body chapters. Accessible via `hoopR` `nba_draftcombine*` functions and `nba_api`.
- **Packages:** `hoopR` `nba_draftcombinestats`, `nba_api`

### Basketball-Reference Draft Index
- **URL:** [basketball-reference.com/draft](https://www.basketball-reference.com/draft/)
- **Access:** cite-scrape
- **Grain:** draft history
- **Coverage:** Historical NBA drafts
- **Priority:** P1
- **Notes:** Draft-value chapters. Sports Reference data-use terms apply.

### Official NBA Transactions / Injury Reports
- **URL:** [nba.com/players/transactions](https://www.nba.com/players/transactions) · `official.nba.com`
- **Access:** cite-only (web)
- **Grain:** transactions / injury PDFs
- **Coverage:** Current
- **Priority:** P1
- **Notes:** Front-office timeline exhibits. Official transaction logs and injury PDFs.

---

## Python & R Packages

### Python

| Package | Repository | Upstream | Priority | Role |
|---------|-----------|----------|----------|------|
| **nba_api** | [github.com/swar/nba_api](https://github.com/swar/nba_api) | stats.nba.com + live | **P0** | **Python default live client.** MIT wrapper; upstream NBA ToS. Prefer V3 endpoints (PBP V3 / Scoreboard V3). |
| **basketball_reference_scraper** | [github.com/vishaalagartha/basketball_reference_scraper](https://github.com/vishaalagartha/basketball_reference_scraper) | Basketball-Reference | **P0** | **Python BRef pulls.** MIT + BRef/SR etiquette (approximately 20 req/min). |
| **pbpstats** | [github.com/dblackrun/pbpstats](https://github.com/dblackrun/pbpstats) | NBA feeds | P1 | Possessions / on-off enrichment. Open-source parser; upstream NBA ToS. |
| **sportsdataverse-py** | [py.sportsdataverse.org](https://py.sportsdataverse.org/) | ESPN / loaders / Torvik | P1 | **Python ESPN + WNBA loaders.** ESPN ToS; see project license. |
| **py-euroleague** | [github.com/sfendourakis/py-euroleague](https://github.com/sfendourakis/py-euroleague) | EuroLeague live API | P1 | International wrapper. Unofficial `api-live.euroleague.net`; ToS unclear. |

### R

| Package | Repository | Upstream | Priority | Role |
|---------|-----------|----------|----------|------|
| **hoopR** | [hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/) | NBA Stats + ESPN + BRef + KenPom | **P0** | **R default.** MIT; 127+ NBA wrappers. Upstream ToS vary; KenPom needs subscription. Includes `bref_*` scrapers, PBP loaders, draft combine, salary scrapers (`hoopshype_*`), Torvik functions. |
| **nbastatR** | [github.com/abresler/nbastatR](https://github.com/abresler/nbastatR) | NBA Stats + FO scrapers | **P0** | **R front-office oriented.** MIT client; broad NBA Stats + FO scrapers; respect upstream ToS. Comprehensive endpoint coverage. |
| **ballr** | [github.com/rtelmore/ballr](https://github.com/rtelmore/ballr) | Basketball-Reference | P1 | **R BRef scrapers.** CRAN/GitHub; simple historical player/team tables; SR ToS. |
| **BasketballAnalyzeR** | [CRAN](https://cran.r-project.org/package=BasketballAnalyzeR) | bring-your-own frames | P1 | **Viz/analysis framework.** CRAN (GPL-family); accompanies Zuccolotto & Manisera *Basketball Data Science*; **cited in Zotero analytics collection (BB4SV25F)**; teaching viz. |
| **wehoop** | [github.com/sportsdataverse/wehoop](https://github.com/sportsdataverse/wehoop) | WNBA/WBB ESPN | P1 | **WNBA companion.** MIT-family; ESPN-derived PBP for women's basketball. |

**Note:** `toddwschneider/ballr` is a different shot-chart Shiny app—not the CRAN Basketball-Reference package `ballr` listed above.

---

## GitHub Data Dumps & Catalogs

### hoopR-data
- **URL:** [github.com/sportsdataverse/hoopR-data](https://github.com/sportsdataverse/hoopR-data)
- **What:** Season PBP/box parquet
- **Priority:** P0
- **Notes:** Static archive for research. **P0 PBP research lane.** Cite ESPN/NBA upstream.

### shufinskiy/nba_data
- **URL:** [github.com/shufinskiy/nba_data](https://github.com/shufinskiy/nba_data)
- **What:** Bulk PBP/shots multi-source
- **Priority:** P0 (local only; no vendor)
- **Notes:** Apache-2.0 repo code; data from NBA endpoints (ToS-bound). **Analyze locally; do NOT vendor into glen-w/hoops data/ directory.**

### sportsdataverse-data Releases
- **URL:** [github.com/sportsdataverse/sportsdataverse-data/releases](https://github.com/sportsdataverse/sportsdataverse-data/releases)
- **What:** Versioned `nba_stats_pbp`, player season stats
- **Priority:** P0/P1
- **Notes:** Stable snapshots for reproducibility. Tag-based versioning.

### awesome-nba-data
- **URL:** [github.com/JovaniPink/awesome-nba-data](https://github.com/JovaniPink/awesome-nba-data)
- **What:** Curated catalog + ToS-aware source matrix
- **Priority:** P0 (discovery)
- **Notes:** **Living index + ToS matrix.** Curation not license. **Link from docs and analytics chapter.**

### neilmj/BasketballData (SportVU Mirrors) — LEGAL CAUTION
- **URL:** [github.com/neilmj/BasketballData](https://github.com/neilmj/BasketballData)
- **What:** SportVU raw 2015–16 + parsers
- **Priority:** later / methods-only
- **Notes:** **Legal gray area / proprietary caution.** MIT code ≠ data rights. **Do not vendor.** Mirrors include `sealneaward/nba-movement-data`, `linouk23/NBA-Player-Movements`. Use for **methods/papers citations only.**

### wyattowalsh/nbadb — PARKED
- **URL:** [github.com/wyattowalsh/nbadb](https://github.com/wyattowalsh/nbadb)
- **What:** ETL for Kaggle warehouse
- **Priority:** later
- **Notes:** Pipeline companion to parked Kaggle DB.

### jsierra999/nba-data-archive
- **URL:** [github.com/jsierra999/nba-data-archive](https://github.com/jsierra999/nba-data-archive)
- **What:** PBP/shots/matchups mirrors
- **Priority:** later
- **Notes:** GitHub repo with periodic snapshots (verify freshness before use).

### data.gov Basketball
- **URL:** [catalog.data.gov/?keyword=basketball](https://catalog.data.gov/?keyword=basketball)
- **What:** Mostly court GIS, not NBA stats
- **Priority:** irrelevant
- **Notes:** U.S. government open data catalog; basketball results are primarily **court location GIS files**, not NBA statistics.

### Google Dataset Search
- **URL:** [datasetsearch.research.google.com](https://datasetsearch.research.google.com/)
- **What:** Discovery search engine
- **Priority:** meta only
- **Notes:** Discovery tool; not a data repository itself.

---

## Paywalled & Commercial (Cite-Only Desk)

| Source | URL | Why |
|--------|-----|-----|
| **Cleaning the Glass** | [cleaningtheglass.com](https://cleaningtheglass.com/) | Paid lineup/on-off statistics (approximately $5/month subscription) |
| **KenPom** | [kenpom.com](https://kenpom.com/) | Subscription + paid API for college efficiency |
| **BigDataBall / NBAstuffer** | [bigdataball.com](https://www.bigdataball.com/) · [nbastuffer.com/sports-data](https://www.nbastuffer.com/sports-data/) | Commercial PBP/Excel products |
| **Stathead Basketball** | [stathead.com/basketball](https://stathead.com/basketball/) | Paid Sports Reference query tool |
| **FIBA GDAP** | [gdap-portal.fiba.basketball](https://gdap-portal.fiba.basketball/) | Auth subscription for international comps |
| **Second Spectrum / Hawk-Eye raw** | — | Proprietary tracking (teams/licensees only) |
| **Sportradar / SportsDataIO** | Developer portals | Licensed B2B commercial feeds |
| **Spotrac bulk extract** | [spotrac.com/service](https://www.spotrac.com/service) | ToS bans scraping |
| **SportVU GitHub dumps** | neilmj et al. | Legal caution—**papers only; do not redistribute** |
| **NBA.com comprehensive DB republication** | [nba.com/termsofuse](https://www.nba.com/termsofuse) | No competing regularly-updated public database without consent |
| **Sports Reference bulk / AI** | [sports-reference.com/data_use.html](https://www.sports-reference.com/data_use.html) | Needs written permission for commercial DB / AI training |

---

## P0 Recommendations for glen-w/hoops

**Priority 0 (baseline for manuscript tables & reproducibility):**

1. **Basketball-Reference season aggregates**—keep as source of truth for decade/average-game tables (committed CSV + citation). **Already in use** for `avg_game_by_decade`.

2. **`nba_api` (Python)** — [github.com/swar/nba_api](https://github.com/swar/nba_api) — live stats.nba.com client; prefer V3 PBP/scoreboard endpoints; **document NBA ToS—no full database publish**.

3. **`hoopR` (R)** — [hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/) — R parity for NBA Stats + ESPN + `bref_*` helpers; 127+ NBA wrappers.

4. **`basketball_reference_scraper` / `ballr` / `hoopR` `bref_*`**—advanced metrics and historical depth beyond committed aggregates. Sports Reference etiquette (approximately 20 req/min).

5. **`hoopR-data` or `shufinskiy/nba_data`**—PBP research lane. **Local analysis only; don't vendor the mirror into `data/` directory** (flag NBA ToS). P0 for offline PBP notebooks.

6. **Barttorvik CSVs** — [barttorvik.com](https://barttorvik.com/) — college chapter efficiency without KenPom paywall. Public `{year}_team_results.csv` files.

7. **EuroLeague API / `py-euroleague`**—international grain beyond NBA/FIBA GDAP. Unofficial but functional.

8. **`wehoop` / `sportsdataverse-py` WNBA**—gender/league comparison chapters. ESPN-derived women's basketball PBP.

9. **Basketball-Reference contracts + NBA Draft Combine**—front-office payroll tables and anthropometrics for skills/body chapters. Combine via `hoopR` `nba_draftcombinestats` or `nba_api`.

10. **awesome-nba-data** — [github.com/JovaniPink/awesome-nba-data](https://github.com/JovaniPink/awesome-nba-data) — living index + ToS matrix; **link from docs and analytics chapter**.

---

## Explicitly Later / Parked

- **Wyatt Walsh Kaggle basketball SQLite/nbadb**—large warehouse; Kaggle authentication; parked per ROADMAP section 6.
- **Nathan Lauga Kaggle nba-games**—parked per project policy.
- **Other Kaggle NBA warehouses**—parked per project policy.
- **KenPom**—cite-only unless active subscription available.
- **BigDataBall / NBAstuffer data shop**—commercial; cite-only.
- **Cleaning the Glass**—subscription required; cite-only.

---

## Explicitly Out of Scope

- **SportVU dump redistribution**—legal caution; **do not vendor**; cite papers/methods only.
- **Spotrac bulk scrape**—ToS violation; cite individual HTML pages only.
- **Capology**—wrong sport (soccer).
- **Second Spectrum / Hawk-Eye raw tracking**—proprietary; teams only; narrative only.
- **NBA.com comprehensive database mirrors**—ToS restriction; derive tables instead.
- **Gambling odds datasets**—narrative only per ROADMAP section 6.
- **Manuscript editing**—Scrivener stays local per ROADMAP.

---

## Cross-References

- [ROADMAP.md](../ROADMAP.md)—research tooling priorities and out-of-scope items
- [README.md](../README.md)—repo overview and Scrivener/Zotero integration
- [data/mentions.csv](../data/mentions.csv)—690 sentences from draft keyword scan; actionable data references
- [docs/open_datasets.csv](open_datasets.csv)—structured catalog of 35 sources (name, URL, grain, coverage, access, license, package, priority, notes)
- [Open Data Landscape Brief](../uploads/OPEN-DATA-LANDSCAPE_14b2.md)—2026-09-19 baseline scan with access flags and P0 recommendations
- [Zotero Dataset Mentions](../uploads/ZOTERO-DATASET-MENTIONS_819c.md)—gap analysis: analytics is method-heavy, tooling thin; new Zotero folder `hoops → data sources` (I5MN75D8) seeded

---

## License & Attribution Notes

This catalog is a research resource for the *Hoops* book project. Package licenses and upstream terms of service vary—consult each source's documentation before redistribution. When in doubt:

- **Cite the source** (Basketball-Reference, NBA Stats, etc.)
- **Derive your tables locally** (don't redistribute full mirrors of stats.nba.com)
- **Check Sports Reference data-use page** for Basketball-Reference scraping etiquette (approximately 20 req/min; no competing DB without permission)
- **Respect explicit anti-scrape ToS** (Spotrac)
- **Treat proprietary tracking as cite-only** (SportVU, Second Spectrum, Hawk-Eye)
- **Client MIT license ≠ data redistribution rights**—open-source package wrappers don't grant permission to violate upstream data ToS

For questions about this catalog, see the [ROADMAP](../ROADMAP.md) or open an issue in this repository.
