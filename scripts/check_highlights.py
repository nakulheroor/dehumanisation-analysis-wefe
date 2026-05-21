"""Quick audit: print paragraphs that have at least one yellow-highlighted run."""
from docx import Document
from docx.enum.text import WD_COLOR_INDEX  # type: ignore[attr-defined]
import sys

path = sys.argv[1] if len(sys.argv) > 1 else (
    "reports/computational results and methodology - albanese.docx"
)

doc = Document(path)
yellow_paras = []
for i, para in enumerate(doc.paragraphs):
    if any(run.font.highlight_color == WD_COLOR_INDEX.YELLOW for run in para.runs):
        yellow_paras.append((i, para.text[:120].replace("\n", " ")))

print(f"Paragraphs with yellow highlighting: {len(yellow_paras)}\n")
for idx, snippet in yellow_paras:
    print(f"  [{idx:4d}] {snippet}")
