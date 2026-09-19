# Basketball data sources

**Last updated:** 2026-09-19

Where a number can come from: grain, coverage, and a practical access flag. Not legal advice. Rows are in [open_datasets.csv](open_datasets.csv). The one-page orientation is [NUMBERS-LANDSCAPE.md](NUMBERS-LANDSCAPE.md). Commercial vendors are [BASKETBALL-SOFTWARE.md](BASKETBALL-SOFTWARE.md).

Rules for this repo, once:

- Derive a table, cite the source, and commit only what we may redistribute.
- [NBA terms](https://www.nba.com/termsofuse): news and private noncommercial use. No regularly updated public database, and no gambling redistribution, without consent.
- [Sports Reference](https://www.sports-reference.com/data_use.html): about 20 requests a minute ([bot policy](https://www.sports-reference.com/bot-traffic.html)). No competing database or AI training without written permission.
- A package's MIT license is not a license to the rows it fetches.
- Kaggle warehouses stay parked ([ROADMAP](../ROADMAP.md) §2 and §6).
- SportVU GitHub dumps: papers and methods only. Do not vendor them.

## Flags

| Flag | Meaning |
|------|---------|
| **open-tool** | Package or API for analysis. Upstream may still forbid republication. |
| **cite-scrape** | Public HTML. A polite research scrape is fine. Redistribution rights are weak. |
| **bulk-mirror** | Someone else's dump. Provenance and terms come from the origin. |
| **paywall** | Subscription or commercial feed. |
| **proprietary** | League or vendor tracking. Cite the narrative, not the file. |
| **later** | Parked. |

**P0** is the baseline for manuscript tables. **P1** is next. **later** is map-only.

## Season aggregates

### Basketball-Reference

[basketball-reference.com](https://www.basketball-reference.com/) · cite-scrape · P0

Season, player, game, and draft tables, BAA/NBA 1946–present. Already behind the decade and average-game series (BPM, WS, VORP). Cite the site; do not mirror it. Clients: `basketball_reference_scraper`, `ballr`, hoopR `bref_*`.

### NBA Stats API

[nba.com/stats](https://www.nba.com/stats) · open-tool · P0

Official public endpoints: season, game, player, hustle, tracking summaries, combine. Most series start around 1996 and depend on the endpoint. Prefer V3 (`PlayByPlayV3`, `ScoreboardV3`). Clients: `nba_api`, `hoopR`, `nbastatR`. Fetch for a notebook; do not ship a season archive.

### ESPN

[espn.com/nba/stats](https://www.espn.com/nba/stats) · `site.api.espn.com` · open-tool, unofficial · P1

Leaders, box scores, and scoreboards for the current season and a few before it. Upstream of many hoopR loads. Clients: hoopR `espn_*`, `sportsdataverse-py`.

### BALLDONTLIE

[docs.balldontlie.io](https://docs.balldontlie.io/) · open-tool · P1

Teams, players, and games on the free tier (about 5 requests a minute; a key is recommended). Stats are paid. Thinner history than Basketball-Reference. A teaching API, not a replacement.

### Dunks & Threes EPM

[dunksandthrees.com/epm](https://dunksandthrees.com/epm) · cite-scrape · P1

Player-season estimated plus-minus. Use this before building RAPM.

### Kaggle, parked

[nathanlauga/nba-games](https://www.kaggle.com/datasets/nathanlauga/nba-games) is games and player box scores from about 2004. [wyattowalsh/basketball](https://www.kaggle.com/datasets/wyattowalsh/basketball) is a star-schema SQLite/DuckDB that claims 1946–, built from `nba_api`; the ETL is [wyattowalsh/nbadb](https://github.com/wyattowalsh/nbadb). Both are later: Kaggle authentication, and the Walsh warehouse is large.

## Play-by-play and shots

### NBA PlayByPlayV3

open-tool · P0

Event-level play-by-play with shot coordinates, through `nba_api` or hoopR. V2 is deprecated on many seasons. Local analysis only.

### hoopR and hoopR-data

[hoopR](https://github.com/sportsdataverse/hoopR) · [hoopR-data](https://github.com/sportsdataverse/hoopR-data) · open-tool / bulk-mirror · P0

MIT package. ESPN-derived NBA play-by-play from about 2002 through 2026, plus WNBA (`wehoop`), college, and Basketball-Reference scrapers. The static parquet, CSV, and RDS in hoopR-data are the offline research lane. Cite ESPN and the NBA; the dump is not an open-data grant. Versioned snapshots also land in [sportsdataverse-data releases](https://github.com/sportsdataverse/sportsdataverse-data/releases).

### shufinskiy/nba_data

[github.com/shufinskiy/nba_data](https://github.com/shufinskiy/nba_data) · bulk-mirror · P0, local only

Play-by-play and shots from stats.nba.com (about 1996/97–), pbpstats.com (about 2000/01–), and data.nba.net (about 2016/17–). Apache-2.0 covers the repository, not the rows. Analyze on disk. Do not copy the mirror into `data/`.

### pbpstats

[github.com/dblackrun/pbpstats](https://github.com/dblackrun/pbpstats) · open-tool · P1

Possession, lineup, and shot-zone enrichment for the NBA, WNBA, and G League. The [pbpstats.com API](https://api.pbpstats.com/docs) (on/off, WOWY) is a separate paywall. Cite the public site.

### ESPN live play-by-play

open-tool, unofficial · P1

Current-season events and shots, through hoopR `espn_*` or `sportsdataverse-py`.

### Commercial play-by-play

[BigDataBall](https://www.bigdataball.com/datasets/nba-data/) and the [NBAstuffer shop](https://www.nbastuffer.com/sports-data/) sell cleaned Excel. Cite-only.

[jsierra999/nba-data-archive](https://github.com/jsierra999/nba-data-archive) is a periodic GitHub snapshot. Later; check the date before using it.

## Tracking

Public substitutes, not raw coordinates:

- NBA tracking aggregates (LeagueDashPtStats, hustle, speed and distance) via `nba_api`, hoopR, or `nbastatR`. Player and team summaries across the SportVU, Second Spectrum, and Hawk-Eye eras. P1.
- ShotChartDetail and play-by-play V3 coordinates. Shot x/y for the modern multi-season window. P1.

Do not vendor:

- SportVU raw dumps, mainly 2015–16, about 25 Hz. [neilmj/BasketballData](https://github.com/neilmj/BasketballData) and the mirrors `sealneaward/nba-movement-data` and `linouk23/NBA-Player-Movements`. Briefly public, then withdrawn. Parsing code may be MIT; the points are not.
- Second Spectrum, about 2017–2023. Teams and licensees. Cite Sloan papers.
- Hawk-Eye, about 2023–. Skeletal pose, teams only. The public figure is about a million tracking entries a game.

Zotero `hoops → analytics` (`B5IYL479`) is thick on tracking and play-by-play methods and thin on package citations. `BasketballAnalyzeR` is in that collection (`BB4SV25F`). Tooling notes belong in `hoops → data sources` (`I5MN75D8`).

## College and international

### Barttorvik

[barttorvik.com](https://barttorvik.com/) · cite-scrape · P0

Free NCAA team ratings and four factors, about 2008–, season-end year in `{YYYY}_team_results.csv`. This is the open college metric. Clients: hoopR and sportsdataverse `torvik_*`.

### KenPom

[kenpom.com](https://kenpom.com/) · paywall · later

Long Division I history, plus a paid API. hoopR `kenpom_*` / `kp_*` need a subscription. Use Barttorvik unless one exists.

### hoopR NCAA / NET

[hoopr.sportsdataverse.org](https://hoopr.sportsdataverse.org/) · open-tool · P1

ESPN men's college play-by-play and NET ratings, current and recent seasons.

### EuroLeague

`api-live.euroleague.net` · [py-euroleague](https://github.com/sfendourakis/py-euroleague) · open-tool, unofficial · P1

Box scores, play-by-play, and shots from the 2000s; play-by-play and shots are stronger after about 2007. Redistribution terms are unclear. This is the international grain that does not need FIBA's portal.

### FIBA GDAP

[gdap-portal.fiba.basketball](https://gdap-portal.fiba.basketball/) · paywall · later

Official World Cup, Olympics, and FIBA box scores and play-by-play. Not open. Public event HTML only. The "something like 450 million" players line is a FIBA publication, not this portal.

### WNBA

[wehoop](https://wehoop.sportsdataverse.org/) · open-tool · P1

ESPN-derived WNBA and women's college play-by-play. `wehoop` (R) and `sportsdataverse-py` (Python). The package license is MIT-family; ESPN's terms still cover the rows.

## Salaries and the front office

### Basketball-Reference contracts

[basketball-reference.com/contracts](https://www.basketball-reference.com/contracts/) · cite-scrape · P0

Multi-year deals and payrolls. Same Sports Reference etiquette as the season tables.

### HoopsHype

[hoopshype.com/salaries](https://hoopshype.com/salaries/) · cite-scrape · P1

Current salaries. GraphQL changes have already broken scrapers. hoopR has `hoopshype_*`; ESPN contracts are the fallback.

### Spotrac

[spotrac.com/nba](https://www.spotrac.com/nba/) · cite-only · later

Contracts, guarantees, and cap figures. The terms ban scraping and data mining. Cite a page. Do not harvest.

### Draft

[NBA Draft Combine](https://www.nba.com/stats/draft/combine) · open-tool · P1. Anthropometrics through hoopR `nba_draftcombine*` or `nba_api`.

[Basketball-Reference draft index](https://www.basketball-reference.com/draft/) · cite-scrape · P1.

### Transactions

[nba.com/players/transactions](https://www.nba.com/players/transactions) and injury PDFs on `official.nba.com` · cite-only · P1. Timeline exhibits, not a feed to mirror.

Capology is soccer. It is not a source.

## Packages

### Python

| Package | Upstream | Priority | Role |
|---------|----------|----------|------|
| [`nba_api`](https://github.com/swar/nba_api) | stats.nba.com | P0 | Default live client. Prefer V3. |
| [`basketball_reference_scraper`](https://github.com/vishaalagartha/basketball_reference_scraper) | Basketball-Reference | P0 | Historical tables. |
| [`pbpstats`](https://github.com/dblackrun/pbpstats) | NBA feeds | P1 | Possessions and on/off. |
| [`sportsdataverse-py`](https://py.sportsdataverse.org/) | ESPN, Torvik | P1 | ESPN and WNBA loaders. |
| [`py-euroleague`](https://github.com/sfendourakis/py-euroleague) | EuroLeague live API | P1 | International box, play-by-play, shots. |

### R

| Package | Upstream | Priority | Role |
|---------|----------|----------|------|
| [`hoopR`](https://hoopr.sportsdataverse.org/) | NBA Stats, ESPN, Basketball-Reference, KenPom | P0 | Default. 127+ NBA wrappers, including `bref_*`, the draft combine, `hoopshype_*`, and Torvik. KenPom needs a subscription. |
| [`nbastatR`](https://github.com/abresler/nbastatR) | NBA Stats and front-office scrapers | P0 | The front-office-oriented client. |
| [`ballr`](https://github.com/rtelmore/ballr) | Basketball-Reference | P1 | Simple historical tables. Not [`toddwschneider/ballr`](https://github.com/toddwschneider/ballr), which is a shot-chart app. |
| [`BasketballAnalyzeR`](https://cran.r-project.org/package=BasketballAnalyzeR) | bring-your-own frames | P1 | Viz for Zuccolotto & Manisera. Zotero `BB4SV25F`. GPL-family. |
| [`wehoop`](https://github.com/sportsdataverse/wehoop) | ESPN WNBA / women's college | P1 | Companion to hoopR. |

## Catalogs

- [awesome-nba-data](https://github.com/JovaniPink/awesome-nba-data) is a living index and a terms matrix. Curation, not a license. P0 as a finder. Link it from the analytics chapter; do not paste it in.
- [data.gov](https://catalog.data.gov/?keyword=basketball) basketball hits are court GIS, not NBA stats.
- [Google Dataset Search](https://datasetsearch.research.google.com/) is a search box, not a repository.

## Paywalled desk

| Source | Why it stays closed |
|--------|---------------------|
| [Cleaning the Glass](https://cleaningtheglass.com/) | Lineups and on/off, about $5 a month |
| [KenPom](https://kenpom.com/) | College efficiency |
| [BigDataBall](https://www.bigdataball.com/), [NBAstuffer shop](https://www.nbastuffer.com/sports-data/) | Cleaned play-by-play Excel |
| [Stathead Basketball](https://stathead.com/basketball/) | Paid Sports Reference queries |
| [FIBA GDAP](https://gdap-portal.fiba.basketball/) | International competitions |
| Second Spectrum, Hawk-Eye | Raw tracking |
| Sportradar, SportsDataIO | Licensed commercial feeds |
| [Spotrac bulk](https://www.spotrac.com/service) | Terms ban scraping |

## Use first

Detail is in the entries above. The CSV carries the same priorities.

1. Basketball-Reference season aggregates, already in `avg_game_by_decade`.
2. `nba_api`.
3. `hoopR`.
4. Basketball-Reference scrapers: `basketball_reference_scraper`, `ballr`, hoopR `bref_*`.
5. hoopR-data or `shufinskiy/nba_data`, on local disk only.
6. Barttorvik CSVs.
7. EuroLeague via `py-euroleague`.
8. `wehoop` or `sportsdataverse-py` for the WNBA.
9. Basketball-Reference contracts, and the Draft Combine.
10. awesome-nba-data, as an index.

## See also

- [ROADMAP.md](../ROADMAP.md)
- [data/mentions.csv](../data/mentions.csv)
- [open_datasets.csv](open_datasets.csv)
- [BASKETBALL-SOFTWARE.md](BASKETBALL-SOFTWARE.md)
- [SLOAN-ARCHIVE.md](SLOAN-ARCHIVE.md)
