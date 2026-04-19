# OHCHR Media Narratives Rubric

This rubric is tailored to article-level analysis for the OHCHR 2026 call on the role of media in the context of Israel's policies and practices toward the Palestinian people, with a focus on section 2: media narratives and discursive practices.

It is designed for structured coding of individual articles. It can suggest patterns consistent with editorial positioning, but it should not be used on its own to make strong outlet-level claims about institutional editorial lines without analyzing a larger corpus.

Edit the JSON block below to add, remove, or change analysis fields without changing the code.

```json
{
  "global_instructions": "Analyze only what is supported by the supplied article text. Distinguish between explicit statements, implied framing, and uncertain cases. If evidence is weak or ambiguous, say so. Do not infer an outlet-wide editorial policy from one article alone. Use concise evidence-based language.",
  "fields": {
    "palestinian_civilian_status_representation": {
      "type": "string",
      "description": "How the article represents Palestinians with respect to civilian status. Choose recognized if the article clearly identifies affected Palestinians as civilians or otherwise clearly marks them as non-combatants, for example through terms such as civilians, civilian population, innocents, families, children, women, patients, aid workers, journalists, residents, or equivalent wording that clearly distinguishes them from fighters. Do not use recognized if the article explicitly introduces unresolved counterclaims that blur whether the relevant Palestinians are civilians. In such cases use partially_or_implicitly_denied. Choose partially_or_implicitly_denied if civilian status would be relevant but is not clearly recognized, or if it is recognized but then blurred, qualified, or contested. This includes cases where the article uses generic terms such as Palestinians, people, population, or individuals without clearly identifying civilian status; describes deaths, injuries, displacement, or humanitarian harm without clearly identifying those affected as civilians; or mixes civilian references with unresolved claims about militants, fighters, terrorists, human shields, or militant use of civilian sites. Choose explicitly_denied if the article clearly labels the relevant Palestinians as militants, combatants, terrorists, or legitimate military targets, or directly rejects civilian classification. Choose not_applicable if the article mentions Palestinians, Palestine, Gaza, or pro-Palestinian actors but does not discuss Palestinian deaths, injuries, displacement, detention, humanitarian harm, vulnerability to attack, or any other context in which civilian status would matter, for example in articles mainly about protests, slogans, diplomacy, party politics, or cultural controversy. Evidence snippets for this field should directly support how the article represents Palestinian civilian status. Prefer snippets that refer to civilians or clearly civilian groups, or that explicitly classify people as militants, fighters, terrorists, combatants, or targets. Do not use snippets that merely mention Palestinians, Palestine, or Gaza without bearing on civilian or combatant status.",
      "enum": ["recognized", "partially_or_implicitly_denied", "explicitly_denied", "not_applicable"]
    },
    "palestinian_civilian_status_representation_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for palestinian_civilian_status_representation.",
      "items": {
        "type": "string"
      }
    },
    "dehumanization_forms": {
      "type": "array",
      "description": "Select all categories of dehumanizing discourse toward Palestinians that are clearly supported by the article text. Leave this array empty if no category is clearly supported. Use animalistic_or_objectifying_language when Palestinians are described through animal comparisons, infestation language, subhuman imagery, or object-like terms that strip personhood, including wording that treats them primarily as targets, collateral, or obstacles rather than people. Do not use this category for ordinary military terminology unless Palestinians themselves are being reduced to objects. Use collective_threat_framing when Palestinians are portrayed as a single dangerous mass or population-level threat, with little or no distinction among individuals, civilians, or subgroups. Do not use this category merely because the article discusses security threats from Hamas or other armed groups; use it only when the threat framing extends to Palestinians broadly. Use erasure_of_individual_humanity when Palestinians are presented in a way that suppresses individuality, personhood, or lived human status, for example as an anonymous mass, as statistics only, or as bodies without names, relationships, voices, or human descriptors where such humanization would normally be relevant. Do not use this category for brief or routine casualty reporting alone; use it only when the article's framing reduces Palestinians to impersonal units or abstracts away their humanity. Use justification_or_normalization_of_harm when harm to Palestinians is presented as deserved, inevitable, acceptable, morally unproblematic, or not requiring serious concern. This includes statements implying they brought it on themselves, that harsh treatment is necessary, or that large-scale suffering is simply the natural price to be paid. Do not use this category for factual descriptions of harm, military action, or competing political arguments unless the article clearly endorses or normalizes the harm. Use denial_of_civilian_existence when the article explicitly denies that Palestinian civilians exist, denies the relevance of Palestinian civilian status, or claims there are no innocents, no civilians, or no uninvolved people among Palestinians in the relevant setting. Do not use this category when civilian status is merely unclear, disputed, or underdescribed; use it only for direct or near-direct denial.",
      "items": {
        "type": "string",
        "enum": [
          "animalistic_or_objectifying_language",
          "collective_threat_framing",
          "erasure_of_individual_humanity",
          "justification_or_normalization_of_harm",
          "denial_of_civilian_existence"
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
    "discrediting_palestinian_journalists": {
      "type": "string",
      "description": "How the article treats Palestinian journalists and their reporting. Use discrediting when the article explicitly or implicitly casts doubt on the credibility, independence, honesty, authenticity, or professional legitimacy of Palestinian journalists, Palestinian photojournalists, Gaza-based reporters, or other Palestinian media workers. This includes suggestions that they are linked to Hamas or other armed groups; are acting as propagandists rather than journalists; are staging, manipulating, fabricating, or falsifying reporting, images, footage, or casualty documentation; or are unreliable because of political affiliation, identity, or location. Questions, insinuations, and attributed accusations can still count as discrediting when they foreground suspicion, for example asking whether Palestinian journalists were instrumentally used by Hamas or stating that someone presented as a journalist was really a militant or only posing as a journalist. Use none when Palestinian journalists are discussed without such doubt, or are presented as credible, trustworthy, or ordinary journalistic sources. Use not_applicable when the article does not discuss Palestinian journalists specifically. Do not code this field for criticism of media in general, Israeli media, Western media, social media users, or non-Palestinian journalists unless the article is specifically discussing Palestinian journalists. Evidence snippets should capture the actual discrediting or credibility-granting language, not merely any mention of journalism or media.",
      "enum": ["discrediting", "none", "not_applicable"]
    },
    "discrediting_palestinian_journalists_evidence_snippets": {
      "type": "array",
      "description": "Short quotations or text snippets that support the classification for discrediting_palestinian_journalists.",
      "items": {
        "type": "string"
      }
    }
  }
}
```
