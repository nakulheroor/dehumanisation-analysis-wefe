#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys

from article_analysis.codex_runner import analyze_with_codex
from article_analysis.fetchers import ArticleFetchError, build_fetcher
from article_analysis.rubric import load_rubric, rubric_prompt, rubric_to_schema

DEFAULT_CODEX_MODEL = "gpt-5.4-mini"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download an online article, analyze it with Codex, and output rubric JSON."
    )
    parser.add_argument("source", help="Online article URL or other source identifier.")
    parser.add_argument(
        "--source-kind",
        default="url",
        help="Source adapter to use. Defaults to 'url'.",
    )
    parser.add_argument(
        "--rubric",
        default="rubric.md",
        help="Path to the rubric markdown file.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_CODEX_MODEL,
        help=f"Codex model to use for analysis. Defaults to '{DEFAULT_CODEX_MODEL}'.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    fetcher = build_fetcher(args.source_kind)
    try:
        article = fetcher.fetch(args.source)
    except ArticleFetchError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    rubric = load_rubric(args.rubric)
    prompt = rubric_prompt(rubric)
    schema = rubric_to_schema(rubric)

    result = analyze_with_codex(
        article_title=article.title,
        article_url=article.source_url,
        article_text=article.text,
        prompt=prompt,
        schema=schema,
        model=args.model,
    )
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
