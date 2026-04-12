from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class SafariWebDriverError(RuntimeError):
    """Raised when Safari WebDriver returns an error."""


@dataclass
class SafariElement:
    driver: "SafariWebDriver"
    element_id: str

    def click(self) -> None:
        self.driver._request(
            "POST",
            f"/session/{self.driver.session_id}/element/{self.element_id}/click",
            {},
        )

    def send_keys(self, value: str) -> None:
        self.driver._request(
            "POST",
            f"/session/{self.driver.session_id}/element/{self.element_id}/value",
            {"text": value, "value": list(value)},
        )

    def clear(self) -> None:
        self.driver._request(
            "POST",
            f"/session/{self.driver.session_id}/element/{self.element_id}/clear",
            {},
        )

    def text(self) -> str:
        response = self.driver._request(
            "GET",
            f"/session/{self.driver.session_id}/element/{self.element_id}/text",
        )
        return str(response)


class SafariWebDriver:
    def __init__(
        self,
        server_url: str,
        min_command_interval_seconds: float = 1.0,
        request_timeout_seconds: float | None = None,
    ) -> None:
        self.server_url = server_url.rstrip("/")
        self.min_command_interval_seconds = min_command_interval_seconds
        self.request_timeout_seconds = request_timeout_seconds
        self._last_command_monotonic = 0.0
        self.session_id: str | None = None

    def create_session(self) -> str:
        response = self._request(
            "POST",
            "/session",
            {"capabilities": {"alwaysMatch": {"browserName": "safari"}}},
            throttle=False,
        )
        self.session_id = response["sessionId"]
        return self.session_id

    def close(self) -> None:
        if not self.session_id:
            return
        try:
            self._request("DELETE", f"/session/{self.session_id}", throttle=False)
        finally:
            self.session_id = None

    def navigate(self, url: str) -> None:
        self._ensure_session()
        self._request("POST", f"/session/{self.session_id}/url", {"url": url})

    def page_source(self) -> str:
        self._ensure_session()
        response = self._request("GET", f"/session/{self.session_id}/source")
        return str(response)

    def title(self) -> str:
        self._ensure_session()
        response = self._request("GET", f"/session/{self.session_id}/title")
        return str(response)

    def current_url(self) -> str:
        self._ensure_session()
        response = self._request("GET", f"/session/{self.session_id}/url")
        return str(response)

    def find_css(self, selector: str) -> SafariElement:
        self._ensure_session()
        response = self._request(
            "POST",
            f"/session/{self.session_id}/element",
            {"using": "css selector", "value": selector},
        )
        return SafariElement(self, self._extract_element_id(response))

    def find_all_css(self, selector: str) -> list[SafariElement]:
        self._ensure_session()
        response = self._request(
            "POST",
            f"/session/{self.session_id}/elements",
            {"using": "css selector", "value": selector},
        )
        return [SafariElement(self, self._extract_element_id(item)) for item in response]

    def execute_script(self, script: str, args: list[Any] | None = None) -> Any:
        self._ensure_session()
        return self._request(
            "POST",
            f"/session/{self.session_id}/execute/sync",
            {"script": script, "args": args or []},
        )

    def wait_for_css(self, selector: str, timeout_seconds: float = 30.0, poll_seconds: float = 1.0) -> SafariElement:
        deadline = time.monotonic() + timeout_seconds
        last_error: Exception | None = None
        while time.monotonic() < deadline:
            try:
                return self.find_css(selector)
            except SafariWebDriverError as exc:
                last_error = exc
                time.sleep(max(poll_seconds, self.min_command_interval_seconds))
        raise SafariWebDriverError(
            f"Timed out waiting for selector {selector!r}."
            + (f" Last error: {last_error}" if last_error else "")
        )

    def wait_for_url_contains(self, text: str, timeout_seconds: float = 30.0) -> str:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            current = self.current_url()
            if text in current:
                return current
            time.sleep(self.min_command_interval_seconds)
        raise SafariWebDriverError(f"Timed out waiting for current URL to contain {text!r}.")

    def _request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        *,
        throttle: bool = True,
    ) -> Any:
        if throttle and self.min_command_interval_seconds > 0:
            delay = self.min_command_interval_seconds - (time.monotonic() - self._last_command_monotonic)
            if delay > 0:
                time.sleep(delay)

        body = None
        headers = {}
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        request = Request(f"{self.server_url}{path}", data=body, method=method, headers=headers)
        try:
            if self.request_timeout_seconds is None:
                response_cm = urlopen(request)
            else:
                response_cm = urlopen(request, timeout=self.request_timeout_seconds)
            with response_cm as response:
                raw = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            raise SafariWebDriverError(self._format_error(raw, fallback=f"HTTP {exc.code} from {path}")) from exc
        except URLError as exc:
            raise SafariWebDriverError(f"Failed to reach Safari WebDriver at {self.server_url}: {exc.reason}") from exc
        finally:
            self._last_command_monotonic = time.monotonic()

        if not raw:
            return None

        parsed = json.loads(raw)
        value = parsed.get("value")
        if isinstance(value, dict) and value.get("error"):
            raise SafariWebDriverError(self._format_error(raw))

        if path == "/session" and method == "POST":
            session_id = parsed.get("sessionId")
            if not session_id and isinstance(value, dict):
                session_id = value.get("sessionId")
            if not session_id:
                raise SafariWebDriverError("Safari WebDriver did not return a session id.")
            return {"sessionId": session_id, "value": value}

        return value

    def _ensure_session(self) -> None:
        if not self.session_id:
            raise SafariWebDriverError("No Safari WebDriver session is active.")

    def _extract_element_id(self, payload: dict[str, Any]) -> str:
        element_id = payload.get("element-6066-11e4-a52e-4f735466cecf")
        if not element_id:
            raise SafariWebDriverError(f"Unexpected element payload: {payload!r}")
        return str(element_id)

    def _format_error(self, raw_json: str, fallback: str | None = None) -> str:
        try:
            parsed = json.loads(raw_json)
        except json.JSONDecodeError:
            return fallback or raw_json
        value = parsed.get("value", {})
        message = value.get("message")
        error = value.get("error")
        if error and message:
            return f"{error}: {message}"
        if message:
            return str(message)
        return fallback or raw_json
