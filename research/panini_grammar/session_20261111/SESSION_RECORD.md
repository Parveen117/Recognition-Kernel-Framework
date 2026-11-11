# Written Sanskrit grammar session · 11 November 2026

Monty · PG119–150 · [PG118 baseline](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/d0a7d69a296f80fd2977985e5235f5eeb770a715) · [PG150 result](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/f38becb5e7414eac06f7f8a826a6768cb05349bd)

The review branch moved from **27,167** to **33,278** written positions. The table counts readings within newly credited positions, so the same word in different requests can contribute more than once. Extra semantic histories and lower-bound witnesses carry no additional position credit.

| Stages | New positions | Readings in those positions | Subject |
| --- | ---: | ---: | --- |
| PG119–121 | 540 | 1,000 | Five selected vṛtādi desideratives |
| PG122–124 | 990 | 1,408 | Colour and sound denominatives, dyutādi membership collation |
| PG125–127 | 360 | 876 | Stop-final denominatives |
| PG128–132 | 1,386 | 2,284 | Nominal roles, purpose and boundary conditions |
| PG133–140 | 0 | 0 | Predicate and participant relations, clause frames and agreement |
| PG141–144 | 900 | 2,336 | kyaṅ with final s, samidh histories and incorporated namas |
| PG145–148 | 1,440 | 2,140 | Action and experience, mocking agreement, perfect collation |
| PG149 | 450 | 640 | Wrongful intention, purpose and direct experience |
| PG150 | 45 | 63 | Five prefixed ṇiṅ presents |
| **Total** | **6,111** | **10,747** | |

## What the machine can represent in the written specification

[Clause frames](../clause_frame_interchange/README.md) encode actor identity, case, role and event membership. Eleven concrete frames instantiate a JSON Schema. In the two-object milking example the cow and the milk retain distinct participant identities through the same accusative case. [PG149](../intention_and_experience/README.md) retains a separate history when an identical word can express either intending a deed or experiencing one's own state. [PG150](../prefixed_ning_present/README.md) adds the other direction of ambiguity: two nasal spellings each preserve the same two robe events. These are finite, inspectable examples of the formal relation.

## Source decisions still open

- [PG121 collation](../desiderative_perfect_policy/README.md) compares 45 A-entitlement perfect slots. The compared primary reading sets are disjoint in 27 and partially overlap in 18. The written count includes their positions with the visible qualification. Traditional licensing remains open.
- [PG131](../nominal_desire_outer/README.md) retains 193 positive readings for 54 outer udaka requests without assigning position credit to those requests. The unresolved question concerns 6.4.50 after the udan selection.
- [PG150](../prefixed_ning_present/README.md) leaves the other nine lakāras of these five prefixed formations open. Immediate tractable work comprises loṭ, vidhi-liṅ and laṅ, a grid of 135 candidate slots. The laṅ augment must be placed with the prefix boundary available. The aorist witness for bhāṇḍa needs a separate collation.

## Effort and verification

A two-hour mixed writing session yielded about 3,050 new positions per hour. A planning allowance of **0.5–1 hour** for the next 135 candidate slots includes the independent prefix and augment review. This is a planning estimate. The total hours to a runnable, validated Sanskrit compiler remain uncalibrated. The catalogue has 3,983 identified sūtras and the lexical inventory has 2,229 root entries. Neither supplies a count of the outstanding rule interactions, semantic constructions or executable implementations. A project completion percentage remains open.

PG119–148 used static document checks under Python 3.12.14. PG149–150 used static source, table and query comparisons in JavaScript while the Python workspace was unavailable. Grammar tests, grammar generators, certificate replay and CI remain deferred. Counts here record the written specification.
