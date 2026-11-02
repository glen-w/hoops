# Coder tick 2026-10-23 summary

**Hoops book status:** ~74.7k words, 441 sections. Biggest holes: MEDIA (7%), FIN (10%), STADIUM (20%).

---

## Grokbot triage complete (14 items)

**All items processed. Verdicts:**
- FT pressure analysis → integration guidance ready (game_time_ft_pressure_cascade.md)
- Code archive paths set (4 scripts → tools/reproducible/ft_pressure_2026-10-22/)
- Zotero keys verified: 48 new items (tag: nightshift-2026-10-22)
- Literature briefs kept for future sections (kinematic variance, automaticity, fatigue, release variability)
- Raw data: summary CSVs extracted; attempt-level 12.2 MB gzipped preserved for reproducibility

**Key finding:** Cascade hypothesis (Hore workload → Rusdiana kinematics → Kinrade reinvestment) partially supported at outcome (pressure −2.5 to −5.3 pp, real). Workload×pressure interaction null; selection effect, not fatigue amplification.

---

## Immediate handoffs

### GAME TIME chapter
- **FT pressure ready to integrate NOW.** Do not wait for MEDIA/FIN/STADIUM.
- Integration guidance: analysis/game_time_ft_pressure_cascade.md
- 7 Zotero keys verified; cite Cao, Toma, Esteves, Arkes, Lantis, Morgulev, Steenland
- Outcome: −2.5pp late-close (≤1 min, ≤3 pts), −5.3pp trailing, p < .001, n=519,640
- Claim: Pressure observable at outcome level; workload does not amplify
- Limitations: observational; can't separate fatigue from selection

---

## Biggest holes → researcher sourcing + coder analysis

**Roadmap:** analysis/MEDIA_FIN_STADIUM_roadmap.md (detailed actions)

### MEDIA (7% → library gap confirmed)
- **In library:** 2016-24 national TV (ABC/ESPN/TNT), pre-2020 sponsorship context
- **Gap:** 2024-25 streaming split (Amazon, Apple, ESPN+), current naming rights inventory, jersey patch contracts, RSN bankruptcy (Sinclair/Diamond post-2023)
- **Coder next:** After researcher sources 2024-25 deals: build media_income_ingredients.csv (parallel to league_income_ingredients.csv)

### FIN (10% → library gap confirmed)
- **In library:** Salary cap history (corrected 2026-10-23), league income ingredients 2016-24, pre-2010 arena patterns
- **Gap:** Post-2010 arena subsidy cases (Vegas, SoFi, Crypto.com, Intuit: 9 Zotero keys pending validation), post-2010 sponsorship trends
- **Blocker:** Researcher validation of 9 Zotero keys; coder debug hoops_record arena path (2026-10-24)
- **Coder next:** After keys validated: extract subsidy %, cost, financing → build arena_financing.csv

### STADIUM (20% → library gap confirmed)
- **In library:** Pre-2010 design evolution, capacity trends, amenity categories
- **Gap:** Post-2010 new builds (SoFi, Crypto.com, Intuit, Vegas Allegiant, Fiserv: architecture, cost per seat, design philosophy)
- **Coder next:** After researcher sources post-2010 builds: build stadium_features.csv (capacity, suites, signature feature, cost, architect, source_url)

---

## Nightshift requests consolidated

**Updated:** analysis/nightshift_requests.json (7 items)
- CRITICAL: Salary-cap CSV (DONE 2026-10-23)
- HIGH: MEDIA 2024-25 (researcher sourcing 2026-10-24+)
- HIGH: MEDIA sponsorship inventory (researcher sourcing 2026-10-24+)
- HIGH: FIN post-2010 arenas (blocked on Zotero validation 2026-10-24)
- HIGH: hoops_record arena path debug (coder 2026-10-24)
- MEDIUM: RSN landscape (optional 2026-10-25)
- MEDIUM: Zotero reconciliation (researcher cleanup 2026-10-25)
- HIGH: FT pressure ready to integrate (coder immediately)

---

## Data files ready for citation

**In analysis/game_time_ft_pressure_cascade.md:**
- ft_models.csv (17.6 KB): model coefficients, SEs, p, marginal effects
- ft_pressure_workload_summary.csv (38.7 KB): descriptive by season type × context × workload
- ft_attempts_2015-2024.csv.gz (12.2 MB): attempt-level data, reproducible

**Data citation:** shufinskiy, *nba_data: NBA play-by-play and shot details 1996/97–2024/25* (GitHub Apache-2.0), derived from stats.nba.com. Accessed 22 Oct 2026.

---

## Code archive path

Move these scripts from grokbot to tools/reproducible/ft_pressure_2026-10-22/:
- build_ft.py (4.8 KB)
- enrich.py (3.4 KB)
- analyze.py (4.2 KB)
- robustness_and_proxies.py (4.1 KB)

These are reproducible; preserve for future validation or extension to 1996–2015 or 2024–25 seasons.

---

## Researcher dependencies (for daytime)

1. **Validate 9 Zotero arena subsidy keys** (Vegas, SoFi, Crypto.com, Intuit) → blocks FIN/STADIUM retry
2. **Source 2024-25 MEDIA streaming + sponsorship** → enables media_income_ingredients.csv build
3. **Source post-2010 stadium features** → enables stadium_features.csv build
4. **Reconcile endnotes 38k vs. bibliography 464 words** (Zotero audit for dups, missing URLs, incomplete citations)

Researcher updates hoops/nightshift_requests.json with findings; coder builds analysis CSVs and updates analyst guidance docs.

---

## Next coder actions (2026-10-24+)

1. Integrate FT pressure into GAME TIME chapter (no wait)
2. Debug hoops_record arena path (Vegas test case)
3. After researcher validation: build media_income_ingredients.csv, arena_financing.csv, arena_naming_rights.csv, stadium_features.csv
4. Update chapter spines in analysis/ (MEDIA, FIN, STADIUM) for researcher integration into Scrivener

**Principle:** Library first, no invented numbers. If researcher can't source, mark out-of-scope in endnotes.
