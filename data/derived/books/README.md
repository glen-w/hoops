# Hoops comparable books pack — 2026-09-19

Writer-facing comparable-title table for Glen’s Hoops book desk.

## Files
| File | Role |
|------|------|
| `comparable.csv` | **Infra schema** — copy to `data/derived/books/comparable.csv` |
| `comparable_basketball_books.csv` | Same data (desk filename) |
| `comparable_basketball_books.md` | Readable markdown table + criteria |
| `README.md` | This file |

## Schema (`comparable.csv`)
`title, author, publisher, year, amazon_url, amazon_rating, amazon_reviews_count, goodreads_url, goodreads_rating, goodreads_ratings_count, price_band, price_as_of, lane, why_comparable, isbn13, format_notes, source_urls, confidence`

### Locked `lane` values
`narrative` | `analytics` | `how_to_watch` | `history` | `memoir`

## Counts
- **Rows:** 19
- **Access / price_as_of:** 2026-09-19 (Europe/Paris)

## Major gaps
1. **Amazon.co.uk ratings & live prices:** Mostly **GAP**. Prefer `.co.uk` search URLs (or known product ASIN pages). Do not treat search-result star widgets as verified without an open product page.
2. **Amazon.com exception:** *Thinking Basketball* amazon.com listing showed **4.7 / 294** in a WebSearch snippet (OFFICIAL page fragment); UK price still GAP.
3. **Price bands:** Only a few UK/US list prices observed live (Greene LoveReading/Abrams; Partnow Triumph list). Others marked `varies — …` rather than fabricated £ ranges.
4. **ISBN:** One primary ISBN-13 per row (usually common pb or original hc); editions differ — see `format_notes`.

## Seeds verified
- Bill Simmons — *The Book of Basketball* (2009)
- Ben Taylor — *Thinking Basketball* (2016)
- Nick Greene — *How to Watch Basketball Like a Genius* (2021 hc / 2022 pb)

## OFFICIAL vs ANECDOTAL
- **OFFICIAL:** Goodreads rating/count pages; publisher sites (Abrams, Triumph, Nebraska, PRH, Hachette, S&S); Wikipedia bibliographic fields; Amazon product pages when successfully opened.
- **ANECDOTAL:** Not used for numeric ratings. Reddit/listicle mentions were not used as rating sources.
