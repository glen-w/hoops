# Coder Focus: 2026-10-24

## Completed
- Grokbot triage: 12/12 items (10 done, 2 partly done)
- CSVs migrated to analysis/: media_rights_deals.csv, sponsorship_inventory_2024-25.csv, arena_financing_post2010.csv
- nightshift_requests.json updated with 10 blockers/gaps

## Blockers Preventing Next Tier
1. **Paperful venv offline** (blocks 3 paper searches: revenue-sharing, team revenue, sponsorship valuation)
   - Path: /Users/89298/Documents/paperful/.venv/bin/paperful
   - Action: pip install paperful or restore venv

2. **Zotero mirror offline** (blocks 9 arena-financing keys validation)
   - Action: Retry zotero_search when mirror is online

3. **2024-25 media cycle scope decision** (affects MEDIA chapter depth)
   - Decision: defer, post-pub verify, or rely on pr.nba.com + press authority
   - Pending: Researcher editorial decision

4. **Glen editorial approvals**
   - Ponzo & Scoppa (I5AB7LWK): keep, remove, or refile?
   - shufinskiy (TFI7VXII): metadata gaps (creator, accessDate) approval

5. **hoops_record output path** (analysis/ → hoops/)
   - Blocks Vegas-Allegiant test
   - Action: Coordinate with rec server

## Actionable (Ready to Start)
- **Salary cap CSV**: compile from pr.nba.com PRs using 2026-09-20 methodology or check hoops/data/derived/
- **RSN consolidation**: archive has SBJ articles (Main Street Sports Group wind-down, DAZN expansion, YouTube hubs)

## Grounded Files (in _grokbot/2026-10-23/)
- MEDIA_grounded_2026-10-23.md: media rights timeline + deals + sponsorship inventory gaps
- STADIUM_grounded_2026-10-23.md: arena financing (post-2010) + gentrification (Barclays, Edmonton, Detroit, Sacramento)
- GAME_TIME_homeadvantage_refbias_2026-10-23.md: referee bias + home advantage (COVID natural experiment)

## Gaps Acknowledged
- Sponsorship inventory mid-season pickups (Hornets, Clippers, Spurs post-Oct 2024) not checked
- Arena financing Barclays public % ambiguous (PILOT treatment)
- Free-throw FTA pressure claim unsourced (need 1 paper)
