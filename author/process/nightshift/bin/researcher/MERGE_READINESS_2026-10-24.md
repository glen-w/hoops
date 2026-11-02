# Merge Readiness Report (2026-10-24)

## Summary
Three chapters (MEDIA, FIN, STADIUM) are grounded and ready for manuscript integration. Four highest-priority research blockers remain unresolved locally and require external escalation for completion.

## Chapters Ready for Merge

### MEDIA (286 → ~3,500 words expanded)
**Status: Grounded, pending 2 blockers**

Expanded draft covers:
- US national broadcast packages (timeline 1990–2024, detailed)
- Regional sports network collapse (Diamond Sports, Main Street transition)
- International digital rights (Tencent, geopolitical fragility)
- Sponsorship (naming rights, patches, 17/30 deals undisclosed)
- Academic literature on TV demand, ratings, RSN economics (Crawford 2018, Foster 2014, Kunz 2017, etc.)
- League Pass blackout economics

**Blockers:**
1. **Causal studies: streaming tier demand and elasticity** (highest priority)
   - Amazon 2024 entry effects on local blackouts and League Pass substitution
   - Escalation: SBJ, Journal of Sports Economics, NBA research partnerships
2. **Tencent 2024 renewal value** (highest priority, undisclosed)
   - Affects international tier assessment
   - Escalation: SBJ paywalled, NBA investor relations, GlobalData

**Secondary gaps (high priority but not blocking):**
- Player/coach compensation tied to media exposure (no causal study found)
- International broadcast negotiations outside China (fragmented data)
- ESPN+/Peacock pricing and escalators (proprietary)
- YouTube local hub proposal (needs official confirmation)

### FIN (512 → ~4,000 words expanded)
**Status: Grounded, pending 1 blocker**

Expanded draft covers:
- Public vs. private arena financing (Chase Center, Intuit Dome, Golden 1, etc.)
- Subsidy literature (130+ studies, 2023 meta-analysis: venues ≠ growth)
- Arena neighborhoods and property values (Barclays, Staples, Oklahoma City, Golden 1)
- Maintenance costs and lifecycle liabilities
- Tax abatement mechanics and renewal risks
- Player salary feedback loops
- International comparators (Europe, Australia)

**Blocker:**
1. **Causal evidence of resident displacement** (highest priority)
   - Property-value studies abundant; displacement causality missing
   - Qualitative evidence (Edmonton Rogers Place) available but non-causal
   - Affects gentrification/displacement narrative in chapter
   - Escalation: urban economics journals, community studies researchers, sociology publishers

**Secondary gaps (high priority but not blocking):**
- Long-term maintenance costs and public liability (proprietary data)
- Intuit Dome post-opening Inglewood impacts (2024 data, too recent)
- Tax abatement renewal outcomes and municipal revenue gaps
- Economic link between arena financing and player compensation

### STADIUM (689 → ~4,500 words expanded)
**Status: Grounded, pending 1 blocker**

Expanded draft covers:
- Home-court advantage (58–60% win rate) and COVID natural experiment
- Fan effects mediated through player behavior (rebounding, intensity), not referee bias
- Crowd noise effects on judgment calls (soccer ≠ basketball)
- Arena as neighborhood anchor (property values, retail survival, displacement narratives)
- Interior experience (climate, seating, accessibility, bathrooms, sound, sightlines)
- Naming rights and corporate branding
- Food and concessions
- Historic arena afterlives (Seattle, Boston, San Antonio)
- London games and international expansion
- Post-9/11 security and safety protocols
- Logistics (court maintenance, scheduling, crowd management, parking)

**Blocker:**
1. **Technical fouls and home-team bias** (highest priority)
   - Do fans influence official judgment-call rates for techs specifically?
   - COVID data shows home advantage disappeared without crowds, but technical-foul rates unanalyzed
   - Blocks home-advantage section framing
   - Escalation: sports economics, academic researchers extending COVID natural experiment

**Secondary gaps (high priority but not blocking):**
- Arena design effects on injury rates and fan satisfaction (causal studies lacking)
- Concessions economics and labor conditions (proprietary)
- Disability access comparison across 30 arenas (systematic audit needed)
- Security costs and efficacy (post-9/11 protocol assessment missing)

## What Blocks Completion

### 4 Highest-Priority Blockers (Awaiting External Discovery)

1. **Streaming tier demand and blackout elasticity** (MEDIA)
   - Academic study or industry analysis showing Amazon 2024 substitution/complementarity effects
   - Status: Zotero 0 hits; no local library coverage
   - Escalation: SBJ ($), sports economics journals, NBA partnerships

2. **Tencent 2024 value** (MEDIA)
   - Official or credible industry estimate of October 2024 renewal amount
   - Status: Zotero 0 hits; deal is confidential
   - Escalation: SBJ paywalled ($), NBA investor filings, industry analysts

3. **Resident displacement causality** (FIN)
   - Causal identification (RDD, IV, matching) of NBA arena–driven displacement
   - Status: Zotero 0 hits; property-value studies available but no causal displacement evidence
   - Escalation: urban economics journals, community studies researchers

4. **Technical fouls and home-team bias** (STADIUM)
   - Quantitative analysis of technical-foul calling patterns with/without crowds
   - Status: Zotero 0 hits; COVID natural experiment not yet analyzed for techs
   - Escalation: sports economics researchers, academic publishers

## Current Constraints

1. **Paperful .venv offline**: Automated paperful_ask unavailable; manual escalation required to SBJ, publisher contacts
2. **Zotero local mirror**: 0 hits on all 4 highest-priority blockers; live Zotero search also empty
3. **No web-search for library papers**: Per factory rules, external discovery must go through credentials and publisher contacts, not generic web search
4. **gb.pend = 0**: No grokbot items pending; all items flagged in nightshift_requests.json for daytime triage

## Recommended Path Forward

### Immediate (Daytime Escalation)
1. **SBJ contacts**: Streaming tier demand, Tencent value, arena financing data
2. **Publisher outreach**: Journal editors for streaming, urban economics, sports management
3. **NBA investor relations**: Tencent renewal value, internal scheduling/viewership data
4. **Academic researchers**: Extend COVID natural experiment to technical fouls; displacement causality work

### Near-term (Next Research Cycle)
- Once blockers resolved or marked "proprietary/unavailable", integrate MEDIA/FIN/STADIUM into main manuscript
- Re-measure word counts across full manuscript post-merge
- Reconcile endnotes (38k w) with bibliography (464 w); flag missing/duplicate refs in Zotero

### If Blockers Cannot Be Resolved
- Mark as "proprietary/missing" in manuscript
- Reframe narrative around what can be safely said (e.g., "arena financing varies; displacement remains unmeasured")
- Proceed with chapter merge using grounded literature and flagged gaps

## Files Updated

- `hoops/nightshift_requests.json`: 25 items, 4 highest-priority, escalation paths specified
- `hoops/MERGE_READINESS_2026-10-24.md`: This file

## Next Steps

1. Daytime Grokbot: triage nightshift_requests.json and activate SBJ/publisher/NBA contact protocol
2. Once blockers resolved: integrate MEDIA/FIN/STADIUM into main manuscript (builder/coder scope)
3. Manuscript reconciliation: endnotes ↔ bibliography, missing/duplicate refs
