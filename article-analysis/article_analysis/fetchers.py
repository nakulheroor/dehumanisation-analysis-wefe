from __future__ import annotations

import re
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class ArticleContent:
    source_url: str
    title: str
    text: str
    metadata: dict[str, str]


class ArticleFetchError(RuntimeError):
    """Raised when an article could not be downloaded or extracted."""


class _ArticleHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_article = 0
        self.capture_depth = 0
        self.skip_depth = 0
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.metadata: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key: value or "" for key, value in attrs}

        if tag == "title":
            self.in_title = True

        if tag == "meta":
            name = (attrs_dict.get("property") or attrs_dict.get("name") or "").strip().lower()
            content = attrs_dict.get("content", "").strip()
            if name and content:
                self.metadata[name] = content

        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
            return

        if tag == "article":
            self.in_article += 1

        if self.skip_depth:
            return

        if self.in_article and tag in {"p", "h1", "h2", "h3", "li", "blockquote"}:
            self.capture_depth += 1
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

        if tag in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
            return

        if tag == "article" and self.in_article:
            self.in_article -= 1

        if self.skip_depth:
            return

        if tag in {"p", "h1", "h2", "h3", "li", "blockquote"} and self.capture_depth:
            self.capture_depth -= 1
            self.text_parts.append("\n")

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return

        if self.in_title:
            self.title_parts.append(text)

        if self.skip_depth:
            return

        if self.in_article or self.capture_depth:
            self.text_parts.append(text)


class DirectURLArticleFetcher:
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )

    def fetch(self, source: str) -> ArticleContent:
        html = self._download(source)
        parser = _ArticleHTMLParser()
        parser.feed(html)

        title = self._pick_title(parser, html, source)
        text = self._pick_text(parser, html)

        return ArticleContent(
            source_url=source,
            title=title,
            text=text,
            metadata={"hostname": urlparse(source).netloc, **parser.metadata},
        )

    def _download(self, source: str) -> str:
        request = Request(
            source,
            headers={
                "User-Agent": self.user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "https://www.google.com/",
            },
        )
        try:
            with urlopen(request, timeout=30) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except HTTPError as exc:
            raise ArticleFetchError(
                f"Direct fetch failed with HTTP {exc.code} for {source}."
            ) from exc
        except URLError as exc:
            raise ArticleFetchError(
                f"Direct fetch failed for {source}: {exc.reason}."
            ) from exc

    def _pick_title(self, parser: _ArticleHTMLParser, html: str, source: str) -> str:
        for key in ("og:title", "twitter:title"):
            if key in parser.metadata:
                return parser.metadata[key]

        title = " ".join(parser.title_parts).strip()
        if title:
            return title

        match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
        if match:
            return self._normalize_text(match.group(1))

        return source

    def _pick_text(self, parser: _ArticleHTMLParser, html: str) -> str:
        if parser.text_parts:
            text = self._normalize_text(" ".join(parser.text_parts))
            if len(text) >= 200:
                return text

        match = re.search(
            r"<article[^>]*>(.*?)</article>",
            html,
            re.IGNORECASE | re.DOTALL,
        )
        if match:
            text = self._normalize_text(self._strip_tags(match.group(1)))
            if text:
                return text

        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)
        text = self._normalize_text(" ".join(self._strip_tags(paragraph) for paragraph in paragraphs))
        if text:
            return text

        raise ValueError("Unable to extract article text from the provided source.")

    def _strip_tags(self, value: str) -> str:
        value = re.sub(r"<script.*?</script>", " ", value, flags=re.IGNORECASE | re.DOTALL)
        value = re.sub(r"<style.*?</style>", " ", value, flags=re.IGNORECASE | re.DOTALL)
        value = re.sub(r"<[^>]+>", " ", value)
        return unescape(value)

    def _normalize_text(self, value: str) -> str:
        value = unescape(value)
        value = re.sub(r"\s+", " ", value)
        return value.strip()


class JinaMirrorArticleFetcher:
    """Fallback text mirror for sites that are readable but hard to parse directly."""

    def fetch(self, source: str) -> ArticleContent:
        mirror_url = f"https://r.jina.ai/http://{source}"
        request = Request(
            mirror_url,
            headers={
                "User-Agent": "article-analysis/1.0",
                "Accept": "text/plain,text/markdown;q=0.9,*/*;q=0.8",
            },
        )
        try:
            with urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            raise ArticleFetchError(
                f"Mirror fetch failed with HTTP {exc.code} for {source}."
            ) from exc
        except URLError as exc:
            raise ArticleFetchError(
                f"Mirror fetch failed for {source}: {exc.reason}."
            ) from exc

        if "Warning: Target URL returned error 403" in body:
            raise ArticleFetchError(
                "The site is blocking automated access even through the fallback mirror."
            )

        title = source
        title_match = re.search(r"^Title:\s*(.+)$", body, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()

        markdown_start = body.find("Markdown Content:")
        if markdown_start == -1:
            raise ArticleFetchError("Mirror response did not include article content.")

        text = body[markdown_start + len("Markdown Content:") :].strip()
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
        text = re.sub(r"`{1,3}", "", text)
        text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.strip()
        if not text:
            raise ArticleFetchError("Mirror response was empty after cleanup.")

        return ArticleContent(
            source_url=source,
            title=title,
            text=text,
            metadata={"source_adapter": "jina_mirror", "hostname": urlparse(source).netloc},
        )


class TextFileArticleFetcher:
    def fetch(self, source: str) -> ArticleContent:
        path = Path(source)
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            raise ArticleFetchError(f"Text file is empty: {source}")

        title = path.stem.replace("_", " ").replace("-", " ").strip() or source
        return ArticleContent(
            source_url=str(path.resolve()),
            title=title,
            text=text,
            metadata={"source_adapter": "text_file"},
        )


class URLArticleFetcher:
    def __init__(self) -> None:
        self.fetchers = [DirectURLArticleFetcher(), JinaMirrorArticleFetcher()]

    def fetch(self, source: str) -> ArticleContent:
        errors: list[str] = []
        for fetcher in self.fetchers:
            try:
                return fetcher.fetch(source)
            except ArticleFetchError as exc:
                errors.append(str(exc))

        host = urlparse(source).netloc or source
        raise ArticleFetchError(
            f"Unable to fetch article from {host}. "
            "This site may require JavaScript, a login, or anti-bot verification. "
            "Try a different article URL or save the article text to a local file and run "
            "`python3 analyze_article.py /path/to/article.txt --source-kind text-file`.\n"
            f"Fetch attempts: {' | '.join(errors)}"
        )


def build_fetcher(source_kind: str):
    if source_kind == "url":
        return URLArticleFetcher()
    if source_kind == "text-file":
        return TextFileArticleFetcher()
    raise ValueError(f"Unsupported source kind: {source_kind}")
