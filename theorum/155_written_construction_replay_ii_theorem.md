# The Written Construction Replayed II — PG19–PG47 merged and tested: PG19's 976 written modal positions (541 / 542 replayed agree, 1 adjudicated), PG47's 29 worked histories compared step by step with the tables' paths (12 / 12 reached agree), 3,796 written rule contracts placed

4 November 2026. The written line's packets PG19–PG47 (modals, benediction, nasal / athematic / lexical / consonant / abhyasta / vowel modals, contextual liṅ, opportunity and necessity, capability and prohibition, counterfactual lṛṅ, luṅ and ciṇ, taddhita, possession and adverbials, compound sound / accent / case, aṅga / affix / abhyāsa, the tripādī, the foundational relations, the two catalogue closures to 3,983 / 3,983 bounded ids, and 29 worked interaction histories) are merged into this branch at this commit (their review files reworded generically, their bytes otherwise kept). Theorem 154 replayed the written line's *reference cases* (PG3–PG13: 604 / 648). This theorem tests the three things the new packets write that a certified table can read: a **complete modal register** (PG19), **ordered rule histories** (PG47), and **rule contracts by sūtra** (PG35–PG46).

## 1. PG19's register replayed cell by cell (R4)

PG19 (`research/panini_grammar/imperative_optative/PARADIGMS.md`) writes its loṭ / vidhiliṅ register as 58 rows, each row a constructor applied to an owned stem — `I_P`, `I_A`, `O_P`, `O_A` exactly as `ENDING_CONSTRUCTION.md` §E7 writes them (read from that file and checked against the quoted lines in the module), the kṛ / krī tuples written out in full in `ATHEMATIC_DERIVATIONS.md` A2–A5 (read from that file). Expanded, the register is exactly its stated **976 written positions**. Every position whose root the verbal table (theorem 129, pin `TING_RULE_TABLE_ENGINE_EXPECTED`) declares is re-derived by the table from the same root, lakāra, pada and cell:

```text
block                         positions   replayed   agree   outside the table (by reason)
BK  basic kartari (15 rows)        270        270     270
CK  causal kartari (22 rows)       396        216     215    180: hṛ, sthā, pā, vid, budh, kṛṣ not declared
CP  causal karma (13 rows)         234          0       0    234: no causative-passive code in the verbal table (the construction branch's PG15 domain)
BP  basic karma (4 rows)            72         54      54     18: hṛ not declared
BH  bhāva 3sg (4 cells)              4          2       2      2: sthā not declared
total                              976        542     541
```

The one cell the table does not reproduce is **adjudicated** against the source: CK02 loṭ 1sg, written *kārayāni*, the table's *kārayāṇi*. By 8.4.1 *raṣābhyāṁ no ṇaḥ samānapade* with 8.4.2 *aṭkupvāṅnumvyavāye 'pi* (both quoted from the pinned edition), the n of the uttama ending follows the r of *kār* across a, y, ā — vowels and y are aṭ — so ṇ. The written line applies the same rule to its own *karavāṇi* (A2, *kar-av-ā-ṇi*) and to no other ṇic cell; the cell is a slip of the written register, not a rule it lacks. Verdict: the table's form. The written bytes are not changed; the adjudication is recorded here and in the certificate.

The 200 positions on roots the table does not declare name the next six roots for the verbal table — hṛ, sthā, pā (pibati), vid, budh, kṛṣ — in addition to theorem 154's 32.

## 2. PG47's histories against the tables' paths, step by step (R5)

PG47 (`interaction_histories/HISTORY_REGISTER.json`, 29 histories) writes ordered rule sequences: numbered steps or step tables, each step naming the sūtras it applies, with `APPLIED`, `BLOCKED` and `OPEN` results. The certificate reads each history's sequence from its document (consecutive repeats folded). For every history whose target word a table derives, the table's own path — the rule ids it fired, in firing order — is compared with the written sequence: the rules the history fires must be in the path, in the history's order (a subsequence); the rules the history blocks must be absent; the table's word must be the history's witness.

```text
history  witness        table call                 table path                                      fires (in order)             blocked (absent)   agree
A01      bhavitā        as + luṭ 3s                2.4.52 3.1.33 2.4.85 7.2.35 7.3.84 6.1.78 6.4.143  2.4.52                                           yes
A02      phalāni        phala + jas (n)            7.1.20 7.1.72 6.4.8                             7.1.20                                           yes
A05      nadyā          nadī + ṭā                  6.1.77                                          6.1.77                                           yes
A06      āsīna          ās + śānac (kṛt table)     3.2.124 7.2.83                                  7.2.83                                           yes
B04      pañca          pañcan + jas               7.1.22 8.2.7                                    7.1.22 8.2.7                                     yes
B06      daduḥ          dā + liṭ 3p                3.4.82 6.1.8 7.4.59 6.4.64 8.2.66 8.3.15        6.4.64                                           yes
B07      lunīyāt        lū + vidhiliṅ 3s           3.1.81 3.4.100 3.4.103 3.4.107 7.2.79 7.3.80 6.4.113   7.2.79                                    yes
B07b     laviṣīṣṭa      lū + āśīrliṅ 3s A          3.4.102 3.4.107 7.2.35 7.3.84 6.1.78 6.1.66 8.3.59 8.4.41   —                       7.2.79      yes
C01      vṛkṣebhyaḥ     vṛkṣa + bhyas              7.3.103 8.2.66 8.3.15                           7.3.103 8.2.66 8.3.15        7.3.102            yes
C02      vṛkṣebhyaḥ     the same, after 103        7.3.103 8.2.66 8.3.15                           7.3.103                      7.3.102            yes
C03      vṛkṣābhyām     vṛkṣa + bhyām              7.3.102                                         7.3.102                      7.3.103            yes
C05      vṛkṣaiḥ        vṛkṣa + bhis               7.1.9 6.1.88 8.2.66 8.3.15                      7.1.9 6.1.88 8.2.66 8.3.15   7.3.103            yes
```

Eleven histories reached, twelve comparisons (B07 has its control and its blessing input), **12 / 12 agree**: the table's rule order is the history's rule order on every word, the blocked rules never fire (7.3.102 never fires on *vṛkṣebhyaḥ*, 7.3.103 never on *vṛkṣaiḥ* or *vṛkṣābhyām*, 7.2.79 never in āśīrliṅ), and the table's word is the Kāśikā / Nyāsa witness each history names. The paribhāṣā and saṁjñā sūtras the histories reason with (1.1.49, 1.1.52, 1.1.55, 1.1.62, 1.1.66, 1.1.67, 1.4.2, 1.4.14, 3.4.113, 3.4.115) are at the ledger's meta level — they decide *how* a row is written, and fire no event of their own in a table path; the certificate lists them per history as the written sequence's meta-level part.

The 18 histories the tables cannot reach are listed with their reason: compounds (A03, B01, B02), taddhita (B03, D01, D02, D04, D05, D07), the feminine ṅīp rows the kṛdanta declension does not carry (D03), Vedic liṅ (B08), the kṛt affixes varac / ṇyat / ghañ the kṛt table does not carry (C04, C06, A07), ṇi-lopa before an aniṭ ārdhadhātuka (B05: the verbal table's ṇic is the present system), designations with no sound event (A04), and the two histories that are OPEN by construction (C07, D06). Every one of the 29 is either compared or placed.

## 3. The written rule contracts (R6)

PG35–PG46 write **3,796 rule contracts** (`RULE_REGISTER.json`, one per sūtra id, each with the quoted Devanāgarī sūtra): every id is a record of the pinned edition and every quoted text is the edition's text (0 mismatches, 0 outside the edition). With theorem 154's 161 rule records (PG3–PG13) and PG47's history sources, the written line's machine-readable files cite **3,849 distinct sūtras** of the edition's 3,983. Against the table line at this commit: **308 are rows of a table, 250 are ledger entries (hand-coded / meta / compiled), 3,291 are in neither** — by adhyāya: 1: 240, 2: 217, 3: 497, 4: 618, 5: 541, 6: 624, 7: 242, 8: 312. That count is the distance between the written line's closed catalogue and the table line's certified rows, exactly, at this commit; it is not a claim about the contracts' content, which are written, not executed.

## 4. Certificate

`proof_lab/pg_written_replay.py`, pinned: `proof_lab/PG_WRITTEN_REPLAY_EXPECTED.sha256` = `7d580c51ff6a156127d03099f61b09620112754c438c3fb056fd68e0a5551f19` (status `PASS_PG_WRITTEN_REPLAY_CANDIDATE`; checks: the register expands to its 976 positions, the replay run with no engine error, every disagreement adjudicated, every history compared or placed, every comparison agrees, every contract id and text in the pinned edition, theorem 154's certificate passes). Previous pin carried inside: theorem 154 `8824583c49310c4b768dd874901462ee16d0beca61e6b8bfe0525ccf1bd8aa4f` (unchanged by the merge: 604 / 648). The verbal, nominal and kṛt tables are unchanged (their pins `df6a008d…`, `9c1cd237…`, `f6ec030c…` stand). The kernel (theorem 142) is re-pinned for the ledger's new entries: see `theorum/142_panini_kernel_theorem.md`.

```text
python -m proof_lab.pg_written_replay
python -m unittest proof_lab.test_pg_written_replay -v
```

## 5. Claim boundary

```text
PG19'S REGISTER EXPANDS TO ITS 976 WRITTEN POSITIONS; 542 REPLAYED BY THE VERBAL TABLE, 541 AGREE, 1 ADJUDICATED (kārayāṇi, 8.4.2)        PROVED (exact, finite)
PG47'S 29 HISTORIES: 11 REACHED, 12 / 12 STEP-SEQUENCE COMPARISONS AGREE (ORDER, BLOCKED RULES ABSENT, WITNESS WORD); 18 PLACED OUT OF SCOPE   PROVED (exact, finite)
3,796 WRITTEN CONTRACTS ALL IN THE PINNED EDITION WITH ITS TEXT; 3,849 CITED SŪTRAS PLACED: 308 ROWS, 250 LEDGER, 3,291 NEITHER             PROVED / COUNTED
THE SIX NEW UNDECLARED ROOTS (hṛ, sthā, pā, vid, budh, kṛṣ) AND THEOREM 154'S 32; THE CAUSATIVE PASSIVE; PG20–PG46'S WRITTEN POSITIONS     DECLARED, NOT REPLAYED
THE CONTRACTS' CONTENT; THE COMPOUND / TADDHITA / VEDIC HISTORIES; WHICH READING IS RIGHT WHERE THEY DIFFER BEYOND THE ONE ADJUDICATED CELL   NOT CLAIMED
RH, YM                                                                                                                                      UNTOUCHED
```

*Note (theorum/156).* The next three registers (PG20 āśīrliṅ, PG21 nasal-class, PG22 athematic loṭ / vidhiliṅ) are replayed by theorem 156: 693 / 693 agree. The kernel is re-pinned again by theorum/156 (`f569ee6a…`); commit 921ee1e holds this theorem's state and its kernel pin `578406c8…`.

*Note (theorum/158).* Re-pinned by theorum/158 (`c98d6ba3…`): with 6.4.35 a row of the verbal table, R6's placement of the written line's 3,849 cited sūtras is 309 rows / 250 ledger / 3,290 neither; nothing else changes. The pin `7d580c51…` holds at commit 98c91c3.

*Note (theorum/160).* Re-pinned by theorum/160 (`5c442eb5…`): hṛ, budh and kṛṣ declared, R4 replays 650 of PG19's positions (was 542), 647 agree; two more cells adjudicated to the table's ṇatva by 8.4.1 / 8.4.2 — *hārayāni → hārayāṇi* (the shape of CK02) and *karṣayāni → karṣayāṇi* (the ṣ of karṣ the trigger; the written line's own *śinaṣāṇi, pinaṣāṇi* in PG22); 92 positions on pā, sthā, vid remain outside; R6's placement 311 rows / 250 ledger / 3,288 neither. The pin `c98d6ba3…` holds at commit b1059b0.
