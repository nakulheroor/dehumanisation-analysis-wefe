from __future__ import annotations

import json
import re
from pathlib import Path


def load_rubric(rubric_path: str | Path) -> dict:
    rubric_path = Path(rubric_path)
    content = rubric_path.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
    if not match:
        raise ValueError("rubric.md must contain a fenced ```json block.")

    rubric = json.loads(match.group(1))
    validate_rubric(rubric)
    rubric["_resolved_reference_documents"] = _load_reference_documents(
        rubric, rubric_path.parent
    )
    return rubric


def fload_rubric(rubric_path: str | Path) -> dict:
    return load_rubric(rubric_path)


def _load_reference_documents(rubric: dict, base_dir: Path) -> list[dict]:
    resolved_documents = []

    for index, config in enumerate(rubric.get("reference_documents", []), start=1):
        path = base_dir / config["path"]
        resolved_documents.append(
            {
                "title": config.get("title", f"Reference document {index}"),
                "path": str(path),
                "content": path.read_text(encoding="utf-8").strip(),
            }
        )

    return resolved_documents


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

    reference_documents = rubric.get("reference_documents", [])
    if not isinstance(reference_documents, list):
        raise ValueError("'reference_documents' must be a list when provided.")

    for index, config in enumerate(reference_documents, start=1):
        if not isinstance(config, dict):
            raise ValueError(f"Reference document {index} must be an object.")
        if "path" not in config:
            raise ValueError(f"Reference document {index} must include a path.")


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
    reference_documents = rubric.get("_resolved_reference_documents", [])
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
        if config.get("type") == "array" and "items" in config:
            item_type = config["items"].get("type")
            if item_type:
                detail += f" Item type: {item_type}."
            if "enum" in config["items"]:
                detail += (
                    " Allowed item values: "
                    + ", ".join(config["items"]["enum"])
                    + "."
                )
        if "minimum" in config or "maximum" in config:
            minimum = config.get("minimum", "-inf")
            maximum = config.get("maximum", "inf")
            detail += f" Range: {minimum} to {maximum}."
        lines.append(detail)

    if scoring_notes:
        lines.extend(["", "Additional instructions:", scoring_notes])

    if reference_documents:
        lines.extend(["", "Reference documents:"])
        for document in reference_documents:
            lines.extend(
                [
                    "",
                    f"{document['title']} ({document['path']}):",
                    document["content"],
                ]
            )

    return "\n".join(lines)
