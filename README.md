# Resume Intelligence

AI-powered resume ingestion, structured extraction, retrieval, and evaluation system for recruiting and talent analysis.

## Overview
This project demonstrates a production-style portfolio application that combines:
- LLM-based resume parsing with structured JSON output
- vector search / RAG for recruiter queries across candidate resumes
- evaluation benchmarking against synthetic ground-truth data
- FastAPI backend and Streamlit frontend

## Repository layout

```text
resume-intelligence/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .env.example
├── src/
│   └��─ resume_intelligence/
│       ├── __init__.py
│       ├── config.py
│       ├── ingestion/
│       │   └── __init__.py
│       ├── parsing/
│       │   └── __init__.py
│       ├── vector_store/
│       │   └── __init__.py
│       ├── evals/
│       │   └── __init__.py
│       ├── api/
│       │   └── __init__.py
│       └── ui/
│           └── __init__.py
├── scripts/
│   └── generate_synthetic_dataset.py
├── data/
│   └── synthetic/
└── tests/
```

## Phase 1: Architecture
The project is organized around the following modules:
- `ingestion`: file loading, PDF/DOCX extraction
- `parsing`: structured extraction with Pydantic and LLM function calling
- `vector_store`: embedding generation and indexing with Chroma/FAISS
- `evals`: benchmark and metric generation
- `api`: FastAPI endpoints for upload/search/chat
- `ui`: Streamlit UI for recruiter interaction

## Phase 2: Synthetic data generation
Run the generator:

```bash
python scripts/generate_synthetic_dataset.py
```

This will generate:
- PDFs in `data/synthetic/resumes/`
- JSON ground truth in `data/synthetic/ground_truth/candidates_ground_truth.json`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## License
MIT
