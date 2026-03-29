from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator, model_validator


class ProjectSection(BaseModel):
    name: str


class CorpusConfig(BaseModel):
    raw_pdf_dir: Path
    raw_text_dir: Path | None = None
    processed_text_dir: Path
    article_glob: str = "*.pdf"
    text_glob: str = "*.txt"
    language: str
    default_encoding: str = "utf-8"

    @field_validator("language")
    @classmethod
    def validate_language(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("corpus.language must not be empty.")
        return cleaned


class MetadataConfig(BaseModel):
    sidecar_csv_path: Path | None = None
    id_column: str = "article_id"

    @field_validator("id_column")
    @classmethod
    def validate_id_column(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("metadata.id_column must not be empty.")
        return cleaned


class PreprocessingConfig(BaseModel):
    normalize_unicode: bool = True
    lowercase: bool = True
    collapse_whitespace: bool = True
    strip_punctuation: bool = False
    strip_digits: bool = False
    min_token_length: int = 1
    stopword_handling: Literal["keep", "remove"] = "keep"
    ocr_cleanup: bool = True

    @field_validator("min_token_length")
    @classmethod
    def validate_min_token_length(cls, value: int) -> int:
        if value < 1:
            raise ValueError("preprocessing.min_token_length must be at least 1.")
        return value


class EmbeddingsConfig(BaseModel):
    path: Path
    format: Literal["word2vec", "keyedvectors", "gensim"]
    binary: bool
    model_name: str

    @field_validator("model_name")
    @classmethod
    def validate_model_name(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("embeddings.model_name must not be empty.")
        return cleaned


class OutputConfig(BaseModel):
    manifest_path: Path
    reports_dir: Path


class AnalysisOutputConfig(BaseModel):
    sentence_features_path: Path
    article_group_features_path: Path


class RepresentationAnalysisConfig(BaseModel):
    target_groups: dict[str, list[str]] = Field(default_factory=dict)
    framing_lexicons: dict[str, list[str]] = Field(default_factory=dict)
    context_window_tokens: int = 8
    parser_model: str = "de_core_news_sm"
    outputs: AnalysisOutputConfig

    @field_validator("target_groups", "framing_lexicons")
    @classmethod
    def validate_named_word_lists(cls, value: dict[str, list[str]], info: ValidationInfo) -> dict[str, list[str]]:
        cleaned_lists: dict[str, list[str]] = {}
        if not value:
            raise ValueError(f"{info.field_name} must define at least one named list.")
        for name, words in value.items():
            normalized_name = name.strip()
            normalized_words = [word.strip().lower() for word in words if word.strip()]
            if not normalized_name:
                raise ValueError(f"{info.field_name} names must not be empty.")
            if not normalized_words:
                raise ValueError(f"{info.field_name} '{normalized_name}' must contain at least one term.")
            cleaned_lists[normalized_name] = normalized_words
        return cleaned_lists

    @field_validator("context_window_tokens")
    @classmethod
    def validate_context_window_tokens(cls, value: int) -> int:
        if value < 1:
            raise ValueError("analysis.context_window_tokens must be at least 1.")
        return value

    @field_validator("parser_model")
    @classmethod
    def validate_parser_model(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("analysis.parser_model must not be empty.")
        return cleaned


class WefeExperimentConfig(BaseModel):
    metric: str = "WEAT"
    description: str | None = None
    target_sets: list[str]
    attribute_sets: list[str]

    @field_validator("metric")
    @classmethod
    def validate_metric(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("WEFE experiment metric must not be empty.")
        return cleaned

    @field_validator("target_sets", "attribute_sets")
    @classmethod
    def validate_set_references(cls, value: list[str], info: ValidationInfo) -> list[str]:
        cleaned = [item.strip() for item in value if item.strip()]
        if not cleaned:
            raise ValueError(f"{info.field_name} must contain at least one word set reference.")
        return cleaned


class WefeConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    word_sets: dict[str, list[str]] = Field(default_factory=dict)
    experiments: dict[str, WefeExperimentConfig] = Field(default_factory=dict)

    @field_validator("word_sets")
    @classmethod
    def validate_word_sets(cls, value: dict[str, list[str]]) -> dict[str, list[str]]:
        cleaned_word_sets: dict[str, list[str]] = {}
        for name, words in value.items():
            normalized_name = name.strip()
            normalized_words = [word.strip() for word in words if word.strip()]
            if not normalized_name:
                raise ValueError("WEFE word set names must not be empty.")
            if not normalized_words:
                raise ValueError(f"WEFE word set '{normalized_name}' must contain at least one word.")
            cleaned_word_sets[normalized_name] = normalized_words
        return cleaned_word_sets

    @model_validator(mode="after")
    def validate_experiment_references(self) -> "WefeConfig":
        if not self.word_sets:
            raise ValueError("wefe.word_sets must define at least one named word set.")
        if not self.experiments:
            raise ValueError("wefe.experiments must define at least one named experiment.")

        available = set(self.word_sets)
        missing_references: list[str] = []

        for experiment_name, experiment in self.experiments.items():
            for ref_name in experiment.target_sets + experiment.attribute_sets:
                if ref_name not in available:
                    missing_references.append(f"{experiment_name}:{ref_name}")

        if missing_references:
            missing_display = ", ".join(sorted(missing_references))
            raise ValueError(
                "WEFE experiments reference undefined word sets: "
                f"{missing_display}. Define them under wefe.word_sets."
            )
        return self


class ProjectConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    project: ProjectSection
    corpus: CorpusConfig
    metadata: MetadataConfig = Field(default_factory=MetadataConfig)
    preprocessing: PreprocessingConfig = Field(default_factory=PreprocessingConfig)
    embeddings: EmbeddingsConfig
    output: OutputConfig
    analysis: RepresentationAnalysisConfig
    wefe: WefeConfig

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ProjectConfig":
        config_path = Path(path)
        with config_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        return cls.model_validate(data)
