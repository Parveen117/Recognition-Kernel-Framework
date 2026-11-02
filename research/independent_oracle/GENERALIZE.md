# Generalisation test — the tiṅ engine on 7,052 cells outside its suite, against vidyut-prakriya 0.4.0

2 November 2026. `generalize.py` derives, for every (root, pada) the engine declares, the full nine-cell paradigm in every lakāra the engine covers for that class, drops the cells that are in the certified / declared suite, and compares the rest with vidyut. Pinned output: `GENERALIZE.json` (sha256 `f667a6c9edb0c844e1e3f3deab41d081eb24ce50256eb1a36c0b5c5b13f33568`).

| lakāra | class | cells | agree | differ | note |
|---|---|---|---|---|---|
| laṭ | bhvādi | 45 | 45 | 0 | |
| laṭ | classes 2–10 | 1,238 | **1,238** | **0** | after the five row corrections below |
| lṛṭ | bhvādi | 45 | 45 | 0 | |
| āśīrliṅ | bhvādi | 45 | 45 | 0 | |
| luṅ | bhvādi | 45 | 44 | 1 | aidhidhvam: the sic before dhvam (8.3.78 / 8.3.79) — not claimed |
| luṭ | bhvādi | 45 | 36 | 9 | gantā: 8.3.23 *mo 'nusvāraḥ* before tās — no suite cell exercises it, so the row is not added; not claimed |
| laṅ | bhvādi | 63 | 63 | 0 | |
| laṅ | classes 2–10 | 1,800 | 1,499 | 292 | **the open lane**: rows fitted on laṭ only |
| loṭ | bhvādi | 63 | 63 | 0 | |
| loṭ | classes 2–10 | 1,800 | 1,367 | 424 | the open lane |
| liṅ | bhvādi | 66 | 63 | 0 | 3 engine errors (as in vidhiliṅ) |
| liṅ | classes 2–10 | 1,797 | 920 | 868 | the open lane |

(27 cells vidyut cannot derive — śās — are excluded from the counts.)

## What laṭ generalisation found and fixed (engine re-pinned by theorum/138)

Five rows were right on the suite and wrong one cell away:

1. **8.2.37** bhaṣ-bhāva reached across the vikaraṇa (bhadhnāsi, dhabhnoṣi, ghudhnāsi): the jhaṣ must stand immediately before the s / dhv.
2. **8.2.41** ṣ → k reached across the vikaraṇa (ikṇāsi, puṣṇāsi …): same correction.
3. **7.1.102** *ud oṣṭhyapūrvasya* fired on the kryādi mṝ (murṇītaḥ) where 7.3.80's hrasva has the field (mṛṇītaḥ).
4. The tripādī block was in the wrong internal order — 8.3.24 / 8.4.2 / 8.4.58 ran before 8.2.26 / 8.2.30 (riñktaḥ for riṅktaḥ, kaṁdhve for kandhve); the rows now run in sūtra order, 8.2.x before 8.3.x before 8.4.x, with 8.4.41 / 8.3.13 the one deliberate exception already recorded.
5. **8.2.29** also before the 2s of āśīrliṅ (bhūyāḥ); **8.2.26** also for the s of tās before dhve (labdhādhve); **6.1.90** for every initial vowel (āḍ ajādīnām on īś, ūrṇu, ṛ).

After these, every laṭ cell the engine produces for its 150-odd declared (root, pada) pairs agrees with the independent generator, in and out of the suite.

## After theorum/139 (the open lane built from this map)

| lakāra | classes 2–10 | agree | differ |
|---|---|---|---|
| laṅ | 1,852 | 1,793 | 59 |
| loṭ | 1,854 | 1,768 | 86 |
| liṅ | 1,853 | 1,692 | 161 |

Overall 6,706 / 7,052 unseen cells (GENERALIZE.json re-pinned: sha256 `2313421a…`). The residue is named in theorum/139.

## After theorum/140 (the second pass)

| lakāra | classes 2–10 | agree | differ |
|---|---|---|---|
| laṅ | 1,852 | 1,811 | 41 |
| loṭ | 1,854 | 1,809 | 45 |
| liṅ | 1,853 | 1,792 | 61 |

Overall 6,865 / 7,052 unseen cells (GENERALIZE.json re-pinned: sha256 `23f925a6…`).

## After theorum/143 (the open lane closed)

| lakāra | unseen cells | agree | differ | generator empty |
|---|---|---|---|---|
| laṭ | 1,283 | 1,283 | 0 | 0 |
| laṅ | 1,863 | 1,854 | 0 | 9 |
| loṭ | 1,863 | 1,854 | 0 | 9 |
| liṅ | 1,863 | 1,854 | 0 | 9 |
| lṛṭ | 45 | 45 | 0 | 0 |
| luṭ | 45 | 36 | 9 (gantā: 8.3.23 not claimed) | 0 |
| luṅ | 45 | 44 | 1 (aidhidhvam: not claimed) | 0 |
| āśīrliṅ | 45 | 45 | 0 | 0 |

Overall 7,015 / 7,052 unseen cells (GENERALIZE.json re-pinned: sha256 `f2b10f64…`). The present-system residue of theorum/139–140 is gone: the open lane (VIDYUT_OPEN_LANE.json, 5,373 cells) is 5,373 / 5,373.

## The open lane (as measured by theorum/138)

laṅ, loṭ and vidhiliṅ of the non-śap classes: the rows for those lakāras were fitted on a-final stems (7.2.80 *ato yeyaḥ*, 6.4.105 *ato heḥ*, 3.4.92's āṭ against an a) and the consonant- and vowel-final stems of classes 2–9 need their own — the yā of liṅ kept with 6.4.?? before us (adyuḥ), 6.4.101 *hujhalbhyo her dhiḥ* (juhudhi, addhi), the 7.3.99 / 7.3.100 īṭ / aṭ of the apṛkta in laṅ (āsīt, ādat), 7.4.21's śī in laṅ, the ḍh of 8.2.40 at the end of the pada (adhok), 6.4.111's a in laṅ 3p (āsan), ātmanepada loṭ of consonant stems … — each with vidyut's own citation list in GENERALIZE.json as the map of what is missing. This is the next packet; the numbers above are its baseline.
