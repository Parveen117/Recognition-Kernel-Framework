# PG3 — Executed validation

Author: Monty. 1 November 2026.

Reviewed parents: PG2 `770c01a`, T81 `36a8ff6`, T82 `674fdc5`.
Primary source commit: `5744762f010d677cfb43f347a42d02796cf615d6`.

## Direct linguistic/source checks

```sh
python3.12 research/panini_grammar/root_progression/verify.py --source-root /path/to/ashtadhyayi-data
```

- Verified SHA-256 pins for six primary data/commentary files and eleven
  historical repository files. No historical pin was regenerated.
- Checked **143 literal citation occurrences**, representing **77 distinct
  file/key/anchor records**.
- Reproduced **45 local reference cases**: 20 roots, 20 marker cases and five
  phonetic readouts. All expected outcomes agree.
- Reproduced **24 structural/adverse controls**, covering original sound and
  marker identity, compound i/ir/ñi distinctions, fresh augment identity,
  immutable query boundaries, missing grammatical input, identity-scoped
  exceptions, non-jhal contexts and independence from expected headwords.
- Ran **12 new historical counterexample probes**: ten T82 lakāras, the PG2
  jhi reading and the T81 vowel-table boundary. These confirm limitations and
  corrections; they do not certify the predecessor packets.
- Compared all 2,259 Dhātupāṭha records, keeping 30 gaṇasūtra directives
  separate from 2,229 roots. Marker-only, root-preprocessed and phonetic-query
  agreements are respectively **1,703**, **1,844** and **2,081**. Two teaching
  conventions remain unresolved throughout; **146** phonetic-query differences
  remain. There are no lost agreements in either transition on this witness.
- Recorded 102 initial ṣ substitutions, 35 initial ṇ substitutions and 292
  num insertions. The separate query applies 8.3.24 on 276 entries and
  continues through 8.4.58 on 241. These are application counts, not counts
  of independently verified complete sūtras.
- Reproduced the checked-in [VERIFICATION_RESULT.json](VERIFICATION_RESULT.json).

The expected outcomes are source-grounded, authored fixtures. Citation
presence and agreement with a lexical spelling are limited evidence; neither
is an independent valid-Sanskrit oracle.

## Repository checks

The required navigation command is:

```sh
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

It passed **8 tests**. Local Markdown targets in the new packet and
`git diff --check` passed. These structural checks add no linguistic coverage.

T81/T82 source and their existing workflow entries were incorporated into the
grammar review branch. Their full test/certificate campaigns and CI workflows
were not run. The review commit uses `[skip ci]`; main was not merged or
updated. The canonical operator engine and quantum calculator are unchanged.
