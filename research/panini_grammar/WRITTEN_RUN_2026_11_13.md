# Four-hour written grammar run · 13 November 2026

Monty · 02:25–06:25 IST. This is the new run, distinct from the expired 12 November window.

Baseline: PG275, commit `3861c38680913b411b608cf43894c09813811954`, **50,108** written finite positions.

## Foreground handoff

The foreground releases branch writing with the PG284 packet. The 03:25 checkpoint or its next available worker should take the actual branch head and continue active sequential development through the next work hour, then hand off to the following checkpoint. Stop new development at 06:25 IST and do final verification/reporting then. Read ACTIVE_WRITTEN_RUN.json and CURRENT_WORK.md before writing. Do not write concurrently with a newly active writer.

The foreground packets PG276–PG284 add **426 finite positions and 456 selected readings**, with **zero nominal positions** and **two separately counted source observations**. Cumulative finite coverage is **50,534**. The two observations are one printed perfect-stem difference and one same-surface causing/narrating construction contrast; they are not finite-position credit.

| Stage | Published commit | New finite positions | Selected readings | New source observations |
| --- | --- | ---: | ---: | ---: |
| PG276 | eabd401d5f782d438603956893a66c71712cd028 | 72 | 72 | 0 |
| PG277 | 74ce05cda09dcd607d1bc0b0e99185538e3deeec | 48 | 48 | 0 |
| PG278 | 8eae280c91d35b1d0b93266f544a27017fd27885 | 24 | 30 | 1 |
| PG279 | 4c2407ab21d9627e81393380353603fbcbe8f8a3 | 36 | 36 | 0 |
| PG280 | 9d0ff6d996fed4b8f634af2b7aa3e1db617561be | 36 | 40 | 0 |
| PG281 | 18597dd4245d2542ad73dd31d632a2537f9827cf | 12 | 24 | 0 |
| PG282 | b86c0129c0370d2d3842fc3206752b0dab948ea2 | 54 | 58 | 0 |
| PG283 | d7115b9a546c155aff173fe6dfd443cfde483cea | 72 | 76 | 1 |
| PG284 | This packet commit; obtain its actual SHA from branch history | 72 | 72 | 0 |
| PG285 | This packet commit; obtain its actual SHA from branch history | 36 | 74 | 1 |

| PG286 | This packet commit; obtain its actual SHA from branch history | 90 | 94 | 0 |

| PG287 | This packet commit; obtain its actual SHA from branch history | 180 | 188 | 0 |

| PG288 | This packet commit; obtain its actual SHA from branch history | 90 | 102 | 0 |

| PG289 | This packet commit; obtain its actual SHA from branch history | 90 | 90 | 0 |

| PG290 | This packet commit; obtain its actual SHA from branch history | 2 | 2 | 0 |

Checkpoint through PG290: **914 finite positions, 1,006 selected readings, zero nominal positions and three source observations** in this run; cumulative finite coverage **51,022**.

## Concrete next work

The four simple han/ṣo profiles have 360 distinct positions under the declared source policy. The two result-qualified han NIC-P profiles have **144/180** positions; periphrastic perfect and caṅ aorist remain, 36 positions in all. Their source archive is pinned in PG283/PG284 at `ashtadhyayi-com/data` commit `5744762f010d677cfb43f347a42d02796cf615d6`, `dhatu/dhatuforms_vidyut_nich_kartari.txt`.

For the perfect, review 3.1.35/40 and especially 6.4.55 before carrying an ordinary vowel rule into the ām host. Keep auxiliary choices, first-person alternatives, same-word policy and the result-qualified P request distinct. For the aorist, review 3.1.48, 6.1.11, 6.4.51, 7.4.1 and the abhyāsa conditions at 7.4.93/94. Mādhavīya entry 662 is an independent lexical source to collate. These are next-source leads, not a claim that the next packet has been completed.

PG282's prefixed ja/vadha words use an explicitly selected non-al lexical-membership reading of 1.1.56/8.4.17. They remain written derivations, not literal prefixed attestations. Preserve that distinction in future expansions. The same source policy is explicit for the new NIC words. Seek independent prefixed corroboration without inventing a witness.

Four primary Uṇādi 4.105 fields (*sya, ḍha, ḍaṭ, āṭac*) and the distinct effect, if any, of k at 5.56 remain open. Continue other documented grammar rather than forcing a witness.

## Checks and publishing

Python **3.12.14** document/provenance checks only. New key uniqueness, baseline/source byte pins, source excerpts, word-table agreement and count/navigation consistency were checked. NIC packets also had literal script/prefix-span projections against their archived Devanāgarī word tables. No Sanskrit generator, grammar execution, certificate replay, old suite or hardware job ran. Source-word comparisons and written derivations are distinguished.

Every grammar packet uses the same branch, `[skip ci]`, the actual current parent and non-forced compare-and-swap publication. The 06:25 final report must re-read actual branch state and report only published work in this run. Do not reuse the previous four-hour baseline or report future work as completed.
