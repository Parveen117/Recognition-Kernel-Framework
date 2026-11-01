# The Feminine Affixes Compiled — ṭāp (4.1.4, with 7.3.44 kārikā), ṅīp after ugit (4.1.6, with 7.1.81 bhavantī) and after the ṇit / ñit / yañ taddhitas (4.1.15, 4.1.16 with 6.4.150), ṅīṣ (4.1.41); declined on Theorems 88 / 89

2 November 2026. Strī-pratyaya. Thirteen feminine stems from the masculine
stems of theorum/103, 107, 109 and three plain a-stems; the forming affix's
markers (ugit, ṇit, ñit) are read by theorum/82 and decide the sūtra; each rule
shown load-bearing on exactly the stems it governs; four stems declined on
the ā- and ī-carriers.

## 1. Sources (quoted)

```text
4.1.3 striyām   4.1.1 ṅyāpprātipadikāt   4.1.4 ajādyataṣ ṭāp   7.3.44 pratyayasthāt kāt pūrvasyāta id āpy asupaḥ   4.1.6 ugitaś ca   7.1.81 śapśyanor nityam
4.1.15 ṭiḍḍhāṇañdvayasajdaghnañmātractayapṭhakṭhañkañkvarapaḥ   4.1.16 yañaś ca   6.4.150 halas taddhitasya   4.1.41 ṣidgaurādibhyaś ca   6.4.148 yasyeti ca   1.4.18   8.4.2   1.3.3   1.3.6   1.3.7   1.3.9
```

## 2. Results

**T1.** ṭāp: bālā, devā, ajā; kārikā, pācikā, nāyikā (7.3.44 on Theorem 107's
ṇvul stems). ṅīp after the ugit (4.1.6): bhavantī (7.1.81 num, the śatṛ after
śap), dhīmatī, bhagavatī (no num: not after śap). ṅīp after the taddhita:
aupagavī, dākṣī (4.1.15; 6.4.148), gārgī (4.1.16; 6.4.150). ṅīṣ: gaurī
(4.1.41; 6.4.148) — 13/13. Without 7.3.44 exactly the three ṇvul feminines
break; 7.1.81 bhavantī; 6.4.150 gārgī; 6.4.148 aupagavī, dākṣī, gaurī.

**T2.** bālā, kārikā on theorum/88 (bālayā, kārikayā, bālānām, kārikāṇām) and
bhavantī, gārgī on theorum/89 (bhavantyā, gārgyā, bhavantīnām, gārgīṇām); the
8.4.2 across ku in kārikāṇām / gārgīṇām is applied after the carrier by
theorum/91's ṇatva and recorded, the ā / ī carriers having been certified on
stems without an r / ṣ trigger.

## 3. Certificate

```text
python -m proof_lab.stri_pratyaya_compiled
python -m unittest proof_lab.test_stri_pratyaya_compiled -v
```
Status `PASS_STRI_PRATYAYA_COMPILED_CANDIDATE`, SHA-256 `57435747f98233302542a21415e4baabf436c9d4a094674ad40a17778f8b1326`
(`proof_lab/STRI_PRATYAYA_COMPILED_EXPECTED.sha256`). Imports theorum/82, 88, 89, 91.

## 4. Claim boundary

```text
13 FEMININE STEMS; EACH RULE BREAKS EXACTLY THE STEMS STATED; FOUR DECLINED ON 88 / 89          PROVED
gaurādi MEMBERSHIP OF gaura; THE AFFIX WHERE THE SŪTRAS GIVE AN OPTION                          DECLARED
4.1.5, 4.1.20–75, ṅīn, ūṅ, mātṛ-TYPE STEMS, ACCENT                                              NOT CLAIMED
RH, YM                                                                                          UNTOUCHED
```
