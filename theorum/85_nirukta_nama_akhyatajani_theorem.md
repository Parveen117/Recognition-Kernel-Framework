# The Nirukta Vedāṅga — "nāmāny ākhyātajāni" computed: nāma and ākhyāta from one dhātu on the pinned carriers

1 November 2026. Fifth Vedāṅga in the repository (Chandas 71, Śulba 72,
Jyotiṣa 73, Śikṣā 83, Vyākaraṇa 58–68/80–82). Yāska's thesis (Śākaṭāyana's,
in Nirukta 1.12) that nouns arise from verbs is made a computation: from one
teaching form, the nāma (kta + sup) and the ākhyāta (śap + tiṅ) are derived
on the pinned packets of theorum/82, 63 and 64, and Yāska's four padajātis
partition the computed padas.

## 1. Sources (quoted)

```text
Nirukta 1.12  tatra nāmāny ākhyātajānīti śākaṭāyano nairuktasamayaś ca /
              na sarvāṇīti gārgyo vaiyākaraṇānāṁ caike
              (verified against a printed citation this session)
Nirukta 1.1   tad yāny etāni catvāri padajātāni nāmākhyāte copasarganipātāś ca ;
              bhāvapradhānam ākhyātam / sattvapradhānāni nāmāni   (standard printed text)

Aṣṭādhyāyī
3.1.91  dhātoḥ               3.1.93  kṛd atiṅ            1.1.26  ktaktavatū niṣṭhā   3.2.102 niṣṭhā
1.2.46  kṛttaddhitasamāsāś ca                            4.1.1   ṅyāpprātipadikāt   4.1.2  svaujas…sup
1.4.14  suptiṅantaṁ padam
6.4.37  anudāttopadeśavanatitanotyādīnām anunāsikalopo jhali kṅiti
7.2.10  ekāca upadeśe 'nudāttāt
1.4.57  cādayo 'sattve       1.4.58  prādayaḥ            1.4.59  upasargāḥ kriyāyoge
```

## 2. Results

**T1 Nāma from dhātu.** `gamḷ~`, `bhū`, `ḍukṛñ` through theorum/82's its, +
kta (1.3.8: `ta`, kit), with 7.2.10 (no iṭ) and 6.4.37 (gam → ga before the
jhal-initial kit affix; fires on gam only) give the prātipadikas **gata,
bhūta, kṛta** (1.2.46, 3.1.93). theorum/63's pinned sup ladder then derives
all 22 forms of each — **66 forms** (gataḥ, gatau, gatāḥ, gatam … gateṣu;
bhūtaḥ …; kṛtaḥ …) — equal to the rāma paradigm with the stem exchanged and
without the 8.4.2 ṇatva (the stem's *t* intervenes).

**T2 Ākhyāta from the same dhātu.** theorum/64's pinned laṭ derivation gives
gacchati … gacchāmaḥ and bhavati … bhavāmaḥ (18 forms) from the same roots.

**T3 The padajāti partition.** Every computed form is a pada (1.4.14); the
sup-anta forms are nāma, the tiṅ-anta forms ākhyāta; the sets are disjoint and
exhaust the computed padas; the same dhātu feeds both. Upasarga (1.4.58, 22
items) and nipāta (1.4.57) are cited lists.

## 3. Certificate

```text
python -m proof_lab.nirukta_nama_akhyatajani
python -m unittest proof_lab.test_nirukta_nama_akhyatajani -v
```
Status `PASS_NIRUKTA_NAMA_AKHYATAJANI_CANDIDATE`, SHA-256
`950cad0deabd1f8185eadb5f85cb7b407a24f6fdf2e544466693cc1542a2b73b`
(`proof_lab/NIRUKTA_NAMA_AKHYATAJANI_EXPECTED.sha256`). Imports theorum/82, 63
(with its own domains), 64 (with its grammar-wide domains); their pins are
unchanged.

## 4. Claim boundary

```text
gata / bhūta / kṛta FROM THE TEACHING FORMS BY 82-its + kta + 6.4.37 / 7.2.10        PROVED
ALL 66 SUP FORMS BY theorum/63's PINNED LADDER (= EXCHANGED rāma PARADIGM)            PROVED
18 LAṬ FORMS BY theorum/64 FROM THE SAME ROOTS                                         PROVED
NĀMA / ĀKHYĀTA DISJOINT AND EXHAUSTIVE ON THE COMPUTED PADAS                           PROVED
"nāmāny ākhyātajāni" IN GENERAL; GĀRGYA'S "na sarvāṇi"                                NOT DECIDED (three roots, one kṛt affix)
6.4.37 ROOT LIST, 7.2.10 ANIṬ STATUS                                                  DECLARED FROM THE DHĀTUPĀṬHA (accent not carried)
NIRUKTA 1.1 TEXT                                                                      STANDARD PRINTED; 1.12 VERIFIED
UPASARGA / NIPĀTA LISTS; ṢAḌ BHĀVAVIKĀRĀḤ; NIRVACANA                                  CITED / NOT MODELLED
RH, YM                                                                                UNTOUCHED
```
