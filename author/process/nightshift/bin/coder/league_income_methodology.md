# League Income Ingredients — Methodology & Source Documentation

**Purpose**: Explain blank cells in `league_income_ingredients.csv` by reason (no PR mention, missing link, data not public) with source URLs.

## Data Extraction Tasks

### 1. NBA Salary Cap / Tax / Apron History (2016-17 through 2026-27)
**Source**: Official pr.nba.com PRs  
**Task**: Locate and cite each PR announcement with URL and publish date  
**Expected**: season-grain rows for cap, tax, first apron, second apron, MLE biannual  
**Status**: [Search pr.nba.com announcement archive]

### 2. Portland Trail Blazers 2015-16 Season Metrics
**Source**: [Basketball-Reference](https://www.basketball-reference.com/teams/POR/2016/)  
**Task**: Extract net rating, attendance, payroll  
**Status**: [Ready to scrape B-R]

### 3. NBA TV Deal Valuations (Pre-2016-17 era)
**Source**: Sports Business Journal, Forbes archives (Oct 2014+)  
**Task**: Locate venue/date/amount for each announced TV deal  
**Status**: [Archive search required; flag unavailable if not found]

### 4. May 2016 Arena/Occupancy Coverage
**Source**: OregonLive and Portland local media  
**Task**: Search for Odom occupancy article, May 2016  
**Status**: [Search and flag unavailable if not found]

## Blank Cell Log
[Entries to be populated as sources are verified]
