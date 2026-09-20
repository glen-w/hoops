# Agent brief — glen-w/hoops

Read this before any PR. Full policy: [SCOPE.md](SCOPE.md). Checklist: [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is

Public **data sidecar** for the Hoops book. Scrivener = prose. Zotero `hoops` = citations. This git tree = derived tables, builders, thin catalogs, short method notes — plus a committed **`author/`** workspace for creative/process so every clone and cloud agent sees it.

## Do

- Land cite-backed artifacts under `data/derived/<product>/` with a short `method.md` / `methodology.md` / `SOURCE.md`.
- Put draft hedges in `data/studies/<slug>.md`.
- Append **at most one** 4-cell row to `docs/CHAPTER-MAP.md` (`topic | path | cite | status`). Status ≤ ~20 words.
- Put regenerable builders in `scripts/` or `src/hoops_data/` only when they emit or validate a committed artifact.
- Prefer blanks / `GAP` over invented numbers. Cite, don’t rehost proprietary data.
- Write creative packs, motif indexes, sonnets, hooks, and spike diaries under **`author/`** (committed).

## Do not

- Put creative/process under `docs/creative/`, `data/derived/creative/`, or other artifact paths — use `author/` instead.
- Append narrative or Phase notes to CHAPTER-MAP (and never point CHAPTER-MAP at `author/`).
- Commit manuscript, Zotero DB/PDFs, `data/raw` dumps, CBA PDF/fulltext.
- Treat an `author/` essay as a citeable deliverable in an artifact PR.

## Author workspace (committed)

Creative work **belongs in this repo** under `author/` so agents always have it. See [author/README.md](author/README.md).

**Cite boundary:** only `data/derived/` and `data/studies/` are what a writer cites. `author/` is draft/motif/process. Machine-only scratch stays in gitignored `local/`.

## Truth sources for writing support

`ROADMAP.md`, `data/mentions.csv`, short method notes beside `data/derived/*`.
