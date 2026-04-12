from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from .config import ProjectConfig
from .pipeline import build_manifest, ingest_corpus
from .representation import analyze_representation
from .wefe_runner import (
    build_query,
    export_wefe_results,
    inspect_experiment_vocabulary,
    run_all_wefe,
    train_embeddings,
)

app = typer.Typer(help="PDF-based newspaper text analysis scaffold for WEFE workflows.")
console = Console()


def load_config(config_path: Path) -> ProjectConfig:
    return ProjectConfig.from_yaml(config_path)


@app.command("ingest-corpus")
def ingest_corpus_command(config: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    project_config = load_config(config)
    written_files = ingest_corpus(project_config)
    console.print(
        f"Extracted {len(written_files)} article(s) into {project_config.corpus.processed_text_dir}"
    )


@app.command("build-manifest")
def build_manifest_command(config: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    project_config = load_config(config)
    manifest_path = build_manifest(project_config)
    console.print(f"Manifest written to {manifest_path}")


@app.command("analyze-representation")
def analyze_representation_command(
    config: Path = typer.Option(..., exists=True, dir_okay=False),
) -> None:
    project_config = load_config(config)
    sentence_path, article_group_path = analyze_representation(project_config)
    console.print(f"Sentence-level features written to {sentence_path}")
    console.print(f"Article/group features written to {article_group_path}")


@app.command("train-embeddings")
def train_embeddings_command(config: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    project_config = load_config(config)
    model_path = train_embeddings(project_config)
    console.print(f"Embeddings written to {model_path}")


@app.command("run-wefe")
def run_wefe_command(config: Path = typer.Option(..., exists=True, dir_okay=False)) -> None:
    project_config = load_config(config)
    results = run_all_wefe(project_config)
    output_path = export_wefe_results(project_config, results)
    console.print(f"WEFE results written to {output_path}")


@app.command("show-query")
def show_query_command(
    config: Path = typer.Option(..., exists=True, dir_okay=False),
    experiment: str | None = typer.Option(None, help="Named WEFE experiment to render."),
) -> None:
    project_config = load_config(config)
    query = build_query(project_config, experiment)
    console.print(query)


@app.command("inspect-vocab")
def inspect_vocab_command(
    config: Path = typer.Option(..., exists=True, dir_okay=False),
    experiment: str | None = typer.Option(None, help="Named WEFE experiment to inspect."),
) -> None:
    project_config = load_config(config)
    inspection = inspect_experiment_vocabulary(project_config, experiment)

    console.print(
        f"Experiment: {inspection['experiment_name']} | Embedding model: {inspection['embedding_model_name']}"
    )
    for report in inspection["set_reports"]:
        present_words = ", ".join(report["present_words"]) if report["present_words"] else "-"
        missing_words = ", ".join(report["missing_words"]) if report["missing_words"] else "-"
        console.print(
            f"[{report['set_name']}] present={len(report['present_words'])}/{report['total_words']} "
            f"missing={len(report['missing_words'])}/{report['total_words']} "
            f"missing_ratio={report['missing_ratio']:.2f}"
        )
        console.print(f"  present_words: {present_words}")
        console.print(f"  missing_words: {missing_words}")
        console.print(
            "  corpus_counts: "
            + ", ".join(
                f"{word}={count}" for word, count in report["corpus_counts"].items()
            )
        )


if __name__ == "__main__":
    app()
