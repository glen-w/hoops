# Contributing to the hoops sidecar

Read [AGENTS.md](AGENTS.md) (short) and [SCOPE.md](SCOPE.md) (full). The repo is **public**. Citeable output lives under `data/derived/` / `data/studies/`. Creative and process live under committed **`author/`** so agents always see them.

## PR checklist (humans and agents)

Before opening a PR, confirm one of:

**Artifact PR**

- [ ] Diff lands or hardens a **cite-backed** derived table/JSON, a regenerable builder, a thin catalog row, or a short method note.
- [ ] No creative/process leaking into `docs/` or `data/derived/` (those belong in `author/`).
- [ ] Method notes are short (schema, sources, blanks, regenerate). No `/workspace/...` agent paths.
- [ ] CHAPTER-MAP: at most one 4-cell row; no Notes narrative; blockers go in `data/studies/`; never point at `author/`.
- [ ] No manuscript, Zotero DB/PDFs, `data/raw` dumps, CBA PDF/fulltext, proprietary tracking.
- [ ] Scripts in `scripts/` / `src/` only if they emit (or validate) a committed artifact; else `author/process/` or `local/`.
- [ ] PR title names the **artifact**.

**Creative / process PR**

- [ ] Diff touches only `author/**` (plus policy docs if needed).
- [ ] Does not reintroduce `docs/creative/` or `data/derived/creative/`.
- [ ] Does not add CHAPTER-MAP rows for author paths.
- [ ] PR title names the pack or process note, and makes clear it is author-workspace.

If an artifact PR’s citeable output is a story rather than a path under `data/derived/` or `data/studies/`, **do not open it** — put the story in `author/` instead.

## Agent PR rules

1. **Write where (artifacts):** tables → `data/derived/<product>/` (+ short `method.md`); hedges → `data/studies/<slug>.md`; map pointer → one CHAPTER-MAP row; builders → `scripts/` or `src/hoops_data/`.
2. **Write where (creative):** essays, motif indexes, sonnets, postcards, hooks, spike/phase diaries → `author/creative/` or `author/process/`. **Commit them.**
3. **Never append** narrative or Phase diaries to `docs/CHAPTER-MAP.md` Notes. Status cells ≤ ~20 words. Never map to `author/`.
4. **CHAPTER-MAP** is append-one-row-only for real artifacts. Do not invent Scrivener binder paths.
5. **Method note ceiling:** schema + sources + blanks + confidence + regenerate command.
6. **Scripts:** commit under `scripts/` / `src/` only if regenerable and tied to a committed artifact; exploratory scripts → `author/process/`.
7. **ROADMAP / mentions.csv** prioritize citeable artifacts; creative packs land under `author/`.
8. **Cite, don’t rehost** proprietary data. Prefer blanks and `GAP` over invented cells.
9. **Collision rule:** if another open PR owns a CSV spine, land a hedge note or wait.
10. **Reject path leakage:** markdown voice + motif tags under `docs/` or `data/derived/` → move to `author/` and close/refile.

## Author workspace

See [author/README.md](author/README.md). Baseline content was restored from the pre-v0.1 overnight branch into `author/` so cloud agents share the same creative tree. Gitignored `local/` remains for machine-only scratch only.
