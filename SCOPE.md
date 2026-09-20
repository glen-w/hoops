# Sidecar scope

**Audience:** humans and agents opening PRs against `glen-w/hoops`.  
**Default:** the repo stays **public**. Citeable surface is artifacts under `data/derived/` / `data/studies/`. Creative and process live in committed **`author/`** so every clone and cloud agent sees them. One repo; no private sibling.

This repo is the **public data sidecar** for *Hoops: An Uncommon Field Guide to the Game of Basketball*. Prose lives in Scrivener. Citations live in Zotero `hoops`. Public framing lives on [glenwright.earth/projects/hoops](https://glenwright.earth/projects/hoops/). Do not rewrite the book here.

## Channel paste (verdict)

**Citeable (artifacts):** redistributable derived CSVs/JSON, short method notes beside them, thin catalogs (`mentions.csv`, CHAPTER-MAP spine, source maps), regenerable `scripts/` / `src/`, schemas, tests.  
**Committed author workspace:** speculative essays, creative packs, motif indexes, spike diaries, agent status writeups, hooks/voice drafts → `author/creative/`, `author/derived-creative/`, `author/process/`.  
**Still ignored:** `local/**` (machine scratch), `data/raw/**` dumps, manuscript, Zotero, proprietary tracking.  
**PR rule of thumb:** artifact PRs must add or harden a cite-backed path (or a one-line CHAPTER-MAP / ROADMAP pointer). Creative-only PRs may touch only `author/**`.

## Architecture (locked — do not re-litigate)

| Layer | Where |
|-------|--------|
| Manuscript prose | Scrivener (`.scriv` — never commit) |
| Citations / PDFs | Zotero `hoops` (+ Paperful for missing PDFs) |
| Public framing / blurb | glenwright.earth project page |
| Sidecar artifacts | Derived tables, builders, catalogs, short method notes |
| Author/agent creative + process | `author/` (committed) — not citeable |
| Machine-only scratch | `local/` (gitignored) |

## In vs out

| Commit as artifact (citeable) | Commit under `author/` (not citeable) | Do not commit |
|-------------------------------|----------------------------------------|---------------|
| Redistributable derived tables + license/provenance | Speculative essays, creative packs, voice drafts | Manuscript, Zotero DB/PDFs |
| Regenerable scripts that emit those tables | Motif CSVs, pocket guides, sonnets, postcards | `data/raw/**` dumps, CBA PDF/fulltext |
| Thin catalogs (`mentions.csv`, CHAPTER-MAP rows, source maps) | Spike diaries, phase reports, hooks | Proprietary tracking dumps |
| One short method note per derived product | Exploratory scripts that emit no artifact | |
| Draft **blockers / hedges** as `data/studies/*.md` | | Narrative appends to CHAPTER-MAP Notes |

### Method note vs “showing the working”

A method note stays in-scope when it answers, in roughly **≤ ~100 lines**: source class, schema, blank rules, confidence, how to regenerate.  
Long brainstorms, motif essays, and process theatre belong under `author/`, not beside the table as if they were methodology.

**Good pattern:** `data/derived/salary_cap_apron/methodology.md`.  
**Author pattern:** `author/creative/…`, `author/process/…`.

### Creative / motifs

Creative packs and motif indexes are committed under `author/` ([author/README.md](author/README.md)). Field-guide prose still ships via Scrivener and the site. Do not reintroduce `docs/creative/` or `data/derived/creative/` as product paths. CHAPTER-MAP never points at `author/`.

## Path allowlist / denylist

### Allow (commit)

- `data/derived/**/*.csv`, `*.json` (redistributable products)
- `data/derived/**/method.md` | `methodology.md` | `SOURCE.md` | `README.md` (short)
- `data/cba/<edition>/derived/*.json` + `metadata.json` / hashes (no agreement text)
- `data/reference/**`, `data/studies/*.md` (one short note per cited claim/paper)
- `data/mentions.csv`, `data/sloan/papers.jsonl`
- `data/raw/**/README.md`, `LICENSES.md` only
- `docs/CHAPTER-MAP.md` (table spine only)
- `docs/DATA-REPOS.md`, `NUMBERS-LANDSCAPE.md`, `open_datasets.csv`, `EVIDENCE.md`
- `docs/*-sources.md`, ownership `*_methodology.md` / `*_README.md` (not trends essays under `docs/`)
- `docs/CBA-LOOKUP.md`, `docs/cba-structure-pipeline.md`, `docs/cba/COMPARE-*.md`
- `docs/colour/`, `docs/teams/` — short methodology for landed colour/name artifacts
- `author/**` — creative packs, motifs, process (not citeable)
- `scripts/`, `src/`, `schemas/`, `tests/`, `ROADMAP.md`, `README.md`, `SCOPE.md`, `CONTRIBUTING.md`, `AGENTS.md`
- `pyproject.toml`, lockfiles, CI config

### Deny (wrong paths — use `author/` instead)

- `docs/creative/**`, `data/derived/creative/**`
- Motif / vignette indexes, pocket guides, sonnets, postcards **outside** `author/`
- `docs/**/SPIKE*.md`, `PHASE*-REPORT*.md`, `PRODUCTIZATION*.md`, `*-FEASIBILITY*.md`
- `docs/**/hooks.md`, writer-journey theatre under `docs/`
- `**/STATUS*.md` under `data/derived/**`
- Ownership `*_trends.md` stretch essays under `docs/ownership/`
- Manuscript, Zotero DB/PDFs, proprietary tracking dumps, CBA PDF/fulltext

### Machine scratch (gitignored)

- `local/**` — secrets, huge dumps, throwaway REPL only

## CHAPTER-MAP rules

1. Append **at most one row** per new cite-backed artifact: `topic | path | cite | status`.
2. Status cells stay short (`ready`, `wanted`, `gap`, `partial`, `quotes_need_pdf`, plus ≤ ~20-word hedge).
3. **Never** append narrative, creative blurbs, or Phase diary paragraphs to Notes.
4. Draft blockers land as `data/studies/*.md` or a `wanted`/`gap` row.
5. Do not invent binder paths. Prefer `data/mentions.csv` / ROADMAP.
6. **Never** point CHAPTER-MAP at `author/**`.

## Scripts: `scripts/` vs `author/` vs `local/`

| Land in `scripts/` or `src/hoops_data/` when… | Keep under `author/process/` when… | Keep under `local/` when… |
|-----------------------------------------------|------------------------------------|---------------------------|
| It regenerates a committed derived file | Exploratory / spike script worth sharing with agents | Secrets, huge dumps, throwaway REPL |
| Tests or CI will call it | Notebook-adjacent process | |
| Schema is stable enough to name | | |

## Enforcement posture

**One public repo:** artifacts + committed `author/` workspace; cite boundary enforced by PR checklist and CHAPTER-MAP rules. No private sibling required for agent access.

## Non-goals

- Do not propose rewriting the book in-repo.
- Do not weaken the Scrivener / Zotero split.
- Do not vendor raw NBA / tracking data or CBA fulltext.
