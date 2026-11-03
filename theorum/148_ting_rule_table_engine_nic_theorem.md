# Rule-Table Engine XVI — the ṇic: the causative present system of every declared root in both padas, 13,824 / 13,896

3 November 2026. The causative enters the one verbal table as theorum/147's passive did — as a state of the aṅga. 3.1.26 *hetumati ca* is a row that appends ṇic to the root and hands the stem to the rows that already conjugate the curādi (3.1.32 *sanādyantā dhātavaḥ*: the ṇic-ending is a dhātu; 1.3.74 *ṇicaś ca*: it takes both padas). Everything the ṇit ṇic demands of the root is written as a row *before* it, in the order the grammar gives them: the root substitutions, the augments, the vṛddhi and guṇa. The curādi rows of theorum/132 (7.3.84 before śap, 6.1.78, the ātmanepada and ṅit endings) do the rest unchanged.

## 1. The rows

```text
3.1.26   hetumati ca (+ 3.1.32, 1.3.74)                         the ṇic appended; the stem a curādi stem: bhāvayati / bhāvayate, abhāvayat, bhāvayatu, bhāvayet
2.4.46   ṇau gamir abodhane                                     gamayati (for iṇ)
7.3.32   hanas to 'ciṇṇaloḥ (+ 7.3.54, 7.2.116)                  ghātayati
6.1.48   krīṅjīnāṁ ṇau                                          krāpayati
7.1.64   labheś ca                                              lambhayati
6.1.50   mīnātiminotidīṅāṁ lyapi ca                            māpayati (mi, mī → mā, then puk)
2.4.52 / 2.4.53                                                 bhāvayati (as), vācayati (brū)
7.3.36   artihrīvlīrīknūyīkṣmāyyātāṁ puṅ ṇau                   dāpayati, dhāpayati, sthāpayati, jñāpayati, khyāpayati, hāpayati, māpayati, arpayati, hrepayati, vlepayati
7.2.115  aco ñṇiti (+ 6.1.78)                                   bhāvayati, kārayati, nāyayati, śāyayati, hāvayati, cāyayati, srāvayati, kārayati (kṝ), pārayati (pṝ)
7.2.116  ata upadhāyāḥ — under 6.4.92 mitāṁ hrasvaḥ             pācayati, vācayati, ghātayati, nābhayati; gamayati, śamayati (the am-final roots), the ghaṭādi (a declared list); jakṣayati (the a is not the upadhā across kṣ)
7.3.86   pugantalaghūpadhasya ca                                bhedayati, bodhayati, rocayati, veśayati, dohayati; hrepayati, vlepayati, arpayati (the puk-ending root)
7.3.85 / 7.2.114                                                jāgarayati (the vṛddhi withheld), mārjayati
```

The root-identity rows of the sārvadhātuka system (as, ad, han, śās, śī, brū, the rudādi, the u-roots, the abhyasta, the kṣubhnādi's 8.4.39) are guarded off the ṇic stem; 8.4.39 is narrowed to the n of the vikaraṇa, so the affix n of the ṇic stem takes ṇatva (kṣobhayāṇi, tarpayāṇi); 7.1.58's nuṁ and 7.1.64's num are placed before the vṛddhi rows, so the penult the vṛddhi reads is the nasal (hiṁsayati, kaṁsayati, lambhayati).

## 2. Results

```text
lane            cells    agree
ṇic laṭ         3,474    3,456     (pā rakṣaṇe ×18 in each column: pālayati is the vārttika's — not claimed)
ṇic laṅ         3,474    3,456
ṇic loṭ         3,474    3,456
ṇic vidhiliṅ    3,474    3,456
```

The kartari and karmaṇi lanes and the suite are unchanged (5,373 / 5,373; 1,845 ×4, 1,800 liṭ, 1,854 luṅ; 6,912 / 6,948; 908 / 908); 232 rows, all load-bearing on the suite or an agreeing cell of one of the four lanes except the seven declared surface-coincident.

## 3. Certificate

theorum/129's module, re-pinned: `proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256` = `5eea0b603fb7ce8fe78f8ebc2f80ee4e0a5baf01e3f64a0026fb6a6dfdfa7871` (status `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE`); the previous pin `5d304194…` (theorum/147, commit 24a2086) and the chain before it stay in the history. The certificate carries `nic_lane` beside the other lanes. The kernel re-pinned: `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `0aa74f88d16bf6484543213f5fe9ac42d0f332a96dbf91b5319a0e878ca2f0e8`.

```text
python -m proof_lab.ting_rule_table_engine
python -m unittest proof_lab.test_ting_rule_table_engine proof_lab.test_panini_kernel -v
python -m research.independent_oracle.nic_lane --data <vidyut data>   # regenerates the lane file (not in CI)
```

## 4. Claim boundary

```text
THE ṆIC PRESENT SYSTEM OF 193 ROOTS IN BOTH PADAS: 13,824 / 13,896 FROM THE ROWS OF §1; 232 ROWS LOAD-BEARING (7 DECLARED)   PROVED on the suite, DECLARED on the lane
THE GHAṬĀDI AS A DECLARED LIST (6.4.92); 7.3.37's yuk (NO ROOT IN THE TABLE), 7.3.43's OPTION, 6.1.54 / 6.1.56 (NOT ROWS)        DECLARED / NOT CLAIMED
pā rakṣaṇe (pālayati: A VĀRTTIKA), THE ṆIC OF THE ĀRDHADHĀTUKA LAKĀRAS AND OF THE KARMAṆI, san, yaṅ                            NOT CLAIMED
RH, YM                                                                                                                      UNTOUCHED
```
