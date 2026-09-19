# Ghost franchises — creative pack (2026-09-20)

**Box path:** `/workspace/hoops-ghost-franchises-2026-09-20/`  
**Repo target:** `glen-w/hoops`  
**Access date:** 2026-09-20 (Europe/Paris)

## What this is
A **creative, cite-backed** TEAMS desk pack: short literary vignettes about NBA (and EuroLeague) ownership *afterimages* — cities that keep a nickname, charters that change letterhead, leagues that vanish while four clubs keep the receipt, member associations that are not American “franchises.”

Accompanying motif CSV indexes each vignette to ledger `event_id`s for writers who need the spine without rereading the essay.

## What this is not
- **Not** a new ownership ledger and **not** a substitute for `ownership_events.csv` / EuroLeague ownership CSVs.
- **Not** invented history. Voice and structure may be imaginative; **prices, owners, dates, and events are never invented.** Every factual claim must already appear in the source ledgers (or their attached public cites).
- **Not** BOG/legal records. Pending deals flagged in source ledgers stay pending.

## Sources (prefer HIGH confidence)
- `/workspace/hoops-ownership-ledgers-PR-pack-2026-09-19/` (land layout)
- `/workspace/hoops-nba-ownership-ledger-2026-09-19/`
- `/workspace/hoops-euroleague-ownership-ledger-2026-09-19/`

## Pack contents
| Path | Role |
|------|------|
| `essays/ghost-franchises.md` | 7 vignettes → land as `docs/creative/ghost-franchises.md` |
| `data/derived/teams/ghost_franchise_motifs.csv` | Motif index (tags + event_ids + hooks) |
| `CHAPTER-MAP-append.md` | One append row for TEAMS / ghost franchises creative |
| `PR-BODY.md` | Draft PR title/body for cloud agent (do not open PR from this box alone unless asked) |
| `README.md` | This file |

## Motif CSV schema
`motif_id,team_abbr,event_ids,motif_tags,one_line_hook,source_url,confidence`

## Vignette titles
1. The Sound That Left Town (Sonics→OKC)
2. Four Cities Under One Net (Nets migrancy)
3. Purple-and-Gold Inheritance (Lakers sales chain)
4. Four Survivors Walk Into the League (ABA→NBA 1976)
5. The Hawks Who Never Nested (ATL itinerancy)
6. The Name That Split in Two (CHA/NOP history split)
7. Clubs Without Franchises (EuroLeague association / multi-sport control)

## Cloud agent
Copy essay → `docs/creative/ghost-franchises.md`; copy motif CSV under `data/derived/teams/`; append CHAPTER-MAP row; open PR with `PR-BODY.md`. Do not invent thicken.
