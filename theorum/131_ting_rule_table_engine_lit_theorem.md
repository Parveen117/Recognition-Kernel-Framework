# Tiṅ Rule-Table Engine III — liṭ as twelve new rows with the abhyāsa as a segment (bhū, gam, kṛ, nī: 20 cells; 75 rows on 325 cells)

2 November 2026. The perfect of theorum/102 goes into the verbal table. What liṭ adds structurally is one more segment — the **abhyāsa** (6.1.8 *liṭi dhātor anabhyāsasya* with 6.1.1 *ekāco dve prathamasya* and 6.1.4 *pūrvo 'bhyāsaḥ*), on which 7.4.59 *hrasvaḥ*, 7.4.62 *kuhoś cuḥ*, 7.4.66 *ur at*, 7.4.73 *bhavater aḥ* and 8.4.54 *abhyāse car ca* act as rows — and one more predicate: the kit of 1.2.5 *asaṁyogāl liṭ kit* for the apit endings, with ṇal pit as tip's substitute (1.1.56), so that the pit cells take vṛddhi (7.2.115 *aco ñṇiti*: nināya, cakāra; 7.2.116 *ata upadhāyāḥ*: jagāma) and the kit cells take none (1.1.5) but 6.4.98's upadhā-lopa (jagmatuḥ) and 6.1.77's yaṇ (ninyatuḥ, cakratuḥ). Two orderings are load-bearing and now visible in the paths: 6.4.88's vuk before 7.2.115 (babhūva, not *babhāva), and 6.1.65's ṇ → n before the doubling (nināya, not *ṇināya). 7.2.13 is a flag that the iṭ row reads (cakṛva against ninyiva, jagmiva).

## 1. The new rows (cells of the 325 each breaks when removed)

```text
3.4.82  ṇal atus us thal athus a ṇal va ma   20    6.1.8   the first ekāc doubled (6.1.1, 6.1.4)   20
7.4.59  hrasvaḥ                               10    7.4.62  kuhoś cuḥ                              10
7.4.66  ur at (ca-kāra)                       5     7.4.73  bhavater aḥ (ba-bhūva)                 5
8.4.54  abhyāse car ca                        5     7.2.13  no iṭ after kṛ … in liṭ (flag)          2
7.2.115 aco ñṇiti (nai-, kār-)                2     7.2.116 ata upadhāyāḥ (jagāma)                 1
6.4.98  gam's upadhā dropped before kit       4     6.1.77  iko yaṇ aci after kit                   6
```

Generalised: 7.2.35 also gives iṭ before liṭ's va / ma for every root outside 7.2.13 (55 cells now); 6.4.88 reads luṅ and liṭ (7); 6.1.78 handles ai / au → āy / āv (nināya). 7.4.60 *halādiḥ śeṣaḥ* is **not** in the table: no root of the certified liṭ oracle begins with a cluster, the row would be vacuous, and a vacuous row is not certified (NOT claimed).

## 2. Worked derivations

```text
babhūva   bhū + liṭ 3s: 3.4.82 ṇal → 6.1.8 bhū-bhū → 7.4.59 bhu → 7.4.73 bha → 8.4.54 ba → 6.4.88 vuk → babhūva   (vṛddhi has no ac to act on)
jagmatuḥ  gam + liṭ 3d: atus (kit, 1.2.5) → 6.1.8 ga-gam → 7.4.62 ja → 6.4.98 jagm → jagmatuḥ
cakāra    ḍukṛñ + liṭ 3s: ṇal (pit) → 6.1.8 kṛ-kṛ → 7.4.66 ka → 7.4.62 ca → 7.2.115 kār → cakāra
cakṛva    kṛ + liṭ 1d: va (kit) → ca-kṛ → 7.2.13 no iṭ → cakṛva   (no yaṇ: va is not vowel-initial)
nināya    ṇīñ + liṭ 3s: 6.1.65 nī → 6.1.8 nī-nī → 7.4.59 ni → 7.2.115 nai → 6.1.78 nināya
ninyiva   nī + liṭ 1d: va (kit) → ni-nī → 7.2.35 iṭ → 6.1.77 niny-i-va
```

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `ed7d4ef420ae9f09c27c893e21a3dae232365ca0bfde5c5f1bc5ad3c152702b9` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pins `ebdf15ca…` (theorum/130, commit 6e8c213) and `e9773755…` (theorum/129) stay in the history. Re-pinned again by theorum/132 (the vikaraṇa classes); commit e638644 holds this pin. Re-pinned again by theorum/143 (the open lane closed); commit 09ee5f5 holds the 3f67387f… pin.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine -v
```

## 4. Claim boundary

```text
liṭ OF bhū, gam, kṛ, nī ON THE 20 CERTIFIED CELLS FROM TWELVE ROWS; THE ABHYĀSA AS A SEGMENT; 1.2.5 AS A PREDICATE; 75 ROWS ON 325 CELLS   PROVED
THE PADA AND seṭ / aniṭ OF kṛ (DHĀTUPĀṬHA), 7.2.13 AS A DECLARED LIST                                                                       DECLARED
7.4.60 (NO CLUSTER-INITIAL ROOT CERTIFIED), liṭ ĀTMANEPADA (3.4.81), thal / athus / a CELLS, 1.2.6 / 7.2.62 OPTIONS                           NOT CLAIMED
RH, YM                                                                                                                                        UNTOUCHED
```
