# The Kṛdanta Declined — three tables, one derivation: 50,265 / 51,326 padas of the participles and verbal nouns in three genders

3 November 2026. theorum/151–152 made the kṛt prātipadika; theorum/125's nominal table declines a prātipadika. This packet joins them: the verbal table builds the laṭ aṅga (for śatṛ / śānac), the kṛt table the stem, the nominal table the pada — and the only rows written here are the ones the join needs: the stem's class by the affix (the ugit of ktavatu and śatṛ, 1.1.26 / 3.2.124; the ṛ-stem of tṛc; the a-stem of the rest; tumun and ktvā indeclinable by 1.1.39 / 1.1.40), and the feminine stem — 4.1.4 *ajādyataṣ ṭāp* (bhūtā, bhavitavyā, bhavamānā), 4.1.5 *ṛnnebhyo ṅīp* with 6.1.77 (kartrī, bhavitrī), 4.1.6 *ugitaś ca* (bhūtavatī, bhavantī), 7.1.81 *śapśyanor nityam* and 7.1.80 *ācchīnadyor num* (bhavantī, dīvyantī, corayantī; tudantī, krīṇantī on the num branch; adatī, juhvatī, kurvatī), 7.3.44 (kārikā, as theorum/111 reads it). The independent generator's lane for the declension (`research/independent_oracle/VIDYUT_KRDANTA_SUP_LANE.json`, 51,326 cells: every masculine cell of the eight declinable affixes, nine cells of the neuter and the feminine) is read whole.

## 1. What the join taught the nominal table

Four things the nominal table had never been asked — and now carries as rows or guards, each load-bearing on a declared paradigm taken from the lane:

```text
7.1.70 / 7.1.72   one num, not two: the neuter śi's num and the ugit's are the same augment (bhūtavanti, not bhūtavannti)
7.1.78            nābhyastāc chatuḥ: no num to the śatṛ after the abhyasta (dadat, bibhrat, juhvat; 7.1.79 in the neuter, the num branch: dadanti)
7.1.81 / 7.1.80   the num of the śatṛ stem before the neuter dual śī after śap / śyan always, after the other a / ā stems optionally (bhavantī, tudantī)
6.4.14            atvasantasya cādhātoḥ: the śatṛ's at is the dhātu's — bhavan, not the pronoun's bhavān; the two are two stems
8.4.2             the n before a jhal is not reached (granthaka, chṛndat, corayantī: the nasal there is 8.4.58's); 8.4.39 kṣubhnādiṣu ca (kṣubhnan, tṛpnuvan)
7.1.21            aṣṭābhya auś is the numeral's: the feminine aṣṭā of aś + kta declines as an ā-stem (aṣṭāḥ)
```

The flags that carry these from one table to the next are the sūtras' own saṁjñās: *ugit*, *abhyasta* (6.1.5), *kṣubhnādi*, the aṅga's final a / ā.

## 2. Results

```text
affix     m             n             f
kta       4,202/4,246   1,719/1,737   1,719/1,737     (the 44 / 18 / 18 are theorum/151's residue declined: daridrita, śvasta)
ktavatu   4,202/4,246   1,719/1,737   1,337/1,737     (f: 386 of the generator's 7s / 6p — §3)
tavya     4,246/4,246   1,737/1,737   1,737/1,737
anīya     4,224/4,246   1,728/1,737   1,728/1,737     (daridraṇīya)
tṛc       4,246/4,246       —         1,544/1,737     (f: the generator's 7s)
ṇvul      4,246/4,246   1,737/1,737       —           (f: 7.3.44 as theorum/111 reads it; the generator's bhāvakā is not in the lane)
śatṛ      3,146/3,146   1,287/1,287   1,001/1,287     (f: the generator's 7s / 6p)
śānac     1,518/1,518     621/621       621/621
total     50,265 / 51,326
```

Every disagreement is one of two named kinds: 196 cells are theorum/151's seven residual stems declined; 865 cells are the generator's 7s and 6p of the ṅīp stems of ktavatu / śatṛ / tṛc, which it writes with the shapes of the 4s and the 7s (*bhūtavatyai*, *bhūtavatyām*) against the certified nadī paradigm of theorum/89 (*bhūtavatyām*, *bhūtavatīnām*) that the nominal table derives — listed by rule, the engine's forms standing. No third kind.

## 3. Certificate

`proof_lab/krdanta_sup.py`, pinned: `proof_lab/KRDANTA_SUP_EXPECTED.sha256` = `bbea4a11f9700ac3d1b5781650eb841b38e91f6ed8402b29f0b8b23d15f0db89` (status `PASS_KRDANTA_SUP_CANDIDATE`; checks: the lane read, every disagreement of a named kind, the five feminine rows load-bearing — 7.3.44 declared vacuous on the lane). The nominal table re-pinned for the rows of §1: `proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256` = `9c1cd237741c9fa62f414ccd511c6e94764dd87f42f22ee32a6031d6f89b7782` (the previous `90dd54de…`, theorum/141, stays in the history); the ISA re-pinned with it (theorum/150 observes the nominal table: `d319faef…`); the kernel re-pinned (`54436c5e…`; re-pinned again by theorum/154, commit 70de41f holds this pin); the verbal and kṛt tables' pins unchanged.

```text
python -m proof_lab.krdanta_sup
python -m unittest proof_lab.test_krdanta_sup proof_lab.test_sup_rule_table_engine -v
python -m research.independent_oracle.krdanta_sup_lane --data <vidyut data>   # regenerates the lane file (not in CI)
```

## 4. Claim boundary

```text
THE KṚDANTA DECLINED, THREE TABLES BY CALL: 50,265 / 51,326; EVERY DISAGREEMENT OF A NAMED KIND; THE FEMININE ROWS LOAD-BEARING     PROVED on the agreeing cells, DECLARED on the lane
THE GENERATOR'S 7s / 6p OF THE ṄĪP STEM (865), 7.3.44 AS theorum/111 READS IT, 7.1.80 / 7.1.79 ON THE num BRANCH                 DECLARED / RECORDED
THE NEUTER OF tṛc, THE FEMININE OF ṇvul ON THE LANE, THE KṚT RESIDUE, ACCENT, THE SAMBODHANA OF THE PRONOUN bhavat               NOT CLAIMED
RH, YM                                                                                                                             UNTOUCHED
```
