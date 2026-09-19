# Chapter-Level Artifact Status

Tracks the status of datasets, tables, and derived artifacts referenced in the *Hoops* manuscript. Cross-references with `data/mentions.csv` for detailed source tracking.

## Status Definitions

- **ready:** Dataset/artifact available and regenerable
- **partial:** Incomplete or placeholder data
- **linked:** Source identified but not yet downloaded/processed
- **missing:** Referenced in manuscript but source not identified
- **hold:** Intentionally deferred (e.g., proprietary tracking data)

---

## GAME TIME

### Average Game by Decade

**Status:** ✅ **ready**

**Artifact:** `data/derived/avg_game_by_decade.csv`  
**Methodology:** `data/derived/avg_game_by_decade_methodology.md`  
**Source:** Basketball-Reference.com league averages (1979-80 through 2023-24)

**Regenerate:**
```bash
uv run python scripts/build_avg_game_by_decade.py
```

**Key Stats (2023-24):** 88.9 FGA, 47.0% FG, 35.1 3PA, 36.7% 3P, 21.7 FTA, 43.6 REB, 26.7 AST, 110.6 PTS

**Notes:**
- No Kaggle credentials required (uses committed source CSV)
- Decade aggregation from 45 seasons (1979-80 to 2023-24)
- 2020s decade incomplete (4 seasons as of 2024)

---

## TEAM / Front Office

### Efficiency Table

**Status:** 🟡 **partial**

**Referenced:** Forbes 2015-16 data (Blazers: lowest payroll, 48 wins, 98%+ attendance)  
**Source:** Forbes / SportNEX, cited in draft; dataset unnamed

**TODO:** Identify complete dataset or reconstruct from Forbes archives

---

## PLAYERS / Characteristics

### Height Evolution

**Status:** 🔗 **linked**

**Source:** https://runrepeat.com/height-evolution-in-the-nba  
**TODO:** Extract time series if chapter keeps the height claim

---

## GAME TIME / Officiating

### Referee Stats (2023-24)

**Status:** 🔗 **linked**

**Source:** https://www.nbastuffer.com/2023-2024-nba-referee-stats/  
**TODO:** Download if manuscript uses referee data

---

## LEAGUE / Disputes

### FIBA BAT Statistics

**Status:** 🔗 **linked**

**Source:** https://www.fiba.basketball/bat-statistics-2022.pdf  
**TODO:** Extract table if disputes chapter needs arbitration data

---

## LEAGUE / Income

### Revenue Breakdown

**Status:** ❌ **missing**

**Ingredients:** Television, salaries, attendance, licensing, arena revenue  
**TODO:** Identify dataset with historical breakdown

---

## STADIUM / Home Court

### Home Court Advantage (2024 Playoffs)

**Status:** ❌ **missing**

**Referenced:** "Home-court advantage appeared to evaporate in the 2024 playoffs"  
**TODO:** Identify source or compute from 2024 playoff box scores

---

## BROADCAST / Marketing

### Advertisement Spreadsheet

**Status:** ❌ **missing**

**Referenced:** Binder item "spreadsheet of ads" has no body  
**TODO:** Clarify scope with manuscript author

---

## ANALYTICS / State of the Data

### SportVU / Second Spectrum

**Status:** 🚫 **hold**

**Reason:** Proprietary tracking data (about 1M entries per game)  
**Action:** Narrative citations only; do not download feeds

---

## Notes

- **Kaggle datasets:** Documented in `data/raw/LICENSES.md` as optional/future
- **Zotero integration:** Study citations tracked separately in `hoops` collection
- **Scrivener editing:** Manuscript stays out of this repo (project-level gate)

---

**Last Updated:** 2024-09-19  
**See Also:** `data/mentions.csv`, `ROADMAP.md`
