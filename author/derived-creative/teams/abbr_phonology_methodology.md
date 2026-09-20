# Abbreviation Phonology Methodology

**Version:** 1.0  
**Date:** 2026-09-20  
**Source:** `data/derived/teams/teams.csv` (441 teams, as of 2026-09-19)

## Purpose

Analyse team abbreviations (`abbr` field) for structural and phonological patterns. This is a *linguistics-adjacent* structured dataset—no abbreviations are invented.

## Methodology

### Pattern classification

Team abbreviations are tagged with one or more patterns:

1. **city_initials**: Abbreviation matches the initials of the city name.
   - Example: BOS (Boston), ATL (Atlanta)

2. **nickname_clip**: Abbreviation is a 3-letter clip of the team nickname.
   - Example: BUL (Bulls), CAV (Cavaliers)

3. **city_plus_nickname**: Abbreviation combines city and nickname initials.
   - Example: CHI (Chicago [C] + [H]...), GSW (Golden State Warriors)

4. **state**: Contains a US state postal code.
   - Example: NYK (NY + Knicks), LAL (LA + Lakers)

5. **trigram** / **tetragram** / **long_form**: Length-based classification.
   - Most NBA abbreviations are 3 letters (trigram).
   - Some leagues use 4-letter codes (tetragram).

6. **other**: Catch-all for patterns not matching the above.

### Pattern detection

Patterns are *cumulative*—an abbreviation can have multiple tags. For example:
- **NYK** (New York Knicks) → `city_plus_nickname | state | trigram`

### Letter count

Simply `len(abbr)`. Most leagues standardise on 3-letter codes; European leagues may vary.

### Confidence

All rows inherit confidence from the source `teams.csv` row. The analysis itself is deterministic pattern-matching, but:
- If `abbr` is blank → `pattern_tags = unknown`, `letter_count = 0`.
- Patterns are *interpretive readings*—"CHI" could be "Chicago" initials or "Chi" nickname clip.

### Limitations

- **No phonetic analysis**: The dataset tags structural patterns, not pronunciation. "PHX" (Phoenix Suns) is tagged as city initials, but a phonological study might analyse /fɛnɪks/ → /fɪks/ clip.
- **International variance**: European leagues (EuroLeague, ACB, LNB) may use city names or club names. Pattern tags are tuned for NBA/WNBA conventions.
- **Ambiguity**: Some abbreviations are opaque (e.g., "OKC" Oklahoma City Thunder could be "Oklahoma City" or "OKlahoma City"). The script makes a best guess.

### Examples

| Team | Abbr | Pattern Tags | Letter Count | Notes |
|------|------|--------------|--------------|-------|
| Boston Celtics | BOS | city_plus_nickname \| trigram | 3 | City initials |
| Golden State Warriors | GSW | city_plus_nickname \| trigram | 3 | City + nickname |
| New York Knicks | NYK | city_plus_nickname \| state \| trigram | 3 | Contains NY state code |
| LA Clippers | LAC | city_plus_nickname \| state \| trigram | 3 | LA + Clippers |
| Oklahoma City Thunder | OKC | city_plus_nickname \| state \| trigram | 3 | OK state code |

## Output

### `abbr_phonology.csv`

| Column | Description |
|--------|-------------|
| `team_id` | Team identifier |
| `abbr` | Team abbreviation (from teams.csv) |
| `pattern_tags` | Pipe-delimited pattern list |
| `letter_count` | Length of abbreviation |
| `league_id` | League identifier |
| `notes` | Human-readable pattern description |

## Future enhancements

- Add International Phonetic Alphabet (IPA) transcriptions.
- Cross-reference abbreviations with broadcast graphics standards.
- Analyse uniqueness within leagues (collision detection).
- Compare NBA vs. EuroLeague abbreviation conventions.

## Honest limitations

This is a *pattern catalogue*, not phonological theory. Tags like "city_initials" are heuristic readings, not authoritative claims about naming intent. When the pattern is unclear (e.g., "CHA" for Charlotte could be city or nickname clip), the dataset flags it as `other` rather than inventing a story.
