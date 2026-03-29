from pathlib import Path

from typer.testing import CliRunner

from wefe_news_analysis.cli import app
from wefe_news_analysis.config import ProjectConfig
from wefe_news_analysis.representation import analyze_article_text, analyze_representation


def valid_config_yaml(base_dir: Path) -> str:
    return "\n".join(
        [
            "project:",
            '  name: "demo"',
            "corpus:",
            f'  raw_pdf_dir: "{base_dir / "raw" / "pdfs"}"',
            f'  processed_text_dir: "{base_dir / "processed" / "text"}"',
            '  article_glob: "*.pdf"',
            '  language: "german"',
            '  default_encoding: "utf-8"',
            "metadata:",
            f'  sidecar_csv_path: "{base_dir / "raw" / "article_metadata.csv"}"',
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
            f'  path: "{base_dir / "models" / "embeddings.kv"}"',
            '  format: "keyedvectors"',
            "  binary: false",
            '  model_name: "demo-model"',
            "output:",
            f'  manifest_path: "{base_dir / "processed" / "articles_manifest.csv"}"',
            f'  reports_dir: "{base_dir / "reports"}"',
            "analysis:",
            "  target_groups:",
            '    migration_groups: ["migrant", "migranten", "flüchtling", "flüchtlinge", "geflüchtete"]',
            "  framing_lexicons:",
            '    dehumanizing: ["flut", "parasiten", "plage"]',
            '    criminalizing: ["kriminell", "illegal", "bedrohung"]',
            '    humanizing: ["familie", "gemeinschaft", "mensch"]',
            "  context_window_tokens: 5",
            "  outputs:",
            f'    sentence_features_path: "{base_dir / "reports" / "sentence_features.csv"}"',
            f'    article_group_features_path: "{base_dir / "reports" / "article_group_features.csv"}"',
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


def test_analyze_article_text_detects_group_framing() -> None:
    base_dir = Path("/tmp/demo")
    config_path = base_dir / "project.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(valid_config_yaml(base_dir), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    features = analyze_article_text(
        "article_1",
        "Migranten wurden nach einer Flut von Gerüchten verhaftet. Migranten organisierten eine Gemeinschaftsküche.",
        config,
    )

    assert len(features) == 2
    assert any(feature.passive_voice == 1 for feature in features)
    assert any(feature.active_voice == 1 for feature in features)
    assert any(feature.lexicon_counts["dehumanizing"] >= 1 for feature in features)
    assert any(feature.lexicon_counts["humanizing"] >= 1 for feature in features)


def test_analyze_representation_exports_csvs(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)

    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text(
        "Migranten wurden nach einer Flut von Gerüchten verhaftet. Migranten organisierten eine Gemeinschaftsküche.",
        encoding="utf-8",
    )
    config.metadata.sidecar_csv_path.parent.mkdir(parents=True, exist_ok=True)
    config.metadata.sidecar_csv_path.write_text(
        "article_id,source\narticle_1,Daily News\n",
        encoding="utf-8",
    )

    sentence_path, article_group_path = analyze_representation(config)

    assert sentence_path.exists()
    assert article_group_path.exists()
    assert "Daily News" in article_group_path.read_text(encoding="utf-8")
    assert "dehumanizing_count" in article_group_path.read_text(encoding="utf-8")


def test_analyze_representation_cli_exports_reports(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_2.txt").write_text(
        "Geflüchtete organisierten Unterstützung und die Gemeinschaft reagierte.",
        encoding="utf-8",
    )

    runner = CliRunner()
    result = runner.invoke(app, ["analyze-representation", "--config", str(config_path)])

    assert result.exit_code == 0
    assert config.analysis.outputs.sentence_features_path.exists()
    assert config.analysis.outputs.article_group_features_path.exists()
