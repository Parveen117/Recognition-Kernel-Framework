# PG9 — Actual validation

Author: Monty. 1 November 2026.

Executed under Python 3.12 against the pinned primary checkout:

```sh
python3.12 -m research.panini_grammar.abhyasa_lat.verify \
  --source-root /path/to/ashtadhyayi-data --write
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

The first command writes only PG9's new report and coverage record. It does
not regenerate any predecessor certificate. The navigation command is the
repository-required check for the index edits.

| Direct check | Result |
| --- | --- |
| Primary Sanskrit word membership | 38 witnesses pass |
| Unsupported requests | 18 expected refusals pass |
| Copy identity, ownership, strength, exceptions, source drift and dispatch | 63 controls pass |
| Literal citation anchors | 112 references / 97 unique anchors match |
| Pinned external source files | 8 unchanged |
| Historical repository files | 71 unchanged |
| Pinned Vidyut comparison | 45 cells / 45 branches, zero differences |
| Mathematics navigation | 8 tests pass |

The CLI was also invoked for all nine dhā ātmanepada cells with its exact
pinned meaning and a supplied pada license; it exited successfully and
returned the PG9 complete-domain status for every cell.

The controls check that ślu cannot be replaced by luk, a copy cannot copy
itself, teaching markers do not enter the copy, shortening does not mutate
the root, and a single constituent cannot stand in for collective abhyasta.
They distinguish hu's root u from affix u, retain the two ghu identities,
require the dhā-specific visibility permission, separate t/th/s/dhv from
v/m, and preserve 8.2.40 for the unrelated dh-final root rudh. Repeated
readout does not mutate or alias the morphological source. Only four prior
dispatch examples are checked; predecessor suites are not replayed.

The comparison table is used only by this verifier. Neither `grammar.py`
nor the CLI reads it or the expected-form cases. Agreement does not replace
traditional source evidence and cannot establish unrestricted Sanskrit
soundness. An absent complete path remains `UNRESOLVED`.

Claude's T89 review was a separate static inspection of the exact commit
patch and an AST extraction of `expected_breaks`: three keys are active and
five claimed entries are hidden inside a comment. No T89 certificate or
suite was executed, and no nominal output is counted as a verb cell here.
Hosted CI, the untouched operator engine suite and main merge were not run.
