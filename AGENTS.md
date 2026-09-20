# Agent brief — glen-w/hoops

Read this before any PR. Full policy: [SCOPE.md](SCOPE.md). Checklist: [CONTRIBUTING.md](CONTRIBUTING.md).

## What this repo is

Public **data sidecar** for the Hoops book. Scrivener = prose. Zotero `hoops` = citations. This git tree = derived tables, builders, thin catalogs, short method notes.

## Do

- Land cite-backed artifacts under `data/derived/<product>/` with a short `method.md` / `methodology.md` / `SOURCE.md`.
- Put draft hedges in `data/studies/<slug>.md`.
- Append **at most one** 4-cell row to `docs/CHAPTER-MAP.md` (`topic | path | cite | status`). Status ≤ ~20 words.
- Put regenerable builders in `scripts/` or `src/hoops_data/` only when they emit or validate a committed artifact.
- Prefer blanks / `GAP` over invented numbers. Cite, don’t rehost proprietary data.

## Do not

- Commit creative packs, essays, sonnets, postcards, hooks, motif CSVs, spike/phase/STATUS diaries.
- Append narrative or Phase notes to CHAPTER-MAP.
- Commit manuscript, Zotero DB/PDFs, `data/raw` dumps, CBA PDF/fulltext.
- Open a PR whose citeable output is a story rather than a path under `data/derived/` or `data/studies/`.

## Scratch

Creative drafts, motif indexes, notebooks, and process notes → gitignored `local/` (one repo; no private sibling).

## Truth sources for writing support

`ROADMAP.md`, `data/mentions.csv`, short method notes beside `data/derived/*`.
