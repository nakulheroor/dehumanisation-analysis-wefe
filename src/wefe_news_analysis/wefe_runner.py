from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from wefe.query import Query
from wefe.word_embedding_model import WordEmbeddingModel

from .config import ProjectConfig

if TYPE_CHECKING:
    from wefe.metrics import WEAT


def run_weat(config: ProjectConfig) -> dict:
    if not config.wefe.experiments:
        raise ValueError("At least one WEFE experiment must be configured.")

    embedding_path = Path(config.embeddings.path)
    if not embedding_path.exists():
        raise FileNotFoundError(
            f"Embedding model not found at {embedding_path}. Add a model before running WEFE."
        )

    raise NotImplementedError(
        "Load your embedding model into a WEFE WordEmbeddingModel and execute the query here."
    )


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


def metric_factory() -> "WEAT":
    from wefe.metrics import WEAT

    return WEAT()


def wrap_model(model: object, model_name: str = "custom-model") -> WordEmbeddingModel:
    return WordEmbeddingModel(model, model_name=model_name)
