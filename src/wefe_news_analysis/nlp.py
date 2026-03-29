from __future__ import annotations

from functools import lru_cache


@lru_cache(maxsize=4)
def load_german_parser(model_name: str):
    try:
        import spacy
    except ImportError as exc:
        raise RuntimeError(
            "spaCy is required for parser-backed German analysis. "
            "Install project dependencies and the German model, for example: "
            "`pip install -e .[dev]` and `python -m spacy download de_core_news_sm`."
        ) from exc

    try:
        return spacy.load(model_name)
    except OSError as exc:
        raise RuntimeError(
            f"spaCy model '{model_name}' is not installed. "
            "Install it with `python -m spacy download de_core_news_sm`."
        ) from exc
