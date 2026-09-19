# Raw Data Sources and Licenses

This file documents the provenance, licensing, and redistribution terms for datasets that **may** be downloaded into `data/raw/`. Raw data files are **not committed** to this repository due to size and licensing constraints.

Currently, derived tables are generated from public APIs (nba_api, Basketball-Reference) without requiring local raw dumps. Bulky datasets below are documented for future use.

---

## Future/Optional Sources

### wyattowalsh/basketball (Kaggle)

**Source:** [Kaggle - Basketball Dataset](https://www.kaggle.com/datasets/wyattowalsh/basketball)  
**Author:** Wyatt Walsh  
**License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
**Status:** **Optional - not required for current derived tables**  
**Description:** Comprehensive NBA statistics including box scores, player stats, team data, and game information. May be used for future per-position and detailed game-level analysis.

**Redistribution Terms:**
- Original data: **Not redistributed** (would stay in gitignored `data/raw/`)
- Derived tables: **May be committed** under CC BY-SA 4.0 with attribution
- Attribution required: Credit Wyatt Walsh and link to original dataset

**Fetch Instructions (when needed):** See `scripts/fetch_basketball_data.py` - requires Kaggle API credentials.

---

## Active Data Sources (API/Web-Based)

### nba_api

**Source:** [nba_api Python package](https://github.com/swar/nba_api)  
**License:** MIT License  
**Status:** **Active - used for derived tables**  
**Description:** Python API client for NBA.com endpoints. Provides league-wide statistics, team data, and historical season averages.

**Redistribution Terms:**
- API data from NBA.com: Public statistics, freely redistributable
- Derived aggregations: May be committed with attribution to NBA.com and nba_api

**Usage:** See `scripts/generate_avg_game.py`

### Basketball-Reference.com

**Source:** https://www.basketball-reference.com/  
**License:** Public statistics (respectful scraping)  
**Status:** **Active - used for historical averages**  
**Description:** Comprehensive basketball statistics archive maintained by Sports Reference LLC.

**Redistribution Terms:**
- Season-level aggregates: May be redistributed with attribution
- Attribution required: Credit Basketball-Reference.com

**Usage:** Historical team/league averages via nba_api or direct citation

---

## Additional Future Sources (Not Yet Downloaded)

### DeepSportRadar v1
**Source:** https://paperswithcode.com/dataset/deepsportradar-v1  
**Status:** Under consideration for tracking-style analysis  
**Notes:** Only to be downloaded if manuscript requires tracking data samples

### Data.world Basketball Catalog
**Source:** https://data.world/datasets/basketball  
**Status:** Exploratory - alternative box score sources  
**Notes:** License terms vary by dataset

### Kaggle Basketball Thread
**Source:** https://www.kaggle.com/discussions/general/52669  
**Status:** Curation resource  
**Notes:** Collection of basketball dataset links

---

## License Compliance Notes

1. **Storage:** Raw data files stay in `data/raw/` (gitignored)
2. **Commits:** Only derived/aggregated tables go into `data/derived/`
3. **Attribution:** All derived tables must credit source datasets
4. **Proprietary Data:** No NBA tracking feeds (SportVU, Second Spectrum) - narrative citations only
5. **Zotero Connection:** Studies and papers tracked in Zotero `hoops` collection, not this repo

---

**Last Updated:** 2026-09-19  
**Maintainer:** See repository README
