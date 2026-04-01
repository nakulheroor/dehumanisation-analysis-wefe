#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

from article_analysis.safari_webdriver import SafariWebDriver, SafariWebDriverError


DEFAULT_START_URL = "https://archiv-szarchiv-de.tum-eaccess.de/Portal/restricted/ExtendedSearch.act"
DEFAULT_WEBDRIVER_URL = "http://127.0.0.1:4444"
DEFAULT_FROM_DATE = "06.10.2023"
DEFAULT_TO_DATE = "26.03.2026"
DEFAULT_DUMP_DIR = "articles_data"


class BrowserArchiveError(RuntimeError):
    """Raised when the Safari-driven archive flow fails."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Drive the TUM SZ archive in Safari WebDriver and inspect or search the authenticated session."
    )
    parser.add_argument("--username", required=True, help="TUM username.")
    parser.add_argument("--password", required=True, help="TUM password.")
    parser.add_argument("--keyword", help="Keyword to search for after login.")
    parser.add_argument("--from-date", default=DEFAULT_FROM_DATE, help="Start date for the search range in DD.MM.YYYY format.")
    parser.add_argument("--to-date", default=DEFAULT_TO_DATE, help="End date for the search range in DD.MM.YYYY format.")
    parser.add_argument("--page", type=int, help="Single results page to download.")
    parser.add_argument("--page-from", type=int, help="First results page to download.")
    parser.add_argument("--page-to", type=int, help="Last results page to download.")
    parser.add_argument("--start-url", default=DEFAULT_START_URL, help="Archive URL to open first.")
    parser.add_argument(
        "--webdriver-url",
        default=DEFAULT_WEBDRIVER_URL,
        help="Safari WebDriver server URL. Defaults to http://127.0.0.1:4444.",
    )
    parser.add_argument(
        "--dump-dir",
        default=DEFAULT_DUMP_DIR,
        help="Directory for HTML snapshots and downloaded articles. Defaults to articles_data.",
    )
    parser.add_argument(
        "--discover-only",
        action="store_true",
        help="Log in, dump the resulting page HTML, and print a summary instead of attempting a search.",
    )
    parser.add_argument(
        "--ad-hoc-inspect",
        action="store_true",
        help="Run the ad hoc keyword search, open the first article result, and print extracted page content.",
    )
    parser.add_argument(
        "--pause-after-login-seconds",
        type=float,
        default=5.0,
        help="Additional wait after submitting credentials so JS handoffs can settle.",
    )
    parser.add_argument(
        "--min-command-interval-seconds",
        type=float,
        default=1.0,
        help="Minimum delay between WebDriver commands. Defaults to 1.0 seconds.",
    )
    return parser.parse_args()


def save_snapshot(dump_dir: Path | None, name: str, html: str) -> None:
    if dump_dir is None:
        return
    dump_dir.mkdir(parents=True, exist_ok=True)
    (dump_dir / name).write_text(html, encoding="utf-8")


def detect_login_page(html: str) -> bool:
    return "name=\"j_username\"" in html and "name=\"j_password\"" in html


def detect_archive_bridge_failure(html: str) -> bool:
    return "performIpLogin" in html and "Benutzername oder Passwort nicht korrekt" in html


def summarize_page(driver: SafariWebDriver, html: str) -> dict[str, object]:
    forms = driver.execute_script(
        """
        return Array.from(document.forms).map((form, index) => ({
          index: index + 1,
          action: form.action,
          method: form.method,
          fields: Array.from(form.elements).map((el) => el.name).filter(Boolean)
        }));
        """
    )
    links = driver.execute_script(
        """
        return Array.from(document.querySelectorAll('a[href]')).slice(0, 50).map((a) => ({
          text: (a.innerText || a.textContent || '').trim(),
          href: a.href
        }));
        """
    )
    return {
        "title": driver.title(),
        "current_url": driver.current_url(),
        "forms": forms,
        "links_sample": links,
        "html_length": len(html),
    }


def extract_result_links(driver: SafariWebDriver) -> list[dict[str, str]]:
    links = driver.execute_script(
        """
        const anchors = Array.from(document.querySelectorAll('a[href]'));
        return anchors
          .map((a) => ({
            text: (a.innerText || a.textContent || '').trim(),
            href: a.href
          }))
          .filter((item) => {
            const href = item.href || '';
            return href.includes('/Portal/restricted/')
              && !href.endsWith('#')
              && !href.includes('ExtendedSearch.act')
              && !href.includes('ExtendedSearch_reset.act')
              && !href.includes('SystemInfo.act')
              && !href.includes('MySpace.act');
          });
        """
    )
    deduped: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in links:
        href = str(item.get("href") or "")
        text = str(item.get("text") or "")
        if not href or href in seen:
            continue
        seen.add(href)
        deduped.append({"text": text, "href": href})
    return deduped


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def save_article_text(
    dump_dir: Path | None,
    article_title: str | None,
    article_text: str | None,
    *,
    article_index: int | None = None,
) -> str | None:
    if dump_dir is None or not article_text:
        return None
    dump_dir.mkdir(parents=True, exist_ok=True)
    name = slugify(article_title or "article")[:80]
    prefix = f"{article_index:03d}-" if article_index is not None else ""
    path = dump_dir / f"{prefix}{name}.txt"
    path.write_text(article_text, encoding="utf-8")
    return str(path)


def save_article_html(
    dump_dir: Path | None,
    article_title: str | None,
    article_html: str | None,
    *,
    article_index: int | None = None,
) -> str | None:
    if dump_dir is None or not article_html:
        return None
    dump_dir.mkdir(parents=True, exist_ok=True)
    name = slugify(article_title or "article")[:80]
    prefix = f"{article_index:03d}-" if article_index is not None else ""
    path = dump_dir / f"{prefix}{name}.html"
    path.write_text(article_html, encoding="utf-8")
    return str(path)


def resolve_page_range(args: argparse.Namespace) -> tuple[int, int]:
    if args.page is not None and (args.page_from is not None or args.page_to is not None):
        raise BrowserArchiveError("Use either --page or --page-from/--page-to, not both.")
    if args.page is not None:
        if args.page < 1:
            raise BrowserArchiveError("--page must be at least 1.")
        return args.page, args.page

    page_from = args.page_from if args.page_from is not None else 1
    page_to = args.page_to if args.page_to is not None else page_from
    if page_from < 1 or page_to < 1:
        raise BrowserArchiveError("--page-from and --page-to must be at least 1.")
    return page_from, page_to


def open_result_article(
    driver: SafariWebDriver,
    result: dict[str, str],
    *,
    pause_after_login_seconds: float,
) -> None:
    fulltext_url = str(result.get("fulltext_url") or "")
    href = str(result.get("href") or "")
    if fulltext_url:
        open_result = driver.execute_script(
            """
            const fulltextUrl = arguments[0];
            if (!window.SSP || typeof window.SSP.loadFulltext !== 'function') {
              return {ok: false, reason: 'SSP.loadFulltext is not available on the results page.'};
            }
            window.SSP.loadFulltext(fulltextUrl);
            return {ok: true};
            """,
            [fulltext_url],
        )
        if not open_result.get("ok"):
            raise BrowserArchiveError(str(open_result.get("reason") or "Opening the fulltext view failed."))
    elif href:
        driver.navigate(href)
    else:
        raise BrowserArchiveError("The result did not include a usable fulltext URL or href.")

    time.sleep(pause_after_login_seconds)


def extract_article_page_data(driver: SafariWebDriver) -> dict[str, object]:
    return driver.execute_script(
        """
        const NAV_LINE_RE = /^(SUCHE|KALENDER|MEIN BEREICH|DOSSIERSTRUKTUR|GANZSEITEN|Systeminfo|Hilfe|Desktop Version|Mobile Version|close)$/i;
        const FOOTER_LINE_RE = /^(AGB|Impressum|Datenschutz|FAQ|Kontakt)$/i;

        function normalize(text) {
          return (text || '')
            .replace(/\\u00a0/g, ' ')
            .replace(/[ \\t]+\\n/g, '\\n')
            .replace(/\\n{3,}/g, '\\n\\n')
            .replace(/[ \\t]{2,}/g, ' ')
            .trim();
        }

        function cleanLines(text) {
          const lines = normalize(text)
            .split('\\n')
            .map((line) => line.trim())
            .filter(Boolean)
            .filter((line) => !NAV_LINE_RE.test(line))
            .filter((line) => !FOOTER_LINE_RE.test(line))
            .filter((line) => !line.includes('Die hier recherchierten Daten sind nur zur persönlichen Kenntnisnahme'))
            .filter((line) => !line.includes('Text- und Data-Mining'))
            .filter((line) => !line.match(/^\\d{1,3}(\\.\\d{1,3}){3}$/));
          return lines.join('\\n');
        }

        function candidate(selector) {
          const elements = Array.from(document.querySelectorAll(selector));
          if (!elements.length) {
            return null;
          }
          const matches = elements
            .map((el) => {
              const text = cleanLines(el.innerText || el.textContent || '');
              return {
                selector,
                text,
                length: text.length,
                className: el.className || null,
                id: el.id || null,
              };
            })
            .sort((a, b) => b.length - a.length);
          return matches[0];
        }

        const selectors = [
          '#fulltextWrapperBodyWrapper',
          '.fullTextCenter',
          '.fullTextLeft',
          '.fulltextWrapperBodyWrapper',
          '.fulltext',
          '.articleText',
          '.article',
          '.content',
          'article',
          'main',
          'body'
        ];

        const candidates = selectors
          .map(candidate)
          .filter(Boolean);

        const best = candidates.find((item) => item.selector !== 'body' && item.length > 200) || candidates.find((item) => item.length > 200) || null;
        const bodyText = cleanLines(document.body ? (document.body.innerText || document.body.textContent || '') : '');

        return {
          title: document.title,
          current_url: window.location.href,
          h1: document.querySelector('h1') ? document.querySelector('h1').innerText.trim() : null,
          h2: document.querySelector('h2') ? document.querySelector('h2').innerText.trim() : null,
          article_text: best ? best.text : (bodyText.length > 200 ? bodyText : null),
          article_source_selector: best ? best.selector : (bodyText.length > 200 ? 'body' : null),
          article_candidates: [...candidates].sort((a, b) => b.length - a.length).slice(0, 10),
          classes: Array.from(document.querySelectorAll('h1,h2,h3,.article,.content,.text,.lead,.headline,#fulltextWrapperBodyWrapper,.fullTextCenter,.fullTextLeft'))
            .slice(0, 20)
            .map((el) => ({
              tag: el.tagName,
              cls: el.className,
              id: el.id || null,
              text: (el.innerText || '').slice(0, 200)
            }))
        };
        """
    )


def wait_for_article_text(
    driver: SafariWebDriver,
    pause_after_login_seconds: float,
    *,
    timeout_seconds: float = 20.0,
) -> dict[str, object]:
    deadline = time.monotonic() + timeout_seconds
    attempted_desktop_switch = False
    last_data: dict[str, object] | None = None

    while time.monotonic() < deadline:
        last_data = extract_article_page_data(driver)
        article_text = str(last_data.get("article_text") or "")
        if len(article_text) > 200:
            return last_data

        if not attempted_desktop_switch:
            try:
                driver.find_css("#desktopSwitch").click()
                attempted_desktop_switch = True
                time.sleep(max(pause_after_login_seconds, 3.0))
                continue
            except SafariWebDriverError:
                attempted_desktop_switch = True

        time.sleep(max(driver.min_command_interval_seconds, 1.0))

    return last_data or extract_article_page_data(driver)


def wait_for_article_links(driver: SafariWebDriver, timeout_seconds: float = 30.0) -> list[dict[str, str]]:
    deadline = time.monotonic() + timeout_seconds
    last_links: list[dict[str, str]] = []
    while time.monotonic() < deadline:
        last_links = driver.execute_script(
            """
            function parseFulltextUrl(onclickValue) {
              const text = onclickValue || '';
              const match = text.match(/SSP\\.loadFulltext\\('([^']+)'\\)/);
              if (!match) {
                return null;
              }
              return new URL(match[1], window.location.origin).href;
            }

            return Array.from(document.querySelectorAll('.hitWrapper'))
              .map((wrapper) => {
                const link = wrapper.querySelector('a.fulltextLink[href*="Start.act?articleId="]');
                if (!link) {
                  return null;
                }
                const fulltextTrigger = wrapper.querySelector('.iconFulltext[onclick]');
                return {
                  text: (link.innerText || link.textContent || '').trim(),
                  href: link.href,
                  fulltext_url: parseFulltextUrl(fulltextTrigger ? fulltextTrigger.getAttribute('onclick') : null)
                };
              })
              .filter(Boolean);
            """
        )
        if last_links:
            return last_links
        time.sleep(max(driver.min_command_interval_seconds, 1.0))
    return last_links


def current_results_page(driver: SafariWebDriver) -> int | None:
    value = driver.execute_script(
        """
        const current = document.querySelector('.resultNav .navTextcurrent');
        if (!current) {
          return null;
        }
        const page = parseInt((current.innerText || current.textContent || '').trim(), 10);
        return Number.isFinite(page) ? page : null;
        """
    )
    return int(value) if value is not None else None


def goto_results_page(driver: SafariWebDriver, page_number: int, timeout_seconds: float = 45.0) -> None:
    current_page = current_results_page(driver)
    if current_page == page_number:
        return

    goto_result = driver.execute_script(
        """
        const targetPage = String(arguments[0]);
        if (!window.SSP || !window.SSP.Navigation || typeof window.SSP.Navigation.gotoPage !== 'function') {
          return {ok: false, reason: 'Pagination function is not available on the results page.'};
        }
        window.SSP.Navigation.gotoPage('/Portal/restricted/ExtendedResultList_showDocuments.act', targetPage, 'articleSearchDIV');
        return {ok: true};
        """,
        [page_number],
    )
    if not goto_result.get("ok"):
        raise BrowserArchiveError(str(goto_result.get("reason") or f"Failed to navigate to page {page_number}."))

    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        page_now = current_results_page(driver)
        links = wait_for_article_links(driver, timeout_seconds=1.0)
        if page_now == page_number and links:
            return
        time.sleep(max(driver.min_command_interval_seconds, 1.0))

    raise BrowserArchiveError(f"Timed out waiting for results page {page_number}.")


def run_ad_hoc_inspection(
    driver: SafariWebDriver,
    keyword: str,
    from_date: str,
    to_date: str,
    page_from: int,
    page_to: int,
    pause_after_login_seconds: float,
    dump_dir: Path | None,
) -> dict[str, object]:
    if not wait_for_search_form(driver, timeout_seconds=30.0):
        raise BrowserArchiveError("No usable search form was found on the current page.")

    search_result = driver.execute_script(
        """
        const keyword = arguments[0];
        const fromDate = arguments[1];
        const toDate = arguments[2];
        const forms = Array.from(document.forms || []);
        const form = forms.find((candidate) => {
          return candidate.elements && (
            candidate.elements.namedItem('searchTerm') ||
            candidate.querySelector('input[type="text"], input[type="search"], textarea')
          );
        });
        if (!form) {
          return {ok: false, reason: 'No usable search form was found on the current page.'};
        }

        const field =
          form.elements.namedItem('searchTerm') ||
          form.querySelector('input[type="text"], input[type="search"], textarea');
        if (!field) {
          return {ok: false, reason: 'No usable search field was found on the current page.'};
        }

        field.focus();
        field.value = keyword;
        field.dispatchEvent(new Event('input', {bubbles: true}));
        field.dispatchEvent(new Event('change', {bubbles: true}));

        const fromField = form.elements.namedItem('fromDate') || document.getElementById('fromDate');
        const toField = form.elements.namedItem('toDate') || document.getElementById('toDate');
        if (fromField) {
          fromField.value = fromDate;
          fromField.dispatchEvent(new Event('input', {bubbles: true}));
          fromField.dispatchEvent(new Event('change', {bubbles: true}));
        }
        if (toField) {
          toField.value = toDate;
          toField.dispatchEvent(new Event('input', {bubbles: true}));
          toField.dispatchEvent(new Event('change', {bubbles: true}));
        }

        form.submit();
        return {
          ok: true,
          fieldName: field.name || field.id || null,
          action: form.action || null,
          fromDate: fromField ? fromField.value : null,
          toDate: toField ? toField.value : null
        };
        """,
        [keyword, from_date, to_date],
    )
    if not search_result.get("ok"):
        raise BrowserArchiveError(str(search_result.get("reason") or "Ad hoc search submission failed."))

    time.sleep(pause_after_login_seconds)
    results_html = driver.page_source()
    save_snapshot(dump_dir, "ad-hoc-after-search.html", results_html)

    articles: list[dict[str, object]] = []
    pages: list[dict[str, object]] = []
    article_index = 0
    first_result: dict[str, str] | None = None
    page_step = 1 if page_to >= page_from else -1
    for page_number in range(page_from, page_to + page_step, page_step):
        goto_results_page(driver, page_number)
        page_html = driver.page_source()
        save_snapshot(dump_dir, f"ad-hoc-results-page-{page_number:03d}.html", page_html)

        links = wait_for_article_links(driver, timeout_seconds=30.0)
        if not links:
            raise BrowserArchiveError(f"The ad hoc search returned no article links on page {page_number}.")
        if first_result is None:
            first_result = links[0]

        page_articles: list[dict[str, object]] = []
        for page_article_index, link in enumerate(links, start=1):
            article_index += 1
            open_result_article(
                driver,
                link,
                pause_after_login_seconds=pause_after_login_seconds,
            )
            article_html = driver.page_source()
            save_snapshot(dump_dir, f"ad-hoc-article-{article_index:03d}.html", article_html)

            data = wait_for_article_text(
                driver,
                pause_after_login_seconds=pause_after_login_seconds,
            )
            article_title = str(data.get("h1") or data.get("title") or link.get("text") or "article")
            downloaded_text_path = save_article_text(
                dump_dir,
                article_title=article_title,
                article_text=str(data.get("article_text") or "") or None,
                article_index=article_index,
            )
            downloaded_html_path = save_article_html(
                dump_dir,
                article_title=article_title,
                article_html=article_html,
                article_index=article_index,
            )
            article_record = {
                "index": article_index,
                "page": page_number,
                "page_index": page_article_index,
                "result": link,
                "page_data": data,
                "downloaded_text_path": downloaded_text_path,
                "downloaded_html_path": downloaded_html_path,
            }
            articles.append(article_record)
            page_articles.append(article_record)

        pages.append(
            {
                "page": page_number,
                "results_found": len(links),
                "articles": page_articles,
            }
        )

    return {
        "search": search_result,
        "page_range": {"from": page_from, "to": page_to},
        "results_found": len(articles),
        "first_result": first_result,
        "articles_downloaded": len(articles),
        "pages": pages,
        "articles": articles,
    }


def login_and_wait(driver: SafariWebDriver, username: str, password: str, start_url: str, pause_after_login_seconds: float) -> str:
    driver.navigate(start_url)
    username_input = driver.wait_for_css("input[name='j_username']", timeout_seconds=45.0)
    password_input = driver.wait_for_css("input[name='j_password']", timeout_seconds=45.0)

    username_input.clear()
    username_input.send_keys(username)
    password_input.clear()
    password_input.send_keys(password)

    try:
        driver.find_css("button[name='_eventId_proceed']").click()
    except SafariWebDriverError:
        driver.find_css("button#btnLogin").click()

    if pause_after_login_seconds > 0:
        time.sleep(pause_after_login_seconds)

    html = driver.page_source()
    return html


def wait_for_search_form(driver: SafariWebDriver, timeout_seconds: float = 30.0) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        found = driver.execute_script(
            """
            const forms = Array.from(document.forms || []);
            return forms.some((form) => form.elements && (
              form.elements.namedItem('searchTerm') ||
              form.querySelector('input[type="text"], input[type="search"], textarea')
            ));
            """
        )
        if found:
            return True
        time.sleep(max(driver.min_command_interval_seconds, 1.0))
    return False


def main() -> int:
    args = parse_args()
    if args.min_command_interval_seconds < 1.0:
        raise BrowserArchiveError("Refusing to issue WebDriver commands faster than 1 per second.")
    page_from, page_to = resolve_page_range(args)

    dump_dir = Path(args.dump_dir).resolve() if args.dump_dir else None
    driver = SafariWebDriver(
        server_url=args.webdriver_url,
        min_command_interval_seconds=args.min_command_interval_seconds,
        request_timeout_seconds=None,
    )

    try:
        driver.create_session()
        html = login_and_wait(
            driver,
            username=args.username,
            password=args.password,
            start_url=args.start_url,
            pause_after_login_seconds=args.pause_after_login_seconds,
        )
        save_snapshot(dump_dir, "after-login.html", html)

        if detect_login_page(html):
            raise BrowserArchiveError(
                "Still on the TUM login page after submitting credentials. "
                "Check the credentials or whether an additional prompt appeared."
            )

        if detect_archive_bridge_failure(html):
            raise BrowserArchiveError(
                "The browser reached the SZ archive bridge, but the archive still fell back to its own portal login. "
                "That suggests the institutional handoff itself was rejected, not just the earlier HTTP-only approach."
            )

        if args.discover_only or not args.keyword:
            json.dump(summarize_page(driver, html), sys.stdout, indent=2)
            sys.stdout.write("\n")
            return 0

        if args.ad_hoc_inspect:
            json.dump(
                run_ad_hoc_inspection(
                    driver,
                    keyword=args.keyword,
                    from_date=args.from_date,
                    to_date=args.to_date,
                    page_from=page_from,
                    page_to=page_to,
                    pause_after_login_seconds=args.pause_after_login_seconds,
                    dump_dir=dump_dir,
                ),
                sys.stdout,
                indent=2,
            )
            sys.stdout.write("\n")
            return 0

        if not wait_for_search_form(driver, timeout_seconds=30.0):
            raise BrowserArchiveError("No form with a usable search field was found on the current page.")

        search_result = driver.execute_script(
            """
            const keyword = arguments[0];
            const fromDate = arguments[1];
            const toDate = arguments[2];
            const candidates = Array.from(document.querySelectorAll('input, textarea'));
            const target = candidates.find((el) => {
              const name = (el.name || '').toLowerCase();
              const id = (el.id || '').toLowerCase();
              const placeholder = (el.placeholder || '').toLowerCase();
              const type = (el.type || '').toLowerCase();
              return ['text', 'search', 'textarea', ''].includes(type) &&
                [name, id, placeholder].some((value) =>
                  ['search', 'query', 'keyword', 'term', 'text', 'wort', 'suche'].some((token) => value.includes(token))
                );
            });
            if (!target) {
              return {ok: false, reason: 'No obvious search input was found on the current page.'};
            }
            target.focus();
            target.value = keyword;
            target.dispatchEvent(new Event('input', {bubbles: true}));
            target.dispatchEvent(new Event('change', {bubbles: true}));

            const form = target.form;
            if (form) {
              const fromField = form.elements.namedItem('fromDate') || document.getElementById('fromDate');
              const toField = form.elements.namedItem('toDate') || document.getElementById('toDate');
              if (fromField) {
                fromField.value = fromDate;
                fromField.dispatchEvent(new Event('input', {bubbles: true}));
                fromField.dispatchEvent(new Event('change', {bubbles: true}));
              }
              if (toField) {
                toField.value = toDate;
                toField.dispatchEvent(new Event('input', {bubbles: true}));
                toField.dispatchEvent(new Event('change', {bubbles: true}));
              }
              const submit = form.querySelector('button[type="submit"], input[type="submit"], button, input[type="button"], a.button');
              if (submit) {
                submit.click();
              } else {
                form.submit();
              }
              return {
                ok: true,
                fieldName: target.name || target.id || null,
                action: form.action || null,
                fromDate: fromField ? fromField.value : null,
                toDate: toField ? toField.value : null
              };
            }
            return {ok: false, reason: 'Search field was not inside a form.'};
            """,
            [args.keyword, args.from_date, args.to_date],
        )
        if not search_result.get("ok"):
            raise BrowserArchiveError(str(search_result.get("reason") or "Search submission failed."))

        time.sleep(args.pause_after_login_seconds)
        results_html = driver.page_source()
        save_snapshot(dump_dir, "after-search.html", results_html)
        result_links = extract_result_links(driver)
        if dump_dir is not None:
            links_path = dump_dir / "result-links.json"
            links_path.write_text(json.dumps(result_links, indent=2), encoding="utf-8")
        json.dump(
            {
                "title": driver.title(),
                "current_url": driver.current_url(),
                "search_field": search_result.get("fieldName"),
                "search_action": search_result.get("action"),
                "html_length": len(results_html),
                "result_links_found": len(result_links),
                "result_links_sample": result_links[:20],
            },
            sys.stdout,
            indent=2,
        )
        sys.stdout.write("\n")
        return 0
    except SafariWebDriverError as exc:
        message = str(exc)
        if "Allow remote automation" in message:
            raise BrowserArchiveError(
                "Safari WebDriver is installed, but Safari's 'Allow Remote Automation' setting is disabled. "
                "Open Safari, enable the Develop menu if needed, then turn on Develop > Allow Remote Automation."
            ) from exc
        raise BrowserArchiveError(message) from exc
    finally:
        driver.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrowserArchiveError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
