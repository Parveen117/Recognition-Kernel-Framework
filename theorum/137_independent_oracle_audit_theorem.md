# The Independent-Oracle Audit — both rule-table engines checked against vidyut-prakriya: 1,728 / 1,744 comparable cells agree, no engine form wrong, three engine attributions corrected

2 November 2026. Until now the engines' oracles were forms I or the verification branch typed from the commentaries; a wrong oracle and a wrong row could agree. This packet removes that circularity for every cell of theorum/125–136 by running them through **vidyut-prakriya 0.4.0** (ambuda-org/vidyut), an open-source Pāṇinian generator written independently from the same Aṣṭādhyāyī, which records the sūtra of every derivational step. The harness is `research/independent_oracle/crosscheck.py`; its pinned output `CROSSCHECK.json` (sha256 `81dc3f08…`) and the adjudicated summary `CROSSCHECK.md` are the evidence.

## 1. Result

- **tiṅ engine (theorum/129–136):** 905 cells run, 896 agree, **0 differ**; 9 cells vidyut cannot derive (śās), 1 root key unmatched (śru).
- **sup engine (theorum/125–128):** 839 cells run, 832 agree, 7 differ — each adjudicated against the pinned text in CROSSCHECK.md: five are vidyut's (nadīḥ for nadī; vāriṇi / triṇi for the 2p śi where 6.4.8 applies exactly as in the 1p vidyut accepts; idāni for imāni), two are an option (the neuter vocative vāre / vāri, madho / madhu) where the engine realises the first alternative.
- **No cell where the engine's form is wrong.**

## 2. What the audit corrected (forms unchanged; engine re-pinned)

1. The iṭ of roditi / svapimi / aniti / jakṣiti is **7.2.76** *rudādibhyaḥ sārvadhātuke*; theorum/136 had cited 7.3.98 (the īṭ of the apṛkta). The row, the ledger entry and the 136 capsule carry the correction.
2. The tuk of gacch is t, made c by **8.4.40**; the engine had inserted c directly. Now two rows.
3. **3.4.107** suṭ applies in vidhiliṅ as well (both padas) and the s falls by 7.2.79; the engine had it only in āśīrliṅ. With it, three redundant applications were removed by placing the apavāda first (3.4.80 before 3.4.79 for thās, 3.4.101 before 3.4.100 for mip, 3.4.108 / 3.4.105 before 7.1.3).

## 3. What the audit did not change

The attribution deltas that remain (CROSSCHECK.md's table) are cases where two numbers name one operation and each system cites one of them — 8.4.2 against 8.4.1 for adjacent ṇatva, 7.2.35 against 7.2.58 for gamiṣyati, 6.1.64 against its vārttika for the ṭ / ṇ reversion — and the saṁjñā / affix-introduction steps the engine does not record as rows. They are recorded so that either derivation can be mapped onto the other; they are not errors on either side.

## 4. Certificate

`proof_lab/ting_rule_table_engine.py` re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `c71269f5a950b6f9eaa2ba6edf743bd760e023856207c7ba0180654d3385a8ca` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`; 147 rows, 908 cells); the previous pin `45a7573f…` (theorum/136, commit d3b5a0a) stays in the history; re-pinned again by theorum/138 (the generalisation test), commit 816acc0 holds this pin. The sup engine's pin is unchanged (no correction was needed). The audit itself is reproduced by the command in `crosscheck.py`'s docstring; it needs the vidyut package and data and is therefore pinned by hash, not run in CI. Re-pinned again by theorum/143 (the open lane closed); commit 09ee5f5 holds the 3f67387f… pin.

## 5. Claim boundary

```text
1,728 OF 1,744 COMPARABLE CELLS AGREE WITH AN INDEPENDENT GENERATOR; THE 16 OTHERS ADJUDICATED; NO ENGINE FORM WRONG; THREE ATTRIBUTIONS CORRECTED   CHECKED (PINNED OUTPUT)
vidyut-prakriya 0.4.0 AS THE INDEPENDENT ORACLE (ITS OWN GAPS: śās, THE 2p śi DĪRGHA, idāni, nadīḥ, THE NEUTER VOCATIVE OPTION)                       DECLARED
THE bhavat PRONOUN AND śru (NO HARNESS INPUT), THE CELLS OUTSIDE THE TWO ENGINES' SUITES                                                               NOT CHECKED
RH, YM                                                                                                                                                 UNTOUCHED
```
