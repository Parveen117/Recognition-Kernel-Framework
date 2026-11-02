# Rule-Table Engine XII — the Dhātupāṭha pinned, and the ārdhadhātuka lane: lṛṭ, luṭ, āśīrliṅ of every declared root, 1,845 / 1,854 each

2 November 2026. Two things the verbal engine had been borrowing are now read from the primary text. First, the seṭ / aniṭ division: theorum/130 declared `SET = {bhū, edh}` and let every other root be aniṭ by fiat. 7.2.10 *ekāca upadeśe 'nudāttāt* says where the fact lives — in the accent of the upadeśa — and the upadeśa is the Dhātupāṭha. The Dhātupāṭha is now in the repository (`research/panini_grammar/DHATUPATHA.tsv`: ashtadhyayi.com's list, 2,259 records with the accent and anubandha marks, as packaged with vidyut-prakriya 0.4.0 under its MIT licence; sha256 `bb2013ead0ea536dc7f887164c385c703cb0014ccf6e5af35b87e6d3049ba380`, recorded in the module as `DHATUPATHA_SHA256`), every declared root is looked up in it by its upadeśa and gaṇa (193 of 194 directly; śru is the bhvādi record, 3.1.74 gives it śnu), and `anudatta()` reads the mark: a backslash after a root vowel is the anudātta of 7.2.10 → aniṭ; the mark after the ~ it-vowel is the pada accent of 1.3.12 / 1.3.72 and is not read for iṭ. The suite is unchanged by the substitution (908 / 908): the declared list and the accent agree on every certified root.

Second, the ārdhadhātuka lakāras beyond bhvādi. theorum/130 built lṛṭ, luṭ, āśīrliṅ, luṅ on five roots; `research/independent_oracle/ardhadhatuka_lane.py` now lists, for all 194 declared (root, pada), every lṛṭ / luṭ / āśīrliṅ / liṭ / luṅ / lṛṅ cell the independent generator derives (`VIDYUT_ARDHADHATUKA_LANE.json`, 11,119 cells; a DECLARED oracle of implementation grade, as in theorum/139). This packet closes the first three columns.

## 1. The rows

```text
2.4.52   aster bhūḥ                                  bhavitā, bhaviṣyati, bhūyāt (as → bhū before the ārdhadhātuka)
2.4.53   bruvo vaciḥ                                 vaktā, vakṣyati, ucyāt
2.4.42   hano vadha liṅi  + 6.4.48 ato lopaḥ         vadhyāt (and avadhīt in luṅ)
7.2.70   ṛddhanoḥ sye                                kariṣyati, bhariṣyati, stariṣyati, haniṣyati
7.2.37   graho 'liṭi dīrghaḥ                         grahītā, grahīṣyati
6.1.50   mīnātiminotidīṅāṁ lyapi ca (6.1.45)         māsyati, mātā; mīyāt with 6.4.66
7.3.86   (before sya / tās / iṭ)                      bhetsyati, rotsyati, deviṣyati, dhokṣyati, notsyati
7.3.84   (before the non-kit sīyuṭ)                   ceṣīṣṭa, stoṣīṣṭa, kreṣīṣṭa; dhaviṣīṣṭa, laviṣīṣṭa with iṭ
7.4.25   akṛtsārvadhātukayor dīrghaḥ                 stūyāt, cīyāt, hūyāt, īyāt, nūyāt
7.4.28   riṅ śayagliṅkṣu                             kriyāt, bhriyāt, priyāt (the i not lengthened: the later special rule)
7.4.29   guṇo 'rtisaṁyogādyoḥ                        staryāt
7.3.85   jāgro 'viciṇṇalṅitsu                        jāgaryāt
7.1.100  ṝta id dhātoḥ (+ 8.2.77)                     kīryāt, stīryāt, īryāt; vūryāt by 7.1.102 (v is oṣṭhya)
6.4.67   er liṅi (under 6.4.66)                      deyāt, dheyāt, meyāt, heyāt — not the adādi pā rakṣaṇe (pāyāt)
6.4.66   ghumāsthāgāpājahātisāṁ hali                 mīyāt (the ā of 6.1.50)
6.1.15   vacisvapiyajādīnāṁ kiti                     ucyāt, supyāt
6.1.16   (before the kit too)                        gṛhyāt, jīyāt — with 6.4.2 halaḥ (declared surface-coincident with 7.4.25, §4)
6.4.24   aniditāṁ hala upadhāyāḥ kṅiti (kit too)     badhyāt, mathyāt, skabhyāt, stabhyāt, kuthyāt
6.4.51   ṇer aniṭi                                   coryāt (corayitā keeps the ṇi before iṭ)
8.3.78   iṇaḥ ṣīdhvaṁluṅliṭāṁ dho 'ṅgāt              bhṛṣīḍhvam, kṛṣīḍhvam; 8.3.79 vibhāṣeṭaḥ: stariṣīdhvam realised, stariṣīḍhvam recorded
8.3.24   (the m clause, ca)                          gantā, gantārau (8.4.58 reads it back to n; gamyāt keeps m)
```

The predicates: 3.4.104 *kid āśiṣi* is read as the yāsuṭ's (parasmaipada); the ātmanepada sīyuṭ is not kit — hence the guṇa of ceṣīṣṭa — except, jhal-initial, after the ṛ-final root (1.2.11 *liṅsicāv ātmanepadeṣu* with 1.2.12 *uś ca*: kṛṣīṣṭa; with iṭ, stariṣīṣṭa). The tripādī rows 8.2.31 / 8.2.32 / 8.2.36 / 8.2.37 / 8.2.41 / 8.4.41 / 8.3.13 now read the s of sya and of āśīrliṅ's sīyuṭ and the t of tās (dhokṣyati, dvekṣyati, lekṣyati, mārkṣyati, dhukṣīṣṭa, dveṣṭā, leḍhā); the `not s.pre` guards of theorum/143 are narrowed to vidhiliṅ, whose sīy has lost its s (7.2.79). 7.1.4 *ad abhyastāt* reads the jh directly after the abhyasta only (cakāsiṣyanti). 7.1.102 and 7.2.114 yield to the ārdhadhātuka guṇa (1.4.2: mariṣyati, mārjiṣyati).

## 2. Results

```text
lane column   cells   agree   left
lṛṭ           1,854   1,845   9   daridrā (daridriṣyati: the ā-lopa before the ārdhadhātuka is a vārttika's — not claimed)
luṭ           1,854   1,845   9   daridrā
āśīrliṅ       1,854   1,845   9   daridrā
liṭ           1,849     514       the next packet's baseline (3.4.81's ātmanepada liṭ, 6.1.17, 7.4.70 …)
luṅ           1,854   1,042       the sic family (3.1.44–57, 7.2.1–7, 8.2.28, 2.4.77 …)
lṛṅ           1,854       0       the lakāra is not yet in the table (3.3.139)
```

The present system stays at 5,373 / 5,373 and the suite at 908 / 908; 184 rows, every one load-bearing on the suite or an agreeing lane cell except the four declared surface-coincident (3.4.92, 7.1.58, 8.4.56, 6.4.2). The row-loading fallback now reads both lanes.

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `46c5b44185666b4fcdf3e64c87eacd8c9c00eec0d6854a57ec033743a7df69da` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pin `c8368071…` (theorum/143, commit 1d76875) and the chain before it stay in the history. The certificate carries `ardhadhatuka_lane` (cells, agreement per lakāra, the closed columns and their residue) beside `open_lane`. The kernel (theorum/142) re-pinned on the new table: `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `49ab58d885904ad90bffccf13f10d02820b7e7a06fe7126e73f9a3d22e72c451`.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine proof_lab.test_panini_kernel -v
python -m research.independent_oracle.ardhadhatuka_lane --data <vidyut data>   # regenerates the lane file (not in CI)
```

## 4. Claim boundary

```text
THE DHĀTUPĀṬHA PINNED; 7.2.10 READ OFF ITS ACCENT FOR EVERY DECLARED ROOT (THE SUITE UNCHANGED)                          PROVED (the file and the reading); DECLARED (the edition)
lṛṭ / luṭ / āśīrliṅ OF 194 (ROOT, PADA): 1,845 / 1,854 EACH, FROM THE ROWS OF §1; 184 ROWS LOAD-BEARING (4 DECLARED)       PROVED on the suite, DECLARED on the lane
6.4.2 SURFACE-COINCIDENT WITH 7.4.25 ON jīyāt                                                                            DECLARED
daridrā BEFORE THE ĀRDHADHĀTUKA (A VĀRTTIKA); 7.2.44 / 7.2.57 OPTIONS (ONE BRANCH REALISED); 8.3.79'S OPTION               NOT CLAIMED / RECORDED
liṭ, luṅ, lṛṅ OF THE SAME LANE (514 / 1,849; 1,042 / 1,854; 0 / 1,854)                                                   MEASURED, NOT CLAIMED
RH, YM                                                                                                                   UNTOUCHED
```
