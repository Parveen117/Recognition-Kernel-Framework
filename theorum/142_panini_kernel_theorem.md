# The Pāṇini Kernel — the two rule-table engines, the ledger and the three evidence layers read as one object: 225 sūtras as rows, 16 shared, every row a ledger entry and every engine ledger entry a row

2 November 2026. Sixty-four packets since theorum/78 built the grammar in three forms: per-theorem engines with exact certificates (theorum/63–124), two shared rule tables that absorbed them (sup: theorum/125–128, 141; tiṅ: 129–140), and written constructions where a table would have been premature (samāsa, kṛt, taddhita: 118–122). This packet reads the two tables and the ledger as **one object** and certifies what can be certified about the whole without deriving a single new form: the consistency of code with claim.

## 1. What is checked (`proof_lab/panini_kernel.py`)

- **K1 — code = claim.** Every sūtra that is a row of either engine is an entry of the ledger at the hand_coded / meta / compiled level; and every hand_coded entry the ledger attributes to an engine theorem (125–141) is a row of the engine that theorem re-pinned, or a *guard clause* of a named row — a sūtra quoted in the engine's SOURCES and named in the host row's note (seven: 7.1.11 in 7.1.9, 7.3.87 in 7.3.86, 7.3.90 in 7.3.89, 8.3.57 in 8.3.59, 8.4.37 and 8.4.39 in 8.4.2, 8.4.44 in 8.4.40). No row without a ledger entry; no ledger entry without a row.
- **K2 — the shared layer.** The rows the two engines have in common are exactly sixteen, and all are junction or tripādī rules — 6.1.77, 6.1.78, 6.1.87, 6.1.88, 6.1.97, 6.1.101, 8.2.23, 8.2.24, 8.2.66, 8.3.15, 8.3.24, 8.3.59, 8.4.2, 8.4.40, 8.4.41, 8.4.55 — the pada-independent layer the grammar states once; no aṅga rule is duplicated across the two tables.
- **K3 — the evidence.** The audit files of theorum/137–141 (`CROSSCHECK.json`, `GENERALIZE.json`, `GENERALIZE_SUP.json`) are present with the hashes their capsules pin.
- **K4 — coverage, counted.** Of the 3,983 sūtras, the ledger holds 899 entries (compiled 10, meta 157, hand_coded 324, cited 406); 225 distinct sūtras are rows of the engines (90 nominal, 151 verbal, 16 shared). Per pāda the rows sit where the engines live — 7.1 (29), 6.4 (35), 7.3 (31), 6.1 (24), 7.2 (24), 3.4 (20), 8.2 (16), 3.1 (14), 7.4 (12), 8.4 — and 6.3 (one row against 50 cited) marks where the written constructions, not the tables, carry the grammar.

## 2. The kernel reading

The state the tables act on — `(ab, ag, r, it, v, pre, aff)` for a verb, `(st, aff)` with flags for a noun — is the owned-constituent carrier of theorum/119 §6 and theorum/122 §1 made concrete: each segment is a constituent with its own history, each row is an event with a rule id, a guard that reads only the state, and an action; the path is the retained history; the pada is the pairing of root and ending; the single sweep in sūtra order is the composition law, with the asiddha relations of 8.2–8.4 as the one place where order is a theorem rather than a convention (theorum/133, 138, 140). The zero-specialisation is the surface form; what the engines certify is that the form and the form alone is what the retained history projects to. Nothing in this is a claim that the carrier *is* the grammar: it is the statement that the grammar, built row by row from the quoted text, has the carrier's shape.

## 3. Evidence layers, in one place

| layer | nominal | verbal |
|---|---|---|
| certified / quoted suite | 861 cells, 94 rows | 908 cells, 157 rows |
| independent cross-check (theorum/137) | 832 / 839 (7 the generator's) | 896 / 896 |
| unseen cells (theorum/138–141) | 1,068 / 1,078 on 48 new stems | 6,865 / 7,052; laṭ of ten classes complete |

## 4. Certificate

`proof_lab/panini_kernel.py`, test `proof_lab/test_panini_kernel.py`, pin `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `41854a6bd4cae4be57bb9b10ab5b12b617f0d98a924b56d562178d860fafcc19` (status `PASS_PANINI_KERNEL_CANDIDATE`). Re-pinned by theorum/143 (`1c46d170…`: 230 rows, 18 shared, GENERALIZE.json re-pinned; commit 1d76875) and by theorum/144 (`49ab58d8…`: 248 rows; commit 3de268d) and theorum/145 (`1919bac6…`: 261 rows; commit d5d0994) and theorum/146 (`84f843df…`: 280 rows; commit db16084) and theorum/147 (`691ca945…`; commit 24a2086) and theorum/148 (`0aa74f88…`; commit fb8547e) and theorum/149 (`5785448b…`), theorum/150 (`224889c5…`: the ledger's counts carried by the certificate, 989 entries, the ISA's ten hand-coded saṁjñā / paribhāṣā sūtras), theorum/151 (`fa1e7397…`: the kṛt table read as the third engine — 325 distinct sūtras as rows, its shared aṅga rows listed), theorum/152 (`2b27183b…`: śatṛ / śānac), theorum/153 (`54436c5e…`: the nominal table's new rows, 329 distinct sūtras as rows), theorum/154 (`68695f17…`: the ledger's counts with the written line's citations), theorum/155 (`578406c8…`: the ledger at 1,030 entries — the paribhāṣā / saṁjñā sūtras PG47's histories reason with at the meta level, 8.4.1 / 8.4.2 as the adjudication's hand-coded sources), theorum/156 (`f569ee6a…`: 7.1.35 entered as cited with its text, the modal registers' option sūtras), theorum/157 (`d68d6208…`: 6.4.35, 6.4.74, 6.4.117 entered as cited with their texts), theorum/158 (`21003192…`: 6.4.35 a row of the verbal table, hand-coded; 330 distinct sūtras as rows), theorum/160 (`2ede883c…`: 7.2.59 and 7.4.10 rows of the verbal table, hand-coded; 1.3.92 at the meta level; 332 distinct sūtras as rows); commit 8824482 holds the first pin.

## 5. Claim boundary

```text
K1 CODE = CLAIM (225 ROWS, 7 GUARD CLAUSES, 0 ORPHANS EITHER WAY); K2 THE 16 SHARED ROWS ARE THE JUNCTION / TRIPĀDĪ LAYER; K3 THE EVIDENCE HASHES HOLD   PROVED
K4 THE COVERAGE OF THE 3,983 SŪTRAS BY LEVEL AND PER PĀDA                                                                                           COUNTED
THAT THE TWO ENGINES IMPLEMENT THE AṢṬĀDHYĀYĪ; THAT A ROW'S GUARD IS THE SŪTRA'S FULL DOMAIN; THE CONSTRUCTIONS OF 118–122 AS ROWS; ACCENT              NOT CLAIMED
RH, YM                                                                                                                                                UNTOUCHED
```
