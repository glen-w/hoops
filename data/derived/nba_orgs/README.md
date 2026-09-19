# NBA front-office / basketball-ops org charts — source playbook

**As of:** 2026-09-19 (Europe/Paris)  
**Purpose:** Sidecar research for Glen Wright’s Hoops book repo (`glen-w/hoops`).  
**Infra deliverable:** flat CSV at `data/derived/nba_orgs/{team_slug}.csv`.

---

## Locked CSV schema (Infra)

Exact columns (order matters):

| column | meaning |
|--------|---------|
| `team` | Full franchise name (e.g. `San Antonio Spurs`) |
| `role` | Controlled vocab (below) |
| `name` | Person’s display name as published |
| `title` | Role title string as published (do not invent) |
| `source_url` | Canonical public URL for the claim; LinkedIn profile URL only when that is the source (no scrape dumps) |
| `as_of` | ISO date `YYYY-MM-DD` for the snapshot |
| `confidence` | `high` \| `medium` \| `low` |

### `role` vocabulary

`ownership` · `president` · `gm` · `basketball_ops` · `analytics` · `scouting` · `medical` · `business` · `coaching`

Map liberally when titles span departments; prefer the **primary** function. Example: “VP Ticket Strategy, Analytics & Operations” → `business` (commercial analytics), not basketball `analytics`.

### `confidence` guidance

| value | use when |
|-------|----------|
| `high` | Official team/NBA.com staff or leadership page, or BBRef executive-of-record |
| `medium` | Credible secondary (NBAstuffer, RealGM, press release) or official title ambiguous |
| `low` | Crowdsourced / stale / single uncorroborated mention |

**Path pattern:** `data/derived/nba_orgs/{team_slug}.csv`  
**Slugs:** kebab-case full names (`san-antonio-spurs`, `denver-nuggets`, `philadelphia-76ers`, `boston-celtics`, …).

Optional sidecars (not required by Infra): `teams/{team_slug}.jsonl`, `teams/{abbr}.md` research notes.

---

## Source hierarchy (best → supporting)

### 1. OFFICIAL — team site / NBA.com staff & leadership pages

**What it covers:** Ownership, C-suite, basketball ops, scouting, medical, sometimes business + analytics. Best single source when present.

**Examples (verified HTTP 200 on 2026-09-19):**

| Team | URL | Notes |
|------|-----|-------|
| Spurs | https://www.nba.com/spurs/leadership | Executive leadership; FO + some basketball ops |
| Nuggets | https://www.nba.com/nuggets/staff | Dense basketball staff directory |
| 76ers | https://www.nba.com/sixers/team/staff-directory | Full ownership + basketball + business |
| Hawks | https://www.nba.com/hawks/staff-directory | Staff directory |
| Bulls | https://www.nba.com/bulls/chicago-bulls-staff-directory | Staff directory |
| Knicks | https://www.nba.com/knicks/front-office | Front office (JS-heavy) |
| Wizards | https://www.nba.com/wizards/staff-directory | Staff directory |
| Nets | https://www.nba.com/nets/front-office | Front office |
| Pelicans | https://www.nba.com/pelicans/staff | Staff listing |
| Thunder | https://www.nba.com/thunder/frontoffice | Basketball ops bios (JS-heavy) |
| Blazers | https://www.nba.com/blazers/frontoffice | Front office (JS-heavy) |

**Freshness caveats:** Pages can lag press releases by days–weeks; mid-season title changes common. Many team sites are SPA/JS — curl may see empty shells; use browser or search snippets as discovery, then cite the official URL.

**License / redistribution:** NBA.com and team sites are proprietary. Fair-use extraction of **names + public titles** for research/book sidecar is the intent; do **not** republish full page HTML, media-guide PDFs wholesale, or contact directories (phones/emails). Prefer link-out citations.

### 2. OFFICIAL — press releases / team news

**What:** Hire/fire/promotion announcements (President, GM, AGM, analytics leads).  
**Use:** Override stale directory rows; set `as_of` to release date when more recent than directory scrape.  
**Cite:** Exact release URL.

### 3. SECONDARY — Basketball-Reference executives

- Directory: https://www.basketball-reference.com/executives/  
- Per team: `https://www.basketball-reference.com/teams/{ABBR}/executives.html`

**Covers:** Historical **personnel executive of record** (usually GM), not full org charts.  
**Freshness:** Good for succession timelines (e.g. PHI Morey → Myers interim → Gansey).  
**License:** Sports Reference terms — cite + link; don’t bulk-mirror tables.

### 4. SECONDARY — NBAstuffer analytics-department list

- https://www.nbastuffer.com/analytics101/nba-teams-that-have-analytics-department/

**Covers:** Team-by-team basketball analytics / strategy / data science roles; crowd + LinkedIn/X + media-guide maintenance since ~2009.  
**Freshness:** Uneven; per-row “Last Updated” dates. Cross-check against official directories when both exist.  
**License:** Cite NBAstuffer; do not scrape LinkedIn via their workflow — use their published table as secondary only.

### 5. SECONDARY — RealGM staff grids

- Pattern: `https://basketball.realgm.com/nba/teams/{Name}/{id}/staff-members/Current/grid`

**Covers:** Broad FO/coaching/medical trees; often richer than official pages.  
**Caveat:** Crowdsourced; verify high-stakes rows against OFFICIAL.  
**License:** Cite RealGM; no bulk dump of their DB.

### 6. SECONDARY — Spotrac / Capology

**Primarily:** Contracts and cap — **not** org charts. Useful only for confirming exec names tied to transactions, not for building FO trees.

### 7. LINKEDIN — public profiles / company pages

**Allowed:** Manual lookup; put **public profile or company page URL** in `source_url` when that is the evidence; title in `title`.  
**Disallowed:** Bulk crawl, email/phone harvest, private data, ToS-violating scraping. Note LinkedIn ToS in notes when used.

### 8. Media guides / PDFs

Often the richest OFFICIAL snapshot (e.g. Warriors historical media guides). Prefer current season PDF from team site CDN; cite PDF URL + page. Do not redistribute the PDF in the sidecar repo.

---

## Recommended deep-dive order (by public data richness)

1. **Done (templates):** SAS, DEN, PHI  
2. **Next (rich official pages):** WAS, NOP, ATL, CHI, NYK, OKC, POR, BKN  
3. **Medium (press + RealGM + NBAstuffer):** IND (Fieldhouse PDF), GSW (media guide), MIL, MIA, TOR, BOS  
4. **Sparse official web:** CLE, DET, CHA, ORL, HOU, DAL, MEM, MIN, LAL, LAC, PHX, SAC, UTA  

East/West can be interleaved; prefer richness over conference order.

---

## Ethics / compliance

- Public pages only.  
- No bulk LinkedIn crawl; no emails/phones in CSV.  
- LinkedIn = URL in `source_url` when used, never scrape dumps.  
- Prefer OFFICIAL over SECONDARY when they conflict; note conflicts in team `.md` notes.  
- UK/EU researcher: respect robots.txt where practical; rate-limit; no credentialed access.

---

## How to extend a team

1. Open `00-TEAMS-INDEX.json`, set `status` → `in_progress`.  
2. Fetch official staff URL (or record `null` and use SECONDARY).  
3. Write `data/derived/nba_orgs/{team_slug}.csv` with locked columns.  
4. Optional: `teams/{team_slug}.md` notes + `.jsonl` mirror.  
5. Set `status` → `complete`, add `csv` path on the team object.

---

## Sources cited in this playbook build (access date 2026-09-19)

| Type | Title | URL |
|------|-------|-----|
| OFFICIAL | Executive Leadership \| San Antonio Spurs | https://www.nba.com/spurs/leadership |
| OFFICIAL | Staff Directory \| Denver Nuggets | https://www.nba.com/nuggets/staff |
| OFFICIAL | Staff Directory \| Philadelphia 76ers | https://www.nba.com/sixers/team/staff-directory |
| OFFICIAL | Front Office \| New York Knicks | https://www.nba.com/knicks/front-office |
| OFFICIAL | Staff Directory \| Washington Wizards | https://www.nba.com/wizards/staff-directory |
| OFFICIAL | Staff Directory \| Atlanta Hawks | https://www.nba.com/hawks/staff-directory |
| OFFICIAL | Chicago Bulls Staff Directory | https://www.nba.com/bulls/chicago-bulls-staff-directory |
| OFFICIAL | Basketball Operations \| Oklahoma City Thunder | https://www.nba.com/thunder/frontoffice |
| OFFICIAL | Staff Listing \| New Orleans Pelicans | https://www.nba.com/pelicans/staff |
| OFFICIAL | Front Office \| Brooklyn Nets | https://www.nba.com/nets/front-office |
| OFFICIAL | Portland Trail Blazers Front Office | https://www.nba.com/blazers/frontoffice |
| SECONDARY | NBA Analytics Departments: Team-by-Team Staff List \| NBAstuffer | https://www.nbastuffer.com/analytics101/nba-teams-that-have-analytics-department/ |
| SECONDARY | NBA & ABA Executives Directory \| Basketball-Reference | https://www.basketball-reference.com/executives/ |
| SECONDARY | Philadelphia 76ers Executives \| Basketball-Reference | https://www.basketball-reference.com/teams/PHI/executives.html |
| SECONDARY | RealGM NBA Staff Members | https://basketball.realgm.com/nba/staff-members |
