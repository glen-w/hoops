# Roadmap

Sidecar for the book, not the book. Prose stays in Scrivener. Citations stay in Zotero. Public framing is the [glenwright.earth project page](https://glenwright.earth/projects/hoops/): a field guide to noticing the game, not a history, a tactics manual, or a hero ranking.

Untangle still has the book as incubating, with a pursue / laterbase / drop call on Sunday 20 September 2026. This repo is the research tooling that call does not block. It does not include writing the blurb, intro, or chapter.

Scanned 18 September 2026. Binder last saved 14 September 2026. Trash and the 14 September recovered-files folder were skipped. 343 documents had text. A keyword pass hit 690 sentences; 215 of those were endnotes. The actionable list is [data/mentions.csv](data/mentions.csv).

Zotero collection `hoops`: 1,357 items, 1,175 of them journal articles. The largest subcollections already mirror the draft: analytics (223), incomplete (155), training (137), socio/anthro/ethno (132), crowd/fans (122), history (115). Missing PDFs are [Paperful](https://github.com/glen-w/Paperful)'s job, not this repo's.

## 1. Connect — done in this commit

- Repo on GitHub.
- Scrivener MCP in `.cursor/mcp.json` (`npx -y scrivener-mcp`). Reload Cursor, then open `/Users/89298/Documents/Hoops/hoops.scriv`. Read the draft from here. Do not write prose into it until the Sunday call is pursue.
- Inventory of data mentions checked in.

## 2. Land the four datasets the Research folder already names

The `datasets` note, and the annotation on `GAME TIME / average game`, point at:

- [Kaggle: basketball datasets thread](https://www.kaggle.com/discussions/general/52669)
- [wyattowalsh/basketball](https://www.kaggle.com/datasets/wyattowalsh/basketball) — **Phase later: blocked on Kaggle API credentials**
- [data.world basketball catalog](https://data.world/datasets/basketball)
- [DeepSportRadar v1](https://paperswithcode.com/dataset/deepsportradar-v1)

Download into `data/raw/` (gitignored). Commit only a license note and any derived table we are allowed to redistribute. No NBA tracking dumps.

**Note:** The script `scripts/fetch_wyattowalsh.sh` is retained but labeled as requiring Kaggle authentication. Kaggle dataset download is deferred until credentials are available.

## 3. Match cited studies to Zotero, then decide what to recompute

The draft already narrates results. The sidecar should point at the paper, and recompute only where the book needs a table of its own.

- Gómez et al. 2013 — 7,234 ball possessions, 40 Spanish league games, 2006–07, logistic regression (`GAME TIME / flow`).
- Li & Zhang 2021 — neural shooting-accuracy model (`skills / scoring / accuracy`).
- Paulauskas et al. — 12 referees, heart rate and tracking; plus a 21-paper SCOPUS review of AI referee tools.
- Bodvarsson & Brastow 1999 — salary regressions for 1985–86 and 1990–91; Brown et al. 1991 beside it (`SOCIETY / race / wage gap`).
- Andreoli et al. 2018 and the ten-year study of 70 professionals, 265 injuries.
- Rim-rolling dynamics paper linked under `ball / physics`.
- Competitive-balance comparison (NFL, MLB, NBA, NHL) and the dribbling-creativity null result are cited without a name. Identify them in Zotero before treating them as sources.

## 4. Build the tables the draft asks for and does not have

- **Average game, by decade.** The 2023–24 line is already drafted (88.9 field-goal attempts, 47% field goals, 35.1 threes, 21.7 free throws, 33 defensive rebounds, 10.6 offensive rebounds, 26.7 assists). The per-decade table is a placeholder. Source candidate: the Kaggle set above.
- **Front-office efficiency.** `efficiency / table` sketches 2015–16 from Forbes 22 Apr 2016 (NOT FOUND, searched 2026-09-19). Corrected source: OregonLive 13 May 2016 (Odom) — Blazers lowest payroll ($61.69M), **44 wins** (not 48; that's Boston); Celtics 14th payroll, 48 wins (~59%). Attendance 98%+ is separate (Forbes/Brown Jun 2016, SBJ).
- **Home court.** One sentence: the advantage "appeared to evaporate in the 2024 playoffs." No source in the document.
- **Broadcast ads.** Binder item `spreadsheet of ads` has no body.
- **League income.** Television, salaries, attendance, licensing, arena revenue — named as the ingredients, not assembled.
- **Height.** Link only, to [runrepeat.com/height-evolution-in-the-nba](https://runrepeat.com/height-evolution-in-the-nba). Pull a series if the chapter keeps the claim.
- **Referees.** [2023–24 NBA referee stats](https://www.nbastuffer.com/2023-2024-nba-referee-stats/) is annotated and unused.
- **FIBA scale.** "Something like 450 million" players, footnoted to FIBA. Pin the year and the publication.
- **FIBA BAT.** [2022 statistics PDF](https://www.fiba.basketball/bat-statistics-2022.pdf), linked from disputes, not yet a table.

## 5. Analytics chapter: describe the pipes, do not host them

`ANALYTICS / state of the data` covers SportVU (about a million entries a game; NBA provider until 2017) and Second Spectrum (the replacement). The timeline names Reb%, BPM, RAPM, PTPM, and "Data Ball" from 1997. Those are licensed products and a glossary. The sidecar keeps public box-score series and citations. YOLO tracking notes are a method, not a collection job.

Front-office staff lists on [NBAstuffer](https://www.nbastuffer.com/analytics101/nba-teams-that-have-analytics-department/) are fair game as a small public table.

The open-data map is [docs/NUMBERS-LANDSCAPE.md](docs/NUMBERS-LANDSCAPE.md), the source catalog is [docs/DATA-REPOS.md](docs/DATA-REPOS.md), and the row list is [docs/open_datasets.csv](docs/open_datasets.csv). Cite that from "state of the data." Do not paste the catalog into the chapter.

## 6. Later, not this sitting

- Ground a model on the Zotero library. Trial is zotero-rag at `/Users/89298/Documents/zotero-rag`, collection `hoops` only. Plan notes stay in `author/process/` if needed — not a download, not a citeable sidecar doc.
- Gambling odds. The fans chapter describes the machinery. Do not build a betting dataset.
- Anything that would edit the manuscript. Wait for the Sunday call.

## Out of scope

Writing the book. The website. Fetching PDFs. Committing `.scriv`, Zotero, or proprietary tracking data.

Creative packs, speculative essays, spike/phase diaries, and agent process theatre live under committed [`author/`](author/README.md) — see [SCOPE.md](SCOPE.md). Voice experiments also go in Scrivener. Do not land them under `docs/` or `data/derived/`.
