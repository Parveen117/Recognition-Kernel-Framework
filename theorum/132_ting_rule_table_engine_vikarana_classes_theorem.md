# Tiṅ Rule-Table Engine IV — the vikaraṇa classes: śyan, śa, śnu, u, śnā and ṇic as rows, their ś-it-ness as the predicate that decides guṇa (seventeen roots, 79 quoted laṭ cells; 96 rows on 404 cells)

2 November 2026. The second, fourth, fifth, sixth, eighth, ninth and tenth classes enter the verbal table, and the fact that carries them is one predicate, not a set of per-class engines: **a vikaraṇa with ś is sārvadhātuka (3.4.113 *tiṅśit sārvadhātukam*) and, being apit, ṅidvat (1.2.4) — so the root takes no guṇa before śyan, śa, śnu, śnā (sunoti, tudati, krīṇāti); the ś-less u (3.1.79) and ṇic (3.1.25) are ārdhadhātuka (3.4.114 *ārdhadhātukaṁ śeṣaḥ*) and the root takes its guṇa (karoti, corayati).** The aṅga-final u of śnu / u takes 7.3.84 before the pit tiṅ only (sunoti against sunutaḥ). Twenty-one rows carry the rest: 6.4.110 / 6.4.108 for kṛ (kurutaḥ, kurvaḥ), 6.4.107's lopa (sunvaḥ, tanmaḥ) against 6.4.77's uvaṅ after a conjunct (āpnuvanti, śaknuvaḥ) and 6.4.87's v after a vowel (sunvanti, cinvāte), 6.4.112 / 6.4.113 for śnā (krīṇanti, krīṇītaḥ), 7.3.80 for the pvādi (punāti), 8.2.77 / 7.3.74 under śyan (dīvyati, śāmyati), 3.1.74 (śṛṇoti), 6.1.64 (su, siv), 7.3.86 for cur and, with its ṅidvat guard, for tud (tudati, not *todati), and 8.4.2 across the root (krīṇāti, śṛṇoti).

The oracle here is **declared**, not certified by an earlier packet: the 79 cells are the grammar-verification branch's quoted present tables (`research/panini_grammar/vikarana_lat`, `non_thematic_lat`), each anchored in the Kāśikā or the Kaumudī text under the sūtra it illustrates. The table is checked on exactly those cells; the pada of each ubhayapadin cell (1.3.72) is declared with the cell. 6.4.107's second branch (sunuvaḥ, sunumaḥ, sunuvahe, tanuvaḥ, tanumaḥ) is recorded in `OPTION_CELLS`; the lopa branch is realised.

## 1. The new rows (cells of the 404 each breaks when removed)

```text
3.1.73  śnu                     26    3.1.81  śnā                     15    3.1.79  u (tanādi, kṛ)           12    6.1.64  ṣ → s                    11
7.3.84v guṇa of the aṅga's u     11    7.3.80  pvādi hrasva            10    6.4.113 ī halyaghoḥ               8    8.4.2   ṇatva across the root     8
6.1.77  u → v (kurvanti)        +1    6.4.87  huśnuvoḥ                 6    6.4.110 ata ut                    5    6.4.107 mvoḥ lopa                 5
3.1.77  śa                       4    6.4.112 śnābhyastayor ātaḥ       4    3.1.69  śyan                      3    3.1.74  śruvaḥ śṛ ca              3
6.4.108 nityaṁ karoteḥ           2    6.4.77  uvaṅ after a conjunct    2    8.2.77  hali ca                   2    3.1.25  ṇic                       1
7.3.86  laghūpadha guṇa          1    7.3.74  śamām aṣṭānām            1
```

7.3.84 (the root's guṇa) is now load-bearing on 117 cells and off on every ṅidvat śit vikaraṇa; 3.1.77 is load-bearing only because 7.3.86 reaches the pit śap (without the śa row, tud would take śap and guṇa: *todati).

## 2. Worked derivations (from the certificate's recorded paths)

```text
karoti     ḍukṛñ + u (3.1.79, ārdhadhātuka) → 7.3.84 kar-u → 7.3.84v kar-o-ti
kurvaḥ     kṛ + u + vas: kar-u → 6.4.110 kur-u (apit vas) → 6.4.108 kur-vas → kurvaḥ
sunvanti   ṣuñ + śnu: ṣu-nu-jhi → 7.1.3 → 6.1.64 su → 6.4.87 sun-v-anti        (no guṇa of su: śnu is ṅidvat)
āpnuvanti  āp + śnu + anti → 6.4.77 uvaṅ (the u after the conjunct pn)
śṛṇoti     śru → 3.1.74 śṛ → śnu → 7.3.84v → 8.4.2 śṛṇoti
krīṇītaḥ   ḍukrīñ + śnā + tas → 6.4.113 nī (hal-initial ṅit) → 8.4.2 krīṇītaḥ ;  krīṇanti: 6.4.112 (vowel-initial)
punate     pūñ + śnā + jha (A) → 3.4.79 → 7.1.5 at → 7.3.80 pu → 6.4.112 punate
corayati   cur + ṇic (3.1.25) → śap → 7.3.86 cor → 7.3.84 core → 6.1.78 corayati
tudati     tud + śa (3.1.77, ṅidvat) → no 7.3.86 → tudati ;  dīvyati: div + śyan → 8.2.77 dīv
```

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `a514d5ff0e0d498cdd663d02103b3a4934867ab1d692b12e55f91f83907f7f0d` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pins `ed7d4ef4…` (theorum/131, commit e638644), `ebdf15ca…`, `e9773755…` stay in the history.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine -v
```

## 4. Claim boundary

```text
THE VIKARAṆA CLASSES AS 22 ROWS WITH ś-IT-NESS AS THE GUṆA PREDICATE; 79 QUOTED laṭ CELLS; 96 ROWS ON 404 CELLS, ALL LOAD-BEARING BUT 3.4.92   PROVED
THE 79 CELLS (KĀŚIKĀ / KAUMUDĪ ANCHORS VIA THE VERIFICATION BRANCH), THE GAṆA AND PADA OF EACH ROOT, THE 7.3.74 / 7.3.80 LISTS               DECLARED
THE FULL PARADIGMS OF THESE ROOTS, 3.1.70 / 3.1.82 OPTIONS, adādi (śap-luk), juhotyādi (ślu), rudhādi (śnam), 6.4.107's SECOND BRANCH         NOT CLAIMED
RH, YM                                                                                                                                         UNTOUCHED
```
