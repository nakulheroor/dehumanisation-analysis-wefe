from __future__ import annotations

import csv
import re
import string
import unicodedata
from pathlib import Path

from .config import ProjectConfig
from .pdf import extract_text_from_pdf

GERMAN_STOPWORDS = {
    "aber",
    "als",
    "am",
    "an",
    "auch",
    "auf",
    "aus",
    "bei",
    "bin",
    "bis",
    "da",
    "das",
    "dem",
    "den",
    "der",
    "des",
    "die",
    "doch",
    "dort",
    "du",
    "ein",
    "eine",
    "einem",
    "einen",
    "einer",
    "er",
    "es",
    "für",
    "hat",
    "hier",
    "ich",
    "ihm",
    "im",
    "in",
    "ist",
    "mit",
    "nach",
    "nicht",
    "noch",
    "oder",
    "sie",
    "sind",
    "so",
    "um",
    "und",
    "vom",
    "von",
    "war",
    "wie",
    "wir",
    "wird",
    "zu",
    "zum",
    "zur",
}


def ensure_directories(config: ProjectConfig) -> None:
    config.corpus.raw_pdf_dir.mkdir(parents=True, exist_ok=True)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    config.output.reports_dir.mkdir(parents=True, exist_ok=True)
    config.output.manifest_path.parent.mkdir(parents=True, exist_ok=True)
    config.analysis.outputs.sentence_features_path.parent.mkdir(parents=True, exist_ok=True)
    config.analysis.outputs.article_group_features_path.parent.mkdir(parents=True, exist_ok=True)
    if config.metadata.sidecar_csv_path is not None:
        config.metadata.sidecar_csv_path.parent.mkdir(parents=True, exist_ok=True)


def discover_pdfs(config: ProjectConfig) -> list[Path]:
    return sorted(config.corpus.raw_pdf_dir.rglob(config.corpus.article_glob))


def preprocess_text(text: str, config: ProjectConfig) -> str:
    processed = text
    rules = config.preprocessing

    if rules.normalize_unicode:
        processed = unicodedata.normalize("NFKC", processed)

    if rules.ocr_cleanup:
        processed = processed.replace("\u00ad", "")
        processed = processed.replace("ﬁ", "fi").replace("ﬂ", "fl")
        processed = re.sub(r"(\w)-\n(\w)", r"\1\2", processed)
        processed = processed.replace("\n", " ")

    if rules.lowercase:
        processed = processed.lower()

    if rules.strip_digits:
        processed = re.sub(r"\d+", " ", processed)

    if rules.strip_punctuation:
        translation = str.maketrans({character: " " for character in string.punctuation})
        processed = processed.translate(translation)

    tokens = processed.split()

    if rules.stopword_handling == "remove":
        if config.corpus.language.lower() != "german":
            raise ValueError(
                "stopword removal is only implemented for corpus.language='german'."
            )
        tokens = [token for token in tokens if token not in GERMAN_STOPWORDS]

    tokens = [token for token in tokens if len(token) >= rules.min_token_length]
    processed = " ".join(tokens)

    if rules.collapse_whitespace:
        processed = re.sub(r"\s+", " ", processed).strip()

    return processed


def load_metadata_rows(config: ProjectConfig) -> dict[str, dict[str, str]]:
    metadata_path = config.metadata.sidecar_csv_path
    if metadata_path is None or not metadata_path.exists():
        return {}

    with metadata_path.open("r", encoding=config.corpus.default_encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or config.metadata.id_column not in reader.fieldnames:
            raise ValueError(
                f"Metadata sidecar must contain the id column '{config.metadata.id_column}'."
            )

        rows: dict[str, dict[str, str]] = {}
        for row in reader:
            article_id = (row.get(config.metadata.id_column) or "").strip()
            if not article_id:
                continue
            rows[article_id] = {
                key: value
                for key, value in row.items()
                if key is not None and key != config.metadata.id_column
            }
        return rows


def extract_pdfs(config: ProjectConfig) -> list[Path]:
    ensure_directories(config)
    written_files: list[Path] = []

    for pdf_path in discover_pdfs(config):
        article = extract_text_from_pdf(pdf_path)
        article_text = preprocess_text(article.text, config)
        output_path = config.corpus.processed_text_dir / f"{pdf_path.stem}.txt"
        output_path.write_text(article_text, encoding=config.corpus.default_encoding)
        written_files.append(output_path)

    return written_files


def build_manifest(config: ProjectConfig) -> Path:
    ensure_directories(config)
    text_files = sorted(config.corpus.processed_text_dir.glob("*.txt"))
    metadata_rows = load_metadata_rows(config)
    metadata_fieldnames = sorted({key for row in metadata_rows.values() for key in row})
    fieldnames = ["article_id", "text_path", "character_count", *metadata_fieldnames]

    with config.output.manifest_path.open(
        "w", encoding=config.corpus.default_encoding, newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for text_path in text_files:
            article_id = text_path.stem
            content = text_path.read_text(encoding=config.corpus.default_encoding)
            row = {
                "article_id": article_id,
                "text_path": str(text_path),
                "character_count": len(content),
            }
            row.update(metadata_rows.get(article_id, {}))
            writer.writerow(row)

    return config.output.manifest_path
