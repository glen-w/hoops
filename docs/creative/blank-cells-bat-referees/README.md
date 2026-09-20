# Blank Cells, BAT, and Referees

A creative micro-pack exploring data ethics, legal infrastructure, and invisible labor through three short essays anchored in the repository's derived datasets.

## Form

Each piece is a structured vignette (a few hundred words, multi-section narrative) blending pop-science clarity with data-backed argument. Voice is imaginative; facts are cite-only.

## Data Discipline

**Hard constraint**: All numbers, dates, and structural claims cite landed derived CSVs or documented methodology notes in this repository. No invented statistics. Each essay includes a citation footer with:
- CSV path and row/column references
- Access dates
- Source URLs where applicable

## Essays

1. **The Blank-Cell Manifesto** — Intentional blanks in salary cap/apron data (COVID MLE blanks, pre-2023 apron blanks) as a data-ethics vignette about provenance and precision.
2. **FIBA BAT as Legal Seismograph** — Case counts by year (2007–2025) from `fiba-bat-2022/` as a timeline essay: the BAT as infrastructure, not scandal.
3. **Referee as Invisible Athlete** — From `nba-referees-2023-24/`: game counts, experience gradients, foul differentials, and the structural invisibility of officiating labor.

## Sources

All numbers drawn from:
- `data/derived/salary_cap_apron/nba_salary_cap_apron_history.csv` — Official NBA salary cap, tax, apron, and MLE figures (2016–17 through 2026–27)
- `data/derived/fiba-bat-2022/fiba_bat_arbitration_by_year.csv` — FIBA BAT annual case statistics (2007–2025)
- `data/derived/nba-referees-2023-24/nba_referees_2023_24.csv` — NBA referee workloads and foul distributions (2023–24 season)

## Motifs

Common themes include:
- **blank-cell-ethics** — Empty cells as documentary fidelity, not error
- **seismograph** — The BAT as a recorder of contractual friction, not a judgment
- **invisible-labor** — Referees as full-season athletes whose work is not box-scored
- **provenance** — Citation discipline as the foundation of data storytelling

See `motif_tags.csv` for the full mapping.

## Background

These essays were created as a creative drop for the *Hoops* manuscript data sandbox (2026-09-20). The pack sits alongside **Box-Score Sonnets**, **Ghost Franchises**, and **FIBA BAT Postcards** in `docs/creative/` — imaginative writing that refuses to invent a single number.
