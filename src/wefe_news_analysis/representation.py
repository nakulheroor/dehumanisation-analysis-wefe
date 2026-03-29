from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from .config import ProjectConfig
from .nlp import load_german_parser
from .pipeline import ensure_directories, load_metadata_rows

TOKEN_PATTERN = re.compile(r"\b[\w'-]+\b")
SENTENCE_SPLIT_PATTERN = re.compile(r"(?<=[.!?])\s+")
PASSIVE_AUXILIARIES = {
    "bin",
    "bist",
    "ist",
    "sind",
    "seid",
    "war",
    "waren",
    "wurde",
    "wurden",
    "worden",
    "werde",
    "werden",
}
COMMON_VERBS = {
    "arbeitete",
    "arbeiten",
    "beschrieb",
    "berichtete",
    "forderte",
    "half",
    "halfen",
    "kritisierte",
    "organisierte",
    "organisierten",
    "protestierte",
    "protestierten",
    "sagte",
    "sagten",
    "sprach",
    "sprachen",
    "stahl",
    "stahlen",
    "stützte",
    "unterstützte",
    "warnte",
    "warnen",
    "arbeiteten",
    "baute",
    "bauten",
}
GERMAN_PASSIVE_PARTICIPLES = {
    "angegriffen",
    "angeklagt",
    "arrestiert",
    "beschuldigt",
    "beschrieben",
    "bedroht",
    "benachteiligt",
    "diskriminiert",
    "festgenommen",
    "getötet",
    "genannt",
    "kritisiert",
    "verletzt",
    "verhaftet",
}


@dataclass(slots=True)
class SentenceFeature:
    article_id: str
    group_name: str
    matched_term: str
    sentence_index: int
    sentence_text: str
    token_count: int
    mention_count: int
    quote_count: int
    quoted_context: int
    active_voice: int
    passive_voice: int
    lexicon_counts: dict[str, int]


@dataclass(slots=True)
class ParsedToken:
    text: str
    lower: str
    lemma: str
    dep: str
    pos: str
    index: int


@dataclass(slots=True)
class ParsedSentence:
    text: str
    tokens: list[ParsedToken]


def split_sentences(text: str) -> list[str]:
    if not text.strip():
        return []
    if any(mark in text for mark in ".!?"):
        return [segment.strip() for segment in SENTENCE_SPLIT_PATTERN.split(text) if segment.strip()]
    return [segment.strip() for segment in re.split(r"\n+", text) if segment.strip()]


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def normalize_match_text(text: str) -> str:
    return " ".join(tokenize(text))


def parse_sentences_with_fallback(text: str, config: ProjectConfig, parser=None) -> list[ParsedSentence]:
    if parser is None and config.corpus.language.lower() == "german":
        try:
            parser = load_german_parser(config.analysis.parser_model)
        except RuntimeError:
            parser = None

    if parser is not None:
        doc = parser(text)
        parsed_sentences: list[ParsedSentence] = []
        for sentence in doc.sents:
            tokens = [
                ParsedToken(
                    text=token.text,
                    lower=token.text.lower(),
                    lemma=getattr(token, "lemma_", token.text.lower()).lower(),
                    dep=getattr(token, "dep_", ""),
                    pos=getattr(token, "pos_", ""),
                    index=token.i - sentence.start,
                )
                for token in sentence
                if not getattr(token, "is_space", False)
            ]
            parsed_sentences.append(ParsedSentence(text=sentence.text.strip(), tokens=tokens))
        return parsed_sentences

    return [
        ParsedSentence(
            text=sentence,
            tokens=[
                ParsedToken(
                    text=token,
                    lower=token,
                    lemma=token,
                    dep="",
                    pos="",
                    index=index,
                )
                for index, token in enumerate(tokenize(sentence))
            ],
        )
        for sentence in split_sentences(text)
        if sentence.strip()
    ]


def find_group_mentions(tokens: list[str], terms: list[str]) -> list[tuple[int, str]]:
    mentions: list[tuple[int, str]] = []
    normalized_tokens = [token.lower() for token in tokens]

    for term in terms:
        term_tokens = tokenize(term)
        if not term_tokens:
            continue
        if len(term_tokens) == 1:
            mentions.extend(
                (index, term) for index, token in enumerate(normalized_tokens) if token == term_tokens[0]
            )
            continue

        span = len(term_tokens)
        for index in range(len(normalized_tokens) - span + 1):
            if normalized_tokens[index : index + span] == term_tokens:
                mentions.append((index, term))

    mentions.sort(key=lambda item: item[0])
    return mentions


def detect_passive_voice(tokens: list[str], mention_index: int, parsed_tokens: list[ParsedToken] | None = None) -> int:
    if parsed_tokens:
        has_passive_aux = any(token.lemma == "werden" and token.pos in {"AUX", "VERB"} for token in parsed_tokens)
        mention_token = parsed_tokens[mention_index]
        if has_passive_aux and mention_token.dep in {"sb", "nsubj", "sbp"}:
            return 1

    window = tokens[max(0, mention_index - 4) : min(len(tokens), mention_index + 9)]
    for index, token in enumerate(window):
        if token in PASSIVE_AUXILIARIES:
            following_tokens = window[index + 1 : index + 7]
            if any(
                candidate in GERMAN_PASSIVE_PARTICIPLES or candidate.startswith("ge")
                for candidate in following_tokens
            ):
                return 1
    return 0


def detect_active_voice(tokens: list[str], mention_index: int, parsed_tokens: list[ParsedToken] | None = None) -> int:
    if parsed_tokens:
        mention_token = parsed_tokens[mention_index]
        has_passive_aux = any(token.lemma == "werden" and token.pos in {"AUX", "VERB"} for token in parsed_tokens)
        if mention_token.dep in {"sb", "nsubj"} and not has_passive_aux:
            return 1

    trailing = tokens[mention_index + 1 : mention_index + 5]
    if trailing and trailing[0] in PASSIVE_AUXILIARIES:
        return 0
    for token in trailing:
        if token in COMMON_VERBS or token.endswith("en") or token.endswith("te"):
            return 1
    return 0


def count_phrase_hits(window_text: str, phrase: str) -> int:
    normalized_phrase = normalize_match_text(phrase)
    if not normalized_phrase:
        return 0
    pattern = re.compile(rf"(?<!\w){re.escape(normalized_phrase)}(?!\w)")
    return len(pattern.findall(window_text))


def count_lexicon_hits(
    tokens: list[str],
    lexicons: dict[str, list[str]],
    mention_index: int,
    window_size: int,
    sentence_text: str,
) -> dict[str, int]:
    lower_bound = max(0, mention_index - window_size)
    upper_bound = min(len(tokens), mention_index + window_size + 1)
    window_tokens = tokens[lower_bound:upper_bound]
    window_text = " ".join(window_tokens)
    sentence_match_text = normalize_match_text(sentence_text)
    counts: dict[str, int] = {}
    for name, words in lexicons.items():
        count = 0
        for word in words:
            normalized_word = normalize_match_text(word)
            if not normalized_word:
                continue
            if " " in normalized_word:
                count += count_phrase_hits(sentence_match_text, normalized_word)
                continue

            for token in window_tokens:
                if token == normalized_word or (
                    len(normalized_word) >= 5 and (token.startswith(normalized_word) or token.endswith(normalized_word))
                ):
                    count += 1
        counts[name] = count
    return counts


def is_quoted_context(sentence_text: str) -> int:
    quote_marks = ['"', "“", "”", "„", "«", "»", "'"]
    return int(sum(sentence_text.count(mark) for mark in quote_marks) >= 2)


def compute_dehumanization_score(lexicon_counts: dict[str, int], passive_voice: int, humanizing_hits: int) -> float:
    severe_categories = {"dehumanizing", "collectivizing", "erasure_of_civilian_status"}
    incitement_categories = {"incitement_displacement", "incitement_destruction"}
    repression_categories = {"criminalizing", "discrediting_journalists", "censorship_repression"}

    score = 0.0
    for name, count in lexicon_counts.items():
        if name in severe_categories:
            score += 2.0 * count
        elif name in incitement_categories:
            score += 2.5 * count
        elif name in repression_categories:
            score += 1.5 * count
        elif name == "victimizing":
            score += 0.5 * count

    score += 0.5 * passive_voice
    score -= 1.0 * humanizing_hits
    return round(score, 4)


def analyze_article_text(article_id: str, text: str, config: ProjectConfig, parser=None) -> list[SentenceFeature]:
    features: list[SentenceFeature] = []
    for sentence_index, sentence in enumerate(parse_sentences_with_fallback(text, config, parser), start=1):
        tokens = [token.lower for token in sentence.tokens]
        if not tokens:
            continue

        for group_name, terms in config.analysis.target_groups.items():
            mentions = find_group_mentions(tokens, terms)
            for mention_index, matched_term in mentions:
                features.append(
                    SentenceFeature(
                        article_id=article_id,
                        group_name=group_name,
                        matched_term=matched_term,
                        sentence_index=sentence_index,
                        sentence_text=sentence.text,
                        token_count=len(tokens),
                        mention_count=len(mentions),
                        quote_count=sentence.text.count('"') + sentence.text.count("'"),
                        quoted_context=is_quoted_context(sentence.text),
                        active_voice=detect_active_voice(tokens, mention_index, sentence.tokens),
                        passive_voice=detect_passive_voice(tokens, mention_index, sentence.tokens),
                        lexicon_counts=count_lexicon_hits(
                            tokens,
                            config.analysis.framing_lexicons,
                            mention_index,
                            config.analysis.context_window_tokens,
                            sentence.text,
                        ),
                    )
                )
    return features


def sentence_feature_rows(features: list[SentenceFeature], metadata_rows: dict[str, dict[str, str]]) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for feature in features:
        row: dict[str, str | int] = {
            "article_id": feature.article_id,
            "group_name": feature.group_name,
            "matched_term": feature.matched_term,
            "sentence_index": feature.sentence_index,
            "sentence_text": feature.sentence_text,
            "token_count": feature.token_count,
            "mention_count": feature.mention_count,
            "quote_count": feature.quote_count,
            "quoted_context": feature.quoted_context,
            "active_voice": feature.active_voice,
            "passive_voice": feature.passive_voice,
        }
        row.update(feature.lexicon_counts)
        row.update(metadata_rows.get(feature.article_id, {}))
        rows.append(row)
    return rows


def aggregate_article_group_rows(features: list[SentenceFeature], metadata_rows: dict[str, dict[str, str]]) -> list[dict[str, str | int | float]]:
    grouped: dict[tuple[str, str], dict[str, int | str]] = {}
    sentence_tracker: dict[tuple[str, str], set[int]] = defaultdict(set)

    for feature in features:
        key = (feature.article_id, feature.group_name)
        if key not in grouped:
            grouped[key] = {
                "article_id": feature.article_id,
                "group_name": feature.group_name,
                "mention_instances": 0,
                "sentence_mentions": 0,
                "active_voice_mentions": 0,
                "passive_voice_mentions": 0,
                "quote_count": 0,
                "quoted_mentions": 0,
            }
            for lexicon_name in feature.lexicon_counts:
                grouped[key][f"{lexicon_name}_count"] = 0

        grouped[key]["mention_instances"] += 1
        grouped[key]["active_voice_mentions"] += feature.active_voice
        grouped[key]["passive_voice_mentions"] += feature.passive_voice
        grouped[key]["quote_count"] += feature.quote_count
        grouped[key]["quoted_mentions"] += feature.quoted_context
        sentence_tracker[key].add(feature.sentence_index)

        for lexicon_name, count in feature.lexicon_counts.items():
            grouped[key][f"{lexicon_name}_count"] += count

    rows: list[dict[str, str | int | float]] = []
    for key, row in grouped.items():
        row["sentence_mentions"] = len(sentence_tracker[key])
        mention_instances = int(row["mention_instances"])
        row["active_voice_rate"] = round(int(row["active_voice_mentions"]) / mention_instances, 4)
        row["passive_voice_rate"] = round(int(row["passive_voice_mentions"]) / mention_instances, 4)
        row["quoted_context_rate"] = round(int(row["quoted_mentions"]) / mention_instances, 4)
        lexicon_counts = {
            key.removesuffix("_count"): int(value)
            for key, value in row.items()
            if key.endswith("_count")
        }
        row["dehumanization_score"] = compute_dehumanization_score(
            lexicon_counts,
            int(row["passive_voice_mentions"]),
            lexicon_counts.get("humanizing", 0),
        )
        row.update(metadata_rows.get(row["article_id"], {}))
        rows.append(row)

    return sorted(rows, key=lambda item: (str(item["article_id"]), str(item["group_name"])))


def write_csv(
    path: Path,
    rows: list[dict[str, str | int | float]],
    encoding: str,
    default_fieldnames: list[str],
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(default_fieldnames)
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    with path.open("w", encoding=encoding, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def analyze_representation(config: ProjectConfig) -> tuple[Path, Path]:
    ensure_directories(config)
    metadata_rows = load_metadata_rows(config)
    text_files = sorted(config.corpus.processed_text_dir.glob("*.txt"))
    parser = None
    if config.corpus.language.lower() == "german":
        try:
            parser = load_german_parser(config.analysis.parser_model)
        except RuntimeError:
            parser = None

    features: list[SentenceFeature] = []
    for text_path in text_files:
        article_id = text_path.stem
        text = text_path.read_text(encoding=config.corpus.default_encoding)
        features.extend(analyze_article_text(article_id, text, config, parser))

    sentence_rows = sentence_feature_rows(features, metadata_rows)
    article_group_rows = aggregate_article_group_rows(features, metadata_rows)
    metadata_fieldnames = sorted({key for row in metadata_rows.values() for key in row})
    sentence_default_fields = [
        "article_id",
        "group_name",
        "matched_term",
        "sentence_index",
        "sentence_text",
        "token_count",
        "mention_count",
        "quote_count",
        "quoted_context",
        "active_voice",
        "passive_voice",
        *config.analysis.framing_lexicons.keys(),
        *metadata_fieldnames,
    ]
    article_group_default_fields = [
        "article_id",
        "group_name",
        "mention_instances",
        "sentence_mentions",
        "active_voice_mentions",
        "passive_voice_mentions",
        "quote_count",
        "quoted_mentions",
        *[f"{name}_count" for name in config.analysis.framing_lexicons],
        "active_voice_rate",
        "passive_voice_rate",
        "quoted_context_rate",
        "dehumanization_score",
        *metadata_fieldnames,
    ]

    sentence_path = write_csv(
        config.analysis.outputs.sentence_features_path,
        sentence_rows,
        config.corpus.default_encoding,
        sentence_default_fields,
    )
    article_group_path = write_csv(
        config.analysis.outputs.article_group_features_path,
        article_group_rows,
        config.corpus.default_encoding,
        article_group_default_fields,
    )
    return sentence_path, article_group_path
