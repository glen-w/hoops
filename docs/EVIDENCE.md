# Evidence Desk

Quick reference for managing citations, sources, and data provenance in the Hoops sidecar repo.

## Purpose

The evidence desk is the daily workflow for tracking what the manuscript claims, what sources support those claims, and which claims need data products from this repo versus narrative-only citations.

## Core Artifact: `data/mentions.csv`

The single source of truth for what the draft asks for. Columns include:
- `section` — Scrivener binder path
- `kind` — dataset, study, figure, wanted
- `mention` — brief description of what's cited or needed
- `source` — URL, DOI, or citation
- `status` — linked, cited, partial, missing, hold

## Enrichment Plan (Phase 0)

`mentions.csv` will be extended with:
- `zotero_key` — item key from the Zotero `hoops` collection
- `doi` — DOI when available
- `priority` — P0/P1/P2 for writing leverage
- `blocks_section` — which Scrivener section can't be completed without this
- `notes` — hunt status, recompute vs cite-only, hedge instructions

## Workflow

1. **When adding a new mention**: Check if a Zotero item exists; if not, search or flag for Paperful PDF fetch
2. **When creating a derived table**: Cross-reference with `mentions.csv` and update status to `ready`; document methodology in the processing script or a sibling `.md` file
3. **When writing prose**: Use `docs/CHAPTER-MAP.md` to locate the derived artifact and Zotero key for the claim

## Paperful Integration

PDFs missing from Zotero `hoops` should be queued via Paperful (separate Infra process, not in this repo).
