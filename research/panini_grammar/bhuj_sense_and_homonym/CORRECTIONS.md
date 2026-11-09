# PG92 — Keyed correction of PG91 P sic readouts

Monty · 9 November 2026

Frozen source packet: PG91 commit
`b40864d48376dd55b4c21511fd98a1edb53e2f65`.
Correction authority: complete Kāśikā, Kaumudī, Nyāsa and
Bālamanoramā fields for 8.2.26, archived in this packet.

| Profile | Slot | Superseded SIC reading | Effective SIC reading |
| --- | --- | --- | --- |
| PRA_YUJ_VESSEL_P | 3du | prāyaukṣṭām | prāyauktām |
| PRA_YUJ_VESSEL_P | 2du | prāyaukṣṭam | prāyauktam |
| PRA_YUJ_VESSEL_P | 2pl | prāyaukṣṭa | prāyaukta |
| SAM_YUJ_ORDINARY_P | 3du | samayaukṣṭām | samayauktām |
| SAM_YUJ_ORDINARY_P | 2du | samayaukṣṭam | samayauktam |
| SAM_YUJ_ORDINARY_P | 2pl | samayaukṣṭa | samayaukta |

All keys have pada P, lakāra lung and branch SIC. Set `sic_lopa`
to `8.2.26`, `sic_retained` to false, and replace the identified
reading in both the position's reading list and that branch's path.
Keep each ANG path and word, original context, irit, vṛddhi, ending,
prefix and history label. Retain the old bytes as superseded provenance.
This is a correction, not an optional reading or a new key.

Effective PG91 totals remain **189 positions, 210 readings, 212 paths**;
its sic-lopa count becomes **19 positions/20 paths**, replacing 13/14.
The combined PG90–91 target remains **630/630**, 651 readings/653 paths.
The keyed overlay in STATE.json is authoritative when consuming PG91
through PG92. PG91's original tables, derivation wording and 13/14
lopa metadata are superseded exactly on this listed domain. Its
static-PASS record remains an integrity report, not a grammar proof.

Only the newly noticed six positions are corrected here. A targeted
text check found the mistaken yaukṣṭ spelling only in PG91's written
Markdown packet; this is not a broader grammar replay or an assertion
that every earlier aorist is certified.
