# The Sup Generalisation Test — 48 new stems of every declared class against vidyut-prakriya: 1,068 / 1,078 cells, two rows the test exposed (the kṣ token in ṇatva; 7.1.25), the ten others the generator's

2 November 2026. theorum/138–140 did for the verbal table what this packet does for the nominal one: run the rows on stems they were never fitted to. 48 stems were chosen across every class the sup engine declares — a-stems (deva, nara, vṛkṣa, putra; jñāna, vana, puṣpa), āp (senā, kanyā, māyā), nadī (devī, gaurī, vāpī), i / u in three genders (muni, agni, kavi, śakti, buddhi, śatru, bhānu, sādhu, ambu, aśru), ṛ (dātṛ, bhartṛ, naptṛ with the tṛ flag; bhrātṛ, duhitṛ without), an (brahman, karman, nāman, yajvan), consonant stems (suhṛd, jagat, sarit, vidyut), s (payas, tejas, yaśas), in (yogin, hastin, balin), sarvanāma (anya in three genders, viśva, eka, pūrva, para) — 1,078 cells, all compared with vidyut-prakriya (`research/independent_oracle/generalize_sup.py`; `GENERALIZE_SUP.json` pinned by hash).

## 1. Result

**1,068 / 1,078.** The ten others: devīḥ, gaurīḥ, vāpīḥ (the generator's nadī 1s, as nadīḥ in theorum/137 — 6.1.68 drops the su), ekāya / ekāt / eke / ekāḥ / ekānām (the generator declines eka as a plain a-stem; eka is sarvādi, ekasmai), ambo / aśro against ambu / aśru (the neuter vocative option, as in theorum/137). No engine form wrong after the two corrections below.

## 2. What the test exposed (engine re-pinned)

1. The ṇatva scanner did not see the ṣ inside the kṣ token (vṛkṣena, vṛkṣānām) — the same blindness the verbal engine had at kṣuṇatti, fixed the same way.
2. **7.1.25** *adḍ ḍatarādibhyaḥ pañcabhyaḥ* was missing: the neuter su / am of anya, anyatara, itara, ḍatara, ḍatama is ad (anyat, anyad), with 7.1.24 yielding to it.

The 1,078 cells are kept in the repository as `VIDYUT_SUP_LANE.json` — a declared oracle of implementation grade, as in theorum/139 — reported as `sup_lane` in the certificate and loading rows only where they agree; the suite's 861 cells and all 94 rows are unchanged and all load-bearing.

## 3. Certificate

`proof_lab/sup_rule_table_engine.py` re-pinned: `proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256` = `90dd54de973176a173a5a7644dcaae9aa65c797f9e3a7a15b481cec9935dd5dc` (status `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE`; 94 rows, 861 suite cells, sup_lane 1,068 / 1,078 reported); the previous pin `d6d7c356…` (theorum/128, commit 9ff31fe) stays in the history. theorum/137's suite cross-check re-run on this pin is byte-identical.

## 4. Claim boundary

```text
48 NEW STEMS, 1,068 / 1,078 CELLS AGREE WITH THE INDEPENDENT GENERATOR; THE TEN OTHERS ADJUDICATED; TWO ROWS CORRECTED / ADDED   CHECKED (PINNED OUTPUT)
VIDYUT_SUP_LANE.json AS A DECLARED ORACLE OF IMPLEMENTATION GRADE; THE CLASS FLAGS OF EACH NEW STEM                                  DECLARED
adas, THE ugit AND matup STEMS BEYOND bhavat, THE ṅīṣ / ṅīn FEMININES, THE DUAL-ONLY STEMS                                             NOT CHECKED
RH, YM                                                                                                                                 UNTOUCHED
```
