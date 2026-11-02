# Tiṅ Rule-Table Engine V — adādi, juhotyādi and rudhādi: the luk, the ślu and the śnam infix as fourteen new rows (fourteen roots, 101 quoted laṭ cells; 109 rows on 505 cells)

2 November 2026. The three classes that do not simply add a vikaraṇa after the root enter the verbal table. **adādi**: 2.4.72 *adiprabhṛtibhyaḥ śapaḥ* is a flag that keeps 3.1.68 off and lets 7.3.84 read the pit tiṅ directly across the empty vikaraṇa; 6.4.111 *śnasor allopaḥ* drops the a of as before the kit / ṅit tiṅ (staḥ, santi, smaḥ) and 7.4.50 its s before the s-initial sip (asi); ad needs only the tripādī (atti, atsi, atthaḥ by 8.4.55). **juhotyādi**: 2.4.75 *ślu* is a flag; 6.1.10 *ślau* doubles the root on the same abhyāsa segment that liṭ uses, so 7.4.59, 7.4.62 and 8.4.54 are shared rows (ju-hu, da-dā, da-dhā); 7.1.4 *ad abhyastāt* gives at (juhvati by 6.4.87, dadati, dadate); 6.4.112 *śnābhyastayor ātaḥ* is generalised to the abhyasta ā and — for the ghu of 1.1.20 — before hal too (dattaḥ, dhattaḥ), while 6.4.113's ī stays *aghoḥ*; 8.2.38 *dadhas tathoś ca* with 8.2.40 read as *adhaḥ* (dhattaḥ, dhatse, dhaddhve). **rudhādi**: 3.1.78 *śnam* is an infix placed by 1.1.47 inside the root segment — ṅidvat like every śit vikaraṇa — whose a falls by 6.4.111 before the kit / ṅit tiṅ (runddhaḥ, bhindanti, rundhe), with 8.2.40 → 8.4.53 (runddhaḥ), 8.4.55 (ruṇatsi, bhinatti), 8.2.30 (riṇakti), 6.4.23 *śnān nalopaḥ* after 7.1.58 (hinasti), and the tripādī order **8.3.24 → 8.4.2 → 8.4.58** which is exactly what keeps rundhanti's n dental and ruṇaddhi's ṇ retroflex: the n that 8.4.58 restores from the anusvāra is asiddha for 8.4.2.

The oracle is again declared: 101 cells from the grammar-verification branch's `exception_lat`, `abhyasa_lat`, `snam_lat` tables (Kaumudī / Laghukaumudī anchors); the pada of each ubhayapadin cell is declared with the cell.

## 1. The new rows (cells of the 505 each breaks when removed)

```text
3.1.78  śnam (1.1.47)                   47    6.4.111 śnasor allopaḥ                   40    2.4.75  ślu                              36
6.1.10  ślau (doubling)                  36    8.4.58  anusvāra → parasavarṇa           28    2.4.72  śap-luk                          15
8.4.2   ṇatva (now also śnam's n)       15    6.4.23  śnān nalopaḥ                      9    8.3.24  n → anusvāra before jhal          6
8.2.38  dadhas tathoś ca                 6    7.1.4   ad abhyastāt                      2    8.2.30  coḥ kuḥ                           2
7.4.50a as's s before sip (asi)          1    7.1.58  idito num                        0*
```

\* 7.1.58's nuṁ is removed again by 6.4.23 in every śnam cell (hinasti, hiṁsanti — the anusvāra there is śnam's n); a hiṁs cell without śnam is not in the suite. The row is kept, applied, recorded in the paths and declared surface-coincident, as 3.4.92 is. Generalised: 6.4.112 (33 cells now), 6.4.87 (juhvati), 7.3.84 (the luk / ślu clause), 8.2.40 (not after dhā).

## 2. Worked derivations (from the certificate's recorded paths)

```text
juhvati    hu + jhi: 2.4.75 ślu → 7.1.4 ati → 6.1.10 hu-hu → 7.4.62 ju-hu → 6.4.87 juhv-ati
dhattaḥ    ḍudhāñ + tas: ślu → da-dhā (7.4.59, 8.4.54) → 6.4.112 (ghu, before hal) dadh → 8.2.38 dhadh → 8.4.55 dhat-taḥ
dhaddhve   dhā + dhvam (A): 3.4.79 dhve → da-dhā → 6.4.112 → 8.2.38 dhadh → 8.4.53 dhad-dhve
runddhaḥ   rudh + tas: 3.1.78 ru-na-dh → 6.4.111 rundh → 8.3.24 ruṁdh → 8.4.58 rundh → 8.2.40 rundh-dhas → 8.4.53 rund-dhaḥ
ruṇadhmi   rudh + mip (pit): ru-na-dh → 8.4.2 ruṇadhmi      (no a-lopa: pit)
hinasti    hisi~ + tip: 7.1.58 hins → 3.1.78 hi-na-ns → 6.4.23 hinas-ti ;  hiṁsanti: 6.4.111 hins → 8.3.24 hiṁs-anti
riṇakti    ric + tip: ri-na-c → 8.4.2 riṇac → 8.2.30 riṇak-ti
asi / santi as + sip: 2.4.72 → 7.4.50 a-si ;  as + jhi → anti → 6.4.111 s-anti
```

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `1258abd4ccc0d5ad3f45fce27c0dd042c6c175af3a2825ab27f974c1c0446a48` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pins `a514d5ff…` (theorum/132, commit 3460993), `ed7d4ef4…`, `ebdf15ca…`, `e9773755…` stay in the history. Re-pinned again by theorum/134 (the nasal classes at breadth); commit ec860d3 holds this pin. Re-pinned again by theorum/143 (the open lane closed); commit 09ee5f5 holds the 3f67387f… pin.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine -v
```

## 4. Claim boundary

```text
adādi, juhotyādi, rudhādi AS FOURTEEN ROWS (LUK / ŚLU FLAGS, THE ŚNAM INFIX, THE SHARED ABHYĀSA); 101 QUOTED laṭ CELLS; 109 ROWS ON 505 CELLS   PROVED
THE 101 CELLS (KAUMUDĪ / LAGHUKAUMUDĪ ANCHORS VIA THE VERIFICATION BRANCH), GAṆA AND PADA OF EACH ROOT, THE GHU LIST                               DECLARED
7.1.58 (SURFACE-COINCIDENT HERE), THE A-3s OF kṣud / chṛd / tṛd / ric / vic, und, añj, tṛh, bhuj, indh, asti, THE 3s / 3p OF dhā                   NOT CLAIMED
RH, YM                                                                                                                                              UNTOUCHED
```
