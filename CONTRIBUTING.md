# Contributing to the hoops sidecar

Read [SCOPE.md](SCOPE.md) first. This repo holds **artifacts**, not thinking.

## PR checklist (humans and agents)

Before opening a PR, confirm:

- [ ] Diff lands or hardens a **cite-backed** derived table/JSON, a regenerable builder, a thin catalog row, or a short method note — not an essay.
- [ ] No new files under `docs/creative/` or `data/derived/creative/`.
- [ ] No spike / phase / productization / feasibility / hooks / STATUS diaries.
- [ ] Method notes are short (schema, sources, blanks, regenerate). No `/workspace/...` agent paths.
- [ ] CHAPTER-MAP: at most one 4-cell row; no Notes narrative; blockers go in `data/studies/` or status cells.
- [ ] No manuscript, Zotero DB/PDFs, `data/raw` dumps, CBA PDF/fulltext, proprietary tracking.
- [ ] Scripts in `scripts/` / `src/` only if they emit (or validate) a committed artifact; else `local/`.
- [ ] PR title names the **artifact** (e.g. “Add salary cap history CSV”), not a creative motif.

If the answer to “what can a writer cite from this PR?” is a story rather than a path under `data/derived/` or `data/studies/`, **do not open the PR**.

## Agent PR rules (copy into agent briefs)

1. **Write where:** new tables → `data/derived/<product>/` (+ short `method.md`); claim hedges → `data/studies/<slug>.md`; map pointer → one CHAPTER-MAP row; builders → `scripts/` or `src/hoops_data/`.
2. **Never write:** `docs/creative/**`, `data/derived/creative/**`, voice essays, sonnets, postcards, pilgrimage/phylogeny guides, motif prose.
3. **Never append** narrative, motifs, or Phase diaries to `docs/CHAPTER-MAP.md` Notes. Status cells ≤ ~20 words.
4. **CHAPTER-MAP** is append-one-row-only for real artifacts. Do not invent Scrivener binder paths.
5. **Method note ceiling:** schema + sources + blanks + confidence + regenerate command. If you are explaining how the agent thought, stop — that stays in the PR body or `local/`.
6. **Scripts:** commit only if regenerable and tied to a committed output. Exploration notebooks and one-off scrapes stay in `local/`.
7. **ROADMAP / mentions.csv** are truth for writing-support priorities; do not invent competing “overnight packs.”
8. **Cite, don’t rehost** proprietary or licensed raw data. Prefer blanks and `GAP` over invented cells.
9. **Collision rule:** if another open PR already owns a CSV spine, land a hedge note or wait — do not open a parallel creative pack on the same spine.
10. **Reject yourself:** if the PR is mostly markdown voice with a CSV of motif tags, close it without opening.

## Migration inventory (follow-up PR; do not rewrite history)

| Path | Class | Suggested action |
|------|--------|------------------|
| `docs/creative/**` | creative/thinking | Freeze; later `git rm` (keep history) or copy to `local/creative/` |
| `data/derived/creative/**` | creative/thinking | Same; keep pure index CSVs only if useful without guides |
| `data/derived/cba_defined_terms_pocket/pocket_guide.md` | creative | Remove vignettes; keep `motif_tags.csv` + short `method.md` if needed |
| `docs/cba/SPIKE*.md`, `PRODUCTIZATION-SUMMARY.md`, `CBA-PARSER-FEASIBILITY-*.md` | agent/process | Remove from tree; operator truth stays in `CBA-LOOKUP.md` + `cba-structure-pipeline.md` |
| `docs/PHASE0-REPORT-*.md` | agent/process | Remove; hedges live in `data/studies/` |
| `docs/average/hooks.md`, ownership `*_trends.md` | creative/thinking | Remove or move to `local/` |
| `data/derived/teams/STATUS*.md`, `NOTES.md`, `nba_orgs/STATUS-COMPLETE.md` | agent/process | Collapse into CHAPTER-MAP status / teams README; delete diaries |
| `docs/ZOTERO-LLM-PLAN.md` | other / parked plan | Hold or move to `local/`; not a sidecar artifact |
| Team derivative CSVs (`relocation_*`, `mascot_*`, `abbr_*`) | artifact | **Keep** if regenerable via `scripts/generate_team_derivatives.py` |
| Average desk CSVs under `data/derived/average/` | artifact | **Keep** tables + short methodology; drop hooks |

## Worst offenders (current tree)

These are the loudest examples of out-of-scope content already on `main` — use them as anti-patterns, not templates:

- `docs/creative/` (sonnets, ghost franchises, postcards, overnight essays)
- `data/derived/creative/*/guide.md` (pilgrimage / phylogeny / “who owns the air”)
- `docs/cba/SPIKE-REPORT.md`, `docs/PHASE0-REPORT-2026-09-19.md`
- `data/derived/cba_defined_terms_pocket/pocket_guide.md`
- CHAPTER-MAP **Notes** Phase/P0 diary blocks and CREATIVE status blurbs
