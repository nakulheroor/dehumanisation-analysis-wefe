# WEFE Newspaper Analysis

Python project for German newspaper corpora that:

- ingests PDFs and raw `.txt` articles
- preprocesses and normalizes corpus text
- builds article manifests with optional sidecar metadata
- runs parser-backed representation/framing analysis
- trains static Word2Vec embeddings from the corpus
- runs configured WEFE experiments and exports results

## Current capabilities

- `src/`-layout Python package with Typer CLI
- YAML-based project configuration
- PDF extraction with `pypdf`
- Raw text ingestion alongside PDFs
- German preprocessing and stopword handling
- German parser-backed analysis with spaCy
- Sentence-level and article/group-level representation features
- Word2Vec embedding training with `gensim`
- WEFE query construction and batch execution
- Test coverage for ingestion, analysis, embedding training, and WEFE export

## Setup

Create and activate a virtual environment, install the project, then install the German spaCy model:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m spacy download de_core_news_sm
```

Create your working config:

```bash
cp configs/project.example.yaml configs/project.yaml
```

## Data layout

Input corpus files can be mixed:

- PDFs under `data/raw/pdfs/`
- Raw text files under `data/raw/text/`

Optional metadata can be supplied as a CSV sidecar, by default:

- `data/raw/article_metadata.csv`

Processed outputs are written under:

- `data/processed/text/`
- `data/processed/articles_manifest.csv`
- `reports/`
- `models/`

## CLI workflow

1. Ingest and preprocess the corpus:

```bash
wefe-news ingest-corpus --config configs/project.yaml
```

2. Build a manifest:

```bash
wefe-news build-manifest --config configs/project.yaml
```

3. Run representation/framing analysis:

```bash
wefe-news analyze-representation --config configs/project.yaml
```

4. Train embeddings from the processed corpus:

```bash
wefe-news train-embeddings --config configs/project.yaml
```

5. Run all configured WEFE experiments:

```bash
wefe-news run-wefe --config configs/project.yaml
```

6. Inspect a configured WEFE query:

```bash
wefe-news show-query --config configs/project.yaml --experiment journalist_discrediting
```

## Config overview

The main config sections are:

- `project`: project identity
- `corpus`: raw input directories, globs, language, processed text directory, encoding
- `metadata`: sidecar CSV path and article id column
- `preprocessing`: normalization and cleanup rules
- `embeddings`: output path, format, model name, and Word2Vec hyperparameters
- `output`: manifest and reports directories
- `analysis`: target groups, framing lexicons, parser model, context window, analysis output paths
- `wefe`: reusable word sets and named WEFE experiments

See [project.example.yaml](/home/nakulheroor/dev/wefe/configs/project.example.yaml) for the current full example.

## Analysis outputs

`analyze-representation` writes:

- sentence-level features to `analysis.outputs.sentence_features_path`
- article/group aggregates to `analysis.outputs.article_group_features_path`

Current representation outputs include:

- target-group mention detection
- framing lexicon hit counts
- active/passive voice flags
- quote-aware context flags
- article/group aggregate counts and rates
- a composite `dehumanization_score`

The analyzer supports:

- German single-word lexicons
- German multiword phrase lexicons
- parser-backed sentence segmentation and dependency cues
- heuristic fallback when the parser is unavailable

## WEFE outputs

`train-embeddings` writes a trained embedding model to `embeddings.path`.

`run-wefe` writes:

- `reports/wefe_results.csv`

Current WEFE flow:

- trains static Word2Vec embeddings from `data/processed/text`
- loads embeddings from disk
- builds configured WEFE queries from `wefe.word_sets` and `wefe.experiments`
- runs WEAT-based experiments
- exports result rows for each configured experiment

## Notes and limitations

- The corpus and analysis defaults are currently German-oriented.
- `ingest-corpus` reads both PDFs and raw text inputs, then writes normalized `.txt` files to `data/processed/text`.
- The representation analysis is stronger than the initial heuristic version, but it is still a lightweight feature extractor rather than a full discourse model.
- WEFE currently uses static embeddings trained from the processed corpus. That is a baseline, not the final word for a serious research setup.
- The repo includes a local NumPy compatibility shim for the current `wefe` package version in this environment.

## Repository layout

```text
configs/                  Example YAML configuration
src/wefe_news_analysis/   Application package
tests/                    Automated tests
data/                     Expected raw and processed corpus directories
models/                   Trained or imported embedding artifacts
reports/                  Analysis and WEFE outputs
```
