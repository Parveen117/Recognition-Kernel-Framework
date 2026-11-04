# tiṅ Rule-Table Engine XXII — twenty roots of the written line declared in the verbal table: 1,006 suite cells (108 of them the written line's own), two rows added (7.2.59, 7.4.10), 3.1.36 and 3.1.55 extended, the five lanes rebuilt on vidyut — open 5,997 / 5,997, ārdhadhātuka 12,424 / 12,485, karmaṇi 7,632 / 7,668, ṇic 15,264 / 15,336, san 10,764 / 10,944; the replays re-pinned: 2,573 written positions on the new roots, 2,569 agree

4 November 2026. Theorems 154–159 named the roots of the written line the verbal table had not declared. Twenty of them need no row the table lacks: declared from the Dhātupāṭha, the table's rows already give their forms in every lakāra. This theorem declares them, puts the written line's own cells for them into the suite, rebuilds the five vidyut lanes so that every cell of every lakāra is tested, adds the two rows the lanes then showed missing, and re-pins everything that reads the table.

## 1. The roots

bhvādi: **hṛ** (hṛñ, U), **budh** (budha~), **kṛṣ** (kṛṣa~), **vand** (vadi~, A), **mud** (muda~, A), **īkṣ** (īkṣa~, A), **īh** (īha~, A), **vṛt** (vṛtu~, A), **vṛdh** (vṛdhu~, A), **śṛdh** (śṛdhu~, A), **syand** (syandū~, A), **svṛ** (svṛ); divādi: **nṛt** (nṛtī~); rudhādi: **chid** (chidi~r, U), **yuj** (yuji~r, U), **śiṣ** (śiṣḷ~), **piṣ** (piṣḷ~), **und** (undī~), **bhuj** (bhuja~, U), **indh** (ñiindhī~, A). Each is `ROOTS` / `GANA` of the table; `dhatu_entry` finds its Dhātupāṭha record.

## 2. The written line's cells in the suite

`W_ORACLE` (theorem 158's mechanism) now carries 108 cells the written line writes for these roots, each with its source: PG32's luṅ (*ahārṣīt, ahārṣuḥ, ahārṣam; ahṛta, ahṛḍhvam, ahṛṣi; avandiṣṭa, amodiṣṭa, aikṣiṣṭa, aihiṣṭa …*), PG31's lṛṅ (*ahariṣyat, avartsyat / avartiṣyata, avartsyat / avardhiṣyata, aśartsyat / aśardhiṣyata, asyantsyat, asvariṣyat*), PG20's āśīrliṅ (*hriyāt, hṛṣīṣṭa*), PG19's ṇic loṭ / liṅ (*hārayatu, bodhayatu, bodhayet, karṣayatu, karṣayatām*), PG22's loṭ / liṅ (*chinattu, chindantu, chinadāni, chindyāt, chindīta; yunaktu, yuṅgdhi, yuṅkṣva, yuñjyāt, yuñjīta; śinaṣṭu, śiṁṣyāt; pinaṣṭu, piṁṣyāt*) and the reference cases of PG7 / PG8 (*śinaṣṭi, śiṁṣṭaḥ; pinaṣṭi; unatti, undanti, unatsi, unadmi; bhunakti, bhuṅkte, bhuñjāte; inddhe, indhate, intse, inddhve*). Where the written line writes two readings (*aihidhvam / aihiḍhvam* by 8.3.79, *asyantsyata / asyandiṣyata* by 7.2.44, *anartsyat / anartiṣyat* by 7.2.57, *untaḥ / unttaḥ* by 8.4.65) the cell is the set and the table's form must be one of them — the suite now admits a set-valued cell. The suite is **1,006 cells, 1,006 agree**; every row is load-bearing except the declared surface-coincident.

## 3. The two rows and the two lists

Rebuilding the lanes on the twenty roots showed 78 ārdhadhātuka cells and 144 san cells the rows did not give. They are four sūtras:

- **7.2.59 *na vṛdbhyaś caturbhyaḥ*** (new row, before the iṭ rows 7.2.35 / 7.2.35s): no iṭ for the four vṛt-roots (vṛtu~, vṛdhu~, śṛdhu~, syandū~ — kṛpū~, the fifth of 1.3.92 *vṛdbhyaḥ syasanoḥ*, excluded) before sya and san in the parasmaipada: *vartsyati, avartsyat, vivṛtsati*; the ātmanepada keeps the iṭ (*vartiṣyate, avartiṣyata, vivartiṣate*). Load-bearing on 5 suite cells.
- **7.4.10 *ṛtaś ca saṁyogāder guṇaḥ*** (new row, before 7.4.11): guṇa of the ṛ-final root beginning with a conjunct before the kit liṭ — *sasvaratuḥ, sasvariva*. Load-bearing (lane).
- **3.1.36 *ijādeś ca gurumato 'nṛcchaḥ***: īkṣ, īh, und, indh join the table's ijādi-gurumat list — the periphrastic liṭ (*īkṣāṁ babhūva / āsa / cakre*; the table realises the bhū alternative, 3.1.40, as before).
- **3.1.55 *puṣādidyutādyḷditaḥ parasmaipadeṣu***: the dyutādi (vṛtu~, vṛdhu~, śṛdhu~, syandū~, kṛpū~) join the puṣādi in the aṅ row — *avṛtat, avṛdhat, aśṛdhat, asyadat* in the parasmaipada luṅ. Load-bearing on 9 cells.

After them the twenty roots' lane cells are **5,158 / 5,158** (open 624, ārdhadhātuka 1,366, karmaṇi 720, ṇic 1,440, san 1,008 — every one agrees with vidyut).

## 4. The lanes

The builder of the open lane, lost to the earlier session, is kept in the repository from here (`research/independent_oracle/open_lane.py`); run on the table as it stood, it reproduces the pinned `VIDYUT_OPEN_LANE.json` cell for cell (5,373). The five lanes rebuilt on vidyut-prakriya 0.4.0 with the twenty roots: every earlier cell unchanged, the new cells added — open **5,997 / 5,997**, ārdhadhātuka **12,424 / 12,485** (residue 61, down from 76: 7.4.10 and 3.1.36 reach earlier roots too), karmaṇi **7,632 / 7,668**, ṇic **15,264 / 15,336**, san **10,764 / 10,944** (the three residues unchanged in count: the new roots add none). The ṇic / san / karmaṇi builders read the root alone; the open and ārdhadhātuka builders now read the kartari pada behind a ṇic / san / karmaṇi suite cell.

## 5. The replays, re-pinned

Every certificate that reads the table re-runs, each noted in its capsule with its old pin and commit:

```text
theorem   certificate                 before                  after                                  new pin
154       pg_replay                   648 replayed, 604 agree  668 replayed, 622 agree, 44 option, 1 to adjudicate (kṣiṇoti), 1 adjudicated (indhe → inddhe, 8.2.40 / 8.4.53)   bf23cf94…
155       pg_written_replay (PG19)    542 / 541               650 / 647; hārayāni → hārayāṇi, karṣayāni → karṣayāṇi adjudicated by 8.4.1 / 8.4.2   5c442eb5…
156       pg_modal_registers          693 / 693               819 / 819 (PG22 in full)               454add96…
157       pg_modal_registers_ii       702 / 702               954 / 954 (PG31, PG32 in full, 144 māṅ cells)   97083eeb…
159       pg_modal_registers_iii      953 / 953               unchanged                              ea798cd7…
150       panini_isa                  —                       two new rows, one op each              0b03696e…
```

On the twenty roots the written line writes **2,573 positions** across these registers; **2,569 agree**, the four others adjudicated to the table (two ṇatva cells of PG19, *indhe*, and the kṣiṇ item unchanged). The kṛt and kṛdanta lanes are not rebuilt here (their pins `f6ec030c…`, `bbea4a11…` stand on the roots of their commits; theorem 161 extends them).

## 6. Certificate

`proof_lab/ting_rule_table_engine.py` (theorem 129's module), re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `301d276c6e4c77cd23d6d4c7807580d3e0c49bd861291c1a342e3ef405cb4696` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`, 254 rows, 1,006 suite cells); the previous pin `4cf5530a…` (theorem 158, commit b1059b0) and the chain before it stay in the history. The kernel (theorem 142) is re-pinned for the ledger (7.2.59, 7.4.10 hand-coded): see `theorum/142_panini_kernel_theorem.md`.

```text
python -m research.independent_oracle.open_lane --data /tmp/vidyut_data/prakriya        # and the four other lane builders
python -m proof_lab.ting_rule_table_engine                                              # ≈ 12 min
python -m unittest proof_lab.test_ting_rule_table_engine proof_lab.test_panini_isa proof_lab.test_pg_replay proof_lab.test_pg_written_replay proof_lab.test_pg_modal_registers proof_lab.test_pg_modal_registers_ii -v
```

## 7. Claim boundary

```text
TWENTY ROOTS OF THE WRITTEN LINE DECLARED; 108 OF ITS CELLS IN THE SUITE (SET-VALUED WHERE IT WRITES TWO); 1,006 / 1,006; TWO ROWS (7.2.59, 7.4.10) AND TWO LISTS (3.1.36, 3.1.55) BY THE QUOTED SŪTRAS   PROVED (exact, finite)
THE FIVE LANES REBUILT, EARLIER CELLS UNCHANGED: 5,997 / 5,997; 12,424 / 12,485; 7,632 / 7,668; 15,264 / 15,336; 10,764 / 10,944 — THE NEW ROOTS' 5,158 CELLS ALL AGREE        DECLARED ORACLE (implementation grade)
THE REPLAYS RE-PINNED: 2,573 WRITTEN POSITIONS ON THE NEW ROOTS, 2,569 AGREE, 4 ADJUDICATED TO THE TABLE (8.4.1 / 8.4.2; 8.2.40 / 8.4.53)                                         PROVED
THE 26 ROOTS STILL UNDECLARED (vid, cakṣ, ṛ, tṛh, añj, sthā, pā, kṛp, iṣ, the class-2 nij-group, ṛṇu / tṛṇu / ghṛṇu, stambh-group …); THE KṚT / KṚDANTA LANES ON THE NEW ROOTS   NOT CLAIMED (theorem 161)
RH, YM                                                                                                                                                                       UNTOUCHED
```
