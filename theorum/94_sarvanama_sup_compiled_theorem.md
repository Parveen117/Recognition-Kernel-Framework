# The Sarvanāma Sup Paradigms Compiled — sarva and tad; the sarvanāma saṁjñā on exactly five cells; 7.2.102 / 7.2.106 on tad

1 November 2026. Eighth nominal class: the pronouns. On the a-stem engine of
theorum/63 the sarvanāma saṁjñā (1.1.27) changes exactly five cells — jas
(7.1.17), ṅe (7.1.14), ṅasi and ṅi (7.1.15), ām (7.1.52) — and tad adds the
tyadādi substitution 7.2.102 (every cell) and 7.2.106 (saḥ, only 1s). theorum/65
had tad in two neuter cells; this gives the masculine paradigm.

## 1. Sources (quoted)

```text
1.1.27  sarvādīni sarvanāmāni   7.1.17  jasaḥ śī   7.1.14  sarvanāmnaḥ smai   7.1.15  ṅasiṅyoḥ smātsminau   7.1.52  āmi sarvanāmnaḥ suṭ
7.3.103 bahuvacane jhaly et     8.3.59  ādeśapratyayayoḥ   7.2.102 tyadādīnām aḥ   7.2.106 tadoḥ saḥ sāv anantyayoḥ   6.1.97 ato guṇe
6.1.87 ; 7.1.9 ; 7.1.12 ; 7.1.13 ; 7.3.102 ; 6.1.102 / 6.1.103 ; 6.1.107 ; 6.1.78 ; 8.4.2 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 sarva.** sarvaḥ, sarvau, sarve; sarvam, sarvau, sarvān; sarveṇa,
sarvābhyām, sarvaiḥ; sarvasmai …; sarvasmāt …; sarvasya, sarvayoḥ, sarveṣām;
sarvasmin, sarvayoḥ, sarveṣu; he sarva — 22/22. The **sarvanāma saṁjñā
breaks exactly {1p, 4s, 5s, 6p, 7s}**; 7.1.17 {1p}; 7.1.14 {4s}; 7.1.15
{5s, 7s}; 7.1.52 {6p}; 7.3.103 {4p, 5p, 6p, 7p} (the suṭ makes ām jhal-initial);
8.3.59 {6p, 7p}; 8.4.2 {3s}; the a-stem sūtras their usual cells.

**T2 tad.** saḥ, tau, te; tam, tau, tān; tena, tābhyām, taiḥ; tasmai …;
tasmāt …; tasya, tayoḥ, teṣām; tasmin, tayoḥ, teṣu — 21/21. **7.2.102 breaks
every cell** (with 6.1.97 pararūpa inside the stem); **7.2.106 exactly {1s}**;
the sarvanāma cells as for sarva; the sambuddhi is refused.

## 3. Certificate

```text
python -m proof_lab.sarvanama_sup_compiled
python -m unittest proof_lab.test_sarvanama_sup_compiled -v
```
Status `PASS_SARVANAMA_SUP_COMPILED_CANDIDATE`, SHA-256
`1a04614384396443b1eaf0c4bf07da61a822b8cbab3b80315bfd53e96f924152`
(`proof_lab/SARVANAMA_SUP_COMPILED_EXPECTED.sha256`). Imports theorum/82, 91.

## 4. Claim boundary

```text
sarva: 22 FORMS; sarvanāma BREAKS EXACTLY {1p, 4s, 5s, 6p, 7s}; EACH STAGE ITS CELLS     PROVED
tad: 21 FORMS; 7.2.102 EVERY CELL, 7.2.106 EXACTLY {1s}; SAMBUDDHI REFUSED              PROVED
FEMININE / NEUTER PRONOUNS, etad / yad / idam / asmad, 1.1.34 OPTION CELLS              NOT CLAIMED
sarva DECLARED FROM THE GAṆA; STAGE ORDER A DECLARED PIPELINE
RH, YM                                                                                  UNTOUCHED
```
