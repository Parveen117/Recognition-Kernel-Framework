# PG13 — Actual validation

Author: Monty. 2 November 2026.

Executed under Python 3.12 against the pinned source checkout:

```sh
python3.12 -m research.panini_grammar.causative_present.verify \
  --source-root /path/to/ashtadhyayi-data --write
python3.12 -m unittest proof_lab.test_mathematics_index -v
```

| Check | Result |
| --- | --- |
| Literal primary-word membership | 11 cases pass across 11 roots |
| Unsupported requests | 31 expected refusals pass |
| Source, licensing, ownership and order controls | 74 pass |
| Primary source anchors | 138 references / 127 unique anchors match |
| Pinned files | 9 external / 130 historical files unchanged |
| Vidyut causative comparison | 108 cells / 108 branches; zero differences |
| T105 listed expectations | 36 agree; companion module not executed |
| Mathematics navigation | 8 tests pass |

The final report binds the three Python modules, the seven evidence/pin
packets and the coverage object. Cumulative counts read the frozen PG12
coverage directly. Future sibling packets cannot silently change PG13's
counts. Earlier grammar suites and certificates were not rerun.

The source checks reject missing ṇic inheritance, wrong substitution
case, missing upadhā scope, collapsed *kartari* occurrences, changed
wording and a rewritten mit note. Request checks separate causative and
pada licensing and reject the unreviewed homonyms, senses and formations.

The direct construction controls inspect root vṛddhi/guṇa, r accompaniment,
gam's actual long intermediate, distinct root/ṇic y owners and the separate
e stage in ṇic's i → e → ay. They distinguish a kit root augment from an
affix or a second root, retain pronunciation-only u, and reject wrong
host, lost kit, invented UID, changed marker role and wrong placement.

The composite checks require every root/augment/ṇic member, prohibit
repeating or reordering stages, and bind the outer ending to the original
request. Śap's guṇa query leaves the root and augment unchanged. Budh's
original A label does not block its explicitly licensed causative P.
Readout is repeatable and has no mutable alias or feedback path into
morphology. Six aggregate invariants are checked on all 108 branches.

Only four inherited dispatch examples are used: bhū, dā, kṛ and khav.
These are direct interface checks, not predecessor-suite replays.

Five separate CLI invocations cover the full nine cells for gam 1011137,
nī 1011049, pā 1011074, dā 1030010 and budh 1040068. Each returns
`COMPLETE_IN_REVIEWED_CAUSATIVE_PRESENT_DOMAIN`. A CLI request without
the causative license returns `UNRESOLVED` and exit code 1 as expected.

An initial comparison and first formal run passed. The final run binds
the explicit frozen-coverage dependency and clarified gām source note.
Kṛṣ's exact-word witness gap remains open. Full grammar soundness, the
native operator-family lift, typed zero-specialization compatibility and
quantum-calculator integration are not certified by these checks. Hosted
CI and main merging remain deferred.
