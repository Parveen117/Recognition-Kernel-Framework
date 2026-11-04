# The Pāṇini ISA — every firing of the two rule tables is a short sequence of sixteen operation types; the tables are a staged program

3 November 2026. theorum/129–149 built the Aṣṭādhyāyī's nominal and verbal morphology as two rule tables — 90 and 251 rows, each row a sūtra with a guard and an action on a segmented state — and certified them on the suites and seven independent lanes (≈ 60,000 derivations). This packet reads the tables as a *program*: an observer records the state before and after every firing of every row on every one of those derivations, and a classifier names what each firing did. The result is an instruction set: every one of the 394,468 firings is a sequence of at most two operations drawn from a catalogue of sixteen, and each of the sixteen is an operation the Aṣṭādhyāyī itself names — the three augment positions of 1.1.46 *ādyantau ṭakitau* and 1.1.47 *mid aco 'ntyāt paraḥ*, the lopa of 1.1.60 *adarśanaṁ lopaḥ*, the ādeśa of 1.1.52 *alo 'ntyasya* and 1.1.55 *anekāl śit sarvasya* and of the upadhā (1.1.65), the vowel grades (1.1.1 *vṛddhir ādaic*, 1.1.2 *adeṅ guṇaḥ*, 1.2.27), the doubling of 6.1.1 *ekāco dve prathamasya*, the affix, the mark, the sandhi at a boundary. Nothing here derives a form; the engines' pins stand, and what is added is the table read as code.

## 1. The catalogue

```text
SAṀJÑĀ        a mark or attribute set, no sound changes (1.1.x, 1.3.x)                            51,729 firings (verbal)   240 (nominal)
PRATYAYA      an affix or augment segment introduced where none stood (3.1; 3.4.102–103; 7.2.35)   77,953                     —
ĀGAMA-ĀDI     an augment at the head of its segment — the kit augment (1.1.46)                       6,807                     82
ĀGAMA-ANTA    an augment at the end — the ṭit augment (1.1.46); the sanādi kept in the root (3.1.32) 16,158                    106
ĀGAMA-MIT     an augment after the last vowel (1.1.47)                                               2,340                     16
LOPA          a sound or sequence disappears (1.1.60; luk / ślu 1.1.61)                             47,684                    696
ANTYĀDEŚA     the final sound of the sthānin replaced (1.1.52)                                       46,574                  1,955
SARVĀDEŚA     the whole sthānin replaced (1.1.55)                                                    21,909                    611
MADHYĀDEŚA    a sound inside the sthānin replaced — the upadhā (1.1.65)                              34,141                    153
ĀDEŚA         a sequence replaced by a sequence inside a segment (1.1.50)                             8,069                    141
GUṆA          the vowel → its guṇa-grade sound (1.1.2)                                               28,542                    113
VṚDDHI        the vowel → ai / au / ār (1.1.1)                                                        3,471                     —
DĪRGHA        the vowel lengthened (1.2.27); a → ā read here, the one sound being both grades      10,844                    335
HRASVA        the vowel shortened (1.2.27)                                                            6,541                      4
DVITVA        the abhyāsa segment set from the root (6.1.1, 6.1.4)                                   12,043                     —
SANDHI        two segments joined at their boundary (6.1.77–6.1.101)                                 14,970                    241
```

The classification is of the *sound change on the segmented state*; the catalogue names it by the Aṣṭādhyāyī's name for that change. Where a sūtra names the same change otherwise, the certificate says so in the entry: 3.4.79's *e* for the ṭi *i* is an ādeśa that is the guṇa-grade sound and is filed under GUṆA; 7.2.116's *ā* for the upadhā *a* is called vṛddhi by the sūtra and 6.4.16's *ā* dīrgha, and both are filed under DĪRGHA. The per-row operation types are in the certificate: the 251 verbal rows carry 227 distinct sūtra ids, and 165 of these do one type of operation only; 62 do more than one across their firings (3.4.79: ANTYĀDEŚA / GUṆA / ĀDEŚA by the shape of the affix; 7.3.84: GUṆA only, 17,865 times). Forty verbal and eleven nominal rows fire compound — two operations in one firing, every one a sound change with its mark (2.4.52 SARVĀDEŚA + SAṀJÑĀ: bhū for as, and the root re-named). No firing is three operations.

## 2. The schedule

The rows of each table stand in phases marked in the source — the verbal table 83 / 134 / 8 / 26 (the lakāra's affixes, the aṅga, the junction, the tripādī), the nominal 7 / 48 / 12 / 10 / 17 — and the phase sequence is monotone: no row of a later phase stands before a row of an earlier. The tripādī phase is one pass in table order. Against the sūtra order of 8.2.1 *pūrvatrāsiddham* the verbal table's tripādī has 71 pairs of rows standing the other way about; the observer finds 45 of them vacuous — on no derivation do both fire — and 26 live, each listed with the number of derivations on which both fire and one example. The live ones are of three kinds: the pada-final *s → ru → visarga* (8.2.66, 8.3.15) placed last, after every row that reads a site the pause does not touch (8.3.24, 8.3.59, 8.4.2, 8.4.40, 8.4.41, 8.4.58 — 2,074 derivations for 8.3.59 alone); the ṣṭutva of 8.4.41 before the ḍh-lopa of 8.3.13 and 6.3.111's dīrgha after both (*leḍhi*, *līḍhaḥ*: 40 and 20 derivations); and 8.2.29 before 8.2.23 (one derivation: *aśikṣan*, the san of śak), 8.4.58 before 8.4.41 (24: *adambhiṣṭām*-type cells). The nominal table has 43 such pairs, 29 vacuous, 14 live, all of the first kind. These re-orderings are the tables' — declared here with their evidence, not derived from 8.2.1.

## 3. The readers

The guards are predicates over the state read through a finite set of readers: in the verbal table 30 attributes of the state (the segments *r*, *v*, *aff*, *it*, *pre*, *ab*, *ag*; the lakāra, the pada, the gaṇa, the upadeśa root, the flags, the kit / ṅit / pit / strong predicates, the next sound, the sound after the root) and 7 helper predicates (`_kity`, `_yas`, `_aprkta`, `_siyut`, `_conj_before_final`, `_natva_site`, `_s_after_in`); in the nominal table 27 attributes and no helper. 251 and 94 guards, every one walked by the syntax tree.

## 4. Certificate

`proof_lab/panini_isa.py`, pinned: `proof_lab/PANINI_ISA_EXPECTED.sha256` = `c2938c01f6f191e7398e97e43296225f24b980516b46a10dd4b53d680cdc39a9` (re-pinned by theorum/153 with the nominal table's new rows: `d319faef…`, commit 751ddde holds the first pin; status `PASS_PANINI_ISA_CANDIDATE`; checks I1 every firing classified, I2 at most four operations per firing (two are used), I3 the catalogue closed at sixteen types and every type used, I4 phases monotone and the tripādī re-orderings listed with their co-firing counts, I5 the readers finite). The observer is `HOOK` in the two engines (`None` in ordinary runs; the engines' pins at the first pin: `df6a008d…`, `90dd54de…`; the nominal table re-pinned by theorum/153). The kernel re-pinned for the ledger's counts: `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `224889c5ef0bcc5374afbfadb175b9d3140bab1762b69fb892367589ddc9c2fb`; re-pinned again by theorum/151 (the kṛt table), commit 1ffd04e holds this pin; the previous pin `5785448b…` (theorum/149, commit 629250f) stays in the history.

```text
python -m proof_lab.panini_isa
python -m unittest proof_lab.test_panini_isa -v
```

## 5. Claim boundary

```text
EVERY FIRING OF 251 + 90 ROWS ON ≈ 60,000 DERIVATIONS IS ≤ 2 OPERATIONS FROM A CLOSED CATALOGUE OF 16 PĀṆINIAN TYPES     PROVED (exact, finite)
THE PHASES MONOTONE; THE TRIPĀDĪ ONE PASS; ITS 26 + 14 LIVE RE-ORDERINGS LISTED WITH EVIDENCE, 45 + 29 VACUOUS            PROVED (listed) / DECLARED (the order is the table's)
THE GUARDS' READERS: 30 + 7 AND 27, BY THE SYNTAX TREE                                                                   COUNTED
WHICH NAME A SŪTRA GIVES A SOUND CHANGE THE CATALOGUE FILES ELSEWHERE (3.4.79, 7.2.116)                                   RECORDED, NOT CLAIMED
THAT THE CATALOGUE IS THE ONLY READING; THAT THE GUARDS ARE A FINITE INSTRUCTION SET; CONFLUENCE; "SANSKRIT IS A PROGRAMMING LANGUAGE"; RH, YM   NOT CLAIMED / UNTOUCHED
```

*Note (theorum/158).* Re-pinned again by theorum/158 (`af942ce6…`) after the verbal table's correction on śās (one new row, 6.4.35, one op); the previous pin `d319faef…` holds at commit 98c91c3.

*Note (theorum/160).* Re-pinned again by theorum/160 (`0b03696e…`) with the verbal table's two new rows and twenty roots; the previous pin `af942ce6…` holds at commit b1059b0.

*Note (theorum/161).* Re-pinned again by theorum/161 (`5661a4b2…`) with the verbal table's five new rows and the nominal table's idam rows restricted to the pronoun; the previous pin `0b03696e…` holds at commit fe99fa9.

*Note (theorum/162).* Re-pinned again by theorum/162 (`7b826f6e…`); the previous pin `5661a4b2…` holds at commit 6469a92.
