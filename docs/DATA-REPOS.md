# Basketball Data Repositories & Tools

Curated catalog of public Git repositories and tools for basketball data acquisition, analysis, and research. This catalog supports the *Hoops* field guide by identifying reliable data sources, not by hosting datasets.

## Purpose

This is a reference guide, not a data warehouse. Each entry describes:
- What data or functionality it provides
- Language and key dependencies
- License and redistribution terms
- Relevance to the book's analytics, training, or socio chapters
- Known risks: rate limits, Terms of Service constraints, scraping policies

---

## Primary Data APIs & Wrappers

### nba_api

**Repository:** https://github.com/swar/nba_api  
**Language:** Python  
**License:** MIT  
**Maintained:** ✓ Active (as of 2026)

**What it provides:**
- Python wrapper for NBA.com's official stats endpoints
- Box scores, play-by-play data, player tracking stats, shot charts
- Coverage from ~1996 onward (varies by endpoint)
- Both modern and legacy endpoint support

**Book usefulness:**
- **Analytics chapter:** Primary source for modern box score tables, shooting efficiency, and tempo metrics
- **Skills chapter:** Shot chart data for accuracy analysis
- **GAME TIME chapter:** Play-by-play for possession flow analysis

**Risks & constraints:**
- Unofficial wrapper; NBA.com may change endpoints without notice
- Rate limiting: respect server load (implement delays between requests)
- No ToS violation as it uses public endpoints, but scraping etiquette applies
- Does not include SportVU tracking data (proprietary, not available)

**Example use cases:**
- Regenerating "average game by decade" tables
- Building shot location heatmaps
- Computing possession-level statistics

---

### hoopR (sportsdataverse)

**Repository:** https://github.com/sportsdataverse/hoopR  
**Language:** R  
**License:** MIT  
**Maintained:** ✓ Active (part of sportsdataverse ecosystem)

**What it provides:**
- R package for NBA, WNBA, and NCAA basketball data
- Integrates data from NBA.com, ESPN, KenPom (college)
- Play-by-play, box scores, player stats, team ratings
- Includes historical college data and advanced metrics

**Book usefulness:**
- **Analytics chapter:** R-based workflows for statistical modeling
- **Training chapter:** College-to-pro trajectory data
- **SOCIETY chapter:** WNBA and NCAA coverage for gender/amateur discussion

**Risks & constraints:**
- Aggregates multiple sources; each has its own ToS
- KenPom data requires subscription for full access
- ESPN scraping subject to their robots.txt and rate limits
- College data coverage varies by conference and year

**Example use cases:**
- WNBA comparison tables
- NCAA tournament performance analysis
- Building predictive models in R

---

### basketball_reference_scraper

**Repository:** https://github.com/vishaalagartha/basketball_reference_scraper  
**Language:** Python  
**License:** MIT  
**Maintained:** ✓ Active

**What it provides:**
- Python scraper for Basketball-Reference.com
- Historical stats, box scores, advanced metrics (BPM, VORP, Win Shares)
- Season summaries, player career data, team records
- Coverage back to BAA/NBA inception (1946–)

**Book usefulness:**
- **Analytics chapter:** Historical context for modern metrics (BPM, RAPM evolution)
- **GAME TIME / average game:** Decade-by-decade statistical evolution
- **History chapter:** Long-term trends in pace, scoring, rebounding

**Risks & constraints:**
- **Scraping-dependent:** Basketball-Reference.com explicitly allows limited scraping but requests courtesy
- Must include User-Agent header and respect rate limits (1 request per 3 seconds recommended)
- Commercial use restrictions: check Basketball-Reference's ToS
- Site structure changes may break scraper
- No play-by-play (only box score summaries)

**Example use cases:**
- Extracting 1950s–present statistical trends
- Building player comparison tables
- Fetching referee assignment data (limited availability)

---

### nbadb / wyattowalsh

**Repository:** https://github.com/wyattowalsh/nbadb  
**Kaggle Dataset:** https://www.kaggle.com/datasets/wyattowalsh/basketball  
**Language:** Python (SQLite database schema)  
**License:** CC0 (dataset); MIT (scripts)  
**Maintained:** ✓ Active (last updated 2024–2025 season)

**What it provides:**
- Comprehensive SQLite database of NBA stats (1946–present)
- Normalized schema: teams, players, games, box scores, play-by-play
- Pre-processed and indexed for fast queries
- Includes draft data, salary information, and injury reports

**Book usefulness:**
- **Analytics chapter:** All-in-one database for statistical analysis
- **GAME TIME / average game:** Easy decade-by-decade aggregation
- **Front-office efficiency:** Salary and payroll data
- **SOCIETY chapter:** Draft and career trajectory analysis

**Risks & constraints:**
- **Kaggle API credentials required** for dataset download  
  **STATUS: Phase later — blocked on Kaggle authentication**
- Dataset size: ~2GB compressed, ~8GB uncompressed
- Kaggle ToS: attribution required, commercial use allowed with restrictions
- Database updates lag by a few weeks (not real-time)

**Example use cases:**
- Running SQL queries for custom aggregations
- Generating "average game" tables by decade
- Analyzing home court advantage trends

**Script location:** `scripts/fetch_wyattowalsh.sh` (retained, awaiting credentials)

---

## Analysis & Research Tools

### NBA Data Repositories (various)

Additional tools and datasets verified for research use:

#### PBPstats
**Repository:** https://github.com/dblackrun/pbpstats  
**Language:** Python  
**What it provides:** Play-by-play parsing, lineup analysis, on/off splits  
**Book usefulness:** Lineup efficiency, substitution pattern analysis

#### nba-data-py
**Repository:** https://github.com/DomSamangy/NBA_Drafts_Analysis  
**Language:** Python  
**What it provides:** Draft analysis datasets and visualizations  
**Book usefulness:** Draft value modeling, pick success rates

---

## International & FIBA Data

### FIBA Official Resources
**Website:** https://www.fiba.basketball/  
**What it provides:** International tournament results, player registrations, BAT statistics  
**Book usefulness:**
- **SOCIETY / FIBA scale:** "450 million players" claim verification
- **GAME TIME / international rules:** FIBA rule differences

**Available data:**
- Tournament brackets and results (FIBA Basketball World Cup, Olympics)
- [BAT Statistics PDF](https://www.fiba.basketball/bat-statistics-2022.pdf) (2022 edition)
- National federation registration numbers

**Risks & constraints:**
- No comprehensive API; mostly PDF reports and press releases
- Player-level data not publicly available
- Registration numbers are self-reported by federations

---

## Proprietary / Limited Access (Not for Download)

These datasets are referenced in the book but **not hosted in this repository**.

**For detailed coverage of commercial tracking and analytics systems, see [BASKETBALL-SOFTWARE.md](BASKETBALL-SOFTWARE.md)**, which provides:
- Citation guidelines for SportVU, Second Spectrum, Hawk-Eye, Synergy, and other vendors
- Timeline of NBA/league adoption
- How to reference proprietary systems in scholarly writing
- Public secondary sources (press releases, SSAC papers)

**Brief entries below; full details in BASKETBALL-SOFTWARE.md:**

### SportVU / Second Spectrum
- **Provider:** NBA official tracking partner (2013–)
- **Coverage:** Player tracking (25 FPS), ~1 million data points per game
- **Status:** Proprietary, not publicly available
- **Book reference:** Analytics chapter (state of the data)
- **See:** [BASKETBALL-SOFTWARE.md](BASKETBALL-SOFTWARE.md) for citation guidelines

### DeepSportRadar-v1
- **Source:** https://paperswithcode.com/dataset/deepsportradar-v1
- **Coverage:** Annotated broadcast video dataset (basketball + other sports)
- **License:** Research use only
- **Status:** Available for academic research with registration
- **Book usefulness:** Video analysis, YOLO tracking notes

### Synergy Sports Technology
- **Provider:** Commercial scouting platform
- **Coverage:** Play-type tagging, defensive matchups
- **Status:** Subscription required; not public
- **Book reference:** Front-office tools chapter
- **See:** [BASKETBALL-SOFTWARE.md](BASKETBALL-SOFTWARE.md) for full vendor profile

---

## Best Practices for Data Use

1. **Attribution:** Always cite the source (repository, dataset, website)
2. **Rate limiting:** Respect API and scraping guidelines (typically 1 req/3s)
3. **ToS compliance:** Check each source's Terms of Service before redistribution
4. **Licensing:** Verify license compatibility (MIT, CC0, CC-BY) before publishing derived work
5. **Reproducibility:** Document data version, date accessed, and processing steps
6. **No gambling data:** Avoid betting odds datasets (out of scope for this book)

---

## Contributing to This Catalog

To add a new resource:
1. Verify the repository is actively maintained (commits in past year)
2. Check license (prefer MIT, CC0, CC-BY)
3. Test a sample query or download
4. Document what it provides and which book chapters it supports
5. Note any ToS or rate limit warnings

This catalog was last updated: **September 19, 2026**
