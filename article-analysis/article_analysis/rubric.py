from __future__ import annotations

import json
import re
from pathlib import Path


def fload_rubric(rubric_path: str | Path) -> dict:
    content = Path(rubric_path).read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    if not match:
        raise ValueError("rubric.md must contain a fenced ```json block.")

    rubric = json.loads(match.group(1))
    validate_rubric(rubric)
    return rubric


def validate_rubric(rubric: dict) -> None:
    if not isinstance(rubric.get("fields"), dict) or not rubric["fields"]:
        raise ValueError("Rubric JSON must contain a non-empty 'fields' object.")

    for field_name, config in rubric["fields"].items():
        if not isinstance(config, dict):
            raise ValueError(f"Field '{field_name}' must be an object.")
        if "description" not in config:
            raise ValueError(f"Field '{field_name}' must include a description.")
        if "type" not in config:
            raise ValueError(f"Field '{field_name}' must include a type.")


def rubric_to_schema(rubric: dict) -> dict:
    properties = {}
    required = []

    for field_name, config in rubric["fields"].items():
        field_schema = {
            "type": config["type"],
            "description": config["description"],
        }

        for key in ("enum", "minimum", "maximum", "items"):
            if key in config:
                field_schema[key] = config[key]

        properties[field_name] = field_schema
        required.append(field_name)

    return {
        "type": "object",
        "additionalProperties": False,
        "properties": properties,
        "required": required,
    }


def rubric_prompt(rubric: dict) -> str:
    scoring_notes = rubric.get("global_instructions", "").strip()
    lines = [
        "Analyze the supplied article using the rubric below.",
        "Return only valid JSON that conforms to the provided schema.",
        "Do not include markdown fences, commentary, or extra keys.",
        "",
        "Rubric fields:",
    ]

    for field_name, config in rubric["fields"].items():
        detail = f"- {field_name} ({config['type']}): {config['description']}"
        if "enum" in config:
            detail += f" Allowed values: {', '.join(config['enum'])}."
        if "minimum" in config or "maximum" in config:
            minimum = config.get("minimum", "-inf")
            maximum = config.get("maximum", "inf")
            detail += f" Range: {minimum} to {maximum}."
        lines.append(detail)

    if scoring_notes:
        lines.extend(["", "Additional instructions:", scoring_notes])

    return "\n".join(lines)
