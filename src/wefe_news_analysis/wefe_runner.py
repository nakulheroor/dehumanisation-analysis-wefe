from __future__ import annotations

import csv
import logging
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from gensim.models import KeyedVectors, Word2Vec
from wefe.query import Query
from wefe.word_embedding_model import WordEmbeddingModel

from .config import ProjectConfig


def ensure_numpy_wefe_compatibility() -> None:
    if not hasattr(np, "float_"):
        np.float_ = np.float64  # type: ignore[attr-defined]


def resolve_experiment_name(config: ProjectConfig, experiment_name: str | None = None) -> str:
    if experiment_name is not None:
        if experiment_name not in config.wefe.experiments:
            available = ", ".join(sorted(config.wefe.experiments))
            raise ValueError(f"Unknown WEFE experiment '{experiment_name}'. Available: {available}")
        return experiment_name

    if len(config.wefe.experiments) == 1:
        return next(iter(config.wefe.experiments))

    available = ", ".join(sorted(config.wefe.experiments))
    raise ValueError(
        "Multiple WEFE experiments are configured. Pass an experiment name. "
        f"Available: {available}"
    )


def build_query(config: ProjectConfig, experiment_name: str | None = None) -> Query:
    resolved_name = resolve_experiment_name(config, experiment_name)
    experiment = config.wefe.experiments[resolved_name]

    return Query(
        target_sets=[config.wefe.word_sets[name] for name in experiment.target_sets],
        attribute_sets=[config.wefe.word_sets[name] for name in experiment.attribute_sets],
        target_sets_names=experiment.target_sets,
        attribute_sets_names=experiment.attribute_sets,
    )


def tokenize_corpus_for_embeddings(config: ProjectConfig) -> list[list[str]]:
    text_files = sorted(config.corpus.processed_text_dir.glob("*.txt"))
    sentences: list[list[str]] = []
    for text_path in text_files:
        content = text_path.read_text(encoding=config.corpus.default_encoding)
        for line in content.splitlines():
            tokens = line.split()
            if tokens:
                sentences.append(tokens)
    if not sentences:
        raise ValueError(
            f"No processed text files were found in {config.corpus.processed_text_dir} for embedding training."
        )
    return sentences


def corpus_token_frequencies(config: ProjectConfig) -> Counter[str]:
    counts: Counter[str] = Counter()
    for sentence in tokenize_corpus_for_embeddings(config):
        counts.update(sentence)
    return counts


def train_embeddings(config: ProjectConfig) -> Path:
    sentences = tokenize_corpus_for_embeddings(config)
    embedding_config = config.embeddings
    embedding_config.path.parent.mkdir(parents=True, exist_ok=True)

    model = Word2Vec(
        sentences=sentences,
        vector_size=embedding_config.vector_size,
        window=embedding_config.window,
        min_count=embedding_config.min_count,
        epochs=embedding_config.epochs,
        sg=embedding_config.sg,
        workers=1,
    )

    if embedding_config.format == "gensim":
        model.save(str(embedding_config.path))
    else:
        model.wv.save(str(embedding_config.path))

    return embedding_config.path


def load_embeddings(config: ProjectConfig) -> KeyedVectors:
    embedding_path = Path(config.embeddings.path)
    if not embedding_path.exists():
        raise FileNotFoundError(
            f"Embedding model not found at {embedding_path}. Train or add a model before running WEFE."
        )

    if config.embeddings.format in {"keyedvectors", "gensim"}:
        if config.embeddings.format == "gensim":
            model = Word2Vec.load(str(embedding_path))
            return model.wv
        return KeyedVectors.load(str(embedding_path), mmap="r")

    return KeyedVectors.load_word2vec_format(str(embedding_path), binary=config.embeddings.binary)


def wrap_model(model: Any, model_name: str = "custom-model") -> WordEmbeddingModel:
    return WordEmbeddingModel(model, name=model_name)


def summarize_query_vocabulary(query: Query, keyed_vectors: KeyedVectors) -> dict[str, dict[str, Any]]:
    vocabulary = keyed_vectors.key_to_index
    summary: dict[str, dict[str, Any]] = {}

    named_sets = [
        *zip(query.target_sets_names, query.target_sets, strict=False),
        *zip(query.attribute_sets_names, query.attribute_sets, strict=False),
    ]

    for set_name, words in named_sets:
        missing_words = [word for word in words if word not in vocabulary]
        summary[set_name] = {
            "total_words": len(words),
            "missing_words": missing_words,
            "missing_ratio": (len(missing_words) / len(words)) if words else 0.0,
        }

    return summary


def format_missing_words_summary(vocabulary_summary: dict[str, dict[str, Any]]) -> str:
    parts: list[str] = []
    for set_name, stats in vocabulary_summary.items():
        missing_words = stats["missing_words"]
        if not missing_words:
            continue
        parts.append(f"{set_name}={','.join(missing_words)}")
    return "; ".join(parts)


def log_missing_query_words(
    experiment_name: str, model_name: str, vocabulary_summary: dict[str, dict[str, Any]]
) -> None:
    for set_name, stats in vocabulary_summary.items():
        missing_words = stats["missing_words"]
        if not missing_words:
            continue
        logging.warning(
            "WEFE experiment '%s' on embedding model '%s' is missing %d/%d words from set '%s': %s",
            experiment_name,
            model_name,
            len(missing_words),
            stats["total_words"],
            set_name,
            ", ".join(missing_words),
        )


def inspect_experiment_vocabulary(
    config: ProjectConfig, experiment_name: str | None = None
) -> dict[str, Any]:
    experiment_key = resolve_experiment_name(config, experiment_name)
    query = build_query(config, experiment_key)
    keyed_vectors = load_embeddings(config)
    frequencies = corpus_token_frequencies(config)
    vocabulary_summary = summarize_query_vocabulary(query, keyed_vectors)

    set_reports: list[dict[str, Any]] = []
    named_sets = [
        *zip(query.target_sets_names, query.target_sets, strict=False),
        *zip(query.attribute_sets_names, query.attribute_sets, strict=False),
    ]

    for set_name, words in named_sets:
        stats = vocabulary_summary[set_name]
        set_reports.append(
            {
                "set_name": set_name,
                "total_words": stats["total_words"],
                "missing_words": stats["missing_words"],
                "present_words": [word for word in words if word in keyed_vectors.key_to_index],
                "missing_ratio": stats["missing_ratio"],
                "corpus_counts": {word: frequencies.get(word, 0) for word in words},
            }
        )

    return {
        "experiment_name": experiment_key,
        "embedding_model_name": config.embeddings.model_name,
        "set_reports": set_reports,
    }


def metric_factory():
    ensure_numpy_wefe_compatibility()
    from wefe.metrics import WEAT

    return WEAT()


def run_wefe(config: ProjectConfig, experiment_name: str | None = None) -> dict[str, Any]:
    experiment_key = resolve_experiment_name(config, experiment_name)
    query = build_query(config, experiment_key)
    keyed_vectors = load_embeddings(config)
    vocabulary_summary = summarize_query_vocabulary(query, keyed_vectors)
    log_missing_query_words(experiment_key, config.embeddings.model_name, vocabulary_summary)
    model = wrap_model(keyed_vectors, config.embeddings.model_name)
    metric = metric_factory()
    experiment = config.wefe.experiments[experiment_key]
    result = metric.run_query(query, model, return_effect_size=True)
    result["experiment_name"] = experiment_key
    result["metric"] = experiment.metric
    result["embedding_model_name"] = config.embeddings.model_name
    result["missing_word_count"] = sum(
        len(stats["missing_words"]) for stats in vocabulary_summary.values()
    )
    result["missing_words_summary"] = format_missing_words_summary(vocabulary_summary)
    return result


def run_all_wefe(config: ProjectConfig) -> list[dict[str, Any]]:
    return [run_wefe(config, experiment_name) for experiment_name in sorted(config.wefe.experiments)]


def export_wefe_results(config: ProjectConfig, results: list[dict[str, Any]]) -> Path:
    output_path = config.output.reports_dir / "wefe_results.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames: list[str] = []
    for result in results:
        for key in result:
            if key not in fieldnames:
                fieldnames.append(key)

    with output_path.open("w", encoding=config.corpus.default_encoding, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    return output_path
