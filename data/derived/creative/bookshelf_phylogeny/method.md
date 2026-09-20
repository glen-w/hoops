# Methodology: Bookshelf phylogeny guide

**Pack:** Creative overnight (2026-09-20)  
**Source constraint:** Cite-only from `data/derived/books/comparable.csv` (+ comparable.md)  
**Confidence rule:** HIGH for Goodreads ratings (official site); GAP for most Amazon UK data (blocked/blank)

---

## Source hierarchy

1. **PRIMARY SURFACE:** `data/derived/books/comparable.csv` (19 rows)  
   Access date: 2026-09-19  
   What it contains:
   - Title, author, publisher, year, ISBN
   - Goodreads URL, rating, ratings count
   - Amazon UK search URL (most stars/prices GAP)
   - `lane` taxonomy: `narrative` | `analytics` | `how_to_watch` | `history` | `memoir`
   - `why_comparable` prose (how each book relates to desk)
   - `confidence` (all HIGH for Goodreads data)

2. **SUPPORTING CONTEXT:** `data/derived/books/comparable.md` (markdown table + selection notes)  
   Why books were selected; exclusions (youth novels); Amazon star gaps noted

3. **RATINGS CONFIDENCE:**
   - **Goodreads:** HIGH (official Goodreads.com pages accessed 2026-09-19; public ratings)
   - **Amazon UK stars:** GAP (most searches blocked or no live scrape; only *Thinking Basketball* had US Amazon.com snippet 4.7/294)
   - **Prices:** GAP or band ranges (no live Amazon UK prices in most rows; publisher/retailer snippets where noted)

---

## Phylogenetic framework: Why this metaphor?

### What is phylogeny?
In biology, phylogeny is the evolutionary history of a group of organisms—a **tree** showing common ancestors and divergent branches.

In this guide, we treat the **nineteen books** as species and ask:
- Which books are **ancestors** (foundational texts that later books cite or react to)?
- Which books are **descendants** (extending a method or voice)?
- Which books are **convergent** (arriving at similar niches via different paths)?
- Which books are **parallel** (occupying adjacent niches without direct descent)?

### Why "cladogram-in-prose"?
A cladogram is a branching diagram showing evolutionary relationships. We do not have formal citation counts (that would require mining bibliographies or acknowledgments), but we can infer relationships from:
- **Method:** analytics vs narrative vs memoir
- **Epistemology:** how the author *knows* (data, access, immersion, memory)
- **Marketing adjacency:** which books are explicitly compared in blurbs/reviews (e.g., Sprawlball name-checks FreeDarko)

The "prose" qualifier means we describe the tree **narratively** rather than diagramming it. The clusters table (`clusters.csv`) is the tabular skeleton.

---

## Cluster taxonomy: How we assigned clusters

Each book was assigned to a **primary cluster** based on:

1. **Method** (how the book generates knowledge)
   - Analytics (Oliver, Taylor, Partnow, Goldsberry)
   - Anecdote + ranking (Simmons, Serrano)
   - Oral history / reported access (Pearlman, Herring)
   - Embedded narrative (Halberstam, McCallum)
   - First-person memory (Bird/Magic, Phil Jackson)
   - Interdisciplinary watch-guide (Nick Greene)
   - Literary cultural essay (Abdurraqib, Axthelm)

2. **Epistemology** (what gives the author authority)
   - **Public data** → analytics lineage
   - **Insider access** → memoirs, FO reportage
   - **Participant-observer** → embedded narratives
   - **Fan-intellectual voice** → Simmons lineage
   - **Place + sociology** → cultural history

3. **Era and audience**
   - Pre-analytics (Halberstam, Axthelm)
   - Cable-era dynasty narratives (Showtime, Dream Team)
   - Analytics boom (Oliver → Taylor → Goldsberry)
   - Social media / YouTube era (FreeDarko, Serrano, Abdurraqib)

### Cluster definitions (as applied)

| Cluster | Definition | Example |
|---------|-----------|---------|
| `Simmons_lineage` | Fan-intellectual voice; anecdote + ranking; cultural references | Simmons, Serrano, Abdurraqib |
| `Oliver_lineage` | Four-factors / per-possession analytics; coach-facing to YouTube-adjacent | Oliver, Taylor, Partnow |
| `Visual_analytics` | Shot-chart spatial data; design-forward | Goldsberry |
| `Proto_analytics` | Pre-YouTube smart-fan aesthetic + early stats | FreeDarko |
| `Cross_sport_econ` | Behavioral econ across multiple sports | *Scorecasting* |
| `Dynasty_oral_history` | Reported access to players/coaches; many voices | Pearlman, McCallum (Dream Team), Strauss |
| `Team_era_deep_dive` | Single-team season or era; deep reporting | McCallum (Phoenix), Herring |
| `Rivalry_memoir` | First-person player/coach memory | Bird/Magic, Phil Jackson |
| `Embedded_narrative` | Season-long immersion; literary journalism | Halberstam |
| `Cultural_history` | Pre-analytics sociology and place | Axthelm |
| `Watch_guide_hybrid` | Interdisciplinary concepts for watching | Nick Greene |

### Why these clusters and not others?
We could have clustered by:
- **Year** (decades) — but that obscures method
- **Publisher** — not relevant to epistemology
- **Sales / popularity** — we lack sales data; Goodreads ratings are popularity proxies but not definitive

We chose **method + epistemology** because the guide's purpose is to show **how readers migrate between books**—not to rank them but to map the tree.

---

## What we did NOT invent

### Citation counts
We did **not** count how many times one book cites another in its bibliography or acknowledgments. We inferred relationships from:
- Blurbs and marketing (e.g., Sprawlball marketed to "Simmons and FreeDarko readers")
- Author backgrounds (e.g., Partnow as former Bucks executive → insider epistemology)
- Shared methods (e.g., Oliver → Taylor both use per-possession frameworks)

These are **reasonable inferences**, not formal citation analysis.

### Amazon ratings and prices
Most Amazon UK data is **GAP**. We did **not**:
- Fabricate Amazon stars when blank
- Average competing price bands
- Invent ISBNs (all ISBNs from Goodreads or publisher pages)

Only *Thinking Basketball* had a visible Amazon.com snippet (4.7 / 294), noted in CSV as US data.

### Literary quality rankings
The guide does **not** rank books by quality (e.g., "Halberstam is better written than Simmons"). It maps **relationships** and **epistemologies**. Goodreads ratings are included as popularity proxies, not editorial judgments.

---

## Evolutionary pressures: Analytical framework

The guide proposes three **constraints** shaping the tree:

### 1. Access (epistemological)
- **Insider access** → memoirs, FO reportage (Phil Jackson, Strauss, Partnow)
- **Public data** → analytics (Oliver, Taylor, Goldsberry)
- **Embedded journalism** → season chronicles (Halberstam, McCallum)
- **No special access** → fan-intellectual voice (Simmons, Serrano)

### 2. Era (temporal)
- **Pre-TV era** → localism (Axthelm on NYC playgrounds)
- **Cable era** → dynasty narratives (Showtime, Dream Team)
- **Analytics era** → stats-driven (Oliver, Taylor, Goldsberry)
- **Social media era** → hybrid (FreeDarko, Serrano, Abdurraqib)

### 3. Audience (market)
- **Coach/GM** → dense analytics (Oliver, Partnow)
- **Smart-fan** → accessible analytics (Taylor, Goldsberry)
- **General reader** → narrative (Simmons, Halberstam)
- **Literary reader** → cultural/memoir (Abdurraqib, Axthelm)

These are **analytical lenses**, not deterministic laws. Books can span multiple audiences (e.g., Goldsberry marketed to both analytics and Simmons readers).

---

## Missing branches: Intentional exclusions

The `comparable.csv` ledger excludes:

1. **Youth fiction** (e.g., Walters' *Triple Threat*) — off-desk per comparable.md notes
2. **Academic monographs** — too dense for smart-fan desk
3. **Coaching textbooks** (X's and O's) — practitioner niche
4. **International basketball** (e.g., EuroLeague histories) — US-centric desk
5. **Player ghostwritten autobiographies** — different epistemology (not literary; promotional)

These are **boundary conditions** of the comparable desk, not oversights. The phylogeny is a **North American smart-fan tree**, not a global or academic one.

---

## Reproducibility

To replicate the clusters:

1. Read `data/derived/books/comparable.csv` (19 rows)
2. Extract: `title`, `author`, `year`, `lane`, `goodreads_rating`, `goodreads_ratings_count`, `why_comparable`
3. Assign each book to a cluster based on:
   - Method (from `why_comparable` prose)
   - Epistemology (inferred from author role: player, coach, journalist, analyst, fan)
   - Marketing adjacency (from `why_comparable`: e.g., "Sprawlball marketed to Simmons/FreeDarko readers")
4. Populate `clusters.csv` with columns: `cluster_name`, `title`, `author`, `year`, `lane`, `goodreads_rating`, `goodreads_count`, `method`, `epistemology`, `notes`

No additional web scraping or citation mining was performed. All cluster assignments are **interpretive** based on the existing CSV prose.

---

## Confidence bands

| Data type | Confidence | Justification |
|-----------|-----------|---------------|
| Goodreads ratings (value + count) | HIGH | Official Goodreads.com pages; public data; accessed 2026-09-19 |
| Amazon UK stars | GAP | Most blocked or blank; only *Thinking Basketball* US snippet captured |
| Amazon UK prices | GAP or band | Publisher/retailer snippets where noted; no live scrape |
| ISBNs | HIGH | From Goodreads or publisher pages; no fabrication |
| `lane` taxonomy | HIGH | Assigned in upstream comparable.csv with justification in `why_comparable` |
| Cluster assignments | MEDIUM | Interpretive; based on method/epistemology; no formal citation counts |

**Why MEDIUM for clusters?** Because we inferred relationships (e.g., "Oliver → Taylor lineage") without counting bibliography citations. The assignments are **reasonable** and **reproducible** from the CSV prose, but not falsifiable via formal network analysis.

---

## Blank fields in clusters.csv

We left **no fields blank** in `clusters.csv` because all columns are derived from existing CSV data or interpretive notes. However, we acknowledge:

- **Price data:** mostly GAP in source CSV (not in clusters.csv)
- **Amazon stars:** mostly GAP in source CSV (not in clusters.csv)
- **Citation counts:** never attempted (would require bibliography mining)

The clusters table is a **derived synthesis**, not a data fetch. Its "blankness" is in the *absence of formal citation analysis*, which we flag as a limitation.

---

**Compiled:** 2026-09-20  
**Reviewer:** Check against `data/derived/books/comparable.csv` (19 rows) for consistency. Verify that no Goodreads ratings were fabricated and that cluster assignments align with `why_comparable` prose.
