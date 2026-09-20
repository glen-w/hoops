# Hoops NBA ownership & sales ledger (2026-09-19)

Writer-facing chronological ledger of NBA franchise ownership changes for **Glen’s Hoops desk**.

**Landed** in `data/derived/teams/ownership_events.csv` and `data/derived/teams/ownership_timeline_by_team.md`. Edit those, not a box copy. There is no second copy of this note under `data/derived/teams/ownership/`.

**Built in:** `/workspace/hoops-nba-ownership-ledger-2026-09-19/`  
**Access / as-of:** 2026-09-19  
**Scope:** All 30 current NBA franchises; 2000–2026 sales plus thickened pre-2000 / 20th-century founding, early sales, and multi-city ownership paths.

## Files
| File | Role |
|------|------|
| `ownership_events.csv` | Event-level ledger (one row per ownership/structure event) |
| `ownership_timeline_by_team.md` | One short section per franchise: current owner + key prior sales |
| `methodology.md` | Source preference, vocab, price hygiene, gaps |
| `nba_methodology.md` | Source rules and confidence bands |
| `README.md` | This file — land path + CHAPTER-MAP note |

## CSV schema (`ownership_events.csv`)
`event_id`, `team_abbr`, `team_name`, `event_date`, `event_type`, `seller`, `buyer`, `buyer_structure`, `price_usd_reported`, `price_notes`, `source_url`, `source_title`, `confidence`, `notes`

- `event_type`: `sale` \| `majority_stake` \| `minority_stake` \| `relocation` \| `rebrand` \| `expansion` \| `bankruptcy` \| `other`
- `buyer_structure`: `sole` \| `majority` \| `group` \| `public` \| `municipal` \| `unknown`
- `confidence`: `HIGH` \| `MEDIUM` \| `LOW`
- Blank `price_usd_reported` = unconfirmed (**do not invent**); see `price_notes` / GAP language.

## Landed
- **Events:** `data/derived/teams/ownership_events.csv`
- **Timeline:** `data/derived/teams/ownership_timeline_by_team.md`
- **Chapter map:** `docs/CHAPTER-MAP.md`, row `TEAMS / ownership — NBA franchise sales & control`

## Pending deals (do not treat as closed control)
- **LAL:** Mark Walter → Josh Kushner & Bob Iger group (~$12.5B reported) — announced 2026-08-12; BOG pending as of access date.
- **MIN:** Marc Lore → Marc Stad controlling stake (~$4.5B valuation) — announced 2026-08-21; BOG pending as of access date.

## Stats (this build)
- Event rows: **158** (final thicken: +1 net — POR-1972 Sarkowsky majority; Weinberg row re-dated to POR-1976-majority)
- Pre-2000 dated rows: **104**
- Teams: 30/30 with at least one event
- Priced rows: **105** / blank price: **53** (blanks intentional — no invented figures)
- Confidence: HIGH 134 / MEDIUM 23 / LOW 1
- Wikipedia-led MEDIUM rows: **0** after final thicken (was several)
- Expansion fees: **21/21** rows now have a cited fee (incl. BAA $10k charter fees)

## Maintenance
Follow `methodology.md`. Prefer official NBA/team releases, then Forbes/Sportico/Athletic/Bloomberg/WSJ/ESPN; Wikipedia as lead then verify.
