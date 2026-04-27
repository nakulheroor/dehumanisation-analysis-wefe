from math import isnan
from pathlib import Path

import numpy as np
import pytest
from typer.testing import CliRunner

from wefe_news_analysis.cli import app
from wefe_news_analysis.config import ProjectConfig
from wefe_news_analysis.wefe_runner import (
    build_query,
    format_missing_words_summary,
    resolve_experiment_name,
    run_wefat,
    summarize_query_vocabulary,
)


def valid_config_yaml() -> str:
    return "\n".join(
        [
            "project:",
            '  name: "demo"',
            "corpus:",
            '  raw_pdf_dir: "data/raw/pdfs"',
            '  processed_text_dir: "data/processed/text"',
            '  article_glob: "*.pdf"',
            '  language: "german"',
            '  default_encoding: "utf-8"',
            "metadata:",
            '  sidecar_csv_path: "data/raw/article_metadata.csv"',
            '  id_column: "article_id"',
            "preprocessing:",
            "  normalize_unicode: true",
            "  lowercase: true",
            "  collapse_whitespace: true",
            "  strip_punctuation: false",
            "  strip_digits: false",
            "  min_token_length: 2",
            '  stopword_handling: "keep"',
            "  ocr_cleanup: true",
            "embeddings:",
            '  path: "models/embeddings.kv"',
            '  format: "keyedvectors"',
            "  binary: false",
            '  model_name: "demo-model"',
            "output:",
            '  manifest_path: "data/processed/articles_manifest.csv"',
            '  reports_dir: "reports"',
            "analysis:",
            "  target_groups:",
            '    migration_groups: ["migrant", "migranten", "flüchtlinge"]',
            "  framing_lexicons:",
            '    dehumanizing: ["flut", "parasiten"]',
            '    humanizing: ["mensch", "gemeinschaft"]',
            "  context_window_tokens: 8",
            '  parser_model: "de_core_news_sm"',
            "  outputs:",
            '    sentence_features_path: "reports/sentence_representation_features.csv"',
            '    article_group_features_path: "reports/article_group_representation_features.csv"',
            "wefe:",
            "  word_sets:",
            '    career_words: ["career", "executive"]',
            '    family_words: ["family", "home"]',
            '    male_terms: ["man", "male"]',
            '    female_terms: ["woman", "female"]',
            "  experiments:",
            "    gender_career_bias:",
            '      metric: "WEAT"',
            '      target_sets: ["career_words", "family_words"]',
            '      attribute_sets: ["male_terms", "female_terms"]',
        ]
    )


def test_build_query_resolves_named_experiment(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    query = build_query(config, "gender_career_bias")

    assert query.target_sets == [["career", "executive"], ["family", "home"]]
    assert query.attribute_sets == [["man", "male"], ["woman", "female"]]
    assert query.target_sets_names == ["career_words", "family_words"]


def test_resolve_experiment_name_requires_explicit_choice_when_multiple(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        valid_config_yaml()
        + "\n".join(
            [
                "",
                "    secondary_experiment:",
                '      metric: "WEAT"',
                '      target_sets: ["family_words", "career_words"]',
                '      attribute_sets: ["female_terms", "male_terms"]',
            ]
        ),
        encoding="utf-8",
    )
    config = ProjectConfig.from_yaml(config_path)

    with pytest.raises(ValueError, match="Multiple WEFE experiments"):
        resolve_experiment_name(config)


def test_show_query_cli_renders_named_experiment(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(), encoding="utf-8")

    runner = CliRunner()
    result = runner.invoke(app, ["show-query", "--config", str(config_path), "--experiment", "gender_career_bias"])

    assert result.exit_code == 0
    assert "career_words" in result.stdout
    assert "male_terms" in result.stdout


def test_summarize_query_vocabulary_reports_missing_words(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    query = build_query(config, "gender_career_bias")

    class FakeKeyedVectors:
        key_to_index = {
            "career": 0,
            "family": 1,
            "man": 2,
            "female": 3,
        }

    summary = summarize_query_vocabulary(query, FakeKeyedVectors())

    assert summary["career_words"]["missing_words"] == ["executive"]
    assert summary["family_words"]["missing_words"] == ["home"]
    assert summary["male_terms"]["missing_words"] == ["male"]
    assert summary["female_terms"]["missing_words"] == ["woman"]
    assert format_missing_words_summary(summary) == (
        "career_words=executive; family_words=home; male_terms=male; female_terms=woman"
    )


def wefat_config_yaml() -> str:
    return "\n".join(
        [
            "project:",
            '  name: "demo"',
            "corpus:",
            '  raw_pdf_dir: "data/raw/pdfs"',
            '  processed_text_dir: "data/processed/text"',
            '  article_glob: "*.pdf"',
            '  language: "german"',
            '  default_encoding: "utf-8"',
            "metadata:",
            '  sidecar_csv_path: "data/raw/article_metadata.csv"',
            '  id_column: "article_id"',
            "preprocessing:",
            "  normalize_unicode: true",
            "  lowercase: true",
            "  collapse_whitespace: true",
            "  strip_punctuation: false",
            "  strip_digits: false",
            "  min_token_length: 1",
            '  stopword_handling: "keep"',
            "  ocr_cleanup: true",
            "embeddings:",
            '  path: "models/embeddings.kv"',
            '  format: "keyedvectors"',
            "  binary: false",
            '  model_name: "demo-model"',
            "output:",
            '  manifest_path: "data/processed/articles_manifest.csv"',
            '  reports_dir: "reports"',
            "analysis:",
            "  target_groups:",
            '    palestinians: ["palästinenser", "gaza"]',
            "  framing_lexicons:",
            '    dehumanizing: ["flut"]',
            '    humanizing: ["mensch"]',
            "  context_window_tokens: 5",
            '  parser_model: "de_core_news_sm"',
            "  outputs:",
            '    sentence_features_path: "reports/sentence_representation_features.csv"',
            '    article_group_features_path: "reports/article_group_representation_features.csv"',
            "wefe:",
            "  word_sets:",
            '    target_group: ["palästinenser", "gaza"]',
            '    negative_attrs: ["flut", "parasiten"]',
            '    positive_attrs: ["mensch", "gemeinschaft"]',
            "  experiments:",
            "    wefat_test:",
            '      metric: "WEFAT"',
            '      target_sets: ["target_group"]',
            '      attribute_sets: ["negative_attrs", "positive_attrs"]',
        ]
    )


class FakeKeyedVectorsWefat:
    """KeyedVectors stub with controllable unit vectors for WEFAT testing."""

    def __init__(self) -> None:
        dim = 4
        self._vecs: dict[str, np.ndarray] = {
            "palästinenser": np.array([1.0, 0.0, 0.0, 0.0]),
            "gaza": np.array([1.0, 0.0, 0.0, 0.0]),
            "flut": np.array([1.0, 0.0, 0.0, 0.0]),
            "parasiten": np.array([1.0, 0.0, 0.0, 0.0]),
            "mensch": np.array([0.0, 1.0, 0.0, 0.0]),
            "gemeinschaft": np.array([0.0, 1.0, 0.0, 0.0]),
        }
        self.key_to_index = {k: i for i, k in enumerate(self._vecs)}

    def __getitem__(self, key: str) -> np.ndarray:
        return self._vecs[key]


def test_run_wefat_returns_positive_score_when_target_aligned_with_attr1(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(wefat_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    kv = FakeKeyedVectorsWefat()
    result = run_wefat(config, "wefat_test", kv)

    assert result["metric"] == "WEFAT"
    assert result["experiment_name"] == "wefat_test"
    assert result["result"] > 0, "Target words aligned with negative_attrs should give positive WEFAT score"
    assert not isnan(result["effect_size"])


def test_run_wefat_returns_nan_when_target_words_absent(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(wefat_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    class EmptyVocab:
        key_to_index: dict = {}

        def __getitem__(self, key: str) -> np.ndarray:  # pragma: no cover
            raise KeyError(key)

    result = run_wefat(config, "wefat_test", EmptyVocab())

    assert isnan(result["result"])
    assert isnan(result["effect_size"])


def test_run_wefat_query_name_matches_single_target_set(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(wefat_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    kv = FakeKeyedVectorsWefat()
    result = run_wefat(config, "wefat_test", kv)

    assert "target_group" in result["query_name"]
    assert "negative_attrs" in result["query_name"]
    assert "positive_attrs" in result["query_name"]


def test_inspect_vocab_cli_renders_missing_words(monkeypatch, tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    processed_dir = tmp_path / "data" / "processed" / "text"
    processed_dir.mkdir(parents=True, exist_ok=True)
    (processed_dir / "article_1.txt").write_text("career family man female career", encoding="utf-8")
    config_path.write_text(valid_config_yaml(), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir = processed_dir

    class FakeKeyedVectors:
        key_to_index = {
            "career": 0,
            "family": 1,
            "man": 2,
            "female": 3,
        }

    monkeypatch.setattr("wefe_news_analysis.cli.load_config", lambda _: config)
    monkeypatch.setattr("wefe_news_analysis.wefe_runner.load_embeddings", lambda _: FakeKeyedVectors())

    runner = CliRunner()
    result = runner.invoke(app, ["inspect-vocab", "--config", str(config_path), "--experiment", "gender_career_bias"])

    assert result.exit_code == 0
    assert "career_words" in result.stdout
    assert "missing_words: executive" in result.stdout
    assert "corpus_counts: career=2, executive=0" in result.stdout
