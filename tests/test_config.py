from pathlib import Path

import pytest
from pydantic import ValidationError

from wefe_news_analysis.config import ProjectConfig


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
            '      description: "demo experiment"',
            '      target_sets: ["career_words", "family_words"]',
            '      attribute_sets: ["male_terms", "female_terms"]',
        ]
    )


def test_project_config_from_yaml(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml(), encoding="utf-8")

    config = ProjectConfig.from_yaml(config_path)

    assert config.project.name == "demo"
    assert config.corpus.language == "german"
    assert config.metadata.sidecar_csv_path == Path("data/raw/article_metadata.csv")
    assert config.embeddings.model_name == "demo-model"
    assert "migration_groups" in config.analysis.target_groups
    assert "gender_career_bias" in config.wefe.experiments


def test_project_example_yaml_is_valid() -> None:
    config = ProjectConfig.from_yaml(Path("configs/project.example.yaml"))

    assert "migration_groups" not in config.wefe.word_sets
    assert "roma_people" not in config.wefe.word_sets
    assert "general_journalists" in config.wefe.word_sets
    assert "journalist_disinformation" in config.wefe.experiments


def test_project_config_requires_corpus_language(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml().replace('  language: "german"\n', ""), encoding="utf-8")

    with pytest.raises(ValidationError, match="language"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_requires_embedding_path(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml().replace('  path: "models/embeddings.kv"\n', ""), encoding="utf-8")

    with pytest.raises(ValidationError, match="path"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_rejects_undefined_word_set_reference(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        valid_config_yaml().replace('["career_words", "family_words"]', '["career_words", "unknown_words"]'),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="undefined word sets"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_rejects_invalid_weat_cardinality(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        valid_config_yaml().replace('["career_words", "family_words"]', '["career_words"]'),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="WEAT experiments must define exactly 2 target_sets"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_rejects_blank_metadata_id_column(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(valid_config_yaml().replace('  id_column: "article_id"', '  id_column: ""'), encoding="utf-8")

    with pytest.raises(ValidationError, match="metadata.id_column"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_requires_analysis_target_groups(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        valid_config_yaml().replace(
            '    migration_groups: ["migrant", "migranten", "flüchtlinge"]\n', ""
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="target_groups"):
        ProjectConfig.from_yaml(config_path)


def wefat_config_yaml() -> str:
    """Minimal valid config with one WEFAT experiment."""
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
            '    palestinians: ["palästinenser", "gaza"]',
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
            '    palestinians: ["palästinenser", "gaza"]',
            '    dehumanizing_terms: ["flut", "parasiten"]',
            '    humanizing_terms: ["mensch", "gemeinschaft"]',
            "  experiments:",
            "    wefat_test:",
            '      metric: "WEFAT"',
            '      target_sets: ["palestinians"]',
            '      attribute_sets: ["dehumanizing_terms", "humanizing_terms"]',
        ]
    )


def test_wefat_config_parses_and_validates(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(wefat_config_yaml(), encoding="utf-8")

    config = ProjectConfig.from_yaml(config_path)

    exp = config.wefe.experiments["wefat_test"]
    assert exp.metric == "WEFAT"
    assert exp.target_sets == ["palestinians"]
    assert len(exp.attribute_sets) == 2


def test_wefat_config_rejects_two_target_sets(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        wefat_config_yaml().replace(
            '      target_sets: ["palestinians"]',
            '      target_sets: ["palestinians", "dehumanizing_terms"]',
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="WEFAT experiments must define exactly 1 target_set"):
        ProjectConfig.from_yaml(config_path)


def test_wefat_config_rejects_one_attribute_set(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        wefat_config_yaml().replace(
            '      attribute_sets: ["dehumanizing_terms", "humanizing_terms"]',
            '      attribute_sets: ["dehumanizing_terms"]',
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="WEFAT experiments must define exactly 2 attribute_sets"):
        ProjectConfig.from_yaml(config_path)


def test_project_config_rejects_unsupported_metric(tmp_path: Path) -> None:
    config_path = tmp_path / "project.yaml"
    config_path.write_text(
        wefat_config_yaml().replace('      metric: "WEFAT"', '      metric: "UNKNOWN_METRIC"'),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="Unsupported metric"):
        ProjectConfig.from_yaml(config_path)


def test_project_yaml_has_israelis_word_set() -> None:
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "israelis" in config.wefe.word_sets
    assert len(config.wefe.word_sets["israelis"]) >= 4


def test_project_yaml_has_wefat_experiments() -> None:
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    wefat_experiments = [name for name, exp in config.wefe.experiments.items() if exp.metric == "WEFAT"]
    assert len(wefat_experiments) >= 5
    assert "wefat_palestinians_dehumanization_absolute" in wefat_experiments
    assert "wefat_palestinian_journalists_violence_absolute" in wefat_experiments


def test_project_yaml_covers_all_special_rapporteur_question_areas() -> None:
    """Verify the config covers all 5 research areas from the Special Rapporteur's call."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))
    exp_names = set(config.wefe.experiments.keys())

    # 1. Targeting and repression of Palestinian journalists
    assert any("journalist" in n and "violence" in n for n in exp_names)
    assert any("detention" in n for n in exp_names)
    assert any("harassment" in n for n in exp_names)
    assert any("family" in n for n in exp_names)
    assert any("exclusion" in n or "blackout" in n for n in exp_names)

    # 2. Dehumanization and narrative practices
    assert any("dehumanization" in n for n in exp_names)
    assert any("civilian_erasure" in n for n in exp_names)
    assert any("displacement" in n for n in exp_names)

    # 3. Incitement and genocide
    assert any("genocide" in n for n in exp_names)
    assert any("coded" in n for n in exp_names)

    # 4. Censorship and retaliation
    assert any("censorship" in n for n in exp_names)

    # 5. Disinformation against journalists
    assert any("disinformation" in n for n in exp_names)


# ---------------------------------------------------------------------------
# Tests for the new WEAT-AS (Additional Scenarios) experiments
# ---------------------------------------------------------------------------


def test_project_yaml_has_conviction_accusation_word_sets() -> None:
    """Conviction and guilt vocabulary must be present for journalist framing tests."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "conviction_accusation_terms" in config.wefe.word_sets
    assert "innocence_protection_terms" in config.wefe.word_sets
    # Core accusation terms derived from SZ corpus
    assert "schuldig" in config.wefe.word_sets["conviction_accusation_terms"]
    assert "verdacht" in config.wefe.word_sets["conviction_accusation_terms"]
    assert "angeklagt" in config.wefe.word_sets["conviction_accusation_terms"]
    assert "unschuldig" in config.wefe.word_sets["innocence_protection_terms"]


def test_project_yaml_has_hamas_organization_word_set() -> None:
    """Hamas/terrorist-organisation vocabulary must be present for Hamas-association test."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "hamas_organization_terms" in config.wefe.word_sets
    assert "hamas" in config.wefe.word_sets["hamas_organization_terms"]
    assert "islamist" in config.wefe.word_sets["hamas_organization_terms"]
    assert len(config.wefe.word_sets["hamas_organization_terms"]) >= 8


def test_project_yaml_has_death_agency_word_sets() -> None:
    """Passive and active death vocabulary must be present for death-language asymmetry test."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "passive_death_terms" in config.wefe.word_sets
    assert "active_murder_terms" in config.wefe.word_sets
    # Passive: agentless death vocabulary used for Palestinian casualties in SZ
    assert "gestorben" in config.wefe.word_sets["passive_death_terms"]
    assert "starben" in config.wefe.word_sets["passive_death_terms"]
    # Active: direct murder vocabulary used for October 7 Israeli victims
    assert "ermordet" in config.wefe.word_sets["active_murder_terms"]
    assert "massaker" in config.wefe.word_sets["active_murder_terms"]


def test_project_yaml_has_victim_humanization_word_sets() -> None:
    """Sympathetic and statistical vocabulary must be present for victim-humanization test."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "sympathetic_victim_terms" in config.wefe.word_sets
    assert "statistical_aggregate_terms" in config.wefe.word_sets
    assert "trauer" in config.wefe.word_sets["sympathetic_victim_terms"]
    assert "geisel" in config.wefe.word_sets["sympathetic_victim_terms"]
    assert "zahlen" in config.wefe.word_sets["statistical_aggregate_terms"]


def test_project_yaml_has_dehumanizing_aggressive_word_sets() -> None:
    """Dehumanizing/aggressive and humanizing child/civilian vocabulary must be present."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "dehumanizing_aggressive_terms" in config.wefe.word_sets
    assert "humanizing_child_civilian_terms" in config.wefe.word_sets
    assert "barbarisch" in config.wefe.word_sets["dehumanizing_aggressive_terms"]
    assert "bestialisch" in config.wefe.word_sets["dehumanizing_aggressive_terms"]
    assert "kind" in config.wefe.word_sets["humanizing_child_civilian_terms"]
    assert "kinder" in config.wefe.word_sets["humanizing_child_civilian_terms"]
    assert "minderjähriger" in config.wefe.word_sets["humanizing_child_civilian_terms"]


def test_project_yaml_has_journalist_conviction_experiment() -> None:
    """Palestinian journalists must be tested against conviction/guilt vocabulary."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "journalist_conviction_association" in config.wefe.experiments
    exp = config.wefe.experiments["journalist_conviction_association"]
    assert exp.metric == "WEAT"
    assert "palestinian_journalists" in exp.target_sets
    assert "general_journalists" in exp.target_sets
    assert "conviction_accusation_terms" in exp.attribute_sets
    assert "innocence_protection_terms" in exp.attribute_sets


def test_project_yaml_has_journalist_hamas_experiment() -> None:
    """Palestinian journalists must be tested against Hamas-organisation vocabulary."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "journalist_hamas_association" in config.wefe.experiments
    exp = config.wefe.experiments["journalist_hamas_association"]
    assert exp.metric == "WEAT"
    assert "palestinian_journalists" in exp.target_sets
    assert "hamas_organization_terms" in exp.attribute_sets
    assert "press_freedom_terms" in exp.attribute_sets


def test_project_yaml_has_death_language_agency_experiment() -> None:
    """Death-language agency asymmetry must compare Palestinians vs. Israelis."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "death_language_agency_asymmetry" in config.wefe.experiments
    exp = config.wefe.experiments["death_language_agency_asymmetry"]
    assert exp.metric == "WEAT"
    assert "palestinians" in exp.target_sets
    assert "israelis" in exp.target_sets
    assert "passive_death_terms" in exp.attribute_sets
    assert "active_murder_terms" in exp.attribute_sets


def test_project_yaml_has_victim_humanization_experiment() -> None:
    """Victim humanization test must compare Israelis vs. Palestinians."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "victim_humanization_sympathy_asymmetry" in config.wefe.experiments
    exp = config.wefe.experiments["victim_humanization_sympathy_asymmetry"]
    assert exp.metric == "WEAT"
    assert "israelis" in exp.target_sets
    assert "palestinians" in exp.target_sets
    assert "sympathetic_victim_terms" in exp.attribute_sets
    assert "statistical_aggregate_terms" in exp.attribute_sets


def test_project_yaml_has_civilian_dehumanization_experiment() -> None:
    """Civilian dehumanization test must compare Palestinians vs. Israelis."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "civilian_dehumanization_asymmetry" in config.wefe.experiments
    exp = config.wefe.experiments["civilian_dehumanization_asymmetry"]
    assert exp.metric == "WEAT"
    assert "palestinians" in exp.target_sets
    assert "israelis" in exp.target_sets
    assert "dehumanizing_aggressive_terms" in exp.attribute_sets
    assert "humanizing_child_civilian_terms" in exp.attribute_sets


def test_project_yaml_has_journalist_dehumanization_experiment() -> None:
    """Journalist dehumanization test must compare Palestinian vs. general journalists."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))

    assert "journalist_dehumanization_asymmetry" in config.wefe.experiments
    exp = config.wefe.experiments["journalist_dehumanization_asymmetry"]
    assert exp.metric == "WEAT"
    assert "palestinian_journalists" in exp.target_sets
    assert "general_journalists" in exp.target_sets
    assert "dehumanizing_aggressive_terms" in exp.attribute_sets


def test_project_yaml_covers_all_new_research_hypotheses() -> None:
    """All five new WEAT-AS hypotheses must be represented as experiments."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))
    exp_names = set(config.wefe.experiments.keys())

    # H1: Palestinian journalists embedded in conviction/guilt discourse
    assert "journalist_conviction_association" in exp_names

    # H2: Palestinian journalists associated with Hamas/terrorist organisations
    assert "journalist_hamas_association" in exp_names

    # H3: Palestinian deaths described with passive vocabulary; Israeli deaths with active murder terms
    assert "death_language_agency_asymmetry" in exp_names

    # H4: Israeli victims receive sympathetic/humanising framing; Palestinian deaths treated statistically
    assert "victim_humanization_sympathy_asymmetry" in exp_names

    # H5: Dehumanising/aggressive vocabulary more associated with Palestinians than Israelis
    assert "civilian_dehumanization_asymmetry" in exp_names
    assert "journalist_dehumanization_asymmetry" in exp_names


def test_new_experiments_all_have_descriptions() -> None:
    """All new WEAT-AS experiments must carry a non-empty description."""
    config = ProjectConfig.from_yaml(Path("configs/project.yaml"))
    new_experiments = [
        "journalist_conviction_association",
        "journalist_hamas_association",
        "death_language_agency_asymmetry",
        "victim_humanization_sympathy_asymmetry",
        "civilian_dehumanization_asymmetry",
        "journalist_dehumanization_asymmetry",
    ]
    for name in new_experiments:
        exp = config.wefe.experiments[name]
        assert exp.description, f"Experiment '{name}' is missing a description"
        assert len(exp.description) > 20, f"Experiment '{name}' description is too short"
