# Samāsa: the Mathematical Construction — sāmarthya, the semantic domains, upasarjana selection, sup-lopa and aluk, the samāsānta affixes (2.1.1–2.2.38, 2.4.1–2.4.85, 5.4.68–5.4.160, 6.3.1–6.3.83)

2 November 2026. A theoretical packet. theorum/104 (twelve compounds declined)
and theorum/114 (avyayībhāva, dvigu) certified *instances*; this packet gives
the **construction** those instances live in: the carrier, the predicates, the
ordering function, the deletion operator, the affix map — every clause taken
from the pinned sūtrapāṭha (`research/panini_grammar/SUTRAPATHA.tsv`, PG1) and
quoted in §A, every example either from an earlier certified packet or marked
as a commentary example. Python certificates are secondary here and deferred
(§8). Nothing in 104 / 114 is re-pinned; §1 records a correction to a *label*
in 114 without touching its certificate.

---

## 0. What a compound is, in one sentence of the text

> 2.1.3 *prāk kaḍārāt samāsaḥ* ; 2.1.4 *saha supā* ; 2.1.1 *samarthaḥ padavidhiḥ*

A samāsa is a *padavidhi* (an operation on padas, 2.1.1) that takes a
**sup-ending pada together with another sup-ending pada** (2.1.4: *saha supā*,
the anuvṛtti of *sup* from 2.1.2) and makes one prātipadika of them (1.2.46
*kṛttaddhitasamāsāś ca*), inside the domain 2.1.3 – 2.2.38 (*prāk kaḍārāt*:
up to, not including, 2.2.38 *kaḍārāḥ karmadhāraye*). Everything below is a
reading of the finite set of clauses in that domain and of the clauses the
domain points to (2.4, 5.4, 6.3).

---

## 1. Primary-source resolution of 2.1.7 (the T114 qualification)

**Pinned text.** `2.1.7  यथासादृश्ये  yathāsādṛśye` — one word in saṁhitā.
Its only lawful analysis against 2.1.6 is **yathā + a-sādṛśye** (*yathā
'sādṛśye*): 2.1.6 already lists *sādṛśya* (similarity) among the senses in
which an avyaya compounds (…*yaugapadya-**sādṛśya**-sampatti*…), so a
2.1.7 reading *yathā sādṛśye* would be empty. The tradition's reading is
the privative: *yathā* forms an avyayībhāva **in a sense other than
similarity** — Kāśikā names the remaining senses of *yathā*: yogyatā
(fitness: *yathāśakti* "according to ability"), vīpsā (distribution:
*yathāgṛham*), padārthānativṛtti (not exceeding: *yathāvidhi*). When *yathā*
means similarity (*yathā Devadattas tathā Yajñadattaḥ*) **no** avyayībhāva is
formed and the sentence stands.

**Consequence for theorum/114.** T114 derives *yathāśakti* by 2.1.7 and
2.4.82; that derivation is right. Its claim-boundary sentence labels the
*sense* of *yathāśakti* "sādṛśya"; that label is the one sense 2.1.7
**excludes**. Corrected reading: sense = yogyatā / anativṛtti, licensed by
2.1.7 *precisely because it is not sādṛśya*. The certificate's forms,
ablations and pin are unaffected (the sense is a declared input there, not
a computed one); the correction is recorded here and in 114's capsule as a
note, pin unchanged, history preserved.

**Domain structure read off 2.1.6 / 2.1.7.**

| sense of the avyaya | licensing clause | compound | vigraha survives? |
|---|---|---|---|
| sādṛśya with an avyaya *other than yathā* | 2.1.6 (…sādṛśya…) | *sadṛśam* type: e.g. *sa-sakhi* (Kāśikā) | nitya (2.1.5–2.1.10 lie before the *vibhāṣā* of 2.1.11) |
| sādṛśya with *yathā* | **none** (2.1.7 excludes it) | — | sentence only |
| yathā in yogyatā / vīpsā / anativṛtti | 2.1.7 | *yathāśakti*, *yathāgṛham*, *yathāvidhi* | nitya |

This is the first explicit branch of the construction: the same avyaya,
two senses, one compounds and one does not, and the text says which.

---

## 2. Definitions

**D1 (pada record).** A sup-ending pada is a record
`p = (π, v, n, g)` — prātipadika π (1.2.45 / 1.2.46), vibhakti
v ∈ {1,…,7} named by its sup (4.1.2), number n ∈ {s, d, p}, gender g — with
the kāraka that assigned v (2.3.1 *anabhihite*, 2.3.2 *karmaṇi dvitīyā*, …,
2.3.50 *ṣaṣṭhī śeṣe*). A **vigraha** is a finite sequence of padas with a
dependency relation `R` (which pada depends on which): the sentence that
says what the compound says.

**D2 (sāmarthya, 2.1.1).** *samarthaḥ padavidhiḥ*: a padavidhi applies to
padas p₁, p₂ **only if** `(p₁, p₂) ∈ R` — the two are in construction with
each other in the vigraha, and (ekārthībhāva, the Mahābhāṣya's reading of
2.1.1 for samāsa) after the operation they denote one thing jointly. The
operational content is a *guard*: samāsa is a partial function whose domain
is the set of edges of R, not the set of adjacent pairs. The classical
counter-example (Mahābhāṣya on 2.1.1, commentary): in *bhāryā rājñaḥ,
puruṣo Devadattasya* the adjacent *rājñaḥ puruṣaḥ* is **not** an edge of R
(*rājñaḥ* depends on *bhāryā*), so *rājapuruṣaḥ* is not formed there.

**D3 (the four classes as a partition of the domain).** The domain
2.1.3 – 2.2.38 is partitioned by its headings:

| class | heading | span | semantic key |
|---|---|---|---|
| avyayībhāva | 2.1.5 *avyayībhāvaḥ* | 2.1.5 – 2.1.21 | first member an avyaya (2.1.6 list), or the listed sup-forms (2.1.9 *suppratinā mātrārthe*, 2.1.10, 2.1.12 *apaparibahirañcavaḥ pañcamyā*, 2.1.13 *āṅ maryādābhividhyoḥ*, …) |
| tatpuruṣa | 2.1.22 *tatpuruṣaḥ* | 2.1.22 – 2.2.22 | second member is the head; vibhakti-named (2.1.24 – 2.1.48, 2.2.8 – 2.2.17), samānādhikaraṇa = karmadhāraya (1.2.42; 2.1.49 – 2.1.72), saṁkhyā-first = dvigu (2.1.52; 2.1.23), nañ (2.2.6), kugatiprādi (2.2.18), upapada (2.2.19) |
| bahuvrīhi | 2.2.23 *śeṣo bahuvrīhiḥ* | 2.2.23 – 2.2.28 | *anekam anyapadārthe* (2.2.24): the referent is outside the members |
| dvandva | 2.2.29 *cārthe dvandvaḥ* | 2.2.29 | the members are coordinated (*ca*) |

2.2.30 – 2.2.38 are not a class: they are the **placement** clauses (D5)
that close the domain.

**D4 (the option algebra).** Each vidhi carries one of five modal marks,
read from the text:

| mark | source | meaning (as a set of licensed outputs) |
|---|---|---|
| nitya | the clauses 2.1.5 – 2.1.10 before 2.1.11; *nityam* in 2.2.17 | {compound} — the vigraha with the same words is not a licensed sentence |
| vibhāṣā | 2.1.11 *vibhāṣā* (adhikāra over the rest of the samāsa section) | {compound, vigraha} |
| vā / anyatarasyām | 2.1.18 *pāre madhye ṣaṣṭhyā vā*; 2.2.3, 2.2.21 *anyatarasyām*; 5.4.109; 6.3.82 | {branch A, branch B} on the sub-case named |
| bahulam | 2.1.32 *kartṛkaraṇe kṛtā bahulam*; 2.1.57 *viśeṣaṇaṁ viśeṣyeṇa bahulam*; 2.4.84; 6.3.14 | the four-valued *bahulam* of the tradition (applies / does not / optional / otherwise) — recorded as **not reducible to a set** without the gaṇa / usage data; left as a declared input |
| na (prohibition) | 2.2.10 *na nirdhāraṇe*; 2.4.14; 5.4.69, 5.4.89, 5.4.155 | removes a pair from the domain of the class |

The output of the construction for a vigraha is therefore a **set** of
licensed surface strings, not one string; every certified instance in
104 / 114 lies in such a set, and where the set had two elements the
certificate declared which element it realised.

**D5 (upasarjana and placement).**
*Upasarjana* (1.2.43 *prathamānirdiṣṭaṁ samāsa upasarjanam*): in a samāsa
vidhi, the member whose vibhakti the sūtra names **in the nominative** is
upasarjana. 1.2.44 *ekavibhakti cāpūrvanipāte*: also upasarjana is the
member that keeps **one fixed vibhakti** in the vigraha, even when it is
not placed first. Placement is the function

```
ORD(class, {m₁, m₂}) =
  2.2.30  upasarjanaṁ pūrvam            : the upasarjana first             (default)
  2.2.31  rājadantādiṣu param           : in the listed gaṇa, upasarjana last
  2.2.32  dvandve ghi                   : dvandva — a ghi member first
  2.2.33  ajādyadantam                  : dvandva — a vowel-initial a-final member first
  2.2.34  alpāctaram                    : dvandva — the member with fewer vowels first
  2.2.35  saptamīviśeṣaṇe bahuvrīhau    : bahuvrīhi — the saptamī member / the viśeṣaṇa first
  2.2.36  niṣṭhā                        : bahuvrīhi — the niṣṭhā member first
  2.2.37  vāhitāgnyādiṣu                : bahuvrīhi — optional (vā) in the listed gaṇa
  2.2.38  kaḍārāḥ karmadhāraye          : karmadhāraya — kaḍāra-words either first or last
```

with the priority: a later clause in 2.2.31 – 2.2.38 is a special case of
2.2.30 and wins on its own domain (the *apavāda* reading, 1.4.2
*vipratiṣedhe paraṁ kāryam* for the dvandva triple 2.2.32 / 33 / 34 when two
apply at once).

**D6 (gender and number of the output).**

| clause | class | output |
|---|---|---|
| 2.4.26 *paravalliṅgaṁ dvandvatatpuruṣayoḥ* | dvandva, tatpuruṣa | gender = gender of the last member |
| 2.4.17 *sa napuṁsakam* (with 2.4.1 *dvigur ekavacanam*, 2.4.2 ff.) | samāhāra dvigu, samāhāra dvandva | neuter singular |
| 2.4.18 *avyayībhāvaś ca* | avyayībhāva | neuter (and avyaya by 1.1.41) |
| 2.4.19 *tatpuruṣo 'nañ karmadhārayaḥ* | tatpuruṣa except nañ / karmadhāraya | the exceptions 2.4.20 – 2.4.31 (e.g. 2.4.29 *rātrāhnāhāḥ puṁsi*, 2.4.30 *apathaṁ napuṁsakam*, 2.4.31 *ardharcāḥ puṁsi ca*) |
| — (2.2.24 semantics) | bahuvrīhi | gender and number of the *anyapadārtha* (the external referent) |

**D7 (the deletion operator on the inner sup).**
`DEL(sup, context)`:
- default: **luk** by 2.4.71 *supo dhātuprātipadikayoḥ* (luk = 1.1.61
  *pratyayasya lukślulupaḥ*);
- **1.1.62** *pratyayalope pratyayalakṣaṇam*: the member remains a pada
  (1.4.14 *suptiṅantaṁ padam*), so pada-final operations apply — 8.2.7
  *nalopaḥ prātipadikāntasya* (rāja-puruṣa), 8.2.66 / 8.3.15 / 8.3.45
  (*nityaṁ samāse 'nuttarapadasthasya*) etc.;
- **1.1.63** *na lumatāṅgasya*: but no **aṅga** operation conditioned on the
  deleted sup applies (so no 7.1.9 *ato bhisa ais* inside the compound,
  no 7.3.102 *supi ca*, …);
- **aluk** on the domain 6.3.1 *aluguttarapade* – 6.3.24: the sup is kept —
  6.3.2 pañcamī after stokādi (*stokānmuktaḥ*), 6.3.3 tṛtīyā after ojas /
  sahas / ambhas / tamas (*ojasākṛtam*), 6.3.4 *manasaḥ saṁjñāyām*, 6.3.7
  caturthī in a *vaiyākaraṇa* name, 6.3.9 *haladantāt saptamyāḥ saṁjñāyām*
  (yudhiṣṭhira, kaṇṭhekāla), 6.3.14 *tatpuruṣe kṛti bahulam*, 6.3.18, 6.3.21
  *ṣaṣṭhyā ākrośe*, 6.3.23 *ṛto vidyāyonisambandhebhyaḥ* (pitur antevāsī →
  *piturantevāsī*? — the gaṇa form; recorded), 6.3.24 *vibhāṣā svasṛpatyoḥ*.

So `DEL` is a two-valued operator (luk / aluk) whose aluk branch is a
finite list, and the luk branch splits the subsequent rule set into
"pada-final: yes" (1.1.62) and "aṅga-conditioned-on-the-sup: no" (1.1.63).

**D8 (the samāsānta map).** Under 5.4.68 *samāsāntāḥ* (an adhikāra to
5.4.160, itself inside 4.1.76 *taddhitāḥ*: the samāsānta is a **taddhita**,
hence 1.4.18 bha, 6.4.144 *nas taddhite*, 6.4.148 *yasyeti ca*, 7.2.117 for
ñit / ṇit ones), `SA(class, final member, condition)` is the partial function

| affix | clause | domain | example (source) |
|---|---|---|---|
| ṭac | 5.4.86 *tatpuruṣasyāṅguleḥ saṁkhyāvyayādeḥ* | tatpuruṣa in aṅguli after saṁkhyā / avyaya | dvyaṅgulam (W10) |
| ṭac | 5.4.87 *ahassarvaikadeśasaṁkhyātapuṇyāc ca rātreḥ* | rātri after the listed | sarvarātraḥ (2.4.29 masc.) |
| ṭac | 5.4.91 *rājāhassakhibhyaṣ ṭac* | tatpuruṣa in rājan / ahan / sakhi | mahārājaḥ (theorum/104, certified) |
| ṭac | 5.4.92 *gor ataddhitaluki* | compound in go (not a taddhita-luk) | pañcagavam (theorum/114, certified) |
| ṭac | 5.4.106 *dvandvāc cudaṣahāntāt samāhāre* | samāhāra dvandva ending in cu / ḍ / ṣ / h | vāktvacam (Kāśikā) |
| ṭac | 5.4.107 *avyayībhāve śaratprabhṛtibhyaḥ*; 5.4.108 *anaś ca*; 5.4.109 *napuṁsakād anyatarasyām* | avyayībhāva in śarad-list / an-final / neuter (optional) | upaśaradam (W12); upacarmam; upacarma / upacarmam |
| a (ac) | 5.4.74 *ṛkpūrabdhūḥpathām ānakṣe* | compound in ṛc, pur, ap, dhur, pathin | ardharcaḥ (W11), rājapathaḥ |
| a (ac) | 5.4.75 *ac pratyanvavapūrvāt sāmalomnaḥ* | sāman / loman after prati / anu / ava | anulomam |
| ḍac | 5.4.73 *bahuvrīhau saṁkhyeye ḍajabahugaṇāt* | bahuvrīhi in a number (not bahu / gaṇa) | upadaśāḥ (W15): ḍit → 6.4.143 ṭi-lopa |
| ṣac | 5.4.113 *bahuvrīhau sakthyakṣṇoḥ svāṅgāt ṣac* | bahuvrīhi in sakthi / akṣi as body-part | dīrghasakthaḥ (W13); ṣit → ṅīṣ 4.1.41 in the feminine |
| ic | 5.4.127 *ic karmavyatihāre* | the 2.2.27 bahuvrīhi | keśākeśi (W16; one step open) |
| kap | 5.4.151 *uraḥprabhṛtibhyaḥ kap*; 5.4.153 *nadyṛtaś ca*; 5.4.154 *śeṣād vibhāṣā*; 5.4.155 *na saṁjñāyām* | bahuvrīhi in uras-list; in a nadī / ṛ-stem; else optional; never in a name | bahunadīkaḥ (W14); bahuyavaḥ / bahuyavakaḥ; *bahuyavo nāma* |
| prohibitions | 5.4.69 *na pūjanāt*, 5.4.71 *nañas tatpuruṣāt* (with 2.4.30), 5.4.89 *na saṁkhyādeḥ samāhāre* | — | — |

`SA` is **optional** exactly where the text says *anyatarasyām* / *vibhāṣā*
(5.4.109, 5.4.154) and **blocked** exactly where it says *na*; everywhere
else in its domain it is obligatory, and outside its domain the compound
takes no samāsānta (the default, which is what 104's rājapuruṣa and
kṛṣṇaśrita realise).

---

## 3. Lemmas

**L1 (the upasarjana is well defined on the vibhakti-tatpuruṣas).** Every
clause in 2.1.24 – 2.1.48 and 2.2.8 – 2.2.17 names exactly one vibhakti in
the nominative (*dvitīyā*, *tṛtīyā*, *caturthī*, *pañcamī*, *saptamī*,
*ṣaṣṭhī*) and names the other member in the instrumental (*śritādibhiḥ*,
*tatkṛtārthena*, *bhayena*, *śauṇḍaiḥ*, …). Hence 1.2.43 selects the
vibhakti-member and 2.2.30 puts it first; this is what theorum/104's
certificate shows as "without 2.2.30 exactly the three mis-ordered
tatpuruṣas break". *Proof*: inspection of the pinned text of the twenty-
five clauses (§A); the only clauses naming two members in the nominative
are 1.2.42 (karmadhāraya), 2.2.24 (*anekam*), 2.2.29 (dvandva: *cārthe*),
and for these the text supplies 2.2.32 – 2.2.38 or the semantic viśeṣaṇa
rule (Kāśikā on 2.2.30: *viśeṣaṇaṁ viśeṣyeṇa* — the qualifier is
upasarjana), so the function ORD of D5 is total on the domain. ∎

**L2 (pada-status survives luk; aṅga-status does not).** By 1.1.62 the
member whose sup was deleted by 2.4.71 is still *suptiṅantam* (1.4.14), so
every rule conditioned on *pada* applies to it; by 1.1.63 no rule
conditioned on the sup as a following affix applies to it as an aṅga.
*Instances*: 8.2.7 on rājan → rāja (pada-final n; 104); 8.2.66 + 8.3.45 on
*manas* + *kāra* → manaskāra (s kept before the uttarapada, pada-conditioned);
but no 7.3.102 (*supi ca*, which would lengthen *rāma* before a bh-initial
sup) inside *rāma-bhakta*. The two clauses are the whole content of
"sup-lopa" and are jointly consistent because they guard different
predicates (*pada* vs *aṅga*). ∎

**L3 (the samāsānta is a taddhita; consequences).** 5.4.68 lies under
4.1.76. Hence (i) the final member before a vowel-initial samāsānta is bha
(1.4.18) — 6.4.144 *nas taddhite* on rājan + ṭac (mahā-rāj-a, certified in
104), 6.4.148 on sakthi + ṣac (dīrgha-sakth-a); (ii) a ṭit samāsānta takes
ṅīp in the feminine by 4.1.15 (*ṭiḍ…*: dvyaṅgulī, Kāśikā), a ṣit one ṅīṣ by
4.1.41 (dīrghasakthī); (iii) 1.2.46 makes the whole a prātipadika again, so
the sup of the compound is added **after** the samāsānta (pañcagava + am,
certified in 114). ∎

**L4 (aluk is sāmarthya-preserving).** The aluk clauses keep the sup but do
not undo 2.1.4 / 1.2.46: *yudhiṣṭhira* is one prātipadika (declined
yudhiṣṭhiraḥ, -am, …) whose first member carries a frozen ṅi. The inner sup
is then no longer a *vibhakti of the sentence* but a part of the stem — which
is why 8.3.59 runs across it (yudhi + sthira → yudhiṣṭhira, W5): the s is
*ādeśa / pratyaya*-internal to the one word. ∎

**L5 (nitya vs vibhāṣā is a position in the text).** 2.1.11 *vibhāṣā* is an
adhikāra; the clauses 2.1.5 – 2.1.10 precede it and are nitya; everything
from 2.1.12 to 2.2.29 inherits *vibhāṣā* unless it says *nityam* (2.2.17
*nityaṁ krīḍājīvikayoḥ*) or *na*. So the licensed-output set of D4 is
{compound} for yathāśakti (2.1.7) and {compound, vigraha} for rājapuruṣa
(2.2.8). ∎

**L6 (gender is not computed from the members for a bahuvrīhi).** 2.4.26
names dvandva and tatpuruṣa only; 2.2.24 defines the bahuvrīhi by the
*anyapadārtha*. Hence the bahuvrīhi's gender is an **input** (the referent),
not an output of the construction — *citragu* is masculine for a man and
feminine (citraguḥ, 1.2.48 hrasva in both) for a woman; the construction
records this as a declared parameter, exactly as 104's certificate declared
it. ∎

---

## 4. The decision procedure

```
SAMĀSA(vigraha V, pair (p₁, p₂), intended sense σ):
 1. guard     : require (p₁, p₂) ∈ R(V)                                   (2.1.1, D2)
 2. class     : find the vidhi clause c in 2.1.5–2.2.29 whose semantic key matches σ
                and whose lexical lists (gaṇa / listed words) admit (p₁, p₂);
                if none → no compound (the sentence stands)              (D3)
 3. mode      : m(c) ∈ {nitya, vibhāṣā, vā, bahulam, na}                  (D4, L5)
 4. head      : u = upasarjana(c)                                         (1.2.43 / 1.2.44, L1)
 5. order     : (m₁, m₂) = ORD(class(c), {p₁, p₂})                        (D5)
 6. delete    : DEL(sup(m₁)) and DEL(sup(m₂)) → luk | aluk                (D7)
 7. stem ops  : pada-final rules on m₁ (1.1.62); junction sandhi 6.1.77 / 87 / 88 / 101;
                the 6.3 uttarapada rules (6.3.34 puṁvat, 6.3.42, 6.3.46 mahat → mahā,
                6.3.67 mum, 6.3.73 nalopo nañaḥ, 6.3.82 vopasarjanasya …)
 8. samāsānta : a = SA(class(c), m₂, σ) ∈ {affix, optional affix, none}    (D8, L3)
                then the taddhita operations on m₂ (6.4.144, 6.4.148, 7.2.117)
 9. category  : prātipadika (1.2.46); gender / number by D6; avyaya if avyayībhāva (1.1.41)
10. sup       : the outer sup by 4.1.2 on the result — 2.4.82 / 2.4.83 / 2.4.84 for
                an avyayībhāva, 2.4.17 + 7.1.24 for a neuter samāhāra, else the
                declension engines (theorum/63, 88, 89, 90, 91, 92, 93, 109)
output: the SET of licensed strings (one per branch of m(c) and of SA)
```

Steps 1 – 5 are what 104 / 114 declared as inputs ("kind of compound and
vidhi sūtra declared"); steps 6 – 10 are what they computed. This packet
turns steps 2 – 5 into explicit functions of the text and names the inputs
that remain inputs (σ, the referent of a bahuvrīhi, gaṇa membership).

---

## 5. Worked derivations

Notation: `[n]` = the sūtra applied; `(m)` = the mode; `⟶` = result;
`{…}` = the licensed set when it has more than one element.

**W1 — rājapuruṣaḥ** (certified, theorum/104). *rājñaḥ puruṣaḥ* ∈ R;
[2.2.8 ṣaṣṭhī] (vibhāṣā: {rājapuruṣaḥ, rājñaḥ puruṣaḥ}); upasarjana = the
ṣaṣṭhī member [1.2.43]; ORD → rājan first [2.2.30]; DEL = luk [2.4.71];
pada-final n → ∅ [8.2.7 via 1.1.62]; no 6.3 rule; SA = none (rājan is the
*first* member, so 5.4.91 — which needs rājan *last* — does not fire);
gender masc. = puruṣa [2.4.26]; prātipadika [1.2.46] ⟶ rājapuruṣa + su.

**W2 — yathāśakti / yathā Devadattaḥ** (the §1 resolution). *śaktim
anatikramya* ∈ R with *yathā* as the avyaya; σ = anativṛtti ≠ sādṛśya ⟹
[2.1.7 yathāsādṛśye] admits; (nitya: {yathāśakti}); ORD: the avyaya first
[2.2.30, the avyaya being the prathamā-named *avyayam* of 2.1.6]; DEL = luk;
neuter [2.4.18], avyaya [1.1.41]; outer sup: śakti is i-final, not a-final,
so [2.4.82 avyayād āpsupaḥ] deletes it ⟶ **yathāśakti**. With σ = sādṛśya
(*yathā Devadattaḥ*): step 2 finds no clause (2.1.7 excludes, 2.1.6's
*sādṛśya* needs an avyaya other than *yathā*) ⟶ no compound. Both branches
are decided by the one pinned word *yathāsādṛśye*.

**W3 — niṣkauśāmbiḥ** (1.2.44 at work). *niṣkrāntaḥ kauśāmbyāḥ* ∈ R;
[2.2.18 kugatiprādayaḥ] (*nis* is a prādi, 1.4.58 ff.) (vibhāṣā);
upasarjana: *kauśāmbī* keeps the fixed pañcamī in the vigraha ⟹ upasarjana
by [1.2.44 ekavibhakti cāpūrvanipāte] **although it is not placed first**
(the prādi stands first by the tatpuruṣa reading of 2.2.18); DEL = luk;
1.2.48 *gostriyor upasarjanasya* on the upasarjana strī-form kauśāmbī ⟶
kauśāmbi (hrasva); [8.3.?] s of nis before k: *niṣ-* by 8.3.41? — not
pulled here; the visarga → ṣ before k is the 8.3.37 / 8.3.41 branch (open,
§6) ⟶ **niṣkauśāmbi** + su ⟶ niṣkauśāmbiḥ. The point of the example: 1.2.44
makes *kauśāmbī* upasarjana for the purpose of 1.2.48 **without** making it
first — upasarjana (a saṁjñā) and *pūrvanipāta* (a placement) are two
different things in the text.

**W4 — kaṇṭhekālaḥ** (bahuvrīhi, aluk, placement). *kaṇṭhe kālo yasya* (Śiva)
∈ R; [2.2.24 anekam anyapadārthe] (vibhāṣā); ORD: the saptamī member first
[2.2.35 saptamīviśeṣaṇe bahuvrīhau]; DEL(ṅi of kaṇṭhe) = **aluk** [6.3.9
haladantāt saptamyāḥ saṁjñāyām: kaṇṭha is a-final (*adantāt*), the compound
is a name]; gender = the referent's (masc., L6) ⟶ **kaṇṭhekāla** + su.
Without 6.3.9 the output would be *kaṇṭhakālaḥ* — a different word; the aluk
list is load-bearing, not cosmetic.

**W5 — yudhiṣṭhiraḥ**. *yudhi sthiraḥ* ∈ R; [2.1.40 saptamī śauṇḍaiḥ]? — no:
sthira is not in the śauṇḍādi list; the compound is by [2.1.57 viśeṣaṇaṁ
viśeṣyeṇa bahulam]? — no, the members are not samānādhikaraṇa. The licensing
clause is the saptamī-tatpuruṣa **by 6.3.9 itself read as nipātana for the
name** (Kāśikā treats *yudhiṣṭhira* under 6.3.9, *haladantāt*: yudh is
hal-final); ORD: saptamī first [2.2.30]; DEL = aluk [6.3.9, saṁjñāyām];
8.3.59 *ādeśapratyayayoḥ*: the s of sthira after the i of the frozen ṅi →
ṣ, then [8.4.41 ṣṭunā ṣṭuḥ] th → ṭh ⟶ **yudhiṣṭhira**. (L4: the ṣatva shows
the ṅi is stem-internal after aluk.) Mode: the licensing clause is a
name-clause ⟹ nitya in the name sense.

**W6 — stokānmuktaḥ**. *stokāt muktaḥ* ∈ R; [2.1.39 stokāntikadūrārthakṛcchrāṇi
ktena] (vibhāṣā); ORD: the pañcamī member first [2.2.30]; DEL = **aluk**
[6.3.2 pañcamyāḥ stokādibhyaḥ]; the frozen ṅasi stands as -āt; 8.4.45
(*yaro 'nunāsike 'nunāsiko vā*) t → n before m ⟶ **stokānmukta** (/ stokātmukta
by the *vā* of 8.4.45) — a second option branch, from the sandhi layer.

**W7 — hariharau** (dvandva, 2.2.32). *hariś ca haraś ca* ∈ R; [2.2.29 cārthe
dvandvaḥ] (vibhāṣā); itaretarayoga (two referents ⟹ dual by 1.4.21 ff.);
ORD: hari is ghi (1.4.7) ⟹ first [2.2.32 dvandve ghi]; DEL = luk ×2; gender =
hara's [2.4.26] ⟶ **harihara** + au ⟶ hariharau.

**W8 — śivakeśavau** (2.2.34). Neither member is ghi, neither vowel-initial;
śiva has 2 vowels, keśava 3 ⟹ śiva first [2.2.34 alpāctaram] ⟶ **śivakeśavau**.
(104's rāmalakṣmaṇau is the same clause, certified: "without 2.2.34 exactly
rāmalakṣmaṇa breaks".)

**W9 — aśvarathau** (2.2.33 over 2.2.34). aśva is vowel-initial and a-final
⟹ first [2.2.33 ajādyadantam]; both have two vowels so 2.2.34 is silent;
had they conflicted, 2.2.33 and 2.2.34 are both apavādas of 2.2.30 and the
later wins (1.4.2) — so *alpāctaram* beats *ajādyadantam* when both apply
(Kāśikā's *indrāgnī* type) ⟶ **aśvarathau**.

**W10 — dvyaṅgulam** (samāsānta ṭac, 5.4.86). *dvayor aṅgulyoḥ samāhāraḥ*;
[2.1.52 saṁkhyāpūrvo dviguḥ] with [2.1.51 taddhitārthottarapadasamāhāre ca]
(samāhāra); ORD: the number first [2.2.30]; DEL = luk; SA = ṭac [5.4.86
tatpuruṣasyāṅguleḥ saṁkhyāvyayādeḥ] ⟹ aṅguli is bha [1.4.18] ⟹ final i →
∅ [6.4.148] ⟹ aṅgul-a; junction dvi + aṅgula: i → y [6.1.77 iko yaṇ aci] ⟹
dvyaṅgula; neuter [2.4.17 sa napuṁsakam], singular [2.4.1]; su → am [7.1.24
ato 'm] ⟶ **dvyaṅgulam**. Feminine of the same by 4.1.15 (ṭit): *dvyaṅgulī*
— the second licensed output when the sense is the measure (4.1.21 / 4.1.15
branch, Kāśikā).

**W11 — ardharcaḥ / ardharcam** (5.4.74 with 2.4.31). *ṛco 'rdham*; [2.2.2
ardhaṁ napuṁsakam] (the *ardha* tatpuruṣa, ekadeśi); ORD: ardha first
[2.2.30, 2.2.2 names *ardham* in the nominative]; DEL = luk; SA = a [5.4.74
ṛkpūrabdhūḥpathām ānakṣe] on ṛc ⟹ ardha + ṛc + a; junction a + ṛ → ar
[6.1.87 ād guṇaḥ, 1.1.51] ⟹ ardharca; gender: [2.4.31 ardharcāḥ puṁsi ca]
⟹ **{ardharcaḥ, ardharcam}** — a two-element licensed set, from the gender
clause this time.

**W12 — upaśaradam** (avyayībhāva + ṭac + am). *śarado samīpam*; [2.1.6
avyayam … samīpa …] (nitya); the avyaya first; DEL = luk; SA = ṭac [5.4.107
avyayībhāve śaratprabhṛtibhyaḥ] ⟹ upaśarad-a; neuter [2.4.18]; the outer sup
after an a-final avyayībhāva → am [2.4.83 nāvyayībhāvād ato 'm tv apañcamyāḥ]
⟶ **upaśaradam**; the pañcamī branch keeps its own ending (*apañcamyāḥ*:
upaśaradāt), and 2.4.84 *tṛtīyāsaptamyor bahulam* makes 3 / 7 a *bahulam*
set {upaśaradam, upaśaradena / upaśarade} — recorded as such.

**W13 — dīrghasakthaḥ / dīrghasakthī** (ṣac). *dīrghe sakthinī yasya*;
[2.2.24] (vibhāṣā); ORD: the viśeṣaṇa first [2.2.35]; DEL = luk; SA = ṣac
[5.4.113 bahuvrīhau sakthyakṣṇoḥ svāṅgāt ṣac] (*svāṅgāt*: a body part — not
in *dīrghasakthi śakaṭam*, the cart's "thigh", where no ṣac is added: the
semantic guard of SA) ⟹ sakthi bha ⟹ i → ∅ [6.4.148] ⟹ dīrghasaktha; masc.
referent ⟶ **dīrghasakthaḥ**; feminine referent: ṣit ⟹ ṅīṣ [4.1.41] ⟹
**dīrghasakthī**. Two outputs, selected by the referent (L6).

**W14 — bahunadīkaḥ** (kap). *bahvyo nadyo yasmin* (deśe); [2.2.24]; ORD
[2.2.35: viśeṣaṇa first]; DEL = luk; SA = kap [5.4.153 nadyṛtaś ca] ⟹
bahunadī-ka; the ī is **not** shortened by 1.2.48 although nadī is
upasarjana and a strī-form — because after kap the compound no longer *ends*
in the strī-form (1.2.48 reads *upasarjanasya* with 1.1.72 *yena vidhis
tadantasya*: the hrasva is of a compound *ending* in go / strī); Kāśikā's
form is bahunadīkaḥ ⟶ **bahunadīkaḥ**. Open point recorded (§6): the
ordering "5.4.153 before 1.2.48" is here derived from 1.1.72, not from a
nipātana.

**W15 — upadaśāḥ** (ḍac). *daśānāṁ samīpe ye* (nine or eleven); [2.2.25
saṁkhyayā 'vyayāsannādūrādhikasaṁkhyāḥ saṁkhyeye]: the avyaya *upa* with the
number; SA = ḍac [5.4.73 bahuvrīhau saṁkhyeye ḍajabahugaṇāt]; ḍit ⟹ ṭi-lopa
[6.4.143 ṭeḥ] on daśan ⟹ daś + a ⟹ upadaśa; plural referent ⟶ **upadaśāḥ**.

**W16 — keśākeśi** (ic; one step open). *keśeṣu keśeṣu gṛhītvā idaṁ yuddhaṁ
pravṛttam*; [2.2.27 tatra tenedam iti sarūpe] (the two members are the same
word, in saptamī / tṛtīyā); SA = ic [5.4.127 ic karmavyatihāre] ⟹ keśa +
keśa + i; the long ā of the first member: the pinned text's 6.3.137
*anyeṣām api dṛśyate* (the *dṛśyate* clause under 6.3.? dīrgha) is the
tradition's licence for the lengthening; it is a *dṛśyate* (attested-form)
clause, so the ā is **declared from usage**, not derived ⟶ **keśākeśi**
(avyaya by 2.2.27's reading as a bahuvrīhi in *vyatihāra*; 1.1.41? no —
2.2.27's product is a bahuvrīhi, neuter by usage; recorded open).

**W17 — saputraḥ / sahaputraḥ** (6.3.82). *putreṇa saha* (āgataḥ); [2.2.28
tena saheti tulyayoge] (bahuvrīhi); ORD: *saha* first (the avyaya; 2.2.28
names *tena* in the nominative-of-the-vidhi? — it names the instrumental
member, so *saha* is the viśeṣaṇa, 2.2.35); DEL = luk; 6.3 uttarapada:
[6.3.82 vopasarjanasya] saha → sa optionally (*vā*) ⟹ **{saputraḥ,
sahaputraḥ}**; in a name the *sa* is nitya [6.3.78 sahasya saḥ saṁjñāyām].

Each derivation above is a path through §4; the eight that reach a
certified packet (W1, W8 via 104; W10 – W12 via 114's ṭac / am machinery)
are already machine-checked; the others are written derivations whose
every clause is quoted in §A and are the next certification targets (§8).

---

## 6. Explicit domains and open branches

What the pinned text decides, and what it does not:

| question | decided by | status |
|---|---|---|
| which pairs may compound | 2.1.1 guard + the clause list 2.1.5 – 2.2.29 | decided up to the gaṇa lists (rājadantādi 2.2.31, vāhitāgnyādi 2.2.37, śauṇḍādi 2.1.40, stokādi 6.3.2, śaratprabhṛti 5.4.107, uraḥprabhṛti 5.4.151) — the lists are **inputs** (PG1 pins the sūtrapāṭha, not the gaṇapāṭha) |
| the sense σ | — | **input** (2.1.6's list, 2.1.24's list, … are senses the speaker intends; the text licenses, it does not infer) |
| nitya / vibhāṣā / vā / na | position relative to 2.1.11 and the explicit words | decided |
| *bahulam* (2.1.32, 2.1.57, 2.4.84, 6.3.14) | the word *bahulam* | **not reducible** to a set without usage data; declared |
| upasarjana | 1.2.43, 1.2.44 | decided; L1 |
| order | 2.2.30 – 2.2.38 | decided, with 1.4.2 for the dvandva clash (W9) |
| sup deletion | 2.4.71 + 1.1.61 / 62 / 63; aluk list 6.3.1 – 24 | decided (the aluk list is finite in the text) |
| samāsānta | 5.4.68 – 5.4.160 | decided where the text says so; optional where *vibhāṣā* / *anyatarasyām*; the lists are inputs |
| gender / number | 2.4.1, 2.4.17 – 2.4.31, 2.4.26 | decided for avyayībhāva, dvigu, dvandva, tatpuruṣa; **input** (the referent) for bahuvrīhi (L6) |
| the ā of keśākeśi | 6.3.137 *dṛśyate* | attested-form clause: declared |
| niṣ- before k in W3 | 8.3.37 / 8.3.41 branch | not pulled in this packet; open |
| the uttarapada 6.3 rules (6.3.34 puṁvat, 6.3.42, 6.3.46, 6.3.67 mum, 6.3.73 nalopo nañaḥ, 6.3.74 tasmān nuḍ aci) | quoted in §A | only 6.3.46 certified (104); the rest are next targets |
| ekaśeṣa (1.2.64 *sarūpāṇām ekaśeṣa ekavibhaktau*, 1.2.65 – 73) | 1.2.64 ff. | **not a samāsa** (one form survives, no new prātipadika); outside this packet by the text's own placement |
| accent (6.1.223 *samāsasya*, 6.2.1 *bahuvrīhau prakṛtyā pūrvapadam*, 6.2.2) | 6.1.223 ff. | not claimed |

---

## 7. Claim boundary

```text
THE CONSTRUCTION (D1–D8), THE LEMMAS L1–L6, THE PROCEDURE §4 — EVERY CLAUSE QUOTED FROM THE PINNED SŪTRAPĀṬHA (§A)   STATED AND SOURCED
2.1.7 = yathā + a-sādṛśye; THE T114 SENSE LABEL CORRECTED (PIN UNCHANGED)                                               RESOLVED FROM THE PRIMARY TEXT
W1, W8, W10–W12 (VIA THEOREMS 104 / 114)                                                                                MACHINE-CHECKED EARLIER
W2–W7, W9, W13–W17                                                                                                      WRITTEN DERIVATIONS, NOT YET CERTIFIED (§8)
σ, THE REFERENT OF A BAHUVRĪHI, GAṆA MEMBERSHIP, bahulam                                                                 INPUTS (DECLARED)
CAUSATIVE PASSIVE, ṇic-LOPA, DOUBLE-KARMAN AGREEMENT                                                                     NOT TOUCHED (another branch owns them)
RH, YM                                                                                                                  UNTOUCHED
```

## 8. Certification plan (secondary, deferred)

One module `proof_lab/samasa_construction_compiled.py` realising §4 on the
seventeen worked derivations, with `ORD`, `DEL`, `SA` as separate
functions and the option algebra as a set-valued output; ablations per
clause as in 104. It is not written in this packet by instruction; the
packet's own check is §A: every sūtra number quoted here is verified
against the pinned sūtrapāṭha by `research/samasa_construction/verify_quotes.py`
(exact match of the transliterated pinned text with the quotation).

---

## A. Sources (quoted from the pinned sūtrapāṭha; IAST by the ledger's transliteration)

```text
2.1.1 samarthaḥ padavidhiḥ · 2.1.2 subāmantrite parāṅgavat svare · 2.1.3 prāk kaḍārāt samāsaḥ · 2.1.4 saha supā · 2.1.5 avyayībhāvaḥ
2.1.6 avyayaṁ vibhaktisamīpasamṛddhivyṛddhyarthābhāvātyayāsampratiśabdaprādurbhāvapaścādyathānupūrvyayaugapadyasādṛśyasampattisākalyāntavacaneṣu
2.1.7 yathāsādṛśye · 2.1.8 yāvadavadhāraṇe · 2.1.9 suppratinā mātrārthe · 2.1.10 akṣaśalākāsaṁkhyāḥ pariṇā · 2.1.11 vibhāṣā · 2.1.12 apaparibahirañcavaḥ pañcamyā · 2.1.13 āṅ maryādābhividhyoḥ
2.1.22 tatpuruṣaḥ · 2.1.23 dviguśca · 2.1.24 dvitīyā śritātītapatitagatātyastaprāptāpannaiḥ · 2.1.30 tṛtīyā tatkṛtārthena guṇavacanena · 2.1.32 kartṛkaraṇe kṛtā bahulam
2.1.36 caturthī tadarthārthabalihitasukharakṣitaiḥ · 2.1.37 pañcamī bhayena · 2.1.39 stokāntikadūrārthakṛcchrāṇi ktena · 2.1.40 saptamī śauṇḍaiḥ · 2.1.49 pūrvakālaikasarvajaratpurāṇanavakevalāḥ samānādhikaraṇena
2.1.51 taddhitārthottarapadasamāhāre ca · 2.1.52 saṁkhyāpūrvo dviguḥ · 2.1.57 viśeṣaṇaṁ viśeṣyeṇa bahulam · 2.1.61 sanmahatparamottamotkṛṣṭāḥ pūjyamānaiḥ
2.2.1 pūrvāparādharottaramekadeśinaikādhikaraṇe · 2.2.2 ardhaṁ napuṁsakam · 2.2.6 nañ · 2.2.8 ṣaṣṭhī · 2.2.10 na nirdhāraṇe · 2.2.17 nityaṁ krīḍājīvikayoḥ · 2.2.18 kugatiprādayaḥ · 2.2.19 upapadamatiṅ
2.2.23 śeṣo bahuvrīhiḥ · 2.2.24 anekamanyapadārthe · 2.2.25 saṁkhyayā'vyayāsannādūrādhikasaṁkhyāḥ saṁkhyeye · 2.2.26 diṅnāmānyantarāle · 2.2.27 tatra tenedamiti sarūpe · 2.2.28 tena saheti tulyayoge · 2.2.29 cārthe dvandvaḥ
2.2.30 upasarjanaṁ pūrvam · 2.2.31 rājadantādiṣu param · 2.2.32 dvandve ghi · 2.2.33 ajādyadantam · 2.2.34 alpāctaram · 2.2.35 saptamīviśeṣaṇe bahuvrīhau · 2.2.36 niṣṭhā · 2.2.37 vāhitāgnyādiṣu · 2.2.38 kaḍārāḥ karmadhāraye
1.2.42 tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ · 1.2.43 prathamānirdiṣṭaṁ samāsa upasarjanam · 1.2.44 ekavibhakti cāpūrvanipāte · 1.2.45 arthavadadhāturapratyayaḥ prātipadikam · 1.2.46 kṛttaddhitasamāsāśca · 1.2.47 hrasvo napuṁsake prātipadikasya · 1.2.48 gostriyorupasarjanasya · 1.2.64 sarūpāṇāmekaśeṣa ekavibhaktau
2.4.1 dvigurekavacanam · 2.4.2 dvandvaśca prāṇitūryasenāṅgānām · 2.4.17 sa napuṁsakam · 2.4.18 avyayībhāvaśca · 2.4.19 tatpuruṣo'nañ karmadhārayaḥ · 2.4.26 paravalliṅgaṁ dvandvatatpuruṣayoḥ · 2.4.29 rātrāhnāhāḥ puṁsi · 2.4.30 apathaṁ napuṁsakam · 2.4.31 ardharcāḥ puṁsi ca
2.4.71 supo dhātuprātipadikayoḥ · 2.4.82 avyayādāpsupaḥ · 2.4.83 nāvyayībhāvādato'mtvapañcamyāḥ · 2.4.84 tṛtīyāsaptamyorbahulam
1.1.41 avyayībhāvaśca · 1.1.46 ādyantau ṭakitau · 1.1.51 uraṇ raparaḥ · 1.1.61 pratyayasya lukślulupaḥ · 1.1.62 pratyayalope pratyayalakṣaṇam · 1.1.63 na lumatāṅgasya · 1.1.72 yena vidhistadantasya · 1.4.2 vipratiṣedhe paraṁ kāryam · 1.4.14 suptiṅantaṁ padam · 1.4.18 yaci bham · 1.4.21 bahuṣu bahuvacanam
5.4.68 samāsāntāḥ · 5.4.69 na pūjanāt · 5.4.71 nañastatpuruṣāt · 5.4.73 bahuvrīhau saṁkhyeye ḍajabahugaṇāt · 5.4.74 ṛkpūrabdhūḥpathāmānakṣe · 5.4.75 ac pratyanvavapūrvāt sāmalomnaḥ · 5.4.86 tatpuruṣasyāṅguleḥ saṁkhyāvyayādeḥ · 5.4.87 ahassarvaikadeśasaṁkhyātapuṇyācca rātreḥ · 5.4.89 na saṁkhyādeḥ samāhāre
5.4.91 rājāhassakhibhyaṣṭac · 5.4.92 gorataddhitaluki · 5.4.106 dvandvāccudaṣahāntāt samāhāre · 5.4.107 avyayībhāve śaratprabhṛtibhyaḥ · 5.4.108 anaśca · 5.4.109 napuṁsakādanyatarasyām · 5.4.113 bahuvrīhau sakthyakṣṇoḥ svāṅgāt ṣac · 5.4.127 ic karmavyatihāre
5.4.151 uraḥprabhṛtibhyaḥ kap · 5.4.153 nadyṛtaśca · 5.4.154 śeṣādvibhāṣā · 5.4.155 na saṁjñāyām
6.3.1 aluguttarapade · 6.3.2 pañcamyāḥ stokādibhyaḥ · 6.3.3 ojaḥsaho'mbhastamasaḥ tṛtīyāyāḥ · 6.3.4 manasaḥ saṁjñāyām · 6.3.7 vaiyākaraṇākhyāyāṁ caturthyāḥ · 6.3.9 haladantāt saptamyāḥ saṁjñāyām · 6.3.14 tatpuruṣe kṛti bahulam · 6.3.21 ṣaṣṭhyā ākrośe · 6.3.23 ṛto vidyāyonisambandhebhyaḥ · 6.3.24 vibhāṣā svasṛpatyoḥ
6.3.34 striyāḥ puṁvadbhāṣitapuṁskādanūṅ samānādhikaraṇe striyāmapūraṇīpriyā''diṣu · 6.3.42 puṁvat karmadhārayajātīyadeśīyeṣu · 6.3.46 ānmahataḥ samānādhikaraṇajātīyayoḥ · 6.3.67 arurdviṣadajantasya mum · 6.3.73 nalopo nañaḥ · 6.3.74 tasmānnuḍaci · 6.3.78 sahasya saḥ saṁjñāyām · 6.3.82 vopasarjanasya · 6.3.137 anyeṣāmapi dṛśyate
6.4.143 ṭeḥ · 6.4.144 nastaddhite · 6.4.148 yasyeti ca · 6.1.77 iko yaṇaci · 6.1.87 ādguṇaḥ · 6.1.101 akaḥ savarṇe dīrghaḥ · 6.1.223 samāsasya · 6.2.1 bahuvrīhau prakṛtyā pūrvapadam
7.1.24 ato'm · 8.2.7 nalopaḥ prātipadikāntasya · 8.3.45 nityaṁ samāse'nuttarapadasthasya · 8.3.59 ādeśapratyayayoḥ · 8.4.41 ṣṭunā ṣṭuḥ · 4.1.15 ṭiḍḍhāṇañdvayasajdaghnañmātractayapṭhakṭhañkañkvarapaḥ · 4.1.41 ṣidgaurādibhyaśca · 4.1.76 taddhitāḥ · 2.3.1 anabhihite · 2.3.50 ṣaṣṭhī śeṣe
```

Commentary examples (not from the pinned text, marked as such in the body):
Kāśikā on 2.1.7 (yathāśakti, yathāgṛham, yathāvidhi), on 2.1.1 (the
Mahābhāṣya's *bhāryā rājñaḥ puruṣo Devadattasya*), on 2.2.31 – 38, 5.4.73 –
153 and 6.3.2 – 9 for the illustrative words; every *rule* cited is the
pinned text.
