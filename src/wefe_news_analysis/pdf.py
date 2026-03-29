from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


@dataclass(slots=True)
class ExtractedArticle:
    source_path: Path
    text: str
    page_count: int


def extract_text_from_pdf(pdf_path: Path) -> ExtractedArticle:
    reader = PdfReader(str(pdf_path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(page.strip() for page in pages if page.strip())
    return ExtractedArticle(source_path=pdf_path, text=text, page_count=len(reader.pages))

