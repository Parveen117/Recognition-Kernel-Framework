# PG7 — Validation record

Author: Monty. 1 November 2026.

Baseline review branch: `0e83db50cb564bf611b233a002d067686146d10b`.
Primary edition: `5744762f010d677cfb43f347a42d02796cf615d6`.

Direct changed-claim checks:

- 11 source-bound records, including four reused IDs and seven new IDs;
  one explicit scope decision and one local nitya relation;
- 85 literal word-membership witnesses and 13 expected refusals;
- 63 direct controls for missing source conditions, lexical identity,
  mit ownership, guṇa priority, strong/weak deletion, phase ordering,
  optional collapse, immutability and coverage-denominator separation;
- 208 literal anchors (204 unique), eight external hashes and
  40 unchanged predecessor hashes;
- 23 new roots / 32 paradigms / 288 cells / 330 branches compared with
  pinned Vidyut output, with zero differences;
- the required eight mathematics-navigation tests.

```sh
python3.12 research/panini_grammar/snam_lat/verify.py \
  --source-root /workspace/scratch/d4fa9af152dc/panini-primary-data
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The verifier reproduces the new `VERIFICATION_RESULT.json` and
`COVERAGE_STATUS.json` without writes. `--write` creates only these new-stage
reports during development. The CLI is checked on the full rudh P paradigm
and an explicitly excluded tṛh request.

Initial literal checks caught an inexact 8.3.59 quotation and standalone
forms cited where Bālamanoramā instead printed their joined *iti* forms.
The new quotation was corrected to the exact source; the word citations
were assigned to the Siddhāntakaumudī witnesses that contain those words.
No source text or predecessor pin was changed.

The read-only pre-publication comparison also found concurrent T86 and ledger
updates on the theorem branch at `7802a351dec44dc8e6dfdfe12b4b6f5ecace9fad`.
The capsule, implementation and ledger were inspected and recorded separately
in the coverage snapshot. Their certificates and runtime refusal behavior
were not replayed. The snapshot preserves both branch contexts without
making the evolving legacy ledger a pinned runtime dependency of PG7.

Only three old-form controls exercise routing through the changed adapter.
No untouched predecessor suite, frozen certificate or operator-engine suite
is replayed. Coverage reads the frozen earlier reports and checks their
identities and denominators; it does not upgrade their evidence grade.
CI, main merging and calculator integration remain deferred.
