from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache


DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"


@dataclass
class GeminiAnalysisResult:
    parsed_json: dict
    usage: dict
    model: str | None


@lru_cache(maxsize=1)
def get_gemini_client():
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError(
            "The Google Gen AI Python package is not installed in this environment. "
            "Install it first, for example with `pip install -r requirements_gemini.txt`."
        ) from exc

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Export it in your shell or place it in a .env file."
        )

    return genai.Client(api_key=api_key)


def analyze_with_gemini_api(
    article_title: str,
    article_url: str,
    article_text: str,
    prompt: str,
    schema: dict | None,
    model: str | None = None,
) -> GeminiAnalysisResult:
    from google.genai import types

    client = get_gemini_client()
    full_prompt = "\n\n".join(
        [
            prompt,
            f"Article title: {article_title}",
            f"Article URL: {article_url}",
            "Article text:",
            article_text,
        ]
    )

    config_kwargs = {"response_mime_type": "application/json"}
    if schema is not None:
        config_kwargs["response_schema"] = schema

    response = client.models.generate_content(
        model=model or DEFAULT_GEMINI_MODEL,
        contents=full_prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    parsed_json = _parse_response_json(response)
    if not isinstance(parsed_json, dict):
        raise RuntimeError("Gemini API returned JSON that was not an object.")

    return GeminiAnalysisResult(
        parsed_json=parsed_json,
        usage=_extract_usage(response),
        model=getattr(response, "model_version", None),
    )


def _parse_response_json(response) -> dict:
    parsed = getattr(response, "parsed", None)
    if isinstance(parsed, dict):
        return parsed

    response_text = getattr(response, "text", None)
    if not response_text:
        raise RuntimeError("Gemini API returned an empty response.")

    try:
        return json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Gemini API returned invalid JSON despite the schema request.\n"
            f"Raw response:\n{response_text}"
        ) from exc


def _extract_usage(response) -> dict:
    usage = getattr(response, "usage_metadata", None)
    if usage is None:
        return {}

    extracted = {
        "input_tokens": _maybe_int(getattr(usage, "prompt_token_count", None)),
        "output_tokens": _maybe_int(getattr(usage, "candidates_token_count", None)),
        "total_tokens": _maybe_int(getattr(usage, "total_token_count", None)),
        "thoughts_token_count": _maybe_int(getattr(usage, "thoughts_token_count", None)),
        "cached_content_token_count": _maybe_int(
            getattr(usage, "cached_content_token_count", None)
        ),
        "tool_use_prompt_token_count": _maybe_int(
            getattr(usage, "tool_use_prompt_token_count", None)
        ),
    }
    return {key: value for key, value in extracted.items() if value is not None}


def _maybe_int(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None
