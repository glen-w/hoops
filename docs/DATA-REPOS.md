# Basketball Data Repositories & Sources

**Last updated:** 2026-09-19

This document maps the open basketball numbers landscape: datasets, APIs, Python/R packages, and key resources for reproducible basketball analytics. Access flags are practical guidance, not legal advice—always re-check terms of service before redistributing data.

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
- **Coverage:** BAA (1946) through present; season, game, and player grain
- **Priority:** P0
- **Notes:** Canonical historical source for season and advanced tables. **Already feeding `avg_game_by_decade`** in this repo. Sports Reference [data-use page](https://www.sports-reference.com/data_use.html) applies—polite scraping for research is acceptable; commercial redistribution requires permission.
- **Packages:** `basketball_reference_scraper` (Python), `ballr` (R), `hoopR` `bref_*` family (R)

### NBA Stats API (stats.nba.com)
- **URL:** [nba.com/stats](https://www.nba.com/stats)
- **Access:** open-tool
- **Coverage:** ~1996–present (varies by endpoint); game/PBP/tracking summaries
- **Priority:** P0
- **Notes:** Official public endpoints. **NBA Terms of Service:** allowed for news/private noncommercial use; **no comprehensive public database mirrors** or commercial gambling redistribution. **Derive tables, cite the source, and don't ship full mirrors.**
- **Packages:** `nba_api` (Python), `hoopR` (R), `nbastatR` (R)

### BALLDONTLIE
- **URL:** [docs.balldontlie.io](https://docs.balldontlie.io/)
- **Access:** open-tool
- **Coverage:** Modern NBA games, players, teams; thinner historical depth than Basketball-Reference
- **Priority:** P1
- **Notes:** Free tier with 5 requests/minute (API key recommended). Good teaching API for basic queries.

### Nathan Lauga: nba-games (Kaggle)
- **URL:** [kaggle.com/datasets/nathanlauga/nba-games](https://www.kaggle.com/datasets/nathanlauga/nba-games)
- **Access:** bulk-mirror
- **Coverage:** Games + player box details, approximately 2004–present
- **Priority:** P1
- **Notes:** Convenient Kaggle dataset; verify license terms on Kaggle before redistribution.

### Wyatt Walsh: basketball (nbadb) — PARKED
- **URL:** [kaggle.com/datasets/wyattowalsh/basketball](https://www.kaggle.com/datasets/wyattowalsh/basketball)
- **Access:** later
- **Coverage:** Large SQLite with multi-table NBA data, 1946–~2024
- **Priority:** later
- **Notes:** **Intentionally parked** per [ROADMAP](../ROADMAP.md) section 6—Kaggle authentication + size. GitHub pipeline companion at [wyattowalsh/nba-db](https://github.com/wyattowalsh/nba-db).

---

## Play-by-Play & Shot Data

### hoopR & hoopR-data
- **URL:** [github.com/sportsdataverse/hoopR](https://github.com/sportsdataverse/hoopR)  
  [github.com/sportsdataverse/hoopR-data](https://github.com/sportsdataverse/hoopR-data)
- **Access:** open-tool / bulk-mirror
- **Coverage:** ESPN-derived NBA play-by-play approximately 2002–present; parquet loaders
- **Priority:** P0
- **Notes:** MIT license; upstream ESPN ToS apply. Static PBP parquet archive in `hoopR-data` for research; dynamic loads via `hoopR` package. Also covers WNBA (via `wehoop`), men's/women's college basketball, and integrates Basketball-Reference scrapers.

### shufinskiy/nba_data
- **URL:** [github.com/shufinskiy/nba_data](https://github.com/shufinskiy/nba_data)
- **Access:** bulk-mirror
- **Coverage:** PBP and shots from stats.nba.com, data.nba.net, and pbpstats.com, approximately 1996–2024/25
- **Priority:** P0
- **Notes:** Apache-2.0 licensed repo. Convenient PBP/shots archive; data sourced from NBA endpoints (inherit NBA ToS—local analysis fine; don't vendor the full mirror as a commercial product).

### pbpstats
- **URL:** [github.com/dblackrun/pbpstats](https://github.com/dblackrun/pbpstats)
- **Access:** open-tool
- **Coverage:** stats.nba.com dependent; enriches PBP with possession/lineup/on-off analysis
- **Priority:** P1
- **Notes:** MIT license. Useful for deriving advanced lineup metrics.

### jsierra999/nba-data-archive
- **URL:** [github.com/jsierra999/nba-data-archive](https://github.com/jsierra999/nba-data-archive)
- **Access:** bulk-mirror
- **Coverage:** PBP, shots, matchups mirrors (verify freshness before use)
- **Priority:** P1
- **Notes:** GitHub repo with periodic snapshots.

### BigDataBall / NBAstuffer (Commercial)
- **URL:** [bigdataball.com/datasets/nba-data](https://www.bigdataball.com/datasets/nba-data/)
- **Access:** paywall
- **Coverage:** Clean commercial PBP and shot CSV files, historical paid tiers
- **Priority:** cite-only
- **Notes:** Paid subscription; clean Excel/CSV exports. See also [nbastuffer.com](https://www.nbastuffer.com/) for free referee stats and team analytics lists.

---

## Python & R Packages

### Python

| Package | Repository | Role | Priority | Notes |
|---------|-----------|------|----------|-------|
| **nba_api** | [github.com/swar/nba_api](https://github.com/swar/nba_api) | stats.nba.com wrapper | P0 | MIT license; Python default for NBA Stats endpoints |
| **basketball_reference_scraper** | [github.com/vishaalagartha/basketball_reference_scraper](https://github.com/vishaalagartha/basketball_reference_scraper) | Basketball-Reference tables | P0 | MIT + BRef scraping etiquette |
| **pbpstats** | [github.com/dblackrun/pbpstats](https://github.com/dblackrun/pbpstats) | Possessions / on-off | P1 | Enrichment layer over NBA feeds |
| **sportsdataverse-py** | [py.sportsdataverse.org](https://py.sportsdataverse.org/) | ESPN NBA/WNBA loaders | P1 | Python port of sportsdataverse family |
| **py-euroleague** | [github.com/hypsin/pyeuroleague](https://github.com/hypsin/pyeuroleague) | EuroLeague live/stats API | P1 | Unofficial but widely used international wrapper |

### R

| Package | Repository | Role | Priority | Notes |
|---------|-----------|------|----------|-------|
| **hoopR** | [hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/) | ESPN + NBA Stats + BRef + KenPom | P0 | MIT; R default; includes `bref_*` scrapers, PBP loaders, draft combine, salary scrapers (`hoopshype_*`) |
| **nbastatR** | [github.com/abresler/nbastatR](https://github.com/abresler/nbastatR) | NBA Stats + FO scrapers | P0 | MIT; front-office oriented; comprehensive endpoint coverage |
| **ballr** | [github.com/rtelmore/ballr](https://github.com/rtelmore/ballr) | BRef per-game scrapers | P1 | CRAN/GitHub; simple historical player/team tables |
| **BasketballAnalyzeR** | [CRAN](https://cran.r-project.org/package=BasketballAnalyzeR) | Viz/analysis framework | P1 | GPL; accompanies Zuccolotto & Manisera *Basketball Data Science*; **cited in Zotero analytics collection** |
| **wehoop** | [github.com/sportsdataverse/wehoop](https://github.com/sportsdataverse/wehoop) | WNBA / women's college BB | P1 | MIT; ESPN-derived PBP for women's basketball |

---

## College & International Basketball

### Barttorvik T-Rank (College)
- **URL:** [barttorvik.com](https://barttorvik.com/)
- **Access:** cite-scrape
- **Coverage:** NCAA Division I team season ratings, approximately 2008–present
- **Priority:** P0
- **Notes:** Free public CSVs (`{year}_team_results.csv` format). **Best open college efficiency metric**—use this for college chapters without requiring a KenPom paywall subscription.

### KenPom (College)
- **URL:** [kenpom.com](https://kenpom.com/)
- **Access:** paywall
- **Coverage:** NCAA Division I team efficiency, modern era
- **Priority:** cite-only
- **Notes:** Subscription required for full tables. `hoopR` supports KenPom scraping with an active subscription (`kenpom_*` functions).

### EuroLeague Live API
- **URL:** [euroleaguebasketball.net](https://www.euroleaguebasketball.net/)
- **Access:** open-tool
- **Coverage:** Box scores from ~2000s; PBP and shots from later seasons
- **Priority:** P1
- **Notes:** Unofficial API (`api-live.euroleague.net`); ToS unclear but widely used. Wrapper: `py-euroleague` (Python).

### FIBA GDAP
- **URL:** [gdap.fiba.basketball](https://gdap.fiba.basketball/)
- **Access:** paywall
- **Coverage:** Official FIBA competitions (World Cup, Olympics, etc.)
- **Priority:** cite-only
- **Notes:** Subscription API—**not open**. Public leaderboard HTML available but limited. For FIBA scale estimates (e.g., ~450 million players globally), cite official FIBA publications.

---

## Salaries & Front Office

### Basketball-Reference Contracts
- **URL:** [basketball-reference.com/contracts](https://www.basketball-reference.com/contracts/)
- **Access:** cite-scrape
- **Coverage:** Team and player salary tables, multi-year historical
- **Priority:** P0
- **Notes:** Use for payroll/front-office efficiency tables (e.g., Forbes-derived FO efficiency in ROADMAP section 4). Sports Reference data-use terms apply.

### HoopsHype Salaries
- **URL:** [hoopshype.com/salaries](https://hoopshype.com/salaries/)
- **Access:** cite-scrape
- **Coverage:** Current NBA salaries
- **Priority:** P1
- **Notes:** GraphQL API shifts have broken some scrapers. `hoopR` includes `hoopshype_*` scrapers; ESPN contracts are fallback option.

### Spotrac NBA
- **URL:** [spotrac.com/nba](https://www.spotrac.com/nba/)
- **Access:** cite-scrape (ToS-hostile)
- **Coverage:** Contracts and salary cap details, current
- **Priority:** cite-only
- **Notes:** **Explicit anti-scrape Terms of Service.** Cite individual HTML pages only; **do not bulk harvest**.

---

## Tracking, Pose, Video (Proprietary / Cite-Only)

### SportVU-Era Public Dumps
- **Access:** proprietary
- **Coverage:** Optical tracking from approximately 2013–2016 (legacy era)
- **Priority:** cite-only
- **Notes:** **Do NOT treat SportVU dumps as redistributable open data.** Cite papers and narrative only. Historical examples sometimes leaked for research; legal redistribution is unclear. Use for method citations, not as a dataset to commit to this repo.

### Second Spectrum / Hawk-Eye
- **Access:** proprietary
- **Coverage:** Current NBA official optical tracking vendor (post-SportVU)
- **Priority:** cite-only
- **Notes:** Vendor/league proprietary. Cite Sloan Sports Analytics Conference (SSAC) papers and official NBA tracking narratives. Approximately 1 million tracking entries per game.

### DeepSportRadar et al.
- **URL:** [paperswithcode.com](https://paperswithcode.com/) (search "basketball tracking")
- **Access:** research license
- **Coverage:** Academic pose/tracking datasets
- **Priority:** cite-only
- **Notes:** Papers With Code aggregates research datasets. These are typically academic licenses—not book-redistributable dumps. Cite methods, not data.

**Zotero Context:** The `hoops → ⭐analytics` collection (B5IYL479) is **rich in tracking and PBP method papers**, but thin on package citations. A new Zotero subfolder `hoops → data sources` (key `I5MN75D8`) has been seeded with P0/P1 tooling stubs. See [ZOTERO-DATASET-MENTIONS.md](../uploads/ZOTERO-DATASET-MENTIONS_bb21.md) for gap analysis.

---

## GitHub Catalogs & Community Resources

### JovaniPink/awesome-nba-data
- **URL:** [github.com/JovaniPink/awesome-nba-data](https://github.com/JovaniPink/awesome-nba-data)
- **Priority:** P0
- **Notes:** Curated list of NBA APIs, tools, and datasets with ToS awareness and source-matrix documentation. **Living index**—link this from manuscript citations and analytics chapter.

### sportsdataverse Release Tags
- **URL:** [github.com/sportsdataverse](https://github.com/sportsdataverse)
- **Priority:** P1
- **Notes:** Versioned parquet/CSV releases for `nba_stats_pbp`, player season stats, and other sportsdataverse datasets. Stable snapshots for reproducibility.

---

## Paywalled & Commercial (Cite-Only Desk)

- **Cleaning the Glass:** [cleaningtheglass.com](https://cleaningtheglass.com/)—lineup/on-off stats, approximately $5/month subscription
- **Synergy Sports:** Commercial video and stats platform
- **Second Spectrum:** NBA official tracking vendor (see Tracking section)
- **KenPom:** College efficiency (see College section)
- **FIBA GDAP:** International official API (see International section)
- **BigDataBall:** Clean commercial PBP/shot CSVs (see PBP section)
- **Sportradar:** Commercial feeds for betting/media

---

## P0 Recommendations for This Repo

**Priority 0 (baseline for manuscript tables & reproducibility):**

1. **Basketball-Reference season aggregates**—keep as source of truth for decade/average-game tables (committed CSV + citation). Already in use for `avg_game_by_decade`.

2. **`nba_api` (Python) or `hoopR` (R)**—regenerate modern season pulls when Basketball-Reference lags; document NBA ToS (no full database redistribution).

3. **`basketball_reference_scraper` / `ballr` / `hoopR` `bref_*`**—advanced metrics and historical depth from Basketball-Reference.

4. **`hoopR-data` or `shufinskiy/nba_data`**—play-by-play for research lane (local analysis; don't vendor the full mirror).

5. **Barttorvik CSVs**—college chapter efficiency metrics without KenPom paywall.

6. **EuroLeague API / `py-euroleague`**—international grain beyond NBA.

7. **`wehoop` / `sportsdataverse-py` WNBA**—gender/league comparison chapters.

8. **Basketball-Reference contracts**—payroll and front-office efficiency (Forbes-derived claims in ROADMAP section 4).

9. **NBA Draft Combine via NBA Stats** (`hoopR` `nba_draftcombine*` or `nba_api`)—anthropometrics for skills/body chapters.

10. **awesome-nba-data**—living index; link from analytics chapter and `docs/DATA-REPOS.md`.

**Explicitly later (per ROADMAP section 6):**
- Wyatt Walsh Kaggle SQLite (authentication + size)

**Explicitly out of scope:**
- SportVU dump redistribution (cite papers only)
- Spotrac bulk scrape (ToS violation)
- Gambling odds datasets (narrative only, per ROADMAP)
- Manuscript editing (Scrivener stays local)

---

## Cross-References

- [ROADMAP.md](../ROADMAP.md)—research tooling priorities and out-of-scope items
- [README.md](../README.md)—repo overview and Scrivener/Zotero integration
- [data/mentions.csv](../data/mentions.csv)—690 sentences from draft keyword scan; actionable data references
- [docs/open_datasets.csv](open_datasets.csv)—structured catalog of ~30 sources (name, URL, grain, coverage, access, license, package, priority, notes)
- [Open Data Landscape Brief](../uploads/OPEN-DATA-LANDSCAPE_7cbd.md)—2026-09-19 baseline scan with access flags and P0 recommendations
- [Zotero Dataset Mentions](../uploads/ZOTERO-DATASET-MENTIONS_bb21.md)—gap analysis: analytics is method-heavy, tooling thin; new Zotero folder `hoops → data sources` seeded

---

## License & Attribution Notes

This catalog is a research resource for the *Hoops* book project. Package licenses and upstream terms of service vary—consult each source's documentation before redistribution. When in doubt:

- **Cite the source** (Basketball-Reference, NBA Stats, etc.)
- **Derive your tables locally** (don't redistribute full mirrors of stats.nba.com)
- **Check Sports Reference data-use page** for Basketball-Reference scraping etiquette
- **Respect explicit anti-scrape ToS** (Spotrac)
- **Treat proprietary tracking as cite-only** (SportVU, Second Spectrum)

For questions about this catalog, see the [ROADMAP](../ROADMAP.md) or open an issue in this repository.
