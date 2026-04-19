from __future__ import annotations

from article_analysis.rubric import load_rubric as base_load_rubric
from article_analysis.rubric import rubric_prompt as base_rubric_prompt
from article_analysis.rubric import rubric_to_schema as base_rubric_to_schema


def load_rubric(rubric_path):
    return base_load_rubric(rubric_path)


def rubric_to_schema(rubric: dict) -> dict:
    schema = base_rubric_to_schema(rubric)
    return _strip_unsupported_keys(schema)


def rubric_prompt(rubric: dict) -> str:
    base_prompt = base_rubric_prompt(rubric)
    gemini_rules = [
        "",
        "Gemini output rules:",
        "- Return exactly one JSON object.",
        "- Use only the rubric field names listed above.",
        "- Do not add any extra keys, notes, commentary, markdown, or prose outside the JSON object.",
        "- Keep each field concise and directly tied to the article.",
        "- Do not quote long passages from the article unless a field explicitly requires it.",
    ]
    return "\n".join([base_prompt, *gemini_rules])


def _strip_unsupported_keys(value):
    if isinstance(value, dict):
        cleaned = {}
        for key, item in value.items():
            if key == "additionalProperties":
                continue
            cleaned[key] = _strip_unsupported_keys(item)
        return cleaned

    if isinstance(value, list):
        return [_strip_unsupported_keys(item) for item in value]

    return value
