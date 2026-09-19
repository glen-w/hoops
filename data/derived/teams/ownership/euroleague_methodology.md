# Methodology — EuroLeague club ownership & sales ledger
**Product:** Glen’s Hoops desk — writer-facing ownership ledger (EuroLeague parallel to NBA pack)  
**Access date:** 2026-09-19  
**Output root:** `/workspace/hoops-euroleague-ownership-ledger-2026-09-19/`  
**Constraint:** Box only — no git PR. **Do not invent prices or owners.**

## Purpose
Chronological ledger of how **current EuroLeague (2026-27)** clubs are controlled: documented private sales / takeovers / stake changes **and** association / multi-sport-club control where there is no market “sale.” Structures are first-class (`current_ownership.csv`), not only transaction rows.

## Preferred sources (in order)
1. **Club official sites / releases** — ownership-structure pages, anniversary founding notes, president statements (e.g. Hapoel ownershipstructure, Paris Basketball, Dubai About, Olympiacos presidents, Anadolu Efes club history, Bayern GmbH notices).
2. **Euroleague.net / ECA communications** — licence / roster confirmations (ownership rarely priced here; useful for as-of roster).
3. **Reputable business / sports-business press** — Les Echos, Il Giorno, Corriere, Marca/2Playbook, Ynet/Globes/Ctech, Eurohoops, BasketNews, Sportando, The Athletic, AP.
4. **Wikipedia** — **lead / navigation only**. Every price and control claim must be verified against #1–#3 before HIGH confidence. If only Wikipedia supports a figure, mark MEDIUM/LOW and note GAP.

## Two products, one desk
| File | Role |
|------|------|
| `current_ownership.csv` | **One row per current EL club** — how control works *now* |
| `ownership_events.csv` | Chronological events (sales, stakes, founding, association_control, etc.) |

### `current_ownership.csv` — `structure` vocab
`association` | `multi_sport_club` | `private_company` | `majority` | `group` | `public` | `municipal` | `unknown`

Pick the **primary** control pattern writers need:
- **association / multi_sport_club** — member-owned or sports-society parent (Real Madrid, Barça, Bayern e.V., Fener SK, Beşiktaş JK, Efes SK, Partizan/Zvezda SD). Basketball is a section/member club, not a freestanding franchise auction.
- **majority / private_company** — one controlling private owner or SAD/KAE/GmbH (Parker/ASVEL, Querejeta/Baskonia, Armani/Milano, Zanetti/Virtus, Angelopoulos/Olympiacos KAE, Giannakopoulos/PAO KAE, Roig/Valencia, Al Naboodah/Dubai, Motiejūnas/Žalgiris).
- **group** — multi-shareholder private (Paris; Hapoel Yannay Sport partners; Maccabi shareholder company).
- **municipal / public** — only when city/state holds equity (rare in this EL set; Kaunas supports Žalgiris ecosystem but is **not** listed as equity owner).
- **unknown** — leave when unclear; never invent.

Also store `buyer_structure_align` using the events vocab (`sole|majority|group|public|municipal|association|unknown`) for join consistency with NBA pack thinking.

### `ownership_events.csv` — column rules
| Field | Rule |
|-------|------|
| `event_date` | ISO `YYYY-MM-DD` when known; else `YYYY-MM` or `YYYY`. |
| `event_type` | `sale` \| `majority_stake` \| `minority_stake` \| `founding` \| `rebrand` \| `takeover` \| `association_control` \| `other` |
| `buyer_structure` | `sole` \| `majority` \| `group` \| `public` \| `municipal` \| `association` \| `unknown` |
| `price_eur_reported` | Integer EUR string when a widely reported **euro** figure exists. **Never invent.** Leave blank + explain in `price_notes`. USD-only deals (e.g. Maccabi ~$50M) stay blank in EUR with USD in notes — do not invent FX. |
| `confidence` | `HIGH` = official or multi-outlet corroboration; `MEDIUM` = strong press with stake/date ambiguity; `LOW` = roundup-only / weakly sourced. |
| `source_url` / `source_title` | Required on every row. |

## Association-owned vs private sales (writer rule)
**Do not invent “sales” for:**
- Real Madrid, FC Barcelona, FC Bayern (e.V. → Basketball GmbH), Fenerbahçe SK, Beşiktaş JK, Anadolu Efes SK, JSD Partizan, SD Crvena zvezda.

Use `association_control` / `founding` / structure rows instead. Sponsorship naming (Beko, Meridianbet, Mozzart Bet, Playtika, IBI, etc.) is **not** ownership.

**Do document private sales / stake changes for:**
- Virtus (Zanetti path; Gherardi buyback ~€5.8M), Olimpia Milano (Armani 2008 ~€4.09M), ASVEL (Parker 2014; Buss talks PENDING), Paris (2018 founding; Omar Sy 2025), Baskonia (Querejeta 1988+ SAD), Valencia (Roig/Forvasa), Hapoel (Yannay 2023; 2025 group), Maccabi (Recanati 2026 ~$50M stake), Žalgiris (Motiejūnas/Tesonet), Olympiacos/PAO KAEs (Angelopoulos / Giannakopoulos), Dubai founding.

## Greek / Serbian nuance
- **Olympiacos / Panathinaikos:** Multi-sport **brand** (CFP / PAO) but professional basketball is a **private KAE** with named controlling owners. Structure = `majority`, notes explain multi-sport parent.
- **Partizan / Zvezda:** Sports-society member clubs — institutional/association, heavy public-sport funding historically; not PE franchise sales.

## Pending (do not treat as closed control)
- **ASVEL:** Parker ↔ Buss brothers group talks (Aug 2026 press); valuation chatter €60–80M is **not** a closed price.
- **Virtus:** Zanetti open to serious offers; no closed successor deal as of access date.
- **Maccabi:** Post-Recanati ROFR/arbitration press — flag dispute risk.

## Coverage priorities (this build)
1. Current structure for **all 20** 2026-27 EL clubs.
2. Documented private sales / takeovers / stake changes.
3. Association_control anchors for multi-sport corps.
4. Blank prices when not public (intentional).
5. Optional `trends.md` — cited only.

## Final thicken (2026-09-19)
Wikipedia leads on events + current_ownership replaced with club official / El País / AS / JSD Partizan / KK Crvena zvezda / Virtus.it / Žalgiris.lt / Olympiacos BC / Hapoel BC / Fenerbahçe.org / Real Madrid / Barça where findable. Valencia Roig controlling-stake date corrected to **1986** (AS). Beşiktaş Basketbol A.Ş. still MEDIUM pending Turkish registry %. **Still do not invent prices or owners.**

## Known gaps
- Pre-2000 European club purchase prices sparse; many founding/association rows blank by design.
- Valencia Roig first-controlling-stake now cited **1986** (AS); Forvasa % from 2026 ACB roundup — deepen vs corporate filings on refresh.
- Panathinaikos 1987 Giannakopoulos entry date MEDIUM; exact equity instrument GAP.
- Maccabi early-2000s privatization package cash GAP.
- Žalgiris Tesonet 2022 cash confidential (BasketNews estimates exist — not entered as fact).
- Beşiktaş Basketbol A.Ş. share % vs JK — MEDIUM pending Turkish registry refresh.
- Armani succession vehicle after Giorgio Armani’s 2025 death — confirm Fondazione/group path on refresh.
- EuroLeague licence fees (Dubai etc.) are not club-sale prices.

## Refresh cadence
Re-pull after closed control changes (ASVEL if Buss closes; Virtus if sold; Maccabi ROFR resolution); bump folder date or append `event_id`s without rewriting history.
