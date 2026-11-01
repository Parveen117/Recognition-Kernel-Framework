# The Āp-Stem Sup Paradigm Compiled — ṭāp feminines of the kta nouns, every stage load-bearing

1 November 2026. The nominal grammar in this repository was the a-stem ladder
of theorum/63 (rāma, and by theorum/86–87 fifteen kta nouns). This capsule
opens the ā-stems: ṭāp (4.1.4) on those nouns, declined through the quoted
sūtras on theorum/82's it-layer, with latā as the oracle and each stage shown
to break exactly the cells it owns.

## 1. Sources (quoted)

```text
4.1.4    ajādyataṣ ṭāp                 7.1.18   auṅ āpaḥ                 7.3.116  ṅer ām nadyāmnībhyaḥ
7.3.113  yāḍ āpaḥ                      7.1.54   hrasvanadyāpo nuṭ        7.3.105  āṅi cāpaḥ
7.3.106  sambuddhau ca                 6.1.68   halṅyābbhyo dīrghāt sutisyapṛktaṁ hal
6.1.69   eṅhrasvāt sambuddheḥ          6.1.87 / 6.1.88 / 6.1.101 / 6.1.107 / 6.1.78 (sandhi, theorum/58, 80, 63)
1.1.46   ādyantau ṭakitau              1.1.56   sthānivad ādeśo 'nalvidhau       1.1.52 / 1.1.55
8.2.66   sasajuṣo ruḥ                  8.3.15   kharavasānayor visarjanīyaḥ      1.3.2–1.3.9 (theorum/82)
```

## 2. Results

**T1 latā.** From the 21 sup teaching forms (+ sambuddhi) through the it-layer:
latā, late, latāḥ; latām, late, latāḥ; latayā, latābhyām, latābhiḥ; latāyai,
latābhyām, latābhyaḥ; latāyāḥ, latābhyām, latābhyaḥ; latāyāḥ, latayoḥ,
latānām; latāyām, latayoḥ, latāsu; he late — all 22 equal to the classical
paradigm. Each path is recorded (e.g. 4s: ṅe → yāṭ prefixed (7.3.113, 1.1.46)
→ ā + yā + e → yai (6.1.88)).

**T2 Every stage is load-bearing on named cells.** Removing 7.1.18 breaks
exactly {1d, 2d}; 7.3.116 {7s}; 7.3.113 {4s, 5s, 6s, 7s}; 7.1.54 {6p};
7.3.105 {3s, 6d, 7d}; 7.3.106 {8s}; 6.1.68 {1s}; 6.1.69 {8s} — and nothing
else.

**T3 Fifteen ṭāp feminines, 330 forms.** bhūtā, sutā, citā, āptā, śaktā, tatā,
kṛtā, krītā, śrutā, pūtā, hutā (theorum/86) and paktā, labdhā, tunnā, lūnā
(theorum/87) decline exactly as latā with the stem exchanged.

## 3. Certificate

```text
python -m proof_lab.ap_stem_sup_compiled
python -m unittest proof_lab.test_ap_stem_sup_compiled -v
```
Status `PASS_AP_STEM_SUP_COMPILED_CANDIDATE`, SHA-256
`0a0e12bffaafc240ce4d8d9edce5aa33776a8f2f440bfc356e03d64859b2c8cb`
(`proof_lab/AP_STEM_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/82, 86, 87.

## 4. Claim boundary

```text
latā: 22 FORMS FROM THE TEACHING FORMS THROUGH THE QUOTED SŪTRAS                 PROVED
EACH STAGE BREAKS EXACTLY ITS OWN CELLS                                          PROVED
15 ṭāp FEMININES OF THE kta NOUNS: 330 FORMS                                      PROVED
STAGE ORDER                                                                      DECLARED PIPELINE (not derived from 1.4.2 / apavāda as theorum/63 does)
ṅīp FEMININES, nadī, CONSONANT STEMS, PRONOUNS; 4.1.4's ajādi LIST                NOT CLAIMED / CITED
RH, YM                                                                           UNTOUCHED
```
