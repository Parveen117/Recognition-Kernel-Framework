# Tiṅ Rule-Table Engine VI — the nasal classes at breadth: 86 svādi / tanādi / kryādi entries (91 quoted cells) on the rows of 132 with eight additions (115 rows on 596 cells)

2 November 2026. A breadth test of the multiplier. theorum/132 built śnu, u and śnā from seventeen roots; here 86 further entries of the fifth, eighth and ninth classes from the grammar-verification branch's quoted tables (`research/panini_grammar/nasal_present`: Kāśikā / Kaumudī anchors, mostly the 3s) are run through the same table. They needed **eight new rows and three guard changes**, no new segment and no new predicate: 3.1.82 *stambhu-…-skuñbhyaḥ śnuś ca* (the śnu branch realised: skunoti, stabhnoti); 6.4.24 *aniditāṁ hala upadhāyāḥ kṅiti* — the penultimate nasal of a non-idit root falls before the ṅidvat vikaraṇa (dabhnoti, stabhnoti, badhnāti, mathnāti, grathnāti, kuthnāti); 7.3.79 *jñājanor jā* (jānāti); 6.1.16 with 1.1.45 and 6.1.108 (gṛhṇāti, gṛhṇītaḥ, jināti, jinītaḥ); 8.4.40 *stoḥ ścunā ścuḥ* under 8.4.44 *śāt* (khacñāti; aśnāti, kliśnāti untouched); 8.4.41's n after ṭu (mṛḍṇāti); 8.4.39 *kṣubhnādiṣu ca* as the ṇatva exception, read from the gaṇapāṭha (kṣubhnāti, tṛpnoti); and 6.1.64 now reverting the ṭ / ṇ the initial ṣ had conditioned (ṣṭigha~ → stigh, ṣaṇu~ → san: *nimittāpāye naimittikasyāpy apāyaḥ*). The guard changes: 7.3.80 is the *kryādi* pvādi (dhūnoti in the fifth class against dhunāti in the ninth), 7.3.86 also reads the ārdhadhātuka u (kṣeṇoti), and the ṇatva scanner reads the kṣ token as ending in ṣ (kṣiṇoti, kṣuṇatti).

## 1. The new rows (cells of the 596 each breaks when removed)

```text
6.4.24  aniditāṁ hala upadhāyāḥ kṅiti   9     3.1.82  śnuś ca                      6     6.1.16  samprasāraṇa (grah, jyā)     5
7.3.79  jñājanor jā                     1     8.4.40  stoḥ ścunā ścuḥ              1     8.4.41n ṣṭunā ṣṭuḥ (n)               1
6.1.64  (extended)                      18    7.3.80  (kryādi only)                22    7.3.86  (also before u)              2
8.4.2   ṇatva, with 8.4.39 excepted     46
```

## 2. What the breadth showed

- 46 cells now rest on the ṇatva row alone; its scanner (r / ṛ / ṣ across vowels, ku, pu, h, y, v — not across a jhal that 8.3.24 has already reached) decides stṛṇoti, drūṇāti, gṛhṇāti, prīṇāti, kuṣṇāti, mṛṇāti and leaves mṛdnāti, gudhnāti, grathnāti, dhrasnāti, rādhnoti alone, with 8.4.39 the only list.
- Two anchored entries are left out rather than forced: **tṛṇu** (the branch anchors tṛṇoti / tṛṇute; the table's 7.3.86, which the same branch needs for kṣeṇoti, would give tarṇoti — the ground of the attested form is not derived here), and **ṛṇu / khav** (ṛṇoti / arṇutaḥ, khaunāti). They are named in NOT_claimed.
- The 3.1.82 roots take the śnu branch; the śnā branch (stabhnāti …) is recorded as the option, not realised (set-valued output remains theorum/118 D4's channel).

## 3. Worked derivations

```text
stabhnoti  stanbhu~ + śnu (3.1.82) → 6.4.24 stabh-nu → 7.3.84v stabhnoti
gṛhṇāti    graha~ + śnā → 6.1.16 gṛh (1.1.45) → 8.4.2 gṛhṇāti ;  jināti: jyā → ji (6.1.16, 6.1.108) → jināti
sanoti     ṣaṇu~ + u → 6.1.64 san (the ṇ reverts with the ṣ) → 7.3.84v sanoti
kṣeṇoti    kṣiṇu~ + u (ārdhadhātuka) → 7.3.86 kṣeṇ → 7.3.84v kṣeṇoti
khacñāti   khac + śnā → 8.4.40 ñ ;  mṛḍṇāti: 8.4.41 ;  kṣubhnāti: 8.4.39 (no ṇatva) ;  dhūnoti (5) / dhunāti (9): 7.3.80 is the kryādi's
```

## 4. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `629719df8dd7f2c1e55376c65efb2e2418b09f8bb6a89ca0ecd0920b8152b791` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pins `1258abd4…` (theorum/133, commit ec860d3) and earlier stay in the history.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine -v
```

## 5. Claim boundary

```text
86 NASAL-CLASS ENTRIES, 91 QUOTED CELLS, FROM EIGHT NEW ROWS AND THREE GUARD CHANGES; 115 ROWS ON 596 CELLS, ALL LOAD-BEARING BUT THE TWO DECLARED   PROVED
THE 91 CELLS (KĀŚIKĀ / KAUMUDĪ ANCHORS VIA THE VERIFICATION BRANCH), THE GAṆA AND PADA OF EACH ENTRY, THE 8.4.39 / 6.1.16 / 3.1.82 LISTS               DECLARED
tṛṇu, ṛṇu, khav; THE śnā BRANCH OF 3.1.82; THE FULL PARADIGMS OF THESE ENTRIES                                                                          NOT CLAIMED
RH, YM                                                                                                                                                  UNTOUCHED
```
