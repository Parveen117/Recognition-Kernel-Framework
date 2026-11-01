# Lṛṭ and Luṭ (the Two Futures) Parasmaipada Compiled — bhū, gam, nī; iṭ by 7.2.35 / 7.2.58; luṭ's ḍā / rau / ras with 6.4.143, 7.4.50, 7.4.51

1 November 2026. Fifth and sixth lakāra. Both are ārdhadhātuka (3.4.114), so
the guṇa of 7.3.84 now comes from theorum/80's antaratama on the bare root
(bhū → bho → bhav-i-, nī → ne) rather than from theorum/58's śap stems, and
the iṭ augment of 7.2.35 (bhū), 7.2.58 (gam, before an s-initial affix only)
or its absence (nī, 7.2.10) decides the shape.

## 1. Sources (quoted)

```text
3.3.13  lṛṭ śeṣe ca      3.3.15  anadyatane luṭ      3.1.33  syatāsī lṛluṭoḥ      3.4.114 ārdhadhātukaṁ śeṣaḥ
7.2.35  ārdhadhātukasyeḍ valādeḥ    7.2.58  gamer iṭ parasmaipadeṣu    7.2.10 ekāca upadeśe 'nudāttāt
7.3.84 ; 6.1.78 ; 8.3.59            2.4.85  luṭaḥ prathamasya ḍārauras   6.4.143 ṭeḥ ; 1.1.64 aco 'ntyādi ṭi
7.4.50  tāsastyor lopaḥ             7.4.51  ri ca                        7.1.3 ; 7.3.101 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1 lṛṭ.** bhaviṣyati … bhaviṣyāmaḥ; gamiṣyati … (iṭ by 7.2.58); neṣyati …
(no iṭ): **27/27**. 3.1.33, 7.2.35, 7.3.84, 6.1.78 and 8.3.59 each break all
nine of bhū; 7.1.3 {3p}; 7.3.101 {1s, 1d, 1p}; 8.2.66 {3d, 2d, 1d, 1p};
**removing 7.2.58 breaks all nine of gam and nothing of bhū / nī**, and
removing 7.2.35 leaves nī untouched.

**T2 luṭ.** bhavitā, bhavitārau, bhavitāraḥ; bhavitāsi, bhavitāsthaḥ,
bhavitāstha; bhavitāsmi, bhavitāsvaḥ, bhavitāsmaḥ; netā …: **18/18**. 2.4.85
{3s, 3d, 3p}; 6.4.143 {3s} (the ṭi *ās* drops before the ḍit); 7.4.50 {2s};
7.4.51 {3d, 3p}; 8.2.66 {3p, 2d, 1d, 1p}. gam's luṭ (gantā) is refused by
name — it needs 8.3.24 / 8.4.58.

## 3. Certificate

```text
python -m proof_lab.lrt_lut_parasmaipada_compiled
python -m unittest proof_lab.test_lrt_lut_parasmaipada_compiled -v
```
Status `PASS_LRT_LUT_PARASMAIPADA_COMPILED_CANDIDATE`, SHA-256
`0d245b9d5254260fb1074afd6344c73b3a7ff532c256bc12ad227d8858182875`
(`proof_lab/LRT_LUT_PARASMAIPADA_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82.

## 4. Claim boundary

```text
lṛṭ OF bhū, gam, nī (27) AND luṭ OF bhū, nī (18); EACH STAGE BREAKS EXACTLY ITS CELLS      PROVED
7.2.58 LOAD-BEARING ON gam ONLY; 7.2.35 NOT ON nī                                          PROVED
gam's luṭ (gantā)                                                                          REFUSED (8.3.24 / 8.4.58)
seṭ / aniṭ STATUS DECLARED; lṛṅ, luṅ, liṭ, ĀTMANEPADA, OTHER ROOTS                         NOT CLAIMED
RH, YM                                                                                     UNTOUCHED
```
