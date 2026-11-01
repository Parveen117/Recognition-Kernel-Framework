# Luṅ (the Aorist) Parasmaipada Compiled — three aorist shapes on three pinned roots; the ḷ-it of gamḷ~ load-bearing through 3.1.55

1 November 2026. Seventh lakāra. The aorist is where Pāṇini's teaching-form
markers earn their keep: gam is written *gamḷ~* in the Dhātupāṭha, and that
ḷ-it — read by theorum/82 — is what 3.1.55 looks at to replace sic by aṅ
(agamat); bhū drops its sic altogether (2.4.77) and takes vuk before vowels
(6.4.88: abhūvan); nī keeps sic and goes through vṛddhi (7.2.1), īṭ (7.3.96),
ṣatva / ṣṭutva and jus (anaiṣīt, anaiṣṭām, anaiṣuḥ).

## 1. Sources (quoted)

```text
3.2.110 luṅ    3.1.43 cli luṅi    3.1.44 cleḥ sic    3.1.55 puṣādidyutādyḷditaḥ parasmaipadeṣu    2.4.77 gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu
6.4.88 bhuvo vug luṅliṭoḥ    7.2.1 sici vṛddhiḥ parasmaipadeṣu    7.3.96 astisico 'pṛkte    8.3.59 ; 8.4.41 ṣṭunā ṣṭuḥ    3.4.109 sijabhyastavidibhyaś ca
6.4.71 ; 3.4.100 ; 3.4.101 ; 3.4.99 ; 7.1.3 ; 8.2.23 ; 7.3.101 ; 7.2.10 ; 8.2.66 ; 8.3.15 ; 1.3.2–1.3.9
```

## 2. Results

**T1.** abhūt, abhūtām, abhūvan; abhūḥ, abhūtam, abhūta; abhūvam, abhūva, abhūma —
agamat, agamatām, agaman; agamaḥ, agamatam, agamata; agamam, agamāva, agamāma —
anaiṣīt, anaiṣṭām, anaiṣuḥ; anaiṣīḥ, anaiṣṭam, anaiṣṭa; anaiṣam, anaiṣva,
anaiṣma: **27/27**. Each stage breaks exactly its cells on exactly the root it
governs: 2.4.77 all nine of bhū and nothing of gam / nī; 6.4.88 {3p, 1s} of
bhū; **3.1.55 all nine of gam and nothing else**; 7.2.1 and 8.3.59 all nine of
nī; 7.3.96 {3s, 2s}; 8.4.41 {3d, 2d, 2p}; 3.4.109 {3p}; 7.3.101 {1d, 1p} of gam.

## 3. Certificate

```text
python -m proof_lab.lun_parasmaipada_compiled
python -m unittest proof_lab.test_lun_parasmaipada_compiled -v
```
Status `PASS_LUN_PARASMAIPADA_COMPILED_CANDIDATE`, SHA-256 `2e5af3d79ef6d321f922d0cb3b140cefd2df8e6646e76dc2054d23b628895bc0`
(`proof_lab/LUN_PARASMAIPADA_COMPILED_EXPECTED.sha256`). Imports theorum/80, 82.

## 4. Claim boundary

```text
LUṄ PARASMAIPADA OF bhū, gam, nī: 27 FORMS; EACH STAGE ON EXACTLY ITS CELLS AND ROOT       PROVED
THE ḷ-IT OF gamḷ~ (1.3.2) LOAD-BEARING THROUGH 3.1.55                                       PROVED
ksa / cāṅ / ciṇ / siṣ AORISTS, ĀTMANEPADA, 6.4.72, puṣādi / dyutādi GAṆAS, OTHER ROOTS     NOT CLAIMED
STAGE ORDER A DECLARED PIPELINE ; RH, YM UNTOUCHED
```
