# The Saṁjñā Layer of Pāda 1.1 on the Sound Carrier — savarṇa derived, selectors exact, pragṛhya blocks sandhi

1 November 2026. First batch of the all-sūtra programme, which now has one
record: the [Aṣṭādhyāyī ledger](../proof_lab/astadhyayi/ASTADHYAYI_LEDGER.md)
(`python -m proof_lab.astadhyayi_ledger`), the single place that lists every
sūtra realized in this repository with its evidence level — compiled
(theorum/80 record interpreter), meta (saṁjñā/paribhāṣā implemented),
hand-coded (exact function in a certified packet), cited — and that states
the claim boundary: every sūtra not listed is unrealized. (Since the merge of the PG1 stage, the ledger also carries each sūtra's Devanagari text from the pinned edition `research/panini_grammar/SUTRAPATHA.tsv`, the edition's total of 3,983 numbered records, and a transliteration cross-check of every curated IAST text against it.) This capsule adds
nine saṁjñā sūtras of pāda 1.1 (with 6.1.125) at the meta level, on the
sound carrier of theorum/78–80.

## 1. Sources (quoted)

```text
1.1.7    halo 'nantarāḥ saṁyogaḥ        consonants with nothing between them are a cluster
1.1.8    mukhanāsikāvacano 'nunāsikaḥ   a sound uttered through mouth and nose is nasal
1.1.9    tulyāsyaprayatnaṁ savarṇam     equal place and internal effort: savarṇa
1.1.10   nājjhalau                       but a vowel and a consonant are never savarṇa
1.1.11   īdūdeddvivacanaṁ pragṛhyam     dual endings in ī, ū, e are pragṛhya
6.1.125  plutapragṛhyā aci nityam       a pluta or pragṛhya vowel is unchanged before a vowel
1.1.64   aco 'ntyādi ṭi                 from the last vowel onward: ṭi
1.1.65   alo 'ntyāt pūrva upadhā        the sound before the last: upadhā
1.1.72   yena vidhis tadantasya         a rule stated by X applies to what ends in X
```

The sthāna table is the traditional one (a: kaṇṭha; i-series, ca-varga, y, ś:
tālu; ṛ-series, ṭa-varga, r, ṣ: mūrdhan; ḷ-series, ta-varga, l, s: danta;
u-series, pa-varga: oṣṭha; e, ai: kaṇṭha-tālu; o, au: kaṇṭha-oṣṭha; v:
danta-oṣṭha; h, ka-varga: kaṇṭha). The internal effort: stops spṛṣṭa,
semivowels īṣat-spṛṣṭa, vowels and ūṣman vivṛta (Siddhānta-kaumudī on 1.1.9,
*ūṣmaṇāṁ vivṛtam* — which is exactly why 1.1.10 is needed). The
sandhyakṣaras e/ai and o/au share place and effort; the tradition keeps them
apart by the proportion of their two places, recorded here as a separate
attribute so the certificate shows where the table alone would not decide.

## 2. Results

### T1 Savarṇa is derived, not declared

1.1.9 with the 1.1.10 exclusion, computed on the table, yields **exactly**:
the vowel length pairs `{a,ā} {i,ī} {u,ū} {ṛ,ṝ} {ḷ,ḹ}` with `e, ai, o, au`
singletons; the **five vargas** `{k kh g gh ṅ} {c ch j jh ñ} {ṭ ṭh ḍ ḍh ṇ}
{t th d dh n} {p ph b bh m}` — theorum/79's varga columns and 1.1.69's udit
classes ku, cu, ṭu, tu, pu are therefore 1.1.9 classes; semivowels and
sibilants are singletons; theorum/80's `SAVARNA` table is the vowel part on
its carrier. Without 1.1.10, `i–ś` and `a–h` would pair: 1.1.10 is
load-bearing.

### T2 Selectors

1.1.64 `ṭi(gam) = am`, `ṭi(bhavati) = i`; 1.1.65 `upadhā(gam) = a`; 1.1.72:
the "aṅga ending in ik" condition of theorum/80's compiled 7.3.84 is the
tadanta reading of *ik* (true for nī, bhū, kṛ; false for gam, iṣ).

### T3 Pragṛhya, saṁyoga, anunāsika

With the pragṛhya flag that 1.1.11 attaches to dual ī/ū/e endings, 6.1.125
makes **every** compiled sandhi rule of theorum/80 inapplicable on those
junctions (`ī + a`, `ū + e`, `e + i`, …) and leaves every other junction
unchanged; without the flag the same junctions fire. 1.1.7: the only cluster
in *gacchati* is `c ch`, *gam* has none. 1.1.8: the nasals on the carrier
are theorum/79's nasal row.

## 3. Certificate

```text
python proof_lab/paninian_samjna_sound_layer.py
python -m unittest proof_lab.test_paninian_samjna_sound_layer -v
python -m unittest proof_lab.test_astadhyayi_ledger -v
```
Status `PASS_PANINIAN_SAMJNA_SOUND_LAYER_CANDIDATE`, SHA-256
`98c8a45c5eee2a022a5a7fe72286d44d5a5cb4eac7b22522e1fca6e30c961c48`
(`proof_lab/PANINIAN_SAMJNA_SOUND_LAYER_EXPECTED.sha256`). The ledger test
checks that the committed ledger equals its rebuild and that every
hand-coded number is carried by its packet's source.

## 4. Claim boundary

```text
1.1.9 + 1.1.10 ON THE TABLE = LENGTH PAIRS + FIVE VARGAS (theorum/79, 80 DERIVED)   PROVED
1.1.10 LOAD-BEARING (i–ś, a–h pair without it)                                      PROVED
ṭi, upadhā, tadanta EXACT; 7.3.84's ik-final = tadanta(ik)                           PROVED
6.1.125 WITH 1.1.11 BLOCKS ALL COMPILED SANDHI ON DUAL ī/ū/e, NOTHING ELSE           PROVED
1.1.7 CLUSTERS, 1.1.8 NASALS ON THE CARRIER                                          PROVED
e/ai, o/au SEPARATION                                                                BY THE RECORDED PROPORTION ATTRIBUTE, NOT BY THE TABLE
PLUTA, ANUSVĀRA, NASALIZED VOWELS; DVIVACANA FROM MORPHOLOGY                         NOT ON THE CARRIER / SUPPLIED FLAG
LEDGER: 156 OF 3959 SŪTRAS LISTED (10 compiled, 34 meta, 72 hand-coded, 38 cited)           CLAIM BOUNDARY, NOT COVERAGE
RH, YM                                                                               UNTOUCHED
```
