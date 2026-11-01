# PG8 — Actual validation

Author: Monty. 1 November 2026.

The new direct checks use Python 3.12:

```sh
python3.12 -m research.panini_grammar.exception_lat.verify \
  --source-root /path/to/ashtadhyayi-data
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The deterministic [result](VERIFICATION_RESULT.json) records:

- 29 literal word-membership witnesses from attributed Sanskrit commentaries.
- 16 expected UNRESOLVED requests, including ambiguous/crossed bhuj meanings,
  missing licenses, unreviewed prefixes, registers, tenses and roots.
- 53 direct controls for source scopes, lexical identity, retained markers,
  nested ownership, deletion targets, local visibility, immutability and routing.
- 80 literal citation anchors (76 unique) in eight pinned external files;
  57 historical files remain byte-identical.
- 45 complete new cells / 45 branches / five profiles / four roots compared
  with pinned Vidyut output, with zero differences.

Commentary membership and implementation-set agreement are separate evidence
grades. Neither is a universal soundness oracle. The new finite profile and
its [source reasoning](SOURCE_REVIEW.md) determine the actual claim.

The [coverage report](COVERAGE_STATUS.json) reads frozen PG5–PG7 records and
checks that new root IDs do not overlap their completed sets. It records 50
roots / 648 cells overall, while leaving overall grammar completion undefined.
Companion nominal outputs remain separately reported rather than reverified.

The navigation command above passed all eight checks after the index update.
The CLI was also exercised on all nine bhuj A forms. One isolated T87 helper
probe, outside its four-root certificate, identified the final-dh reuse boundary;
no companion certificate was run. Hosted CI and merging to main are
deferred. The operator engine is untouched and its full suite is not rerun;
no frozen theorem certificate is replayed, regenerated or repinned.
