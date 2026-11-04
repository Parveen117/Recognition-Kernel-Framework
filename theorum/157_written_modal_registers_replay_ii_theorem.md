# The Written Modal Registers Replayed II — PG23's lexical and PG25's abhyasta loṭ / vidhiliṅ, PG31's lṛṅ and PG32's luṅ and māṅ registers: 999 positions, 702 replayed, 692 agree, 10 adjudicated — against the table (śās: 6.4.35 missing, 6.4.34 / 8.3.60 not reaching the yāsuṭ cells)

4 November 2026. Four more registers of the written line are explicit nine-slot tables; this theorem reads them from their `PARADIGMS.md` and re-derives every position on a declared root by the verbal table (theorem 129, pin `TING_RULE_TABLE_ENGINE_EXPECTED` `df6a008d…`), as theorems 155–156 did for PG19–PG22. For the first time the comparison finds the **table** wrong: ten cells of śās, where the written line has the Kāśikā's forms and the table lacks a row.

## 1. What is read

- **PG23** `lexical_modals/PARADIGMS.md` §P1: 10 explicit loṭ tuples (han, śās, rud, svap, śvas, an, jakṣ, brū P / A, śī); §P2: the K / J factors of O_P / O_A for the 10 vidhiliṅ profiles (the constructors quoted in theorem 156's module).
- **PG25** `abhyasta_modals/PARADIGMS.md` §P1–P2: 13 loṭ P and 6 loṭ A explicit tuples of the juhotyādi roots (bhī, hrī, pṝ, pṛ, bhṛ, hāk, hāṅ, māṅ, nij, vij, viṣ, ṛ, jāgṛ, daridrā, cakās), set-valued where 6.4.115 / 6.4.116 / 6.4.117 give options; §P3: the K / J factors of the 19 vidhiliṅ profiles.
- **PG31** `counterfactual_contexts/PARADIGMS.md` §P1–P2: 32 explicit basic lṛṅ rows; the rows of one root and pada that differ only in iṭ (dhūñ: R14 / R15, R16 / R17) are one position with the union of readings — 7.2.44's option; §P3's 21 causal rows are placed outside the table.
- **PG32** `prohibitive_lung/PARADIGMS.md` §P1: 10 luṅ rows; §P2: 8 māṅ-luṅ rows without the augment; §P3: 8 māṅ + sma laṅ rows without the augment. The table has no māṅ context; its reading of 6.4.74 *na māṅyoge* is the withholding of its two augment rows — 6.4.71 *luṅlaṅlṛṅkṣv aḍ udāttaḥ* and 6.4.72 *āḍ ajādīnām* — through the engine's own row-withholding argument (`conjugate(…, off=)`), which is exactly what 6.4.74 prescribes (*aḍāṭau na*); those 54 cells are counted separately.

## 2. Results

```text
packet   rows   positions   replayed   agree   adjudicated   outside the table (by reason)
PG23       20        180        180     170        10        —
PG25       38        342        324     324         0        18: ṛ (iyarti) not declared
PG31       32        243        108     108         0       135: hṛ, iṣ, nṛt, svṛ, vṛt, vṛdh, śṛdh, syand, kṛp not declared; +189 causal (ṇic beyond the present system)
PG32       26        234     36 + 54     90         0       144: hṛ, vand, mud, īkṣ, īh not declared
total     116        999        702     692        10       297 undeclared (+189 causal)
```

**692 / 702 agree**, including *jahi, hanyāt, bravītu / bruvīta, śetām / śayīta, roditu / rudihi, svapihi, jakṣāṇi, bibhetu / bibhayāni, jihretu / jihrayāṇi, pipartu / pipūrhi, bibhartu / bibhṛṣva, jahāhi / jahatu, mimītām / jihītām, nenektu / nenigdhi / nenikṣva, veveṣṭu / veviḍḍhi, jāgartu, daridrihi, cakādhi; akārṣīt / akṛta, aidhiṣṭa, akariṣyata / alapsyata / aidhiṣyata / apakṣyat*; and the augmentless *bhūt, bhūvan, edhiṣṭa, kṛta, kṛḍhvam; bhavat, edhata, kuruta, kurvi, kurmahi* under 6.4.74. 35 cells are the other branch of a named option — 18 of 7.2.44 *svaratisūtisūyatidhūñūdito vā* (dhūñ: the table realises the seṭ branch *adhaviṣyat*, uniformly), 13 of 6.4.115 *bhiyo 'nyatarasyām* and 4 of 6.4.116 *jahāteś ca* (the table realises *bibhītām, jahīhi*; the written line keeps both). The two branch rows are uniform.

**The ten adjudicated cells are the table's.** śās loṭ 2sg: written *śādhi*, table *śiḍḍhi* — 6.4.35 *śā hau* (quoted) replaces śās by śā before hi; the table has no row for 6.4.35 and lets 6.4.34 and 6.4.101 run. śās vidhiliṅ, all nine cells: written *śiṣyāt, śiṣyātām, śiṣyuḥ …*, table *śāsyāt, śisyātām, śāsyuḥ …* — 6.4.34 *śāsa id aṅhaloḥ* makes the ā of śās i before the hal-initial ṅit yāsuṭ (3.4.103), and 8.3.60 *śāsivasighasīnāṁ ca* then makes its s ṣ; the table's 6.4.34 row does not reach the 3sg yāsuṭ cell (it fires in the dual and plural but after 7.2.79 and without 8.3.60), and its 8.3.60 row reads only a following t / v / m. The verdict in every one of the ten is the written form; these three row defects of the verbal table are corrected by theorem 158 (the table re-pinned there; the old pin stays in history). The written bytes are unchanged.

Outside the table, counted: 297 positions on 14 undeclared roots (ṛ; hṛ, iṣ, nṛt, svṛ, vṛt, vṛdh, śṛdh, syand, kṛp; vand, mud, īkṣ, īh), PG31's 189 causal positions, and the tāt words of PG23 (7) and PG25 (14): no row for 7.1.35.

## 3. Certificate

`proof_lab/pg_modal_registers_ii.py`, pinned: `proof_lab/PG_MODAL_REGISTERS_II_EXPECTED.sha256` = `c400f14174919a6710c2db654bc1c935733d8e1316ae85a06f2650f8884a443b` (status `PASS_PG_MODAL_REGISTERS_II_CANDIDATE`; checks: the replay run, 20 / 38 / 32 / 26 rows read, every option cell and every adjudication names its sūtra, the augment rows are rows of the table). This pin is against the verbal table at `df6a008d…`; theorem 158's correction of the table re-pins this certificate (the śās cells then agree). The kernel (theorem 142) is re-pinned for the ledger's new entries: see `theorum/142_panini_kernel_theorem.md`.

```text
python -m proof_lab.pg_modal_registers_ii
python -m unittest proof_lab.test_pg_modal_registers_ii -v
```

## 4. Claim boundary

```text
PG23 / PG25 / PG31 / PG32'S EXPLICIT REGISTERS READ FROM THE WRITTEN FILES: 999 POSITIONS, 702 REPLAYED (54 UNDER 6.4.74 BY ROW WITHHOLDING), 692 AGREE   PROVED (exact, finite)
10 CELLS ADJUDICATED TO THE WRITTEN FORM BY 6.4.34 / 6.4.35 / 8.3.60 (QUOTED): THREE ROW DEFECTS OF THE VERBAL TABLE ON śās, NAMED                    PROVED (adjudicated)
35 CELLS THE OTHER BRANCH OF 7.2.44 / 6.4.115 / 6.4.116 (QUOTED); 2 BRANCH ROWS, BOTH UNIFORM                                                         PROVED / COUNTED
THE 14 UNDECLARED ROOTS; THE CAUSAL lṛṅ; THE TĀT FORMS (NO 7.1.35 ROW)                                                                              DECLARED, NOT REPLAYED
THE CORRECTION OF THE TABLE (theorum/158); PG24, PG26–PG30, PG33–PG34'S REGISTERS                                                                    NOT CLAIMED HERE
RH, YM                                                                                                                                             UNTOUCHED
```

*Note (theorum/158).* The table corrected as this theorem asked: re-pinned by theorum/158 (`632be289…`), all **702 / 702** replayed positions now agree and the adjudication list is empty (the ten śās cells are in the table's suite as witness cells). The pin `c400f141…`, with the ten adjudicated cells, holds at commit 98c91c3. The kernel is re-pinned by theorum/158 (`21003192…`); this theorem's kernel pin `d68d6208…` holds at commit 98c91c3.
