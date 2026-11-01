# The Nadī (ṅī-Stem) Sup Paradigm Compiled — nadī, and kartrī … sotrī built from the pinned roots with tṛc and ṅīp

1 November 2026. After the a-stems (theorum/63, 86, 87) and the ā-stems
(theorum/88), the ī-stems that Pāṇini calls *nadī* (1.4.3): nadī itself, and
five agent feminines built end to end from the pinned Dhātupāṭha entries —
tṛc with theorum/80's guṇa and 1.1.51, then ṅīp (4.1.5), then the nadī
declension.

## 1. Sources (quoted)

```text
1.4.3    yū stryākhyau nadī            4.1.5   ṛnnebhyo ṅīp              3.1.133  ṇvultṛcau
3.4.114  ārdhadhātukaṁ śeṣaḥ           7.3.84  sārvadhātukārdhadhātukayoḥ (theorum/80)   1.1.51 ur aṇ raparaḥ
6.1.64   dhātvādeḥ ṣaḥ saḥ             7.3.112 āṇ nadyāḥ                 7.3.116  ṅer ām nadyāmnībhyaḥ
7.1.54   hrasvanadyāpo nuṭ             7.3.107 ambārthanadyor hrasvaḥ    6.1.68 / 6.1.69
6.1.77   iko yaṇ aci                   6.1.102 prathamayoḥ pūrvasavarṇaḥ 6.1.105  dīrghāj jasi ca
6.1.107  ami pūrvaḥ                    6.1.88 / 6.1.101                  8.3.57 iṇkoḥ ; 8.3.59 ādeśapratyayayoḥ
8.2.66 ; 8.3.15 ; 1.1.46 ; 1.1.56 ; 1.3.2–1.3.9
```

## 2. Results

**T1 nadī.** nadī, nadyau, nadyaḥ; nadīm, nadyau, nadīḥ; nadyā, nadībhyām,
nadībhiḥ; nadyai, …; nadyāḥ, …; nadyāḥ, nadyoḥ, nadīnām; nadyām, nadyoḥ,
nadīṣu; he nadi — all 22 equal the classical paradigm. Removing a stage
breaks exactly its cells: 7.3.112 {4s, 5s, 6s}, 7.3.116 {7s}, 7.1.54 {6p},
7.3.107 {8s}, 6.1.68 {1s}, 6.1.69 {8s}, 6.1.105 {1p} (6.1.102 would give
*nadīḥ* for jas), 8.3.59 {7p}. **Recorded:** on 7s the āṭ of 7.3.112 collapses
into ām by 6.1.101, so there 7.3.112 is redundant with 7.3.116.

**T2 Agent feminines from the roots.** ḍukṛñ, śru, hu, ciñ, ṣuñ + tṛc
(ārdhadhātuka by 3.4.114): guṇa of the ik-final aṅga by theorum/80's
antaratama with 1.1.51 → kartṛ, śrotṛ, hotṛ, cetṛ, sotṛ (6.1.64 on ṣu); +
ṅīp (4.1.5), ṛ + ī → rī (6.1.77) → kartrī, śrotrī, hotrī, cetrī, sotrī; each
is nadī (1.4.3) and gives the exchanged nadī paradigm: **110 forms**.

**Correction after external review.** In the first pinned run (8d832667…d7b5) an inline comment swallowed five entries of the ablation table, so only three of the eight stage-removal checks were active (the paradigm equality was unaffected). Repaired; all eight run; `trc_agent` now refuses ids outside the five admitted roots. New pin; the first stays in history.

## 3. Certificate

```text
python -m proof_lab.ngi_stem_sup_compiled
python -m unittest proof_lab.test_ngi_stem_sup_compiled -v
```
Status `PASS_NGI_STEM_SUP_COMPILED_CANDIDATE`, SHA-256
`b13ad1d61f7330ba83b7ebd4fe8e9e7215578b189898be111c3ed8843dac591d`
(`proof_lab/NGI_STEM_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82, 86.

## 4. Claim boundary

```text
nadī: 22 FORMS; EACH STAGE BREAKS EXACTLY ITS CELLS; 7.3.112 REDUNDANT ON 7s             PROVED
kartṛ … sotṛ BY 7.3.84 GUṆA (ANTARATAMA + 1.1.51) FROM THE PINNED ROOTS; + ṅīp → 110 FORMS  PROVED
ANIṬ BEFORE tṛc (bhū, pū, lū, tan EXCLUDED)                                                DECLARED
STAGE ORDER                                                                                DECLARED PIPELINE
ṅīṣ / ṅīn, ū-STEMS, strī, GAURĀDI LIST                                                     NOT CLAIMED
RH, YM                                                                                     UNTOUCHED
```
