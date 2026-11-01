# The Feminine Sarvanāma (Āp) Sup Paradigms Compiled — sarvā and sā; 7.3.114 syāṭ with the shortening; the masculine rules shown not to reach the feminine

1 November 2026. theorum/94 gave sarva and tad in the masculine; this capsule
gives their feminines on theorum/88's āp engine. The sarvanāma now acts
through 7.3.114 (syāṭ instead of 7.3.113's yāṭ, and the āp shortened:
sarvasyai, sarvasyāḥ, sarvasyām) and 7.1.52 (sarvāsām), while 7.1.17 and
7.1.15 — which stand under *ataḥ* — must not apply: the certificate shows
what their misapplication would produce.

## 1. Sources (quoted)

```text
1.1.27 sarvādīni sarvanāmāni   4.1.4 ajādyataṣ ṭāp   7.2.102 tyadādīnām aḥ   7.2.106 tadoḥ saḥ sāv anantyayoḥ
7.3.114 sarvanāmnaḥ syāḍ ḍhrasvaś ca   7.3.113 yāḍ āpaḥ (superseded)   7.1.52 āmi sarvanāmnaḥ suṭ   7.1.17 / 7.1.15 (under 7.1.9 ataḥ)
7.1.18 ; 7.3.116 ; 7.3.105 ; 7.3.106 ; 6.1.68 ; 6.1.69 ; 6.1.87 ; 6.1.88 ; 6.1.101 ; 6.1.107 ; 6.1.78 ; 6.1.97 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 sarvā.** sarvā, sarve, sarvāḥ; sarvām, sarve, sarvāḥ; sarvayā, sarvābhyām,
sarvābhiḥ; sarvasyai …; sarvasyāḥ …; sarvasyāḥ, sarvayoḥ, sarvāsām; sarvasyām,
sarvayoḥ, sarvāsu; he sarve — 22/22. The sarvanāma saṁjñā breaks exactly
{4s, 5s, 6s, 7s, 6p}; 7.3.114 {4s, 5s, 6s, 7s}; 7.1.52 {6p}; 7.3.113 nothing
(superseded); the āp stages their cells as in theorum/88. **Control:** reading
7.1.17 / 7.1.15 onto the feminine yields *sarve (1p) and *sarvāsmin (7s),
both wrong against the oracle — the *ataḥ* restriction is load-bearing.

**T2 sā.** sā, te, tāḥ; tām, te, tāḥ; tayā, tābhyām, tābhiḥ; tasyai …; tasyāḥ …;
tasyāḥ, tayoḥ, tāsām; tasyām, tayoḥ, tāsu — 21/21; 7.2.102 every cell, 7.2.106
{1s}; sambuddhi refused.

## 3. Certificate

```text
python -m proof_lab.sarvanama_ap_sup_compiled
python -m unittest proof_lab.test_sarvanama_ap_sup_compiled -v
```
Status `PASS_SARVANAMA_AP_SUP_COMPILED_CANDIDATE`, SHA-256 `dc7a91476353ced6c2f85ef1c50ca5eccf55f5469ebcf685f20a381209b68ed9`
(`proof_lab/SARVANAMA_AP_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/82.

## 4. Claim boundary

```text
sarvā 22, sā 21; sarvanāma / 7.3.114 / 7.1.52 / 7.2.102 / 7.2.106 EACH ON EXACTLY ITS CELLS   PROVED
7.1.17 / 7.1.15 DO NOT REACH THE FEMININE (CONTROL *sarve, *sarvāsmin)                      PROVED
NEUTER PRONOUNS, idam / etad / yad, 1.1.34 OPTIONS, 7.3.115                                   NOT CLAIMED
STAGE ORDER A DECLARED PIPELINE ; RH, YM UNTOUCHED
```
