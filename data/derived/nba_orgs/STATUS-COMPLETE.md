# NBA org charts — STATUS COMPLETE

**Access / as_of date:** 2026-09-19 (Europe/Paris)
**Infra path:** `data/derived/nba_orgs/{team_slug}.csv`
**Schema:** team,role,name,title,source_url,as_of,confidence
**role_vocab:** ownership, president, gm, basketball_ops, analytics, scouting, medical, business, coaching

## 30-team checklist

| Abbr | Team | Slug | Rows | Status | Notes |
|------|------|------|------|--------|-------|
| ATL | Atlanta Hawks | `atlanta-hawks` | 27 | DONE | teams/ATL.md |
| BOS | Boston Celtics | `boston-celtics` | 23 | DONE | teams/BOS.md |
| BKN | Brooklyn Nets | `brooklyn-nets` | 21 | DONE | teams/BKN.md |
| CHA | Charlotte Hornets | `charlotte-hornets` | 23 | DONE | teams/CHA.md |
| CHI | Chicago Bulls | `chicago-bulls` | 18 | DONE | teams/CHI.md |
| CLE | Cleveland Cavaliers | `cleveland-cavaliers` | 14 | DONE | teams/CLE.md |
| DET | Detroit Pistons | `detroit-pistons` | 21 | DONE | teams/DET.md |
| IND | Indiana Pacers | `indiana-pacers` | 41 | DONE | teams/IND.md |
| MIA | Miami Heat | `miami-heat` | 40 | DONE | teams/MIA.md |
| MIL | Milwaukee Bucks | `milwaukee-bucks` | 18 | DONE | teams/MIL.md |
| NYK | New York Knicks | `new-york-knicks` | 20 | DONE | teams/NYK.md |
| ORL | Orlando Magic | `orlando-magic` | 31 | DONE | teams/ORL.md |
| PHI | Philadelphia 76ers | `philadelphia-76ers` | 28 | DONE | teams/PHI.md |
| TOR | Toronto Raptors | `toronto-raptors` | 12 | DONE | teams/TOR.md |
| WAS | Washington Wizards | `washington-wizards` | 26 | DONE | teams/WAS.md |
| DAL | Dallas Mavericks | `dallas-mavericks` | 17 | DONE | teams/DAL.md |
| DEN | Denver Nuggets | `denver-nuggets` | 49 | DONE | teams/DEN.md |
| GSW | Golden State Warriors | `golden-state-warriors` | 21 | DONE | teams/GSW.md |
| HOU | Houston Rockets | `houston-rockets` | 19 | DONE | teams/HOU.md |
| LAC | LA Clippers | `la-clippers` | 21 | DONE | teams/LAC.md |
| LAL | Los Angeles Lakers | `los-angeles-lakers` | 20 | DONE | teams/LAL.md |
| MEM | Memphis Grizzlies | `memphis-grizzlies` | 17 | DONE | teams/MEM.md |
| MIN | Minnesota Timberwolves | `minnesota-timberwolves` | 18 | DONE | teams/MIN.md |
| NOP | New Orleans Pelicans | `new-orleans-pelicans` | 20 | DONE | teams/NOP.md |
| OKC | Oklahoma City Thunder | `oklahoma-city-thunder` | 19 | DONE | teams/OKC.md |
| PHX | Phoenix Suns | `phoenix-suns` | 19 | DONE | teams/PHX.md |
| POR | Portland Trail Blazers | `portland-trail-blazers` | 16 | DONE | teams/POR.md |
| SAC | Sacramento Kings | `sacramento-kings` | 19 | DONE | teams/SAC.md |
| SAS | San Antonio Spurs | `san-antonio-spurs` | 34 | DONE | teams/SAS.md |
| UTA | Utah Jazz | `utah-jazz` | 21 | DONE | teams/UTA.md |

**CSV row total (all complete teams):** 693

## This batch (11 teams finished 2026-09-19)

- **CHA** `charlotte-hornets.csv` — 23 rows; notes `teams/CHA.md`
- **DET** `detroit-pistons.csv` — 21 rows; notes `teams/DET.md`
- **DAL** `dallas-mavericks.csv` — 17 rows; notes `teams/DAL.md`
- **HOU** `houston-rockets.csv` — 19 rows; notes `teams/HOU.md`
- **LAC** `la-clippers.csv` — 21 rows; notes `teams/LAC.md`
- **LAL** `los-angeles-lakers.csv` — 20 rows; notes `teams/LAL.md`
- **MEM** `memphis-grizzlies.csv` — 17 rows; notes `teams/MEM.md`
- **MIN** `minnesota-timberwolves.csv` — 18 rows; notes `teams/MIN.md`
- **PHX** `phoenix-suns.csv` — 19 rows; notes `teams/PHX.md`
- **SAC** `sacramento-kings.csv` — 19 rows; notes `teams/SAC.md`
- **UTA** `utah-jazz.csv` — 21 rows; notes `teams/UTA.md`

## Source mix for sparse-official teams

- Official press / team FO pages when available
- Basketball-Reference executives (personnel executive of record)
- RealGM 2025-26 roster Front Office grids (medium confidence; verify high-stakes)
- NBAstuffer analytics department list
- Media guides (MIN 2025-26; DAL 2025 yearbook selective)

## Caveats

- DAL/LAC/LAL mid-cycle FO or ownership flux — titles snapshotted 2026-09-19
- Dual-title Pelinka: both `president` and `gm` rows
- No emails/phones; LinkedIn not required for this batch

