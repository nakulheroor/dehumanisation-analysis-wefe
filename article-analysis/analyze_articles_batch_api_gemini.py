#!/usr/bin/env python3
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from threading import Lock
import sys
import time
from datetime import datetime
from pathlib import Path

from article_analysis.fetchers import ArticleFetchError, build_fetcher
from article_analysis.gemini_runner import (
    DEFAULT_GEMINI_MODEL,
    analyze_with_gemini_api,
)
from article_analysis.rubric_gemini import load_rubric, rubric_prompt, rubric_to_schema


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Gemini article analysis over many local text files in configurable batches."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing source .txt article files.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where analysis .json files will be written.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=250,
        help="Maximum number of articles to process in this run. Defaults to 250.",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=0,
        help="Start at this index within the sorted input file list. Defaults to 0.",
    )
    parser.add_argument(
        "--end-index",
        type=int,
        default=None,
        help="Optional exclusive end index within the sorted input file list.",
    )
    parser.add_argument(
        "--rubric",
        default=None,
        help="Optional path to the rubric markdown file. Overrides --snippets.",
    )
    parser.add_argument(
        "--snippets",
        action="store_true",
        help="Use the snippet-enabled short rubric. Defaults to the no-snippets short rubric.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_GEMINI_MODEL,
        help="Gemini model override. Defaults to the Gemini runner default.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-run analysis even if the output JSON file already exists.",
    )
    parser.add_argument(
        "--error-log",
        default=None,
        help="Optional path for the batch error log. Defaults to <output-dir>/batch_errors.log.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of parallel worker threads for API requests. Defaults to 1.",
    )
    return parser.parse_args()


def resolve_rubric_path(args: argparse.Namespace) -> str:
    if args.rubric:
        return args.rubric
    if args.snippets:
        return "rubric_short.md"
    return "rubric_short_no_snippets.md"


def model_output_suffix(model: str) -> str:
    normalized = model.strip().lower().replace("_", "-").replace(" ", "-")
    if "3.1" in normalized and "flash" in normalized and "lite" in normalized:
        return "gemini_flash_lite_31"
    if "2.5" in normalized and "flash" in normalized and "lite" in normalized:
        return "gemini_flash_lite_25"

    safe = []
    for char in normalized:
        if char.isalnum():
            safe.append(char)
        else:
            safe.append("_")
    slug = "".join(safe).strip("_")
    while "__" in slug:
        slug = slug.replace("__", "_")
    return slug or "gemini_model"


def build_output_path(output_dir: Path, source_path: Path, model: str | None) -> Path:
    model_name = model or DEFAULT_GEMINI_MODEL
    return output_dir / f"{source_path.stem}_{model_output_suffix(model_name)}.json"


def format_seconds(seconds: float) -> str:
    total_seconds = max(0, int(round(seconds)))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def collect_input_files(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.iterdir() if path.is_file() and path.suffix == ".txt")


def choose_batch(
    files: list[Path],
    output_dir: Path,
    start_index: int,
    end_index: int | None,
    batch_size: int,
    overwrite: bool,
    model: str | None,
) -> tuple[list[tuple[int, Path]], int]:
    sliced_files = files[start_index:end_index]
    pending_files: list[tuple[int, Path]] = []
    skipped_existing = 0

    for relative_index, source_path in enumerate(sliced_files):
        output_path = build_output_path(output_dir, source_path, model)
        if output_path.exists() and not overwrite:
            skipped_existing += 1
            continue
        pending_files.append((start_index + relative_index, source_path))
        if len(pending_files) >= batch_size:
            break

    return pending_files, skipped_existing


def run_single_article(
    fetcher,
    source_path: Path,
    output_path: Path,
    prompt: str,
    schema: dict,
    model: str | None,
) -> tuple[bool, str | None, dict]:
    try:
        article = fetcher.fetch(str(source_path))
        result = analyze_with_gemini_api(
            article_title=article.title,
            article_url=article.source_url,
            article_text=article.text,
            prompt=prompt,
            schema=schema,
            model=model,
        )
    except (ArticleFetchError, RuntimeError) as exc:
        return False, str(exc), {}

    output_path.write_text(json.dumps(result.parsed_json, indent=2) + "\n", encoding="utf-8")
    usage_record = {
        "source_path": str(source_path),
        "output_path": str(output_path),
        "model": result.model or model,
        "usage": result.usage,
        "article_chars": len(article.text),
        "article_words": len(article.text.split()),
        "title": article.title,
    }
    return True, None, usage_record


def append_error(error_log_path: Path, source_path: Path, message: str) -> None:
    timestamp = datetime.now().isoformat(timespec="seconds")
    with error_log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {source_path}\n{message}\n\n")


def append_usage(usage_log_path: Path, usage_record: dict, lock: Lock) -> None:
    with lock:
        with usage_log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(usage_record, ensure_ascii=False) + "\n")


def main() -> int:
    try:
        from dotenv import load_dotenv
    except ImportError:
        load_dotenv = None

    if load_dotenv is not None:
        load_dotenv()

    args = parse_args()

    if args.batch_size <= 0:
        print("Error: --batch-size must be greater than 0.", file=sys.stderr)
        return 1
    if args.start_index < 0:
        print("Error: --start-index must be 0 or greater.", file=sys.stderr)
        return 1
    if args.end_index is not None and args.end_index < args.start_index:
        print("Error: --end-index must be greater than or equal to --start-index.", file=sys.stderr)
        return 1
    if args.workers <= 0:
        print("Error: --workers must be greater than 0.", file=sys.stderr)
        return 1

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    if not input_dir.is_dir():
        print(f"Error: input directory does not exist: {input_dir}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    error_log_path = Path(args.error_log) if args.error_log else output_dir / "batch_errors.log"
    usage_log_path = output_dir / "batch_usage.jsonl"
    fetcher = build_fetcher("text-file")
    rubric = load_rubric(resolve_rubric_path(args))
    prompt = rubric_prompt(rubric)
    schema = rubric_to_schema(rubric)

    all_files = collect_input_files(input_dir)
    if not all_files:
        print(f"No .txt files found in {input_dir}")
        return 0

    batch_files, skipped_existing = choose_batch(
        files=all_files,
        output_dir=output_dir,
        start_index=args.start_index,
        end_index=args.end_index,
        batch_size=args.batch_size,
        overwrite=args.overwrite,
        model=args.model,
    )
    total_candidates = len(all_files[args.start_index : args.end_index])

    if not batch_files:
        print("No articles to process for the selected range.")
        if skipped_existing and not args.overwrite:
            print(f"Skipped {skipped_existing} files because output JSON already existed.")
        return 0

    selected_start = batch_files[0][0]
    selected_end = batch_files[-1][0]
    requested_end = (args.end_index - 1) if args.end_index is not None else (len(all_files) - 1)

    print(f"Total .txt files found: {len(all_files)}")
    print(f"Requested range: {args.start_index} to {requested_end}")
    print(f"Skipped existing outputs in range while selecting batch: {skipped_existing}")
    print(f"Selected batch size: {len(batch_files)} article(s)")
    print(f"Global indices covered by this batch: {selected_start} to {selected_end}")
    print(f"Parallel workers: {args.workers}")
    print(f"Writing JSON outputs to {output_dir}")
    if not args.overwrite:
        print("Existing outputs are being skipped. Use --overwrite to re-run them.")
    print()

    started_at = time.perf_counter()
    success_count = 0
    failure_count = 0
    usage_log_lock = Lock()

    future_to_job = {}
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for global_index, source_path in batch_files:
            output_path = build_output_path(output_dir, source_path, args.model)
            article_started_at = time.perf_counter()
            future = executor.submit(
                run_single_article,
                fetcher,
                source_path,
                output_path,
                prompt,
                schema,
                args.model,
            )
            future_to_job[future] = (global_index, source_path, article_started_at)

        for future in as_completed(future_to_job):
            global_index, source_path, article_started_at = future_to_job[future]
            article_elapsed = time.perf_counter() - article_started_at
            elapsed = time.perf_counter() - started_at

            try:
                succeeded, error_message, usage_record = future.result()
            except Exception as exc:
                succeeded = False
                error_message = f"Unexpected worker error: {exc}"
                usage_record = {}

            if succeeded:
                success_count += 1
                status = "OK"
                append_usage(usage_log_path, usage_record, usage_log_lock)
            else:
                failure_count += 1
                status = "FAIL"
                append_error(error_log_path, source_path, error_message or "Unknown error")

            processed_count = success_count + failure_count
            average_seconds = elapsed / processed_count
            remaining_count = len(batch_files) - processed_count
            eta_seconds = remaining_count * average_seconds
            percent = (processed_count / len(batch_files)) * 100

            usage = usage_record.get("usage", {})
            usage_suffix = ""
            if usage:
                usage_suffix = (
                    f" | tokens in/out/total "
                    f"{usage.get('input_tokens', 'n/a')}/"
                    f"{usage.get('output_tokens', 'n/a')}/"
                    f"{usage.get('total_tokens', 'n/a')}"
                )

            print(
                f"[batch {processed_count}/{len(batch_files)} | global {global_index + 1}/{len(all_files)} | "
                f"{percent:5.1f}% | {status}] "
                f"{source_path.name} | article {article_elapsed:.1f}s | "
                f"avg {average_seconds:.1f}s | elapsed {format_seconds(elapsed)} | "
                f"eta {format_seconds(eta_seconds)}"
                f"{usage_suffix}"
            )

    total_elapsed = time.perf_counter() - started_at
    print()
    print(
        f"Finished batch: {success_count} succeeded, {failure_count} failed, "
        f"total time {format_seconds(total_elapsed)}."
    )
    if success_count:
        print(f"Usage metadata was appended to {usage_log_path}")
    if failure_count:
        print(f"Failure details were appended to {error_log_path}")

    return 0 if failure_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
