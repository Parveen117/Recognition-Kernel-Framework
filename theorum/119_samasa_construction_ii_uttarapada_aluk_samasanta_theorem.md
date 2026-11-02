# Samāsa Construction II — the review resolved (inherited nityam, the pre-sup upapada carrier, 8.3.95, 8.2.39 jaśtva, the ordering relation); the 6.3 uttarapada and aluk families; selected samāsānta families; the native carrier for compounding (owned constituents, typed cuts, retained history, pairing, exact zero-specialization)

2 November 2026. Additive to theorum/118 (whose text and §A are preserved
unchanged); every clause here is quoted from the pinned sūtrapāṭha (§A,
machine-checked by `research/samasa_construction/verify_quotes.py`, which
now covers both capsules). Commentary attributions are marked as such.
Python certificates remain deferred (§8).

---

## 0. Review resolution (the PG15 source review of T118, `research/panini_grammar/causative_passive/T118_SOURCE_REVIEW.md`)

None of the five findings was already fixed in an earlier commit; they are
resolved **here** (this packet's commit), T118 untouched.

| finding | status | resolution |
|---|---|---|
| C1 2.1.7 attribution | accepted | §1 of T118 stands; the segmentation *yathā + asādṛśye* is **the commentaries'** (Kāśikā *asādṛśye vartamānam*; Bālamanoramā *asādṛśye iti chedaḥ*), the pinned sūtrapāṭha alone gives the unsegmented word; the sense list is Bālamanoramā's, Kāśikā's own examples being yathāvṛddham / yathādhyāpakam. Recorded in §1 below. |
| C2 inherited nityam; pre-sup upapada inputs | **resolved** | §1: the mode function takes anuvṛtti (2.2.17 *nityam* runs into 2.2.18, 2.2.19, Kāśikā *nityam iti vartate*); the carrier D1 is widened to admit pre-sup inputs for the gati / kāraka / upapada class (the vārttika read by Kāśikā under 2.2.19), with a typed flag. W3 of T118 is re-labelled nitya and re-derived as W3′. |
| C3 yudhiṣṭhira's ṣatva | **resolved** | §2: 8.3.95 *gaviyudhibhyāṁ sthiraḥ* is the licence (the s of *sthira* is neither ādeśa nor pratyaya, so 8.3.59 cannot act); then 8.4.41. W5′. |
| C4 stokāt + mukta | **resolved** | §2: the retained pada-final t takes 8.2.39 jaśtva (d) and 8.4.45 gives the nasal **optionally**: {stokānmukta, stokādmukta}; the earlier *stokātmukta* was wrong. W6′. 6.3.2's number qualification recorded as Kāśikā's. |
| C5 ORD as a relation; indrāgnī | **resolved** | §3: ORD is a **relation** with branch labels; *indrāgnī* is Kāśikā's 2.2.33-over-2.2.32 case (2.2.33 later than 2.2.32); no pinned conflict example for 2.2.33 vs 2.2.34 is claimed — both orders retained as branches until a source is pinned. W9′. |
| C5 native carrier, pairing, zero-specialization | **provided** | §6: the compounding events as an instance of PG14's S-state and N1–N5 carrier; Theorem N4 applies verbatim; the exact-branch-recovery example is the C4 pair. |

---

## 1. Mode with anuvṛtti; the widened carrier (C2)

**Mode is a function of the text *with* anuvṛtti.** T118 L5 located *nitya*
by the position of 2.1.11 and by a local *nityam*. The correct statement:

> MODE(c) = the modal word in force at c — the adhikāra *vibhāṣā* (2.1.11)
> unless a nearer clause supplies *nityam* / *vā* / *na* **by anuvṛtti**.

2.2.17 *nityaṁ krīḍājīvikayoḥ* supplies *nityam*, and Kāśikā begins 2.2.18
*kugatiprādayaḥ* and 2.2.19 *upapadam atiṅ* with *nityam iti vartate*. So
the gati / prādi and upapada compounds are **nitya**: the vigraha with the
same words is not a licensed sentence (*niṣkauśāmbiḥ*, *kumbhakāraḥ* — not
**niṣkrāntaḥ kauśāmbyāḥ* with those words in that sense, not **kumbhaṁ
kāraḥ*). T118's W3 label "vibhāṣā" is withdrawn; the licensed set is
{niṣkauśāmbiḥ}.

**The carrier is widened.** 2.1.4 *saha supā* describes the ordinary
input: two sup-ending padas. Kāśikā on 2.2.19 reads the vārttika
*gatikārakopapadānāṁ kṛdbhiḥ saha samāsavacanaṁ prāk subutpatteḥ*: the
gati / kāraka / upapada member compounds with the kṛt-form **before the sup
is produced**. D1 therefore gets a typed flag:

```
pada record  p = (π, v, n, g)        v ∈ {1..7}            ordinary input (2.1.4)
             p = (π, ⊥, –, –)         v = ⊥ (pre-sup)       gati / kāraka / upapada input (2.2.18, 2.2.19; vārttika under 2.2.19)
```

A pre-sup input never meets 2.4.71 (there is no sup to delete) and never
meets 1.1.62 / 1.1.63 for that sup; its pada-status for 8.2.7-type rules
comes from 1.4.14 only if it is a tiṅ / sup form — a *kāraka* word like
*kumbha* in *kumbhakāra* is **not** a pada at the junction, which is why
no pada-final rule fires there. This is the typed distinction the review
asked for; T118's D1 is not withdrawn for the sup-bearing classes.

**W3′ — niṣkauśāmbiḥ (nitya, pre-sup).** [2.2.18] (mode: *nityam* by
anuvṛtti from 2.2.17); input (nis, ⊥) + (kauśāmbī, 5 fixed) — the second
member is sup-bearing with the fixed pañcamī of the vigraha, so [1.2.44
ekavibhakti cāpūrvanipāte] makes it upasarjana without first placement;
ORD: the gati first (2.2.18 names the prādi in the nominative, 1.2.43);
DEL(ṅasi) = luk [2.4.71]; [1.2.48 gostriyor upasarjanasya] → kauśāmbi;
the s of *nis* before k: 8.3.37 / 8.3.41 (not pulled; still open) ⟶
**niṣkauśāmbi** + su ⟶ niṣkauśāmbiḥ; licensed set {niṣkauśāmbiḥ}.

**W18 — kumbhakāraḥ (upapada, pre-sup).** *kumbham karoti* ⟶ [3.2.1
karmaṇy aṇ: kumbha is the upapada karman]; [2.2.19 upapadam atiṅ] (nitya):
(kumbha, ⊥) + (kāra, ⊥) compound before any sup; the upapada first [2.2.30,
2.2.19 names *upapadam* in the nominative]; no 2.4.71 event (nothing to
delete) — the construction records **no luk event** here, which is the
observable difference from W1; 1.2.46; then su ⟶ **kumbhakāraḥ**. (3.2.1
not pulled into §A; the upapada mechanism is the point, the kṛt affix is
theorum/107's domain.)

**1.1 — the 2.1.7 attribution, precisely (C1).** Pinned sūtrapāṭha:
*yathāsādṛśye* (unsegmented). Kāśikā: *asādṛśye vartamānam*, examples
yathāvṛddham, yathādhyāpakam, excluded *yathā Devadattas tathā Yajñadattaḥ*.
Bālamanoramā: *asādṛśye iti chedaḥ*, senses yogyatā, vīpsā,
padārthānativṛtti. T118 §1's table is retained with this attribution;
the quote-checker verifies the sūtrapāṭha word only.

---

## 2. Two rule witnesses repaired (C3, C4)

**W5′ — yudhiṣṭhiraḥ.** *yudhi sthiraḥ*; saptamī-tatpuruṣa licensed by
the name clause [6.3.9 haladantāt saptamyāḥ saṁjñāyām] (Kāśikā places the
word there; nitya in the name sense); ORD: saptamī first; DEL(ṅi) = **aluk**
[6.3.9]; the s of *sthira* is lexical — neither an ādeśa nor a pratyaya —
so [8.3.59 ādeśapratyayayoḥ] is **silent**; the ṣatva is the named rule
[8.3.95 gaviyudhibhyāṁ sthiraḥ] (Kāśikā: gaviṣṭhiraḥ, yudhiṣṭhiraḥ); then
[8.4.41 ṣṭunā ṣṭuḥ] th → ṭh ⟶ **yudhiṣṭhira** + su. T118 L4's sentence
"8.3.59 runs across the frozen ṅi" is withdrawn; L4's *content* (aluk keeps
the sup inside one prātipadika) stands, now witnessed by 8.3.95's own
wording *yudhi-bhyām*: the rule names the locative form, i.e. the aluk
compound.

**W6′ — stokānmuktaḥ / stokādmuktaḥ.** *stokāt muktaḥ*; [2.1.39] (vibhāṣā);
pañcamī first; DEL(ṅasi) = **aluk** [6.3.2 pañcamyāḥ stokādibhyaḥ]; the
retained -āt is pada-final (1.4.14 with the sup present) ⟹ [8.2.39 jhalāṁ
jaśo 'nte] t → d; before m no [8.4.55 khari ca] (m is not khar) ⟹ d stands;
[8.4.45 yaro 'nunāsike 'nunāsiko vā]: d → n **optionally** ⟹ licensed set
**{stokānmuktaḥ, stokādmuktaḥ}** (Kāśikā 6.3.2 prints stokānmuktaḥ; its
8.4.45 examples contrast nasal / voiced stop). T118's *stokātmukta* is
withdrawn: the non-nasal branch is the jaś form. Kāśikā's number
qualification on 6.3.2 (the stokādi words in this use are singular) is
recorded as commentary; the pinned sūtra carries no number word.

---

## 3. The ordering relation (C5)

ORD is a **relation** `ORD ⊆ Class × Pair × Order × Label`, not a function:

```
(class, {m₁,m₂}, m₁≺m₂, "2.2.30")   when m₁ is upasarjana (1.2.43 / 1.2.44) and no later clause applies
(tatpuruṣa, …, m₂≺m₁, "2.2.31")     in the rājadantādi gaṇa (input list)
(dvandva, …, ghi≺other, "2.2.32")
(dvandva, …, ajādi-adanta≺other, "2.2.33")
(dvandva, …, fewer-vowels≺more, "2.2.34")
(bahuvrīhi, …, saptamī/viśeṣaṇa≺other, "2.2.35")
(bahuvrīhi, …, niṣṭhā≺other, "2.2.36")
(bahuvrīhi, …, either, "2.2.37 vā")  in the vāhitāgnyādi gaṇa
(karmadhāraya, …, either, "2.2.38")  for the kaḍāra words
```

**Tie policy.** When two of 2.2.32 / 2.2.33 / 2.2.34 apply to one pair, the
text's own instrument is 1.4.2 *vipratiṣedhe paraṁ kāryam*; the **pinned
conflict example** is Kāśikā's under 2.2.33: *indrāgnī* — agni is ghi
(2.2.32 would place it first), indra is vowel-initial a-final (2.2.33),
and 2.2.33 wins. For 2.2.33 vs 2.2.34 no conflict example is pinned here;
the relation **keeps both orders as labelled branches** for such a pair
until a source is pinned. T118 W9's sentence attributing *indrāgnī* to
2.2.34-over-2.2.33 is withdrawn.

**W9′ — indrāgnī.** *indraś cāgniś ca* (devatādvandva); [2.2.29]; ORD:
branch "2.2.33" (indra first) over branch "2.2.32" (agni first) by 1.4.2;
DEL = luk; [6.3.26 devatādvandve ca] with [6.3.25 ānaṅ ṛto dvandve]: ānaṅ
to the first member (1.1.53 ṅic ca: replaces the final sound) ⟹ indrān ⟹
pada-final n → ∅ [8.2.7 via 1.1.62] ⟹ indrā; dual by the two referents;
the ī of *agnī*: [7.1.? the dual ending with 6.1.102 prathamayoḥ
pūrvasavarṇaḥ on agni + au] — theorum/91's ghi carrier ⟶ **indrāgnī**.

---

## 4. The 6.3 uttarapada and aluk families — written derivations

Each row: the clause (pinned), the operation on the typed state, the
witness word (Kāśikā unless certified earlier), the open step if any.

### 4.1 Aluk (6.3.1 *aluguttarapade* — 6.3.24)

| clause | sup kept | witness | derivation |
|---|---|---|---|
| 6.3.2 pañcamyāḥ stokādibhyaḥ | ṅasi | stokānmuktaḥ / stokādmuktaḥ | W6′ |
| 6.3.3 ojaḥsaho'mbhastamasaḥ tṛtīyāyāḥ | ṭā | ojasākṛtam, sahasākṛtam, ambhasākṛtam, tamasākṛtam | ojas + ṭā (= ā after the s-stem, 7.3.? none) kept; kṛta [3.2.102 niṣṭhā]; neuter by the referent |
| 6.3.4 manasaḥ saṁjñāyām | ṭā | (name; example not pinned here) | open |
| 6.3.7 vaiyākaraṇākhyāyāṁ caturthyāḥ; 6.3.8 parasya ca | ṅe | **ātmanepadam**, **parasmaipadam** | ātman + ṅe (ātmane) kept; para + ṅe → [7.1.14 sarvanāmnaḥ smai] parasmai, kept by 6.3.8; + pada — the grammar's own technical terms are aluk compounds |
| 6.3.9 haladantāt saptamyāḥ saṁjñāyām | ṅi | yudhiṣṭhiraḥ, kaṇṭhekālaḥ | W5′, T118 W4 |
| 6.3.10 kāranāmni ca prācāṁ halādau | ṅi | (prācām: Eastern usage; declared) | open |
| 6.3.14 tatpuruṣe kṛti bahulam | ṅi (bahulam) | stambekarmaṇaḥ (Kāśikā) | bahulam: declared |
| 6.3.21 ṣaṣṭhyā ākrośe | ṅas | caurasyakulam | caura + ṅas (caurasya, 7.1.12 ṭāṅasiṅasām inātsyāḥ) kept in abuse |
| 6.3.23 ṛto vidyāyonisambandhebhyaḥ | ṅas | hotur antevāsī-type (Kāśikā) | hotṛ + ṅas → hotur (7.3.110? no: 6.1.111 ṛta ut + 8.2.66 ru) kept; 8.2.66 / 8.3.15 give hotuḥ at pause, *hotur* before a vowel (6.1.113 / 6.1.114 branch) |
| 6.3.24 vibhāṣā svasṛpatyoḥ | ṅas (vā) | {pituḥṣvasā, pitṛṣvasā} with 8.3.84 mātṛpitṛbhyāṁ svasā (ṣatva) | the *vā* gives a two-element set; 8.3.84 applies on both |

**Mathematical content.** ALUK is a finite partial function on (sup,
first member, condition) → {keep}; outside it DEL = luk. Its rows are
*additive* over the luk default: no row changes a luk result elsewhere.

### 4.2 Dvandva: ānaṅ and the devatā-dvandva (6.3.25 – 6.3.33)

| clause | operation | witness | derivation |
|---|---|---|---|
| 6.3.25 ānaṅ ṛto dvandve | ṛ-final first member → ānaṅ (1.1.53: the final al) | hotāpotārau | hotṛ → hotān [6.3.25] → hotā [8.2.7 via 1.1.62, pada-final n] + potṛ + au (theorum/90's ṛ-carrier: potārau) |
| 6.3.25 + 6.3.32 mātarapitarāv udīcām | option by dialect | {mātāpitarau, mātarapitarau} | the Northern branch keeps *mātara-* (6.3.32: *udīcām*) — a dialect-labelled branch, recorded as such |
| 6.3.26 devatādvandve ca | ānaṅ to the first deity name | mitrāvaruṇau, indrāgnī (W9′) | mitra → mitrān → mitrā [8.2.7] + varuṇa + au |
| 6.3.27 īd agneḥ somavaruṇayoḥ | agni → agnī before soma / varuṇa | agnīṣomau | agni → agnī (ī replaces the final i, 1.1.52) + soma; [8.3.82 agneḥ stutstomasomāḥ] s → ṣ ⟹ agnīṣomau; agnīvaruṇau (no ṣatva: varuṇa has no s) |
| 6.3.29 divo dyāvā; 6.3.30 divasaś ca pṛthivyām | div → dyāvā / divas before pṛthivī | dyāvāpṛthivī, divaspṛthivī | two labelled branches (6.3.30 *ca*) |
| 6.3.31 uṣāsoṣasaḥ | uṣas → uṣāsa | uṣāsānaktam-type | Vedic; recorded |

### 4.3 Puṁvadbhāva (6.3.34 – 6.3.41)

| clause | operation | witness | derivation |
|---|---|---|---|
| 6.3.34 striyāḥ puṁvad bhāṣitapuṁskād anūṅ samānādhikaraṇe striyām apūraṇīpriyādiṣu | the feminine first member (whose masculine exists, not ūṅ-ending) takes the masculine form before a samānādhikaraṇa feminine uttarapada | darśanīyabhāryaḥ (bahuvrīhi: *darśanīyā bhāryā yasya*) | darśanīyā → darśanīya [6.3.34] + bhāryā; the compound then masculine by the referent; the **guards**: bhāṣitapuṁska (a masculine *darśanīya* exists), anūṅ (not *vadhū*-type), samānādhikaraṇa, striyām, not pūraṇī / priyādi |
| 6.3.35 tasilādiṣv ākṛtvasucaḥ | likewise before tasil … kṛtvasuc | (feminine + tasil → masculine base) | the adverbs of theorum/113 from a feminine base: input recorded |
| 6.3.37 na kopadhāyāḥ | **blocked** for a feminine with k as penultimate | pācikābhāryaḥ (the ā stays) | pācikā (theorum/111) + bhāryā: 6.3.37 vetoes 6.3.34 ⟹ pācikā-bhāryaḥ |
| 6.3.42 puṁvat karmadhārayajātīyadeśīyeṣu | masculine form before a karmadhāraya uttarapada and before jātīya / deśīya | paṭujātīyā, mṛdujātīyā | paṭvī → paṭu [6.3.42] + jātīya + ṭāp |
| 6.3.43 gharūpakalpacelaḍbruvagotramatahateṣu ṅyo 'nekāco hrasvaḥ | the ṅī of a polysyllable → short before gha / rūpa / kalpa / … | brāhmaṇitarā, brāhmaṇirūpā, brāhmaṇikalpā | brāhmaṇī + tarap (gha, 1.1.22) → ī → i [6.3.43] |
| 6.3.46 ān mahataḥ samānādhikaraṇajātīyayoḥ | mahat → mahā | mahārājaḥ (certified, theorum/104) | — |

**Mathematical content.** Puṁvadbhāva is a *substitution event* on the
owner "first member's feminine affix": its observation changes (ṭāp / ṅīp
→ the masculine form) while the owner and the original (O) are retained —
exactly PG14's rule that it-lopa and substitution change observation, not
ownership (§6). 6.3.37 is a prohibition event on the same owner, guarded by
the penultimate k.

### 4.4 Nañ, mum, ku, the sarvanāma before dṛś / vatu (6.3.67 – 6.3.104)

| clause | operation | witness | derivation |
|---|---|---|---|
| 2.2.6 nañ; 6.3.73 nalopo nañaḥ | nañ + x: the n of *na* dropped | abrāhmaṇaḥ | na (ñ it, 1.3.3) + brāhmaṇa → [6.3.73] a-brāhmaṇa; gender by 2.4.26 |
| 6.3.74 tasmān nuḍ aci | nuṭ to the vowel-initial uttarapada after the n-less nañ | anaśvaḥ | a + aśva → [6.3.74] a + n(uṭ) + aśva ⟹ anaśva (ṭit → initial, 1.1.46) |
| 5.4.71 nañas tatpuruṣāt (prohibition) | no samāsānta after a nañ-tatpuruṣa | arājā | a + rājan: 5.4.91's ṭac **blocked** [5.4.71] ⟹ arājan declined on theorum/92: arājā, arājānau …; 5.4.72 patho vibhāṣā reopens the option for pathin: {apathaḥ, apanthāḥ} with 2.4.30 apathaṁ napuṁsakam |
| 3.2.43 meghartibhayeṣu kṛñaḥ; 6.3.67 arurdviṣadajantasya mum | khac after kṛ with bhaya as upapada; mum to the vowel-final upapada | bhayaṅkaraḥ | bhaya (⊥, upapada, W18-type) + kṛ + khac (kh 1.3.8, c 1.3.3 → a; the ṅ-… ) → kara; [6.3.67] mum after the last vowel of bhaya (1.1.47) ⟹ bhayam-kara ⟹ [8.3.23 mo 'nusvāraḥ] ⟹ [8.4.58 anusvārasya yayi parasavarṇaḥ] ⟹ **bhayaṅkaraḥ** |
| 6.3.101 koḥ kat tatpuruṣe 'ci | ku → kat before a vowel-initial uttarapada | kadannam | ku + anna → [6.3.101] kat + anna ⟹ kadanna (8.2.39 t → d before the vowel? — no: *kat* + a: the t is not pada-final inside the compound… it is: ku is a pada by 1.1.62 ⟹ 8.2.39 jaś ⟹ kad-anna) ⟹ kadannam (neuter, anna) |
| 6.3.104 kā pathyakṣayoḥ | ku → kā before pathin / akṣi | kāpathaḥ, kākṣaḥ | ku + pathin → kā + pathin + a [5.4.74] ⟹ kāpathaḥ |
| 6.3.107 kavaṁ coṣṇe | ku → kava **and** kat before uṣṇa | {kavoṣṇam, kadoṣṇam} | *ca* keeps 6.3.101's kat: two branches |
| 6.3.89 dṛgdṛśavatuṣu; 6.3.91 ā sarvanāmnaḥ | the sarvanāma's final → ā before dṛś / dṛśa / vatu | tādṛśaḥ, tādṛk, yādṛśaḥ, tāvat, etāvat | tad + kañ [3.2.60 tyadādiṣu dṛśo 'nālocane kañ ca] on dṛś: tad → ta [7.2.102 tyadādīnām aḥ, 6.1.97] → tā [6.3.91] + dṛś + a ⟹ **tādṛśaḥ**; with kvin: tā + dṛś + kvin ⟹ [8.2.62 kvinpratyayasya kuḥ] ś → k ⟹ **tādṛk**; tad + vatup [5.2.39 yattadetebhyaḥ parimāṇe vatup] ⟹ tā + vat ⟹ **tāvat** (declined by theorum/109) |
| 6.3.90 idaṅkimor īśkī | idam → ī, kim → kī before dṛś / vatu | īdṛśaḥ, kīdṛśaḥ | idam → ī [6.3.90] + dṛś + a; kim → kī + dṛś + a; kim + vatu: [5.2.40 kimidaṁbhyāṁ vo ghaḥ] gives *kiyat* / *iyat* with the gh-form — recorded, not derived here |
| 6.3.109 pṛṣodarādīni yathopadiṣṭam | the listed words as taught | pṛṣodaram, balāhakaḥ | a declared list (nipātana) |

### 4.5 The dīrgha family under 6.3.114 *saṁhitāyām* (6.3.115 – 6.3.136)

| clause | operation | witness | derivation |
|---|---|---|---|
| 6.3.115 karṇe lakṣaṇasyāviṣṭāṣṭapañcamaṇibhinnachinnachidrasruvasvastikasya | a mark-word lengthened before karṇa (not viṣṭa, aṣṭa, …) | dātrākarṇaḥ | dātra + karṇa → dātrā-karṇa [6.3.115] (bahuvrīhi: the animal with a sickle-mark on its ear) |
| 6.3.116 nahivṛtivṛṣivyadhirucisahitaniṣu kvau | the upapada lengthened before nah / vṛt / … + kvip | upānat, parīvṛt | upa + nah + kvip → upā-nah [6.3.116] ⟹ [8.2.34 naho dhaḥ] h → dh ⟹ upānadh ⟹ [8.2.39] jaś d ⟹ [8.4.56 vāvasāne] **upānat** / upānad at pause |
| 6.3.117 vanagiryoḥ saṁjñāyāṁ koṭarakiṁśulakādīnām | koṭara-list lengthened before vana / giri in a name | koṭarāvaṇam | koṭara + vana → koṭarā-vaṇa (ṇatva by 8.4.2 across the ā: r…ṇ) |
| 6.3.119 matau bahvaco 'najirādīnām | a polysyllable lengthened before matup | udumbarāvatī | udumbara + matup → [8.2.9] vat (m → v after a) → udumbarā-vat [6.3.119] + ṅīp [4.1.6] ⟹ udumbarāvatī (theorum/111's path) |
| 6.3.122 upasargasya ghañy amanuṣye bahulam | an upasarga lengthened before a ghañ-form (not of a person; bahulam) | (bahulam: declared) | open |
| 6.3.123 ikaḥ kāśe | an upasarga's ik lengthened before kāśa | nīkāśaḥ, vīkāśaḥ | ni + kāśa [3.3.18 ghañ on kāś] → nī-kāśa [6.3.123] |
| 6.3.128 viśvasya vasurāṭoḥ | viśva lengthened before vasu / rāj | viśvāvasuḥ, viśvārāṭ | viśva + vasu → viśvā-vasu [6.3.128] |
| 6.3.137 anyeṣām api dṛśyate | lengthening *attested* elsewhere | keśākeśi (T118 W16) | *dṛśyate* clause: attested-form licence, declared |

**Mathematical content.** The dīrgha family is one operator *D* (lengthen
the first member's final vowel) with a finite guard table; 6.3.137 is the
guard "attested", which the construction records as an input, not a rule
it can discharge.

---

## 5. Selected samāsānta families — written derivations

### 5.1 ṭac (5.4.86 – 5.4.92, 5.4.106 – 5.4.109)

| witness | clause chain |
|---|---|
| dvyaṅgulam | T118 W10 |
| sarvarātraḥ | sarva + rātri (samāhāra, 2.1.51 / 2.1.52-type with 2.1.49's sarva) → ṭac [5.4.87 ahassarvaikadeśasaṁkhyātapuṇyāc ca rātreḥ] ⟹ rātri bha ⟹ i → ∅ [6.4.148] ⟹ sarvarātra; gender [2.4.29 rātrāhnāhāḥ puṁsi] masculine ⟹ **sarvarātraḥ** |
| paramāhaḥ | parama + ahan (karmadhāraya) → ṭac [5.4.91 rājāhassakhibhyaṣ ṭac] ⟹ [6.4.144 nas taddhite] ṭi (an) → ∅ ⟹ param-ah-a ⟹ **paramāhaḥ** (6.1.101 a + a → ā); likewise **rājasakhaḥ** (sakhi + ṭac, 6.4.148) |
| mahārājaḥ, pañcagavam | certified (theorum/104, 114) |
| vāktvacam | vāc + tvac (samāhāra dvandva; both end in c = cu) → ṭac [5.4.106 dvandvāc cudaṣahāntāt samāhāre] ⟹ vāk-tvac-a (8.2.30 coḥ kuḥ on the pada-final c of vāc → k; 8.4.55) ⟹ neuter [2.4.17] + am [7.1.24] ⟹ **vāktvacam** |
| upaśaradam | T118 W12 |
| upacarmam / upacarma | upa + carman (avyayībhāva) → ṭac [5.4.108 anaś ca] ⟹ [6.4.144] carm-a ⟹ upacarma; + am [2.4.83] ⟹ upacarmam; **and** [5.4.109 napuṁsakād anyatarasyām]: carman being neuter, the ṭac is optional ⟹ {upacarmam, upacarma} — the second with 2.4.82's luk after the an-final avyaya |
| arājā | ṭac **blocked** [5.4.71] (§4.4) |

### 5.2 a / ac (5.4.74 – 5.4.75), ḍac (5.4.73), ṣac (5.4.113), ic (5.4.127)

| witness | clause chain |
|---|---|
| ardharcaḥ / ardharcam | T118 W11 |
| rājapathaḥ | rājan + pathin (2.2.8) → a [5.4.74 ṛkpūrabdhūḥpathām ānakṣe] ⟹ pathin bha [1.4.18] ⟹ [6.4.144 nas taddhite] ṭi (in) → ∅ ⟹ path-a; the first member: rājan pada-final n → ∅ [8.2.7] ⟹ **rājapathaḥ** |
| anulomam | anu + loman (2.1.6, avyayībhāva? — no: 5.4.75 names *prati / anu / ava* before *sāman / loman*: the compound is an avyayībhāva in anu-) → ac [5.4.75 ac pratyanvavapūrvāt sāmalomnaḥ] ⟹ [6.4.144] lom-a ⟹ anuloma; neuter [2.4.18]; + am [2.4.83] ⟹ **anulomam** |
| upadaśāḥ | T118 W15 (ḍac, 6.4.143) |
| dīrghasakthaḥ / -sakthī | T118 W13 (ṣac) |
| jalajākṣaḥ / jalajākṣī | jalaja + akṣi (bahuvrīhi, *jalaje iva akṣiṇī yasya*) → ṣac [5.4.113] (akṣi as body part) ⟹ akṣi bha ⟹ i → ∅ [6.4.148] ⟹ jalajākṣa (6.1.101 a + a → ā); fem. ṅīṣ [4.1.41, ṣit] ⟹ **jalajākṣī** |
| keśākeśi | T118 W16 (ic; the ā by 6.3.137, declared) |

### 5.3 kap (5.4.151 – 5.4.155)

| witness | clause chain |
|---|---|
| bahunadīkaḥ | T118 W14: kap [5.4.153 nadyṛtaś ca]; 1.2.48 does not shorten the ī because the compound no longer *ends* in the strī-form (1.1.72) |
| bahukartṛkaḥ | bahu + kartṛ (bahuvrīhi) → kap [5.4.153, *ṛtaḥ*] ⟹ **bahukartṛkaḥ** (no 7.3.110 ṛ → ar: kap is not ṅi / sarvanāmasthāna) |
| bahuyavaḥ / bahuyavakaḥ | bahu + yava → kap optional [5.4.154 śeṣād vibhāṣā] ⟹ {bahuyavaḥ, bahuyavakaḥ} |
| bahuyavo (nāma) | in a name kap is **blocked** [5.4.155 na saṁjñāyām] ⟹ {bahuyavaḥ} |
| vyūḍhoraskaḥ | vyūḍha + uras → kap [5.4.151 uraḥprabhṛtibhyaḥ kap]; uras is a pada before kap (1.4.17 *svādiṣu*: kap lies in the sv-ādi span 4.1.2 – 5.4.151) ⟹ s → ru [8.2.66] ⟹ visarga [8.3.15] ⟹ the s before k: **open** — 8.3.46 names kṛ / kami / kaṁsa / … not kap, and the kaskādi list (8.3.48) is not pinned here; the attested form is Kāśikā's, the witness rule not yet identified in the pinned text |

**Mathematical content.** SA(kap) carries the richest option structure in
the map: obligatory (5.4.151 – 153), optional (5.4.154), blocked (5.4.155);
it is the model case for D4's *set-valued* output.

---

## 6. The native carrier for compounding (owned constituents, typed cuts, retained history, pairing, exact zero-specialization)

This section places the samāsa construction inside the carrier of
`research/panini_grammar/grammar_construction/` (PG14, N1–N6; S1–S6)
**additively**: no shared engine is changed, no second engine is created.

**6.1 State.** A compounding state is PG14's
`s = (L, F, K, V, P, M, O, H, Q)` with the nominal reading of the slots:

- `L`: the lexical IDs of the two (or more) members, their teaching forms
  (e.g. *rājan*, *stokāt* with its pinned sup), gaṇa memberships as
  **inputs**;
- `F`: the vigraha as an interpreted frame — the dependency relation R of
  T118 D2 lives here, as does the intended sense σ and, for a bahuvrīhi,
  the referent (L6);
- `K`: the kāraka that assigned each member's vibhakti (2.3.x);
- `V`: unused for nominals (no lakāra); `P`: the compound's gender /
  number decision (D6) and the pada / bha status of each member;
- `M`: the constituent tree with **stable owners**: `member₁.prātipadika`,
  `member₁.sup`, `member₂.prātipadika`, `member₂.sup`, `samāsānta`,
  `outer.sup`, each augment (nuṭ, mum, ānaṅ, num) as its own owner;
- `O`: the pinned originals (the sūtrapāṭha words, the Kāśikā witness);
- `H`: the ordered event history; `Q`: open obligations (§7).

**6.2 Owned constituents and the two deletion laws.** Sup-luk (2.4.71) is
an **event on the owner `member.sup`**: its observation becomes empty
(1.1.60 *adarśanaṁ lopaḥ*), the owner stays. This is exactly S2's rule for
it-lopa ("adds an event and changes the observation of a marker; it does
not remove its owner"), applied to a whole affix. 1.1.62 and 1.1.63 are
then **visibility laws on guards**:

```
guard kind                        sees the luk-deleted owner?    clause
pada-conditioned (8.2.7, 8.2.66…)  yes                             1.1.62 pratyayalope pratyayalakṣaṇam
aṅga-conditioned (7.3.102, 7.1.9…) no                              1.1.63 na lumatāṅgasya
```

Aluk (6.3.2 – 24) is the **absence** of that event on the listed owners;
the owner's observation is unchanged and later guards (8.3.95, 8.2.39)
read it as any other sound. Substitution events (puṁvat 6.3.34, ānaṅ
6.3.25, kat 6.3.101, dīrgha 6.3.115 ff.) change an owner's value and keep
its ancestry in O; augment events (nuṭ 6.3.74, mum 6.3.67, num 7.1.70)
**create** owners (S2: "substitution and augment insertion are different
constructors").

**6.3 Events.** The typed events of compounding, each carrying rule ID,
source occurrence, inherited scope (the anuvṛtti of *nityam* / *vibhāṣā* —
§1), guard evidence, branch label, affected owners, old / new values,
visibility interpretation, consumed events:

`SAM(c, mode)` (class + modal branch) · `UPA` (1.2.43 / 1.2.44) ·
`ORD(label)` (§3 relation; a branch per label) · `LUK(owner)` / `ALUK(owner, clause)`
· `UTT(clause)` (6.3 substitutions, prohibitions, augments) · `SA(affix | ∅, mode)`
· `CAT` (1.2.46; D6; 1.1.41) · `SUP(outer)`.

Every history in §4 – §5 is a finite word in these events; the licensed
set of D4 is the set of **terminal histories**, and two histories that
print the same word (e.g. *upacarma* via 2.4.82 after the 5.4.109 "no
ṭac" branch, and a hypothetical *upacarma* by another route) remain
distinct objects (N2: "distinct branches remain distinct even if they
print the same word").

**6.4 Carrier, cuts, pairing.** Take PG14's N1 coefficient algebra
`B = C_Σ⟨z_e, z_e* : e ∈ E⟩` with `E` now including the compounding
events above (a disjoint union with PG14's verbal events; no relation is
imposed between the two families, as N1 imposes none). The right
B-module of histories, the event operators `T_{e,λ}` (unit coefficient
`U_e = 1 + z_e` on the edge, as in N5), the typed cuts

```
P_class   : histories whose SAM event carries that class
P_mode    : histories whose SAM / SA events carry that modal branch
P_aluk    : histories with an ALUK event
P_print   : histories whose surface observation equals a given word   (N6's observation cut, not ε)
```

and the pairing `⟨x, y⟩_B` are **PG14's objects applied to a larger index
set**; nothing is re-defined. The complementary cut `1 − P` is retained.

**6.5 Exact zero-specialization.** Theorem N4 is stated for "every admitted
finite operator construction" over `E`; its proof uses only ε(U_e a) = ε(a),
ε(U_e*) = 1, linearity and finite products. The compounding events satisfy
the same edge identity by construction (unit coefficient 1 + z_e), and the
guards of §6.2 – 6.3 inspect **H / F / O only** (sāmarthya reads R in F;
gaṇa membership reads L; the referent reads F; visibility reads H), never a
residue coefficient. Hence:

> **Theorem (N4 for compounding).** For every finite compounding
> construction A over the extended E and every finite-support state x,
> π₀,M(Ax) = Π₀,op(A) π₀,M(x), and ε⟨x, y⟩_B = ⟨π₀,M x, π₀,M y⟩_C.
> *Proof.* Verbatim N4; the only new obligation — that the guards are
> residue-blind — is discharged by §6.2 – 6.3 (declared interaction law,
> as N4 requires). ∎

**6.6 Exact branch recovery (N5) on the C4 pair.** Start at e_{h₀} =
(stokāt, mukta) with unit coefficient. The events `ALUK(6.3.2)` = a,
`UTT(8.2.39)` = b, and the optional `UTT(8.4.45)` = c (branch "nasal") /
`UTT(8.4.45, ∅)` = c′ (branch "no change") give two terminal histories

```
h_n : coefficient (1 + z_c)(1 + z_b)(1 + z_a)        prints stokānmukta
h_d : coefficient (1 + z_{c′})(1 + z_b)(1 + z_a)     prints stokādmukta
```

Both specialize to the unit (ε kills every residue letter) — the classical
"two licensed forms" — while the carrier keeps **which rule produced
which**: the printed pair is `P_print` applied to the two histories, and,
as N6 shows, `P_print` is not ε: collapsing the pair to a set of two
strings loses the event c′ (the *absence* of 8.4.45's nasal) that
distinguishes the second branch from a hypothetical form never touched by
8.4.45. This is the review's point that printed-word sets must not erase
branch histories, made exact.

**6.7 Why this is additive.** The S-state slots are PG14's; the events are
new labels on PG14's edge type; B is the same algebra on a larger E; the
cuts and pairing are PG14's constructors; N4 is applied, not re-proved;
the earlier certified packets (104, 114) are the `P_print`-images of
particular terminal histories and keep their pins.

---

## 7. Open obligations (Q)

| item | status |
|---|---|
| W3′ *niṣ-* before k (8.3.37 / 8.3.41) | not pulled; open |
| vyūḍhoraskaḥ's s before kap | witness rule not identified in the pinned text (8.3.46 does not name kap; kaskādi 8.3.48 not pinned); open |
| 6.3.4, 6.3.10, 6.3.14 (bahulam), 6.3.122 (bahulam) | rule quoted, witness open / declared |
| 2.2.33 vs 2.2.34 conflict | both branches retained; no pinned example |
| 5.2.40 / 5.2.41 (kiyat, iyat) | gh-form of vatu: recorded, not derived |
| the implementation map from the owned-sound records of the certified packets (104, 114) to the §6 operator category | the same interface PG14 N7 leaves open; shared |
| Python certificates for W2 – W7, W9′, W13 – W18 and the §4 – §5 tables | deferred (§8) |

---

## 8. Certification plan (secondary, deferred)

`proof_lab/samasa_construction_compiled.py` realising §6.3's events on the
T118 + T119 derivations with `MODE` (anuvṛtti-aware), `ORD` as a labelled
relation, `DEL` = luk / aluk on owners, `UTT`, `SA`, set-valued output, and
per-clause ablations as in theorum/104; plus a history-object test that two
printed-equal branches are distinct (§6.6). Not written here by
instruction. The packet's own check remains `verify_quotes.py` over both
capsules (§A of 118 and §A below).

---

## A. Sources (quoted from the pinned sūtrapāṭha; IAST by the ledger's transliteration)

```text
2.2.17 nityaṁ krīḍājīvikayoḥ · 2.2.18 kugatiprādayaḥ · 2.2.19 upapadamatiṅ · 2.1.39 stokāntikadūrārthakṛcchrāṇi ktena · 1.2.43 prathamānirdiṣṭaṁ samāsa upasarjanam · 1.2.44 ekavibhakti cāpūrvanipāte · 1.2.48 gostriyorupasarjanasya · 1.4.2 vipratiṣedhe paraṁ kāryam
8.3.95 gaviyudhibhyāṁ sthiraḥ · 8.3.59 ādeśapratyayayoḥ · 8.4.41 ṣṭunā ṣṭuḥ · 8.2.39 jhalāṁ jaśo'nte · 8.4.45 yaro'nunāsike'nunāsiko vā · 8.4.55 khari ca · 8.4.56 vāvasāne · 8.2.34 naho dhaḥ · 8.2.30 coḥ kuḥ · 8.2.62 kvinpratyayasya kuḥ · 8.3.82 agneḥ stutstomasomāḥ · 8.3.84 mātṛpitṛbhyāṁ svasā · 8.3.23 mo'nusvāraḥ · 8.4.58 anusvārasya yayi parasavarṇaḥ · 8.2.7 nalopaḥ prātipadikāntasya · 8.2.66 sasajuṣo ruḥ · 8.3.15 kharavasānayor visarjanīyaḥ · 8.3.46 ataḥ kṛkamikaṁsakumbhapātrakuśākarṇīṣvanavyayasya · 8.3.48 kaskādiṣu ca
2.2.29 cārthe dvandvaḥ · 2.2.30 upasarjanaṁ pūrvam · 2.2.31 rājadantādiṣu param · 2.2.32 dvandve ghi · 2.2.33 ajādyadantam · 2.2.34 alpāctaram · 2.2.35 saptamīviśeṣaṇe bahuvrīhau · 2.2.36 niṣṭhā · 2.2.37 vāhitāgnyādiṣu · 2.2.38 kaḍārāḥ karmadhāraye · 2.2.6 nañ · 2.2.8 ṣaṣṭhī
6.3.1 aluguttarapade · 6.3.2 pañcamyāḥ stokādibhyaḥ · 6.3.3 ojaḥsaho'mbhastamasaḥ tṛtīyāyāḥ · 6.3.4 manasaḥ saṁjñāyām · 6.3.7 vaiyākaraṇākhyāyāṁ caturthyāḥ · 6.3.8 parasya ca · 6.3.9 haladantāt saptamyāḥ saṁjñāyām · 6.3.10 kāranāmni ca prācāṁ halādau · 6.3.14 tatpuruṣe kṛti bahulam · 6.3.21 ṣaṣṭhyā ākrośe · 6.3.23 ṛto vidyāyonisambandhebhyaḥ · 6.3.24 vibhāṣā svasṛpatyoḥ
6.3.25 ānaṅ ṛto dvandve · 6.3.26 devatādvandve ca · 6.3.27 īdagneḥ somavaruṇayoḥ · 6.3.29 divo dyāvā · 6.3.30 divasaśca pṛthivyām · 6.3.31 uṣāsoṣasaḥ · 6.3.32 mātarapitarāvudīcām
6.3.34 striyāḥ puṁvadbhāṣitapuṁskādanūṅ samānādhikaraṇe striyāmapūraṇīpriyā''diṣu · 6.3.35 tasilādiṣvākṛtvasucaḥ · 6.3.37 na kopadhāyāḥ · 6.3.42 puṁvat karmadhārayajātīyadeśīyeṣu · 6.3.43 gharūpakalpacelaḍbruvagotramatahateṣu ṅyo'nekāco hrasvaḥ · 6.3.46 ānmahataḥ samānādhikaraṇajātīyayoḥ
6.3.67 arurdviṣadajantasya mum · 6.3.73 nalopo nañaḥ · 6.3.74 tasmānnuḍaci · 6.3.89 dṛgdṛśavatuṣu · 6.3.90 idaṅkimorīśkī · 6.3.91 ā sarvanāmnaḥ · 6.3.101 koḥ kat tatpuruṣe'ci · 6.3.104 kā pathyakṣayoḥ · 6.3.107 kavaṁ coṣṇe · 6.3.109 pṛṣodarādīni yathopadiṣṭam
6.3.114 saṁhitāyām · 6.3.115 karṇe lakṣaṇasyāviṣṭāṣṭapañcamaṇibhinnachinnachidrasruvasvastikasya · 6.3.116 nahivṛtivṛṣivyadhirucisahitaniṣu kvau · 6.3.117 vanagiryoḥ saṁjñāyāṁ koṭarakiṁśulakādīnām · 6.3.119 matau bahvaco'najirādīnām · 6.3.122 upasargasya ghañyamanuṣye bahulam · 6.3.123 ikaḥ kāśe · 6.3.128 viśvasya vasurāṭoḥ · 6.3.137 anyeṣāmapi dṛśyate
3.2.43 meghartibhayeṣu kṛñaḥ · 3.2.60 tyadādiṣu dṛśo'nālocane kañ ca · 5.2.39 yadtadetebhyaḥ parimāṇe vatup · 5.2.40 kimidaṁbhyāṁ vo ghaḥ · 7.2.102 tyadādīnāmaḥ · 7.1.14 sarvanāmnaḥ smai · 7.1.12 ṭāṅasiṅasām inātsyāḥ · 6.1.111 ṛta ut · 6.1.97 ato guṇe · 6.1.101 akaḥ savarṇe dīrghaḥ · 6.1.102 prathamayoḥ pūrvasavarṇaḥ · 1.1.46 ādyantau ṭakitau · 1.1.47 midaco'ntyātparaḥ · 1.1.52 alo'ntyasya · 1.1.53 ṅicca · 1.1.60 adarśanaṁ lopaḥ · 1.1.62 pratyayalope pratyayalakṣaṇam · 1.1.63 na lumatāṅgasya · 1.1.72 yena vidhistadantasya · 1.4.14 suptiṅantaṁ padam · 1.4.17 svādiṣvasarvanāmasthāne · 1.4.18 yaci bham · 1.4.7 śeṣo ghyasakhi
5.4.71 nañastatpuruṣāt · 5.4.72 patho vibhāṣā · 5.4.73 bahuvrīhau saṁkhyeye ḍajabahugaṇāt · 5.4.74 ṛkpūrabdhūḥpathāmānakṣe · 5.4.75 ac pratyanvavapūrvāt sāmalomnaḥ · 5.4.86 tatpuruṣasyāṅguleḥ saṁkhyāvyayādeḥ · 5.4.87 ahassarvaikadeśasaṁkhyātapuṇyācca rātreḥ · 5.4.91 rājāhassakhibhyaṣṭac · 5.4.92 gorataddhitaluki · 5.4.106 dvandvāccudaṣahāntāt samāhāre · 5.4.108 anaśca · 5.4.109 napuṁsakādanyatarasyām · 5.4.113 bahuvrīhau sakthyakṣṇoḥ svāṅgāt ṣac · 5.4.127 ic karmavyatihāre · 5.4.151 uraḥprabhṛtibhyaḥ kap · 5.4.153 nadyṛtaśca · 5.4.154 śeṣādvibhāṣā · 5.4.155 na saṁjñāyām
6.4.143 ṭeḥ · 6.4.144 nastaddhite · 6.4.148 yasyeti ca · 7.1.24 ato'm · 2.4.17 sa napuṁsakam · 2.4.18 avyayībhāvaśca · 2.4.26 paravalliṅgaṁ dvandvatatpuruṣayoḥ · 2.4.29 rātrāhnāhāḥ puṁsi · 2.4.30 apathaṁ napuṁsakam · 2.4.71 supo dhātuprātipadikayoḥ · 2.4.82 avyayādāpsupaḥ · 2.4.83 nāvyayībhāvādato'mtvapañcamyāḥ · 4.1.6 ugitaś ca · 4.1.41 ṣidgaurādibhyaśca · 8.2.9 mād upadhāyāś ca mator vo'yavādibhyaḥ · 3.3.18 bhāve · 3.2.102 niṣṭhā · 2.1.49 pūrvakālaikasarvajaratpurāṇanavakevalāḥ samānādhikaraṇena · 2.1.51 taddhitārthottarapadasamāhāre ca · 2.1.52 saṁkhyāpūrvo dviguḥ · 1.1.22 taraptamapau ghaḥ · 1.1.41 avyayībhāvaśca · 2.1.6 avyayaṁ vibhaktisamīpasamṛddhivyṛddhyarthābhāvātyayāsampratiśabdaprādurbhāvapaścādyathānupūrvyayaugapadyasādṛśyasampattisākalyāntavacaneṣu · 2.1.7 yathāsādṛśye · 2.1.11 vibhāṣā
```

Commentary (marked in the body): Kāśikā on 2.1.7, 2.2.18 – 19 (*nityam iti vartate*, the vārttika *prāk subutpatteḥ*), 2.2.33 (*indrāgnī*), 6.3.2, 6.3.3, 6.3.7, 6.3.9, 6.3.21, 6.3.25 – 27, 6.3.34 – 43, 6.3.67, 6.3.73 – 74, 6.3.89 – 91, 6.3.101 – 107, 6.3.115 – 128, 8.3.95, 8.4.45, 5.4.71 – 155; Bālamanoramā on 2.1.7. The PG15 review is `research/panini_grammar/causative_passive/T118_SOURCE_REVIEW.md`.
