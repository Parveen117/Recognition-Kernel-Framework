# The Written Construction Replayed — the grammar-construction packets' reference forms re-derived by the certified tables: 604 / 648 agree, 43 the other branch of a named option, 1 to adjudicate

4 November 2026. The repository carries two readings of the Aṣṭādhyāyī. One is the *written* line — the grammar-construction packets PG1–PG18 under `research/panini_grammar/`, made by hand from the sources, each with its reference cases (the commentaries' literal words), its rule records (the sūtras it reads, with their text and evidence) and its own small executable; the written line's tests and replay were deferred by its own account. The other is the *table* line — theorum/125's nominal, theorum/129's verbal and theorum/151's kṛt table, made as code and certified against the independent generator on some 110,000 cells. This packet is the test the written line deferred: every reference form the tables can read is re-derived from the same Dhātupāṭha entry, and the two answers compared; and every sūtra the packets cite is placed against the pinned edition, the tables and the ledger. Where both lines derive the same word from the same root, they can disagree only by a rule one of them lacks — so a disagreement is not a verdict but a named rule to adjudicate against the source.

## 1. The replay (R1)

```text
packet                cases   replayed   agree     outside the tables (by reason)
vikarana_lat  (PG5)      87        37      37      22 refusal cases, 25 selection cases, 3 undeclared roots
non_thematic_lat (PG6)   61        53      53      8 refusal cases
snam_lat      (PG7)      98        59      51      13 refusal, 26 undeclared roots (tṛh, und, añj, bhuj, śiṣ, indh …)
exception_lat (PG8)      45        18      18      16 refusal, 11 undeclared roots
abhyasa_lat   (PG9)      56        38      38      18 refusal cases
present_expansion (PG10) 188       153     130     35 refusal cases
lexical_present (PG11)   285       186     180     40 refusal, 59 undeclared roots (vid, cakṣ, ṛ, the ā-śās of 02.0070 …)
nasal_present (PG12)     146        98      91     37 refusal, 11 undeclared roots
causative_present (PG13)  42         6       6     31 refusal, 5 undeclared roots
root_progression (PG3), scoped_derivations (PG4): no form cases (markers, roots, phonetic readouts)
total                  1,124       648     604
```

The 44 cells on which the two lines differ are of two kinds. **43 are the other branch of an option** both lines know, each named by its sūtra and quoted: 7.3.95 *turustuśamyamaḥ sārvadhātuke* (the written line's *ravīti, tavīti, stavīti*; the tables' *rauti, tauti, stauti* — 15 cells), 8.4.65 *jharo jhari savarṇe* (*rundhaḥ / runddhaḥ*, *kṣunte / kṣuntte* — 8), 3.1.82 (*skunāti / skunoti*, *stabhnāti / stabhnoti* — 6), 3.4.84 *bruvaḥ pañcānām ādita āho bruvaḥ* (*āha / bravīti* — 5), 6.4.115 (*bibhitaḥ / bibhītaḥ* — 4), 6.4.116 (*jahitaḥ / jahītaḥ* — 3), 7.2.114 with its vārttika (*mārjanti / mṛjanti*), 7.3.90 (*ūrṇoti / ūrṇauti*). **One is to adjudicate**: *kṣiṇoti* (the written line, PG12) against *kṣeṇoti* (the tables: the u of 3.1.79 read as ārdhadhātuka by 3.4.114, so that 7.3.86's guṇa reaches the root as in *karoti*); the generator lists both. The anusvāra the two lines write differently (ṁ / ṃ) is one sound and is read as one.

The 115 cases the tables cannot read name **32 roots of the written line the tables do not declare** — the next roots for the verbal table (vid 02.0059 with 19 cases, cakṣ, śās icchāyām, ṛ, tṛh, und, añj, bhuj, indh, ṛṇu, tṛṇu …) — and the written line's refusal and selection cases, which test contracts the tables do not have.

## 2. The sūtras (R2, R3)

The packets' rule records cite 161 distinct sūtras; every one is a record of the pinned edition (`research/panini_grammar/SUTRAPATHA.tsv`) with the same Devanāgarī text. Against the table line: 106 are rows of a table, 35 are ledger entries at the hand-coded / meta / compiled level (the eight option sūtras of §1 among them), and **20 are in neither** — 1.1.58, 1.3.66, 1.3.86, 3.1.70–72, 3.1.75–76, 3.1.80, 3.4.83, 6.1.74–76, 6.1.89, 7.3.92, 8.2.35, 8.2.78–79, 8.4.42–43: the first list of what one reading has that the other has not. The ledger's 'cited' level (what the capsules mention) is not counted, so that the certificate does not read its own capsule.

## 3. Certificate

`proof_lab/pg_replay.py`, pinned: `proof_lab/PG_REPLAY_EXPECTED.sha256` = `8824583c49310c4b768dd874901462ee16d0beca61e6b8bfe0525ccf1bd8aa4f` (status `PASS_PG_REPLAY_CANDIDATE`; checks: the replay run and recorded, every cited sūtra in the pinned edition with its text). The certificate re-runs on every packet that arrives in `research/panini_grammar/` with a `REFERENCE_CASES.json`; its counts are of this commit's packets.

```text
python -m proof_lab.pg_replay
python -m unittest proof_lab.test_pg_replay -v
```

## 4. Claim boundary

```text
648 REFERENCE FORMS OF THE WRITTEN LINE REPLAYED BY THE TABLES: 604 AGREE, 43 THE OTHER BRANCH OF EIGHT NAMED OPTIONS, 1 TO ADJUDICATE   PROVED (exact, finite)
161 CITED SŪTRAS IN THE PINNED EDITION WITH THEIR TEXT; 106 ROWS, 35 LEDGER, 20 IN NEITHER (LISTED)                                  PROVED / COUNTED
WHICH LINE IS RIGHT WHERE THEY DIFFER (kṣiṇoti); THE 32 UNDECLARED ROOTS; THE REFUSAL AND SELECTION CONTRACTS; PACKETS NOT IN THE REPOSITORY   NOT CLAIMED
RH, YM                                                                                                                                      UNTOUCHED
```

*Note (theorum/155).* PG19–PG47 of the written line are merged after this theorem; its certificate re-runs unchanged on them (pin `8824583c…` stands: no new packet carries a REFERENCE_CASES.json). Theorem 155 tests what the new packets write that the tables can read — PG19's register, PG47's rule histories, the rule contracts — and names six further undeclared roots. The kernel is re-pinned again by theorum/155 (`578406c8…`); commit 71daacf holds this theorem's state.

*Note (theorum/156).* On the one case to adjudicate, *kṣiṇoti / kṣeṇoti*: the written line's PG21 (merged after this theorem) no longer realises one branch but keeps both as labelled commentary policies (G0 *kṣiṇ-*, G1 *kṣeṇ-*, 3.1.79), each uniform across the tuple; the table realises the guṇa in the strong cells only (*kṣeṇotu, kṣiṇutām*) — a third, mixed reading (theorem 156 §2). The item stands, now stated exactly: whether 7.3.86's laghūpadha guṇa reads the tanādi u, and in which cells — to be adjudicated against the Kāśikā on 3.1.79 / 7.3.86.

*Note (theorum/160).* Re-pinned by theorum/160 (`bf23cf94…`): with the twenty roots declared, 668 reference forms replay (was 648), 622 agree, 44 the other branch of an option (8.4.65 now also unttaḥ / untaḥ), 1 to adjudicate (kṣiṇoti, unchanged) and 1 adjudicated — the reference list's *indhe* against the table's *inddhe* by 8.2.40 / 8.4.53, the list's own *inddhve* and its other *inddhe* case agreeing; 26 roots remain undeclared (vid, cakṣ, ṛ, tṛh, añj, the class-2 nij / śij / pij / vṛj / pṛc, ṛṇu / tṛṇu, sthā, pā …). The pin `8824583c…` holds at commit b1059b0.

*Note (theorum/161).* Re-pinned again by theorum/161 (`cf3b5fce…`): with sthā, pā, kṛp, iṣ, tṛh declared, 678 reference forms replay, 632 agree (tṛh's eight laṭ cells and the two causatives among them); 23 roots remain undeclared. The pin `bf23cf94…` holds at commit fe99fa9.
