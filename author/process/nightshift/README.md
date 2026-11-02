# Nightshift → Hoops process workspace

Basketball research from the factory. Citeable derived tables still belong under
`data/derived/`; this tree is **author/process** (not citeable).

Triage 2026-11-01: **27** keepers; 2026-11-02 pass: **58** keepers (126 → 58 after factory Nov 1–2). Rest in `bin/cards/`. See [TRIAGE.md](TRIAGE.md).
Week plan 1–7 Nov: [WEEK-2026-11-01.md](WEEK-2026-11-01.md) (factory loads `prompts/days/YYYY-MM-DD.md` each night).

## Layout

| Path | What |
|------|------|
| `researcher/cards/` | Keepers only (120–250w review cards) |
| `researcher/HOOPS_SHELF.md` | Index of keepers |
| `researcher/notes/` | Sourced MEDIA / FIN / STADIUM drafts, free-throw pressure, Kinrade |
| `researcher/_grokbot/` | Daytime source drops |
| `coder/analysis/` | CSVs with real rows + citation registry |
| `builder/misc/` | Court-dimension notes |
| `bin/` | Everything triaged out (not deleted) |
| `hoops_status.md` | Manuscript hole report |

Machine-only bib: `local/nightshift/hoops_data/` (gitignored).

Factory sandboxes still symlink here (`sandbox/researcher/hoops` → `researcher/`).
New cards should add a *new* hole, not another Nielsen/regional-TV/Detroit–Orlando paraphrase.
