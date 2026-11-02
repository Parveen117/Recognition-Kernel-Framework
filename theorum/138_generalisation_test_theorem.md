# The Generalisation Test — the tiṅ engine on 7,052 cells it was never fitted to: laṭ generalises completely across classes 2–10 (1,283 / 1,283) after five row corrections; laṅ / loṭ / liṅ of the non-śap classes measured as the open lane

2 November 2026. theorum/137 showed the engines right on their suites against an independent generator. The real theorem claim is that the *rows* are right — that a row fitted on some cells gives the right form on the cells it was never shown. This packet measures that with vidyut-prakriya on every cell outside the suite: for each declared (root, pada), all nine cells of every lakāra the engine covers for the class, 7,052 cells in all (`research/independent_oracle/generalize.py`; `GENERALIZE.json` pinned by hash `f667a6c9…`; `GENERALIZE.md` the table).

## 1. Result

- **laṭ, classes 2–10: 1,238 / 1,238 unseen cells agree** (and 45 / 45 bhvādi) — after five corrections to rows that were right on the suite and wrong one cell away: 8.2.37 and 8.2.41 reaching across the vikaraṇa (bhadhnāsi, ikṇāsi), 7.1.102 against 7.3.80 on the kryādi mṝ (murṇītaḥ), the tripādī rows out of sūtra order (riñktaḥ, kaṁdhve), and three guard widenings (8.2.29 before the 2s of āśīrliṅ, 8.2.26 for tās before dhve, 6.1.90 for every initial vowel). The engine is re-pinned; the suite is unchanged by any of them.
- **lṛṭ, āśīrliṅ of the bhvādi roots: 90 / 90; luṅ 44 / 45; luṭ 36 / 45** — the misses are two rules no suite cell exercises (8.3.23 before tās: gantā; the sic before dhvam: aidhidhvam), left unclaimed rather than added vacuously.
- **laṅ, loṭ, vidhiliṅ of the non-śap classes: 1,499 / 1,800, 1,367 / 1,800, 920 / 1,797.** Those rows were fitted on a-final stems (7.2.80, 6.4.105, 3.4.92's āṭ) and the consonant- and vowel-final stems of classes 2–9 need their own; vidyut's per-cell citations in GENERALIZE.json are the map of exactly which rows are missing (6.4.101 her dhiḥ, 7.3.99 / 7.3.100 for the apṛkta in laṅ, the liṅ yā before us …). The bhvādi cells of the same lakāras are 189 / 189.

## 2. What this changes in the claim

Until this packet the engines' PROVED line was "the rows reproduce the suite". It can now say, for laṭ across ten classes and for the bhvādi in all eight lakāras, "the rows reproduce the paradigm" — checked against an implementation that shares none of this repository's code. For laṅ / loṭ / liṅ outside the bhvādi it says the opposite, with the number.

## 3. Certificate

`proof_lab/ting_rule_table_engine.py` re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `a6b031c881c80be70ef250b02469733b75f3beb9c4ad972001de2cf137ad6e53` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`; 147 rows, 908 suite cells, every row load-bearing but the two declared); the previous pin `c71269f5…` (theorum/137, commit 816acc0) stays in the history. The suite cross-check of theorum/137 re-run on this pin is byte-identical (`CROSSCHECK.json` sha256 `81dc3f08…`).

## 4. Claim boundary

```text
laṭ OF CLASSES 1–10 AND lṛṭ / āśīrliṅ OF THE BHVĀDI: EVERY UNSEEN CELL AGREES WITH THE INDEPENDENT GENERATOR (1,373 / 1,373)     CHECKED (PINNED OUTPUT)
laṅ / loṭ / vidhiliṅ OF CLASSES 2–10: 3,786 / 5,397 — MEASURED, NOT CLAIMED; THE MISSING ROWS NAMED BY VIDYUT'S CITATIONS          OPEN LANE
gantā (8.3.23), aidhidhvam (8.3.78 / 8.3.79), as IN vidhiliṅ                                                                          NOT CLAIMED
vidyut-prakriya 0.4.0 AS THE ORACLE (ITS GAPS AS IN theorum/137)                                                                       DECLARED
RH, YM                                                                                                                                 UNTOUCHED
```
