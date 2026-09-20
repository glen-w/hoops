# Phase 0 evidence desk — report

**Date:** 2026-09-19 (access date for all URLs below)  
**Repo context:** glen-w/hoops — PRs #1 and #2 MERGED on main (`avg_game_by_decade` exists; do **not** rebuild). Org-chart CSVs also on main.  
**Deliverables path:** `/workspace/hoops-phase0/` (Infra can PR; no GitHub write from this lane)

---

## 1. Unnamed study resolutions

### Competitive balance (revenue sharing / salary caps; NFL, MLB, NBA, NHL)

| Field | Value |
|-------|--------|
| **Best ID** | Evan S. Totty & Mark F. Owens (2011). *Salary Caps and Competitive Balance in Professional Sports Leagues.* Journal for Economic Educators 11(2): 46–56 |
| **URL** | https://libjournals.mtsu.edu/index.php/jfee/article/view/1474 — PDF https://libjournals.mtsu.edu/index.php/jfee/article/download/1474/1056 |
| **Label** | SECONDARY |
| **Confidence** | HIGH-MEDIUM (~0.80) |
| **Zotero** | Not in `hoops` yet — **add** |
| **Hedge** | Draft: “e.g. Totty & Owens (2011)” until Scrivener confirms. In-library alt: Vrooman (2009) *Theory of the Perfect Game* (`M7KEA87F`). |
| **Note** | Caps do not improve balance; revenue sharing does (paper’s finding). |

Study note: `studies/totty-owens-2011-competitive-balance.md`

### Dribbling creativity (sensorimotor cortex; null on creative performance)

| Field | Value |
|-------|--------|
| **Best ID** | Thomas Kanatschnig, Christian Rominger, Andreas Fink, Guilherme Wood, Silvia Erika Kober (2023). *Sensorimotor cortex activity during basketball dribbling and its relation to creativity.* PLOS ONE 18(4): e0284122 |
| **DOI / URL** | 10.1371/journal.pone.0284122 — https://doi.org/10.1371/journal.pone.0284122 — PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC10132548/ |
| **Label** | OFFICIAL academic (PLOS ONE OA) |
| **Confidence** | HIGH (~0.95) |
| **Zotero** | `M53K3EAJ` |
| **Hedge** | Keep null-on-creativity separate from “SMC activity was present.” |

Study note: `studies/kanatschnig-2023-dribbling-creativity.md`

---

## 2. FIBA “~450 million players” — PINNED (vintage)

**Not UNCONFIRMED.** Official FIBA wording exists; figure is mid-2000s / ~2010, not current.

| Source | Exact / close wording | URL | Label |
|--------|----------------------|-----|-------|
| FIBA Quick facts | “Over 450 million people play basketball on competition and grassroots level in **2007**…”; Key dates: “**March 2003**: … estimated **450 million players**” | https://www.fiba.basketball/en/news/fcom-about-fiba-quick-facts | OFFICIAL |
| FIBA Happy Birthday (78th anniv. → 2010) | “over 450 million people regularly practising” | https://www.fiba.basketball/en/news/fiba-happy-birthday-fiba | OFFICIAL |
| World Basketball Day 2024 | “More than **610 million** people … play basketball at least twice a month” | https://www.fiba.basketball/en/news/fiba-celebrates-more-than-610-million-players-globally-on-second-edition-of-wbd | OFFICIAL (current) |

**Suggested prose:** pin 2003/2007 estimate + URL; footnote that FIBA now cites 610M (2024). Do not present 450M as current.

Study note: `studies/fiba-450-million-players.md`

---

## 3. Missing study names — identified

| Draft mention | Full cite | DOI | Zotero | Label |
|---------------|-----------|-----|--------|-------|
| Paulauskas et al. referee HR | Rūtenis Paulauskas, Alejandro Vaquera, Bruno Figueira (2024). *Absence of Monotony and Strain Effects on Referees’ Physical Performance…* Int J Sports Physiol Perform. **12 referees; 7 WC + 7 WC-U19 games; HR + wearables.** Companion: Nabli et al. 2019 narrative review. | 10.1123/ijspp.2023-0199 | `8GYT2RR5` (Nabli `Z5FDUP5M`) | SECONDARY |
| PICO / SCOPUS 21-paper AI referee review | Rafael Thomas-Acaro & Brian Meneses-Claudio (2024). *Technological assistance… systematic literature review.* Data and Metadata 3:188. **PICO + 21 SCOPUS**; multi-sport. | 10.56294/dm2024188 | `89QX6WA8` | SECONDARY |
| Li & Zhang 2021 shooting accuracy | Hongfei Li & Maolin Zhang (2021). *Artificial Intelligence and Neural Network-Based Shooting Accuracy Prediction…* Mobile Information Systems 2021:4485589. Paper: both models “above 70%”; CIRAN contribution “above 90%.” Lv = editor, not author. | 10.1155/2021/4485589 | `ZCHCYQLI` | SECONDARY |
| Gómez et al. 2013 possession | Miguel-Ángel Gómez, Alberto Lorenzo, Sergio-José Ibáñez, Jaime Sampaio (2013). *Ball possession effectiveness…* J Sports Sci 31:1578–1587. | 10.1080/02640414.2013.792942 | `TJLRSX3C` (fix author metadata) | SECONDARY |

Study notes: `paulauskas-2024-referee-hr.md`, `thomas-acaro-2024-ai-referee-pico.md`, `li-zhang-2021-shooting-accuracy.md`, `gomez-2013-possession.md`

**Still open (not this sitting’s hunt target but flagged):** draft “70 pros / 265 injuries / early-season” is **not** Andreoli 2018 (`QPZHSPFR` = integrative review). Hunt separately.

---

## 4. Home-court 2024 playoffs

**Draft:** advantage “appeared to evaporate” in 2024 playoffs — **not supported** by game counts.

| Scope | Numbers | URL | Label |
|-------|---------|-----|-------|
| 2024 playoffs (full) | **82 games**; home **48–34** (**58.54%**) | https://www.basketball-reference.com/playoffs/NBA_2024.html | SECONDARY (BRef schedule parse) |
| 2023–24 regular season | Home **.5431** — “worst home-court mark in league history” | https://www.foxsports.com/articles/nba/inside-the-nba-numbers-lots-of-comebacks-no-homecourt-edge-3s-went-up-scoring-went-down (AP wire) | SECONDARY |
| Early 2024 playoffs | R1 Game 1s **8–0** home; recent R1 home ~58% | https://www.espn.co.uk/nba/insider/story/_/id/40018981/2024-nba-playoffs-real-not-siakam-brunson-scoring | SECONDARY |

**Verdict:** soft playoff HCA (~59%), historically weak regular-season HCA — **not evaporation**. Rewrite STADIUM sentence.

Study note: `studies/home-court-2024-playoffs.md` (candidate for `data/derived/home_court_2024_playoffs.md`)

---

## 5. Enriched mentions pack

**Path:** `/workspace/hoops-phase0/mentions-enriched-2026-09-19.csv`  
**Columns added:** `priority`, `zotero_key`, `doi`, `blocks_section`, `resolution_notes`, `next_action`  
Original 29 data rows kept; filled where resolved.

---

## 6. Suggested CHAPTER-MAP / ROADMAP updates

### CHAPTER-MAP rows to add (when `docs/CHAPTER-MAP.md` is created)

| Binder / section | Data product | Status after Phase 0 |
|------------------|--------------|----------------------|
| GAME TIME / average game | `data/derived/avg_game_by_decade.csv` | **DONE on main** (PR #1) |
| STADIUM / home court | `data/derived/home_court_2024_playoffs.md` | Evidence ready in phase0/studies; needs Infra copy + prose hedge |
| PRE-GAME / popularity | FIBA 450M → pin Quick facts 2003/2007 + 610M 2024 footnote | Evidence ready |
| LEAGUE / competitive balance | Totty & Owens 2011 (+ optional Vrooman 2009) | ID ready; add Zotero |
| Annexes / dribbling creativity | Kanatschnig et al. 2023 (`M53K3EAJ`) | ID ready |
| GAME TIME / possession | Gómez et al. 2013 DOI | ID ready |
| GAME TIME / shooting AI | Li & Zhang 2021 DOI | ID ready; hedge 70/90 |
| Officiating / physical | Paulauskas 2024 + Nabli 2019 | ID ready |
| Officiating / AI assistants | Thomas-Acaro & Meneses-Claudio 2024 | ID ready; multi-sport hedge |
| PLAYERS / height | `nba_height_series.csv` | **Still open** |
| Officiating / referee stats table | `nba_referees_2023_24.csv` | **Still open** |
| Disputes / BAT | `fiba_bat_2022.csv` | **Still open** |
| TEAM / efficiency | `franchise_efficiency_2015_16.md` | **Still open** |
| LEAGUE / income | `league_income_ingredients.md` | **Still open** |
| BROADCAST / ads | ads spreadsheet | **Still open** / maybe drop |

### ROADMAP §3 / §4 one-liners
- §3: mark competitive-balance + dribbling-creativity as **identified** (Totty & Owens; Kanatschnig); Paulauskas / PICO / Li–Zhang / Gómez DOIs filled.
- §4: strike “build avg game by decade” as open; add “home-court: rewrite evaporate claim using BRef 48–34 / 58.5%.”
- §4 FIBA: replace “pin year” with “pinned 2003/2007; update vs 610M 2024.”

---

## 7. Next P0 tables still open (after main)

Already on main (skip): `avg_game_by_decade`; `nba_orgs/` (PR #2).

| # | Product | Path (suggested) | Blocks |
|---|---------|------------------|--------|
| 2 | Home-court 2024 playoffs check | `data/derived/home_court_2024_playoffs.md` | STADIUM (rewrite claim) |
| 3 | Height series | `data/derived/nba_height_series.csv` | PLAYERS / height |
| 4 | Referee stats extract | `data/derived/nba_referees_2023_24.csv` | Officiating |
| 5 | Analytics / FO public list (optional; org charts exist) | `data/derived/nba_analytics_staff.csv` | TEAM / staff |
| 6 | FIBA BAT 2022 extract | `data/derived/fiba_bat_2022.csv` | Disputes |
| 7 | Franchise efficiency (name source or drop “our dataset”) | `data/derived/franchise_efficiency_2015_16.md` | Efficiency table |
| 8 | League income stack | `data/derived/league_income_ingredients.md` | LEAGUE / income |
| 9 | Broadcast ads spreadsheet | only if binder revived | BROADCAST |

**Also P0 hygiene (not tables):** add Totty & Owens to Zotero; fix Gómez / Li author metadata; Scrivener hedges after Sunday pursue — no Scrivener edits this sitting.

---

## 8. Files written this sitting

```
/workspace/hoops-phase0/
  PHASE0-REPORT-2026-09-19.md          ← this file
  mentions-enriched-2026-09-19.csv
  studies/
    totty-owens-2011-competitive-balance.md
    kanatschnig-2023-dribbling-creativity.md
    paulauskas-2024-referee-hr.md
    thomas-acaro-2024-ai-referee-pico.md
    li-zhang-2021-shooting-accuracy.md
    gomez-2013-possession.md
    fiba-450-million-players.md
    home-court-2024-playoffs.md
```

No Scrivener edits. No gambling datasets. No rebuild of `avg_game_by_decade`.
