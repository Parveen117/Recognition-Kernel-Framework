# PG1 — Pāṇini: grammar before implementation

Author: Monty. 1 November 2026.

This stage establishes the Sanskrit grammar specification before extending its
software or applying it in the quantum calculator. It integrates the existing
T78–T80 research and records the linguistic obligations that their finite
carriers leave open. PG1 is a source and specification packet, not a claim that
the entire Aṣṭādhyāyī has been interpreted, proved complete or implemented.

## Read in this order

1. [Sources and editorial policy](SOURCES.md): editions, commentary attribution,
   Dhātupāṭha, Gaṇapāṭha, phonetics and the distinction from Śaiva philosophy.
2. [Sūtrapāṭha](SUTRAPATHA.tsv): all **3,983 numbered records in the pinned
   ashtadhyayi.com edition**, in Sanskrit, across all eight chapters and 32 pādas.
   This is a text catalogue; presence here does not mean operational coverage.
3. [Foundation register](FOUNDATION_REGISTER.md): selected foundational sūtras,
   Sanskrit, IAST, grammatical function, source links and scope cautions.
4. [Grammar specification](GRAMMAR_SPEC.md): inputs, inherited conditions,
   lexical dependencies, lopa, replacement, conflicts and rule-relative visibility.
5. [Worked derivations](WORKED_DERIVATIONS.md): source-grounded positive cases,
   blocked alternatives and an explicit instance of information lost by a
   surface-only representation.
6. [Coverage and completion gates](COVERAGE_AND_GATES.md): the actual T58–T80
   coverage, the complete chapter inventory and what must be resolved before
   an implementation can be described as grammar-complete.
7. [Validation](VALIDATION.md) and [source pins](SOURCE_PINS.json): what was
   actually checked and which original source bytes were retained.

## What changes in the reading of the earlier work

- **It-lopa is not pratyaya-lopa.** 1.3.2–9 designate and elide markers;
  1.1.62 concerns the disappearance of an entire affix, with the restriction
  1.1.63. Retaining a marker in a software ledger is a useful model, but is not
  itself a derivation from 1.1.62.
- **Pāṇini does not prescribe a universal numerical priority queue.** The
  Kāśikā on 1.4.2 treats equal-strength conflicts; exception relations and
  other priority conditions must be established first.
- **Asiddha is relative to a rule's view.** 8.2.1 and 6.4.22 have different
  scopes. Neither means deleting the actual derivation history.
- **The T80 place-set/Jaccard calculation is a modern finite model.** Its
  agreement with selected substitutions does not make that metric the general
  historical meaning of 1.1.50.
- **A Sanskrit case ending needs interpretation.** The locative *kartari* in
  3.1.68 is an agent/voice condition, not a following phoneme. T80's manually
  supplied records cannot be generalized by mapping every locative to a
  right-hand sound context.

These are additive reading boundaries. Earlier theorem files, result hashes
and source packets remain unchanged. Their exact finite findings remain
findings about their stated models, rather than proof of unrestricted Sanskrit
correctness. The Māheśvara phonetic sūtras are distinguished from Vasugupta's
Śivasūtras. The [SP1 research](../spanda_recognition/README.md) remains a separate
mathematical/philosophical route.

## Immediate result and next research obligation

The text inventory, foundational grammar contract, source interpretation notes
and worked controls are now available together. The next grammar work is to
close each family's inherited scopes, exceptions, lexical classes and
attested alternatives against the chosen commentary. The inventory explicitly
keeps unreviewed material open. No new Sanskrit runtime, calculator feature or
automatic parser is added by PG1.
