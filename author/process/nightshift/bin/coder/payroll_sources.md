# NBA Payroll Data: Authoritative Sources

## Primary Sources (Use These)

### Hoops Rumors
- **Scope:** Season-by-season salary cap breakdowns, 2010-present
- **Grain:** Team total, guaranteed vs. non-guaranteed splits
- **URL Pattern:** hoopsrumors.com/{YEAR}-salary-cap-{TEAM}.html
- **Example:** [2015-16 Portland Trail Blazers](https://hoopsrumors.com/2015/11/201516-salary-cap-portland-trail-blazers.html)
- **Confidence:** HIGH (aggregated from official league sources)

### NBA Official Communications (pr.nba.com)
- **Scope:** Salary cap, luxury tax threshold, aprons, minimum payroll
- **Grain:** League-wide annual
- **Use for:** Cap floor validation, official rules
- **Example:** 2015-16 cap = $70M, luxury tax = $84.74M

### Basketball-Reference
- **Scope:** Win-loss records, team stats, payroll tables (historical)
- **Grain:** Season by season
- **Confidence:** HIGH (authoritative for wins/losses)
- **Note:** Payroll figures cross-check against Hoops Rumors

## Secondary Sources (Verify First)

### Spotrac
- **Scope:** Team cap tables, year-by-year (requires paid access for historical)
- **Limitation:** Paywalled for 2015-16 season; free access 2016-17 onward
- **Use for:** Current season validation

### HoopsHype
- **Scope:** Salary information, contract details
- **Limitation:** Focus on current/upcoming seasons
- **Use for:** Individual player verification

## Do Not Use
- Forbes articles without direct link/verification
- Kaggle datasets without source documentation
- Invented figures or estimates marked "approximate"

## For Book: Cite Hoops Rumors + Basketball-Reference
Pair win totals (BR) with payroll (Hoops Rumors) for transparency.