# Basketball Tracking & Analytics Software

Catalog of dedicated commercial tracking and analytics systems used in professional basketball. This document provides context for citing vendor platforms in the *Hoops* field guide, not instructions for acquiring proprietary data.

## Purpose

This is a **citation guide for book authors**, not a data acquisition manual. Each entry describes:
- What the system does and what data it produces
- NBA/league adoption timeline and current status
- Open vs. closed/proprietary access model
- How to cite it appropriately in scholarly or trade publishing
- Public secondary sources (press releases, conference papers, league announcements)

**⚠️ OUT OF SCOPE FOR THIS REPOSITORY:** No proprietary tracking dumps, no API access to paywalled systems, no scraped Second Spectrum/SportVU files, no betting feeds. Per the ROADMAP: "cite, don't rehost."

---

## Quick Reference Table

| Vendor/System | Data Type | Typical Access | NBA/League Use | Book-Safe Citation |
|---------------|-----------|----------------|----------------|-------------------|
| **SportVU (STATS LLC)** | Optical tracking (XY coordinates, 25 FPS) | Proprietary (discontinued) | NBA 2013–2017 | Primary: NBA press releases, SSAC papers that *discuss* tracking; Secondary: academic papers using archived SportVU |
| **Hawk-Eye (Sony)** | Optical tracking (pose/multi-point 3D, ~14 cameras, 60 FPS) | Proprietary | NBA 2023–present (optical capture) | Primary: Sports Business Journal (2023-03-09), The Guardian (2023-10-20); cite as current NBA optical provider |
| **Second Spectrum (Genius Sports)** | AI-derived analytics, broadcast augmentation | Proprietary (NBA partner) | NBA 2017–2023 (optical + analytics); 2023–present (analytics engine only) | Primary: NBA.com/stats tracking page, Second Spectrum white papers, Genius Sports partnership announcements; Secondary: SSAC papers |
| **Synergy Sports** | Video tagging, play-type classification (uses Hawk-Eye optical inputs as of 2023) | Subscription service | NBA teams, NCAA, FIBA | Primary: Synergy Sports Technology website, SBJ (2023-10-27) on Hawk-Eye integration; cite as "commercial scouting platform" |
| **Stats Perform (formerly Opta)** | Event tagging, advanced stats | Proprietary/Subscription | European leagues, some international | Primary: Stats Perform press releases; cite when discussing international basketball analytics |
| **Sportradar** | Live data feeds, odds, video tagging (uses Hawk-Eye optical inputs as of 2023) | Proprietary API | NBA data partner (betting, media) | Primary: NBA-Sportradar partnership announcements, SBJ (2023-10-27); cite for betting/media context, not raw feeds |
| **ShotTracker** | Sensor-based tracking (wearables + arena) | Proprietary (team/venue contracts) | NBA G-League, NCAA programs | Primary: ShotTracker case studies, NCAA partnership announcements |
| **Catapult** | Wearable GPS/IMU sensors | Proprietary (subscription) | Training/practice (not NBA games) | Primary: Catapult Sports press releases, team training staff interviews |
| **Kinexon** | Ultra-wideband (UWB) tracking | Proprietary (venue installation) | FIBA, European leagues, some NBA practice facilities | Primary: Kinexon press releases, FIBA partnership announcements |
| **FIBA LiveStats** | Manual event tagging (official stats) | Public (summary stats) | FIBA tournaments | Primary: FIBA.basketball official stats pages; free but limited detail |

---

## Optical Tracking Systems (Player/Ball XY Coordinates)

### SportVU (STATS LLC)

**Provider:** STATS LLC (acquired by Vista Equity Partners in 2014; SportVU basketball operations wound down post-2017)  
**Technology:** Six fixed cameras per arena, tracking player and ball positions at 25 frames per second  
**Data produced:**
- X, Y coordinates for all 10 players and the ball
- Derived metrics: player speed, distance traveled, touches, passes, defensive matchups
- ~1 million data points per game (often cited in media)

**NBA adoption timeline:**
- **2009–2010:** Pilot installations (Dallas Mavericks, Houston Rockets)
- **2013–2014:** League-wide rollout to all 30 arenas
- **2013–2017:** Official NBA tracking provider
- **2017:** NBA transitions to Second Spectrum; STATS focuses on other sports and non-tracking products

**Access model:**
- **Proprietary:** Never publicly released; available only to NBA teams and league office
- **NBA.com/stats:** Select derived metrics (player speed, touches, etc.) published on official NBA stats portal but not raw XY data

**Book-safe citation:**
- **Primary sources:**
  - NBA press releases (2013 league-wide announcement, 2017 transition to Second Spectrum)
  - STATS LLC white papers and case studies (if available via company archive)
  - NBA.com/stats tracking pages (cite specific metrics like "player speed" or "touches")
- **Secondary sources:**
  - Academic papers: Many SSAC papers from 2013–2018 reference SportVU data (e.g., "Deconstructing the Rebound with Optical Tracking Data," "CourtVision: New Visual and Spatial Analytics")
  - Trade press: ESPN, The Athletic, Sports Illustrated articles discussing the "tracking era"
- **Citation format:** "SportVU optical tracking system (STATS LLC, NBA partnership 2013–2017)"

**Public secondary sources:**
- NBA.com/stats tracking dashboard (derived metrics only): https://www.nba.com/stats/players/speed-distance
- SSAC conference papers (see SLOAN-ARCHIVE.md for papers using tracking data)
- Grantland/ESPN articles by Zach Lowe and Kirk Goldsberry (2013–2016 era)

---

### Second Spectrum (Genius Sports)

**Provider:** Second Spectrum (acquired by Genius Sports in 2021)  
**Technology:** Machine learning and AI-derived analytics engine (processes optical tracking data from hardware providers)  
**Data produced:**
- Advanced metrics: shot quality, defensive influence, pass quality, off-ball movement scores
- Augmented reality overlays for broadcasts (ESPN/ABC CourtVision)
- Real-time coaching tools and team analytics platforms
- "Dragon" mesh technology (R&D on player mesh modeling)

**NBA adoption timeline:**
- **2013:** Founded by Rajiv Maheswaran (USC professor) and research team
- **2015:** Initial NBA partnerships (LA Clippers, Dallas Mavericks)
- **2017–2023:** Official NBA tracking provider (both optical capture and analytics)
- **2023–present:** Analytics engine and League Pass augmentation partner (optical capture transitioned to Sony Hawk-Eye)
- **2021:** Acquired by Genius Sports

**Important distinction (as of 2023-24):**
- **Raw optical capture:** Now handled by Sony Hawk-Eye (~14 cameras, 60 FPS, pose/multi-point 3D)
- **Second Spectrum role:** Processes Hawk-Eye optical data to generate AI-derived metrics, powers team tools, and provides broadcast augmentation (CourtVision)

**Access model:**
- **Proprietary:** Available only to NBA teams, league office, and broadcast partners
- **NBA.com/stats:** Select metrics exposed on official stats portal
- **CourtVision (broadcast):** Fans see augmented reality overlays during ESPN/ABC broadcasts, but underlying data is not downloadable

**Book-safe citation:**
- **Primary sources:**
  - NBA press releases: "NBA Partners with Second Spectrum" (2017), Genius Sports partnership expansion (League Pass + Dragon)
  - Second Spectrum website: https://www.secondspectrum.com/index.html
  - NBA.com/stats tracking metrics (cite specific endpoints)
  - ESPN CourtVision broadcast examples (cite as "broadcast augmentation," not data source)
- **Secondary sources:**
  - SSAC papers discussing Second Spectrum metrics (2018–present)
  - Trade press: The Athletic, ESPN features on "next-gen stats"
  - Academic papers: Some research labs have collaborated with Second Spectrum for published studies (cite paper, not direct data access)
- **Citation format (2017–2023):** "Second Spectrum tracking system (NBA official partner, optical and analytics)"
- **Citation format (2023–present):** "Second Spectrum analytics engine (NBA partner, processes Hawk-Eye optical data)"

**Public secondary sources:**
- Second Spectrum company page: https://www.secondspectrum.com/index.html
- NBA.com tracking stats: https://www.nba.com/stats/
- SSAC papers: "HoopEval: Individual Player Action Evaluation via Deep Reinforcement Learning" (2026, uses tracking data)
- Genius Sports acquisition announcement (2021): https://geniussports.com/
- Genius Sports NBA partnership expansion (League Pass, Dragon): Check Genius Sports press releases

---

### Hawk-Eye (Sony)

**Provider:** Hawk-Eye Innovations (Sony subsidiary)  
**Technology:** Multi-camera optical tracking system with pose estimation and multi-point 3D tracking  
**Data produced:**
- Player and ball positions (pose estimation, skeletal tracking)
- Multi-point 3D coordinates (more detailed than previous XY tracking)
- ~14 cameras per arena, 60 frames per second (upgrade from SportVU's 25 FPS)
- Raw optical data fed to analytics partners (Second Spectrum, Synergy, Sportradar)

**NBA adoption timeline:**
- **Pre-2023:** Primarily known for tennis line-calling, soccer goal-line technology, cricket ball tracking
- **2023–present:** Official NBA optical tracking provider (replaced Second Spectrum for raw capture)
- **Partnership model:** Hawk-Eye provides raw optical data; Second Spectrum processes it for analytics and broadcast augmentation

**Basketball-specific use (as of 2023-24):**
- **NBA official optical capture:** All 30 NBA arenas equipped with Hawk-Eye camera systems
- **Data distribution:** Hawk-Eye optical feeds power Second Spectrum analytics, Synergy scouting, Sportradar team platforms
- **Officiating aids:** Shot clock accuracy, out-of-bounds review (secondary use)
- **International:** Some FIBA and international leagues use Hawk-Eye for officiating technology

**Access model:**
- **Proprietary:** Raw optical data not publicly available
- **Indirect access:** NBA.com/stats metrics (processed by Second Spectrum from Hawk-Eye inputs)
- **Team platforms:** Teams access analytics via Second Spectrum, Synergy, Sportradar (all using Hawk-Eye optical data)

**Book-safe citation:**
- **Primary sources:**
  - Sports Business Journal (2023-03-09): "NBA bringing in Hawk-Eye for tracking data in 2023-24"
  - The Guardian (2023-10-20): Hawk-Eye NBA data coverage
  - Sports Business Journal (2023-10-27): Sportradar/Synergy integration with Hawk-Eye optical inputs
  - Hawk-Eye Innovations press releases (NBA partnership)
- **Secondary sources:**
  - Trade press: SBJ, SportTechie, Sports Innovation Lab
  - FIBA officiating technology announcements (international use)
- **Citation format (2023–present):** "Hawk-Eye optical tracking system (Sony; NBA official optical provider, 2023–present)"
- **Citation format (pre-2023):** "Hawk-Eye officiating technology (Sony; limited basketball deployment)"

**Public secondary sources:**
- Hawk-Eye Innovations website: https://www.hawkeyeinnovations.com/
- Sony Sports Technology page (Hawk-Eye): https://www.sony.com/en/SonyInfo/technology/activities/Hawk-Eye/
- Sports Business Journal (2023-03-09): NBA/Hawk-Eye partnership announcement
- The Guardian (2023-10-20): NBA tracking technology shift

---

## Video Tagging & Scouting Platforms

### Synergy Sports Technology

**Provider:** Synergy Sports Technology (acquired by Collegiate Sports Management Group in 2014; later integrated with Stats Perform in some markets)  
**Technology:** Video indexing and play-type tagging (manual + assisted), integrated with optical tracking data  
**Data produced:**
- Play-type classifications: pick-and-roll, isolation, post-up, transition, spot-up, off-screen, cuts
- Defensive matchup tagging
- Shot location and outcome (make/miss)
- Video clips indexed by player, team, play type
- **As of 2023:** Enhanced with Hawk-Eye optical tracking inputs for NBA team platform

**League adoption:**
- **NBA:** Used by team front offices and coaching staffs (2000s–present); not an official league-wide system but widely adopted
- **2023:** Integration with Hawk-Eye optical data via Sportradar partnership (see Sports Business Journal 2023-10-27)
- **NCAA:** Official stats provider for Division I men's and women's basketball (2008–present)
- **FIBA:** Used by international federations for scouting
- **WNBA, European leagues:** Various team subscriptions

**Access model:**
- **Subscription service:** Teams, media, and individuals can purchase access (pricing varies by tier)
- **Not public API:** No programmatic data access; web-based video platform only
- **Scouting reports:** Some teams publish partial Synergy data in press releases (e.g., draft scouting reports)

**Book-safe citation:**
- **Primary sources:**
  - Synergy Sports Technology website: https://synergysports.com/
  - Sports Business Journal (2023-10-27): Sportradar/Synergy integration with Hawk-Eye optical inputs
  - NCAA partnership announcements: "NCAA Partners with Synergy Sports" (2008)
  - Team scouting reports: When teams cite Synergy data publicly (e.g., "Player X scored 1.2 PPP in pick-and-roll per Synergy")
- **Secondary sources:**
  - Draft analyst reports (e.g., The Stepien, ESPN draft coverage citing Synergy)
  - Academic papers using Synergy classifications (e.g., play-type efficiency studies)
- **Citation format (2023–present):** "Synergy Sports Technology play-type classification (commercial scouting platform, Hawk-Eye optical integration)"
- **Citation format (pre-2023):** "Synergy Sports Technology play-type classification (commercial scouting platform)"

**Public secondary sources:**
- Synergy Sports website: https://synergysports.com/
- NCAA stats portal (powered by Synergy): https://www.ncaa.com/stats/basketball-men/d1
- ESPN/The Athletic draft coverage citing Synergy data
- Sports Business Journal (2023-10-27): Hawk-Eye integration announcement

---

### Stats Perform (formerly Opta)

**Provider:** Stats Perform (formed from merger of STATS LLC and Perform Group's sports data division)  
**Technology:** Event tagging (manual + AI-assisted), similar to Opta soccer data  
**Data produced:**
- Event-level data: shots, passes, turnovers, fouls (timestamped)
- Advanced metrics: expected goals (xG equivalent for basketball), pass networks
- Historical archives for European leagues

**Basketball relevance:**
- **Limited NBA use:** Primarily a soccer/football analytics vendor
- **European basketball:** Stats Perform provides data for some European leagues (e.g., EuroLeague)
- **International coverage:** FIBA events, Olympic basketball

**Access model:**
- **Proprietary API:** Available to media partners, betting operators, teams (subscription)
- **Not public:** No free tier or open data access

**Book-safe citation:**
- **Primary sources:**
  - Stats Perform website: https://www.statsperform.com/
  - EuroLeague data partnership announcements (if applicable)
- **Secondary sources:**
  - Academic papers using Stats Perform data for international basketball
  - Trade press: European basketball analytics coverage
- **Citation format:** "Stats Perform event tagging (European basketball leagues, international events)"
- **⚠️ Note:** Do not cite as NBA source unless specific NBA partnership is documented

**Public secondary sources:**
- Stats Perform website: https://www.statsperform.com/
- EuroLeague stats portal (check if powered by Stats Perform)

---

### Sportradar

**Provider:** Sportradar AG (Swiss company; publicly traded on NASDAQ as SRAD)  
**Technology:** Live data collection (scorekeeping + event tagging), betting odds aggregation, video tagging, integrated with optical tracking  
**Data produced:**
- Real-time game events (shots, fouls, substitutions)
- Play-by-play data (timestamped)
- Betting odds and lines (multi-bookmaker aggregation)
- Video highlights and tagging
- **As of 2023:** Enhanced team platform with Hawk-Eye optical tracking inputs (via Synergy partnership)

**NBA adoption:**
- **2016:** NBA announces Sportradar as official data partner for international betting and media distribution
- **2018:** Expanded partnership for real-time data feeds to authorized betting operators
- **2023:** Integration with Hawk-Eye optical data for team analytics platform (see Sports Business Journal 2023-10-27)
- **Role:** Data distribution and integrity monitoring; team platform provider

**Access model:**
- **Proprietary API:** Available to media partners, sportsbooks, and authorized partners
- **Not public:** No free access to raw feeds
- **NBA.com:** Sportradar powers some backend data infrastructure, but public-facing stats are NBA's own

**Book-safe citation:**
- **Primary sources:**
  - NBA-Sportradar partnership press releases: https://www.nba.com/news/nba-sportradar-partnership-2016
  - Sports Business Journal (2023-10-27): Sportradar/Synergy integration with Hawk-Eye optical inputs
  - Sportradar website: https://sportradar.com/
- **Secondary sources:**
  - Trade press: Sports Business Journal, Legal Sports Report (betting/media context)
- **Citation format (2023–present):** "Sportradar live data feeds and team platform (NBA partner, Hawk-Eye optical integration)"
- **Citation format (pre-2023):** "Sportradar live data feeds (NBA partner for betting and media distribution)"
- **⚠️ Context:** Cite when discussing betting markets, media infrastructure, or team analytics platforms

**Public secondary sources:**
- Sportradar corporate site: https://sportradar.com/
- NBA data partnership page: https://www.nba.com/news/nba-sportradar-partnership-2016
- Sports Business Journal coverage of NBA data deals
- Sports Business Journal (2023-10-27): Hawk-Eye integration announcement

---

## Wearable & In-Venue Sensor Systems

### ShotTracker

**Provider:** ShotTracker, Inc. (founded 2013)  
**Technology:** Sensor-based tracking system  
- **Ball sensors:** Embedded in basketballs to detect makes/misses, shot arc, release angle
- **Player sensors:** Wristbands or jersey tags for positioning and player identification
- **Arena sensors:** Mounted sensors triangulate ball and player locations

**Data produced:**
- Shot location, arc, and outcome (make/miss)
- Shot charts and heatmaps
- Player positioning during practice or games
- Real-time stats for in-arena displays and coaching dashboards

**League adoption:**
- **NBA G-League:** Installed in all G-League arenas (2017–present)
- **NCAA:** Partnerships with Division I programs (e.g., Purdue, Iowa, Kansas)
- **High school/AAU:** Expanding into youth basketball programs
- **Not NBA regular season:** NBA uses Hawk-Eye optical tracking (processed by Second Spectrum) instead

**Access model:**
- **Proprietary:** Data available only to teams/venues with ShotTracker installations
- **Team dashboards:** Coaching staff and players access via web portal
- **Fan-facing:** Some venues display ShotTracker data on arena screens; limited public download

**Book-safe citation:**
- **Primary sources:**
  - ShotTracker website: https://shottracker.com/
  - NBA G-League partnership announcement: "G-League Partners with ShotTracker" (2017)
  - NCAA case studies (e.g., Purdue Athletics press releases)
- **Secondary sources:**
  - Sports tech media: SportTechie, Front Office Sports coverage
- **Citation format:** "ShotTracker sensor-based tracking system (NBA G-League, NCAA programs)"

**Public secondary sources:**
- ShotTracker website: https://shottracker.com/
- NBA G-League press release: https://gleague.nba.com/ (search "ShotTracker")
- SportTechie coverage: https://www.sporttechie.com/ (search "ShotTracker basketball")

---

### Catapult Sports

**Provider:** Catapult Sports (Australian company; publicly traded on ASX as CAT)  
**Technology:** Wearable GPS and inertial measurement unit (IMU) sensors  
- **Devices:** Small pods worn in vests during practice or training (not allowed in NBA games)
- **Metrics:** Acceleration, deceleration, jump load, distance covered, sprint speed

**Data produced:**
- Load management metrics (cumulative strain, readiness scores)
- Movement patterns during practice
- Jump counts and landing impact
- Training intensity zones

**Basketball use:**
- **NBA teams:** Used in practice facilities for load management and injury prevention (exact team count undisclosed)
- **NCAA programs:** Adopted by some Division I programs
- **FIBA/International:** Some national teams use Catapult for training camps
- **Not game data:** Wearables are prohibited during NBA games (league rules)

**Access model:**
- **Proprietary:** Data available only to teams with Catapult subscriptions
- **Research collaborations:** Some teams have published anonymized data in academic journals (e.g., load management studies)

**Book-safe citation:**
- **Primary sources:**
  - Catapult Sports website: https://www.catapultsports.com/
  - Team training staff interviews (e.g., "Team X uses Catapult for load management per interview with Head of Performance")
  - Academic papers: Studies using anonymized Catapult data (cite the paper, not direct Catapult access)
- **Secondary sources:**
  - Trade press: Sports Illustrated, The Athletic features on load management
- **Citation format:** "Catapult wearable tracking system (NBA practice facilities, load management)"
- **⚠️ Context:** Cite for training and injury prevention, not in-game analytics

**Public secondary sources:**
- Catapult Sports website: https://www.catapultsports.com/
- Academic journals: Search "Catapult basketball load management" in PubMed, JSTOR
- Sports science conferences (e.g., NSCA, ACSM) presentations on Catapult data

---

### Kinexon

**Provider:** Kinexon GmbH (German company)  
**Technology:** Ultra-wideband (UWB) real-time location system (RTLS)  
- **Player tags:** Small sensors worn by players (in vests or integrated into jerseys)
- **Arena anchors:** Fixed sensors around the court for precise positioning (sub-10 cm accuracy)

**Data produced:**
- Real-time XY coordinates (similar to optical tracking but sensor-based)
- Player speed, distance, acceleration
- Proximity analytics (player spacing, defensive pressure)
- Ball tracking (when ball sensor is used)

**Basketball use:**
- **FIBA:** Official tracking partner for FIBA competitions (2019–present), including FIBA Basketball World Cup and Olympic Qualifying Tournaments
- **European leagues:** Some EuroLeague and national league teams use Kinexon
- **NBA practice facilities:** A few NBA teams have installed Kinexon for practice tracking (exact teams undisclosed)
- **Not NBA games:** Second Spectrum is the official NBA game tracking system

**Access model:**
- **Proprietary:** Data available only to teams/leagues with Kinexon installations
- **FIBA Live Stats:** Some Kinexon-derived metrics appear on FIBA.basketball during tournaments, but raw data is not downloadable

**Book-safe citation:**
- **Primary sources:**
  - Kinexon website: https://kinexon.com/
  - FIBA partnership announcement: "FIBA Partners with Kinexon" (2019)
  - FIBA tournament stats pages (cite specific metrics when public)
- **Secondary sources:**
  - Sports tech media: SportTechie, Sports Innovation Lab
  - Academic papers: Some European research uses Kinexon data (cite the paper)
- **Citation format:** "Kinexon UWB tracking system (FIBA official partner, European leagues)"

**Public secondary sources:**
- Kinexon website: https://kinexon.com/
- FIBA press release: https://www.fiba.basketball/news/fiba-kinexon-partnership-2019
- EuroLeague technology announcements (if applicable)

---

## FIBA & International Tournament Tracking

### FIBA LiveStats

**Provider:** FIBA (Fédération Internationale de Basketball)  
**Technology:** Manual event tagging by official statisticians (courtside data entry)  
**Data produced:**
- Play-by-play events (shots, fouls, turnovers, substitutions)
- Box score stats (points, rebounds, assists, etc.)
- Shot charts (basic location zones, not continuous XY)

**Availability:**
- **Public access:** Summary stats and play-by-play available on FIBA.basketball during tournaments (World Cup, Olympics, Continental Championships)
- **No API:** No official API for downloading historical data; web scraping is possible but check FIBA's Terms of Service
- **PDF reports:** FIBA publishes annual [BAT Statistics Reports](https://www.fiba.basketball/bat-statistics-2022.pdf) (Basketball Arbitral Tribunal stats, not game tracking)

**Book-safe citation:**
- **Primary sources:**
  - FIBA official tournament pages: https://www.fiba.basketball/
  - FIBA LiveStats web interface (during tournaments)
  - FIBA BAT Statistics PDF (for governance data, not game stats)
- **Secondary sources:**
  - FIBA press releases on tournament results
- **Citation format:** "FIBA LiveStats (official tournament statistics, FIBA competitions)"

**Public secondary sources:**
- FIBA Basketball website: https://www.fiba.basketball/
- FIBA BAT Statistics 2022: https://www.fiba.basketball/bat-statistics-2022.pdf
- Olympic Games basketball pages: https://olympics.com/en/sports/basketball/

---

### EuroLeague & European Tracking

**EuroLeague Basketball (EB):**
- **Official stats provider:** EuroLeague uses a combination of Stats Perform (formerly Opta) and proprietary tagging
- **Access:** Stats available on EuroLeague.net; no public API
- **Tracking systems:** Some EuroLeague teams use Kinexon or other vendors for internal analytics (not league-wide)

**Book-safe citation:**
- **Primary sources:**
  - EuroLeague Basketball website: https://www.euroleague.net/
  - EuroLeague stats portal: https://www.euroleague.net/main/statistics
- **Citation format:** "EuroLeague official statistics (EuroLeague.net)"

**Public secondary sources:**
- EuroLeague Basketball: https://www.euroleague.net/
- EuroCup Basketball: https://www.eurocupbasketball.com/

---

## Open-Source Approximations & Research Systems

These are **not commercial systems** but academic/open-source projects that approximate tracking data from broadcast video. They do not replace SportVU/Second Spectrum but are useful for researchers without access to proprietary data.

### DeepSportRadar-v1

**Source:** https://paperswithcode.com/dataset/deepsportradar-v1  
**Technology:** Annotated broadcast video dataset (basketball + other sports)  
**Data produced:** Bounding boxes for players, ball detection, court keypoint annotations  
**Access:** Available for academic research with registration (research use only, not commercial)  
**Book-safe citation:**
- **Primary source:** DeepSportRadar-v1 dataset page (Papers with Code)
- **Citation format:** "DeepSportRadar-v1 annotated broadcast video dataset (research use)"
- **⚠️ Context:** Cite when discussing broadcast-based tracking research, not as equivalent to in-arena optical tracking

### Academic Broadcast Tracking Papers

Several research groups have published methods to reconstruct player tracking from broadcast video:

1. **"Approaching In-Venue Quality Tracking from Broadcast Video using Generative AI"** (SSAC 2024)  
   *Abstract:* Generative AI for extracting tracking data from broadcast video  
   *Relevance:* Democratizing tracking access for leagues without optical systems

2. **YOLO-based basketball detection** (various papers)  
   *Technology:* YOLO (You Only Look Once) object detection applied to basketball broadcast  
   *Relevance:* Real-time player and ball detection from TV feeds  
   *⚠️ Note:* YOLO is a computer vision method, not a commercial product

**Book-safe citation for research methods:**
- **Primary sources:** The academic paper itself (journal article or conference proceeding)
- **Citation format:** "Broadcast-based tracking using [method name], per [Author et al., Year]"
- **⚠️ Context:** Cite as research methodology, not commercial system

---

## Out of Scope for This Repository

**This repository does NOT include:**

1. **Proprietary tracking dumps:** No SportVU, Second Spectrum, Kinexon, or ShotTracker raw data files
2. **API access credentials:** No Synergy logins, no Stats Perform API keys, no Sportradar feeds
3. **Betting data:** No odds, lines, or gambling-specific datasets (per ROADMAP)
4. **Team-internal analytics:** No leaked front-office reports, no confidential scouting data
5. **Broadcast video files:** No NBA League Pass recordings, no EuroLeague TV archives
6. **Paywalled research:** No PDFs behind journal paywalls (link to DOI instead)

**What this repository DOES include:**
- This citation guide (how to reference commercial systems)
- Links to public secondary sources (press releases, company websites, SSAC papers)
- Documentation of what data types exist and which chapters of the book they support

---

## Cross-References

### Related Documentation in This Repository

- **[CHAPTER-MAP.md](CHAPTER-MAP.md):** Maps Scrivener binder paths to data artifacts; reference this doc when "ANALYTICS / state of the data" needs SportVU/Second Spectrum context
- **[DATA-REPOS.md](DATA-REPOS.md):** Catalogs public Git repositories and open data sources; complementary to this doc (this doc = commercial systems, DATA-REPOS.md = open-source tools)
- **[SLOAN-ARCHIVE.md](SLOAN-ARCHIVE.md):** Index of SSAC papers; many papers discuss or use tracking data (see references above)
- **[ROADMAP.md](ROADMAP.md):** "Analytics chapter: describe the pipes, do not host them" — this doc implements that principle

### How to Use This Document

**For book authors:**
1. Identify which tracking system is relevant to your claim (e.g., "SportVU tracking showed...")
2. Check the "Book-safe citation" section for proper attribution format
3. Use primary sources (press releases, official websites) when possible
4. Use secondary sources (SSAC papers, trade press) to support claims about what the system revealed
5. Do NOT claim access to raw data unless you have explicit permission

**For data scientists:**
1. Use this as a landscape overview (what systems exist, what they measure)
2. For actual data access: check [DATA-REPOS.md](DATA-REPOS.md) for open-source alternatives
3. For research using proprietary data: contact the vendor directly or collaborate with a university/team with access

---

## Bibliography & Primary Sources

### Press Releases & Announcements

- **SportVU NBA Partnership (2013):** "NBA, STATS LLC Announce Full League Integration of SportVU Player Tracking Technology" — NBA.com press release (archived)
- **Second Spectrum NBA Partnership (2017):** "NBA Partners with Second Spectrum for Optical Tracking, Data, and Broadcast Augmentation" — NBA.com
- **Hawk-Eye NBA Partnership (2023):** "NBA bringing in Hawk-Eye for tracking data in 2023-24" — Sports Business Journal, March 9, 2023
- **Hawk-Eye NBA Coverage (2023):** The Guardian, October 20, 2023 (Hawk-Eye NBA data coverage)
- **Sportradar/Synergy Hawk-Eye Integration (2023):** Sports Business Journal, October 27, 2023 (Sportradar/Synergy integration with Hawk-Eye optical inputs)
- **Genius Sports Acquires Second Spectrum (2021):** https://geniussports.com/
- **Genius Sports NBA Partnership Expansion:** Genius Sports press releases (League Pass, Dragon mesh technology)
- **NBA-Sportradar Partnership (2016):** https://www.nba.com/news/nba-sportradar-partnership-2016
- **ShotTracker G-League Partnership (2017):** "NBA G-League Announces Partnership with ShotTracker" — GLeague.NBA.com
- **FIBA-Kinexon Partnership (2019):** "FIBA Partners with Kinexon for Real-Time Tracking" — FIBA.basketball press release

### Company Websites

- **Second Spectrum:** https://www.secondspectrum.com/
- **Hawk-Eye Innovations:** https://www.hawkeyeinnovations.com/
- **Synergy Sports Technology:** https://synergysports.com/
- **Stats Perform:** https://www.statsperform.com/
- **Sportradar:** https://sportradar.com/
- **ShotTracker:** https://shottracker.com/
- **Catapult Sports:** https://www.catapultsports.com/
- **Kinexon:** https://kinexon.com/

### NBA & League Resources

- **NBA.com/stats tracking dashboard:** https://www.nba.com/stats/ (Hawk-Eye optical data processed by Second Spectrum analytics, 2023–present)
- **FIBA Basketball:** https://www.fiba.basketball/ (tournament stats, BAT reports)
- **EuroLeague Basketball:** https://www.euroleague.net/ (European league stats)
- **NCAA Basketball Stats:** https://www.ncaa.com/stats/basketball-men/d1 (powered by Synergy)

### Academic & Conference Papers

See [SLOAN-ARCHIVE.md](SLOAN-ARCHIVE.md) for full index. Key papers discussing tracking systems:

- "CourtVision: New Visual and Spatial Analytics for the NBA" (SSAC 2012) — Early SportVU visualization
- "Deconstructing the Rebound with Optical Tracking Data" (SSAC 2012) — SportVU rebounding analysis
- "HoopEval: Individual Player Action Evaluation via Deep Reinforcement Learning" (SSAC 2026) — Second Spectrum-era tracking
- "Approaching In-Venue Quality Tracking from Broadcast Video using Generative AI" (SSAC 2024) — Alternative to optical systems

### Trade Press & Analysis

- **Grantland / ESPN (2013–2016):** Zach Lowe, Kirk Goldsberry articles on SportVU era
- **The Athletic (2017–present):** "Next-gen stats" features on Second Spectrum
- **Sports Business Journal:** Coverage of NBA data partnerships
  - "NBA bringing in Hawk-Eye for tracking data in 2023-24" (March 9, 2023)
  - "Sportradar/Synergy integration with Hawk-Eye optical inputs" (October 27, 2023)
  - Sportradar, Second Spectrum partnership announcements
- **The Guardian (2023):** Hawk-Eye NBA data coverage (October 20, 2023)
- **SportTechie:** Sports technology vendor coverage (ShotTracker, Kinexon, Catapult)

---

## License & Attribution

This document catalogs publicly available information about commercial basketball tracking and analytics systems. All product names and trademarks are property of their respective owners. Links point to official company websites and press releases; no proprietary data or internal documentation is redistributed in this repository.

**Citation format for this document:**
> Wright, Glen. "Basketball Tracking & Analytics Software." *Hoops Data Sidecar*, 2026. https://github.com/glen-w/hoops/blob/main/docs/BASKETBALL-SOFTWARE.md

**Last updated:** September 19, 2026
