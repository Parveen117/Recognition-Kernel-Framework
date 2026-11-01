# PG2 — Actual validation and its boundaries

Author: Monty. 1 November 2026.

The source commit is `5744762f010d677cfb43f347a42d02796cf615d6`;
the reviewed repository baseline is `ada439f6ba3109d798b41c216fe7cedc79e60afb`.
The source files and eight legacy code modules are SHA-256 pinned.

## Linguistic/source checks executed

`python3.12 research/panini_grammar/verification/verify.py --source-root /path/to/ashtadhyayi-data`

- Parsed all 3,983 sūtra records and 23,589 term-reference annotations.
  All referenced IDs resolve; 344 interval flags and two heading-tag flags
  remain explicitly represented, with six commentary adjudications.
- Checked 136 literal source anchors in the supplied records and fixtures.
- Reproduced 44 marker, 26 inheritance and nine priority cases: **79 local
  expectations agree**. One marker case and five priority cases intentionally
  return `UNRESOLVED`; agreement is not a claim that these inputs were solved.
- Reproduced **24 structural/adverse controls**, including preservation of
  original teaching positions, compound `ir` versus standalone `i`, retained
  affix identity, source-tagged scope and rejection of unsupported priority.
- Audited all 2,259 Dhātupāṭha records, separating 30 `ganasutra` directives
  from 2,229 root entries: 1,703 exact marker-only headword agreements,
  524 differences, two unresolved teaching conventions. All differences and
  directives are retained in the report. Also audited 262 gaṇa and 748
  Uṇādi record identities and required fields.
- Ran exactly **three new direct probes** of T80's existing five-rule
  junction interface. They confirm absent apadānta/padānta information for
  the source cases *pacanti*, *agne'tra*, *vāyo'tra*. These are expected
  limitations, not three new claims of successful general derivation.
- Compared the reproduced output with `VERIFICATION_RESULT.json`.

## Repository checks, counted separately

The required navigation module
`python3.12 -m unittest proof_lab.test_mathematics_index -v` passed **8 tests**.
Local Markdown links in the new packet and `git diff --check` also passed.
These are structural checks; they add no linguistic verification coverage.

No CI workflow was requested, no branch was merged, and no historical
certificate was regenerated. The canonical operator engine and quantum
calculator were not modified. The review commit uses `[skip ci]`.

## What the result does not prove

The literal anchors establish provenance, not the truth of a semantic
interpretation by themselves. The expected local decisions were read from
commentaries rather than copied from predecessor output tables, but have
not received an independent specialist or cross-edition review.

The scope reader consumes publisher annotations. The marker and inheritance
records are authored, and their grammatical input facts are supplied. The
priority interpreter has four conditional witnesses, not a complete priority
theory. A diagnostic headword match is not a complete derivation, and an
unknown remains unknown. **Soundness, completeness and a general valid-Sanskrit
oracle remain unclaimed.**
