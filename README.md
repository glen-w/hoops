# Hoops

Data and processing sandbox for [*Hoops: An Uncommon Field Guide to the Game of Basketball*](https://glenwright.earth/projects/hoops/).

The manuscript stays in Scrivener (`/Users/89298/Documents/Hoops/hoops.scriv`). Papers stay in the Zotero `hoops` collection. This repo is the sidecar: datasets, derived tables, and the notes that connect them to the draft.

## Quick Links

- Roadmap: [ROADMAP.md](ROADMAP.md)
- What the draft already asks for: [data/mentions.csv](data/mentions.csv)
- Open basketball data landscape: [docs/NUMBERS-LANDSCAPE.md](docs/NUMBERS-LANDSCAPE.md) | [docs/DATA-REPOS.md](docs/DATA-REPOS.md)
- CBA structure extraction: [docs/cba-structure-pipeline.md](docs/cba-structure-pipeline.md)
- CBA lookup (Scrivener mid-draft): [docs/CBA-LOOKUP.md](docs/CBA-LOOKUP.md) — `python scripts/cba_lookup.py "Article VII"`
- One desk lookup: `uv run hoops ask "home court 2024"`
- Scrivener access from Cursor: [writerslogic/scrivener-mcp](https://github.com/writerslogic/scrivener-mcp), configured in `.cursor/mcp.json`. Reload the window once so the server connects. The project to open is the `.scriv` above, not this repo.

## Documentation

- **[CHAPTER-MAP.md](docs/CHAPTER-MAP.md)** — Maps Scrivener binder paths to data artifacts
- **[DATA-REPOS.md](docs/DATA-REPOS.md)** — Source catalog: APIs, dumps, packages, and what not to vendor
- **[BASKETBALL-SOFTWARE.md](docs/BASKETBALL-SOFTWARE.md)** — Commercial tracking & analytics systems (SportVU, Second Spectrum, Synergy, etc.)
- **[SLOAN-ARCHIVE.md](docs/SLOAN-ARCHIVE.md)** — MIT Sloan Sports Analytics Conference papers index
- **[creative/](docs/creative/README.md)** — Cite-backed creative packs (numbers only from derived files)
- **[ownership/](docs/ownership/nba_README.md)** — NBA and EuroLeague ownership ledgers

## Layout

- `data/derived/` — tables we may commit, one artifact per folder or file pair, with a method note beside it
- `data/cba/` — committed CBA structure metadata (no agreement text). `data/derived/cba/` is an older fixture, not a second copy
- `data/studies/` — one note per cited paper
- `data/raw/` — local downloads, not committed
- `docs/` — catalogs, the chapter map, creative packs, ownership notes
- `scripts/` — one-off builders. `src/hoops_data/` — the installed package (`hoops ask`, the CBA parser, the Wikidata fetch)

## Data Policy

Do not commit the manuscript, the Zotero library, or raw tracking dumps. `data/raw/` is gitignored on purpose. For proprietary systems: cite, don't rehost.
