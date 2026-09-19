# Chapter Map

This file maps Scrivener binder paths to data sources, research notes, and status tracking. 

**Rules:**
- **APPEND ONLY** — never replace existing rows
- All 30 NBA organizations must be preserved
- Status values: `source_map`, `wanted`, `linked`, `partial`, `missing`, `hold`

## Format

`binder_path,kind,target,status,note`

---

## NBA Organizations (30 teams)

binder_path,kind,target,status,note
"nba_orgs/atlanta-hawks",org_profile,,wanted,Atlanta Hawks
"nba_orgs/boston-celtics",org_profile,,wanted,Boston Celtics
"nba_orgs/brooklyn-nets",org_profile,,wanted,Brooklyn Nets
"nba_orgs/charlotte-hornets",org_profile,,wanted,Charlotte Hornets
"nba_orgs/chicago-bulls",org_profile,,wanted,Chicago Bulls
"nba_orgs/cleveland-cavaliers",org_profile,,wanted,Cleveland Cavaliers
"nba_orgs/dallas-mavericks",org_profile,,wanted,Dallas Mavericks
"nba_orgs/denver-nuggets",org_profile,,wanted,Denver Nuggets
"nba_orgs/detroit-pistons",org_profile,,wanted,Detroit Pistons
"nba_orgs/golden-state-warriors",org_profile,,wanted,Golden State Warriors
"nba_orgs/houston-rockets",org_profile,,wanted,Houston Rockets
"nba_orgs/indiana-pacers",org_profile,,wanted,Indiana Pacers
"nba_orgs/la-clippers",org_profile,,wanted,LA Clippers
"nba_orgs/la-lakers",org_profile,,wanted,LA Lakers
"nba_orgs/memphis-grizzlies",org_profile,,wanted,Memphis Grizzlies
"nba_orgs/miami-heat",org_profile,,wanted,Miami Heat
"nba_orgs/milwaukee-bucks",org_profile,,wanted,Milwaukee Bucks
"nba_orgs/minnesota-timberwolves",org_profile,,wanted,Minnesota Timberwolves
"nba_orgs/new-orleans-pelicans",org_profile,,wanted,New Orleans Pelicans
"nba_orgs/new-york-knicks",org_profile,,wanted,New York Knicks
"nba_orgs/oklahoma-city-thunder",org_profile,,wanted,Oklahoma City Thunder
"nba_orgs/orlando-magic",org_profile,,wanted,Orlando Magic
"nba_orgs/philadelphia-76ers",org_profile,,wanted,Philadelphia 76ers
"nba_orgs/phoenix-suns",org_profile,,wanted,Phoenix Suns
"nba_orgs/portland-trail-blazers",org_profile,,wanted,Portland Trail Blazers
"nba_orgs/sacramento-kings",org_profile,,wanted,Sacramento Kings
"nba_orgs/san-antonio-spurs",org_profile,,wanted,San Antonio Spurs
"nba_orgs/toronto-raptors",org_profile,,wanted,Toronto Raptors
"nba_orgs/utah-jazz",org_profile,,wanted,Utah Jazz
"nba_orgs/washington-wizards",org_profile,,wanted,Washington Wizards

## Source Notes & Research

binder_path,kind,target,status,note
"LEAGUE/efficiency",source_note,docs/franchise-efficiency-sources.md,source_map,"Forbes 2016 valuation + DEA efficiency literature; UNCONFIRMED: Forbes '22 Apr 2016' Blazers/Celtics attribution not verified - treat as UNCONFIRMED until original clipping/URL supplied"
"LEAGUE/income",source_note,docs/league-income-sources.md,source_map,League revenue ingredients - national media rights + local + gate + sponsorship + CBA BRI definitions
"BROADCAST/ads",source_note,docs/broadcast-ads-sources.md,source_map,Distinction between media rights fees (NBA income) and ad sales (network income); sponsor inventory schema
"LEAGUE/income/schema",design_note,docs/SCHEMA-sketch.md,wanted,Proposed CSV schemas for franchise valuations and league income components
"eng/cba-parser",feasibility,docs/CBA-PARSER-FEASIBILITY-2026-09-19.md,wanted,Engineering scaffold for CBA clause parser - research reference
