# PG1 foundation sūtra register

Author: Monty. 1 November 2026.

This register supplies reading notes for the foundations; it is not a closed
executable grammar. Sanskrit is copied from the pinned sūtrapāṭha; IAST is an
editorial transliteration of that exact spelling, retaining its word joining.
The brief English notes are our specification, not verbatim translations.
Source and commentary distinctions are defined in [SOURCES.md](SOURCES.md).

Every row has status **text checked; bounded reading note**. It does not claim
all exceptions, anuvṛtti paths or commentary debates have been discharged.
Existing finite implementations and their limits are mapped separately in
[COVERAGE_AND_GATES.md](COVERAGE_AND_GATES.md).

## Sound, duration and designation

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [1.1.1](https://ashtadhyayi.com/sutraani/1/1/1) | वृद्धिरादैच् — *vṛddhirādaic* | Defines vṛddhi; a designation, not an instruction to strengthen every vowel. |
| [1.1.2](https://ashtadhyayi.com/sutraani/1/1/2) | अदेङ् गुणः — *adeṅ guṇaḥ* | Defines guṇa; distinguish the class from a rule that licenses replacement. |
| [1.1.3](https://ashtadhyayi.com/sutraani/1/1/3) | इको गुणवृद्धी — *iko guṇavṛddhī* | Interprets guṇa/vṛddhi replacement with respect to ik; retain the governing context. |
| [1.1.8](https://ashtadhyayi.com/sutraani/1/1/8) | मुखनासिकावचनोऽनुनासिकः — *mukhanāsikāvacano'nunāsikaḥ* | Defines nasalization; preserve it in upadeśa and distinguish spoken nasal sounds from markers. |
| [1.1.9](https://ashtadhyayi.com/sutraani/1/1/9) | तुल्यास्यप्रयत्नं सवर्णम् — *tulyāsyaprayatnaṃ savarṇam* | Savarṇa depends on articulatory criteria, not matching Unicode characters. |
| [1.1.10](https://ashtadhyayi.com/sutraani/1/1/10) | नाज्झलौ — *nājjhalau* | Limits the savarṇa relation; a vowel/consonant shortcut cannot ignore this restriction. |
| [1.1.69](https://ashtadhyayi.com/sutraani/1/1/69) | अणुदित् सवर्णस्य चाप्रत्ययः — *aṇudit savarṇasya cāpratyayaḥ* | Extends designated non-affix sounds to savarṇas with specified conditions; aṇ endpoint matters. |
| [1.1.70](https://ashtadhyayi.com/sutraani/1/1/70) | तपरस्तत्कालस्य — *taparastatkālasya* | Tapara restricts duration; do not expand a short trigger to every long/pluta form indiscriminately. |
| [1.1.71](https://ashtadhyayi.com/sutraani/1/1/71) | आदिरन्त्येन सहेता — *ādirantyena sahetā* | Forms pratyāhāras with an initial and terminal it marker; preserve endpoint identity. |
| [1.2.27](https://ashtadhyayi.com/sutraani/1/2/27) | ऊकालोऽज्झ्रस्वदीर्घप्लुतः — *ūkālo'jjhrasvadīrghaplutaḥ* | Distinguishes short, long and pluta durations; pluta needs a separate feature. |
| [1.2.28](https://ashtadhyayi.com/sutraani/1/2/28) | अचश्च — *acaśca* | Carries vowel scope into the following accent designations. |
| [1.2.29](https://ashtadhyayi.com/sutraani/1/2/29) | उच्चैरुदात्तः — *uccairudāttaḥ* | Udatta designation; a phonetic/accent layer distinct from lexical spelling. |
| [1.2.30](https://ashtadhyayi.com/sutraani/1/2/30) | नीचैरनुदात्तः — *nīcairanudāttaḥ* | Anudātta designation; do not discard it before marker/pada interpretation. |
| [1.2.31](https://ashtadhyayi.com/sutraani/1/2/31) | समाहारः स्वरितः — *samāhāraḥ svaritaḥ* | Svarita designation; an accent class, not an operator time parameter. |
| [1.2.32](https://ashtadhyayi.com/sutraani/1/2/32) | तस्यादित उदात्तमर्धह्रस्वम् — *tasyādita udāttamardhahrasvam* | Further specifies svarita; a full accent account needs the surrounding rules. |
| [1.4.109](https://ashtadhyayi.com/sutraani/1/4/109) | परः सन्निकर्षः संहिता — *paraḥ sannikarṣaḥ saṃhitā* | Defines saṃhitā; adjacency alone is not a complete domain declaration. |
| [1.4.110](https://ashtadhyayi.com/sutraani/1/4/110) | विरामोऽवसानम् — *virāmo'vasānam* | Defines avasāna; pause must be explicit in a phonological derivation. |
| [8.4.68](https://ashtadhyayi.com/sutraani/8/4/68) | अ अ — *a a* | Final a instruction; preserve the distinction between teaching and pronunciation conventions. |

## Rule interpretation, replacement and lopa

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [1.1.44](https://ashtadhyayi.com/sutraani/1/1/44) | न वेति विभाषा — *na veti vibhāṣā* | Vibhāṣā terminology; optional alternatives must remain alternatives with their own conditions. |
| [1.1.46](https://ashtadhyayi.com/sutraani/1/1/46) | आद्यन्तौ टकितौ — *ādyantau ṭakitau* | Ṭ/k-marked augment placement; identity of an augment differs from substitution. |
| [1.1.47](https://ashtadhyayi.com/sutraani/1/1/47) | मिदचोऽन्त्यात्परः — *midaco'ntyātparaḥ* | Mit placement after the relevant final vowel; not merely append-to-word. |
| [1.1.48](https://ashtadhyayi.com/sutraani/1/1/48) | एच इग्घ्रस्वादेशे — *eca igghrasvādeśe* | Special interpretation of ec in a short-vowel substitution; not literal string truncation. |
| [1.1.49](https://ashtadhyayi.com/sutraani/1/1/49) | षष्ठी स्थानेयोगा — *ṣaṣṭhī sthāneyogā* | Genitive in a replacement relation identifies the sthānin after semantic interpretation. |
| [1.1.50](https://ashtadhyayi.com/sutraani/1/1/50) | स्थानेऽन्तरतमः — *sthāne'ntaratamaḥ* | Closest eligible replacement; specify the source-supported similarity relation for each case. |
| [1.1.51](https://ashtadhyayi.com/sutraani/1/1/51) | उरण् रपरः — *uraṇ raparaḥ* | R-following treatment of aṇ replacements of ṛ; the ḷ extension needs its traditional reading. |
| [1.1.52](https://ashtadhyayi.com/sutraani/1/1/52) | अलोऽन्त्यस्य — *alo'ntyasya* | Default final-sound replacement; preserve the relevant unit and competing scope rules. |
| [1.1.54](https://ashtadhyayi.com/sutraani/1/1/54) | आदेः परस्य — *ādeḥ parasya* | Initial-of-the-following-unit replacement; distinguish from a whole-word target. |
| [1.1.55](https://ashtadhyayi.com/sutraani/1/1/55) | अनेकाल्शित्सर्वस्य — *anekālśitsarvasya* | Multi-sound or ś-marked substitution scope; apply to the interpreted sthānin. |
| [1.1.56](https://ashtadhyayi.com/sutraani/1/1/56) | स्थानिवदादेशोऽनल्विधौ — *sthānivadādeśo'nalvidhau* | Restricted sthānivad inheritance; the an-al-vidhi boundary is mandatory. |
| [1.1.60](https://ashtadhyayi.com/sutraani/1/1/60) | अदर्शनं लोपः — *adarśanaṃ lopaḥ* | Lopa is nonappearance; it does not assert that provenance has ceased to exist. |
| [1.1.61](https://ashtadhyayi.com/sutraani/1/1/61) | प्रत्ययस्य लुक्श्लुलुपः — *pratyayasya lukślulupaḥ* | Names luk/ślu/lup for affix disappearance; retain which operation occurred. |
| [1.1.62](https://ashtadhyayi.com/sutraani/1/1/62) | प्रत्ययलोपे प्रत्ययलक्षणम् — *pratyayalope pratyayalakṣaṇam* | Retains licensed affix-conditioned effects after entire-affix lopa; not a generic it-marker law. |
| [1.1.63](https://ashtadhyayi.com/sutraani/1/1/63) | न लुमताङ्गस्य — *na lumatāṅgasya* | Restricts aṅga effects after lu-marked affix deletion; not a universal erasure of features. |
| [1.1.64](https://ashtadhyayi.com/sutraani/1/1/64) | अचोऽन्त्यादि टि — *aco'ntyādi ṭi* | Defines ṭi, a structural segment of a unit; preserve segmentation. |
| [1.1.65](https://ashtadhyayi.com/sutraani/1/1/65) | अलोऽन्त्यात् पूर्व उपधा — *alo'ntyāt pūrva upadhā* | Defines upadhā; compute within the relevant morphological unit. |
| [1.1.66](https://ashtadhyayi.com/sutraani/1/1/66) | तस्मिन्निति निर्दिष्टे पूर्वस्य — *tasminniti nirdiṣṭe pūrvasya* | Locative sound-context convention, where that interpretation is licensed; not every locative is spatial. |
| [1.1.67](https://ashtadhyayi.com/sutraani/1/1/67) | तस्मादित्युत्तरस्य — *tasmādityuttarasya* | Ablative prior-context convention, where applicable; retain adjacency and unit scope. |
| [1.1.68](https://ashtadhyayi.com/sutraani/1/1/68) | स्वं रूपं शब्दस्याशब्दसंज्ञा — *svaṃ rūpaṃ śabdasyāśabdasaṃjñā* | Distinguishes literal word-form reference from technical designations. |
| [1.1.72](https://ashtadhyayi.com/sutraani/1/1/72) | येन विधिस्तदन्तस्य — *yena vidhistadantasya* | Tadanta interpretation with commentary restrictions; no unrestricted suffix matching. |
| [1.3.10](https://ashtadhyayi.com/sutraani/1/3/10) | यथासंख्यमनुदेशः समानाम् — *yathāsaṃkhyamanudeśaḥ samānām* | Ordered correspondence of equal lists; sets alone lose the order needed here. |
| [1.4.1](https://ashtadhyayi.com/sutraani/1/4/1) | आ कडारादेका संज्ञा — *ā kaḍārādekā saṃjñā* | Governs exclusivity of designations in its region; scope cannot be assumed global. |
| [1.4.2](https://ashtadhyayi.com/sutraani/1/4/2) | विप्रतिषेधे परं कार्यम् — *vipratiṣedhe paraṃ kāryam* | Later rule in an equal-strength conflict; exceptions and visibility are decided separately. |

## Upadeśa and it markers

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [1.3.2](https://ashtadhyayi.com/sutraani/1/3/2) | उपदेशेऽजनुनासिक इत् — *upadeśe'janunāsika it* | Designates nasalized vowels as it in upadeśa; ordinary nasal speech is a different domain. |
| [1.3.3](https://ashtadhyayi.com/sutraani/1/3/3) | हलन्त्यम् — *halantyam* | Final consonant it designation in the inherited domain, subject to restrictions such as 1.3.4. |
| [1.3.4](https://ashtadhyayi.com/sutraani/1/3/4) | न विभक्तौ तुस्माः — *na vibhaktau tusmāḥ* | Protects specified dental/s/m finals in vibhakti from the preceding it rule. |
| [1.3.5](https://ashtadhyayi.com/sutraani/1/3/5) | आदिर्ञिटुडवः — *ādirñiṭuḍavaḥ* | Initial ñi/ṭu/ḍu designations; use teaching-form segmentation. |
| [1.3.6](https://ashtadhyayi.com/sutraani/1/3/6) | षः प्रत्ययस्य — *ṣaḥ pratyayasya* | Initial ṣ of an affix; preserve inherited position/category conditions. |
| [1.3.7](https://ashtadhyayi.com/sutraani/1/3/7) | चुटू — *cuṭū* | Initial cu/ṭu material in affixes; the sound classes are not character substrings. |
| [1.3.8](https://ashtadhyayi.com/sutraani/1/3/8) | लशक्वतद्धिते — *laśakvataddhite* | Initial l/ś/ku in non-taddhita affixes; the exclusion is part of the rule. |
| [1.3.9](https://ashtadhyayi.com/sutraani/1/3/9) | तस्य लोपः — *tasya lopaḥ* | Elides the designated it material; preserve the identity needed by later licensed rules. |
| [1.4.104](https://ashtadhyayi.com/sutraani/1/4/104) | विभक्तिश्च — *vibhaktiśca* | Vibhakti designation in its inherited scope; needed when evaluating 1.3.4. |

## Lexical and morphological units

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [1.2.45](https://ashtadhyayi.com/sutraani/1/2/45) | अर्थवदधातुरप्रत्ययः प्रातिपदिकम् — *arthavadadhāturapratyayaḥ prātipadikam* | Defines prātipadika with meaning and category exclusions; not every input string is a stem. |
| [1.2.46](https://ashtadhyayi.com/sutraani/1/2/46) | कृत्तद्धितसमासाश्च — *kṛttaddhitasamāsāśca* | Extends prātipadika designation to kṛt/taddhita/compound products. |
| [1.3.1](https://ashtadhyayi.com/sutraani/1/3/1) | भूवादयो धातवः — *bhūvādayo dhātavaḥ* | Dhātu designation depends on the root inventory and its extensions. |
| [1.3.12](https://ashtadhyayi.com/sutraani/1/3/12) | अनुदात्तङित आत्मनेपदम् — *anudāttaṅita ātmanepadam* | Ātmanepada selection reads root upadeśa features; the full pada-selection section is larger. |
| [1.3.78](https://ashtadhyayi.com/sutraani/1/3/78) | शेषात् कर्तरि परस्मैपदम् — *śeṣāt kartari parasmaipadam* | Residual kartari parasmaipada selection after prior restrictions; not a blanket default first. |
| [1.4.13](https://ashtadhyayi.com/sutraani/1/4/13) | यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम् — *yasmāt pratyayavidhistadādi pratyaye'ṅgam* | Aṅga is relative to a following affix prescription; boundaries must be retained. |
| [1.4.14](https://ashtadhyayi.com/sutraani/1/4/14) | सुप्तिङन्तं पदम् — *suptiṅantaṃ padam* | Sup/tiṅ-ending pada designation, including separately licensed effects after deletion. |
| [1.4.18](https://ashtadhyayi.com/sutraani/1/4/18) | यचि भम् — *yaci bham* | Bha designation in its inherited environment; lexical and morphological scope matter. |
| [1.4.58](https://ashtadhyayi.com/sutraani/1/4/58) | प्रादयः — *prādayaḥ* | Prādi designation needs the associated lexical gaṇa. |
| [1.4.59](https://ashtadhyayi.com/sutraani/1/4/59) | उपसर्गाः क्रियायोगे — *upasargāḥ kriyāyoge* | Upasarga status depends on relation to a verbal operation, not position alone. |
| [3.1.1](https://ashtadhyayi.com/sutraani/3/1/1) | प्रत्ययः — *pratyayaḥ* | Pratyaya heading; the affix domain must be attached to individual readings. |
| [3.1.2](https://ashtadhyayi.com/sutraani/3/1/2) | परश्च — *paraśca* | Following placement in its inherited scope; exceptions and augments remain separate. |
| [3.1.22](https://ashtadhyayi.com/sutraani/3/1/22) | धातोरेकाचो हलादेः क्रियासमभिहारे यङ् — *dhātorekāco halādeḥ kriyāsamabhihāre yaṅ* | Full yaṅ prescription also supplies inherited dhātoḥ later; do not reduce the source to one word. |
| [3.1.67](https://ashtadhyayi.com/sutraani/3/1/67) | सार्वधातुके यक् — *sārvadhātuke yak* | Yak prescription and source of sārvadhātuke inherited into 3.1.68. |
| [3.1.68](https://ashtadhyayi.com/sutraani/3/1/68) | कर्तरि शप् — *kartari śap* | Śap before an agent-expressing sārvadhātuka; kartari is semantic, not a sound on the right. |
| [3.1.134](https://ashtadhyayi.com/sutraani/3/1/134) | नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः — *nandigrahipacādibhyo lyuṇinyacaḥ* | Three lexical-group affix prescriptions; ac provides a marker-loss comparison with śap. |
| [3.2.123](https://ashtadhyayi.com/sutraani/3/2/123) | वर्तमाने लट् — *vartamāne laṭ* | Laṭ in the present-time domain; the semantic input must be supplied. |
| [3.3.1](https://ashtadhyayi.com/sutraani/3/3/1) | उणादयो बहुलम् — *uṇādayo bahulam* | Uṇādi/bahulam dependency; a source-scoped extension, not an invitation to guess missing forms. |
| [3.4.69](https://ashtadhyayi.com/sutraani/3/4/69) | लः कर्मणि च भावे चाकर्मकेभ्यः — *laḥ karmaṇi ca bhāve cākarmakebhyaḥ* | Lakāra expression of semantic roles with inherited context; required for abhihita accounting. |
| [3.4.77](https://ashtadhyayi.com/sutraani/3/4/77) | लस्य — *lasya* | Lakāra substitution heading for endings; preserve the replaced lakāra identity. |
| [3.4.78](https://ashtadhyayi.com/sutraani/3/4/78) | तिप्तस्झिसिप्थस्थमिब्वस्मस् तातांझथासाथांध्वमिड्वहिमहिङ् — *tiptasjhisipthasthamibvasmas tātāṃjhathāsāthāṃdhvamiḍvahimahiṅ* | The eighteen tiṅ endings; expanded segmentation is recorded separately in the specification. |
| [3.4.113](https://ashtadhyayi.com/sutraani/3/4/113) | तिङ्शित्सार्वधातुकम् — *tiṅśitsārvadhātukam* | Tiṅ and śit sārvadhātuka designation; the elided ś can remain grammatically relevant. |
| [3.4.114](https://ashtadhyayi.com/sutraani/3/4/114) | आर्धधातुकं शेषः — *ārdhadhātukaṃ śeṣaḥ* | Ārdhadhātuka designation in the root-affix domain; not every unclassified token gets the label. |
| [4.1.1](https://ashtadhyayi.com/sutraani/4/1/1) | ङ्याप्प्रातिपदिकात् — *ṅyāpprātipadikāt* | Nominal affix domain; retain feminine-affix and prātipadika dependencies. |
| [4.1.2](https://ashtadhyayi.com/sutraani/4/1/2) | स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप् — *svaujasamauṭchaṣṭābhyāmbhisṅebhyāmbhyasṅasibhyāmbhyasṅasosāṅṅyossup* | The twenty-one sup endings; selection needs case/number and the governing domain. |
| [4.1.76](https://ashtadhyayi.com/sutraani/4/1/76) | तद्धिताः — *taddhitāḥ* | Taddhita heading; meaning and lexical class are indispensable downstream. |
| [5.4.68](https://ashtadhyayi.com/sutraani/5/4/68) | समासान्ताः — *samāsāntāḥ* | Samāsānta heading; compounds require their own structured input. |

## Person, number, kāraka and compounds

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [1.4.24](https://ashtadhyayi.com/sutraani/1/4/24) | ध्रुवमपायेऽपादानम् — *dhruvamapāye'pādānam* | Apādāna definition; the semantic relation is input to the grammatical assignment. |
| [1.4.32](https://ashtadhyayi.com/sutraani/1/4/32) | कर्मणा यमभिप्रैति स सम्प्रदानम् — *karmaṇā yamabhipraiti sa sampradānam* | Sampradāna definition; do not infer the relation from a preselected case ending. |
| [1.4.42](https://ashtadhyayi.com/sutraani/1/4/42) | साधकतमं करणम् — *sādhakatamaṃ karaṇam* | Karaṇa definition; needs the intended event structure. |
| [1.4.45](https://ashtadhyayi.com/sutraani/1/4/45) | आधारोऽधिकरणम् — *ādhāro'dhikaraṇam* | Adhikaraṇa definition; not synonymous with every locative noun. |
| [1.4.49](https://ashtadhyayi.com/sutraani/1/4/49) | कर्तुरीप्सिततमं कर्म — *karturīpsitatamaṃ karma* | Karman definition; additional rules extend/restrict the domain. |
| [1.4.54](https://ashtadhyayi.com/sutraani/1/4/54) | स्वतन्त्रः कर्ता — *svatantraḥ kartā* | Kartṛ definition; a semantic role distinct from an English word-order position. |
| [1.4.99](https://ashtadhyayi.com/sutraani/1/4/99) | लः परस्मैपदम् — *laḥ parasmaipadam* | Parasmaipada designation for the relevant lakāra substitutes. |
| [1.4.100](https://ashtadhyayi.com/sutraani/1/4/100) | तङानावात्मनेपदम् — *taṅānāvātmanepadam* | Ātmanepada designation for taṅ/ānau in its domain. |
| [1.4.101](https://ashtadhyayi.com/sutraani/1/4/101) | तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः — *tiṅastrīṇi trīṇi prathamamadhyamottamāḥ* | Triples of tiṅ endings define prathama, madhyama and uttama; prathama corresponds to English third person. |
| [1.4.102](https://ashtadhyayi.com/sutraani/1/4/102) | तान्येकवचनद्विवचनबहुवचनान्येकशः — *tānyekavacanadvivacanabahuvacanānyekaśaḥ* | Each triple is ordered singular, dual, plural. |
| [1.4.105](https://ashtadhyayi.com/sutraani/1/4/105) | युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः — *yuṣmadyupapade samānādhikaraṇe sthāninyapi madhyamaḥ* | Madhyama selection under the yuṣmad relation; supplied discourse agreement matters. |
| [1.4.107](https://ashtadhyayi.com/sutraani/1/4/107) | अस्मद्युत्तमः — *asmadyuttamaḥ* | Uttama selection under the asmad relation. |
| [1.4.108](https://ashtadhyayi.com/sutraani/1/4/108) | शेषे प्रथमः — *śeṣe prathamaḥ* | Residual prathama selection after the preceding conditions. |
| [2.1.1](https://ashtadhyayi.com/sutraani/2/1/1) | समर्थः पदविधिः — *samarthaḥ padavidhiḥ* | Samartha condition on pada operations; phonological adjacency is insufficient. |
| [2.1.3](https://ashtadhyayi.com/sutraani/2/1/3) | प्राक् कडारात् समासः — *prāk kaḍārāt samāsaḥ* | Samāsa heading; later prescriptions require compound type and meaningful relation. |
| [2.3.1](https://ashtadhyayi.com/sutraani/2/3/1) | अनभिहिते — *anabhihite* | Anabhihita gate on relevant kāraka-vibhakti prescriptions; retain what another affix already expresses. |
| [2.3.2](https://ashtadhyayi.com/sutraani/2/3/2) | कर्मणि द्वितीया — *karmaṇi dvitīyā* | Karman accusative in its licensed unexpressed domain. |
| [2.3.18](https://ashtadhyayi.com/sutraani/2/3/18) | कर्तृकरणयोस्तृतीया — *kartṛkaraṇayostṛtīyā* | Agent/instrument instrumental with its governing conditions. |
| [2.3.46](https://ashtadhyayi.com/sutraani/2/3/46) | प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा — *prātipadikārthaliṅgaparimāṇavacanamātre prathamā* | Nominative in the specified stem-meaning/gender/measure/number-only domain. |
| [2.3.50](https://ashtadhyayi.com/sutraani/2/3/50) | षष्ठी शेषे — *ṣaṣṭhī śeṣe* | Residual genitive; do not reduce every genitive relation to ownership. |
| [2.4.71](https://ashtadhyayi.com/sutraani/2/4/71) | सुपो धातुप्रातिपदिकयोः — *supo dhātuprātipadikayoḥ* | Sup deletion in the specified dhātu/prātipadika domain; compounding is not arbitrary word concatenation. |

## Sandhi, aṅga and visibility regions

| Sūtra | Sanskrit / IAST | Grammatical role and boundary |
|---|---|---|
| [6.1.72](https://ashtadhyayi.com/sutraani/6/1/72) | संहितायाम् — *saṃhitāyām* | Saṃhitā heading; record its inherited effect for every selected sandhi rule. |
| [6.1.77](https://ashtadhyayi.com/sutraani/6/1/77) | इको यणचि — *iko yaṇaci* | Ik to yaṇ before a vowel; savarṇa, optional/exceptional cases and the actual context still matter. |
| [6.1.78](https://ashtadhyayi.com/sutraani/6/1/78) | एचोऽयवायावः — *eco'yavāyāvaḥ* | Ec to ay/av/āy/āv with aci inherited from 6.1.77; ordered substitution list. |
| [6.1.84](https://ashtadhyayi.com/sutraani/6/1/84) | एकः पूर्वपरयोः — *ekaḥ pūrvaparayoḥ* | One substitute for both units; the chosen Kāśikā scope is 6.1.85–111. |
| [6.1.85](https://ashtadhyayi.com/sutraani/6/1/85) | अन्तादिवच्च — *antādivacca* | Ekādeśa can have end/beginning behavior; subsequent tests cannot simply forget its two inputs. |
| [6.1.87](https://ashtadhyayi.com/sutraani/6/1/87) | आद्गुणः — *ādguṇaḥ* | Guṇa after a/ā in the source's vowel domain; T80's ik restriction is a finite-model restriction. |
| [6.1.88](https://ashtadhyayi.com/sutraani/6/1/88) | वृद्धिरेचि — *vṛddhireci* | Vṛddhi with ec in the governing two-unit scope; an inherited prior a/ā condition is essential. |
| [6.1.97](https://ashtadhyayi.com/sutraani/6/1/97) | अतो गुणे — *ato guṇe* | Pararūpa after non-pada-final a before guṇa; retain apadāntāt and the declared exception reading. |
| [6.1.101](https://ashtadhyayi.com/sutraani/6/1/101) | अकः सवर्णे दीर्घः — *akaḥ savarṇe dīrghaḥ* | Long substitute for savarṇa ak junctions; its application competes with context-specific exceptions. |
| [6.4.1](https://ashtadhyayi.com/sutraani/6/4/1) | अङ्गस्य — *aṅgasya* | Aṅga heading for following prescriptions; cannot be flattened into whole-string editing. |
| [6.4.22](https://ashtadhyayi.com/sutraani/6/4/22) | असिद्धवदत्राभात् — *asiddhavadatrābhāt* | Ābhīya asiddhavat: chosen Kāśikā end-of-6.4 scope and same-support restriction; not Tripādī order. |
| [6.4.129](https://ashtadhyayi.com/sutraani/6/4/129) | भस्य — *bhasya* | Bha region within 6.4; preserve the chosen commentary's treatment under 6.4.22. |
| [7.1.3](https://ashtadhyayi.com/sutraani/7/1/3) | झोऽन्तः — *jho'ntaḥ* | Jh-ending replacement by ant; used in the bhavanti derivation. |
| [7.3.84](https://ashtadhyayi.com/sutraani/7/3/84) | सार्वधातुकार्धधातुकयोः — *sārvadhātukārdhadhātukayoḥ* | Guṇa in the licensed sārvadhātuka/ārdhadhātuka context; other guards can block it. |
| [8.1.16](https://ashtadhyayi.com/sutraani/8/1/16) | पदस्य — *padasya* | Pada heading relevant to the later phonological domain. |
| [8.2.1](https://ashtadhyayi.com/sutraani/8/2/1) | पूर्वत्रासिद्धम् — *pūrvatrāsiddham* | Rule-relative Tripādī invisibility; includes later effects versus earlier Tripādī rules. |
| [8.2.66](https://ashtadhyayi.com/sutraani/8/2/66) | ससजुषो रुः — *sasajuṣo ruḥ* | Ru substitution in the pada-final domain; technical ru includes a marker, not a spoken u. |
| [8.3.15](https://ashtadhyayi.com/sutraani/8/3/15) | खरवसानयोर्विसर्जनीयः — *kharavasānayorvisarjanīyaḥ* | Visarga before khar or at pause; preserve the distinction from voiced continuations. |
| [8.3.23](https://ashtadhyayi.com/sutraani/8/3/23) | मोऽनुस्वारः — *mo'nusvāraḥ* | Pada-final m to anusvāra in its inherited consonant context; not unconditional m replacement. |
| [8.4.40](https://ashtadhyayi.com/sutraani/8/4/40) | स्तोः श्चुना श्चुः — *stoḥ ścunā ścuḥ* | Ścutva in a specified sound environment; full blocking and optional contexts exceed the local table. |
| [8.4.56](https://ashtadhyayi.com/sutraani/8/4/56) | वाऽवसाने — *vā'vasāne* | Optional pause voicing/devoicing context; one mandatory output is not a general completeness criterion. |

## The fourteen Māheśvara sūtras

The final consonant in each teaching formula is its terminal marker. Store
its **position and sūtra identity**: the two ṇ markers and repeated ha cannot
be distinguished by a bare character alone. The Sanskrit below is the pinned
publisher text. For token-separated finite interval calculations, see
[T78](../../theorum/78_shaiva_sources_maheshvara_spanda_pratyabhijna_theorem.md).

| Number | Sanskrit | IAST transcription |
|---|---|---|
| 1 | अइउण् | aiuṇ |
| 2 | ऋऌक् | ṛḷk |
| 3 | एओङ् | eoṅ |
| 4 | ऐऔच् | aiauc |
| 5 | हयवरट् | hayavaraṭ |
| 6 | लण् | laṇ |
| 7 | ञमङणनम् | ñamaṅaṇanam |
| 8 | झभञ् | jhabhañ |
| 9 | घढधष् | ghaḍhadhaṣ |
| 10 | जबगडदश् | jabagaḍadaś |
| 11 | खफछठथचटतव् | khaphachaṭhathacaṭatav |
| 12 | कपय् | kapay |
| 13 | शषसर् | śaṣasar |
| 14 | हल् | hal |

Total: **120 selected Aṣṭādhyāyī records**, plus the fourteen phonetic
sūtras. The complete numbered text inventory remains in
[SUTRAPATHA.tsv](SUTRAPATHA.tsv); unselected entries are not thereby unimportant.
