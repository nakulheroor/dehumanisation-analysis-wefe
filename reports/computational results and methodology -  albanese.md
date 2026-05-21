**German Media Coverage of Palestinian Civilians and Journalists**  
**A Computational Analysis**

**By Academics for Justice, Decolonial Practices Group and Uni for Palestine Munich**

**ABSTRACT:** This report presents findings from a computational text analysis of German news coverage of the genocide in Gaza between October 2023 and March 2026\. Specifically, our analysis examines how Palestinians were represented across a diverse range of mainstream German news outlets, focusing on dehumanization, the denial of civilian status, and the defamation of Palestinian journalists. Whilst a deliberately heterogenous corpus was included to capture potential variation across outlets, our findings point towards remarkably uniform representations. Our findings show that the denial of civilian status was present in 30% of the sample; including in ‘left wing’ and ‘quality’ outlets. Such uniformity in coverage suggests not only some level of editorial guidance, but state and corporation level media influence. Moreover, we find 1955 articles exhibiting dehumanizing language within just 12 months, and the consistent delegitimization of Palestinian journalists. Besides the computational analysis, we present 3 important case studies of Palestinian journalists specifically targeted by the German media, before and after being murdered by Israel; Anas Al-Shahif, Ahmed Abu Mutair and Saleh Aljafarawi. Overall, the media analysis reveals how Palestinians were systematically represented in ways that normalized violence towards them, and shaped the German public’s perception towards the ongoing atrocities.

**Introduction**

“Bundestag unanimously pledges full solidarity with Israel” – *Sueddeutsche Zeitung*, 12.10.2023

Whilst the German government’s unanimous support for Israel through discourse (Bundesregierung, 2023), weapons exports (Bundestag, 2025; SIPRI, 2026\) and legal backing (ICJ, 2024\) is well known, German media coverage of Gaza in the period that followed October 2023 has not been properly documented or analyzed. Indeed, although several qualitative analysts and social media influencers – notably, including Fabian Goldmann and Nadia Zaboura – have drawn attention to cases of bias, and German news outlets publishing blatant propaganda (see: Zaboura, 2025; Goldmann, 2025), systematic empirical evidence is lacking. This matters hugely, because media coverage has the power to shape the public’s opinions, evaluation and basic knowledge of events (see: McCombs & Shaw, 1972). In a country with above average levels of trust in public institutions, including the media (OECD, 2024), the effects of the German news coverage analyzed in this report are undoubtedly profound and wide reaching. That said, recent surveys show that trust in German media, specifically in reporting on Palestine and Israel, continues to erode, resulting in only one quarter of Germans being convinced of the impartiality of German news coverage on the region since October 7th 2023 (Reinemann, 2025). Importantly, the research presented in this report is guided by the following research questions: (1) How did linguistic features such as passive versus active voice, blame attribution, and conflict framing shape representations, particularly in ways that may justify or undermine Palestinian civilian status? (2) To what extent did dehumanizing language appear in coverage, and how did this vary across outlets? And finally, (3) how did the German media represent and delegitimize Palestinian journalists? Whilst these questions cover several important aspects of the German news coverage of Palestinians from October 2023-March 2026, our analysis is by no means exhaustive; indeed, this report presents the initial findings of a working group compiled of academics, students and activists, that shall continue to dive deeper and add further evidence to our analysis of the German media.

The report is structured as follows; firstly, we provide a brief overview of the methods employed, before moving on to outline our analysis of the denial of civilian status, dehumanizing language and Palestinian journalists' representations. Finally, we conclude our report with key takeaways, and potential implications of our findings.

**Methodology** 

**Sample**

Our analysis focuses on German media coverage of Palestine and Israel following October 7th 2023 up until March 1st 2026\. The selected timeframe allows for an in-depth examination of media narratives following the events of October 7th, 2023, capturing both immediate reporting and longer-term discursive patterns, thus contributing to a deeper understanding of how media language can shape perceptions of legitimacy in contemporary conflict coverage. Our analysis includes six nationwide and well-established news outlets, namely “Die Tageszeitung“ (taz), “Süddeutsche Zeitung” (SZ), “Die Zeit”, “Die Welt”, and “BILD” which rank among the most-read news outlets in Germany. By this selection, we aimed to cover a broad range of the German media landscape across the political spectrum, with *taz*, *Der Spiegel*, and *Die Zeit* representing comparatively left-wing perspectives, while *Die Welt* and *BILD* can be situated on the more conservative end. With the exception of *BILD*, which is typically classified as a tabloid, the selected outlets are generally considered part of the quality press. In total, our analysis sample consists of 46,890 news articles (*BILD*: 7,000; *Der Spiegel*: 8,912; *Die Welt*: 10,047; *Die Zeit*: 6,128; SZ: 10,186; *taz*: 4,617) which have been published between October 2023 and March 2026\. This includes all articles published during the specified time period that were retrieved from the online databases *Wiso* and *Nexis Uni* using a search query filtering for at least one of the following keywords: “Gaza”, ”Israel”, “Hamas”, and “Palästina”. The full texts of the articles were obtained through web scraping techniques.

**Method**

Our analysis uses the large language model (LLM) *Gemini 3.1 Flash Lite* which showed the highest accuracy out of 4 tested LLMs to systematically classify news articles along three key dimensions of media narratives: (1) representation of Palestinian civilian status, (2) forms of dehumanization, and (3) discrediting of Palestinian journalists. For the exact prompt used for classification, please refer to Appendix A. Our results are reproducible with the provided code, although some variation in the results are expected across repeated runs due to the non-deterministic nature of LLMs. The sample of news articles underlying the analysis can also be provided upon request.  
The model is guided by a structured prompt with strict rules (e.g. evidence-based classification, separation of explicit vs. implied framing, and confidence ratings). Classifications are supported by textual evidence snippets that have been human-verified and labeled as non applicable (*NA*) when evidence is insufficient or the classification does not apply. To additionally determine the accuracy of LLM-based classification, we have sampled randomly across all the journals 50 articles for each of the categories that the model has flagged and had them verified manually by members of our team. We report as accuracy the percentage of human-verified articles for which both the model and one researcher agreed on a classification. The rate of false positives is therefore 100% minus the estimated accuracy. We have not estimated the rate of false negatives.  
First, for news articles discussing Palestinian deaths and suffering during the study period, *Palestinian civilian status representation* captures how affected Palestinians are framed: In the *recognized* category*,* Palestinian victims are explicitly identified as civilians or marked as non-combatants. *Implicitly denied,* refers to cases in which civilian status would be relevant but is not clearly specified, e.g. when killed Palestinians are described without clarification of their civilian or combatant status. Articles flagged as *partially denied* present contested or ambiguous descriptions, such as when civilian labels are followed by counterclaims, creating uncertainty about civilian versus combatant status. Finally, *explicitly denied* applies when Palestinians are clearly described as combatants or otherwise framed as military targets.  
Second, *dehumanization forms* capture whether and how Palestinians are framed in ways that diminish their personhood. *Animalistic or objectifying language* refers to descriptions that portray Palestinians using animal comparisons, subhuman imagery, or object-like terms that strip them of human status. *Collective threat framing* applies when Palestinians are depicted as a homogeneous and inherently dangerous group, without differentiation between individuals or subgroups. *Erasure of individual humanity* captures instances in which Palestinians are presented primarily as an impersonal mass, for example through purely statistical or anonymous representations that lack humanizing detail where such detail would be expected. *Justification or normalization of harm* refers to framing that presents harm against Palestinians as deserved, inevitable, or morally acceptable.   
Third, *discrediting of Palestinian journalists* assesses whether Palestinian media workers are portrayed as unreliable or lacking professional legitimacy. Articles are classified as *true* if they explicitly or implicitly cast doubt on the credibility, independence, or authenticity of Palestinian journalists, for example by suggesting links to militant groups, accusing them of propaganda, or questioning the accuracy of their reporting. The category *false* applies when Palestinian journalists are presented as credible or are discussed without such discrediting cues.   
The retrieved classifications are then aggregated by media outlets to enable cross-outlet comparison. In the following, we present our findings of the analysis.

To complement the LLM-based classification, we additionally applied the Word Embedding Fairness Evaluation (WEFE) framework (Badilla et al., 2020) using the Word Embedding Association Test (WEAT; Caliskan et al., 2017). WEAT quantifies linguistic bias by measuring the differential association of two target groups — for instance, *Palestinians* versus *Israelis* — with contrasting attribute sets (e.g., dehumanizing versus humanizing vocabulary) in the geometric space of a word embedding model trained on the corpus. The strength of this association is reported as an effect size (Cohen's *d*), where *d* ≥ 0.20 indicates a small, *d* ≥ 0.50 a medium, and *d* ≥ 0.80 a large effect. The WEFE analysis was restricted to *Süddeutsche Zeitung* articles covering the first year of the genocide (October 2023 – December 2024; N = 2,522 articles), for two reasons: first, training reliable domain-specific word embeddings requires a dense and internally coherent co-occurrence structure, which is best preserved within a single editorial source; second, *SZ* constituted the primary focus of our local media monitoring and archiving infrastructure during this period, and its volume and editorial consistency make it a suitable proxy for quality press coverage more broadly.

**Civilian status representation**  
Under International Humanitarian Law (IHL) ‘any person who is not a member of armed forces is considered to be a civilian’ (ICRC, n.d.), and is therefore protected. Within our analysis, we focused on the representation of Palestinian civilians, including men, women and children, to see whether their civilian status was recognized, or implicitly, partially, or explicitly denied. In total, we have identified 14,523 articles where civilian status is relevant. Out of those, 9,446 (68.0%) showed recognition, 4,435 (27.3%) showed implicit denial, and 642 (4.6%) showed partial or explicit denial. Strikingly, across the corpus, more than 30% of the articles mentioning Palestinian civilians show some form of civilian status denial. The majority of these cases were of ‘implicit denial’ (see Fig. 1), meaning that the articles cast doubt on civilian status. Word-embedding analysis on the SZ sub-corpus corroborates this pattern: a WEAT test comparing how Palestinians versus civilians are associated with civilian-status erasure terms (e.g., *Kämpfer* [fighter], *Terroristen*) against humanizing vocabulary yields a large effect size (*d* = 1.03), indicating that the term *Palestinians* is strongly and systematically embedded closer to civilian-status denial than the neutral word *civilians* in the corpus. A further WEAT test on death language agency finds that Palestinian deaths are encoded substantially closer to passive, agentless vocabulary (*gestorben*, *Todesfälle*) while Israeli deaths align more strongly with direct murder terminology (*ermordet*, *massakriert*), revealing a large structural asymmetry in the attribution of perpetrator accountability (*d* = 1.16) consistent with the implicit denial pattern.

**Figure 1: Civilian Status Across All Outlets**    
Notably, further analysis at the level of news outlets reveals variations in the proportion of articles denying Palestinians’ civilian status (see Fig. Two). Right-wing tabloid *BILD* contains the highest proportion of articles both implicitly and partially denying civilian status. All articles explicitly denying civilian status within the sample were from this outlet. Articles published in *Die Welt* revealed similarly high levels of civilian status denial (implicit and partial).  

Nonetheless, one important takeaway is that even within ‘quality’ and ‘left-wing’ outlets \- including *SZ* and *taz*) we still find a significant portion of articles implicitly, and sometimes partially denying Palestinians’ civilian status. This reveals some level of systematization in coverage; during the genocide, all German outlets included in this analysis included representations of Palestinians that undermined their civilian status to some degree, irrespective of the political leaning of the outlet, or the quality of investigative journalism. A WEAT test on editorial framing in the SZ sub-corpus (*d* = 1.03) registers a large and consistent association between Palestinian-related vocabulary and editorial-line terms (e.g., *Narrativ*, *Kampagne*, *Propaganda*) over editorial-independence terms, providing strong embedding-level evidence that the framing of Palestinians is anchored in a coordinated editorial register rather than treated as an independently reported subject.

**Figure 2: Palestinian Civilian Status Representation by Journal**

	

The estimated accuracy for this analysis (see methodology) is above 85% for the categories of partially or explicitly denied. However, one limitation of this analysis is that for the category, *implicitly denied*, the estimated accuracy is slightly lower, at 65%. This category flags articles where civilian status is relevant but not explicitly recognized, as well as generic terms (Palestinians, population…) and the use of passive constructions with no clear identification of the actor. The working group that author this report will extend upon and fine tune this analysis in our next steps.

**Dehumanization forms**  
Dehumanization can be understood as the representation of some individuals or groups in ways that remove or diminish their humanity, and may imply they are inferior and subhuman (Haslam, 2006). This could be achieved in several ways, including through framing groups as threatening, or justifying their harm (see: Kelman, 1973); two categories of dehumanization we focus upon in this report. Across the sample, a total of 1,593 articles are flagged by our models as showing some form of dehumanization. Taking into account that the time span is of approx. 30 months, this means that an average of more than 53almost 55 articles per month, or more than 13almost 14 per week, has been present in the German media. This finding is independently corroborated at the level of word embeddings: a WEAT test on the SZ sub-corpus finds that Palestinian-related terms are strongly associated with explicitly dehumanizing vocabulary — including terms such as *Barbaren* (barbarians), *Monster* (monsters), and *Gräueltat* (atrocity) — relative to humanizing terms, compared to the neutral baseline *civilians*, yielding a large effect size (*d* = 1.00).

As Fig. 1 demonstrates, most representations identified as dehumanizing by the model were justifying or normalizing the harm of Palestinian civilians (80% accuracy). Whilst the highest number of articles justifying and normalizing harm were published by *BILD* (411), this language was similarly employed across ideologically diverse and ‘quality’ news outlets, including *Der Spiegel* (275) and *SZ* (222). A WEAT test on death language in the SZ sub-corpus further shows that Palestinian deaths are described with more euphemistic vocabulary (*gestorben*, *leben verloren*) while Israeli deaths align more closely with direct murder terminology (*mord*, *ermordet*, *massaker*), amplifying the moral asymmetry embedded in the normalization of harm (*d* = 0.66).

**Figure 1: Dehumanization categories across all outlets**  
**![][image1]**  
The second category of dehumanizing language analysed across the news articles was *collective threat*, whereby Palestinian civilians were framed as a homogenous and dangerous mass. The model was 75% in identifying this form of dehumanizing language. As Fig. 1 illustrates, whilst the right wing tabloid, the *BILD* dominates with 67 instances of ‘collective threat’ framing, this form of dehumanization is present in all newspapers. Counts in Fig. 1 are non-exclusive; there are 45 flagged in both categories. Overall, similarly to the analysis of civilian status denial, our report demonstrates the clear and frequent presence of dehumanizing language \- through the justification of harm and collective threat frame \- in the representation of Palestinians across the diverse German news landscape. A WEAT test on violence framing in the SZ sub-corpus confirms this collective threat pattern: Palestinians are embedded significantly closer to negative violence terms (e.g., *Terrorist*, *barbarisch*, *zivile Ziele* [civilian targets]) while Israelis are closer to protective or defensive vocabulary, yielding a large effect size (*d* = 0.81). An additional WEAT test on hostage and prisoner framing reveals a striking asymmetry: Israeli captives are embedded closer to sympathy-laden hostage vocabulary (*Geisel*, *Geiselkrise*, *Befreiung* [release]) while Palestinian prisoners are associated with neutral detention terms (*Häftling*, *Inhaftiert*, *Gefangenschaft*), with a large effect size (*d* = 0.81), reflecting a differential humanization of captivity that further entrenches Palestinian dehumanization in the corpus.

It should be noted that the dehumanization forms shown in Fig. 1 are not the only ones present in German media sample. We have also found examples of animalistic or objectifying language. This was often present in reported speech, but without critique or context clarification, and often as part of the article’s main framing. We have also investigated the erasure of individuality present and found extensive examples in the media. While we don’t report quantitatively on this data,examples of dehumanizing animalistic or objectifying language can be found in the attached appendix. 

**The Systematic Discrediting of Journalists**  
Within the German news sample, 911 articles mentioned Palestinian journalists; notably, more than 30% (N=284) exhibited discrediting language (with model accuracy of above 90%). In this section, we briefly present an overview of the coverage of three cases of Palestinian journalists being defamed within the German news media. This section provides some insight into the consistent undermining of Palestinian journalists’ professional integrity within the German media, but is by no means exhaustive. To this date, 235 journalists and media workers have been killed in Gaza (IFJ, 2026), the majority of whom have been simply ignored or smeared as terrorists by the Israeli regime.

Word-embedding analysis on the SZ sub-corpus provides systematic corroboration of these discrediting patterns. A WEAT test on Hamas association (*journalist\_hamas\_association*) finds that Palestinian journalists are strongly embedded closer to militant-organization vocabulary than to press freedom terms, relative to general journalists, yielding a large effect size (*d* = 0.97) — the single strongest journalist-related signal in our embedding analysis. A WEAT test on terrorist labelling (*journalist\_terror\_labelling*, *d* = 0.64) similarly shows that Palestinian journalists are more strongly associated with terrorist labelling terms (e.g., *Terrorist*, *Propagandist*, *Militant*, *Islamist*) compared to professional journalistic vocabulary, corroborating the LLM-classified discrediting language at the semantic level. The results reflect how coverage consistently links Palestinian media workers to violence rather than to journalistic standards — a pattern that renders the defamatory framing documented in the case studies below structurally embedded in the corpus.

### **Anas Al-Sharif**

Anas al-Sharif was a 28-year-old correspondent for al-Jazeera. In 2024 he was awarded a Pulitzer Price for his photographic documentation of the genocide in Gaza. Only a year later the Israeli Defense Forces (IDF) defamed him as a Hamas operative. On August 10th, 2025 Anas al-Sharif was killed in an Israeli airstrike targeting the media tent outside of al-Shifa-Hospital. Four other journalists were killed alongside him. After the attack the Israeli Defense forces posted on X: 

“*STRUCK: Hamas terrorist Anas Al-Sharif, who posed as an Al Jazeera journalist*  
*Al-Sharif was the head of a Hamas terrorist cell and advanced rocket attacks on Israeli civilians and IDF troops. Intelligence and documents from Gaza, including rosters, terrorist training lists and salary records, prove he was a Hamas operative integrated into Al Jazeera. A press badge isn’t a shield for terrorism.*”  

This framing was copied 1:1 by the German media landscape. Instead of questioning the Israeli narrative, German outlets such as *der Spiegel*, *Süddeutsche Zeitung* or *Bild* used the Israeli military as a trusted primary source (DPA, 2025; der Spiegel, 2025, BILD, 2025), which is a classic example of journalistic malpractice. The Süddeutsche Zeitung even went as far as to directly adopt the IDF’s wording in their headline: “[Al-Jazeera correspondent killed  in Gaza \- Israel: Terrorist” and later supplemented this framing by quoting the IDF again](https://www.sueddeutsche.de/politik/nahost-al-dschasira-reporter-in-gaza-getoetet-israel-terrorist-dpa.urn-newsml-dpa-com-20090101-250811-930-899424) to further defame the Gazan journalist. The news outlet actively reproduces the narrative of Anas al-Sharif being “the head of a Hamas terrorist cell” thus justifying his murder. Only much later in the article are these statements relativized by Non-Governmental-Organizations, which criticize the Israeli regime and question the validity of these claims. This follows a distinct pattern of defamation of palestinian journalists by German media. Already a year prior another SZ-journalist conflated the journalist Ashraf al-Sarraj and Hossam Shabat as Hamas terrorists, based on inconclusive documents, provided by the Israeli state (Haase, 2024). 

**Ahmed Abu Mutair**  
**Ahmed Abu Mutair** was a 37-year-old broadcast engineer and media worker, employed by Palestine Media Production (PMP), a Gaza-based media company. Notably, PMP partnered with ZDF (German public broadcaster) over many years to provide local technical services for international news-gathering operations.

The IDF killed Ahmed Abu Mutair in a targeted drone strike at PMP’s headquarters on 19th October 2025, after claiming that he was a Hamas militant (Quassam Brigades). These claims of Hamas linkages were propagated by the German and international press (see example: Beug, 2025), but never independently verified in any transparent or judicial process. In fact, the claims were based entirely on Israeli documents. These accusations – and the subsequent news coverage – were heavily criticized by local and international journalist organizations (IFEX, 2025; CPJ, 2025). The Investigative reports and deep dives by *Der Spiegel* and *Paper Trail Media* noted blatant inconsistencies in the supporting documentation from Israel, and found no definitive external confirmation of the claim (Alkhalil Alnajjar *et al*., 2025). On top of this, Ahmed Abu Mutair’s brother, Dr. Mahmoud Abu Mutair spoke with the Committee to Protect Journalists (CPJ, 2025), sharing that his brother was not a member of any political group, and that the evidence from the IDF was entirely fabricated – for example, the documents included the wrong birthday, blood type, and the wrong number of children.

Despite the inconsistent evidence that lacked any independent verification, the German broadcaster ZDF suspended its cooperation with PMP entirely, based on the documents provided by Israel (Akrap. 2025). In doing so, ZDF silenced trusted, professional journalistic voices in Gaza.

### **Saleh Aljafarawi**

**Saleh Aljafarawi** was a Gaza-based freelance journalist, photographer and social media influencer who reported throughout the genocide in Gaza, from the front line. His reporting focused on civilians experiencing suffering during this period. Saleh was killed on October 12th 2025, days after a ceasefire agreement was established. He was 28 years old.

Since October 2023, German media outlets published content about Saleh Aljafarawi, initially, mocking his professional work, or accusing Saleh of being a ‘victim actor’ or producing ‘Pallywood content’ (Stroß, 2023). Following these baseless accusations that were debunked and criticized on the grounds of lacking evidence (see: Haaretz, 2025; Reuters, 2023), baseless accusations and suggestions of Hamas connections were shared widely by German news outlets (t-online, 2023).

**REPORT TAKEAWAYS**

* The denial of Palestinians’ civilian status was systemic in the German news media coverage from October 2023-March 2026, present across left, right, centre, quality and tabloid newspapers. This means international humanitarian law was consistently undermined. The issue is structural, not isolated to poor quality news outlets.  
* From October 2023 \- March 2026 almost 1600 articles were identified using dehumanizing language – that is, more than 13 per week. These were not isolated cases, but a pattern in coverage.  
* The German news media played a key role in undermining Palestinian journalists professional integrity and civilian status \- in some cases legitimizing their murder by the IDF.

## **CONCLUSION**

Our findings build upon some important analysis of other German news outlets (Grimm et al., 2025), providing special detail on the instances of civilian status denial, dehumanization, and the defamation of Palestinian journalists. We hope that our analysis will provide sufficient evidence to empirically demonstrate how widespread and systematic the patterns in coverage are in Germany, so that both individuals and institutions may be eventually held accountable for their words and actions. Importantly, the working group formed to produce this report \- including individuals from a range of grassroots organizations based in Munich \- shall continue this line of research, and extend upon the analysis by adding new outlets, and focusing on more dimensions of coverage. We would be happy to provide further details, extended analysis and materials upon request.

**REFERENCES** 

Akrap, D. (2025, October 28). *ZDF hält Mitarbeiter eines Dienstleisters für Hamas-Mitglied*. *taz – die tageszeitung*. [https://taz.de/ZDF-haelt-Mitarbeiter-eines-Dienstleisters-fuer-Hamas-Mitglied/\!6124974/](https://taz.de/ZDF-haelt-Mitarbeiter-eines-Dienstleisters-fuer-Hamas-Mitglied/!6124974/?utm_source=chatgpt.com)

Alkhalil Alnajjar, M., Antoniadis, N., Obermaier, F., Retter, M. and Schröd T. (2025, 7th November). Brilliant technician, loving father – and terrorist?. *Der Spiegel*. Available at: [https://www.spiegel.de/ausland/gaza-ahmed-abu-mutair-der-techniker-der-fuer-eine-zdf-partnerfirma-arbeitete-und-offenbar-hamas-mitglied-war-a-d3140169-4152-40ae-bd86-1e70fb4614b7?context=issue](https://www.spiegel.de/ausland/gaza-ahmed-abu-mutair-der-techniker-der-fuer-eine-zdf-partnerfirma-arbeitete-und-offenbar-hamas-mitglied-war-a-d3140169-4152-40ae-bd86-1e70fb4614b7?context=issue)

Badilla, P., Bravo-Marquez, F., & Pérez, J. (2020). WEFE: The Word Embedding Fairness Evaluation Framework. In *Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence* (pp. 430–436). [https://doi.org/10.24963/ijcai.2020/60](https://doi.org/10.24963/ijcai.2020/60)

Beug, S. (2025, October 28). *Gaza: Mitarbeiter von ZDF-Produktionsfirma war Hamas-Mitglied – Union spricht von „Skandal“*. WELT. [https://www.welt.de/kultur/medien/article68ff48c443484db51ab15e52/gaza-mitarbeiter-von-zdf-produktionsfirma-war-hamas-mitglied-union-spricht-von-skandal.html](https://www.welt.de/kultur/medien/article68ff48c443484db51ab15e52/gaza-mitarbeiter-von-zdf-produktionsfirma-war-hamas-mitglied-union-spricht-von-skandal.html)

BILD. (2025, August 11). *Israel tötet Al-Jazeera-Reporter Anas al-Sharif in Gaza*. [https://www.bild.de/news/ausland/israel-toetet-al-jazeera-reporter-anas-al-sharif-in-gaza-68991792204e050eae235be5](https://www.bild.de/news/ausland/israel-toetet-al-jazeera-reporter-anas-al-sharif-in-gaza-68991792204e050eae235be5) 

Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. *Science*, 356(6334), 183–186. [https://doi.org/10.1126/science.aal4230](https://doi.org/10.1126/science.aal4230)

Committee to Protect Journalists (CPJ). (2025). *Ahmed Abu Mutair.* Available at: [https://cpj.org/data/people/ahmed-abu-mutair/\#:\~:text=On%20October%2028%2C%20CPJ%20emailed,evidence%20remains%20unclear%20and%20inconclusive](https://cpj.org/data/people/ahmed-abu-mutair/#:~:text=On%20October%2028%2C%20CPJ%20emailed,evidence%20remains%20unclear%20and%20inconclusive).

Die Bundesregierung. (2023, October 7). *Germany continues to stand by Israel and is committed to de-escalation*. [https://www.bundesregierung.de/breg-en/news/support-israel-2228294](https://www.bundesregierung.de/breg-en/news/support-israel-2228294)

DER SPIEGEL. (2025, August 11). *Gaza-Krieg: Israel meldet Tötung von palästinensischem Journalisten Anas al-Sharif*. [https://www.spiegel.de/ausland/gaza-krieg-israel-meldet-toetung-von-palaestinensischem-journalisten-anas-al-sharif-a-9dfde0b5-c5d3-4a37-b52c-fe2e9d37aee1](https://www.spiegel.de/ausland/gaza-krieg-israel-meldet-toetung-von-palaestinensischem-journalisten-anas-al-sharif-a-9dfde0b5-c5d3-4a37-b52c-fe2e9d37aee1) 

DPA (Deutsche Presse-Agentur). (2025, August 11). *Nahost: Al-Dschasira-Reporter in Gaza getötet – Israel: Terrorist*. Süddeutsche Zeitung. [https://www.sueddeutsche.de/politik/nahost-al-dschasira-reporter-in-gaza-getoetet-israel-terrorist-dpa.urn-newsml-dpa-com-20090101-250811-930-899424](https://www.sueddeutsche.de/politik/nahost-al-dschasira-reporter-in-gaza-getoetet-israel-terrorist-dpa.urn-newsml-dpa-com-20090101-250811-930-899424) 

German Bundestag. (2025). *Response by the Federal Government to a parliamentary question regarding arms export licences to Israel (Oct 2023–May 2025\)*. [https://www.bundesregierung.de](https://www.bundesregierung.de)

Goldmann, F. (2025). *Untersuchung der Berichterstattung zum Gaza-Krieg* (media analysis excerpt commentary). NachDenkSeiten. [https://www.nachdenkseiten.de/?p=148504](https://www.nachdenkseiten.de/?p=148504)

Grimm, J. J., Könneker, J. M., & Salehi, M. (2025). Hierarchies in death: coverage of Palestinian and Israeli victims in the context of October 7 and the war on Gaza. *Peacebuilding*, 1-16.

Haaretz. (2025, September 22). *“They’re painting a target”: Gaza influencer’s followers raise alarm after IDF’s allegations*. [https://www.haaretz.com/middle-east-news/palestinians/2025-09-22/ty-article/.premium/theyre-painting-a-target-gaza-influencer-followers-raise-alarm-after-idfs-allegations/00000199-7054-db6e-a5d9-f67c73d30000](https://www.haaretz.com/middle-east-news/palestinians/2025-09-22/ty-article/.premium/theyre-painting-a-target-gaza-influencer-followers-raise-alarm-after-idfs-allegations/00000199-7054-db6e-a5d9-f67c73d30000)

Haase, K. (2024). *Mutmaßliche Hamas-Mitglieder wurden ins Münchner Protest-Camp zugeschaltet.* [Mutmaßliche Hamas-Mitglieder wurden ins Münchner Protest-Camp zugeschaltet \- München \- SZ.de](https://www.sueddeutsche.de/muenchen/muenchen-nahostkonflikt-palaestina-camp-hamas-terror-antisemitismus-firm-lux.Qegy4B26haaHXbX6aVFa5t?reduced=true) 

HaslamN.StratemeyerM. (2016). Recent research on dehumanization. *Curr. Opin. Psychol*. 11, 25–29. 

International Committee of the Red Cross (ICRC). (n.d.). *Rule 5\. Definition of civilians*. Customary IHL Database. [https://ihl-databases.icrc.org/pt/customary-ihl/v2/rule5](https://ihl-databases.icrc.org/pt/customary-ihl/v2/rule5) 

IFEX. (2025, October 22). *Israeli strike on Gaza media site another war crime against journalists*. [https://ifex.org/israeli-strike-on-gaza-media-site-another-war-crime-against-journalists/](https://ifex.org/israeli-strike-on-gaza-media-site-another-war-crime-against-journalists/)

International Court of Justice. (2024). *Application of the Convention on the Prevention and Punishment of the Crime of Genocide (Nicaragua v. Germany) — Provisional measures order*. [https://www.icj-cij.org](https://www.icj-cij.org)

International Federation of Journalists (IFJ). (2026, April 9). *Palestine: At least 235 journalists and media workers killed in Gaza*. [https://www.ifj.org/media-centre/news/detail/article/palestine-at-least-235-journalists-and-media-workers-killed-in-gaza](https://www.ifj.org/media-centre/news/detail/article/palestine-at-least-235-journalists-and-media-workers-killed-in-gaza) 

Kelman, H. C. (1973). Violence without moral restraint: Reflections on the dehumanization of victims and victimizers. *Journal of Social Issues, 29*(4), 25–61. [https://doi.org/10.1111/j.1540-4560.1973.tb00102.x](https://doi.org/10.1111/j.1540-4560.1973.tb00102.x) 

McCombs, M. E., & Shaw, D. L. (1972). *The agenda-setting function of mass media*. Public Opinion Quarterly, 36(2), 176–187.

OECD. (2024). *OECD survey on drivers of trust in public institutions 2024: Country note – Germany*. [https://www.oecd.org/en/publications/2024/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2024-results-country-notes\_33192204/germany\_1b23ffcd.html](https://www.oecd.org/en/publications/2024/06/oecd-survey-on-drivers-of-trust-in-public-institutions-2024-results-country-notes_33192204/germany_1b23ffcd.html)

Reinemann, C. (2025, November 26). Wahrnehmung der Nahostberichterstattung. Tendenz, Qualität und Vertrauen im Urteil der Bevölkerung im Herbst 2025\. CIVIS Mediendialog, Berlin, den 26\. November 2025	[CIVIS-Mediendialog-2025-11-26-Vortrag-Reinemann.https://www.civismedia.eu/wp-content/uploads/2025/12/CIVIS-Mediendialog-2025-11-26-Vortrag-Reinemann.pdf](https://www.civismedia.eu/wp-content/uploads/2025/12/CIVIS-Mediendialog-2025-11-26-Vortrag-Reinemann.pdf) 

Reuters. (2023, December 8). *Fact check: Palestinian YouTuber’s Qatar video predates Israel-Hamas war*. [https://www.reuters.com/fact-check/palestinian-youtubers-qatar-video-predates-israel-hamas-war-2023-12-08/](https://www.reuters.com/fact-check/palestinian-youtubers-qatar-video-predates-israel-hamas-war-2023-12-08/) 

Stockholm International Peace Research Institute. (2026). *Global arms flows jump nearly 10 per cent as European demand soars*. [https://www.sipri.org](https://www.sipri.org)

Stroß, P. (2023, November 8). *Ist „Gaza Joe“ ein Opfer-Schauspieler für die Hamas?* Kölnische Rundschau. [https://www.rundschau-online.de/politik/propaganda-im-krieg-ist-gaza-joe-ein-schauspieler-fuer-die-hamas-mr-fafo-palaestinensischer-influencer-saleh-aljafarawi-pallywood-679236](https://www.rundschau-online.de/politik/propaganda-im-krieg-ist-gaza-joe-ein-schauspieler-fuer-die-hamas-mr-fafo-palaestinensischer-influencer-saleh-aljafarawi-pallywood-679236) 

t-online. (2023, November 8). *Hamas-Propaganda: „Gaza Joe“ – Wer ist Saleh Aljafarawi?* [https://www.t-online.de/nachrichten/ausland/krisen/id\_100276500/hamas-propaganda-gaza-joe-wer-ist-saleh-aljafarawi-.html](https://www.t-online.de/nachrichten/ausland/krisen/id_100276500/hamas-propaganda-gaza-joe-wer-ist-saleh-aljafarawi-.html) 

Zaboura, N. (2025). *Media coverage of the Middle East and the need for broader context* (Interview). KNA Mediendienst. [https://mediendienst.kna.de/250626-89-00221.html](https://mediendienst.kna.de/250626-89-00221.html)

 

# APPENDIX A

## Methodology regarding the LLM models used for the classification

We provide here the prompt used for the LLM model to provide the classification across three different fields. All of our results are reproducible and we have reported the estimated accuracy in the main text. 

We evaluated our code on four models spanning different categories from *OpenAI* and *Google*. We found that *Gemini 3 Preview* and *Gemini 3.1 Flash Lite* achieved the highest accuracy; given their similar performance, we selected the latter. Note that these models are non-deterministic, so some variation between runs is expected.

**\# Media narrative analysis**

You are a researcher analyzing the framing used by media when reporting about the policies and practices of the state of Israel toward the Palestinian people. Your focus is media narrative and discursive practices. You follow these general rules:

\- Report only what is supported by the supplied article text.  
\- Distinguish between explicit statements, implied framing, and uncertain cases.  
\- Do not treat quoted or attributed language as the article's own framing unless the article explicitly adopts, endorses, or generalizes that language in its own narrative voice. Statements by interviewees, officials, witnesses, protesters, social media posts, slogans, or other quoted sources should not on their own determine the classification.  
\- If evidence is weak or ambiguous, report it as well.  
\- For each classification, also report confidence as high, medium, or low. Confidence should reflect the strength and directness of the textual evidence, the amount of interpretation required, and the degree of ambiguity or competing alternatives. Use high when the article text directly and clearly supports the classification, medium when the classification is supported but requires some interpretation or depends on indirect framing, and low when the evidence is weak, ambiguous, mixed, or close to NA. Borderline cases should be downgraded to NA rather than assigned an unsupported low-confidence label.  
\- Do not infer an outlet-wide editorial policy from one article alone.  
\- Use concise evidence-based language.

**\# Task**

Your task is to evaluate an individual article across a set of dimensions, to write your reasoning supporting the classification, and to provide evidence snippets supporting the classification. Each evidence snippet should directly support the classification and not require additional interpretation. If a classification cannot be clearly supported by a specific snippet, it should be downgraded to NA.

**\#\# Palestinian civilian status representation**  
Apply this field in the following order: if the article doesn't discuss Palestinian deaths, injuries, displacement, detention, humanitarian deprivation, vulnerability to attack, or other contexts in which civilian status would matter, assign NA. Otherwise, assign one of the following categories.

\* **recognized**: if the article clearly and directly identifies the affected Palestinians as civilians or otherwise clearly marks them as non-combatants, for example through terms such as civilians, civilian population, families, children, women, patients, aid workers, journalists, residents, worshippers, or equivalent wording that clearly distinguishes them from fighters. Do not use recognized based only on generic references to Palestinians, people, victims, the population, those in Gaza, humanitarian suffering, or deaths in Gaza without explicit civilian or non-combatant identification.

\* **implicitly\_denied**: Choose this category if one of the following cases applies regarding Palestinians:  
 \- if civilian status would be relevant but is not clearly recognized.  
 \- the article uses generic terms such as Palestinians, people, population, or individuals without clearly identifying civilian status.  
 \- Passive constructions with no identity clarification of the actor, like “Ten Palestinians were killed in clashes”.  
 \- Focus on “clashes” or “violence” instead of victims, like “Casualties were reported following the strike.”

\* **partially\_denied**: Choose this category if one of the following cases applies regarding Palestinians:  
 \- The civilian label is followed by a counterclaim.  
 \- Civilian and combatant ambiguity is present.  
 \- Competing narratives presented without resolution, for example, “Local officials said the victims were civilians, but Israel said they were militants”, “The dead included civilians, though some were suspected fighters”.

\* **explicitly\_denied**: if the article clearly labels the relevant Palestinians as militants, combatants, terrorists, or legitimate military targets, or directly rejects civilian classification.

\* **NA:** if the article mentions Palestinians, Palestine, Gaza, or pro-Palestinian actors but does not discuss Palestinian deaths, injuries, displacement, detention, humanitarian deprivation, vulnerability to attack, or any other context in which civilian status would matter. This includes articles mainly about protests, slogans, diplomacy, party politics, cultural controversy, antisemitism debates, international law debates in the abstract, or general political reactions, even when Palestine or Gaza is central to the article.

If there is evidence for more than one, choose the most severe category, where the order from less to more severe is: recognized, implicitly\_denied, partially\_denied, explicitly\_denied.

Evidence snippets for this field must directly support the classification. Generic references to Gaza, Palestine, suffering, deaths, or humanitarian conditions are not sufficient evidence for recognized unless the snippet explicitly identifies civilians or another clearly non-combatant group.

**\# Dehumanization forms**  
Choose one or more of the following (except if NA):

\* **animalistic\_or\_objectifying\_language**: when Palestinians are described through animal comparisons, infestation language, subhuman imagery, or object-like terms that strip personhood, including wording that treats them primarily as targets, collateral, or obstacles rather than people. Do not use this category for ordinary military terminology unless Palestinians themselves are being reduced to objects.

\* **collective\_threat\_framing**: when Palestinians are portrayed as a single dangerous mass or population-level threat, with little or no distinction among individuals, civilians, or subgroups. Do not use this category merely because the article discusses security threats from Hamas or other armed groups; use it only when the threat framing extends to Palestinians broadly.

\* **erasure\_of\_individual\_humanity**: when the article's own framing presents Palestinians primarily as an impersonal, undifferentiated mass in a way that strips personhood, human significance, or moral salience, for example as an anonymous mass, as statistics only, or as bodies without names, relationships, voices, or human descriptors where such humanization would normally be relevant. Do not use this category merely because the article reports casualty figures, refers to Palestinians as a population, or lacks names, interviews, or personal stories. Ordinary summary reporting on war, displacement, or humanitarian conditions often uses collective or statistical language and should not by itself be treated as dehumanizing. Do not assign this category when the broader context of the article is clearly sympathetic to Palestinian suffering or critical of dehumanization, unless the article itself still adopts dehumanizing framing in its own voice.

\* **justification\_or\_normalization\_of\_harm**: when harm to Palestinians is presented as deserved, inevitable, acceptable, morally unproblematic, or not requiring serious concern. This includes statements implying they brought it on themselves, that harsh treatment is necessary, or that large-scale suffering is simply the natural price to be paid. Use this category when claims such as "Hamas is hiding weapons in civilian infrastructure" are used to report or justify civilian deaths. Do not use this category for factual descriptions of harm, military action, or competing political arguments unless the article clearly endorses or normalizes the harm.

\* **NA**: When none of the other categories applies. Or if the article mentions Palestinians, Palestine, Gaza, or pro-Palestinian actors but does not discuss Palestinian deaths, injuries, displacement, detention, humanitarian harm, vulnerability to attack, or any other context in which civilian status would matter, for example in articles mainly about protests, slogans, diplomacy, party politics, or cultural controversy.

**\# Discrediting of palestinian journalists**

Choose one of the following:

\* **true**: when the article explicitly or implicitly casts doubt on the credibility, independence, honesty, authenticity, or professional legitimacy of Palestinian journalists, Palestinian photojournalists, Gaza-based reporters, or other Palestinian media workers. This includes:  
 \- Suggestions that they are linked to Hamas or other armed groups.  
 \- Suggestions that they are acting as propagandists rather than journalists.  
 \- Suggestions that they are staging, manipulating, fabricating, or falsifying reporting, images, footage, or casualty documentation.  
 \- Suggestions that they are unreliable because of political affiliation, identity, or location.  
 \- Questions, insinuations, and attributed accusations can still count as discrediting when they foreground suspicion, for example asking whether Palestinian journalists were instrumentally used by Hamas or stating that someone presented as a journalist was really a militant or only posing as a journalist.

 Do not code this field for criticism of media in general, Israeli media, Western media, social media users, or non-Palestinian journalists unless the article is specifically discussing Palestinian journalists. 

\* **false**: when Palestinian journalists or palestinian media are discussed without such doubt, or are presented as credible, trustworthy, or ordinary journalistic sources.  
 Do not code this field when other media (Israeli media, Western media, social media users, or non-Palestinian journalists) appear, unless the article is specifically discussing Palestinian journalists.

\* **NA**: when the article does not discuss Palestinian journalists, Palestinian photojournalists, Gaza-based reporters, or other Palestinian media workers specifically.

Evidence snippets should capture the actual discrediting or credibility-granting language, not merely any mention of journalism or media.

Return ONLY valid JSON matching this exact schema:  
\`\`\`json  
{  
 "palestinian\_civilian\_status\_representation": {  
   "classification": "recognized" | "implicitly\_denied" | "partially\_denied" | "explicitly\_denied" | "NA",  
   "reasoning": "string",  
   "evidence\_snippets": "array of type string",  
   "confidence": "high" | "medium" | "low"  
 },

 "dehumanization\_forms": {  
   "classification": 'array with elements among ("animalistic\_or\_objectifying\_language" | "collective\_threat\_framing" | "erasure\_of\_individual\_humanity" | "justification\_or\_normalization\_of\_harm" | "denial\_of\_civilian\_existence"| "NA")',  
   "reasoning": "string",  
   "evidence\_snippets": "array of type string",  
    "confidence": "high" | "medium" | "low"  
 },

 "discrediting\_palestinian\_journalists": {  
   "classification": "true" | "false" | "NA" ,  
   "reasoning": "string",  
   "evidence\_snippets": "array of type string",  
   "confidence": "high" | "medium" | "low"  
 },  
}  
\`\`\`  
Fill in "reasoning" field with a concise explanation in English, independently of the language of the article. Reproduce the evidence snippets verbatim. Always fill the evidence snippet except when the classification is NA.  
Do NOT include any text outside the JSON object.

# APPENDIX B

## Evidence snippets of articles showing discrediting of journalist

We provide here some evidence snippets, that have been human verified, of articles that explicitly discredit journalists, of some of the media outlets analyzed. We provide both evidence snippets that cast doubts on general media and information from sources based in Gaza, as well as snippets that target individual Journalists by linking them to Hamas and reproducing discourses that justify their killing. We provide both the original in German as well as an English translation. Sometimes we have added a brief note after the snippet when clarification of context was relevant.

**BILD, 11.11.2023**   
**Journalisten als Komplizen des Terrors\!; Der böse Verdacht gegen einige Medien bleibt.**  
---

Journalisten als Komplizen des Terrors\!   
Journalists as accomplices of terror\!

Wie wahrscheinlich ist es, dass Terroristen und Journalisten unter einer Decke stecken?   
How likely is it that terrorists and journalists are under the same blanket?

Ist unabhängige Berichterstattung aus dem Gazastreifen möglich? Es ist weitgehend unmöglich. Grund: Die Hamas kontrolliert das Gebiet, setzt Journalisten unter Druck. Die Reporter können sich nicht frei bewegen.   
Is independent reporting from the Gaza Strip possible? It is largely impossible. The reason: Hamas controls the territory and puts pressure on journalists. Reporters cannot move freely.

**BILD, 15.10.2023**   
**Babys aus Plastik, Horror-Bilder aus Syrien; Die übelsten Fakes im Hamas-Krieg.**  
---

Die Hamas-Führung ist seit vielen Jahren dafür bekannt, immer wieder Videos zu inszenieren. Es gibt dafür sogar einen eigenen Begriff: "Pallywood" \- ein Kunstwort aus Palästinensern und Hollywood. So werden etwa  Kleinkinder Richtung israelischer Soldaten geschubst , damit es Aufnahmen gibt, die für die Soldaten ungünstig aussehen.  
The Hamas leadership has been known for many years for repeatedly staging videos. There's even a term for it: "Pallywood"—a portmanteau of Palestinian and Hollywood. For example, small children are pushed toward Israeli soldiers to create footage that looks unfavorable to the soldiers.

**BILD, 17.10.2023**  
**Zivile Opfer in Gaza; Verbreitet die UN ungeprüft Hamas-Propaganda?**  
---

Jedes getötete oder verletzte Kind \- selbst ungeborene Babys \- werden vom Hamas-"Gesundheitsministerium" in die Kameras der Hamas loyalen Medien gehalten.  
Every child killed or injured—even unborn babies—is held up by the Hamas "Ministry of Health” to the cameras of Hamas-loyal media. 

Doch aus diesen Aufnahmen ergibt sich ein ganz anderes, verifizierbares Bild. Nämlich, dass nicht "Hunderte und Hunderte" Kinder pro Tag Opfer der Luftangriffe werden, sondern eine mittlere einstellige Zahl. Woher stammen also die Bilder Dutzender aufgereihter getötete Kinder "aus Gaza"? Zumeist aus Syrien.  
But these images paint a completely different, verifiable picture: that it is not "hundreds and hundreds" of children who fall victim to the airstrikes each day, but rather a moderate single-digit number. So where do the images of dozens of dead children lined up "from Gaza" come from? Mostly from Syria.

**BILD, 30.10.2023**  
**Bodenoffensive kommt schnell voran; Israel will Gaza-Stadt einkesseln\!**  
---

Hamas-nahe Journalisten filmten die Szene aus einiger Entfernung, bevor sie das Weite suchen.  
Journalists close to Hamas filmed the scene from a distance before fleeing.

**BILD, 02.11.2023**  
**Rätsel um RAKETEN-KRATER; KRIEG GEGEN DEN TERROR BILD hakt nach.**  
---

Gibt es unabhängige Berichterstattung und prüfbare Bildquellen über Raketenangriffe? Es gibt im Gazastreifen arabische und palästinensische Journalisten sowie Mitarbeiter von internationalen Nachrichtenagenturen (AP, AFP, Reuters), dazu über zehn TV-Sender. ABER: Ihre Unabhängigkeit muss bezweifelt werden. Viele sympathisieren mit der Hamas, die in die Berichterstattung eingreifen kann.  
Are there independent reports and verifiable sources of images from rocket attacks? There are Arab and Palestinian journalists in the Gaza Strip, as well as staff from international news agencies (AP, AFP, Reuters), and over ten TV stations. BUT: Their independence is questionable. Many sympathize with Hamas, which can interfere with the reporting.

**BILD, 09.11.2023**  
**Kommentar von BILD-Chefin Marion Horn; Journalisten als Terror-Helfer?**  
---

Journalisten als Terror-Helfer?   
Journalists as accomplices of terrorism?

**BILD,11.11.2023**  
**Nur Hamas-Bilder vom Massaker; So betrieb der Terror-Fotograf Propaganda**  
---

Auch von dort lieferte Eslaiah nur Hamas-Propaganda \- MIT dem Leid der Palästinenser.   
Even from there, Eslaiah delivered nothing but Hamas propaganda—using the suffering of the Palestinians.

Angesichts der Fotos aus Israel muss die Frage erlaubt sein: Was kann man von dem, was man auf den Gaza-Fotos von Fotografen wie Hassan Eslaiah sieht, überhaupt glauben?   
In light of the photos from Israel, one must be allowed to ask: What, if anything, can we believe of what we see in the Gaza photos taken by photographers like Hassan Eslaiah?

Nach dem Skandal stellt sich die Frage: Welchen Bildern aus Gaza können wir noch glauben?  
In the wake of the scandal, the question arises: Which images from Gaza can we still believe?

**BILD, 31.12.2023**  
**Dramatischer Moment nach Luftangriff; 10 Monate altes Baby aus Gaza-Trümmern gerettet**  
---

Auch lokale Journalisten sind vom Wohlwollen der Terroristen abhängig, haben teilweise einen engen Draht zur Hamas.  
Local journalists, too, are dependent on the goodwill of the terrorists and, in some cases, have close ties to Hamas.

**SPIEGEL ONLINE, 07.04.2025**  
**Roter Halbmond wirft israelischen Soldaten Tötungsabsicht vor**  
---

Israel hat Journalisten im Gazastreifen mehrfach vorgeworfen, für die Hamas tätig zu sein. Mehrere Medien in dem Küstenstreifen stehen der Islamistenorganisation nahe.  
Israel has repeatedly accused journalists in the Gaza Strip of working for Hamas. Several media outlets in the coastal enclave are affiliated with the Islamist organization.

**SPIEGEL ONLINE, 28.10.2025**  
**In Gaza getöteter Ingenieur war Hamas-Mitglied; Unionspolitiker kritisieren ZDF**  
---

Die Tarnung als angebliche Journalisten und Techniker ist eine der perfidesten Methoden der Islamisten. Leider sind allzu viele Medien weltweit auch bei ihrer Berichterstattung darauf reingefallen.  
Disguising themselves as so-called journalists and technicians is one of the most insidious tactics used by Islamists. Unfortunately, far too many media outlets around the world have fallen for this ruse in their reporting.

*Note: See report on Ahmed Abu Mutair of terrorism in the main text.* 

**Der Spiegel,  07.11.2025**  
**Tod am Sendewagen**  
---

Zugleich berichten Journalisten vor Ort, dass einige Kollegen eine große Nähe zu den herrschenden Islamisten pflegten. Dazu gehörten nicht nur die Mitarbeiter des Hamas-finanzierten Fernsehsenders Al-Aqsa TV und anderer Propagandaorgane, sondern auch ­einige Reporter des katarischen Nachrichtensenders Al Jazeera.  
At the same time, journalists on the ground report that some of their colleagues maintained close ties to the ruling Islamists. This included not only staff members of the Hamas-funded television station Al-Aqsa TV and other propaganda outlets, but also some reporters from the Qatari news channel Al Jazeera.

*Note: See report on Ahmed Abu Mutair of terrorism in the main text.* 

**SPIEGEL Plus,14.11.2025**  
**Weniger Moral und Empörung, bitte\!**  
---

Besonders BBC Arabic hat sich offenbar wiederholt auf Augenzeugen gestützt, die den Terroranschlag vom 7\. Oktober feierten.  
BBC Arabic, in particular, has apparently repeatedly relied on eyewitnesses who celebrated the terrorist attack on October 7\.

Kürzlich wurde ein freier Mitarbeiter des Senders in Gaza getötet. Es stellte sich heraus, dass er offenbar ein Hamas-Kämpfer war.  
A freelance contributor to the network was recently killed in Gaza. It turned out that he was apparently a Hamas fighter.

**WELT ONLINE, 11.01.2024**  
**Krieg in Nahost; Geisel-Angehörige rufen mit Lautsprechern Botschaften nach Gaza**  
---

Die israelische Armee hat zwei bei einem Luftangriff im Gaza-Streifen getötete palästinensische Journalisten des Fernsehsenders Al-Dschasira als Mitglieder von "Terrororganisationen" bezeichnet.  
The Israeli military has described two Palestinian journalists from Al Jazeera who were killed in an airstrike in the Gaza Strip as members of “terrorist organizations.”

Geheimdienstinformationen hätten bestätigt, dass Hamsa Wael Dahduh und Mustafa Thuria im Gaza-Streifen ansässigen Terrororganisationen angehört hätten, erklärte die Armee am Mittwoch.  
Intelligence reports confirmed that Hamsa Wael Dahduh and Mustafa Thuria belonged to terrorist organizations based in the Gaza Strip, the military said on Wednesday.

**WELT ONLINE,21.04.2024**  
**Nahost-Konflikt; Etwas stimmt nicht bei diesem prämierten World-Press-Foto**  
---

Man mag kaum glauben, dass dieser Moment nicht inszeniert ist. Dazu ist alles zu perfekt. Und man sträubt sich gegen die Indienstnahme eines Moments großer Trauer für eine im Grunde politische Aussage, für einen propagandistischen Effekt.  
It is hard to believe that this moment is not staged. Everything is too perfect for that. And one resists the exploitation of a moment of great grief for what is essentially a political statement, for a propagandistic effect. The photo conveys: Innocent people are being subjected to horrific suffering—by Israel. Two victims, who are nothing but victims, are depicted. Pure humanity.

*Note: This paragraph refers to the photography of Mohammed Salem that won the World Press Photo of the Year 2024\. See full article for context.* 

**WELT ONLINE, 02.08.2024**  
**Gazastreifen; Getöteter Al-Dschasira-Journalist war laut Israel Hamas-Kämpfer**  
---

Bei dem im Gazastreifen getöteten Korrespondenten des arabischen Fernsehsenders Al-Dschasira, Ismail al-Ghoul, handelt es sich nach Angaben der israelischen Armee um einen Hamas-Kämpfer.  
According to the Israeli army, Ismail al-Ghoul, the correspondent for the Arab television network Al Jazeera who was killed in the Gaza Strip, was a Hamas fighter.

Der Hamas-Kämpfer sei ,,aktiv an der Aufnahme und Verbreitung von Inhalten über die Angriffe auf israelische Truppen beteiligt" gewesen  
The Hamas fighter was “actively involved in recording and disseminating content about the attacks on Israeli troops.”

Israels Kommunikationsminister Schlomo Karhi hatte Al-Dschasira im Juni als ,,ein Sprachrohr des Terrorismus im Dienste der Hamas" bezeichnet.  
In June, Israel’s Communications Minister Shlomo Karhi had described Al Jazeera as “a mouthpiece for terrorism in the service of Hamas.”

**WELT ONLINE,  26.12.2024**  
**Bei israelischem Angriff; Fünf palästinensische Journalisten in Gaza getötet**  
---

Bei einem israelischen Angriff auf das Fahrzeug des palästinensischen, mit der islamistischen Miliz Islamischer Dschihad verbundenem TV-Sender Al-Kuds Today sind nach Senderangaben fünf palästinensische Journalisten getötet worden.   
According to the station, five Palestinian journalists were killed in an Israeli attack on a vehicle belonging to the Palestinian TV station Al-Quds Today, which is affiliated with the Islamist militia Islamic Jihad.

**WELT ONLINE, 11.08.2025**  
**Krieg in Gaza; Bundesregierung fordert Israel auf, Tötung von Journalisten zu erklären**  
---

Er habe sich als Al-Dschasira-Journalist ausgegeben, aber eine Terrorzelle der islamistischen Hamas angeführt, erklärten die israelischen Streitkräfte auf X. Der israelischen Armee zufolge sei das durch Geheimdienstinformationen und Dokumente aus Gaza belegt. Er war von Israel schon länger als Hamas-Aktivist beschuldigt worden. Schon in der Vergangenheit hatte es Debatten über Hamas-Verbindungen von Journalisten im Gazastreifen gegeben.  
He had posed as an Al Jazeera journalist but was actually leading a terrorist cell affiliated with the Islamist group Hamas, the Israeli military stated on X. According to the Israeli army, this is substantiated by intelligence reports and documents from Gaza. Israel had long accused him of being a Hamas activist. There have been debates in the past about journalists in the Gaza Strip having ties to Hamas.

*Note: see the report on Al-Scharif on the main text.* 

**WELT ONLINE, 24.11.2025**  
**Neues Feature auf X; Donald Trumps Fans twittern massenhaft aus Nigeria, Russland und Pakistan**  
---

Ein Journalist in Gaza-Stadt, der von der BBC als Augenzeuge zitiert wurde, schreibt laut seines Accounts aus Polen  \- auch über das aktuelle Wetter und über gerade angeblich stattfindende israelische Luftangriffe. Mittlerweile postet er Videos von sich aus Gaza, um zu beweisen, dass er tatsächlich vor Ort ist.  
A journalist in Gaza City, who was quoted by the BBC as an eyewitness, writes on his account from Poland—including about the current weather and alleged Israeli airstrikes taking place at the moment. He has since been posting videos of himself in Gaza to prove that he is actually there.

**Die Zeit, 12.12.2024**  
**Immer Ärger mit Resolutionen; Der PEN Berlin droht, sich zu zerlegen. Warum nur, um Gottes willen?**  
---

Die Unzufriedenheit entzündet sich unter anderem an der Frage, ob es statthaft ist, auch jene palästinensischen Journalisten als »Kolleg:innen« zu bezeichnen, die sich in den Dienst antiisraelischer Propaganda gestellt haben.  
The discontent stems, among other things, from the question of whether it is appropriate to refer to Palestinian journalists who have placed themselves at the service of anti-Israel propaganda as “colleagues”.

ZEIT-online, 12.06.2025  
**Leserbriefe zur Ausgabe 24/2025**  
---

Aber wer kann sich erinnern, jemals in der Tagesschau das Bild eines getöteten Hamas Kämpfers gesehen zu haben? Woran liegt das? Die Bilder, die wir aus Gaza zu sehen bekommen, sind fast ausschließlich Bilder der Hamas.  
But who can remember ever seeing a picture of a killed Hamas fighter on the evening news? Why is that? The images we see from Gaza are almost exclusively of Hamas.

**ZEIT-online, 02.10.2025**  
**Leserbriefe zur Ausgabe 41/2025**  
---

Die Tatsache, dass Bilder aus Gaza nur nach Zensur durch die Hamas in die Öffentlichkeit gelangen, ist den Verantwortlichen offenbar nicht wirklich bewusst.  
Those in charge are apparently not truly aware of the fact that images from Gaza only reach the public after being censored by Hamas.  
SZ,  09.11.2023  
**Küsschen von der Hamas**  
---

Wer in Gaza für Medien arbeitet, tut das nicht gegen den Willen der Hamas.  
Anyone working for the media in Gaza does not do so against Hamas’s will.

\[...\] dass einheimische Fotografen und Videojournalisten, die längerfristig vor Ort das Geschehen dokumentieren, das nicht gegen den Willen der Machthaber tun können.  
\[...\] that local photographers and videojournalists who have been documenting events on the ground over the long term cannot do so against the will of those in power.

Israels Regierungschef Benjamin Netanjahu ist sich sicher, dass Journalisten 'Komplizen bei Verbrechen gegen die Menschlichkeit' gewesen seien  
Israeli Prime Minister Benjamin Netanyahu is certain that journalists have been “accomplices to crimes against humanity”

Wie nah sind die freien Mitarbeiter internationaler Medien in Gaza dran an der Terrororganisation – oder kann man gar nicht mehr von Nähe sprechen, weil sie fast schon Teil von ihr sind?  
How close are the freelance journalists working for international media in Gaza to the terrorist organization—or is it no longer even possible to speak of proximity, since they are practically part of it?

# APPENDIX C

## Evidence snippets of articles flagged with civilian status denial

**BILD, 08.10.2023**  
**Terror-Erziehung in Gaza; Hamas-Kinder demütigen israelische Geisel**  
---

Category: Implicitly denied  
---

In einem der vielen Horror-Videos aus dem Gazastreifen ist zu sehen, wie die Hamas ihre eigenen Kinder zu unmenschlichen Terroristen erzieht.  
In one of the many horror videos from the Gaza Strip, we see how Hamas is raising its own children to become inhuman terrorists.

**BILD, 12.10.2023**  
**Experten warnen vor Terror auch bei uns; Haben "Hunderttausende" Antisemiten zu uns gelassen**  
---

Category: Implicitly denied  
---

Nach dem schrecklichen Terrorangriff der Hamas wird Israel im Gazastreifen massiv gegen die Hamas vorgehen, das wird auch dort zu vielen Toten führen. Diese Bilder wird die Terrororganisation natürlich für sich nutzen, es ist sogar zu befürchten, dass sie gezielt auch Opfer instrumentalisieren wird, Kinder und Frauen möglicherweise sogar als lebendige Schutzschilde benutzt  
Following the horrific Hamas terrorist attack, Israel will take massive action against Hamas in the Gaza Strip, which will also result in many deaths there. The terrorist organization will, of course, exploit these images for its own purposes; there are even fears that it will deliberately instrumentalize victims, possibly even using children and women as human shields.

**BILD, 13.10.2023**  
**Kommentar zu Gaza-Hilfen; Hört endlich auf, den Schlächtern Geld zu schicken**  
---

Category: Implicitly denied  
---

Ich habe derzeit Schwierigkeiten, zu glauben, dass die Mehrheit der Palästinenser die Taten und das Weltbild der Hamas vollkommen ablehnt.  
I currently find it hard to believe that the majority of Palestinians completely reject Hamas’s actions and worldview.

Und Geld, das wirklich in Infrastruktur und Nahrungsmittel gesteckt wird, hilft ebenfalls dabei, ihre Macht zu erhalten \- weil der Alltag für Gazas Bevölkerung unter ihrer Herrschaft weiter funktioniert.  
And money that is actually invested in infrastructure and food also helps to maintain their power—because daily life for Gaza’s population continues to function under their rule.

**BILD Bund, 14.10.2023**  
**SCHLUSS DAMIT\!**  
---

Category: Implicitly denied  
---

Die Islamisten opfern die eigene Bevölkerung mit voller Absicht: Um die Weltöffentlichkeit auf ihre Seite zu ziehen, wollen sie möglichst viele Bilder von toten oder trauernden Menschen produzieren.  
The Islamists deliberately sacrifice their own people: in order to win over the global public, they want to produce as many images as possible of dead or grieving people.

**BILD, 18.10.2023**  
**Top-Experte erklärt; Das wahre Ziel der Hamas-Terroristen**  
---

Category: Implicitly denied  
---

\[Hamas\] betrieb Krankenhäuser, Schulen und Kindergärten, um unter den Palästinensern an Einfluss zu gewinnen.  
\[Hamas\] ran hospitals, schools, and kindergartens to gain influence among the Palestinians.

Sie genießt eine breite Unterstützung der Bevölkerung, ist keine isolierte Terror-Zelle.  
It enjoys broad support among the population; it is not an isolated terrorist cell.

Bitter: Offenbar scheinen viele Menschen in Gaza nicht zu sehen, wie groß das Leid ist, das die Hamas über sie bringt.  
Bitter: Apparently, many people in Gaza do not seem to realize the extent of the suffering that Hamas is inflicting on them.

**BILD, 13.10.2023**  
**Terroristen wollen Bevölkerung opfern; Hamas lässt Zivilisten nicht fliehen**  
---

Category: partially or explicitly denied  
---

Zudem werden auch zivile Opfer vermeldet, die in Wahrheit Hamas-Kämpfer sind.  
In addition, there are reports of civilian casualties who are, in fact, Hamas fighters.

Dabei rekrutieren mehrere Terrororganisationen im Gazastreifen minderjährige Palästinenser und setzen sie als Kämpfer ein.  
Several terrorist organizations in the Gaza Strip recruit Palestinian minors and deploy them as fighters.

**BILD, 13.07.2024**  
**Führung im Visier; Schwerer Schlag gegen Hamas-Hochburg in Gaza**  
---

Category: partially or explicitly denied  
---

Die Angaben können nicht unabhängig überprüft werden und die Hamas-Behörde unterscheidet nicht zwischen Zivilisten und Terroristen.  
The figures cannot be independently verified, and the Hamas authorities do not distinguish between civilians and terrorists.

In der Vergangenheit hat die Hamas wiederholt Opferzahlen überhöht.  
In the past, Hamas has repeatedly exaggerated its casualty figures.

**BILD, 03.10.2024**  
**Lafontaine pöbelt Strack-Zimmermann an;  Wer das glaubt, setzt die Welt in Brand**  
---

Category: partially or explicitly denied  
---

Sie wissen ganz genau, dass die Hamas gezielt ihre Kommandozentralen dort aufbaut, wo Kindergärten und Hospitäler sind.  
They know full well that Hamas deliberately sets up its command centers in areas where there are kindergartens and hospitals.

**BILD, 08.10.2024**  
**Neuer Bericht über Todesopfer in Gaza; Verschweigt die Hamas ein wichtiges Detail?**  
---

Category: partially or explicitly denied  
---

Neuer Bericht über Todesopfer in Gaza; Verschweigt die Hamas ein wichtiges Detail?  
New report on fatalities in Gaza; Is Hamas hiding a key detail?

Der palästinensischen Quelle zufolge habe die israelische Luftwaffe die Terroristen oft in ihrem Zuhause ausgeschaltet, wo sie sich zum Zeitpunkt der Angriffe mit ihren Angehören aufhielten. So sei zu erklären, dass vier von fünf Todesopfern entweder Terroristen seien oder mit den Terroristen verwandt.  
According to the Palestinian source, the Israeli Air Force has often eliminated the terrorists in their homes, where they were staying with their relatives at the time of the attacks. This explains why four out of five fatalities are either terrorists or related to terrorists.

Dem Hamas-Ministerium zufolge starben im Krieg, der mit dem palästinensischen Überfall auf Israel am 7\. Oktober 2023 begann, mehr als 41.000 Menschen in Gaza. Israel kritisiert die Angaben, weil die Hamas bewusst nicht zwischen getöteten Terroristen und Zivilisten unterscheidet. Dadurch wolle sie den Eindruck erwecken, dass Israel fast ausschließlich Zivilisten töte.  
Offiziellen israelischen Angaben töteten die israelischen Streitkräfte im Gazastreifen zwischen 15.000 und 17.000 palästinensische Terroristen. Um zivile Opfer zu vermeiden, unternimmt Israels Armee nach eigenen Angaben große Anstrengungen. So ist etwa belegt, dass palästinensische Zivilisten immer wieder über Flugblätter oder Anrufe vor bevorstehenden Angriffen gewarnt werden.  
Hamas nutzt hohe Opferzahlen.  
According to the Hamas Ministry, more than 41,000 people died in Gaza during the war that began with the Palestinian attack on Israel on October 7, 2023\. Israel criticizes these figures because Hamas deliberately fails to distinguish between killed terrorists and civilians. By doing so, it seeks to create the impression that Israel is killing almost exclusively civilians.  
According to official Israeli figures, the Israeli military killed between 15,000 and 17,000 Palestinian terrorists in the Gaza Strip. Israel’s army claims it makes great efforts to avoid civilian casualties. For example, there is evidence that Palestinian civilians are repeatedly warned of impending attacks via leaflets or phone calls.  
Hamas exploits high casualty figures.

**SPIEGEL ONLINE, 26.11.2023**  
**Israel entlässt 39 Palästinenser aus Gefängnis   Freilassung weiterer Gaza-Geiseln erwartet**  
---

Category: partially or explicitly denied  
---

Palästinensischen Medien zufolge handelt es sich bei den Freigelassenen um sechs Frauen sowie 33 männliche Jugendliche unter 19 Jahren.  
According to Palestinian media, those released include six women and 33 male youths under the age of 19\.  
Diese seien wegen terroristischer Straftaten verurteilt oder angekl，“ worden, erklärte in der Nacht der israelische Armeesprecher Doron Spielman. »Es ist eine Schande, dass wir sie freilassen«, sagte er. Dass sich die Freigelassenen unter den Fahnen der Hamas feiern ließen, zeige, um was für Menschen es sich handele.  
“They were convicted or charged with terrorist offenses,” Israeli Army Spokesperson Doron Spielman stated overnight. “It is a shame that we are releasing them,” he said. The fact that those released celebrated under Hamas flags shows what kind of people they are.

**SPIEGEL Plus, 22.12.2023**  
**»Ich glaube nicht, dass wir noch über Frieden sprechen können«**  
---

Category: partially or explicitly denied  
---

Aber er hätte nicht gedacht, sagt er, dass die palästinensischen Zivilisten, sozusagen seine Nachbarn, mitmachten.  
Nach den Hamas-Kämpfern mit ihren weißen Pick-ups kam ein Mob von palästinensischen Zivilisten über die Grenze, so zeigen es Videos. Man sieht auch Männer in Badeschlappen, die nicht wirken, als hätten sie sich für einen Angriff vorbereitet. Einige von ihnen sollen mitgemordet und gebrandschatzt haben. Auszumachen, wer Kämpfer ist und wer Mitläufer, ist unmöglich.  
But he says he never would have thought that Palestinian civilians—his neighbors, so to speak—would go along with it.  
Videos show that after the Hamas fighters in their white pickup trucks, a mob of Palestinian civilians crossed the border. You can also see men in flip-flops who don’t look as though they’ve prepared for an attack. Some of them are said to have participated in the killings and looting. It’s impossible to tell who is a fighter and who is a follower.

**SPIEGEL Plus, 17.04.2024**  
**Antisemitismus aus Ahnungslosigkeit**  
---

Category: partially or explicitly denied  
---

Man könnte fragen, warum selbst seriöse Medien von den gegenwärtig nach Hamas-Angaben rund 33.000 Toten Palästinenser:innen sprechen   aber fast nie dazusagen, wie viele darunter Kämpfer der Hamas sind, sodass Ahnungslose geradezu zwangsläufig den Eindruck haben müssen, es handele sich um zivile Opfer?  
One might ask why even reputable media outlets report the current death toll of Palestinians—which, according to Hamas, stands at around 33,000—but almost never specify how many of them are Hamas fighters, so that the uninformed are bound to get the impression that these are civilian casualties?

**BILD, 26.11.2023**  
**So feiern Israelis die Freiheit \- und so die Palästinenser; Diese zwei Fotos sagen alles über den Krieg**  
---

Category: partially or explicitly denied  
---

Unter den freigelassenen palästinensischen Häftlingen befinden sich auch Minderjährige. Viele arabische, aber auch einige westliche Medien bezeichneten sie als 'Kinder'. Dabei saßen viele von ihnen wegen Gewalttaten und Terror-Unterstützung im Gefängnis.  
Among the released Palestinian prisoners are also minors. Many Arab, and even some Western, media outlets referred to them as ‘children’. Yet many of them were imprisoned for acts of violence and supporting terrorism.

**WELT ONLINE, 04.02.2024**  
**Frauen in Gaza; Kinderkriegen für den Kampf gegen die Juden**  
---

Category: partially or explicitly denied  
---

Frauen in Gaza; Kinderkriegen für den Kampf gegen die Juden  
Women in Gaza; raising children for the fight against the Jews. 

Seit 17 Jahren ruft die Hamas die dortigen Frauen dazu auf, mehr Kinder zu bekommen \- damit ihnen der Nachschub für die Terrortruppen nie ausgeht.  
For 17 years, Hamas has been urging local women to have more children—so that the supply of recruits for its terrorist forces never runs dry.

Auf diese Weise fallen das Interesse der Hamas an Terrornachwuchs, das Interesse männlich-chauvinistischer Palästinenser und das Interesse der UNRWA an der Erhaltung einer abhängigen Klientel zusammen.  
In this way, Hamas’s interest in recruiting new terrorists, the interests of male-chauvinist Palestinians, and UNRWA’s interest in maintaining a dependent clientele all converge.

**WELT ONLINE, 30.12.2023**  
**Befreite Hamas-Geisel; "Ich habe die Hölle erlebt. Es gibt keine unschuldigen Zivilisten in Gaza"**  
---

Category: partially or explicitly denied  
---

“Es gibt keine unschuldigen Zivilisten in Gaza”  
“There are no innocent civilians in Gaza”

“Es gibt dort keine unschuldigen Bürger. Es sind Familien, die von der Hamas kontrolliert werden.”  
“There are no innocent civilians there. These are families controlled by Hamas.”

*Note: These are quotes from an interviewee and therefore not written by the journal itself. However, the fact that the journal has chosen them as the title of the article and has adopted them as the general frame of the article has triggered this classification in the model.* 

# Appendix D

## Evidence snippets of articles flagged with dehumanization forms

**SPIEGEL ONLINE, 26.10.2023**  
**Wer ruft die Hamas zur Mäßigung auf?**  
---

Category: justification or normalization of harm  
---

Und doch muss man sich daran erinnern, dass die Menschen in Gaza diese verzweifelte Lage den Todesschwadronen der Hamas verdanken.  
And yet, it must be remembered that the people of Gaza owe this desperate situation to the Hamas death squads.

Dass sie 200 Geiseln in ihrer Gewalt behalten, auch wenn das eine israelische Bodenoffensive und damit Not, Elend und Massensterben der eigenen Leute bedeutet  
That they are holding 200 hostages, even if it means an Israeli ground offensive and thus hardship, misery, and mass death among their own people.

**WELT ONLINE, 13.11.2023**  
**Krieg in Nahost; Israel findet Hinweise auf Geisel-Verstecke in Kinderklinik in Gaza**  
---

Category: justification or normalization of harm  
---

Die neue israelische Enthüllung stärkt die Rechtsposition der Israelis, was eventuelle zukünftige Angriffe auf von der Hamas genutzte Krankenhäuser wie Al-Schifa anbelangt. Krankenhäuser genießen laut internationalem Recht im Kriegsfall eines besonderen Schutzstatus. Der geht jedoch verloren, wenn eine Kriegspartei ein Krankenhaus für militärische Zwecke nutzt.  
The new Israeli revelations strengthen Israel's legal position regarding potential future attacks on hospitals used by Hamas, such as Al-Shifa. According to international law, hospitals enjoy special protection in times of war. This protection is lost, however, if a belligerent party uses a hospital for military purposes.

**WELT ONLINE, 18.01.2024**  
**Gaza-Streifen; Wenn ein Lehrer der UN den Hamas-Terror preist**  
---

Category: justification or normalization of harm  
---

So hat die UNRWA die Terrororganisation nie klar dafür verurteilt, dass sie palästinensische Zivilisten als menschliche Schutzschilde nimmt oder kritisiert, dass Hamas Schulen der UNRWA nachweislich als Waffenlager, Waffenproduktionsstätten und Abschussrampen für Raketenwerfer missbraucht hat, darunter auch Schulen, die direkt von Deutschland mitfinanziert werden.  
UNRWA has never clearly condemned the terrorist organization for using Palestinian civilians as human shields, nor has it criticized Hamas for demonstrably misusing UNRWA schools as weapons depots, weapons production facilities, and launching sites for rocket launchers—including schools directly co-financed by Germany.

Zum Teil beginnt die Militarisierung der Palästinenser schon im Kindergarten.  
In some cases, the militarization of the Palestinians begins as early as kindergarten.

**BILD, 05.02.2025**  
**Gastkommentar aus Israel; Dieses Foto zeigt, warum Trumps Plan richtig ist**  
---

Category: justification or normalization of harm  
---

Dass natürlich nicht alle, aber die Mehrheit der sogenannten unbeteiligten Zivilisten in Gaza das Terrorregime unterstützen, das Zerstörung über sie gebracht hat.  
That, of course, not all, but the majority of so-called uninvolved civilians in Gaza support the terror regime that has brought destruction upon them.

**BILD, 30.10.2023**  
**Bodenoffensive kommt schnell voran; Israel will Gaza-Stadt einkesseln\!**  
---

Category: justification or normalization of harm  
---

Ein israelischer Sicherheitsexperte, der anonym bleiben will, erklärte gegenüber BILD, in dem Fahrzeug hätten sich sowohl Zivilisten als auch Hamas-Späher oder gar bewaffnete Kämpfer befinden können.Es sei daher aus Sicht der Soldaten, "schwierig, aber vielleicht auch notwendig" gewesen, das Feuer auf das Fahrzeug zu eröffnen.  
An Israeli security expert, who wished to remain anonymous, told BILD that the vehicle could have contained civilians, Hamas spies, or even armed fighters. Therefore, from the soldiers' perspective, opening fire on the vehicle was "difficult, but perhaps also necessary."

Doch der Experte sagt auch: "Die Szene zeigt, wie schmutzig der urbane Kampf in Gaza werden kann." Denn: Israels Armee stehe nun vor der Entscheidung, bei jedem Kontakt mit Palästinensern die eigene Sicherheit gegen die mutmaßlicher Zivilisten \- oder eben doch bewaffneter Terroristen \- abzuwägen. Und dies jeweils binnen Sekunden.  
But the expert also says: "This scene shows how dirty urban warfare in Gaza can become." Because: Israel's army now faces the decision of weighing its own safety against that of suspected civilians—or even armed terrorists—in every encounter with Palestinians. And this must be done within seconds.

**WELT ONLINE,  01.08.2025**  
**Nahost; Wenn wir Israel verraten, verraten wir uns selbst**  
---

Category: justification or normalization of harm  
---

Die ,,Washington Post" druckte eine Liste mit den Namen von 18.500 Kindern, die angeblich in Gaza getötet wurden. Die Liste stammte von einer Hamas-geführten Institution, die Namen oder die vermeintlichen Todesumstände ließen sich nicht verifizieren. Fakt ist aber: Die Hamas setzt ihre eigenen Kinder als Schutzschilde ein, um Bilder für ihre Propaganda zu produzieren.  
The Washington Post published a list of 18,500 children allegedly killed in Gaza. The list came from a Hamas-run institution, and the names and the alleged circumstances of their deaths could not be verified. However, it is a fact that Hamas uses its own children as human shields to produce images for its propaganda.

Denn noch ist die Hamas de facto Palästina \[...\].  
Because Hamas is still de facto Palestine \[...\].

**BILD Bund, 13.10.2025**  
**Die Palästinenser müssen sich vom Terror befreien**  
---

Category:  collective threat framing  
---

Es gibt keinen innerpalästinensischen Diskurs, der Gewalt ernsthaft infrage stellt.  
There is no internal Palestinian discourse that seriously questions violence.

**WELT ONLINE, 03.02.2025**  
**Hilfswerk UNRWA; Die Lebenslüge der Palästinenser**  
---

Category:  collective threat framing,  justification or normalization of harm  
---

Das UNRWA soll den Flüchtlingsstatus der Palästinenser verewigen, auf dass sie und ihre Kinder und Kindeskinder als propagandistische Waffe, Kanonenfutter und Schutzschilde im Vernichtungskrieg gegen Israel eingesetzt werden können.  
UNRWA is intended to perpetuate the refugee status of the Palestinians, so that they, their children, and their grandchildren can be used as propaganda weapons, cannon fodder, and human shields in the war of annihilation against Israel.

**WELT ONLINE, 22.08.2024**  
**Warum die USA keine palästinensischen Flüchtlinge aufnehmen sollten**  
---

Category:  collective threat framing,  justification or normalization of harm  
---

Ein Grund dafür ist, dass keine noch so gute Überprüfung die jahrelange Indoktrination und Radikalisierung rückgängig machen kann.  
One reason for this is that no matter how thorough the vetting process, it cannot undo years of indoctrination and radicalization.

Die beunruhigenden Statistiken und das dokumentierte Eintauchen der Palästinenser in eine Kultur des Hasses legen nahe, dass nur wenige bis gar keine derjenigen, die sich einer Überprüfung unterziehen, für eine Aufnahme infrage kommen sollten.  
The alarming statistics and the documented immersion of Palestinians in a culture of hatred suggest that few, if any, of those undergoing vetting should be eligible for admission.

**SZ, 10.10.2023**  
**Der Hass, der nicht vergeht**  
---

Category: erasure of individuality, collective threat framing,  justification or normalization of harm  
---

Die Feindschaft zu Israel ist für die Palästinenser wie ein Lebenselixier.  
Hostility toward Israel is, for Palestinians, like an elixir of life.

Nur wird das nichts daran ändern, dass der Konflikt für die Palästinenser ihr Leben ist.  
But that will not change the fact that, for Palestinians, the conflict is their life.

\[Hamas\] hat ihren Fanatismus unters palästinensische Volk gebracht, das Gift, dass Gewalt okay ist.  
\[Hamas\] has brought its fanaticism into the Palestinian people—the poison that violence is acceptable.

**BILD am Sonntag, 08.10.2024**  
Kein deutsches Geld mehr für diese Barbaren\!; Kommentar von BILD-Chefin Marion Horn  
---

Category: animalistic or objectifying language, collective threat framing,  justification or normalization of harm  
---

Kein deutsches Geld mehr für diese Barbaren\!  
No more German money to these barbarians\!

Steinzeit, Gesetz des Dschungels.  
Stone age, law of the jungle. 

Die deutsche Regierung finanziert mit deutschem Steuergeld ein palästinensisches Regime, das Judenhass predigt und den Holocaust relativiert.  
The german government finances with german taxes a palestinian regime, that predicates jew hate and relativizes the Holocaust. 

# APPENDIX C: WEFE Word Sets and Experiment Definitions

This appendix documents all word sets and experiments used in the Word Embedding Fairness Evaluation (WEFE) analysis. All experiments were run on word embeddings trained on the *Süddeutsche Zeitung* sub-corpus (N = 2,522 articles, October 2023 – December 2024). Word sets are defined in German, matching the language of the corpus.

## C.1 Word Sets

### Target Groups

| Set Name | Terms |
|---|---|
| *palestinians* | palästinenser, palästinensern, palästinensische, palästinensischen, gaza, gazastreifen, gazaner |
| *israelis* | israel, israelis, israelische, israelischen, israelischer, israelischem |
| *civilians* | zivilisten, bevölkerung, familien, anwohner, kinder, menschen |
| *palestinian\_journalists* | palästinensische, palästinensischen, journalist, journalisten, reporter, korrespondent, presse, kameramann, kameraleute |
| *general\_journalists* | journalist, journalisten, reporter, korrespondent, redaktion, presse, medien, auslandspresse |
| *foreign\_journalists* | ausländische, ausländischen, internationale, internationalen, auslandspresse, reporter, presse, korrespondenten |
| *media\_institutions* | redaktion, sender, fernsehsender, agentur, nachrichtenbüro, pressebüro, medienhaus, studio |
| *media\_infrastructure* | studio, kamera, sender, sendemast, internet, telefonnetz, funknetz, übertragung |

### Attribute Sets

| Set Name | Terms |
|---|---|
| *targeting\_violence\_terms* | töten, erschießen, bombardieren, angreifen, beschuss, verletzen, verwunden, verstümmeln, mord, ermordet, massaker, kaltblütig, vergeltungsschlag |
| *detention\_disappearance\_terms* | festnehmen, verhaften, verschleppen, haft, gefangenschaft, willkür, festnahme, festgenommen, verhaftet, verschleppt, gefangen |
| *harassment\_intimidation\_terms* | bedrohen, einschüchtern, terrorisieren, überwachen, verfolgen, drohen, drohungen, bedroht, verfolgt, drohende, einschüchterung |
| *infrastructure\_destruction\_terms* | zerstören, sprengen, verwüsten, durchsuchen, plündern, bombardieren, razzia, beschlagnahmen |
| *telecom\_disruption\_terms* | abschalten, blockieren, unterbrechen, drosseln, kappen, stören, sperren, abschneiden |
| *terrorist\_labelling\_terms* | terrorist, terroristen, propagandist, militant, extremist, mörder, islamist, barbarisch, extrem, gewalttätig, radikal, bruderschaft, miliz, jihad, islamismus, salafist, dschihadist |
| *family\_targeting\_terms* | angehörige, familie, familienmitglieder, bedrohen, töten, einschüchtern, bestrafen, vergelten |
| *exclusion\_blackout\_terms* | einreiseverbot, abschottung, ausschluss, sperren, gesperrt, verboten, abweisen, verweigern, ausweisen, blockieren, abgeschnitten |
| *dehumanizing\_terms* | barbaren, parasiten, ungeziefer, monster, menschenmaterial, welle, flut, plage, barbarisch, gräuel, gräueltat, grauenhaft, horror |
| *dehumanizing\_aggressive\_terms* | barbarisch, barbarei, bestialisch, unmenschlich, bestie, bestien, fanatisch, blutrünstig, gräueltat, gräueltaten, schrecken, horror, grauenhaft, abscheulich, verabscheuungswürdig, brutal, brutalität, barbar, barbaren, unmensch, tierisch, mordlust, monströs, gräuel |
| *collectivizing\_terms* | feind, feindvolk, masse, welle, flut, kollektivschuld, gesamtheit, block |
| *erasure\_civilian\_status\_terms* | schutzschild, mitschuldig, kämpfer, kämpfern, milizionäre, terroristen, hamas-strukturen |
| *criminalizing\_terms* | illegal, kriminalität, kriminell, bande, bedrohung, verdächtig, terrorverdacht, sicherheitsrisiko, terrorist, mörder, islamist, miliz, palästinensermiliz, radikal, extremist, fundamentalist, radikalislamist, gewalttätig, suspekt |
| *mass\_displacement\_terms* | vertreiben, verdrängen, räumen, entvölkern, vertreibung, vertriebene, umsiedlung, zwangsumsiedlung, flucht, flüchtlinge |
| *destruction\_gaza\_terms* | vernichten, auslöschen, einebnen, zerstören, demolieren, ausradieren, zerstörung, verwüstung, dem erdboden gleichmachen |
| *genocide\_incitement\_terms* | ausrotten, vernichten, auslöschen, eliminieren, tilgen, restlos, endlösung, vertreiben |
| *coded\_incitement\_terms* | säubern, ausmisten, durchgreifen, befrieden, räumen, abschrecken, ordnung, härte |
| *editorial\_line\_terms* | vorgaben, kampagne, kampagnen, abgestimmt, propaganda, narrativ, linie, kommentar |
| *disinformation\_terms* | desinformation, propaganda, verleumdung, delegitimierung, diskreditierung, lüge, manipulation, angeblich, mutmaßlich, behauptung, behaupten, lügen, agent, kollaborateur, sympathisant, gestellt, inszeniert, arrangiert |
| *censorship\_retaliation\_terms* | zensur, verbot, verbote, entlassung, sanktion, strafen, einschüchterung, abschalten, einschränkung, beschlagnahmt |
| *press\_freedom\_terms* | pressefreiheit, schutz, unabhängigkeit, berichterstattung, journalismus, dokumentation, zeugen, öffentlichkeit, objektiv, neutral, professionell, akkurat, korrekt, genau |
| *editorial\_independence\_terms* | unabhängigkeit, sorgfalt, transparenz, ethik, korrektur, objektiv, neutral, professionell, akkurat, genau, wahrheit, quellenangabe, fakten |
| *journalist\_professionalism\_terms* | objektiv, neutral, professionell, unabhängig, unabhängigkeit, akkurat, korrekt, genau |
| *journalist\_discrediting\_terms* | propagandist, propaganda, agent, kollaborateur, sympathisant, gestellt, inszeniert, arrangiert, jihad, desinformation, verleumdung |
| *conviction\_accusation\_terms* | schuldig, verdacht, verdächtig, beschuldigt, angeklagt, anklage, vorwurf, vorwürfe, verurteilt, verurteilung, haftbefehl, inhaftiert, festgenommen, verhaftet, verhört, geständnis, terrorverdacht, komplize, komplizenschaft, mitschuld, mitschuldig, tatvorwurf, ermittlungen, beschuldigung, eingeweiht, informiert |
| *innocence\_protection\_terms* | unschuldig, freigesprochen, entlastet, rehabilitiert, zeuge, berichterstatter, professionell, unabhängig, objektiv, quellenarbeit, recherche, sorgfalt, wahrheit, korrekt, transparent, rechtschutz, opferstatus, schutzwürdig, journalistische |
| *hamas\_organization\_terms* | hamas, dschihadist, islamist, islamismus, jihad, milizionär, terrororganisation, terrorgruppe, extremist, fundamentalist, dschihadismus, salafist, islamischer, hamas-führer, bewaffnet, kombattant, kriegspartei, waffenarm, hamas-kämpfer |
| *civilian\_protection\_terms* | zivilisten, schutz, völkerrecht, humanitär, menschenrechte, rettung, versorgung, sicherheit, opfer, verteidigung, abwehr, humanitäre, zivile |
| *legal\_accountability\_terms* | völkerrecht, ermittlung, beweise, verantwortung, haftung, rechtsbruch, kriegsverbrechen, anordnung |
| *humanizing\_terms* | familie, arbeiter, gemeinschaft, nachbar, mensch, menschen, zivilisten, bewohner, unbewaffnet, opfer, unschuldig, flüchtling, zuflucht, zufluchtsort, trauma, traumatisiert |
| *humanizing\_child\_civilian\_terms* | kind, kinder, kleinkind, baby, mädchen, junge, jugendlicher, jugendliche, minderjähriger, minderjährige, schüler, schülerin, teenager, heranwachsend, schutzlos, hilflos, eltern, unschuldige, zivilist, zivilisten, neugeborene, säugling |
| *violence\_positive\_terms* | selbstverteidigung, unbewaffnet, reaktion, gegenangriff, opfer, abwehr, zivilisten, verteidigungsstreitkräfte, sicherheitskräfte, verteidigung |
| *violence\_negative\_terms* | terrorist, mörder, islamist, barbarisch, extrem, extremist, gewalttätig, vergeltungsschlag, zivile ziele, kaltblütig, sprachrohr der hamas & des terrorismus, militant |
| *language\_of\_death\_direct\_terms* | mord, ermordet, massaker |
| *language\_of\_death\_euphemistic\_terms* | tod, gestorben, tot, leben verloren, umkommen, sterben |
| *passive\_death\_terms* | gestorben, starben, starb, todesfälle, verstorben, umgekommen, sterben, sterbend, gefallen, ableben, tot, todesfall, ums leben |
| *active\_murder\_terms* | ermordet, erschossen, erschlagen, abgeschlachtet, hingerichtet, massakriert, umgebracht, mord, massaker, kaltblütig, mordete, blutbad, hingemetzelt, mordanschlag, exekutiert, liquidiert |
| *sympathetic\_victim\_terms* | trauern, trauer, trauerfeier, beileid, vermisst, entführt, geisel, geiseln, überlebende, überlebt, gedenken, gedenkfeier, held, schicksal, einzelschicksal, mutter, vater, tochter, sohn, erinnerung, persönlich, herzensbrecher, angehörige, familienangehörige |
| *statistical\_aggregate\_terms* | todesfälle, opferzahl, gesamtzahl, bilanz, schätzungen, hochrechnung, daten, zahlen, statistik, insgesamt, prozent, laut, angaben, anzahl, zähler, berichten, zahl |
| *hostage\_sympathy\_terms* | geisel, geiseln, geiselnahme, entführt, entführte, verschleppt, verschleppte, freilassung, befreit, freigelassen, verschleppung, geiselhaft, geiselkrise, lebenszeichen |
| *prisoner\_detention\_neutral\_terms* | häftling, häftlinge, gefangene, gefangener, gefangenschaft, inhaftiert, inhaftierte, verhaftete, inhaftierung, haftstrafe, gefängnis, verwaltungshaft |
| *credibility\_positive\_terms* | wahrheit, staat |
| *credibility\_negative\_terms* | angeblich, mutmaßlich, behauptung, behaupten, lüge, lügen |
| *self\_defense\_terms* | selbstverteidigung, verteidigungsrecht, verteidigungsmaßnahme, notwehr, abwehrkampf, gegenwehr, sicherheitsoperation, legitim, rechtmäßig, verhältnismäßig |
| *terror\_attack\_terms* | terrorangriff, terrorakt, überfall, blutbad, massenmord, attentat, terroroffensive, eindringen, terrorwelle, terroristisch, anschlag, mordanschlag |

## C.2 Experiment Definitions

Each WEAT experiment compares two target groups against two attribute sets. Each WEFAT experiment measures the absolute association of a single target group against two attribute sets. Descriptions are translated from the original German configuration.

| Experiment | Metric | Target 1 | Target 2 | Attribute 1 | Attribute 2 | Description |
|---|---|---|---|---|---|---|
| death\_language\_agency\_asymmetry | WEAT | palestinians | israelis | passive\_death\_terms | active\_murder\_terms | Tests whether Palestinian deaths are described in passive/agentless language while Israeli deaths are described with active murder vocabulary |
| institutional\_editorial\_line | WEAT | palestinians | civilians | editorial\_line\_terms | editorial\_independence\_terms | Tests whether Palestinian-related vocabulary is embedded in an editorial-directive register rather than an editorially independent one |
| palestinian\_civilian\_erasure | WEAT | palestinians | civilians | erasure\_civilian\_status\_terms | humanizing\_terms | Tests whether Palestinian references are closer to civilian-status erasure vocabulary than to humanizing vocabulary, relative to the neutral baseline *civilians* |
| palestinian\_dehumanization | WEAT | palestinians | civilians | dehumanizing\_terms | humanizing\_terms | Tests whether Palestinian references are more strongly associated with dehumanizing vocabulary than with humanizing vocabulary |
| journalist\_hamas\_association | WEAT | palestinian\_journalists | general\_journalists | hamas\_organization\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are embedded closer to Hamas/militant-organization vocabulary than to press-freedom vocabulary |
| hostage\_prisoner\_framing | WEAT | israelis | palestinians | hostage\_sympathy\_terms | prisoner\_detention\_neutral\_terms | Tests whether Israeli captives are described with sympathy-laden hostage vocabulary while Palestinian detainees are described with neutral detention terms |
| israel\_palestine\_violence\_framing | WEAT | palestinians | israelis | violence\_negative\_terms | violence\_positive\_terms | Tests asymmetric framing of violence: whether Palestinian actions are embedded near negative violence terms while Israeli actions appear near protective/defensive vocabulary |
| journalist\_targeting\_violence | WEAT | palestinian\_journalists | general\_journalists | targeting\_violence\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with physical targeting and violence vocabulary than with press-freedom vocabulary |
| journalist\_detention\_disappearance | WEAT | palestinian\_journalists | general\_journalists | detention\_disappearance\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with detention and disappearance vocabulary |
| journalist\_harassment\_intimidation | WEAT | palestinian\_journalists | general\_journalists | harassment\_intimidation\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with harassment and intimidation vocabulary |
| foreign\_press\_exclusion\_blackout | WEAT | foreign\_journalists | general\_journalists | exclusion\_blackout\_terms | press\_freedom\_terms | Tests whether foreign journalists are associated with access-denial vocabulary relative to general journalists |
| israel\_palestine\_death\_language | WEAT | palestinians | israelis | language\_of\_death\_euphemistic\_terms | language\_of\_death\_direct\_terms | Tests whether Palestinian deaths are described euphemistically (*gestorben*, *leben verloren*) while Israeli deaths are described with direct murder vocabulary |
| journalist\_family\_targeting | WEAT | palestinian\_journalists | general\_journalists | family\_targeting\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with vocabulary relating to family members being threatened or targeted |
| journalist\_terror\_labelling | WEAT | palestinian\_journalists | general\_journalists | terrorist\_labelling\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with terrorist labelling vocabulary |
| coded\_incitement | WEAT | palestinians | civilians | coded\_incitement\_terms | civilian\_protection\_terms | Tests whether Palestinian references appear closer to coded escalation vocabulary (e.g., *säubern*, *räumen*) than to civilian protection vocabulary |
| censorship\_retaliation | WEAT | palestinian\_journalists | general\_journalists | censorship\_retaliation\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more associated with censorship and retaliation vocabulary |
| legal\_accountability\_obscuring | WEAT | palestinians | civilians | legal\_accountability\_terms | disinformation\_terms | Tests the relative association of Palestinian references with legal accountability versus disinformation vocabulary |
| journalist\_disinformation | WEAT | palestinian\_journalists | general\_journalists | disinformation\_terms | editorial\_independence\_terms | Tests whether Palestinian journalists are more associated with disinformation and discrediting vocabulary than with editorial independence vocabulary |
| mass\_displacement\_incitement | WEAT | palestinians | civilians | mass\_displacement\_terms | civilian\_protection\_terms | Tests whether Palestinian references are closer to forced displacement vocabulary than to civilian protection vocabulary |
| victim\_humanization\_sympathy\_asymmetry | WEAT | israelis | palestinians | sympathetic\_victim\_terms | statistical\_aggregate\_terms | Tests whether Israeli victims are personalized with sympathy vocabulary while Palestinian deaths are rendered as statistical aggregates |
| journalist\_professionalism\_contestation | WEAT | palestinian\_journalists | general\_journalists | journalist\_discrediting\_terms | journalist\_professionalism\_terms | Tests whether Palestinian journalists are associated with discrediting vocabulary over professional journalistic vocabulary |
| genocide\_incitement | WEAT | palestinians | civilians | genocide\_incitement\_terms | civilian\_protection\_terms | Tests whether Palestinian references are closer to direct extermination vocabulary than to civilian protection vocabulary |
| gaza\_destruction\_incitement | WEAT | palestinians | civilians | destruction\_gaza\_terms | civilian\_protection\_terms | Tests whether Palestinian references are closer to destruction and annihilation vocabulary than to civilian protection vocabulary |
| journalist\_access\_exclusion\_parity | WEAT | palestinian\_journalists | foreign\_journalists | exclusion\_blackout\_terms | press\_freedom\_terms | Tests whether Palestinian journalists are more strongly associated with access-denial vocabulary than foreign journalists |
| journalist\_conviction\_association | WEAT | palestinian\_journalists | general\_journalists | conviction\_accusation\_terms | innocence\_protection\_terms | Tests whether Palestinian journalists are embedded in a guilt-and-accusation framing rather than an innocence-and-professionalism framing |
| civilian\_dehumanization\_asymmetry | WEAT | palestinians | israelis | dehumanizing\_aggressive\_terms | humanizing\_child\_civilian\_terms | Tests whether Palestinian references are more strongly associated with aggressive dehumanizing terms relative to humanizing child/civilian vocabulary |
| israel\_palestine\_credibility\_framing | WEAT | palestinians | israelis | credibility\_negative\_terms | credibility\_positive\_terms | Tests asymmetries in source credibility framing between Palestinian and Israeli references |
| journalist\_dehumanization\_asymmetry | WEAT | palestinian\_journalists | general\_journalists | dehumanizing\_aggressive\_terms | humanizing\_child\_civilian\_terms | Tests whether Palestinian journalists appear in a dehumanizing context relative to general journalists |
| media\_infrastructure\_disruption | WEAT | media\_institutions | media\_infrastructure | infrastructure\_destruction\_terms | telecom\_disruption\_terms | Tests the association of media institutions versus physical media infrastructure with destruction vocabulary |
| self\_defense\_vs\_terror\_framing | WEAT | israelis | palestinians | self\_defense\_terms | terror\_attack\_terms | Tests whether Israeli actions are framed as self-defense while Palestinian actions are framed as terror attacks |
| wefat\_mass\_displacement\_absolute | WEFAT | palestinians | — | mass\_displacement\_terms | civilian\_protection\_terms | Absolute association of Palestinian vocabulary with forced displacement versus civilian protection vocabulary (no comparison group) |
| wefat\_genocide\_incitement\_absolute | WEFAT | palestinians | — | genocide\_incitement\_terms | civilian\_protection\_terms | Absolute association of Palestinian vocabulary with extermination vocabulary versus civilian protection vocabulary |
| wefat\_palestinians\_dehumanization\_absolute | WEFAT | palestinians | — | dehumanizing\_terms | humanizing\_terms | Absolute association of Palestinian vocabulary with dehumanizing versus humanizing vocabulary |
| wefat\_media\_institutions\_destruction\_absolute | WEFAT | media\_institutions | — | infrastructure\_destruction\_terms | press\_freedom\_terms | Absolute association of media institution vocabulary with destruction versus press-freedom vocabulary |
| wefat\_palestinian\_journalists\_violence\_absolute | WEFAT | palestinian\_journalists | — | targeting\_violence\_terms | press\_freedom\_terms | Absolute association of Palestinian journalist vocabulary with targeting/violence versus press-freedom vocabulary |
| wefat\_civilians\_erasure\_absolute | WEFAT | civilians | — | erasure\_civilian\_status\_terms | humanizing\_terms | Absolute association of civilian vocabulary with civilian-status erasure versus humanizing vocabulary |

[image1]: <data:image/png;base64,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HS90butUocDBg+rW1GYUOB90butY2rZtWzZu3Lj4s7d58+a49u///u/xdtUBp6vo3NbxQue2jhc6t3W80LmtU4UCBw+qW1ObUeB80Lmt0y69/fyFctdfOrd1vNC5reOFzm0dL3Ru61ShwMGDno9aQ6S3B9AcBS4dOrd12mHr1q3xsDe54447Lhs+fHhc7y+d2zpe6NzW8ULnto4XOrd1qlDg4EF1a2ozCpwPOrd12qG3n73w9OqECRN0uZLObR0vdG7reKFzW8cLnds6VShw8KDnI9cQ6e1BNEeBS4fObR1rO+20ky4VGv1MKp3bOkNly5YtutSQzm0dL3Ru63ihc1unCgUOHvT/EcpYowdLClw6dG7rWAplJPzc5Ql+9KMfxevlp1T7Q+e2jrXwpo7y7+STTz6ZPf7446V79I/ObR0vdG7reKFzW6cKBQ4eVLemNqPA+aBzW8cLnds67VD+nQzXly5dms2dO7d0j77p3NbxQue2jhc6t3WqUODgQXVrajMKnA86t3W80Lmt0w5a4FavXh2vN3OIFZ3bOl7o3NbxQue2ThUKHDyobk1tRoGzVX6aMHjjjTd6rPWHzm0dL3Ru67RD+Wdj2rRpva73Ree2Tjs99dRTutRvOrd1vNC5rVOFAgcP+v+X2FijBwUKXGvoHpXcihUriut90bmtM1C3//bBtkbnto61E044If6MhMvcqFGjstmzZ2fLli0r3bMxnds67RK+DkF4SnndunWytW86t3W80LmtU4UCBw+qW1ObUeDsVRW4WbNmFdf7onNbZ6D0e2odnds6Xujc1mmX8u/PpEmTSlv6R+e2jhc6t3WqUODgQXVrajMKnL2qAjdz5sziel90busMlH5PraNzW8cLnds67ZL//tx///0N/3ZV0bmt44XObZ0qFDh40PxfHiON/ghS4FqjqsDl5wHtD53bOgOl31Pr6NzW8ULntk475Wfq2GeffWRL33Ru63ihc1unCgUOHlS3pjajwNkKX9885bVwyqhm6NzWGSj9nlpH57aOFzq3ddrlsccei5c77LCDbOkfnds67RL+powePbrp4yjmdG7rVKHAwYPq1tRmFDgfdG7rDJR+T62jc1tnoHRu6+jc1mmnO++8U5f6Tee2Trt985vfbOpcwjmd2zpVKHDwoLo1tRkFzged2zoDpd9T6+jc1hkonds6Ord1vNC5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>