# Rule-Table Engine XV — the karmaṇi: the passive present system of every declared root, 6,912 / 6,948

3 November 2026. theorum/110 built the passive as a separate construction on a handful of roots. Here it enters the one verbal table as a *state of the aṅga*, not a second engine: 3.4.69 *laḥ karmaṇi ca bhāve cākarmakebhyaḥ* names the prayoga; 1.3.13 *bhāvakarmaṇoḥ* gives it the ātmanepada; 3.1.67 *sārvadhātuke yak* is one row — a kit vikaraṇa that stands where the gaṇa's vikaraṇa would, so that śap / śyan / śnu / śnā / u / ṇic, the luk and ślu of adādi and juhotyādi, the śnam of rudhādi and every sārvadhātuka-only row (6.4.34, 6.4.114, 7.4.21, 7.3.74 …) stay off. What the kit y-initial ārdhadhātuka requires of the root is what āśīrliṅ's yāsuṭ (3.4.104) already required in theorum/144: those rows are generalised through one predicate, `_kity(s)` — "before the kit y-initial ārdhadhātuka: the yāsuṭ of āśīrliṅ in parasmaipada, or yak" — and the passive falls out of the table that was already there.

## 1. The rows

```text
3.1.67   sārvadhātuke yak (+ 3.4.69, 1.3.13)                 bhūyate, nīyate, adyate, rudhyate, sūyate, hiṁsyate, śāsyate, bhūyete, bhūyeta, bhūyai, abhūyata
7.4.28   riṅ śayagliṅkṣu                                      kriyate, bhriyate, priyate
7.4.29   guṇo 'rtisaṁyogādyoḥ                                 staryate, smaryate; aryate
7.4.25   akṛtsārvadhātukayor dīrghaḥ                          cīyate, śrūyate, hūyate, sūyate, stūyate, īyate
7.1.100 / 7.1.102 (+ 8.2.77)                                  kīryate, stīryate, īryate; pūryate, mūryate, vūryate
6.4.66   ghumāsthāgāpājahātisāṁ hali                          dīyate, dhīyate, sthīyate, hīyate (hāk), mīyate (mā and 6.1.50's mā)
6.1.15 / 6.1.16 / 6.4.2                                       ucyate, supyate, gṛhyate, jīyate
6.4.24   aniditāṁ hala upadhāyāḥ kṅiti                       badhyate, mathyate, skabhyate
7.3.85 / 6.4.51 / 2.4.52 / 2.4.53 / 2.4.42                    jāgaryate, coryate, bhūyate (as), ucyate (brū), vadhyeta (the vidhiliṅ after the ārdhadhātuka yak)
7.4.22   ayaṅ yi kṅiti                                        śayyate
6.4.44   tanoter yaki (+ 6.4.42 / 6.4.43)                     tāyate, sāyate — the ā branch realised; tanyate, sanyate recorded (declared surface-coincident, §3)
```

The readers that the earlier packets had set to the next sound after the aṅga now read the sound after the root where the rule is a root rule (6.4.37, 6.4.98, 6.4.81: hanyate, hanyete, īyete); the idit nuṁ and 8.3.24 stand before yak (hiṁsyate, kaṁsyate); 6.1.90's vṛddhi waits for 7.1.100's ir (airyata); 7.2.77 / 7.2.78 read the se / dhve directly after the root (īśyase).

## 2. Results

```text
lane                cells   agree
karmaṇi laṭ         1,737   1,728    (daridrā ×9 in each: the ā-lopa before the ārdhadhātuka is a vārttika's — not claimed)
karmaṇi laṅ         1,737   1,728
karmaṇi loṭ         1,737   1,728
karmaṇi vidhiliṅ    1,737   1,728
```

The kartari lanes and the suite are unchanged (5,373 / 5,373; 1,845 ×4, 1,799, 1,854; 908 / 908); 224 rows, all load-bearing on the suite or an agreeing cell of one of the three lanes except the seven declared surface-coincident (3.4.92, 7.1.58, 8.4.56, 6.4.2, 3.1.57, 7.3.73, 6.4.44).

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); re-pinned again by theorum/148 (the ṇic), commit 24a2086 holds this pin; the previous pin `95d065ae…` (theorum/146, commit db16084) and the chain before it stay in the history. The certificate carries `karmani_lane` beside `open_lane` and `ardhadhatuka_lane`. The kernel re-pinned: `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `691ca9459edbfe2341c4773a258eb6847a4cbda89933c49aa335357bb39128d5`.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine proof_lab.test_panini_kernel -v
python -m research.independent_oracle.karmani_lane --data <vidyut data>   # regenerates the lane file (not in CI)
```

## 4. Claim boundary

```text
THE KARMAṆI PRESENT SYSTEM OF 193 ROOTS: 6,912 / 6,948 FROM yak AND THE ROWS OF §1; 224 ROWS LOAD-BEARING (7 DECLARED)   PROVED on the suite, DECLARED on the lane
6.4.44 / 6.4.43 (ONE BRANCH REALISED)                                                                                  OPTION RECORDED
daridrā (A VĀRTTIKA), THE bhāve PRAYOGA AS A SEPARATE READING, THE KARMAṆI OF THE ĀRDHADHĀTUKA LAKĀRAS (3.1.66 ciṇ, 6.4.62)   NOT CLAIMED
RH, YM                                                                                                                 UNTOUCHED
```
