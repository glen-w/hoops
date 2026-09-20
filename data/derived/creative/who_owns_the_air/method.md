# Methodology: Who owns the air field notes

**Pack:** Creative overnight (2026-09-20)  
**Source constraint:** Cite-only from `data/derived/broadcast_ads/` artifacts (known_public_facts.csv, source_map.md, binder_schema.md)  
**Confidence rule:** HIGH for official partner/term disclosures; MEDIUM for contract totals/ad spend (secondary); GAP for rate cards/inventory

---

## Source hierarchy

1. **PRIMARY SURFACE:** `data/derived/broadcast_ads/known_public_facts.csv` (19 rows)  
   Access date: 2026-09-19  
   What it contains:
   - National media rights: partners, contract totals, per-team payouts
   - National ad sales estimates (vendor data: iSpot, Guideline via Sportico/MediaPost)
   - Gaps explicitly marked (local RSN rollup, inventory, sponsorship fee schedules)
   - All rows carry: `source_url`, `as_of`, `confidence`, `notes`

2. **SUPPORTING CONTEXT:**
   - `data/derived/broadcast_ads/source_map.md` — "Prose rule (do not blur)" table defining three streams
   - `data/derived/broadcast_ads/binder_schema.md` — Proposed table structures; inventory dictionary

3. **CONFIDENCE BANDS (from source CSV):**
   - **HIGH:** Official NBA Communications or NBA.com releases (partners, term, package structure)
   - **MEDIUM:** Secondary journalism (contract dollar totals, ad spend vendor estimates, per-team payouts)
   - **GAP:** Unknowable without private data (rate cards, inventory, local RSN fees, activation spend)

---

## The three streams: Why we separate them

From `source_map.md` prose rule:

| Stream | Who pays whom | What it is |
|--------|---------------|------------|
| **Media rights fees** | Networks/streamers → **NBA** | Contract price for game windows |
| **Ad sales / bookings** | Advertisers → **networks/streamers** | Monetization of airtime / impressions — **not** the rights fee |
| **Sponsorship rights fees** | Brands → **league / team** | Patches, naming rights, in-arena, digital, entitlements |

**Critical error to avoid:** Never write "the TV deal is a $X ad market." The rights fee (~$76–77B over 11 years) and ad sales (~$2.1B first season) are **parallel economies**, not additive.

The field notes guide treats streams 1 and 2 (rights fees and ad sales) with **national scope only**. Stream 3 (sponsorship) is noted (e.g., Amex, Kia, Emirates entitlements) but not quantified (fee schedules private). Local RSN fees (stream 1, local variant) are flagged as **GAP**.

---

## Facts ledger: What we cited and how

### Rights cycle 1 (2016–17 through 2024–25)

| Fact | Value | Confidence | Source |
|------|-------|-----------|--------|
| Partners | ABC/ESPN, TNT/Turner | HIGH | OFFICIAL NBA Communications 2014-10-06 |
| Contract total | ~$24B | MEDIUM | SECONDARY Sports Illustrated 2014-10-06 |
| Annual avg | "more than $2.6B" | MEDIUM | SECONDARY SI |
| Per-team payout (2024-25) | ~$103M | MEDIUM | SECONDARY Sportico |

**Why MEDIUM for totals?** Official NBA release confirms partners and term but **does not disclose package dollars**. We trust SI's $24B figure (no contradicting source) but label it SECONDARY per protocol.

### Rights cycle 2 (2025–26 through 2035–36)

| Fact | Value | Confidence | Source |
|------|-------|-----------|--------|
| Partners | ABC/ESPN, NBC/Peacock, Prime Video | HIGH | OFFICIAL NBA.com 2024-07-24 |
| Contract total (CNBC) | ~$77B | MEDIUM | SECONDARY CNBC 2024-07-24 |
| Contract total (Sportico) | ~$76B | MEDIUM | SECONDARY Sportico |
| Annual avg framing | ~$6.9B/yr | MEDIUM | DERIVED ($76B / 11) |
| Disney annual | ~$2.62B/yr | MEDIUM | SECONDARY CNBC "people familiar" |
| NBCU annual | ~$2.45B/yr | MEDIUM | SECONDARY CNBC "people familiar" |
| Amazon annual | ~$1.8B/yr | MEDIUM | SECONDARY CNBC "people familiar" |
| Per-team payout (2025-26) | ~$143M | MEDIUM | SECONDARY Sportico |

**Why two contract totals?** CNBC reports ~$77B; Sportico reports ~$76B. We **do not average** them. Both are MEDIUM-confidence secondary journalism. The guide notes both and flags the discrepancy.

**Why MEDIUM for partner splits?** CNBC cites "people familiar with the matter," not official NBA disclosure. Treat as informed reporting, not audited figures.

### Ad sales (advertiser → network spend)

| Fact | Value | Confidence | Source |
|------|-------|-----------|--------|
| Full season 2025-26 | ~$2.1B | MEDIUM | SECONDARY Sportico / Guideline data |
| Regular season 2025-26 | ~$760M | MEDIUM | SECONDARY MediaPost / iSpot.tv |

**Why two ad figures?** Different **windows** (full season vs regular season) and different **vendors** (Guideline vs iSpot). We **do not reconcile** them. The guide presents both and warns against arithmetic.

**Who gets this money?** Networks/streamers (ABC/ESPN, NBC, Amazon), **not the NBA**. This is parallel to rights fees, not additive.

### Sponsored moments (brand → league entitlements)

| Fact | Value | Confidence | Source |
|------|-------|-----------|--------|
| Partners (Amex, Kia, Emirates, etc.) | Named assets exist | HIGH | OFFICIAL NBA.com Partners hub |
| Fee schedules | GAP | GAP | Private; trade press snapshots (IEG) exclude media buys but not line-item invoices |

**What we can say:** Entitlements exist (tip-off, halftime, awards, patches). **What we cannot say:** How much brands pay. The guide flags this as **intentional opacity**.

---

## What we left blank (intentional gaps)

From the CSV and guide:

1. **Local RSN fees (leaguewide):** Team anecdotes exist in Sportico; no unified 30-team table. Sportico mentions ~10% of 2024-25 revenue, but this is **not** a cite-backed leaguewide rollup.

2. **Network P&L:** Do networks profit after paying rights fees and production costs? (Private financial data; not in earnings calls at game-level detail)

3. **Inventory architecture:** How many 30-second units per game? Unsold rates? Makegoods? (Network sales private)

4. **Activation spend:** How much do sponsors spend *executing* deals (e.g., Kia activating MVP award via marketing campaigns) vs the rights fee itself? (Private)

5. **BRI timing:** When do rights-fee dollars hit Basketball Related Income for salary cap calculations? (NBA-NBPA private; CBA language generic)

We **mark these as GAP** rather than invent. The field notes guide's thesis is that the air is **plural and opaque**—we map the fragments we can cite.

---

## Motif tagging: How we grouped facts

Each row in `facts_used.csv` carries a **motif** column to cluster related claims:

| Motif | Definition | Row count in facts_used.csv |
|-------|-----------|------------------------------|
| `rights_cycle_1` | 2016–25 Disney/Turner contracts | 3 |
| `rights_cycle_2` | 2025–36 Disney/NBCU/Amazon contracts | 4 |
| `partner_splits` | Per-partner annual fees (cycle 2) | 3 |
| `per_team_payout` | National TV revenue to teams | 2 |
| `ad_sales` | Advertiser spend estimates (vendor data) | 2 |
| `sponsored_moments` | Entitlements (Amex, Kia, Emirates) | 2 (existence + fee gap) |
| `local_media_gap` | Missing leaguewide RSN ledger | 1 |
| `inventory_gap` | Unknowable sellable units / splits | 2 |

**Purpose:** Motifs allow the guide to **narrative-cluster** facts (e.g., Section I on rights cycles; Section III on ad sales) while the CSV remains a flat ledger. Motifs are **analytical tags**, not data fields.

---

## The prose trap: Why "the TV deal is a $77B ad market" is wrong

### The error
Casual writing often **blurs or sums** rights fees and ad sales:
- Rights fees: ~$76–77B (11 years, NBA ← networks)
- Ad sales: ~$2.1B (one season, networks ← advertisers)
- **Incorrect:** "The TV deal generates ~$78–79B"

### Why it persists
1. Both involve "TV" and "money"
2. Rights fees are large and frequently quoted
3. Ad sales are large and frequently quoted
4. Writers assume they are **parts of one total**

### The correction
The NBA **receives** the rights fee (~$76–77B over 11 years).  
The networks **receive** ad revenue (~$2.1B in 2025-26, varying by season).  
The networks must **cover** rights fees, production, talent, and profit from ad sales + subscription revenue + other monetization.

These are **parallel economies**, not a single pot. The guide explains this in Section VIII ("The prose trap").

---

## Augmented inventory: The fourth stream (emerging)

From `source_map.md` and broader binder context:

**Augmented / AI in-broadcast ads:**  
- Genius Sports + local RSN platforms (2026 press)
- Virtual signage, data-triggered overlays
- Not traditional 30-second spots
- Existence confirmed (company press); inventory prices **GAP**

This is a **hybrid stream**:
- Monetizes broadcast image (like ad sales)
- Placed via league/team partnership deals (like sponsorship)
- Sold per impression or per game, not per 30-second unit

The guide notes this in Section VI ("The augmented layer") as **emerging** but does not quantify it (prices private). The field notes framing allows us to **name the phenomenon** without fabricating metrics.

---

## What we did NOT invent

### Dollar arithmetic
- We did **not** sum $76B rights + $2.1B ads = $78.1B
- We did **not** average CNBC $77B and Sportico $76B to get $76.5B
- We did **not** reconcile iSpot $760M (regular season) with Guideline $2.1B (full season) by subtraction

**Rule:** When two vendors or sources give different figures, **report both** and note the difference. Do not resolve it by math unless the source explains the relationship.

### Confidence inflation
- Official partner/term disclosures: **HIGH** (NBA Communications or NBA.com)
- Contract dollar totals: **MEDIUM** (secondary journalism, no audited trail)
- Ad spend estimates: **MEDIUM** (vendor data via trade press, not invoices)
- Rate cards / inventory: **GAP** (private)

We **did not** upgrade MEDIUM to HIGH because "it's widely reported." Consensus is not audit.

### Sponsorship fee schedules
- We cited **existence** of entitlements (Amex, Kia, Emirates) as HIGH (official Partners page)
- We marked **amounts** as GAP (no public rate cards)
- We did **not** scrape agency marketing pages quoting "$250k–$3M/season" LED ranges, per `source_map.md` instruction to **not treat as confirmed** without primary deal disclosure

---

## Reproducibility

To replicate the guide:

1. Read `data/derived/broadcast_ads/known_public_facts.csv` (19 rows)
2. Extract facts by category:
   - `national_media_rights_*` → rights cycles
   - `national_ad_*` → ad sales
   - `local_media_*` → local gaps
   - `*_inventory` → inventory gaps
3. Assign motif tags (defined above)
4. Populate `facts_used.csv` with columns: `motif`, `fact_id`, `season_or_period`, `category`, `value`, `unit`, `source_url`, `as_of`, `confidence`, `notes`
5. Write guide sections using motif clusters (e.g., Section I = `rights_cycle_1` + `rights_cycle_2`)

No additional web scraping or vendor data fetching was performed. All facts are from the upstream CSV (`known_public_facts.csv` accessed 2026-09-19).

---

## Confidence bands summary

| Data type | Confidence | Justification |
|-----------|-----------|---------------|
| Partners + term (official releases) | HIGH | NBA Communications / NBA.com; public, dated, authoritative |
| Contract totals (SI, CNBC, Sportico) | MEDIUM | Secondary journalism; no audit trail; consensus ≠ official |
| Per-team payouts (Sportico) | MEDIUM | "League declined to comment" in article; vendor projection |
| Ad spend (iSpot, Guideline) | MEDIUM | Measurement vendor estimates via trade press; not invoices |
| Partner splits (CNBC "people familiar") | MEDIUM | Informed reporting; not official disclosure |
| Entitlement existence (NBA.com Partners) | HIGH | Official Partners hub; public list |
| Entitlement fees | GAP | Private; IEG/SponsorUnited snapshots are summaries, not invoices |
| Local RSN fees (leaguewide) | GAP | Team anecdotes only; no unified table |
| Rate cards / inventory | GAP | Network private sales data |

**Blank preferred over invention.** The field notes guide's thesis is that **the air is opaque**. We cite what we can; we flag what we cannot.

---

**Compiled:** 2026-09-20  
**Reviewer:** Check against `data/derived/broadcast_ads/known_public_facts.csv` (19 rows) and `source_map.md` (three-streams table) for consistency. Verify that no dollar figures were summed across streams and that all GAP rows remain unfilled.
