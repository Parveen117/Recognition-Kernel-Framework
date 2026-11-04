# tiṅ Rule-Table Engine XXI — the verbal table corrected on śās from the written line's register: 6.4.35 śā hau added, 6.4.34 reaching the ṅit yāsuṭ, 8.3.60 before any following sound; six Kāśikā witness cells in the suite; 914 / 914, every lane unchanged, theorem 157's ten cells now 702 / 702

4 November 2026. Theorem 157 replayed PG23's lexical register and found ten cells where the **table**, not the written line, was wrong — all on śās (adādi, *śāsu~*): loṭ 2sg *śiḍḍhi* for *śādhi*, and the whole vidhiliṅ *śāsyāt, śisyātām …* for *śiṣyāt, śiṣyātām …*. This theorem corrects the table by the three sūtras the adjudication quoted, puts the written line's witnesses into the table's own suite so that the correction is load-bearing, and re-pins the table and everything that reads it.

## 1. The three rows

- **6.4.35 *śā hau*** (quoted from the pinned edition) — a new row: śās → śā before hi. Kāśikā's order: the dhi of 6.4.101 *hujhalbhyo her dhiḥ* first (śās is jhal-final; 6.4.101 is an al-vidhi, so no sthānivadbhāva could give dhi after śā), then *śā* — *śādhi*. The row stands after 6.4.101 and reads hi / dhi. It is the apavāda of 6.4.34, and on this table the apavāda is written into 6.4.34's guard (not before hi). With 6.4.35 withheld, 8.2.25 *dhi ca* would drop the same s (*śāsdhi → śādhi*), so the row is applied and recorded in every path but cannot be load-bearing against the surface: it is declared **surface-coincident** with that reason (the mechanism of theorems 143–149). What the witness *śādhi* loads is 6.4.34's exclusion before hi: without it, *śiḍḍhi*.
- **6.4.34 *śāsa id aṅhaloḥ*** — the row read only the apit sārvadhātuka ending (1.2.4) and only the ending segment; it now reads the ṅit yāsuṭ of liṅ too (3.4.103 *yāsuṭ parasmaipadeṣūdātto ṅic ca*) and the next sound wherever it stands: ā → i before the hal-initial kit / ṅit — *śiṣṭaḥ, śiṣmaḥ* as before, and now *śiṣyāt* in every liṅ cell (the 3sg had escaped the old guard because tip is pit; the dual and plural had fired after 7.2.79 but without 8.3.60).
- **8.3.60 *śāsivasighasīnāṁ ca*** — the row read only a following t / v / m; it now reads nothing after the s (8.3.57 *iṇkoḥ* is the context): *śiṣyāt*.

No other root's cell changes: the lanes are what they were (open 5,373 / 5,373; ārdhadhātuka 11,043 / 11,119; karmaṇi 6,912 / 6,948; ṇic 13,824 / 13,896; san 9,756 / 9,936), and the kṛt and kṛdanta certificates re-run to their pins (`f6ec030c…`, `bbea4a11…` unchanged).

## 2. The witness cells

Six cells of the written line's quoted register (`research/panini_grammar/lexical_modals/PARADIGMS.md` §P1–P2, the Kāśikā witnesses of 6.4.34 / 6.4.35 / 8.3.60) join the suite as a declared oracle `W_ORACLE`, read ahead of the laṭ cells śās already had: loṭ 2sg *śādhi*, 3du *śiṣṭām*, 2pl *śiṣṭa*; liṅ 3sg *śiṣyāt*, 3pl *śiṣyuḥ*, 1sg *śiṣyām*. The suite is 914 cells, 914 agree; 6.4.34 and 8.3.60 are load-bearing on ten cells each; every row is load-bearing except the declared surface-coincident.

## 3. Certificate and re-pins

`proof_lab/ting_rule_table_engine.py` (theorem 129's module), re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `4cf5530af6beda30b4392092d9d31f2c059b0de35cbda748250cf344cf3931ca` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`, 252 rows); the previous pin `df6a008d…` (theorem 149, commit 98c91c3) and the chain before it stay in the history. Re-pinned with it, each noted in its capsule with its old pin and commit: the Pāṇini ISA (theorem 150) `af942ce6…` (one new row, one op); theorem 155 `c98d6ba3…` (R6's placement: 309 rows / 250 ledger / 3,290 neither, 6.4.35 now a row); theorem 157 `632be289…` (**702 / 702**, the adjudication list empty). Theorems 154 and 156 re-run to their pins unchanged. The kernel (theorem 142) is re-pinned for the ledger: see `theorum/142_panini_kernel_theorem.md`.

```text
python -m proof_lab.ting_rule_table_engine        # ≈ 10 min
python -m unittest proof_lab.test_ting_rule_table_engine proof_lab.test_panini_isa proof_lab.test_pg_modal_registers_ii -v
```

## 4. Claim boundary

```text
śās: 6.4.35 ADDED, 6.4.34 AND 8.3.60 CORRECTED BY THE QUOTED SŪTRAS; SIX KĀŚIKĀ WITNESS CELLS FROM THE WRITTEN REGISTER IN THE SUITE; 914 / 914   PROVED (exact, finite)
THEOREM 157'S TEN ADJUDICATED CELLS NOW AGREE: 702 / 702; EVERY LANE AND THE KṚT / KṚDANTA PINS UNCHANGED                                       PROVED
6.4.35 SURFACE-COINCIDENT WITH 8.2.25 ON THIS TABLE (REASON RECORDED); THE APAVĀDA CARRIED BY 6.4.34'S GUARD                                   DECLARED
THE OTHER TWO ADĀDI ROOTS OF 8.3.60 (vas, ghas) IN THEIR OWN CELLS; THE UNDECLARED ROOTS                                                       NOT CLAIMED
RH, YM                                                                                                                                        UNTOUCHED
```
