# Ownership enrichment — methodology

**Desk:** glen-w/hoops teams  
**Access / as_of:** 2026-09-19 (Europe/Paris)  
**Scope this pack:** NBA 30 + WNBA 12 (pre-2025 expansion core). EuroLeague deferred (see below).  
**Locked `ownership_structure` vocab:** `sole` | `majority` | `group` | `public` | `municipal` | `unknown`

No invented owners, emails, or colours. Prefer leaving `unknown` / blank over guessing.

## Decision order (per team)

1. **Official / primary filings or closing PRs** when a recent transfer is in play (example: Connecticut Sun → Fertitta family, Mohegan closing PR 2026-05-14).
2. **Team front-office / staff directory / media guide** when they name Owner, Governor, Chairman, or Managing Partner.
3. **Wikipedia *List of NBA team owners*** (table scrape 2026-09-19) for controlling name + reported stake % when present.
4. **Team Wikipedia infobox “Owner(s)”** for WNBA when no better FO page was fetched under rate limits.
5. **Cross-check** against the same-day org-chart pack at `/workspace/hoops-nba-org-charts/` (`role=ownership` rows). Conflicts are called out in `notes` and usually drop confidence to MEDIUM.
6. **Wikidata P127** was attempted via SPARQL on access date; the query endpoint returned empty/non-JSON under timeout. Do **not** treat missing P127 as evidence of no owner — leave structure unknown only when *public* controlling identity is unclear, not because Wikidata is empty.
7. **Forbes valuation lists** (NBA 2025; WNBA 2026) are useful for owner *names* but often list multiple principals without stake math. Used as secondary confirmation only; never sole basis for `sole` vs `majority`.

## Mapping rules → `ownership_structure`

| Value | Use when |
|-------|----------|
| `sole` | One person/family clearly owns essentially the whole club (e.g. Ballmer ~99%, Fertitta Rockets/Sun, Gores, Pera, Benson). |
| `majority` | Named controlling owner with cited majority stake **or** unambiguous controlling/governor role with a cite (Ressler, Chisholm, Walter, Ishbia, Edens, etc.). |
| `group` | Co-equal chairs, GP/LP syndicates, or corporate partnerships without a single public majority individual (Plotkin & Schnall; Harris & Blitzer; Lore & Rodriguez; MLSE; Force 10 Hoops LLC; Dream partners). |
| `public` | Parent is a publicly traded sportsco (Knicks → Madison Square Garden Sports Corp., NYSE:MSGS). Dolan family voting control does **not** change `public`. |
| `municipal` | City, state, or tribal government / gaming authority is the owner. **None in this pack as of 2026-09-19** after the Sun left Mohegan. |
| `unknown` | Controlling owner or stake class not attested in sources above. Prefer this over inventing `majority`. |

### Confidence

- **HIGH** — controlling owner named consistently in official FO page, closing PR, or Wikipedia List with stake/role language.
- **MEDIUM** — controlling role clear but (a) equity % conflicting/sub-50% controlling (Warriors), (b) named individual differs across reputable sources (Nuggets Ann Walton Kroenke vs E. Stanley Kroenke on team staff), or (c) WNBA group principal inferred from infobox without stake split (Sky, Wings).
- **LOW** — not used in this pack; would mean thin secondary press only.
- Never mark HIGH/MEDIUM for structure if the public record only says “ownership group” with no controlling name — use `unknown`.

## Notable judgements

- **Knicks (`public`):** MSG Sports is the parent; James L. Dolan is governor/CEO. Structure is `public`, not `sole`.
- **Raptors (`group`):** Maple Leaf Sports & Entertainment (Rogers ~75% / Tanenbaum ~25% per Wikipedia List). Tanenbaum is governor; entity is still `group` (MLSE pattern called out in the brief).
- **Connecticut Sun:** Mohegan closing PR (2026-05-14) supersedes Wikipedia infobox that still listed Mohegan Tribe on access day. Owner = Tilman J. Fertitta; structure = `sole` (no longer `municipal`). Team plays out 2026 in Connecticut; Houston relocation planned 2027.
- **Lakers:** Mark Walter majority; Jeanie Buss remains governor/CEO as of access date — both facts kept in notes.
- **Celtics:** William Chisholm majority tranche closed 2025; Grousbeck role retained as CEO/alternate — structure `majority`.
- **Trail Blazers:** Tom Dundon majority from 2026 (Allen Trust sale).
- **Warriors:** Lacob is governor/controlling; Wikipedia List ~25% equity → `majority` with **MEDIUM** (control clear, block size not classic >50%).

## When to leave unknown

- No cite for who holds control (not merely who is on a long LP list).
- Conflicting sale status (announced but not closed / not BOG-approved) without a closing source on as_of.
- EuroLeague / EuroLeague Women clubs (multi-jurisdiction corporate webs; Wikidata P127 sparse) — **out of this pack**.

## EuroLeague (optional)

Not included. Club holding companies change sponsors/labels season to season; reliable English controlling-owner cites are uneven. Recommend a follow-up pass: Wikidata P127 + club imprint pages + Euroleague Basketball club profiles, club-by-club, with default `unknown`.

## Non-goals

- No hex colours, emails, phone numbers, or private cap-table inventing.
- No fair-use logo work.
- Expansion WNBA clubs beyond the core 12 (Valkyries, Fire, Tempo, etc.) deferred; Valkyries ownership is Warriors-aligned (Lacob/Guber) if a later patch is needed.
