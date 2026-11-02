"""Print the Hoops data-source catalog as a markdown table.

Every row is copied from the Zotero ds entries (paperful-out/hoops). Nothing here is a basketball statistic.
Usage: python3 -I list_sources.py
"""

# (name, zotero key, language/kind, access note taken from the ds abstract)
SOURCES = [
    ("Basketball-Reference", "WNKIH56T", "web", "Scrape with etiquette; not a bulk open license. Primary for avg_game_by_decade season rows."),
    ("NBA Stats", "6HB5G2B3", "web/API", "Official API behind nba_api; endpoints change; tracking/advanced uneven by era."),
    ("nba_api", "9FJZPDKM", "python", "NBA.com Stats client; rate-limit / ToS sensitive; check license before redistributing raw dumps."),
    ("Basketball_reference_scraper", "ZJQF9C6X", "python", "Scrapes Basketball-Reference; rate-limit politely; commercial ToS check before redistribute."),
    ("nbastatR", "PXFIX2G8", "R", "NBA Stats API plus Basketball-Reference, HoopsHype, RealGM, draft sources."),
    ("hoopR", "NEGCDXKA", "R", "ESPN NBA/NCAAM loads, NBA Stats wrappers, B-Ref scrapers; KenPom needs subscription."),
    ("wehoop", "4J27S9CP", "R", "WNBA and women's college via ESPN."),
    ("pbpstats", "ASRNZRRW", "python", "PBP parsing, lineups, on/off from NBA Stats feeds."),
    ("BasketballAnalyzeR", "ZV8R54SA", "R", "CRAN package for Basketball Data Science; analysis/visualization helpers."),
    ("Barttorvik T-Rank", "NVTWTCHG", "web/CSV", "Free D-I team ratings; verify scrape/ToS for bulk use."),
    ("KenPom", "RTJ8Q7E6", "web", "Paywall; cite-only for the manuscript unless subscribed."),
    ("wyattowalsh/basketball (Kaggle)", "VVBZ3IXN", "sqlite", "Parked; needs Kaggle auth; optional bulk land."),
    ("awesome-nba-data", "CTJJ3N4H", "index", "ToS matrix to read before choosing between scrapers. Not a license grant."),
]


def main():
    print("| source | key | kind | access note |")
    print("|---|---|---|---|")
    for name, key, kind, note in SOURCES:
        print(f"| {name} | {key} | {kind} | {note} |")


if __name__ == "__main__":
    main()
