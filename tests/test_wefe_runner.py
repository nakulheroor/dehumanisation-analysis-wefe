from pathlib import Path

import pytest
from typer.testing import CliRunner

from wefe_news_analysis.cli import app
from wefe_news_analysis.config import ProjectConfig
from wefe_news_analysis.wefe_runner import (
    build_query,
    format_missing_words_summary,
    resolve_experiment_name,
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
