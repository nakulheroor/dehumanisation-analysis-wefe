# WEFE Newspaper Analysis

Scaffold for a Python project that extracts text from newspaper PDFs and runs word embedding fairness evaluation workflows with WEFE.

## What is included

- A `src/`-layout Python package
- A Typer-based CLI
- YAML-based project configuration
- PDF text extraction utilities
- Corpus manifest generation
- A placeholder WEFE execution layer
- Basic tests for the initial structure

## Quick start

1. Create a virtual environment and install the project:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

2. Copy the example config and adapt it:

```bash
cp configs/project.example.yaml configs/project.yaml
```

3. Put input PDFs under `data/raw/pdfs/`.

4. Extract text:

```bash
wefe-news extract-pdfs --config configs/project.yaml
```

5. Build a manifest of extracted articles:

```bash
wefe-news build-manifest --config configs/project.yaml
```

6. Export sentence-level and article-level representation features:

```bash
wefe-news analyze-representation --config configs/project.yaml
```

7. Inspect a configured WEFE experiment:

```bash
wefe-news show-query --config configs/project.yaml --experiment gender_career_bias
```

## Config structure

The config is organized by subsystem:

- `project`: project-level identity
- `corpus`: PDF input, processed text output, language, and encoding
- `metadata`: optional sidecar CSV settings keyed by article id
- `preprocessing`: deterministic text cleanup rules applied during PDF extraction
- `embeddings`: local pretrained embedding artifact settings
- `output`: manifest and report destinations
- `analysis`: target groups, framing lexicons, context window, and representation export paths
- `wefe`: reusable named word sets and named experiments

## Suggested next steps

- Fill `data/raw/article_metadata.csv` if you want article metadata merged into the manifest
- Replace the example target groups and framing lexicons with the terms specific to your newsroom study
- Choose or train the embedding model you want to audit
- Implement the WEFE execution path in `wefe_runner.py` for your embedding format
- Add preprocessing rules for multilingual or OCR-heavy PDFs

## Layout

```text
configs/                  Example YAML configuration
src/wefe_news_analysis/   Application package
tests/                    Initial test coverage
data/                     Expected raw/processed corpus directories
reports/                  Future metrics and exported evaluation results
```
