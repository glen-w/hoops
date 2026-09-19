# Hoops EuroLeague ownership & sales ledger (2026-09-19)

Writer-facing ledger of **EuroLeague club ownership structures and documented sales** for **Glen’s Hoops desk** — parallel to the NBA pack in [nba_README.md](nba_README.md).

**Landed** in `data/derived/teams/euroleague_current_ownership.csv`, `data/derived/teams/euroleague_ownership_events.csv`, and `data/derived/teams/euroleague_ownership_timeline_by_team.md`. Edit those, not a box copy.

**Built in:** `/workspace/hoops-euroleague-ownership-ledger-2026-09-19/`  
**Access / as-of:** 2026-09-19  
**Scope:** All 20 current EuroLeague clubs (2026-27 roster) — Anadolu Efes, ASVEL, Baskonia, Beşiktaş, Crvena zvezda, Dubai Basketball, Olimpia Milano, Barcelona, Bayern, Fenerbahçe, Hapoel Tel Aviv, Maccabi Tel Aviv, Olympiacos, Panathinaikos, Paris Basketball, Partizan, Real Madrid, Valencia, Virtus Bologna, Žalgiris.  
**Do not invent prices or owners.**

## Files
| File | Role |
|------|------|
| `current_ownership.csv` | **One row per club** — current structure + controlling entity |
| `ownership_events.csv` | Event-level ledger (sales, stakes, founding, association_control, …) |
| `ownership_timeline_by_team.md` | One short section per current EL club |
| `methodology.md` | Sources, association vs private, price hygiene, gaps |
| `trends.md` | Optional one-pager: PE / multi-club / Gulf entry (cited) |
| `README.md` | This file — land path |

## CSV schemas

### `current_ownership.csv`
`team_slug`, `team_name`, `country`, `structure`, `controlling_entity`, `buyer_structure_align`, `as_of`, `source_url`, `source_title`, `confidence`, `notes`

- `structure`: `association` \| `multi_sport_club` \| `private_company` \| `majority` \| `group` \| `public` \| `municipal` \| `unknown`

### `ownership_events.csv`
`event_id`, `team_slug`, `team_name`, `country`, `event_date`, `event_type`, `seller`, `buyer`, `buyer_structure`, `price_eur_reported`, `price_notes`, `source_url`, `source_title`, `confidence`, `notes`

- `event_type`: `sale` \| `majority_stake` \| `minority_stake` \| `founding` \| `rebrand` \| `takeover` \| `association_control` \| `other`
- Blank `price_eur_reported` = unconfirmed (**do not invent**)

## Landed
- **Current structures:** `data/derived/teams/euroleague_current_ownership.csv`
- **Events:** `data/derived/teams/euroleague_ownership_events.csv`
- **Timeline:** `data/derived/teams/euroleague_ownership_timeline_by_team.md`
- **Chapter map:** `docs/CHAPTER-MAP.md`, row `TEAMS / ownership — EuroLeague club structures & sales`

## Stats (this build)
- Current-structure rows: **20/20** (final thicken: Wikipedia sources cleared from `current_ownership.csv`)
- Event rows: **54** (count unchanged; sources thickened)
- Clubs with ≥1 event: **20/20**
- Confidence events: HIGH 43 / MEDIUM 11
- Wikipedia URLs in events CSV: **0** after final thicken
- Priced EUR rows: **2** (Milano Armani 2008; Virtus Zanetti←Gherardi 2025) — blanks intentional
- Pending (not closed control): ASVEL–Buss talks; Virtus sale listening; Maccabi ROFR dispute risk

## Maintenance
Follow `methodology.md`. Prefer club releases and reputable biz press; Wikipedia as lead then verify.
