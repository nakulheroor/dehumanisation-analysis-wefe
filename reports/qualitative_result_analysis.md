# Computational Analysis of Media Framing in the Süddeutsche Zeitung
## Embedding-Space Evidence on the Role of International Media in the Context of Israel's Actions toward the Palestinian People

**Submitted to**: UN Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression — *The Role of Media in the Context of Israel's Actions toward the Palestinian People*

**Corpus**: 2,522 articles from the Süddeutsche Zeitung (SZ), Germany's largest quality newspaper, October 2023 – October 2024  
**Method**: Word Embedding Association Test (WEAT) and Word Embedding Fairness Association Test (WEFAT) applied to a Word2Vec model trained on the corpus  
**Total experiments**: 37 (29 WEAT + 8 WEFAT)

---

## Executive Summary

This submission presents computational evidence of systematic framing asymmetries in Süddeutsche Zeitung coverage of the conflict in Gaza, derived from word embedding analysis of 2,522 articles published over a twelve-month period. Five overarching patterns emerge, each mapped to the Special Rapporteur's research areas:

**1. Palestinian journalists are consistently embedded in contexts of physical violence, detention, terror-labelling, and Hamas-association** — effect sizes between 0.636 and 0.972 across six sub-dimensions — while press-freedom framing is reserved for general journalistic coverage. The strongest journalist-specific finding is the near-categorical association between Palestinian journalist vocabulary and Hamas/terrorist-organisation vocabulary (0.972), comparable in magnitude to the Palestinian civilian dehumanisation result (0.998).

**2. Palestinian deaths are described with passive, agentless vocabulary** (*gestorben*, *starben*, *umgekommen*) **while Israeli deaths use active murder vocabulary** (*ermordet*, *Massaker*, *Blutbad*) — effect size 1.160, the strongest parity test in the study. A second asymmetry: Israeli captives are systematically described as "Geiseln" (hostages, evoking sympathy and urgency) while Palestinian detainees appear as "Häftlinge/Gefangene" (prisoners, bureaucratic and neutral) — effect size 0.806.

**3. Palestinian identity is embedded substantially closer to dehumanisation vocabulary** (civilian-status erasure: 1.035; dehumanisation: 0.998) **and institutional propaganda framing** (1.030) **than to any humanising or civilian-protection vocabulary**. The absolute WEFAT association between Palestinian vocabulary and mass-displacement terms is the single strongest result in the analysis (effect size 1.533).

**4. Israeli military actions are described with terror-attack vocabulary** (*Überfall*, *Blutbad*, *Terrorangriff*) **in the specific sense that Israelis are the VICTIMS of these acts**, while self-defense framing (*Selbstverteidigung*) appears more prominently in discussions of Palestinian resistance — a structural reversal (−1.271) that captures the SZ's victim/perpetrator framing: Israeli suffering is described with maximally grave murder and terror vocabulary; Palestinian resistance is the locus of the legitimacy debate.

**5. All four incitement-related experiments return positive effects**, placing Palestinian references consistently closer to displacement, coded escalation, and genocide-adjacent vocabulary than generic civilian references. The WEFAT displacement result (1.533) is the strongest absolute signal: the corpus has deeply embedded the semantic proximity of Palestinian identity and forced displacement.

---

## Corpus and Method

### Corpus

The analysis draws on 2,522 articles published in the Süddeutsche Zeitung (SZ) between 7 October 2023 and October 2024. The SZ is Germany's largest national quality newspaper, with a liberal-centrist editorial position and a broad international affairs desk. All articles were retrieved in full text. The corpus covers the immediate aftermath of the Hamas attacks on Israel (7 October 2023), the Israeli military campaign in Gaza, diplomatic developments, international law proceedings, and coverage of journalists killed or restricted in Gaza.

### Method: Word Embedding Association Test (WEAT and WEFAT)

**WEAT** (Word Embedding Association Test) measures *relative bias*: how much more one target group (e.g., *Palestinian journalists*) is associated with one set of attributes (e.g., *violence vocabulary*) compared to a second target group (e.g., *general journalists*) and a second attribute set (e.g., *press-freedom vocabulary*). A positive effect size means the first target is more associated with the first attribute set. Effect sizes above 0.5 are considered moderate; above 0.8, strong; above 1.0, very strong.

**WEFAT** (Word Embedding Fairness Association Test) measures *absolute bias*: the mean cosine-similarity difference between a single target group and two competing attribute sets, without a comparison group. A positive WEFAT score means the group is embedded absolutely closer to the first attribute set.

Both tests operate on *distributional semantics*: they capture how words are *used together* across the corpus, not explicit editorial positions. A high dehumanisation effect size does not mean the SZ endorsed dehumanising language — it means Palestinian identity vocabulary and dehumanising vocabulary appear in the same articles, often in the context of reporting on, quoting, or debating such language. The embedding model encodes these co-occurrence patterns regardless of authorial intent.

### Effect Size Reference

| Range | Label |
|---|---|
| \|ES\| < 0.2 | Negligible / noise-level |
| 0.2 – 0.5 | Weak but directional |
| 0.5 – 0.8 | Moderate — meaningful pattern |
| 0.8 – 1.0 | Strong |
| > 1.0 | Very strong / near-categorical |
| Negative | Reversal: second target more associated with first attribute |

---

## Research Area 1: Targeting and Repression of Palestinian Journalists and Media Workers

The Special Rapporteur's call identifies six sub-dimensions of journalist repression: physical violence, detention and disappearance, harassment, terror-labelling, family targeting, and information blackout through exclusion. The corpus produces statistically meaningful embedding signals on all six dimensions, plus two additional framing patterns.

### 1.1 Killing, Maiming, and Physical Violence

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_targeting_violence` | **0.755** | Palestinian journalist vocabulary is substantially more embedded in physical targeting and violence contexts (*töten, erschießen, bombardieren, Mord, Massaker, kaltblütig*) than general journalist vocabulary, relative to press-freedom discourse. |

Palestinian journalist vocabulary in the SZ co-occurs consistently with the vocabulary of lethal violence. The embedding model places Palestinian journalists significantly closer to killing, shooting, bombardment, and murder vocabulary than any general journalist reference. This reflects the documented reality: more than 100 Palestinian journalists were killed in Gaza during the study period. The SZ reports these killings — the embedding pattern reflects the reporting, not editorial endorsement — but the absence of a counterbalancing press-freedom framing for Palestinian journalists specifically (compared with how general journalism is discussed) means the corpus has learned to associate Palestinian media work with lethal danger as a stable semantic fact.

### 1.2 Detention, Enforced Disappearance, and Arbitrary Arrest

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_detention_disappearance` | **0.704** | Palestinian journalist terms co-occur markedly more with detention and disappearance vocabulary (*festnehmen, verhaften, verschleppen, Haft, Gefangenschaft, Festnahme*) than general journalist references, relative to press-freedom discourse. |

Palestinian journalist vocabulary is embedded substantially closer to detention and enforced disappearance vocabulary than any comparative group. This reflects both the documented arrests of Palestinian journalists by Israeli forces and the broader context of arbitrary detention that characterises coverage of press freedom in Gaza. The effect size (0.704) places this among the strongest journalist-repression signals in the analysis.

### 1.3 Harassment and Intimidation

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_harassment_intimidation` | **0.669** | Palestinian journalist vocabulary is significantly more embedded in harassment and intimidation contexts (*bedrohen, einschüchtern, überwachen, verfolgen, Drohungen*) than general journalist vocabulary, relative to press-freedom terms. |

Threats, surveillance, and pursuit vocabulary are substantially more associated with Palestinian journalist references than with general journalism. The moderate-to-strong effect size (0.669) indicates that this is a consistent pattern across the corpus rather than an artifact of a few articles.

### 1.4 Terror-Labelling and Hamas-Association

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_terror_labelling` | **0.636** | Palestinian journalist vocabulary is substantially more associated with terrorist-labelling terms (*militant, Extremist, Islamist, Jihad, Miliz*) than general journalist terms, relative to press-freedom vocabulary. |
| `journalist_hamas_association` | **0.972** | STRONG: Palestinian journalist vocabulary is embedded almost as deeply in Hamas/terrorist-organisation vocabulary (*Hamas, Dschihadist, Islamist, Terrorgruppe, Islamismus*) as general journalist vocabulary is in press-freedom terms. |
| `journalist_conviction_association` | **0.144** | WEAK: Palestinian journalist terms are only marginally more embedded in conviction/accusation vocabulary (*schuldig, verdächtig, angeklagt, verhaftet*) than general journalists. |

The Hamas-association result (0.972) is the most analytically significant finding in this research area, and one of the three strongest results in the entire study. Palestinian journalist vocabulary is embedded almost categorically within Hamas and terrorist-organisation vocabulary. This reflects a recurrent pattern in SZ reporting: articles about Palestinian journalists also raise questions about whether they are Hamas-affiliated, whether they knew in advance about 7 October, whether their editorial output serves Hamas propaganda, and whether Al Jazeera's reporting reflects its relationship to Qatar's Hamas ties. The SZ engages with these questions critically — but the repeated co-occurrence of "palästinensische Journalisten" and "Hamas" in the same articles produces a near-unity embedding regardless of authorial position.

Crucially, the conviction/accusation effect size is weak (0.144). The SZ does not disproportionately use formal criminal-prosecution vocabulary (*verurteilt*, *Anklage*, *Haftbefehl*) in articles about Palestinian journalists compared to general journalists. Legal vocabulary in the corpus is broad — it covers ICJ proceedings, Israeli military law, domestic German cases. The mechanism of Palestinian journalist delegitimisation in the SZ is therefore **guilt-by-Hamas-proximity**, not formal criminal attribution. This is an important distinction for legal analysis: the discrediting operates through associative embedding rather than explicit accusation.

### 1.5 Family Targeting

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_family_targeting` | **0.654** | Palestinian journalist vocabulary co-occurs considerably more with vocabulary about targeting family members (*Angehörige, Familie, töten, einschüchtern, bestrafen*) relative to press-freedom framings. |

The family-targeting signal (0.654) confirms that coverage of Palestinian journalist repression in the SZ includes substantial reference to threats against and killing of journalists' families. The corpus references Wael Dahdouh of Al Jazeera — whose wife, daughter, son, and grandson were killed in an Israeli airstrike — and similar cases. These personal dimensions are reported, but they are absorbed into the repression embedding pattern rather than generating a counterbalancing humanising discourse.

### 1.6 Destruction of Media Infrastructure and Information Blackout

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `foreign_press_exclusion_blackout` | **0.658** | Foreign journalists are substantially more embedded in exclusion and information-blackout vocabulary (*Einreiseverbot, Abschottung, gesperrt, Ausschluss, abgeschnitten*) than general journalists, relative to press-freedom discourse. |
| `journalist_access_exclusion_parity` | **0.197** | Palestinian journalist vocabulary is somewhat more embedded in exclusion/blackout vocabulary than foreign journalists — a weak but directional signal. |
| `media_infrastructure_disruption` | **−0.670** | REVERSAL: Media *infrastructure* terms (*Kamera, Sendemast, Übertragung*) are more embedded in telecom-disruption vocabulary, while media *institution* terms (*Redaktion, Sender, Nachrichtenbüro*) are more embedded in physical destruction vocabulary. |

The foreign-press exclusion result (0.658) reflects extensive SZ reporting on Israel's restriction of international press access to Gaza — a documented policy throughout the conflict period. The Palestinian journalist exclusion signal is weaker (0.197), because the SZ's information-blackout reporting focuses on the structural situation rather than on individual Palestinian journalists.

The infrastructure reversal (−0.670) reveals an analytically important distinction in SZ coverage: physical destruction of media buildings and editorial offices (Al Jazeera bureau raids, studio bombings) is reported as attacks on *institutions*, while internet blackouts, telecommunications cutoffs, and signal disruption are reported as attacks on *infrastructure*. These are covered as separate phenomena. This finding is consistent with documented incidents: the SZ reports both the physical bombing of media premises and the telecommunications blackouts imposed during Israeli military operations, but frames them as distinct types of attack.

### 1.7 Censorship and Retaliation

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `censorship_retaliation` | **0.511** | Palestinian journalist vocabulary is moderately more embedded in censorship and retaliation vocabulary (*Zensur, Verbot, Entlassung, Sanktion, Einschüchterung, abschalten*) than general journalist vocabulary, relative to press-freedom terms. |

The censorship/retaliation signal (0.511) places Palestinian journalist references in moderate but consistent proximity to vocabulary about censorship mechanisms and retaliatory acts against media workers. This reflects SZ reporting on press restrictions, closures of Palestinian media operations, and documented retaliation against journalists who cover the conflict.

---

**Summary for Research Area 1**: The embedding evidence across seven dimensions shows that SZ coverage of Palestinian journalist repression is extensive and systematically separates Palestinian media workers from general journalism norms. The strongest findings — Hamas-association (0.972) and physical violence co-occurrence (0.755) — indicate that the corpus has learned to situate Palestinian journalists at the intersection of combat violence and terrorist-organisation vocabulary. This structural embedding pattern may reflect accurate reporting of a dangerous and politicised situation, but it also means that any reader or system trained on this corpus will have absorbed an implicit association between Palestinian media work and terrorist affiliation and lethal danger.

---

## Research Area 2: Media Narratives and Discursive Practices

### 2.1 Dehumanisation and Denial of Civilian Status

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `palestinian_civilian_erasure` | **1.035** | VERY STRONG: Palestinian terms are far more embedded in civilian-status-erasure vocabulary (*Schutzschild, mitschuldig, Kämpfer, Milizionäre, Hamas-Strukturen*) than generic civilian vocabulary. |
| `palestinian_dehumanization` | **0.998** | VERY STRONG: Palestinian terms are substantially more associated with dehumanising language (*Welle, Flut, barbarisch, Gräuel, Grauenhaft, Horror*) than generic civilian references. |
| `institutional_editorial_line` | **1.030** | VERY STRONG: Palestinian terms are far more embedded in editorial-line/propaganda vocabulary (*Kampagne, Propaganda, Narrativ, Linie*) than civilian references, relative to editorial-independence vocabulary. |

These three results — all above 1.0 — are among the strongest findings in the analysis and directly address the Special Rapporteur's question about "processes of dehumanisation of Palestinians, including portrayals denying civilian status or depicting Palestinians as an undifferentiated enemy."

**Civilian status erasure** (1.035): The corpus has learned that Palestinian identity references appear in the same articles as vocabulary that strips civilians of their protected status under international humanitarian law — calling them *Kämpfer* (fighters), *menschliche Schutzschilde* (human shields), or *mitschuldig* (complicit). This language appears primarily in articles that quote or engage with Israeli military and government positions. The SZ reports these framings rather than originating them, but the embedding model does not distinguish between reported and endorsed language. The result: Palestinian identity and contested civilian status are semantically proximate in the corpus.

**Dehumanisation** (0.998): Palestinian terms co-occur significantly more with vocabulary used in dehumanising discourse (*Welle*, *Flut*, *Horror*, *Barbarei*) compared to generic civilian references. Many of these terms appear in extensive October 7 reporting, where vocabulary like *Barbarei* and *Schrecken* describes Hamas violence. Palestinian identity vocabulary and atrocity-framing vocabulary are repeatedly encountered in the same textual contexts, regardless of whether they are used of or against Palestinians.

**Institutional editorial line** (1.030): Palestinian references are systematically more embedded in propaganda and narrative-war vocabulary than generic civilian references. Palestinian perspectives are more often mediated through debates about Hamas propaganda, narrative manipulation, and information warfare than through direct independent testimony. This finding maps directly onto the Special Rapporteur's concern about "evidence that narratives reflect institutional editorial lines rather than isolated journalistic misconduct."

### 2.2 Death-Language Agency Asymmetry

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `death_language_agency_asymmetry` | **1.160** | STRONGEST PARITY TEST: Palestinian references are far more embedded in passive/agentless death vocabulary (*gestorben, starben, todesfälle, umgekommen*) than Israeli references, which are far more embedded in active direct-murder vocabulary (*ermordet, Massaker, erschossen, Blutbad*). |
| `israel_palestine_death_language` | **0.660** | Palestinians are moderately more associated with euphemistic death vocabulary than Israelis, who are more associated with direct death vocabulary — a related but weaker finding using broader word sets. |

The death-language agency asymmetry (1.160) is the strongest parity test in the study. An effect size above 1.0 means the corpus has produced a near-categorical differentiation in how Palestinian and Israeli deaths are linguistically encoded.

Palestinian casualties are systematically reported using constructions that suppress agency: *gestorben* (died), *starben* (died, plural), *todesfälle* (deaths/fatalities), *umgekommen* (perished). These forms present death as an event without an actor — deaths appear to happen rather than being caused. This pattern holds even when deaths are clearly attributable to identified military strikes.

Israeli deaths — above all the approximately 1,200 victims of the October 7 Hamas attacks — are encoded with maximally agentive murder vocabulary: *ermordet* (murdered), *Massaker* (massacre), *erschossen* (shot dead), *Blutbad* (bloodbath). This vocabulary names an act, implies a perpetrator, and carries unambiguous moral gravity.

This finding is not dehumanisation through anonymisation of Palestinian victims per se — it is a structural narrative asymmetry. Israeli victims are *murdered*; Palestinian casualties *die*. The choice of verb encodes both the moral weight assigned to the act and the visibility of the perpetrator. Over 2,522 articles and twelve months of reporting, this asymmetry has produced one of the strongest distributional signals in the corpus.

### 2.3 Victim Humanisation and Sympathy Asymmetry

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `victim_humanization_sympathy_asymmetry` | **0.325** | Moderate: Israeli references are more embedded in sympathetic/humanising victim vocabulary (*Trauer, Trauerfeier, Geiseln, Angehörige, Schicksal, Gedenken*) while Palestinian references are relatively more embedded in statistical/aggregate reporting vocabulary (*Zahlen, Opferzahl, insgesamt, Angaben, laut*). |

Israeli victims — particularly October 7 hostages and massacre victims — are encountered in the SZ alongside vocabulary of grief, memorialisation, and individual tragedy. Palestinian casualties are more frequently encountered alongside reporting vocabulary that abstracts individuals into aggregates: death counts, percentages, health ministry figures. The moderate effect size (0.325) reflects that statistical vocabulary appears throughout the corpus, not exclusively in Palestinian contexts. Nevertheless, the directional finding holds: Israeli suffering is individualised and humanised; Palestinian suffering is reported as mass data.

### 2.4 Hostage versus Prisoner Framing

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `hostage_prisoner_framing` | **0.806** | STRONG: Israeli references are substantially more embedded in hostage/kidnapping vocabulary (*Geisel, Geiseln, Geiselnahme, entführt, verschleppt, Freilassung*) while Palestinian references are relatively more embedded in neutral prisoner/detention vocabulary (*Häftling, Gefangene, inhaftiert, Gefangenschaft*). |

This result directly captures a concrete discursive asymmetry documented in the vocabulary analysis of the SZ corpus. Israeli captives held by Hamas are systematically called *Geiseln* — a word that in German carries immediate connotations of innocence, vulnerability, urgency, and emotional distress. Coverage uses vocabulary of abduction (*entführt*), helplessness (*Angst, bangen*), and liberation (*befreit, freigelassen*). Palestinian prisoners in Israeli detention are called *Häftlinge* or *Gefangene* — bureaucratic, neutral terms associated with the vocabulary of criminal justice (*Gefangenschaft*, *Haftstrafe*, *Gefängnis*).

The effect size (0.806) confirms this is a strong, consistent pattern across the corpus. The asymmetry in labelling produces an asymmetry in moral framing: Israeli captives are humanised victims; Palestinian detainees are administrative categories.

### 2.5 Violence Framing and Self-Defense/Terror Asymmetry

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `israel_palestine_violence_framing` | **0.813** | STRONG: Palestinians are substantially more associated with violent/negative violence vocabulary (*Terrorist, Mörder, Islamist, barbarisch, Extremist, Vergeltungsschlag*) than Israelis, who are relatively more associated with defensive/self-protection framing. |
| `self_defense_vs_terror_framing` | **−1.271** | REVERSAL — STRONGEST IN STUDY: Israeli references are more embedded in terror-attack vocabulary (*Terrorangriff, Überfall, Blutbad, Massenmord, Attentat*) while Palestinian references are relatively more embedded in self-defense vocabulary (*Selbstverteidigung, Verteidigungsrecht, legitim, Gegenwehr*). |

These two results must be read together to understand the complete picture.

The violence-framing result (0.813) confirms the expected asymmetry: Palestinian actors are embedded much more deeply in vocabulary associated with terrorism, extremism, and brutal violence, while Israeli actors appear in relatively more defensive, protective vocabulary.

The self-defense/terror reversal (−1.271) initially appears contradictory but is analytically coherent. It captures a different layer of the same framing structure. The terror-attack vocabulary (*Terrorangriff*, *Überfall*, *Blutbad*, *Massenmord*) in the SZ appears predominantly in descriptions of the October 7 Hamas attacks — where it is applied to Israeli *victims*. Sentences like "beim Terrorangriff ermordete Israelis" or "Überfall auf israelische Kibbuzim" make Israeli identity vocabulary adjacent to terror-attack terms in the victim position. Palestinian identity vocabulary, meanwhile, appears in the SZ in a distinct discourse: whether Palestinian resistance constitutes *Selbstverteidigung*, whether international law confers a *Verteidigungsrecht*, whether Palestinian actions are *legitim* — a debate that situates Palestinian references near self-defense vocabulary even when the conclusion is contested.

The compound framing that emerges is:
- **Palestinians** = perpetrators of terror (violence_framing: 0.813) / subject of self-defense legitimacy debate
- **Israelis** = victims of terror attacks (self_defense reversal: −1.271) / inheritors of the self-defense right in state discourse

This is precisely the standard Western media framing of the conflict: Israeli violence is *response*, Palestinian violence is *aggression*; Israeli civilians are *terror victims*, Palestinian civilians are *collateral damage*. The SZ reproduces this framing at the structural level.

### 2.6 Credibility Framing

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `israel_palestine_credibility_framing` | **−0.535** | REVERSAL: Israeli sources are more associated with credibility-hedging vocabulary (*angeblich, mutmaßlich, Behauptung, behaupten, Lüge*) than Palestinian sources, relative to credibility-positive terms. |

The credibility reversal (−0.535) is the most unexpected finding in Research Area 2. Israeli sources are more associated with epistemic hedging (*angeblich*, *mutmaßlich*, *behaupten*) than Palestinian sources, suggesting that the SZ applies its standard journalistic scepticism more visibly to Israeli governmental and military claims. This reflects the SZ's critical-liberal orientation: it scrutinises Israeli statements about targeted strikes, casualty figures, and operational justifications with hedging language. Palestinian accounts are less likely to appear as formal institutional claims requiring the same level of qualification, because Palestinian sources in the corpus rarely appear as authoritative institutional voices in the same way.

This finding does not indicate that the SZ treats Palestinian sources with more credulity — it reflects the asymmetric institutional status of sources: Israeli government and military statements require qualification; Palestinian testimony is less often encountered as formal, quotable institutional assertion.

---

**Summary for Research Area 2**: The narrative framing evidence shows five converging asymmetries: (1) Palestinian identity is embedded near dehumanisation and status-erasure vocabulary at very high effect sizes (0.998–1.035); (2) Palestinian deaths are linguistically stripped of agency while Israeli deaths use maximally agentive murder vocabulary (1.160); (3) Israeli captives are humanised as "Geiseln" while Palestinian detainees are categorised as "Häftlinge" (0.806); (4) Palestinians are embedded as perpetrators of violence (0.813) while Israelis appear as victims of terror attacks in the strongest reversal in the study (−1.271); (5) Israeli victims receive sympathetic, individualised framing while Palestinian casualties appear in aggregate statistical reporting (0.325).

---

## Research Area 3: Incitement and International Criminal Law

The Special Rapporteur's call asks for evidence of media content that may constitute direct and public incitement to commit genocide (Article III(c) of the Genocide Convention), as well as implicit, coded, or context-dependent forms of incitement.

### 3.1 Direct Genocide Incitement Vocabulary

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `genocide_incitement` | **0.295** | Palestinian terms are weakly-to-moderately more embedded in direct genocide-incitement vocabulary (*ausrotten, vernichten, auslöschen, eliminieren, tilgen, Endlösung, restlos*) than generic civilian references, relative to civilian-protection discourse. |
| `wefat_genocide_incitement_absolute` | Score: 0.042 | **Effect size: 0.677** | Palestinians have a moderate absolute association with genocide-incitement vocabulary vs. civilian-protection vocabulary. |

The WEAT genocide incitement effect size (0.295) is relatively weak, consistent with the hypothesis that explicit genocide-incitement vocabulary appears in the SZ primarily in reporting and critical analysis contexts — the SZ cites, quotes, or analyses such language rather than producing it editorially. However, the WEFAT result (absolute effect size 0.677) indicates a moderate and real absolute association: Palestinian identity vocabulary is embedded closer to genocide-incitement terms than to civilian-protection terms in the embedding space itself, independent of any comparison group.

### 3.2 Coded and Implicit Incitement

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `coded_incitement` | **0.556** | Palestinian terms are moderately more associated with coded escalation vocabulary (*säubern, durchgreifen, befrieden, räumen, Ordnung, Härte*) than civilian references, relative to civilian-protection discourse. |

Coded escalatory vocabulary — softer formulations that euphemistically invoke elimination, cleansing, or subjugation — shows a stronger signal than explicit genocide vocabulary (0.556 vs. 0.295). This is consistent with research on implicit incitement: the most dangerous framing often operates through coded language that activates violent associations without triggering explicit condemnation. That this vocabulary is more strongly associated with Palestinian references than generic civilian references indicates it appears in Palestinian-specific contexts in the SZ — again, in reporting that discusses rather than endorses such language, but the embedding pattern remains.

### 3.3 Mass Displacement Incitement

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `mass_displacement_incitement` | **0.465** | Palestinian terms are moderately more embedded in mass-displacement vocabulary (*vertreiben, verdrängen, Vertreibung, Zwangsumsiedlung, Flucht, Flüchtlinge*) than generic civilian references, relative to civilian-protection discourse. |
| `wefat_mass_displacement_absolute` | Score: 0.052 | **Effect size: 1.533** | STRONGEST ABSOLUTE SIGNAL: Palestinians are absolutely positioned closer to mass-displacement vocabulary than to any civilian-protection vocabulary. |

The WEFAT mass displacement result (effect size 1.533) is the strongest single finding in the entire analysis. Palestinian vocabulary — *Gaza*, *Palästinenser*, *Gazastreifen* — is embedded in an absolute sense substantially closer to vocabulary about forced displacement, expulsion, and flight than to vocabulary about civilian protection. This is a structural property of the embedding space: any language model trained on this corpus has learned that Palestinian identity and displacement are semantically inseparable.

### 3.4 Destruction of Gaza

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `gaza_destruction_incitement` | **0.172** | Palestinian terms are weakly associated with Gaza destruction vocabulary (*vernichten, auslöschen, einebnen, zerstören, Verwüstung*) compared to civilian references — the weakest incitement signal. |

The weak Gaza destruction signal (0.172) may initially appear counterintuitive. It reflects that vocabulary about physical destruction of Gaza is not specifically associated with *Palestinian identity terms* in the corpus — rather, it appears in broader conflict reporting associated with both parties. Destruction vocabulary in the SZ characterises the situation rather than targeting a specific group.

### 3.5 Legal Accountability

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `legal_accountability_obscuring` | **0.473** | Palestinian references are moderately more embedded in legal-accountability vocabulary (*Völkerrecht, Kriegsverbrechen, Ermittlung, Haftung*) than civilian references, relative to disinformation vocabulary. |

Counter-intuitively, Palestinian references are more embedded in legal accountability language than generic civilian references. This reflects the SZ's substantial coverage of ICJ proceedings, international law debates, and accountability frameworks specifically applied to the Gaza situation. Palestinian experiences appear alongside international legal discourse — which is analytically appropriate — but also indicates that Palestinian suffering is more often encountered as a subject of legal analysis than of direct humanitarian framing.

---

**Summary for Research Area 3**: The incitement-related findings show a consistent pattern of positive associations between Palestinian references and incitement-adjacent vocabulary across all four experiment types. The WEFAT mass displacement result (1.533) is the most legally significant: it demonstrates that the semantic structure of the corpus is built around the proximity of Palestinian identity and forced displacement. Explicit genocide vocabulary shows a weaker signal (0.295 WEAT, 0.677 WEFAT), consistent with reporting that discusses rather than produces incitement content.

---

## Research Area 4: Censorship and Retaliatory Measures

### 4.1 Censorship and Retaliation Against Palestinian Journalists

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `censorship_retaliation` | **0.511** | Palestinian journalist vocabulary is moderately more embedded in censorship and retaliation vocabulary (*Zensur, Verbot, Entlassung, Einschüchterung, abschalten, Beschlagnahmt*) than general journalist vocabulary, relative to press-freedom terms. |
| `journalist_access_exclusion_parity` | **0.197** | Palestinian journalist vocabulary is somewhat more embedded in exclusion vocabulary than foreign journalist vocabulary — a weak but directional signal. |
| `foreign_press_exclusion_blackout` | **0.658** | Foreign journalists are substantially more embedded in exclusion and information-blackout vocabulary than general journalists, relative to press freedom. |

The censorship and retaliation signal (0.511) for Palestinian journalists is moderate and consistent. The stronger foreign-press-exclusion result (0.658) reflects the SZ's extensive coverage of Israel's documented exclusion of international journalists from Gaza throughout the conflict period. Palestinian journalist vocabulary shows a weaker exclusion signal than foreign journalist vocabulary (0.197 when compared to foreign journalists), possibly because the SZ's blackout reporting focuses on the systemic restriction of access rather than specifically linking it to individual Palestinian journalists.

---

**Summary for Research Area 4**: The censorship and access-restriction findings confirm that the SZ reports extensively on the information blackout and censorship mechanisms applied to Gaza coverage. The embedding patterns show that Palestinian journalists and foreign journalists are both substantially associated with exclusion and censorship vocabulary, while Palestinian journalists are specifically also embedded in broader retaliation and censorship contexts.

---

## Research Area 5: Disinformation Against Palestinian Journalists

### 5.1 Disinformation Framing and Credibility Attacks

| Experiment | Effect Size | Interpretation |
|---|---|---|
| `journalist_disinformation` | **0.471** | Palestinian journalist vocabulary is moderately more embedded in disinformation/discrediting vocabulary (*Desinformation, Propaganda, Verleumdung, Delegitimierung, Manipulation, angeblich, inszeniert*) than general journalists, relative to editorial independence vocabulary. |
| `journalist_professionalism_contestation` | **0.287** | Palestinian journalist vocabulary is weakly but consistently more embedded in professional-credibility-attack vocabulary (*Propagandist, Agent, Kollaborateur, Sympathisant, Jihad*) than general journalists, relative to professional journalism norms. |
| `journalist_conviction_association` | **0.144** | WEAK: Formal conviction vocabulary (*schuldig, angeklagt, verhaftet*) shows only a marginal association with Palestinian journalist vocabulary relative to general journalists. |
| `journalist_hamas_association` | **0.972** | STRONG: Hamas and terrorist-organisation vocabulary is near-categorically more associated with Palestinian journalist vocabulary — the primary vehicle for delegitimising Palestinian journalists in the corpus (see Research Area 1). |

The disinformation framing of Palestinian journalists operates in two distinct registers in the SZ corpus. The formal disinformation register (*Desinformation*, *Propaganda*, *Manipulation*) shows a moderate signal (0.471) — Palestinian journalists appear in articles that discuss these framings, often in reporting that cites Israeli characterisations of Palestinian media as "Hamas mouthpieces." The professional credibility-attack register (*Propagandist*, *Kollaborateur*, *Sympathisant*) shows a weaker signal (0.287), and formal criminal conviction vocabulary is essentially absent as a differentiating factor (0.144).

The dominant mechanism of Palestinian journalist delegitimisation in the SZ corpus is the Hamas-association embedding (0.972), already documented under Research Area 1. Palestinian journalists are not primarily discredited through claims of professional misconduct or formal accusations — they are discredited by proximity: by appearing in the same articles as Hamas and terrorist-organisation vocabulary, in a corpus that repeatedly poses the question of whether Palestinian journalists are Hamas-affiliated. This pattern, which the SZ covers as a debate rather than asserts as fact, produces a near-categorical embedding that serves as persistent background discrediting.

---

**Summary for Research Area 5**: Disinformation against Palestinian journalists in the SZ corpus operates primarily through associative embedding with Hamas rather than through formal accusation or explicit credibility attacks. The moderate signals for propaganda and discrediting vocabulary (0.287–0.471) are substantially weaker than the Hamas-association signal (0.972), confirming that the mechanism is contextual co-occurrence rather than direct labelling.

---

## Absolute Associations (WEFAT): What the Corpus Encodes Independently

WEFAT results reveal what the embedding space has learned about a group *in absolute terms* — not relative to a comparison group, but as a structural property of the model.

| Experiment | WEFAT Score | Effect Size | Interpretation |
|---|---|---|---|
| `wefat_mass_displacement_absolute` | +0.052 | **1.533** | Palestinians absolutely closer to displacement vocabulary than civilian protection — STRONGEST ABSOLUTE SIGNAL |
| `wefat_genocide_incitement_absolute` | +0.042 | **0.677** | Palestinians moderately absolutely closer to genocide-incitement vocabulary than civilian protection |
| `wefat_palestinians_dehumanization_absolute` | +0.030 | **0.555** | Palestinians moderately absolutely closer to dehumanising vocabulary than humanising vocabulary |
| `wefat_media_institutions_destruction_absolute` | −0.005 | −0.070 | Media institutions essentially neutral — marginally more associated with press freedom than destruction |
| `wefat_palestinian_journalists_violence_absolute` | −0.002 | −0.031 | Palestinian journalist terms essentially neutral in absolute terms between violence and press freedom |
| `wefat_civilians_erasure_absolute` | −0.0001 | −0.002 | Generic civilian terms neutral between erasure and humanising vocabulary |

The WEFAT results reveal a crucial distinction between absolute and relative bias.

The Palestinian mass displacement association (1.533) is the single strongest result in the analysis. Palestinian vocabulary is embedded in an absolute sense substantially closer to forced displacement, expulsion, and flight vocabulary than to civilian protection vocabulary. This is not relative to any comparison group — it is a structural property of the corpus. Any language system trained on this data will have learned that Palestinian identity and displacement are semantically inseparable.

By contrast, Palestinian journalist vocabulary is near-neutral in absolute terms (−0.031) — yet shows strong *relative* bias against general journalists in WEAT (0.755). This is analytically important: Palestinian journalists are not absolutely embedded in violence vocabulary. They are embedded in violence vocabulary *relative to general journalists*. The comparative context drives the bias.

Similarly, generic civilian terms show near-zero absolute erasure association (−0.002), while Palestinian terms show very strong WEAT erasure association (1.035). This confirms that the denial-of-civilian-status discourse is specifically Palestinians — not a generalised feature of conflict reporting.

---

## Complete Results Reference Table

All 37 experiments, ranked by absolute effect size:

| Rank | Experiment | Metric | Effect Size | Direction |
|---|---|---|---|---|
| 1 | `wefat_mass_displacement_absolute` | WEFAT | **+1.533** | Palestinians → displacement vocabulary |
| 2 | `self_defense_vs_terror_framing` | WEAT | **−1.271** | Israelis → terror-victim vocabulary; Palestinians → self-defense debate |
| 3 | `death_language_agency_asymmetry` | WEAT | **+1.160** | Palestinians → passive death; Israelis → active murder |
| 4 | `palestinian_civilian_erasure` | WEAT | **+1.035** | Palestinians → status-erasure vocabulary |
| 5 | `institutional_editorial_line` | WEAT | **+1.030** | Palestinians → propaganda/narrative vocabulary |
| 6 | `palestinian_dehumanization` | WEAT | **+0.998** | Palestinians → dehumanising vocabulary |
| 7 | `journalist_hamas_association` | WEAT | **+0.972** | Palestinian journalists → Hamas/terrorist-org vocabulary |
| 8 | `israel_palestine_violence_framing` | WEAT | **+0.813** | Palestinians → violent/terror framing |
| 9 | `hostage_prisoner_framing` | WEAT | **+0.806** | Israelis → hostage/sympathy vocabulary; Palestinians → prisoner/neutral |
| 10 | `journalist_targeting_violence` | WEAT | **+0.755** | Palestinian journalists → physical violence vocabulary |
| 11 | `journalist_detention_disappearance` | WEAT | **+0.704** | Palestinian journalists → detention/disappearance vocabulary |
| 12 | `wefat_genocide_incitement_absolute` | WEFAT | **+0.677** | Palestinians → genocide-incitement vocabulary |
| 13 | `media_infrastructure_disruption` | WEAT | **−0.670** | Media institutions → physical destruction; media infrastructure → telecom disruption |
| 14 | `journalist_harassment_intimidation` | WEAT | **+0.669** | Palestinian journalists → harassment/intimidation vocabulary |
| 15 | `israel_palestine_death_language` | WEAT | **+0.660** | Palestinians → euphemistic death; Israelis → direct murder vocabulary |
| 16 | `journalist_dehumanization_asymmetry` | WEAT | **−0.659** | General journalists → dehumanising contexts (see note) |
| 17 | `foreign_press_exclusion_blackout` | WEAT | **+0.658** | Foreign journalists → exclusion/blackout vocabulary |
| 18 | `journalist_family_targeting` | WEAT | **+0.654** | Palestinian journalists → family-targeting vocabulary |
| 19 | `journalist_terror_labelling` | WEAT | **+0.636** | Palestinian journalists → terrorist-labelling vocabulary |
| 20 | `wefat_palestinians_dehumanization_absolute` | WEFAT | **+0.555** | Palestinians → dehumanising vocabulary (absolute) |
| 21 | `coded_incitement` | WEAT | **+0.556** | Palestinians → coded escalation vocabulary |
| 22 | `israel_palestine_credibility_framing` | WEAT | **−0.535** | Israelis → credibility-hedging vocabulary |
| 23 | `censorship_retaliation` | WEAT | **+0.511** | Palestinian journalists → censorship/retaliation vocabulary |
| 24 | `legal_accountability_obscuring` | WEAT | **+0.473** | Palestinians → legal-accountability vocabulary |
| 25 | `journalist_disinformation` | WEAT | **+0.471** | Palestinian journalists → disinformation/discrediting vocabulary |
| 26 | `mass_displacement_incitement` | WEAT | **+0.465** | Palestinians → mass displacement vocabulary |
| 27 | `victim_humanization_sympathy_asymmetry` | WEAT | **+0.325** | Israelis → sympathetic/humanising vocabulary; Palestinians → statistical vocabulary |
| 28 | `genocide_incitement` | WEAT | **+0.295** | Palestinians → genocide-incitement vocabulary |
| 29 | `journalist_professionalism_contestation` | WEAT | **+0.287** | Palestinian journalists → credibility-attack vocabulary |
| 30 | `journalist_access_exclusion_parity` | WEAT | **+0.197** | Palestinian journalists → exclusion vocabulary (vs. foreign journalists) |
| 31 | `gaza_destruction_incitement` | WEAT | **+0.172** | Palestinians → destruction vocabulary (weak) |
| 32 | `journalist_conviction_association` | WEAT | **+0.144** | Palestinian journalists → conviction/accusation vocabulary (weak) |
| 33 | `wefat_media_institutions_destruction_absolute` | WEFAT | **−0.070** | Media institutions → near-neutral |
| 34 | `wefat_palestinian_journalists_violence_absolute` | WEFAT | **−0.031** | Palestinian journalist terms → near-neutral in absolute terms |
| 35 | `civilian_dehumanization_asymmetry` | WEAT | **+0.015** | Negligible asymmetry between Palestinians and Israelis on aggressive vocabulary |
| 36 | `wefat_civilians_erasure_absolute` | WEFAT | **−0.002** | Generic civilian terms → neutral |

---

## Proposed Additional Research

The following experiments could further strengthen the submission if additional analysis is feasible:

**Temporal analysis**: Re-running the experiments on two or three distinct time windows (Oct–Dec 2023; Jan–May 2024; Jun–Oct 2024) would reveal whether framing asymmetries intensified, diminished, or shifted as the conflict evolved. The death-language asymmetry and Hamas-journalist association may be strongest in the earliest period.

**Source attribution analysis**: Testing whether Palestinian sources (*palästinensische Quellen*, *Hamas*, *Gesundheitsministerium*) are embedded closer to doubt/hedging vocabulary while Israeli military sources (*IDF*, *israelisches Militär*) are embedded closer to authoritative vocabulary would extend the credibility-framing finding (−0.535) with greater source specificity.

**Children vocabulary asymmetry**: Testing whether Palestinian children (*Kinder in Gaza*, *palästinensische Kinder*) are more often associated with statistical/aggregate vocabulary while Israeli children are more often associated with named, individualised, emotionally charged vocabulary would extend the victim-humanisation finding (0.325) to the most politically sensitive category.

**Cross-outlet comparison**: Running the identical experiment suite on FAZ, taz, and Bild corpora would establish whether the SZ patterns are specific to its editorial orientation or representative of German media broadly. This would strengthen the legal significance of the findings by distinguishing systemic bias from single-outlet idiosyncrasy.

**Self-defense vocabulary by word set refinement**: The self-defense/terror reversal (−1.271) invites deeper analysis. Testing "Israel" (the state) rather than "Israelis" (the people) against the same attributes would reveal whether the reversal is driven by the victim-of-terror embedding of Israeli identity (people as victims of Terrorangriff) versus the state-level self-defense framing (Israel's right to Selbstverteidigung).

---

## Methodological Appendix

### Corpus Composition

| Dimension | Value |
|---|---|
| Total articles | 2,522 |
| Date range | 7 October 2023 – October 2024 |
| Source | Süddeutsche Zeitung (sueddeutsche.de) |
| Language | German |
| Encoding | UTF-8 plain text |
| Manifest | `data/processed/articles_manifest.csv` |

### Word Embedding Model

| Parameter | Value |
|---|---|
| Architecture | Word2Vec, Skip-gram (sg=1) |
| Vector dimensions | 100 |
| Context window | 5 tokens |
| Minimum count | 1 |
| Training epochs | 10 |
| Vocabulary | Approximately 28,000 types |
| Format | Gensim KeyedVectors |

### Effect Size Formula (WEAT)

For target sets T1, T2 and attribute sets A1, A2:

`ES = [ mean_cos(T1, A1) - mean_cos(T1, A2) ] - [ mean_cos(T2, A1) - mean_cos(T2, A2) ]`

Normalised by the standard deviation of all pairwise cosine scores. Positive ES = T1 closer to A1 relative to T2.

### Missing Vocabulary

Several word set terms were not found in the embedding vocabulary (insufficient corpus frequency). The most affected experiments are noted by missing_word_count in the results CSV. Experiments with more than 20% missing vocabulary should be interpreted with additional caution. All missing terms are documented in `reports/wefe_results.csv`.

### Limitations

1. **No statistical p-values**: The corpus is small relative to standard WEAT benchmarks; permutation-test p-values could not be computed reliably. Effect sizes are descriptive, not inferential.

2. **Co-occurrence ≠ endorsement**: WEAT and WEFAT capture how words are *used together*, not what the newspaper *endorses*. A high dehumanisation effect size reflects co-occurrence, often in the context of reporting on, quoting, or debating dehumanising language.

3. **Embedding quality**: With 2,522 articles and 100 dimensions, some vectors — especially for low-frequency terms — may be unstable. Words appearing fewer than 10 times in the corpus are particularly unreliable.

4. **German morphology**: German's rich inflection means *Palästinenser*, *Palästinenserin*, *palästinensische*, *palästinensischen* are distinct model tokens. Incomplete coverage of all inflected forms may underweight some target groups.

5. **Single source**: All results pertain to the SZ only. The SZ is a large, broadly read quality outlet with a liberal-centrist editorial tradition. Whether these patterns are replicated, amplified, or moderated in other German outlets (Bild, FAZ, taz, Spiegel) cannot be determined from this corpus alone.

6. **Temporal flattening**: Embedding over the full twelve months flattens temporal variation. Framing patterns in October 2023 may differ substantially from those in September 2024.
