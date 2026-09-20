# Contributing to the hoops sidecar

Read [SCOPE.md](SCOPE.md) first. Public git holds **artifacts**, not thinking. Creative and motif indexes live under gitignored `local/` (one repo).

## PR checklist (humans and agents)

Before opening a PR, confirm:

- [ ] Diff lands or hardens a **cite-backed** derived table/JSON, a regenerable builder, a thin catalog row, or a short method note — not an essay.
- [ ] No `docs/creative/`, `data/derived/creative/`, motif CSVs, pocket guides, or voice packs.
- [ ] No spike / phase / productization / feasibility / hooks / STATUS diaries.
- [ ] Method notes are short (schema, sources, blanks, regenerate). No `/workspace/...` agent paths.
- [ ] CHAPTER-MAP: at most one 4-cell row; no Notes narrative; blockers go in `data/studies/`.
- [ ] No manuscript, Zotero DB/PDFs, `data/raw` dumps, CBA PDF/fulltext, proprietary tracking.
- [ ] Scripts in `scripts/` / `src/` only if they emit (or validate) a committed artifact; else `local/`.
- [ ] PR title names the **artifact**, not a creative motif.

If the answer to “what can a writer cite from this PR?” is a story rather than a path under `data/derived/` or `data/studies/`, **do not open the PR**.

## Agent PR rules

1. **Write where:** tables → `data/derived/<product>/` (+ short `method.md`); hedges → `data/studies/<slug>.md`; map pointer → one CHAPTER-MAP row; builders → `scripts/` or `src/hoops_data/`.
2. **Never commit:** creative packs, motif indexes, sonnets, postcards, hooks, spike/phase diaries — use `local/` instead.
3. **Never append** narrative or Phase diaries to `docs/CHAPTER-MAP.md` Notes. Status cells ≤ ~20 words.
4. **CHAPTER-MAP** is append-one-row-only for real artifacts. Do not invent Scrivener binder paths.
5. **Method note ceiling:** schema + sources + blanks + confidence + regenerate command.
6. **Scripts:** commit only if regenerable and tied to a committed output.
7. **ROADMAP / mentions.csv** are writing-support priorities; do not invent overnight creative packs.
8. **Cite, don’t rehost** proprietary data. Prefer blanks and `GAP` over invented cells.
9. **Collision rule:** if another open PR owns a CSV spine, land a hedge note or wait.
10. **Reject yourself:** markdown voice + motif tags → close without opening.

## Local archive

When creative/process was removed from the public tree, copies were placed under `local/archive/` on author machines (gitignored). That folder is not part of the sidecar contract.
