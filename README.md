# Hoops

Data and processing sandbox for [*Hoops: An Uncommon Field Guide to the Game of Basketball*](https://glenwright.earth/projects/hoops/).

The manuscript stays in Scrivener (`/Users/89298/Documents/Hoops/hoops.scriv`). Papers stay in the Zotero `hoops` collection. This repo is the sidecar: datasets, derived tables, and the short notes that connect them to the draft. Creative packs and process notes live under committed [`author/`](author/README.md) so every clone and cloud agent sees them — they are not citeable artifacts.

## Quick Links

- **What belongs here:** [AGENTS.md](AGENTS.md) · [SCOPE.md](SCOPE.md) · [CONTRIBUTING.md](CONTRIBUTING.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- What the draft already asks for: [data/mentions.csv](data/mentions.csv)
- Open basketball data landscape: [docs/NUMBERS-LANDSCAPE.md](docs/NUMBERS-LANDSCAPE.md) | [docs/DATA-REPOS.md](docs/DATA-REPOS.md)
- CBA structure extraction: [docs/cba-structure-pipeline.md](docs/cba-structure-pipeline.md)
- CBA lookup (Scrivener mid-draft): [docs/CBA-LOOKUP.md](docs/CBA-LOOKUP.md) — `python scripts/cba_lookup.py "Article VII"`
- One desk lookup: `uv run hoops ask "home court 2024"`
- Scrivener access from Cursor: [writerslogic/scrivener-mcp](https://github.com/writerslogic/scrivener-mcp), configured in `.cursor/mcp.json`. Reload the window once so the server connects. The project to open is the `.scriv` above, not this repo.

## Documentation

- **[CHAPTER-MAP.md](docs/CHAPTER-MAP.md)** — Maps Scrivener binder paths to data artifacts (spine only)
- **[DATA-REPOS.md](docs/DATA-REPOS.md)** — Source catalog: APIs, dumps, packages, and what not to vendor
- **[BASKETBALL-SOFTWARE.md](docs/BASKETBALL-SOFTWARE.md)** — Commercial tracking & analytics systems (SportVU, Second Spectrum, Synergy, etc.)
- **[SLOAN-ARCHIVE.md](docs/SLOAN-ARCHIVE.md)** — MIT Sloan Sports Analytics Conference papers index
- **[ownership/](docs/ownership/nba_README.md)** — NBA and EuroLeague ownership ledgers (methodology + CSV spines)

## Layout

- `data/derived/` — tables we may commit, one artifact per folder or file pair, with a short method note beside it
- `data/cba/` — committed CBA structure metadata (no agreement text). `data/derived/cba/` is an older fixture, not a second copy
- `data/studies/` — one short note per cited paper or draft hedge
- `data/raw/` — local downloads, not committed
- `docs/` — catalogs and the chapter map (not creative essays or spike diaries)
- `author/` — committed creative + process workspace (not citeable). See [author/README.md](author/README.md)
- `local/` — gitignored machine-only scratch (secrets, huge dumps, throwaway REPL)
- `scripts/` — builders that emit committed artifacts. `src/hoops_data/` — the installed package (`hoops ask`, the CBA parser, the Wikidata fetch)

## Data Policy

Do not commit the manuscript, the Zotero library, or raw tracking dumps. `data/raw/` is gitignored on purpose. For proprietary systems: cite, don't rehost. See [SCOPE.md](SCOPE.md) for the full in/out allowlist.
