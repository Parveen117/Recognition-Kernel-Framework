# Tiṅ Rule-Table Engine IX — the open lane: laṅ, loṭ and vidhiliṅ of classes 2–10 from the strong-ending predicate and nine rows (5,064 / 5,373 generator cells; 154 rows; 6,706 / 7,052 unseen cells overall)

2 November 2026. theorum/138 measured the present-system lakāras of the non-śap classes at 3,786 / 5,397 and named the missing rows from the generator's own citations. This packet builds them. One predicate did most of the work: the ending that licenses guṇa and blocks the lopa rules is the **strong** one — pit and not ṅit (1.2.4; 3.4.103 for liṅ), with 3.4.92's āṭ making the loṭ uttama pit — and every guṇa / lopa row (7.3.84, 7.3.84v, 7.3.86, 6.4.110, 6.4.111, 6.4.112, 6.4.113) now reads it instead of the bare pit flag; so cinavāni and juhavāni take the guṇa (āṭ: pit), cinuyāt and dhṛṣṇuyāt do not (liṅ: ṅit), bhindyāt drops the a (liṅ) where bhinatti kept it. The next-sound readers (6.4.77, 6.4.87, 6.4.112, 6.4.113, 6.1.77's u) read the yāsuṭ / sīyuṭ as the sound that follows the aṅga, so aśnuvīta, cinvīta, dadhyāt and krīṇīyāt come from the rows that already existed. The augment goes before the abhyāsa (ajuhot, abibharam). Nine rows are added: 6.1.96 *usy apadāntāt* (adyuḥ, juhuyuḥ), 6.4.101 *hujhalbhyo her dhiḥ* (juhudhi, addhi, runddhi), 6.4.119 (dehi, dhehi, edhi), 7.3.83 *jusi ca* with 3.4.109 reaching the abhyasta in laṅ (abibhayuḥ, ajuhavuḥ), 8.2.24 *rāt sasya* (abibhaḥ), 7.3.100 *adaḥ sarveṣām* (ādat), 3.1.83 *halaḥ śnaḥ śānaj jhau* (aśāna, badhāna), 6.4.106 (sunu, tanu, kuru), and 7.3.96 reaching as (āsīt); 8.2.23 generalised to the pada-final conjunct (abhinat), 6.1.101 to ā + ā, 6.1.78 to the vikaraṇa's o (aśnavai), the jhal rows of 8.2 kept off the augment (duhyāt, not *dughyāt).

## 1. The oracle, and how it loads the rows

The cells are the independent generator's: `research/independent_oracle/VIDYUT_OPEN_LANE.json` holds every laṅ / loṭ / vidhiliṅ cell vidyut-prakriya derives for the engine's declared roots of classes 2–10 (5,373 cells, all alternatives, in the repository as data). This is a DECLARED oracle of a different grade from the suite's — an implementation, not a commentary anchor — and it is treated accordingly: the certificate reports the agreement as a fraction (`open_lane`), PASS does not require it, and a row that no suite cell loads counts as load-bearing only if an *agreeing* open-lane cell loads it. Nothing is selected: the 309 disagreeing cells are listed in the certificate.

## 2. Result

```text
                 theorum/138 baseline      this packet
laṅ   (1,791)        1,499                   1,730
loṭ   (1,791)        1,367                   1,705
liṅ   (1,791)          920                   1,629
                     3,786 / 5,373           5,064 / 5,373
```

On the full generalisation run (theorum/138's 7,052 unseen cells, re-pinned as `GENERALIZE.json` sha256 `2313421a…`): **6,706 / 7,052**, with laṭ, lṛṭ and āśīrliṅ still complete. The suite (908 cells) is unchanged and every one of the 154 rows is load-bearing but the two declared.

## 3. The residue, named

309 open-lane cells: kṛ (the loṭ / liṅ of karoti beyond the suite: kurvīta, kuryāt — 6.4.110 against the sīy), viṣ / dviṣ / vij / nij (the ṣ / j before the yāsuṭ and dhvam: dviṣyāt, vevikṣva), chṛd / ṝ / tan / san / kṣaṇ in laṅ (the apṛkta after a cluster: acchṛṇat, ārṇot), hā / daridrā (the 6.4.116 / 6.4.114 option cells), han (ahan, jahi: 6.4.36 / 8.2.?), as in liṅ (syāt: the lopa before the yāsuṭ), īḍ / brū (the īṭ cells), ūrṇu (7.3.90's second branch). Each is one or two rows; they are the next iteration of the same loop, and none is claimed here.

## 4. Certificate

`proof_lab/ting_rule_table_engine.py` re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `be902838c55159fc82878effd7b6b6b460778ca7b1a45590316b96ba8ad649a0` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`; 154 rows, 908 suite cells, open-lane 5,064 / 5,373 reported); the previous pin `a6b031c8…` (theorum/138, commit 5b30c93) stays in the history; re-pinned again by theorum/140 (the second pass), commit 769da4f holds this pin. The suite cross-check of theorum/137 is byte-identical on this pin.

## 5. Claim boundary

```text
THE STRONG-ENDING PREDICATE AND NINE ROWS; THE SUITE UNCHANGED (908 / 908); 154 ROWS ALL LOAD-BEARING BUT THE TWO DECLARED                 PROVED
laṅ / loṭ / vidhiliṅ OF CLASSES 2–10: 5,064 / 5,373 OF THE GENERATOR'S CELLS; 6,706 / 7,052 UNSEEN CELLS OVERALL                          CHECKED (PINNED OUTPUT)
VIDYUT_OPEN_LANE.json AS A DECLARED ORACLE OF IMPLEMENTATION GRADE                                                                        DECLARED
THE 309 RESIDUE CELLS OF §3                                                                                                              NOT CLAIMED
RH, YM                                                                                                                                    UNTOUCHED
```
