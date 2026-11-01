# Samāsa Compiled — tatpuruṣa, karmadhāraya, dvandva, bahuvrīhi from sup-ending padas (2.4.71, 1.2.43 / 2.2.30, 8.2.7, junction sandhi, 5.4.91 ṭac) and the compound declined

2 November 2026. Compounding. Twelve classical compounds built from their two
sup-ending members exactly as 2.1.4 *saha supā* describes, the inner sup
deleted by 2.4.71, the upasarjana placed first by 1.2.43 / 2.2.30 (the dvandva
by 2.2.34), the junction sandhi and the pūrvapada's 8.2.7 applied — then the
compound stem handed to the existing declension engines (theorum/63, 91, 93).

## 1. Sources (quoted)

```text
2.1.3 prāk kaḍārāt samāsaḥ   2.1.4 saha supā   2.1.22 tatpuruṣaḥ   2.1.24 dvitīyā śritā…   2.1.36 caturthī tadartha…   2.1.37 pañcamī bhayena   2.1.40 saptamī śauṇḍaiḥ   2.2.8 ṣaṣṭhī
1.2.42 tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ   2.2.23 śeṣo bahuvrīhiḥ   2.2.24 anekam anyapadārthe   2.2.29 cārthe dvandvaḥ
1.2.43 prathamānirdiṣṭaṁ samāsa upasarjanam   2.2.30 upasarjanaṁ pūrvam   2.2.34 alpāctaram   2.4.71 supo dhātuprātipadikayoḥ   1.2.46   2.4.26 paraval liṅgaṁ dvandvatatpuruṣayoḥ
1.4.14   1.1.62   8.2.7 nalopaḥ prātipadikāntasya   6.1.87 ād guṇaḥ   6.1.101 akaḥ savarṇe dīrghaḥ   1.1.51 ur aṇ raparaḥ
6.3.46 ān mahataḥ samānādhikaraṇajātīyayoḥ   5.4.91 rājāhaḥsakhibhyaṣ ṭac   6.4.144 nas taddhite   1.2.48 gostriyor upasarjanasya   8.4.1 raṣābhyāṁ no ṇaḥ samānapade   8.4.2
```

## 2. Results

**T1.** rājapuruṣa (2.2.8; 8.2.7 on the pūrvapada, a pada by 1.4.14 with
1.1.62), kṛṣṇaśrita (2.1.24), yūpadāru (2.1.36), vṛkabhaya (2.1.37),
akṣaśauṇḍa (2.1.40), devālaya (2.2.8; 6.1.101), nīlotpala (1.2.42; 6.1.87),
rājarṣi (1.2.42; 8.2.7, 6.1.87 with 1.1.51), mahārāja (1.2.42; 6.3.46, 5.4.91
ṭac, 6.4.144), pītāmbara (2.2.24; 6.1.101), citragu (2.2.24; 1.2.48),
rāmalakṣmaṇa (2.2.29; 2.2.34 from the vigraha order lakṣmaṇa, rāma) — 12/12.
Three tatpuruṣas are given in the wrong vigraha order and are put right by
1.2.43 / 2.2.30 alone (without it exactly those three break); 2.4.71 breaks
all twelve; every other rule breaks exactly the compounds named.

**T2.** rājapuruṣa declined on theorum/63's resolver ladder: 21 cells equal the
classical paradigm. theorum/63's own 8.4.2 rule looks only for an r trigger, so
the ṣ-trigger of 8.4.1 is supplied after the ladder by theorum/91's ṇatva
(recorded): without it exactly 3s rājapuruṣeṇa and 6p rājapuruṣāṇām break.
rāmalakṣmaṇau (1d, 2d); citragu on theorum/91 (citraguḥ, citraguṇā, citragoḥ);
nīlotpala neuter by 2.4.26 on theorum/93 (nīlotpalam, nīlotpalāni).

## 3. Certificate

```text
python -m proof_lab.samasa_compiled
python -m unittest proof_lab.test_samasa_compiled -v
```
Status `PASS_SAMASA_COMPILED_CANDIDATE`, SHA-256 `d23a43e951dd5217e30315dabe4cc4ff3d95d24f6ea6a35e51675bb0933eeec4`
(`proof_lab/SAMASA_COMPILED_EXPECTED.sha256`). Imports theorum/63, 80, 91, 93.

## 4. Claim boundary

```text
12 COMPOUNDS FROM SUP-ENDING MEMBERS; EACH RULE BREAKS EXACTLY THE COMPOUNDS STATED          PROVED
rājapuruṣa 21 CELLS, rāmalakṣmaṇau, citragu, nīlotpala ON THE EXISTING ENGINES               PROVED
KIND OF COMPOUND / VIDHI SŪTRA; ORDER OF karmadhāraya AND bahuvrīhi MEMBERS                  DECLARED
OTHER samāsānta AFFIXES, ACCENT 6.1.223, dvigu, avyayībhāva, ekaśeṣa, dvandva NUMBER         NOT CLAIMED
RH, YM                                                                                       UNTOUCHED
```
