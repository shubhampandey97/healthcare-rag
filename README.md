# Healthcare RAG: WHO immunisation + AI-medical-device regulation

> Work in progress. A question-answering system over official WHO, FDA and EU documents,
> with page-level citations, refusal when the answer is not in the sources,
> and a measured evaluation of retrieval and answer quality.

## Status
| Step | What | Status |
|---|---|---|
| 1 | PDF ingestion (page-level text, header/footer removal, bilingual WHO papers -> English column only) | done |
| 2 | Chunking | next |
| 3 | Embeddings + vector index | |
| 4 | Retrieval evaluation (gold questions, recall@k, MRR) | |
| 5 | Answer generation with citations and refusal | |
| 6 | Hybrid search + reranker | |
| 7 | End-to-end evaluation (faithfulness, refusal accuracy, robustness) | |
| 8 | App, Docker, deployment | |

## Sources
10 public documents (WHO position papers and summary table, FDA guidance and FDA/Health Canada/MHRA
principles, EU MDCG 2025-6). Exact titles, versions and download links: [docs/sources.md](docs/sources.md).
PDFs are not stored in this repo; download them into `data/raw/`.

## Findings so far
- WHO position papers are printed in English and French side by side. Reading whole pages mixed
  French into ~50 % of the WHO text. Fixed by detecting bilingual documents and keeping the
  English column only (column gap measured at 47 % of page width).

## Run
```bash
pip install pymupdf pytest ruff
pip install -e .
pytest -q
python -m rag.ingest        # data/raw/*.pdf -> data/processed/pages.jsonl
```
