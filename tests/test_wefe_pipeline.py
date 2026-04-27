from pathlib import Path

import wefe_news_analysis.wefe_runner as wefe_runner
from wefe_news_analysis.config import ProjectConfig
from wefe_news_analysis.wefe_runner import export_wefe_results, load_embeddings, run_all_wefe, run_wefe, train_embeddings


def valid_config_yaml(base_dir: Path, include_wefat: bool = False) -> str:
    lines = [
        "project:",
        '  name: "demo"',
        "corpus:",
        f'  raw_pdf_dir: "{base_dir / "raw" / "pdfs"}"',
        f'  raw_text_dir: "{base_dir / "raw" / "text"}"',
        f'  processed_text_dir: "{base_dir / "processed" / "text"}"',
        '  article_glob: "*.pdf"',
        '  text_glob: "*.txt"',
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
        "  vector_size: 20",
        "  window: 2",
        "  min_count: 1",
        "  epochs: 5",
        "  sg: 1",
        "output:",
        f'  manifest_path: "{base_dir / "processed" / "articles_manifest.csv"}"',
        f'  reports_dir: "{base_dir / "reports"}"',
        "analysis:",
        "  target_groups:",
        '    migration_groups: ["migranten"]',
        "  framing_lexicons:",
        '    dehumanizing: ["flut"]',
        '    humanizing: ["gemeinschaft"]',
        "  context_window_tokens: 5",
        '  parser_model: "de_core_news_sm"',
        "  outputs:",
        f'    sentence_features_path: "{base_dir / "reports" / "sentence_features.csv"}"',
        f'    article_group_features_path: "{base_dir / "reports" / "article_group_features.csv"}"',
        "wefe:",
        "  word_sets:",
        '    migration_groups: ["migranten", "geflüchtete"]',
        '    humanizing_terms: ["gemeinschaft", "familie"]',
        '    dehumanizing_terms: ["flut", "invasion"]',
        "  experiments:",
        "    migration_dehumanization:",
        '      metric: "WEAT"',
        '      target_sets: ["migration_groups", "migration_groups"]',
        '      attribute_sets: ["dehumanizing_terms", "humanizing_terms"]',
    ]
    if include_wefat:
        lines += [
            "    migration_dehumanization_absolute:",
            '      metric: "WEFAT"',
            '      target_sets: ["migration_groups"]',
            '      attribute_sets: ["dehumanizing_terms", "humanizing_terms"]',
        ]
    return "\n".join(lines)


def test_train_embeddings_and_load_keyed_vectors(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text(
        "migranten gemeinschaft familie flut",
        encoding="utf-8",
    )

    model_path = train_embeddings(config)
    keyed_vectors = load_embeddings(config)

    assert model_path.exists()
    assert keyed_vectors.vector_size == 20
    assert "migranten" in keyed_vectors.key_to_index


def test_run_all_wefe_and_export_results(monkeypatch, tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text(
        "migranten gemeinschaft familie flut invasion",
        encoding="utf-8",
    )
    train_embeddings(config)

    class FakeMetric:
        def run_query(self, query, model, return_effect_size=True, **kwargs):
            return {
                "query_name": "migration_dehumanization",
                "result": 0.42,
                "weat": 0.42,
                "effect_size": 0.84,
            }

    monkeypatch.setattr(wefe_runner, "metric_factory", lambda: FakeMetric())

    results = run_all_wefe(config)
    output_path = export_wefe_results(config, results)

    assert len(results) == 1
    assert results[0]["experiment_name"] == "migration_dehumanization"
    assert output_path.exists()
    assert "effect_size" in output_path.read_text(encoding="utf-8")


def test_run_all_wefe_handles_mixed_weat_and_wefat(monkeypatch, tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path, include_wefat=True), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text(
        "migranten gemeinschaft familie flut invasion migranten flut",
        encoding="utf-8",
    )
    train_embeddings(config)

    class FakeMetric:
        def run_query(self, query, model, return_effect_size=True, **kwargs):
            return {"query_name": "test", "result": 0.5, "weat": 0.5, "effect_size": 1.0}

    monkeypatch.setattr(wefe_runner, "metric_factory", lambda: FakeMetric())

    results = run_all_wefe(config)

    assert len(results) == 2
    metrics = {r["experiment_name"]: r["metric"] for r in results}
    assert metrics["migration_dehumanization"] == "WEAT"
    assert metrics["migration_dehumanization_absolute"] == "WEFAT"


def test_run_wefe_wefat_uses_real_embeddings(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(tmp_path, include_wefat=True), encoding="utf-8")
    config = ProjectConfig.from_yaml(config_path)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text(
        "migranten gemeinschaft familie flut invasion migranten flut migranten",
        encoding="utf-8",
    )
    train_embeddings(config)

    result = run_wefe(config, "migration_dehumanization_absolute")

    assert result["metric"] == "WEFAT"
    assert "wefat_score" in result
    assert isinstance(result["result"], float)
