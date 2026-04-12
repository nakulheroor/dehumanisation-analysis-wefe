# OHCHR Media Narratives Rubric

This rubric is tailored to article-level analysis for the OHCHR 2026 call on the role of media in the context of Israel's policies and practices toward the Palestinian people, with a focus on section 2: media narratives and discursive practices.

It is designed for structured coding of individual articles. It can suggest patterns consistent with editorial positioning, but it should not be used on its own to make strong outlet-level claims about institutional editorial lines without analyzing a larger corpus.

Edit the JSON block below to add, remove, or change analysis fields without changing the code.

```json
{
  "global_instructions": "Analyze only what is supported by the supplied article text. Distinguish between explicit statements, implied framing, and uncertain cases. If evidence is weak or ambiguous, say so. Do not infer an outlet-wide editorial policy from one article alone. Use concise evidence-based language.",
  "fields": {
    "article_relevance": {
      "type": "string",
      "description": "Whether the article is relevant to the OHCHR focus on reporting about events in the occupied Palestinian territory after October 7, 2023.",
      "enum": ["high", "medium", "low", "none"]
    },
    "article_type": {
      "type": "string",
      "description": "Journalistic format of the piece.",
      "enum": ["news_report", "analysis", "opinion", "editorial", "interview", "live_blog", "other"]
    },
    "primary_frame": {
      "type": "string",
      "description": "Main interpretive frame used to organize the article, such as security or terrorism, humanitarian crisis, diplomacy, military necessity, law or crimes, or social disorder."
    },
    "problem_definition": {
      "type": "string",
      "description": "How the article defines the central problem, event, or conflict dynamic."
    },
    "causal_attribution": {
      "type": "string",
      "description": "Who or what the article presents as responsible for the situation. Who or what the article presents as the victim. "
    },
    "moral_evaluation": {
      "type": "string",
      "description": "The article's explicit or implicit moral evaluation of the actors and events."
    },
    "proposed_or_implied_remedy": {
      "type": "string",
      "description": "Any explicit or implied solution, response, or justified course of action."
    },
    "palestinian_civilian_status_representation": {
      "type": "string",
      "description": "How Palestinians are represented with respect to civilian status.",
      "enum": ["recognized", "partially_denied", "implicitly_denied", "explicitly_denied", "not_applicable"]
    },
    "palestinian_civilian_status_representation_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for palestinian_civilian_status_representation.",
      "items": {
        "type": "string"
      }
    },
    "dehumanization_present": {
      "type": "boolean",
      "description": "Whether the article contains dehumanizing portrayals of Palestinians."
    },
    "dehumanization_present_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for dehumanization_present.",
      "items": {
        "type": "string"
      }
    },
    "dehumanization_forms": {
      "type": "array",
      "description": "Types of dehumanizing discourse present in the article.",
      "items": {
        "type": "string",
        "enum": [
          "undifferentiated_enemy",
          "denial_of_civilian_status",
          "collective_guilt",
          "denial_of_agency_or_subjectivity",
          "moral_disgust",
          "animalizing_or_vermin_metaphor",
          "erasure_of_suffering",
          "other"
        ]
      }
    },
    "dehumanization_forms_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for dehumanization_forms.",
      "items": {
        "type": "string"
      }
    },
    "incitement_or_advocacy_of_crimes": {
      "type": "string",
      "description": "Whether the piece includes explicit or implicit calls for acts that may amount to international crimes.",
      "enum": ["none", "implicit", "explicit", "unclear"]
    },
    "incitement_or_advocacy_of_crimes_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for incitement_or_advocacy_of_crimes.",
      "items": {
        "type": "string"
      }
    },
    "incitement_targets_or_actions": {
      "type": "array",
      "description": "Specific harmful actions advocated, justified, or normalized.",
      "items": {
        "type": "string",
        "enum": [
          "mass_displacement",
          "destruction_of_gaza",
          "collective_punishment",
          "starvation_or_siege",
          "indiscriminate_killing",
          "other"
        ]
      }
    },
    "discrediting_palestinian_journalists": {
      "type": "string",
      "description": "How the article treats Palestinian journalists and their reporting.",
      "enum": ["none", "implicit_discrediting", "explicit_discrediting", "mixed", "not_applicable"]
    },
    "discrediting_palestinian_journalists_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for discrediting_palestinian_journalists.",
      "items": {
        "type": "string"
      }
    },
    "disinformation_or_unverified_claims": {
      "type": "string",
      "description": "Assessment of whether the article relays serious claims without adequate verification, correction, or qualification."
    },
    "source_visibility_balance": {
      "type": "string",
      "description": "Overall degree of imbalance in whose voices are quoted, paraphrased, or treated as authoritative in the article.",
      "enum": ["heavily_skewed", "somewhat_skewed", "roughly_balanced", "not_applicable"]
    },
    "source_visibility_skew_direction": {
      "type": "string",
      "description": "If the article's source visibility is skewed, indicate toward which side or institutional perspective it is skewed.",
      "enum": [
        "toward_israeli_official_or_pro_israeli_sources",
        "toward_palestinian_or_pro_palestinian_sources",
        "toward_other_international_official_sources",
        "mixed_or_unclear",
        "not_applicable"
      ]
    },
    "palestinian_voice_presence": {
      "type": "string",
      "description": "Whether Palestinians appear as speaking subjects, credible witnesses, or only as objects of discussion.",
      "enum": ["substantial", "limited", "minimal", "absent"]
    },
    "palestinian_voice_presence_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for palestinian_voice_presence.",
      "items": {
        "type": "string"
      }
    },
    "israeli_voice_presence": {
      "type": "string",
      "description": "Whether Israelis appear as speaking subjects, credible witnesses, or only as objects of discussion.",
      "enum": ["substantial", "limited", "minimal", "absent"]
    },
    "israeli_voice_presence_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for israeli_voice_presence.",
      "items": {
        "type": "string"
      }
    },
    "evidence_of_editorial_line_in_article": {
      "type": "string",
      "description": "Whether this article itself contains signs of routinized editorial positioning, recognizing that outlet-level judgment requires multiple articles.",
      "enum": ["none", "possible", "strong", "insufficient_basis"]
    },
    "international_law_presence": {
      "type": "string",
      "description": "Whether this article talks about international law. ",
    },
    "confidence": {
      "type": "integer",
      "description": "Confidence in the coding on a scale from 1 to 5.",
      "minimum": 1,
      "maximum": 5
    },
    "evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets from the article that support the coding decisions.",
      "items": {
        "type": "string"
      }
    }
  }
}
```
