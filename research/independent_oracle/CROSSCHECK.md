# Independent-oracle cross-check — the two rule-table engines against vidyut-prakriya 0.4.0

2 November 2026. `crosscheck.py` runs every cell of `proof_lab/sup_rule_table_engine.py` (theorum/125–128) and `proof_lab/ting_rule_table_engine.py` (theorum/129–136) through vidyut-prakriya (ambuda-org/vidyut, an independent open-source Pāṇinian generator that records the sūtra of every step) and compares both the surface form and the set of sūtras applied. Pinned output: `CROSSCHECK.json` (sha256 `81dc3f08367b0e58fc97547cf56ac25e2fd79146f2c12d09385fb998a3d74aac`). Not in CI (needs the vidyut package and its data download; the command is in the module docstring).

## Forms

| engine | cells run | agree | differ | no vidyut output | no vidyut input |
|---|---|---|---|---|---|
| tiṅ (908 cells) | 905 | **896** | **0** | 9 (śās: vidyut derives nothing) | 1 (śru: upadeśa key not matched) |
| sup (861 cells) | 839 | **832** | 7 | 0 | 22 (bhavat: the honorific pronoun has no vidyut input in this harness) |

The seven sup differences, adjudicated against the pinned sūtrapāṭha:

| cell | ours (= oracle) | vidyut | adjudication |
|---|---|---|---|
| nadī 1s | nadī | nadīḥ | ours: 6.1.68 *halṅyābbhyo dīrghāt sutisyapṛktaṁ hal* drops the su after the nadī ī |
| vāri 2p, tri (n) 2p | vārīṇi, trīṇi | vāriṇi, triṇi | ours: śas → śi (7.1.20) is sarvanāmasthāna (1.1.42), so 6.4.8's dīrgha applies as in 1p, where vidyut agrees |
| idam (n) 1p, 2p | imāni | idāni | ours: 7.2.109 *daś ca* before the vowel-initial śi |
| vāri 8s, madhu 8s | vāre, madho | vāri, madhu | both: the neuter vocative takes the guṇa optionally; the engine realises the first alternative, vidyut the other |

No cell was found where the engine's form is wrong.

## Attributions (on agreeing cells)

Rules the engine applies that vidyut does not cite, with the reason:

| rule | cells | what vidyut has instead |
|---|---|---|
| 8.4.2 | 24 | 8.4.1 (adjacent r / ṣ + n: the engine's scanner cites the vyavāya rule for the adjacent case too — both numbers name the same ṇatva) |
| 6.1.64 | 14 | 6.1.64.2 (a vārttika id for the ṭ / ṇ reversion the engine folds into 6.1.64's row) |
| 7.4.66 | 13 | 7.4.60 … (pṝ / kṛ abhyāsa: vidyut reaches a through its own abhyāsa path) |
| 7.2.35 | 9 | 7.2.58 (gamiṣyati: the engine cites the general iṭ rule, with 7.2.58 named in the row note; vidyut cites only the specific) |
| 3.4.103, 3.1.44, 7.4.59, 7.1.4, 3.4.101, 7.3.84, 6.1.101, 7.3.86, 7.3.89, 8.2.26 | ≤ 9 each | the same operation under the neighbouring number (3.1.43 for the cli, 3.4.104 / 3.4.116 for āśīrliṅ, 7.3.90 for ūrṇauti …) |

Three attribution errors of the engine that this audit found and theorum/137 corrects (forms unchanged, engine re-pinned):

1. **7.3.98 → 7.2.76.** The iṭ of roditi, svapimi, aniti, jakṣiti is 7.2.76 *rudādibhyaḥ sārvadhātuke*; 7.3.98 *rudaś ca pañcabhyaḥ* is the īṭ of the apṛkta (laṅ). theorum/136 had cited 7.3.98.
2. **6.1.73 + 8.4.40.** The tuk is t; gacch arises by 8.4.40 *stoḥ ścunā ścuḥ*. The engine had inserted c directly.
3. **3.4.107 in vidhiliṅ.** suṭ tithoḥ applies in vidhiliṅ too and the s then falls by 7.2.79; the engine applied suṭ only in āśīrliṅ. Also three redundant applications removed by ordering the apavāda first: 3.4.80 before 3.4.79 (thās → se), 3.4.101 before 3.4.100 (mip → am), 3.4.108 / 3.4.105 before 7.1.3 (jus, ran).

Rules vidyut cites that the engine does not record as steps: the affix-introduction and saṁjñā steps (3.4.78, 3.4.113 / 3.4.114, the lakāra rules 3.2.110–3.3.173, 3.1.68, 6.1.4 / 6.1.5, 7.2.10's aniṭ statement), the vacuous tripādī cycle at pause (8.2.39 + 8.4.56 on a final t), 8.3.24 + 8.4.58 on an affix-internal n before t (bhavanti), and 7.4.60 on a single-consonant abhyāsa — all surface-vacuous in the cells concerned.

## Reading

vidyut is an independent implementation from the same primary text. 1,728 of 1,744 comparable cells agree outright; the 7 that differ are vidyut's (five) or an option (two); the engine's three attribution slips were real and are corrected. The remaining attribution deltas are differences in which of two co-applicable numbers is named, recorded above so that a reader of either system can map one onto the other.
