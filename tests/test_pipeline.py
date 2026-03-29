from pathlib import Path

from wefe_news_analysis.config import (
    AnalysisOutputConfig,
    CorpusConfig,
    EmbeddingsConfig,
    MetadataConfig,
    OutputConfig,
    PreprocessingConfig,
    ProjectConfig,
    ProjectSection,
    RepresentationAnalysisConfig,
    WefeConfig,
    WefeExperimentConfig,
)
from wefe_news_analysis.pipeline import build_manifest, ensure_directories, preprocess_text


def make_config(tmp_path: Path, sidecar_csv_path: Path | None = None) -> ProjectConfig:
    return ProjectConfig(
        project=ProjectSection(name="demo"),
        corpus=CorpusConfig(
            raw_pdf_dir=tmp_path / "raw" / "pdfs",
            processed_text_dir=tmp_path / "processed" / "text",
            article_glob="*.pdf",
            language="german",
            default_encoding="utf-8",
        ),
        metadata=MetadataConfig(sidecar_csv_path=sidecar_csv_path, id_column="article_id"),
        preprocessing=PreprocessingConfig(
            normalize_unicode=True,
            lowercase=True,
            collapse_whitespace=True,
            strip_punctuation=True,
            strip_digits=True,
            min_token_length=3,
            stopword_handling="remove",
            ocr_cleanup=True,
        ),
        embeddings=EmbeddingsConfig(
            path=tmp_path / "models" / "embeddings.kv",
            format="keyedvectors",
            binary=False,
            model_name="demo-model",
        ),
        output=OutputConfig(
            manifest_path=tmp_path / "processed" / "articles_manifest.csv",
            reports_dir=tmp_path / "reports",
        ),
        analysis=RepresentationAnalysisConfig(
            target_groups={"migrant_groups": ["migrant", "migranten", "flüchtlinge"]},
            framing_lexicons={
                "dehumanizing": ["flut", "parasiten"],
                "humanizing": ["mensch", "gemeinschaft"],
            },
            context_window_tokens=5,
            outputs=AnalysisOutputConfig(
                sentence_features_path=tmp_path / "reports" / "sentence_features.csv",
                article_group_features_path=tmp_path / "reports" / "article_group_features.csv",
            ),
        ),
        wefe=WefeConfig(
            word_sets={
                "career_words": ["career", "executive"],
                "family_words": ["family", "home"],
                "male_terms": ["man", "male"],
                "female_terms": ["woman", "female"],
            },
            experiments={
                "gender_career_bias": WefeExperimentConfig(
                    metric="WEAT",
                    target_sets=["career_words", "family_words"],
                    attribute_sets=["male_terms", "female_terms"],
                )
            },
        ),
    )


def test_build_manifest_writes_csv_and_merges_metadata(tmp_path: Path) -> None:
    sidecar_path = tmp_path / "raw" / "article_metadata.csv"
    config = make_config(tmp_path, sidecar_path)
    ensure_directories(config)
    config.corpus.processed_text_dir.mkdir(parents=True, exist_ok=True)
    (config.corpus.processed_text_dir / "article_1.txt").write_text("hello world", encoding="utf-8")
    sidecar_path.write_text(
        "article_id,source,publication_date\narticle_1,Daily News,2026-03-29\n",
        encoding="utf-8",
    )

    result = build_manifest(config)

    manifest_text = result.read_text(encoding="utf-8")
    assert result == config.output.manifest_path
    assert result.exists()
    assert "article_1" in manifest_text
    assert "Daily News" in manifest_text


def test_preprocess_text_applies_configured_cleanup(tmp_path: Path) -> None:
    config = make_config(tmp_path)

    processed = preprocess_text("Die 2026 ﬁnan-\nzen und das haus!", config)

    assert processed == "finanzen haus"
