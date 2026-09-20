# Mascot Bestiary Methodology

**Version:** 1.0  
**Date:** 2026-09-20  
**Source:** `data/derived/teams/teams.csv` (441 teams, as of 2026-09-19)

## Purpose

Classify team mascots into interpretive taxonomic categories: animal, human, abstract, object, or unknown. This is a *linguistics-adjacent* structured dataset—no mascot names are invented.

## Methodology

### Taxonomy

- **animal**: Living creatures (real or mythical). Subdivided:
  - `bovine` (bulls, bison)
  - `ursine` (bears)
  - `avian` (hawks, eagles, raptors)
  - `feline` (cats, panthers, lions, tigers)
  - `canine` (dogs, wolves, coyotes)
  - `equine` (horses)
  - `primate` (gorillas)
  - `insect` (hornets, bees)
  - `lagomorph` (rabbits)
  - `mythical` (dragons)
  - `general` (unspecified animal)

- **human**: Anthropomorphic or humanoid figures.
  - `mythological` (leprechauns)
  - `anthropomorphic` (wizards, kings, knights)

- **abstract**: Non-physical concepts.
  - `elemental` (heat, storm, magic)

- **object**: Inanimate things.
  - `inanimate` (rockets, suns)

- **unknown**: Mascot name provided but does not match keywords, or no mascot given.

### Classification rules

1. Extract the `mascot` field from teams.csv.
2. If blank → `taxon = unknown`, `confidence = GAP`.
3. If present → keyword matching against curated lists:
   - "bull" in name → `animal / bovine`
   - "hawk" in name → `animal / avian`
   - "leprechaun" in name → `human / mythological`
4. Unmatched mascots default to `unknown / unclassified` but are marked `HIGH` confidence (the string exists; the taxonomy is interpretive).

### Confidence

- **HIGH**: Mascot name present in source data.
- **GAP**: Mascot field blank in teams.csv.

### Limitations

- **Interpretation is subjective**: "Hooper" (Detroit Pistons) could be human (basketball player) or abstract (action). The script classifies it as `unknown` because it lacks clear keywords.
- **Mascot evolution**: Teams may have retired or changed mascots. This dataset reflects the 2026-09-19 snapshot from teams.csv.
- **Detail granularity**: `taxon_detail` is interpretive. "Lucky the Leprechaun" → `human / mythological` is a reading, not a canonical classification.

### Examples

| Team | Mascot | Taxon | Taxon Detail | Notes |
|------|--------|-------|--------------|-------|
| Chicago Bulls | Benny the Bull | animal | bovine | Clear bovine |
| Boston Celtics | Lucky the Leprechaun | human | mythological | Irish folklore |
| Miami Heat | Burnie | abstract | elemental | "Heat" → fire/elemental |
| Brooklyn Nets | (blank) | unknown | (blank) | No mascot listed |
| Indiana Pacers | Boomer | unknown | unclassified | Ambiguous name |

## Output

### `mascot_bestiary.csv`

| Column | Description |
|--------|-------------|
| `team_id` | Team identifier |
| `mascot` | Mascot name (from teams.csv, may be blank) |
| `taxon` | Top-level category |
| `taxon_detail` | Subcategory (interpretive) |
| `league_id` | League identifier |
| `source_url` | Wikidata QID URL |
| `confidence` | `HIGH` if mascot present, `GAP` if blank |

## Future enhancements

- Add mascot debut year (would require external sources).
- Distinguish official vs. unofficial mascots.
- Link to mascot images or design notes.
- Expand keyword list for international leagues (e.g., "Condor" → avian).

## Honest limitations

Taxonomy is a *reading aid* for textual analysis, not zoological fact. "Raptor" (Toronto) is avian here, but the mascot costume may be a dinosaur (Velociraptor). The dataset prioritises structural clarity over perfect classification. When ambiguous, it leaves `taxon = unknown` rather than guessing.
