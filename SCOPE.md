# Sidecar scope

**Audience:** humans and agents opening PRs against `glen-w/hoops`.  
**Default for the next ~30 days:** freeze creative/process theatre; land tables, hedges, and regenerable builders.

This repo is the **public data sidecar** for *Hoops: An Uncommon Field Guide to the Game of Basketball*. Prose lives in Scrivener. Citations live in Zotero `hoops`. Public framing lives on [glenwright.earth/projects/hoops](https://glenwright.earth/projects/hoops/). Do not rewrite the book here.

## Channel paste (verdict)

**Public stays:** redistributable derived CSVs/JSON, short method notes beside them, thin catalogs (`mentions.csv`, CHAPTER-MAP spine, source maps), regenerable `scripts/` / `src/`, schemas, tests.  
**Moves / freezes:** speculative essays, creative packs, motif vignettes, spike diaries, agent status writeups, “hooks” and voice drafts → `local/` (already gitignored) or stay uncommitted; do not open PRs for them.  
**Ignored (already):** `data/raw/**` dumps, manuscript, Zotero, proprietary tracking. Expand ignore for agent scratch under `local/` only — do not gitignore tracked allowlisted paths.  
**PR rule of thumb:** if the diff does not add or harden a cite-backed artifact (or a one-line CHAPTER-MAP / ROADMAP pointer to it), reject it.

## Architecture (locked — do not re-litigate)

| Layer | Where |
|-------|--------|
| Manuscript prose | Scrivener (`.scriv` — never commit) |
| Citations / PDFs | Zotero `hoops` (+ Paperful for missing PDFs) |
| Public framing / blurb | glenwright.earth project page |
| Sidecar (this repo) | Derived tables, builders, catalogs, short method notes |

## In vs out

| Commit (in) | Do not commit (out) |
|-------------|---------------------|
| Redistributable derived tables + license/provenance | Speculative essays, creative packs, voice drafts |
| Regenerable scripts that emit those tables | Author exploration notebooks that emit no artifact |
| Thin catalogs that unblock writing (`mentions.csv`, CHAPTER-MAP rows, source maps) | Process writeups, spike diaries, agent scratch, “how we thought about it” |
| One short method note per derived product | Long brainstorms, alternative framings, motif essays |
| Draft **blockers / hedges** (wrong claim, year pin, unnamed study) as a study note or status cell | Narrative appends to CHAPTER-MAP Notes |

### Method note vs “showing the working”

A method note stays in-scope when it answers, in roughly **≤ ~100 lines**: source class, schema, blank rules, confidence, how to regenerate.  
It becomes out-of-scope theatre when it narrates agent paths (`/workspace/...`), lane collisions, PR choreography, productization stories, or motif/voice essays longer than the table they describe.

**Good pattern:** `data/derived/salary_cap_apron/methodology.md` (schema + primary-source rule).  
**Out of pattern:** `docs/cba/SPIKE-REPORT.md`, `docs/PHASE0-REPORT-*.md`, `docs/creative/**` essays, `data/derived/creative/**/guide.md`, `docs/average/hooks.md`.

### When is creative content “required”?

The book’s uncommon / field-guide voice is a **manuscript** job (Scrivener) and a **site** job (glenwright.earth). Cite-backed sonnets, postcards, and pilgrimage essays are optional voice experiments. They are **not** required for the sidecar to do its job. Motif **CSV indexes** that only point at landed rows are closer to catalogs; the prose packs are not. Until Glen explicitly re-opens a creative lane, treat creative packs as **frozen**.

## Path allowlist / denylist

### Allow (commit)

- `data/derived/**/*.csv`, `*.json` (redistributable products)
- `data/derived/**/method.md` | `methodology.md` | `SOURCE.md` | `README.md` (short)
- `data/cba/<edition>/derived/*.json` + `metadata.json` / hashes (no agreement text)
- `data/reference/**`, `data/studies/*.md` (one short note per cited claim/paper)
- `data/mentions.csv`, `data/sloan/papers.jsonl`
- `data/raw/**/README.md`, `LICENSES.md` only
- `docs/CHAPTER-MAP.md` (table spine only — see rules below)
- `docs/DATA-REPOS.md`, `NUMBERS-LANDSCAPE.md`, `open_datasets.csv`, `EVIDENCE.md`
- `docs/*-sources.md`, ownership `*_methodology.md` / `*_README.md` (not trends essays)
- `docs/CBA-LOOKUP.md`, `docs/cba-structure-pipeline.md` (operator docs for landed tools)
- `scripts/`, `src/`, `schemas/`, `tests/`, `ROADMAP.md`, `README.md`, `SCOPE.md`, `CONTRIBUTING.md`
- `pyproject.toml`, lockfiles, CI config

### Deny (do not add; migrate when touched)

- `docs/creative/**` — frozen; no new packs
- `data/derived/creative/**` — frozen; keep CSVs only if they are pure indexes, else move with prose
- New `docs/**/SPIKE*.md`, `PHASE*-REPORT*.md`, `PRODUCTIZATION*.md`, `*-FEASIBILITY*.md`
- `docs/**/hooks.md`, writer journey theatre, OPEN-THE-DESK style guides
- `**/STATUS*.md`, agent desk diaries under `data/derived/**` (fold one line into CHAPTER-MAP status or delete)
- Ownership `*_trends.md` stretch essays (keep methodology + CSV)
- `pocket_guide.md`-style vignette prose (structure JSON + short method is enough)
- Manuscript, Zotero DB/PDFs, proprietary tracking dumps, CBA PDF/fulltext

### Park locally (already gitignored)

- `local/**` — author/agent scratch, creative drafts, notebooks, spike diaries
- `data/raw/**` — downloads pending license check
- `.venv/`, secrets, sqlite dumps

## CHAPTER-MAP rules

`docs/CHAPTER-MAP.md` is a **spine**, not a lab notebook.

1. Append **at most one row** per new cite-backed artifact: `topic | path | cite | status`.
2. Status cells stay short (`ready`, `wanted`, `gap`, `partial`, `quotes_need_pdf`, plus a ≤ ~20-word hedge if needed).
3. **Never** append narrative, creative blurbs, motif essays, or Phase diary paragraphs to the Notes section.
4. Draft blockers (e.g. home-court rewrite, FIBA 450M year pin, unnamed studies) land as `data/studies/*.md` or a `wanted`/`gap` row — not as CHAPTER-MAP prose.
5. Do not invent binder paths. Prefer existing Scrivener paths from `data/mentions.csv` / ROADMAP.

## Scripts: `scripts/` vs local

| Land in `scripts/` or `src/hoops_data/` when… | Keep under `local/` when… |
|-----------------------------------------------|---------------------------|
| It regenerates a committed derived file | One-off scrape that wrote no redistributable table |
| Tests or CI will call it | Notebook / exploratory REPL |
| Schema is stable enough to name | Spike that will be thrown away |

`scripts/parse_cba_spike.py` is legacy; new spikes stay local until productized.

## Chosen enforcement posture (30 days)

**Hybrid of A + D, with C for overflow — not B as the primary lever.**

- **A (policy):** this file + `CONTRIBUTING.md` checklist. Reject out-of-scope PRs.
- **D (two-tier docs):** commit indexes/CSV spines; essays cite paths from Scrivener/`local/`.
- **C (move thinking):** new creative/process → `local/`; optional private sibling only if multi-machine sharing of drafts becomes painful (not default).
- **Not B first:** expanding gitignore over already-tracked creative paths does not untrack them and invites agents to “fix” by writing elsewhere. Prefer explicit deny + freeze; ignore only untracked scratch under `local/`.

## Migration (existing committed creative / process)

Do **not** rewrite git history. Prefer a follow-up PR after this freeze:

1. **Freeze now** — no new files under `docs/creative/` or `data/derived/creative/`; update indexes to say so.
2. **Inventory** — creative essays, spike/feasibility/productization reports, STATUS diaries, hooks, trends essays, pocket vignettes (see `CONTRIBUTING.md`).
3. **Keep history** — `git rm` from the tree (or move contents into `local/` on author machines) so main stays thin; history retains archaeology.
4. **Preserve spines** — keep motif/index CSVs only when they are pure pointers to landed derived rows; otherwise remove with the essay.
5. **CHAPTER-MAP** — drop or mark `hold` on CREATIVE rows; collapse Phase/P0 Notes into ROADMAP or delete.
6. **Private sibling** — only if Glen wants shared drafts across agents without public noise; otherwise `local/` is enough.

## Non-goals

- Do not propose rewriting the book in-repo.
- Do not weaken the Scrivener / Zotero split.
- Do not vendor raw NBA / tracking data or CBA fulltext.
