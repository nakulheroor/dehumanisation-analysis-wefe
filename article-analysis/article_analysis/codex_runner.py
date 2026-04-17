from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def analyze_with_codex(
    article_title: str,
    article_url: str,
    article_text: str,
    prompt: str,
    schema: dict,
    model: str | None = None,
) -> dict:
    with tempfile.TemporaryDirectory() as temp_dir:
        schema_path = Path(temp_dir) / "schema.json"
        output_path = Path(temp_dir) / "output.json"

        schema_path.write_text(json.dumps(schema, indent=2), encoding="utf-8")

        full_prompt = "\n\n".join(
            [
                prompt,
                f"Article title: {article_title}",
                f"Article URL: {article_url}",
                "Article text:",
                article_text,
            ]
        )

        command = [
            "codex",
            "exec",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
        ]
        if model:
            command.extend(["--model", model])
        command.append("-")

        completed = subprocess.run(
            command,
            input=full_prompt,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                "Codex analysis failed.\n"
                f"stdout:\n{completed.stdout}\n"
                f"stderr:\n{completed.stderr}"
            )

        return json.loads(output_path.read_text(encoding="utf-8"))
