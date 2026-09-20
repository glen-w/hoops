# Point a local LLM at the Zotero hoops collection

Status, 19 September 2026: this custom CLI was not built. The sitting uses [anapaulagomes/zotero-rag](https://github.com/anapaulagomes/zotero-rag) instead, cloned at `/Users/89298/Documents/zotero-rag`. The plan below is kept so it does not have to be redesigned.

Untangle does not implement this. `projects/hoops-book.md` and `big-ideas.md` only point at [Emmett McFarlane’s Medium RAG guide](https://medium.com/@emcf1/diy-ground-a-language-model-on-your-papers-from-zotero-with-finesse-a5c4ca7c187a): download a Zotero collection into a `pdfs/` folder, extract pages (the “finesse” is AI extraction), embed them, then generate. [ROADMAP.md](../ROADMAP.md) parks the same idea as “later, not a download.”

The library is already local. Zotero’s data dir is `/Users/89298/Documents/papers` (`zotero.sqlite` + `storage/`). Collection `hoops` (`BV4J5URJ`) and its children hold **2,516 items** and **1,446 PDFs**. The whole data dir is **16,708** non-attachment items. Do not re-download them, and do not commit the database, the PDFs, or extracted text.

## What we will not copy from the article

- No `pyzotero` download into a second `pdfs/` folder. Resolve attachments from sqlite: `itemAttachments.path` is `storage:<filename>` under `/Users/89298/Documents/papers/storage/<itemKey>/`.
- No AI page extraction and no Chroma. Nothing embedding-shaped was installed when this was written (`ollama list` had chat models only; no `nomic-embed-text`). Indexing 1,446 papers that way is a different project.
- No OpenRouter. Generation stays on loopback `http://127.0.0.1:11434`, which is the rule in Untangle `systems/ai.md`.
- Do not fold this into `src/hoops_data/ask.py`. That command is a desk lookup and must keep returning GAP instead of inventing. Do not put it under `src/hoops_data/cba/`.

Retrieval, if this plan is ever built, is keyword rank on title, creators, and abstract already in sqlite, then `pdftotext` on the top few PDFs. That is the local version of “point the model at the folder”: the model sees paper text, not the whole library.

```mermaid
flowchart LR
  query[Question] --> sql[Read-only sqlite]
  sql --> rank[Rank title and abstract]
  rank --> pdf[pdftotext top hits]
  pdf --> gen["Ollama /api/generate"]
  gen --> answer[Answer plus Zotero keys]
```

## Ollama shape to copy

Lift a small stdlib client, not a transcriptx import (this repo should not depend on that package).

From transcriptx `src/transcriptx/core/llm/ollama_client.py`: `POST /api/generate`, `"stream": false`, system text in `system` (not pasted into the prompt), temperature in `options`, answer from `response`. Three retries on timeout, connection errors, and HTTP 5xx only. Probe with `GET /api/tags` before the call.

From Untangle `scripts/opencode_watch.py`, which the transcriptx client does not do: `"think": false`. Required for `qwen3.8:latest` (the Untangle automation model, and it is installed). Thinking models otherwise leave `response` empty.

From transcriptx `src/transcriptx/core/llm/prompting.py`: instruction, then a data delimiter, then the papers, then a close delimiter. Cap the user prompt (transcriptx default 48,000 chars; use something closer to rollup’s 30,000 so a 17GB model stays usable). Head-and-tail truncation, not a mid-sentence cut.

Defaults: model `qwen3.8:latest`, base `http://127.0.0.1:11434`, temperature `0.2`, timeout about 300s. Override with `HOOPS_LLM_MODEL` and `HOOPS_LLM_BASE_URL`. If Ollama is down, print that and exit; do not fall through to a cloud API.

## Code

- `src/hoops_data/zotero_library.py` — open `file:/Users/89298/Documents/papers/zotero.sqlite?mode=ro`. Walk `hoops` and child collections (recursive `parentCollectionID`). Optional `--collection` matches a child name or key (`analytics` → `B5IYL479`). Return item key, title, creators, abstract, year, and PDF path. Read-only; never write the Zotero db.
- `src/hoops_data/library_ask.py` — rank those rows the same way `ask.py` scores tokens. Take the top 5 with a PDF. Extract with `pdftotext` (no `-layout`), the same tool as `src/hoops_data/cba/extract.py`. Cache extracts under `data/cache/zotero-text/<key>.txt`, gitignored. Build the delimited prompt. Call Ollama. Print the answer and the Zotero keys it was given. If the excerpts do not support an answer, the system prompt tells the model to say so.
- `scripts/hoops_library.py` — `uv run python scripts/hoops_library.py "home court mechanisms"`. Flags: `--collection`, `--model`, `--top`. No new console-script entry; `hoops` stays the desk lookup, where `ask` is currently just another query word.
- Tests with a tiny fixture sqlite and a fake HTTP response. No live Ollama, no real `zotero.sqlite`.
- Add `data/cache/` to `.gitignore`. One sentence in ROADMAP section 6 pointing at the script, so the parked line is no longer “not started.”

## Why this was not built

Off-the-shelf local RAG already does the Medium pipeline. zotero-rag reads `zotero.sqlite`, parses PDFs with docling, embeds with Ollama (`nomic-embed-text`) into LanceDB, and chats through Chainlit. A local patch (`ZOTERO_COLLECTION`) keeps ingestion on `hoops` and its children. The upstream tool has no collection filter, and ingesting the whole data dir would be days of CPU.
