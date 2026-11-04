# Gaṇa Sweep I — the Dhātupāṭha itself as the root list: every undeclared root of adādi, juhotyādi, rudhādi and tanādi in vidyut's Dhātupāṭha compared with the table across 234 cells each; the 29 the table already derives whole declared (the lanes their oracle), the 13 that need rows inventoried by sūtra; theorem 159's replay 1,385 / 1,382 with 3 adjudicated; the re-pin cascade made one command

4 November 2026. Theorems 160–162 declared roots as the written line reached them, three to five a theorem. The written line is now nearly exhausted as a source of roots (theorem 154: 20 undeclared), and the grammar is not: the Dhātupāṭha has about two thousand roots and the table declared ninety-two. This theorem changes the unit of work from the root to the gaṇa. A sweep tool declares every root of a gaṇa provisionally — upadeśa and gaṇa from vidyut-prakriya's Dhātupāṭha, the pada by what vidyut derives — and compares the table with vidyut cell by cell on the same 234 cells the seven lanes carry (the ten kartari lakāras, the karmaṇi, the ṇic in both padas, the san). The roots the table derives whole are declared at once; for the rest the sweep says which lakāras disagree, so the missing rows can be read off the sūtras before a root is touched.

## 1. The sweep

`research/independent_oracle/gana_sweep.py` (`--gana N`): the entries of the gaṇa not yet declared by the table, each conjugated under a provisional key, 234 cells (360 for an ubhayapadin: both padas), agreement counted by lakāra. Four gaṇas swept — the four the table's NASAL block (theorem 139) already covers in part:

```text
gaṇa          entries   clean   with residue (cells agree / 234; the lakāras that disagree)
2 adādi          20       14    i (iṅ, 113: 2.4.49 gāṅ liṭi, 2.4.51 ṇau ca saṁścaṅoḥ, 6.1.90 āṭaś ca in laṅ); i (ik, 117: ṇic gamayati, luṅ); dīdhī, vevī (13 each: 1.1.6 dīdhīvevīṭām, the ī before yak); ṣast (195: 8.2.23 / 8.2.29 before t, the san's nasal); vaś (149: 6.1.15 vacisvapiyajādīnāṁ kiti for the ṅit sārvadhātuka, 8.2.36)
3 juhotyādi      12        7    ṛ (135: 6.4.78 abhyāsasyāsavarṇe on the ślu abhyāsa — iyarti); sṛ (225: 3.1.56 sartiśāstyartibhyaś ca, luṅ asarat); bhas (157: 6.4.100 ghasibhasor hali ca); jan (143: ṇic janayati; four laṅ / laṭ cells, the liṭ); gā (189: the present system of the juhotyādi gā — jigāti)
7 rudhādi         7        6    vij (161: 1.2.2 vija iṭ — the iṭ kit: no guṇa before it; the san)
8 tanādi          3        2    ṛṇu (342 / 360: liṭ in both padas)
```

(The sūtras named for the residues are the sweep's reading of the disagreeing cells, to be confirmed when each row is added; nothing about them is claimed here.) The 29 clean roots are declared in one block, `DHATUPATHA_ROOTS` of the verbal table — key, upadeśa, pada, gaṇa, Dhātupāṭha code — with no written-line cell: they enter the suite as `(root, laṭ, [], pada)` so that the lane builders and the replays see them, and the seven lanes are their oracle (declared, implementation grade). vṛj's two adādi entries (02.0022 vṛjī, 02.0023 vṛji: idit, so 7.1.58 num — *vṛṅkte, vṛñjīta* beside *vṛkte, vṛjīta*) are two roots of the table, as they are two entries of the Dhātupāṭha.

```text
adādi       nij2 (ṇiji~, A: niṅkte, niniñje, aniñjiṣṭa), śij2, pij2, pṛj2, vṛj2 (vṛjī~), vṛj2n (vṛji~), pṛc2 (pṛcī~, A), su2 (ṣu: sauti, suṣāva, asauṣīt), ku2 (kauti), śrā2, rā2, dāp2, prā2, sas2 (ṣasa~: sasti)
juhotyādi   ghṛ3 (jagharti, jaghāra, aghārṣīt), hṛ3, ki3, kit3, tur3, dhiṣ3, dhan3
rudhādi     khid7 (khintte, cikhide, akhitta), vid7 (vintte), bhañj7 (bhanakti, babhañja, abhāṅkṣīt), tañc7, vṛj7, pṛc7
tanādi      tṛṇu8 (tṛṇoti / tṛṇute), ghṛṇu8 (ghṛṇoti / ghṛṇute) — theorem 145 left tṛṇu out because 7.3.86 as a row would give tarṇoti; the table as it now stands gives tṛṇoti, agreeing with vidyut on all 360 cells
```

## 2. The certificates

The verbal table's suite is unchanged (**1,072 / 1,072**: the 29 roots add no suite cell); the seven lanes, rebuilt with every earlier cell unchanged, now carry the 29: open **7,028 / 7,028**, ārdhadhātuka **14,563 / 14,617**, karmaṇi **8,928 / 9,000**, ṇic **17,856 / 18,000**, san **12,204 / 12,420** — the residues unchanged in count (54 / 72 / 144 / 216: daridrā, ūrṇu, and cakṣ under the open question of theorem 162), so every cell of the 29 roots agrees. The kṛt lane **2,265 / 2,275** — the residue of 10 is theorem 161's 8 and bhañj's kta / ktavatu (*bhagna, bhagnavat*: the root is odit, 8.2.45 *oditaś ca* turns the niṣṭhā's t into n — a row the kṛt table lacks, inventoried); the kṛdanta-declension lane **65,116 / 66,500**, every disagreement of the two named kinds.

**Theorem 159's replay** (PG24 / PG26 / PG27, the class-2 modal registers) — the written roots nij, śij, pij, pṛj, vṛj (both entries), pṛc, su, ku, śrā, rā, dāp, prā, khid, vid (class 7), bhañj, tañc, vṛj (class 7), pṛc (class 7) now keyed to the table: **1,385 replayed of 1,457 (was 1,043), 1,382 agree**, 79 the other branch of an option, **3 adjudicated**, 0 to adjudicate; 54 positions on three roots remain undeclared (kas with num, nis, vij) and 18 on dih's ātmanepada. The three adjudicated cells are PG27's loṭ 1s / 1d / 1p of the non-num vṛj — the written line gives *vrajai, vrajāvahai, vrajāmahai*; the guṇa of ṛ is ar (1.1.2, 1.1.51) before the pit ātmanepada ai (7.3.84): *varjai, varjāvahai, varjāmahai*, as the table and vidyut give; the written *vraj-* has no sūtra (recorded as the table's form, `ADJUDICATED`).

**Theorem 154's replay** (the written line's reference forms): with the 29 roots declared, **734 replayed (was 713), 676 agree, 56 the other branch of an option** — the new option cells are khid's and the class-7 vid's ātmanepada 3s (*khintte / khinte, vintte / vinte*: 8.4.65, as for kṣud, chṛd, tṛd) and tṛṇu's *tṛṇoti*: vidyut lists *tṛṇoti* and *tarṇoti* both, the u of ṛṇu / tṛṇu / ghṛṇu read as the root's final (then the ṛ is no upadhā for 7.3.86) or as 3.1.79's vikaraṇa alone, and the table realises the guṇa branch (*tarṇoti, gharṇoti*) — recorded as an option under 3.1.79, the ground of the u-final reading not derived here; 1 to adjudicate (kṣiṇoti, as before), 1 adjudicated (*inddhe*); 10 roots of the written line remain undeclared (laṣ, śās, ṛ, budh, bhram, yas, ṛṇu, vṝ, kṝ, khav).

## 3. The cascade as one command

`scripts/repin_cascade.py --by N` re-runs every certificate that reads the tables (ISA, kṛt, kṛdanta, theorems 154–157, 159), writes each moved pin, replaces the hash in `CERTIFICATE_INDEX.md`, appends the standard note to the certificate's capsule — new pin, the headline numbers read from the certificate itself, old pin and the commit that holds it — then rebuilds the ledger (IAST mismatch must be 0) and re-pins the kernel with its entry in theorem 142's list. The ceremony that took a third of every turn is one command; nothing in it decides anything — every number in a note is read from the certificate it names. The pinned history is as before: no pin file is rewritten in git, each old pin's line stays in its own theorem's index, and each note names the commit at which the old pin held.

## 4. Certificate

`proof_lab/ting_rule_table_engine.py`, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `50f0cdf7a983cbf6e5c9d92f6ad682a0169b7c38dbb4ec764f90ae7932241c46` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`, 261 rows, 1,072 suite cells, 29 lane-only roots listed under `dhatupatha_lane_only_roots`); the previous pin `a7a6606c…` (theorem 162, commit cc7b39b) and the chain before it stay in the history. Every dependent certificate re-pinned by the cascade, each noted in its capsule.

```text
python3.12 -B -W ignore -m research.independent_oracle.gana_sweep --data /tmp/vidyut_data/prakriya --gana 2 --out /tmp/sweep2.json
python3.12 -B -W ignore -m research.independent_oracle.open_lane --data /tmp/vidyut_data/prakriya     # and the six other builders
python3.12 -B -W ignore -m proof_lab.ting_rule_table_engine                                            # ≈ 17 min
python3.12 -B -W ignore scripts/repin_cascade.py --by 163
```

## 5. Claim boundary

```text
THE 29 CLEAN ROOTS OF THE FOUR SWEPT GAṆAS DECLARED (DHATUPATHA_ROOTS), THE SEVEN LANES THEIR ORACLE: EVERY ONE OF THEIR CELLS AGREES WITH vidyut-prakriya 0.4.0            DECLARED ORACLE (implementation grade)
THE VERBAL TABLE's SUITE 1,072 / 1,072 UNCHANGED; THE EARLIER LANE CELLS UNCHANGED; THEOREM 159's REPLAY 1,385 / 1,382, 0 TO ADJUDICATE; THE vṛj CELLS ADJUDICATED BY 1.1.2 / 7.3.84   PROVED (exact, finite)
tṛṇoti / tarṇoti (3.1.79: THE u AS THE ROOT's FINAL OR AS THE VIKARAṆA — THE TABLE REALISES THE GUṆA BRANCH, THE GROUND OF THE OTHER NOT DERIVED); kṣiṇoti                       RECORDED, NOT CLAIMED
THE 13 ENTRIES WITH RESIDUE (i in both its entries, dīdhī, vevī, ṣast, vaś, ṛ, sṛ, bhas, jan, gā, vij, ṛṇu) AND THE SŪTRAS THE SWEEP NAMES FOR THEM                                                      INVENTORIED, NOT CLAIMED
THE OTHER GAṆAS (bhvādi, divādi, svādi, tudādi, kryādi, curādi); kas-num, nis, dih's ātmanepada; 2.4.54's SCOPE (theorem 162); kṣiṇoti                                                NOT CLAIMED
RH, YM                                                                                                                                                                                UNTOUCHED
```
