#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
from pathlib import Path


SOURCE_DIR = Path("articles_data")
TARGET_DIR = Path("articles_data_clean")
SUPPORTED_EXTENSIONS = {".txt", ".html"}
DATE_RE = re.compile(r"\b(\d{2})\.(\d{2})\.(\d{4})\b")
FIRST_LINE_DATE_RE = re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})\b")


def extract_date(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")

    if path.suffix == ".txt":
        first_line = text.splitlines()[0] if text.splitlines() else ""
        match = FIRST_LINE_DATE_RE.search(first_line)
    else:
        date_match = re.search(
            r"<strong>\s*Datum\s*</strong>.*?(\d{2}\.\d{2}\.\d{4})",
            text,
            re.DOTALL,
        )
        if date_match is None:
            raise ValueError(f"Could not extract a date from {path}")
        match = DATE_RE.search(date_match.group(0))
        if match is None:
            raise ValueError(f"Could not normalize the date from {path}")

    if match is None:
        raise ValueError(f"Could not extract a date from {path}")

    day, month, year = match.groups()
    return f"{year}_{month}_{day}"


def extract_slug(path: Path) -> str:
    stem = path.stem
    match = re.match(r"^\d+-(.+)$", stem)
    if match is None:
        raise ValueError(f"Unexpected filename format: {path.name}")
    return match.group(1)


def should_skip(path: Path) -> bool:
    if path.suffix not in SUPPORTED_EXTENSIONS:
        return True
    if path.name.startswith("ad-hoc-"):
        return True
    return False


def main() -> None:
    TARGET_DIR.mkdir(exist_ok=True)
    existing_targets = {
        (path.name.rsplit("_", 3)[-1], path.suffix)
        for path in TARGET_DIR.iterdir()
        if path.is_file() and path.suffix in SUPPORTED_EXTENSIONS and "_" in path.name
    }

    copied = 0
    skipped_existing = 0
    skipped_ignored = 0
    skipped_unparseable = 0

    for source_path in sorted(SOURCE_DIR.iterdir()):
        if not source_path.is_file():
            continue

        if should_skip(source_path):
            skipped_ignored += 1
            continue

        try:
            slug = extract_slug(source_path)
        except ValueError:
            skipped_unparseable += 1
            continue

        if (f"{slug}{source_path.suffix}", source_path.suffix) in existing_targets:
            skipped_existing += 1
            continue

        try:
            date_prefix = extract_date(source_path)
        except ValueError:
            skipped_unparseable += 1
            continue

        target_name = f"{date_prefix}_{slug}{source_path.suffix}"
        shutil.copy2(source_path, TARGET_DIR / target_name)
        existing_targets.add((f"{slug}{source_path.suffix}", source_path.suffix))
        copied += 1

    print(f"Copied: {copied}")
    print(f"Skipped existing: {skipped_existing}")
    print(f"Skipped ignored: {skipped_ignored}")
    print(f"Skipped unparseable: {skipped_unparseable}")


if __name__ == "__main__":
    main()
