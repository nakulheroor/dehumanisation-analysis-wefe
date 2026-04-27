# Qualitative Analysis of WEAT and WEFAT Results
## Süddeutsche Zeitung Coverage of the Israel-Palestine Conflict, October 2023 – October 2024

**Corpus**: 2,522 articles from the Süddeutsche Zeitung (SZ), Germany's largest quality newspaper  
**Method**: Word Embedding Association Test (WEAT) and Word Embedding Fairness Association Test (WEFAT) on a Word2Vec model trained on the corpus  
**Research context**: Submission to the UN Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression — *The Role of Media in the Context of Israel's Actions toward the Palestinian People*

---

## Methodological Note

WEAT measures **relative bias**: how much more one target group (e.g., *Palestinian journalists*) is associated with one set of attributes (e.g., *violence vocabulary*) compared to a second target group (e.g., *general journalists*) and a second attribute set (e.g., *press-freedom vocabulary*). A positive effect size means the first target group is relatively more associated with the first attribute set. Effect sizes above 0.5 are considered moderate; above 0.8, strong.

WEFAT measures **absolute bias**: the mean cosine-similarity difference between a single target group and two competing attribute sets, without needing a comparison group. A positive WEFAT score means the target group is, in absolute terms, embedded closer to the first attribute set than the second. The WEFAT effect size normalises this difference by the spread across individual target words.

Both tests operate on distributional semantics: they capture how words are *used together* in the corpus, not explicit editorial statements.

---

## Part I — WEAT Results

### 1. Targeting and Repression of Palestinian Journalists

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_targeting_violence` | **0.755** | Palestinian journalist vocabulary is substantially more embedded in targeting/violence contexts than general journalist vocabulary, relative to press-freedom discourse. |
| `journalist_detention_disappearance` | **0.704** | Palestinian journalist terms co-occur markedly more with detention and disappearance vocabulary (arrest, abduction, captivity) than general journalist terms. |
| `journalist_harassment_intimidation` | **0.669** | Palestinian journalist vocabulary is significantly more embedded in harassment/intimidation contexts (threats, surveillance, pursuit). |
| `journalist_terror_labelling` | **0.636** | Palestinian journalist terms are substantially more associated with terrorist-labelling vocabulary (militant, extremist, jihad) than general journalist references, relative to press-freedom terms. |
| `journalist_family_targeting` | **0.654** | Palestinian journalist vocabulary co-occurs considerably more with vocabulary about targeting of family members, compared to press-freedom framings. |
| `journalist_access_exclusion_parity` | **0.197** | Palestinian journalists are somewhat more embedded in exclusion/blackout discourse than foreign journalists, though this signal is relatively weak. |

**Interpretation**: Across all six sub-dimensions of journalist repression, the embedding model positions Palestinian journalist vocabulary closer to repression vocabulary than any comparison group. The strongest signals — targeting/violence (0.755) and detention/disappearance (0.704) — indicate that the SZ corpus systematically embeds Palestinian journalist references in contexts of physical violence and deprivation of liberty. This is consistent with reporting that documents events (killings, arrests) but does not counterbalance those reports with press-freedom framings. The terrorist-labelling association (0.636) suggests that Palestinian journalists are regularly encountered in articles that also use militant/extremist vocabulary, even if the SZ itself is not deploying such labels directly — the proximity in embedding space reflects co-occurrence patterns in context.

The access/exclusion signal is weaker (0.197), possibly because the SZ reports the information blackout in Gaza through general descriptions of the situation rather than repeatedly linking it to the figure of the Palestinian journalist specifically.

---

### 2. Dehumanisation and Denial of Civilian Status

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `palestinian_civilian_erasure` | **1.035** | STRONG: Palestinian terms are far more embedded in civilian-status-erasure vocabulary (collaborator, human shield, complicit, fighter) than generic civilian vocabulary. |
| `palestinian_dehumanization` | **0.998** | STRONG: Palestinian terms are substantially more associated with dehumanising language (wave, flood, barbaric, horror, atrocity) than generic civilian references. |
| `coded_incitement` | **0.556** | Palestinian terms are moderately more associated with coded escalation vocabulary (cleanse, pacify, purge) than civilian references, relative to civilian-protection discourse. |
| `institutional_editorial_line` | **1.030** | STRONG: Palestinian terms are far more embedded in editorial-line/propaganda vocabulary (campaign, narrativ, propaganda, line) than civilian references, relative to editorial-independence vocabulary. |

**Interpretation**: The most striking findings concern dehumanisation and civilian erasure. Effect sizes above 1.0 are very strong in the WEAT framework. The civilian erasure result (1.035) means the model has learned to situate Palestinian identity references in the same semantic neighbourhood as vocabulary that strips civilians of their protected status — calling them fighters, shields, or accomplices. This is not necessarily because the SZ uses such terms of Palestinians itself; it reflects that Palestinian references appear in articles that *discuss* these framings (often to quote Israeli military or government sources, or to describe the content of debates). The fact that the corpus embeds these terms together means a reader — and a language model — would implicitly associate Palestinian identity with contested civilian status.

The institutional editorial line result (1.030) is equally striking: Palestinian references are systematically more embedded in propaganda/narrative/campaign vocabulary than generic civilian references. This may indicate that Palestinian perspectives are primarily encountered in the SZ as objects of *narrative contests* — discussions of Hamas propaganda, pro-Palestinian campaigns, or information warfare — rather than as sources of authoritative testimony.

The dehumanisation score (0.998) corroborates this: Palestinian terms co-occur significantly more with vocabulary used in dehumanising discourse (wave, flood, horror) compared to generic references to civilians. Many of these terms appear in articles describing Hamas attacks on Israel, where vocabulary like "Schrecken" (horror) and "Barbarei" (barbarism) is used. The shared embedding with Palestinian identity terms reflects that Palestinian identity and barbaric violence vocabulary are repeatedly encountered in the same textual contexts.

---

### 3. Israel–Palestine Comparative Framing

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `israel_palestine_violence_framing` | **0.813** | STRONG: Palestinians are substantially more associated with violent/negative violence vocabulary than Israelis, who are relatively more associated with defensive/positive framing. |
| `israel_palestine_death_language` | **0.660** | Palestinians are moderately more associated with euphemistic death vocabulary (died, passed, deceased) than Israelis, who are relatively more associated with direct death vocabulary (murdered, massacre, killing). |
| `israel_palestine_credibility_framing` | **−0.535** | REVERSAL: Israeli sources are more associated with credibility-negative language (alleged, claimed, supposed, doubt) than Palestinian sources. |

**Interpretation**: The violence-framing asymmetry (0.813) is substantial: Palestinian actors are embedded much more deeply in vocabulary associated with terrorism, extremism, and brutal violence, while Israeli actors are embedded relatively more in vocabulary of defence, security, and self-protection. This tracks the standard framing of the conflict in Western media: Hamas attacks are described with maximally strong condemnatory vocabulary; Israeli military operations are described in terms of security and defence. The SZ, despite being a liberal quality newspaper, reproduces this asymmetry at the level of embedding structure.

The death-language finding (0.660) is counter-intuitive and analytically important. Palestinian deaths are described more often with *soft* death vocabulary (tod, gestorben, tot, umkommen) while Israeli deaths — in particular the October 7 massacre — are described with *direct* murder vocabulary (ermordet, massaker, mord). This is not dehumanisation by softening Palestinian deaths per se; it reflects that the corpus contains extensive October 7 coverage that uses extremely direct violence vocabulary (massacre, murdered) in the context of Israeli victims. Palestinian civilian deaths in Gaza are more often reported in aggregate, aggregate numbers being accompanied by softer vocabulary. The embedding model captures this asymmetric expressiveness.

The credibility reversal (−0.535) is the most unexpected finding. Israeli sources are more associated with hedging/credibility-negative vocabulary than Palestinian sources. A plausible explanation is that the SZ — a critical-liberal newspaper — frequently applies epistemological scrutiny to Israeli government and military statements, using "angeblich" (alleged), "mutmaßlich" (supposed), and "behauptung" (claim) when reporting on Israeli narratives about Gaza, targeted strikes, and casualty figures. This signals something important: the SZ applies journalist standards of source skepticism more visibly to Israeli governmental claims than to Palestinian ones, possibly because Palestinian accounts rarely appear as direct institutional claims that require the same level of epistemic qualification.

---

### 4. Media Infrastructure and Access

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `foreign_press_exclusion_blackout` | **0.658** | Foreign journalists are substantially more associated with exclusion/blackout vocabulary than general journalists, relative to press-freedom discourse. |
| `media_infrastructure_disruption` | **−0.670** | REVERSAL: Media infrastructure terms are more associated with telecom disruption than physical destruction, while media institution terms are more associated with physical infrastructure destruction. |
| `journalist_access_exclusion_parity` | **0.197** | Palestinian journalist vocabulary is somewhat more associated with exclusion than foreign journalists. |

**Interpretation**: The foreign press exclusion result (0.658) indicates that the SZ extensively covers the exclusion of international journalists from Gaza in terms of blackout and access denial — this is logically expected given that Israel restricted foreign press access to Gaza throughout the conflict period. The inversion in `media_infrastructure_disruption` (−0.670) is analytically interesting: media *institutions* (editorial offices, news agencies) are more embedded in physical destruction vocabulary, while *infrastructure* (cameras, transmission equipment, networks) is more embedded in telecom disruption. This may reflect a reporting pattern where the destruction of Al Jazeera offices or news bureau buildings is reported alongside coverage of digital/communications blackouts as a distinct phenomenon.

---

### 5. Disinformation and Censorship Framings

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_disinformation` | **0.471** | Palestinian journalist vocabulary is moderately more associated with disinformation/discrediting vocabulary than general journalists, relative to editorial independence. |
| `journalist_professionalism_contestation` | **0.287** | Palestinian journalist vocabulary is weakly but consistently more associated with discrediting vocabulary than general journalists, relative to professional journalism norms. |
| `censorship_retaliation` | **0.511** | Palestinian journalist vocabulary is moderately more associated with censorship/retaliation vocabulary than general journalists, relative to press freedom. |
| `legal_accountability_obscuring` | **0.473** | Palestinian references are moderately more embedded in legal accountability vocabulary than civilian references, relative to disinformation vocabulary. |

**Interpretation**: The disinformation result (0.471) indicates that Palestinian journalist references co-occur meaningfully more with propaganda, discrediting, and manipulation vocabulary than generic journalist references. This likely reflects the regular appearance of Israeli characterisations of Palestinian media as "Hamas mouthpieces" in articles that cite or engage with Israeli positions — the SZ reports this framing rather than endorsing it, but the co-occurrence still shapes the embedding structure.

The legal accountability result (0.473) shows an opposite pattern to what one might expect: Palestinian references are more embedded in legal accountability language (war crimes, evidence, international law, accountability) than generic civilian references. This reflects the extensive SZ coverage of ICJ proceedings, international law debates, and accountability frameworks specifically in the context of Gaza — meaning Palestinian experiences are frequently encountered alongside legal accountability discourse, which is substantively appropriate but confirms that the SZ does engage with the legal dimension of the conflict.

---

### 6. Incitement-Related Findings

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `genocide_incitement` | **0.295** | Palestinian terms are weakly-to-moderately more associated with genocide incitement vocabulary than civilian references. |
| `coded_incitement` | **0.556** | Palestinian terms are moderately more associated with coded escalation vocabulary. |
| `mass_displacement_incitement` | **0.465** | Palestinian terms are moderately more associated with mass displacement vocabulary than civilian references. |
| `gaza_destruction_incitement` | **0.172** | Palestinian terms are weakly associated with Gaza destruction vocabulary compared to civilian references — the weakest WEAT incitement signal. |

**Interpretation**: All four incitement-related experiments show positive effects, consistently placing Palestinian references in closer proximity to incitement vocabulary than generic civilian references. The weak Gaza destruction signal (0.172) is noteworthy: vocabulary directly about destroying Gaza physically is not strongly differentiated between Palestinian and civilian embedding contexts. This may reflect that destruction vocabulary in the corpus is associated broadly with the conflict rather than specifically with Palestinian identity. The coded incitement signal (0.556) is stronger, suggesting that softer escalatory vocabulary (purge, pacify, clean) co-occurs more with Palestinian references than generic civilian ones.

---

## Part II — WEFAT Results (Absolute Associations)

WEFAT allows measurement of a group's *absolute* embedding position relative to two attribute sets, without requiring a comparison group. This complements WEAT by revealing what the corpus does to a group on its own terms.

| Experiment | WEFAT Score | Effect Size | Interpretation |
|---|---|---|---|
| `wefat_mass_displacement_absolute` | 0.052 | **1.533** | STRONGEST SIGNAL: Palestinians are absolutely positioned closer to mass displacement vocabulary than civilian protection vocabulary. |
| `wefat_genocide_incitement_absolute` | 0.042 | **0.677** | Palestinians are moderately absolutely associated with genocide incitement vocabulary vs. civilian protection. |
| `wefat_palestinians_dehumanization_absolute` | 0.030 | **0.555** | Palestinians have a moderate absolute association with dehumanising vocabulary vs. humanising vocabulary. |
| `wefat_civilians_erasure_absolute` | −0.0001 | −0.002 | Generic civilian terms are essentially *neutral* between erasure and humanising vocabulary. |
| `wefat_media_institutions_destruction_absolute` | −0.005 | −0.070 | Media institution terms are essentially neutral, marginally more associated with press freedom than destruction. |
| `wefat_palestinian_journalists_violence_absolute` | −0.002 | −0.031 | Palestinian journalist terms are essentially neutral in absolute terms between violence and press freedom vocabulary. |

**Interpretation**: The WEFAT results reveal important distinctions between absolute and relative bias.

The most significant finding is the Palestinian mass displacement absolute association (effect size 1.533): this is the strongest single result in the entire analysis. Palestinian vocabulary — "Gaza", "Palestinians", "West Bank" — is embedded in an absolute sense substantially closer to vocabulary about forced displacement, expulsion, and flight than to vocabulary about civilian protection. This is a property of the embedding space itself: any model trained on this corpus will have learned that Palestinian identity and displacement are semantically proximate in an absolute, not merely relative, sense.

By contrast, Palestinian journalist vocabulary is essentially neutral in absolute terms (effect −0.031) — yet shows significant *relative* bias against general journalists in WEAT (0.755). This is analytically important: Palestinian journalist identity by itself is not absolutely situated in a violence semantic field, but it is situated there *relative to* general journalist identity. This means the comparative framing matters: Palestinian journalists are reported as journalists but the specific context of their mention is systematically more violent than the context in which general journalists are mentioned.

Similarly, generic civilian terms show near-zero absolute erasure association (−0.002), while Palestinian terms show strong WEAT erasure association (1.035). This contrast confirms that the denial-of-civilian-status discourse is specifically applied to Palestinian references — not to civilian references in general. The embedding model has learned a specifically Palestinian erasure pattern, not a general civilian-erasure pattern.

The near-neutral absolute associations for media institutions and Palestinian journalist vocabulary suggest that the SZ does not consistently embed these categories in a single semantic direction. Journalism vocabulary in the corpus is genuinely polysemous — it appears in press-freedom contexts and in repression contexts — while Palestinian-as-collective and Palestinian-displacement vocabulary have a clearer absolute semantic trajectory.

---

## Summary and Research Implications

### For Research Question 1 (Targeting of Palestinian Journalists)
The corpus shows consistent and substantial embedding of Palestinian journalist vocabulary in violence, detention, harassment, and terror-labelling contexts, with all WEAT effect sizes between 0.636 and 0.755. The SZ clearly reports extensively on journalist repression. The WEFAT finding that Palestinian journalist terms are neutral in absolute terms indicates the SZ also provides contexts of professional journalism identity for these figures, but those contexts are outnumbered by repression contexts when compared with general journalism coverage.

### For Research Question 2 (Dehumanisation and Narrative Practices)
The strongest findings in the entire dataset concern dehumanisation and civilian erasure, with effect sizes of 0.998 and 1.035 respectively. The SZ corpus — despite not being an explicitly dehumanising source — has an embedding structure that places Palestinian identity substantially closer to dehumanising and status-erasing vocabulary than any other group. The absolute WEFAT results confirm that Palestinian vocabulary is genuinely closer to displacement and dehumanisation vocabulary in the embedding space, independent of any comparison group.

The institutional editorial line result (1.030) is particularly significant: Palestinian references appear in the SZ predominantly in the context of narrative/information warfare discourse rather than in contexts of editorial independence. This reflects a structural pattern where Palestinian perspectives are more often mediated through debates about propaganda and narrative than through direct, independently verified reporting.

### For Research Question 3 (Incitement and International Criminal Law)
All four incitement tests show positive associations between Palestinian references and incitement vocabulary, with coded incitement showing the strongest signal (0.556). The displacement finding is especially relevant to legal analysis: the WEFAT mass displacement result (1.533) is the strongest finding in the analysis, suggesting that the corpus has deeply embedded the association between Palestinian identity and forced displacement at a semantic level that would inform any downstream use of this language model.

The genocide vocabulary association is weaker in WEAT (0.295) and moderate in WEFAT (0.677), consistent with the hypothesis that explicit genocide incitement language appears in the corpus primarily in reporting and critical analysis rather than as editorial endorsement.

### For Research Question 4 (Censorship and Media Access)
The censorship retaliation (0.511) and exclusion/blackout (0.658 for foreign press) results demonstrate that access denial and censorship vocabulary consistently co-occurs with Palestinian journalist and foreign journalist references. The SZ reports on the information blackout; the embedding model captures this as a consistent semantic pattern.

### For Research Question 5 (Disinformation Against Journalists)
The disinformation result (0.471) and professionalism contestation (0.287) indicate a consistent but moderate pattern: Palestinian journalists appear in disinformation-labelling contexts more than general journalists. The relative weakness of this signal compared to the physical violence signals (0.636–0.755) may reflect that the SZ more readily reports the physical dimension of journalist repression than the credibility-attack dimension.

---

## Limitations

1. **No statistical p-values**: The corpus is small relative to standard WEAT benchmarks; p-values could not be computed with the permutation test as the number of permutations required exceeds corpus constraints. Effect sizes should be interpreted as descriptive rather than inferential.
2. **Co-occurrence ≠ endorsement**: WEAT and WEFAT capture how words are *used together*, not what the newspaper *endorses*. A high dehumanisation effect size reflects that Palestinian references and dehumanising vocabulary appear in the same articles — often in the context of reporting on and critiquing such language.
3. **Embedding quality**: With 2,522 articles and a 100-dimensional Word2Vec model, some word vectors may be unstable. Words with fewer than 10 corpus occurrences are particularly unreliable.
4. **German morphology**: German's rich inflection means that "Palästinenser", "Palästinenserin", "palästinensische", "palästinensischen" are distinct tokens in the model. Partial coverage of inflected forms may underweight some targets.
5. **Single source**: All results pertain to the SZ only. Comparison with other outlets (Bild, taz, FAZ) would be necessary to assess whether the patterns observed are specific to the SZ or representative of German media more broadly.

Qualitative Analysis of WEAT and WEFAT Results
Süddeutsche Zeitung Coverage of the Israel-Palestine Conflict, October 2023 – October 2024
Corpus: 2,522 articles from the Süddeutsche Zeitung (SZ), Germany's largest quality newspaper
Method: Word Embedding Association Test (WEAT) and Word Embedding Fairness Association Test (WEFAT) on a Word2Vec model trained on the corpus
Research context: Submission to the UN Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression — The Role of Media in the Context of Israel's Actions toward the Palestinian People

Methodological Note
WEAT measures relative bias: how much more one target group (e.g., Palestinian journalists) is associated with one set of attributes (e.g., violence vocabulary) compared to a second target group (e.g., general journalists) and a second attribute set (e.g., press-freedom vocabulary). A positive effect size means the first target group is relatively more associated with the first attribute set. Effect sizes above 0.5 are considered moderate; above 0.8, strong.

WEFAT measures absolute bias: the mean cosine-similarity difference between a single target group and two competing attribute sets, without needing a comparison group. A positive WEFAT score means the target group is, in absolute terms, embedded closer to the first attribute set than the second. The WEFAT effect size normalises this difference by the spread across individual target words.

Both tests operate on distributional semantics: they capture how words are used together in the corpus, not explicit editorial statements.

Part I — WEAT Results
1. Targeting and Repression of Palestinian Journalists
Experiment	Effect Size	Interpretation
journalist_targeting_violence	0.755	Palestinian journalist vocabulary is substantially more embedded in targeting/violence contexts than general journalist vocabulary, relative to press-freedom discourse.
journalist_detention_disappearance	0.704	Palestinian journalist terms co-occur markedly more with detention and disappearance vocabulary (arrest, abduction, captivity) than general journalist terms.
journalist_harassment_intimidation	0.669	Palestinian journalist vocabulary is significantly more embedded in harassment/intimidation contexts (threats, surveillance, pursuit).
journalist_terror_labelling	0.636	Palestinian journalist terms are substantially more associated with terrorist-labelling vocabulary (militant, extremist, jihad) than general journalist references, relative to press-freedom terms.
journalist_family_targeting	0.654	Palestinian journalist vocabulary co-occurs considerably more with vocabulary about targeting of family members, compared to press-freedom framings.
journalist_access_exclusion_parity	0.197	Palestinian journalists are somewhat more embedded in exclusion/blackout discourse than foreign journalists, though this signal is relatively weak.
Interpretation: Across all six sub-dimensions of journalist repression, the embedding model positions Palestinian journalist vocabulary closer to repression vocabulary than any comparison group. The strongest signals — targeting/violence (0.755) and detention/disappearance (0.704) — indicate that the SZ corpus systematically embeds Palestinian journalist references in contexts of physical violence and deprivation of liberty. This is consistent with reporting that documents events (killings, arrests) but does not counterbalance those reports with press-freedom framings. The terrorist-labelling association (0.636) suggests that Palestinian journalists are regularly encountered in articles that also use militant/extremist vocabulary, even if the SZ itself is not deploying such labels directly — the proximity in embedding space reflects co-occurrence patterns in context.

The access/exclusion signal is weaker (0.197), possibly because the SZ reports the information blackout in Gaza through general descriptions of the situation rather than repeatedly linking it to the figure of the Palestinian journalist specifically.

2. Dehumanisation and Denial of Civilian Status
Experiment	Effect Size	Interpretation
palestinian_civilian_erasure	1.035	STRONG: Palestinian terms are far more embedded in civilian-status-erasure vocabulary (collaborator, human shield, complicit, fighter) than generic civilian vocabulary.
palestinian_dehumanization	0.998	STRONG: Palestinian terms are substantially more associated with dehumanising language (wave, flood, barbaric, horror, atrocity) than generic civilian references.
coded_incitement	0.556	Palestinian terms are moderately more associated with coded escalation vocabulary (cleanse, pacify, purge) than civilian references, relative to civilian-protection discourse.
institutional_editorial_line	1.030	STRONG: Palestinian terms are far more embedded in editorial-line/propaganda vocabulary (campaign, narrativ, propaganda, line) than civilian references, relative to editorial-independence vocabulary.
Interpretation: The most striking findings concern dehumanisation and civilian erasure. Effect sizes above 1.0 are very strong in the WEAT framework. The civilian erasure result (1.035) means the model has learned to situate Palestinian identity references in the same semantic neighbourhood as vocabulary that strips civilians of their protected status — calling them fighters, shields, or accomplices. This is not necessarily because the SZ uses such terms of Palestinians itself; it reflects that Palestinian references appear in articles that discuss these framings (often to quote Israeli military or government sources, or to describe the content of debates). The fact that the corpus embeds these terms together means a reader — and a language model — would implicitly associate Palestinian identity with contested civilian status.

The institutional editorial line result (1.030) is equally striking: Palestinian references are systematically more embedded in propaganda/narrative/campaign vocabulary than generic civilian references. This may indicate that Palestinian perspectives are primarily encountered in the SZ as objects of narrative contests — discussions of Hamas propaganda, pro-Palestinian campaigns, or information warfare — rather than as sources of authoritative testimony.

The dehumanisation score (0.998) corroborates this: Palestinian terms co-occur significantly more with vocabulary used in dehumanising discourse (wave, flood, horror) compared to generic references to civilians. Many of these terms appear in articles describing Hamas attacks on Israel, where vocabulary like "Schrecken" (horror) and "Barbarei" (barbarism) is used. The shared embedding with Palestinian identity terms reflects that Palestinian identity and barbaric violence vocabulary are repeatedly encountered in the same textual contexts.

3. Israel–Palestine Comparative Framing
Experiment	Effect Size	Interpretation
israel_palestine_violence_framing	0.813	STRONG: Palestinians are substantially more associated with violent/negative violence vocabulary than Israelis, who are relatively more associated with defensive/positive framing.
israel_palestine_death_language	0.660	Palestinians are moderately more associated with euphemistic death vocabulary (died, passed, deceased) than Israelis, who are relatively more associated with direct death vocabulary (murdered, massacre, killing).
israel_palestine_credibility_framing	−0.535	REVERSAL: Israeli sources are more associated with credibility-negative language (alleged, claimed, supposed, doubt) than Palestinian sources.
Interpretation: The violence-framing asymmetry (0.813) is substantial: Palestinian actors are embedded much more deeply in vocabulary associated with terrorism, extremism, and brutal violence, while Israeli actors are embedded relatively more in vocabulary of defence, security, and self-protection. This tracks the standard framing of the conflict in Western media: Hamas attacks are described with maximally strong condemnatory vocabulary; Israeli military operations are described in terms of security and defence. The SZ, despite being a liberal quality newspaper, reproduces this asymmetry at the level of embedding structure.

The death-language finding (0.660) is counter-intuitive and analytically important. Palestinian deaths are described more often with soft death vocabulary (tod, gestorben, tot, umkommen) while Israeli deaths — in particular the October 7 massacre — are described with direct murder vocabulary (ermordet, massaker, mord). This is not dehumanisation by softening Palestinian deaths per se; it reflects that the corpus contains extensive October 7 coverage that uses extremely direct violence vocabulary (massacre, murdered) in the context of Israeli victims. Palestinian civilian deaths in Gaza are more often reported in aggregate, aggregate numbers being accompanied by softer vocabulary. The embedding model captures this asymmetric expressiveness.

The credibility reversal (−0.535) is the most unexpected finding. Israeli sources are more associated with hedging/credibility-negative vocabulary than Palestinian sources. A plausible explanation is that the SZ — a critical-liberal newspaper — frequently applies epistemological scrutiny to Israeli government and military statements, using "angeblich" (alleged), "mutmaßlich" (supposed), and "behauptung" (claim) when reporting on Israeli narratives about Gaza, targeted strikes, and casualty figures. This signals something important: the SZ applies journalist standards of source skepticism more visibly to Israeli governmental claims than to Palestinian ones, possibly because Palestinian accounts rarely appear as direct institutional claims that require the same level of epistemic qualification.

4. Media Infrastructure and Access
Experiment	Effect Size	Interpretation
foreign_press_exclusion_blackout	0.658	Foreign journalists are substantially more associated with exclusion/blackout vocabulary than general journalists, relative to press-freedom discourse.
media_infrastructure_disruption	−0.670	REVERSAL: Media infrastructure terms are more associated with telecom disruption than physical destruction, while media institution terms are more associated with physical infrastructure destruction.
journalist_access_exclusion_parity	0.197	Palestinian journalist vocabulary is somewhat more associated with exclusion than foreign journalists.
Interpretation: The foreign press exclusion result (0.658) indicates that the SZ extensively covers the exclusion of international journalists from Gaza in terms of blackout and access denial — this is logically expected given that Israel restricted foreign press access to Gaza throughout the conflict period. The inversion in media_infrastructure_disruption (−0.670) is analytically interesting: media institutions (editorial offices, news agencies) are more embedded in physical destruction vocabulary, while infrastructure (cameras, transmission equipment, networks) is more embedded in telecom disruption. This may reflect a reporting pattern where the destruction of Al Jazeera offices or news bureau buildings is reported alongside coverage of digital/communications blackouts as a distinct phenomenon.

5. Disinformation and Censorship Framings
Experiment	Effect Size	Interpretation
journalist_disinformation	0.471	Palestinian journalist vocabulary is moderately more associated with disinformation/discrediting vocabulary than general journalists, relative to editorial independence.
journalist_professionalism_contestation	0.287	Palestinian journalist vocabulary is weakly but consistently more associated with discrediting vocabulary than general journalists, relative to professional journalism norms.
censorship_retaliation	0.511	Palestinian journalist vocabulary is moderately more associated with censorship/retaliation vocabulary than general journalists, relative to press freedom.
legal_accountability_obscuring	0.473	Palestinian references are moderately more embedded in legal accountability vocabulary than civilian references, relative to disinformation vocabulary.
Interpretation: The disinformation result (0.471) indicates that Palestinian journalist references co-occur meaningfully more with propaganda, discrediting, and manipulation vocabulary than generic journalist references. This likely reflects the regular appearance of Israeli characterisations of Palestinian media as "Hamas mouthpieces" in articles that cite or engage with Israeli positions — the SZ reports this framing rather than endorsing it, but the co-occurrence still shapes the embedding structure.

The legal accountability result (0.473) shows an opposite pattern to what one might expect: Palestinian references are more embedded in legal accountability language (war crimes, evidence, international law, accountability) than generic civilian references. This reflects the extensive SZ coverage of ICJ proceedings, international law debates, and accountability frameworks specifically in the context of Gaza — meaning Palestinian experiences are frequently encountered alongside legal accountability discourse, which is substantively appropriate but confirms that the SZ does engage with the legal dimension of the conflict.

6. Incitement-Related Findings
Experiment	Effect Size	Interpretation
genocide_incitement	0.295	Palestinian terms are weakly-to-moderately more associated with genocide incitement vocabulary than civilian references.
coded_incitement	0.556	Palestinian terms are moderately more associated with coded escalation vocabulary.
mass_displacement_incitement	0.465	Palestinian terms are moderately more associated with mass displacement vocabulary than civilian references.
gaza_destruction_incitement	0.172	Palestinian terms are weakly associated with Gaza destruction vocabulary compared to civilian references — the weakest WEAT incitement signal.
Interpretation: All four incitement-related experiments show positive effects, consistently placing Palestinian references in closer proximity to incitement vocabulary than generic civilian references. The weak Gaza destruction signal (0.172) is noteworthy: vocabulary directly about destroying Gaza physically is not strongly differentiated between Palestinian and civilian embedding contexts. This may reflect that destruction vocabulary in the corpus is associated broadly with the conflict rather than specifically with Palestinian identity. The coded incitement signal (0.556) is stronger, suggesting that softer escalatory vocabulary (purge, pacify, clean) co-occurs more with Palestinian references than generic civilian ones.

Part II — WEFAT Results (Absolute Associations)
WEFAT allows measurement of a group's absolute embedding position relative to two attribute sets, without requiring a comparison group. This complements WEAT by revealing what the corpus does to a group on its own terms.

Experiment	WEFAT Score	Effect Size	Interpretation
wefat_mass_displacement_absolute	0.052	1.533	STRONGEST SIGNAL: Palestinians are absolutely positioned closer to mass displacement vocabulary than civilian protection vocabulary.
wefat_genocide_incitement_absolute	0.042	0.677	Palestinians are moderately absolutely associated with genocide incitement vocabulary vs. civilian protection.
wefat_palestinians_dehumanization_absolute	0.030	0.555	Palestinians have a moderate absolute association with dehumanising vocabulary vs. humanising vocabulary.
wefat_civilians_erasure_absolute	−0.0001	−0.002	Generic civilian terms are essentially neutral between erasure and humanising vocabulary.
wefat_media_institutions_destruction_absolute	−0.005	−0.070	Media institution terms are essentially neutral, marginally more associated with press freedom than destruction.
wefat_palestinian_journalists_violence_absolute	−0.002	−0.031	Palestinian journalist terms are essentially neutral in absolute terms between violence and press freedom vocabulary.
Interpretation: The WEFAT results reveal important distinctions between absolute and relative bias.

The most significant finding is the Palestinian mass displacement absolute association (effect size 1.533): this is the strongest single result in the entire analysis. Palestinian vocabulary — "Gaza", "Palestinians", "West Bank" — is embedded in an absolute sense substantially closer to vocabulary about forced displacement, expulsion, and flight than to vocabulary about civilian protection. This is a property of the embedding space itself: any model trained on this corpus will have learned that Palestinian identity and displacement are semantically proximate in an absolute, not merely relative, sense.

By contrast, Palestinian journalist vocabulary is essentially neutral in absolute terms (effect −0.031) — yet shows significant relative bias against general journalists in WEAT (0.755). This is analytically important: Palestinian journalist identity by itself is not absolutely situated in a violence semantic field, but it is situated there relative to general journalist identity. This means the comparative framing matters: Palestinian journalists are reported as journalists but the specific context of their mention is systematically more violent than the context in which general journalists are mentioned.

Similarly, generic civilian terms show near-zero absolute erasure association (−0.002), while Palestinian terms show strong WEAT erasure association (1.035). This contrast confirms that the denial-of-civilian-status discourse is specifically applied to Palestinian references — not to civilian references in general. The embedding model has learned a specifically Palestinian erasure pattern, not a general civilian-erasure pattern.

The near-neutral absolute associations for media institutions and Palestinian journalist vocabulary suggest that the SZ does not consistently embed these categories in a single semantic direction. Journalism vocabulary in the corpus is genuinely polysemous — it appears in press-freedom contexts and in repression contexts — while Palestinian-as-collective and Palestinian-displacement vocabulary have a clearer absolute semantic trajectory.

Summary and Research Implications
For Research Question 1 (Targeting of Palestinian Journalists)
The corpus shows consistent and substantial embedding of Palestinian journalist vocabulary in violence, detention, harassment, and terror-labelling contexts, with all WEAT effect sizes between 0.636 and 0.755. The SZ clearly reports extensively on journalist repression. The WEFAT finding that Palestinian journalist terms are neutral in absolute terms indicates the SZ also provides contexts of professional journalism identity for these figures, but those contexts are outnumbered by repression contexts when compared with general journalism coverage.

For Research Question 2 (Dehumanisation and Narrative Practices)
The strongest findings in the entire dataset concern dehumanisation and civilian erasure, with effect sizes of 0.998 and 1.035 respectively. The SZ corpus — despite not being an explicitly dehumanising source — has an embedding structure that places Palestinian identity substantially closer to dehumanising and status-erasing vocabulary than any other group. The absolute WEFAT results confirm that Palestinian vocabulary is genuinely closer to displacement and dehumanisation vocabulary in the embedding space, independent of any comparison group.

The institutional editorial line result (1.030) is particularly significant: Palestinian references appear in the SZ predominantly in the context of narrative/information warfare discourse rather than in contexts of editorial independence. This reflects a structural pattern where Palestinian perspectives are more often mediated through debates about propaganda and narrative than through direct, independently verified reporting.

For Research Question 3 (Incitement and International Criminal Law)
All four incitement tests show positive associations between Palestinian references and incitement vocabulary, with coded incitement showing the strongest signal (0.556). The displacement finding is especially relevant to legal analysis: the WEFAT mass displacement result (1.533) is the strongest finding in the analysis, suggesting that the corpus has deeply embedded the association between Palestinian identity and forced displacement at a semantic level that would inform any downstream use of this language model.

The genocide vocabulary association is weaker in WEAT (0.295) and moderate in WEFAT (0.677), consistent with the hypothesis that explicit genocide incitement language appears in the corpus primarily in reporting and critical analysis rather than as editorial endorsement.

For Research Question 4 (Censorship and Media Access)
The censorship retaliation (0.511) and exclusion/blackout (0.658 for foreign press) results demonstrate that access denial and censorship vocabulary consistently co-occurs with Palestinian journalist and foreign journalist references. The SZ reports on the information blackout; the embedding model captures this as a consistent semantic pattern.

For Research Question 5 (Disinformation Against Journalists)
The disinformation result (0.471) and professionalism contestation (0.287) indicate a consistent but moderate pattern: Palestinian journalists appear in disinformation-labelling contexts more than general journalists. The relative weakness of this signal compared to the physical violence signals (0.636–0.755) may reflect that the SZ more readily reports the physical dimension of journalist repression than the credibility-attack dimension.

Limitations
No statistical p-values: The corpus is small relative to standard WEAT benchmarks; p-values could not be computed with the permutation test as the number of permutations required exceeds corpus constraints. Effect sizes should be interpreted as descriptive rather than inferential.
Co-occurrence ≠ endorsement: WEAT and WEFAT capture how words are used together, not what the newspaper endorses. A high dehumanisation effect size reflects that Palestinian references and dehumanising vocabulary appear in the same articles — often in the context of reporting on and critiquing such language.
Embedding quality: With 2,522 articles and a 100-dimensional Word2Vec model, some word vectors may be unstable. Words with fewer than 10 corpus occurrences are particularly unreliable.
German morphology: German's rich inflection means that "Palästinenser", "Palästinenserin", "palästinensische", "palästinensischen" are distinct tokens in the model. Partial coverage of inflected forms may underweight some targets.
Single source: All results pertain to the SZ only. Comparison with other outlets (Bild, taz, FAZ) would be necessary to assess whether the patterns observed are specific to the SZ or representative of German media more broadly.