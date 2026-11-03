# Kṛt Rule-Table Engine II — śatṛ and śānac: the present participles as the verbal table's laṭ aṅga, 212 / 212

3 November 2026. The present participles are laṭ's own: 3.2.124 *laṭaḥ śatṛśānacāv aprathamāsamānādhikaraṇe* puts śatṛ and śānac in the place of laṭ, and both are śit, so by 3.4.113 *tiṅśit sārvadhātukam* the aṅga before them is the sārvadhātuka aṅga — the gaṇa's vikaraṇa, its luk / ślu / śnam, the ṅidvat substitutions (1.2.4) — exactly what theorum/129's verbal table builds before the third-person plural of laṭ. This packet therefore does not write those rows again: the kṛt table's row 3.2.124 *calls the verbal table* for the laṭ 3p form of the root in the pada the affix demands (śatṛ with the parasmaipada, śānac with the ātmanepada; 1.3.78 / 1.3.12), removes the ending (anti / ati of 7.1.3 / 7.1.4; ante / ate), and places *at* or *āna*. Four rows read the result: 6.1.97 *ato guṇe* (bhavat, adat, corayat), 6.1.101 (bhāt), 7.2.82 *āne muk* (bhavamāna, edhamāna, labhamāna, corayamāṇa), 7.2.83 *īdāsaḥ* (āsīna), 7.4.21 *śīṅaḥ sārvadhātuke guṇaḥ* (śayāna — the ruṭ of 7.1.6 is jha's, not śānac's); 8.4.2 gives kurvāṇa, bruvāṇa, corayamāṇa.

This is the first place one table is built from another by call rather than by restatement — the direction theorum/151 named for the shared aṅga rows.

## 1. Results

```text
affix     cells   agree
śatṛ      143     143     bhavat, adat, juhvat, dadat, sunvat, kurvat, tanvat, krīṇat, rundhat, bhindat, ghnat, sat, yat, jāgrat, dīvyat, gacchat, āpnuvat, bhāt, corayat
śānac      69      69     bhavamāna, edhamāna, labhamāna, kurvāṇa, bruvāṇa, dadāna, sunvāna, krīṇāna, rundhāna, śayāna, āsīna, corayamāṇa
```

The lane (`research/independent_oracle/VIDYUT_KRT_LANE.json`) now carries 1,756 cells — theorum/151's 1,544 and these 212, the generator's cells for the root in its declared pada (the ubhayapadin takes both) — and the table agrees on 1,749; the seven left are theorum/151's. 78 rows, every one load-bearing.

## 2. Certificate

theorum/151's module, re-pinned: `proof_lab/KRT_RULE_TABLE_ENGINE_EXPECTED.sha256` = `f6ec030c3a759e6205ab86a537357cbc547ec8807839f28eb4965e81a55c296c` (status `PASS_KRT_RULE_TABLE_ENGINE_CANDIDATE`); the previous pin `a2a124d3…` (theorum/151, commit 7a7a419) stays in the history. The verbal table's pin is unchanged (`df6a008d…`): it is called, not changed. The kernel re-pinned: `proof_lab/PANINI_KERNEL_EXPECTED.sha256` = `2b27183b68fed716a87bbd11fae1b5bded5442429a802dd16596cf63cbfab411` (the previous `fa1e7397…` stays in the history).

```text
python -m proof_lab.krt_rule_table_engine
python -m unittest proof_lab.test_krt_rule_table_engine proof_lab.test_panini_kernel -v
```

## 3. Claim boundary

```text
śatṛ / śānac OF 193 ROOTS IN THE DECLARED PADA: 212 / 212 FROM 3.2.124 CALLING THE VERBAL TABLE AND FIVE ROWS       PROVED on the agreeing cells, DECLARED on the lane
THE ENDING READ OFF THE 3p FORM (anti / ati / ante / ate / nti) RATHER THAN THE AFFIX PLACED BEFORE THE AṄGA IS BUILT    DECLARED (an implementation reading; the aṅga is the sūtras')
THE FEMININE (7.1.70 nuṁ, ṅīp), THE DECLENSION OF THE PARTICIPLE, THE śānac OF THE KARMAṆI, lyuṭ / ghañ / ṇini / kvip      NOT CLAIMED
RH, YM                                                                                                                  UNTOUCHED
```
