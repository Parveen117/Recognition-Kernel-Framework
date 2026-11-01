# PG2 — Verification of the pending grammar

Author: Monty. 1 November 2026.

**The grammar is not complete.** This packet investigates the six open areas
identified after PG1. It adds source-grounded counterexamples, an annotated
scope reader, bounded review interpreters, and reproducible results. It does
not extend the operator engine or quantum calculator. CI and merging are
deferred at the owner's request.

Baseline: `ada439f6ba3109d798b41c216fe7cedc79e60afb`, including the theorem branch's
`06f5bef` and `3da3466`. Historical code, theorem packets and certificate pins
are unchanged.

## What was actually verified

| Requested gap | Result of this review | What remains open |
|---|---|---|
| Adhikāra / anuvṛtti | All 3,983 source records parsed into 9,266 anuvṛtti and 14,323 adhikāra term-reference edges; 73 declared headings. All references resolve. Six commentary reviews cover 344 range flags and two missing-heading flags. | The input is publisher annotation, not raw Sanskrit. Term splitting, 279 downstream `vā` annotations, commentary alternatives, and automatic semantic scope inference remain open. |
| Apavāda / nitya / antaraṅga | Three conditional exception edges and one source-attested nitya ordering; nine local priority cases. Later paribhāṣā qualifications are attributed explicitly. | General nitya/antaraṅga inference, optionality and a complete rule-relative resolver; the T66 *edhe* path still needs independent adjudication. |
| 1.1.56–59 | Four query-specific contracts and 26 positive/negative reference cases, including the lopa-only qualification inside 1.1.58 and temporary restoration in 1.1.59. | Automatic classification of every grammatical query and interaction with all other restrictions. |
| It-saṃjñā 1.3.2–8 | All seven rules represented in authored records; 44 cases, of which 43 resolve and one deliberately remains unknown. Composite `ñi/ṭu/ḍu` and supplementary `ir` designation retain unit identity. | Exhaustive teaching conventions and commentarial exceptions; these records are not extracted automatically from Sanskrit. |
| Lexical data | Schema and identity audit of 2,259 Dhātupāṭha records: 2,229 root entries and 30 tagged gaṇasūtra directives; also 262 Gaṇapāṭha and 748 Uṇādi records. All 262 gaṇa-to-sūtra references resolve. Every root receives a marker-only diagnostic. | Full lexical interpretation, root normalization, sense-sensitive selection, gaṇa membership and Uṇādi derivations. |
| Soundness reference | 79 commentary/lexicon-grounded local cases, 24 structural controls and three new probes of the old boundary-free sandhi interface. 136 literal source anchors checked. | A complete Sanskrit acceptance oracle, end-to-end correctness and completeness, cross-edition and independent specialist review. |

The successful checks mean **agreement with these explicitly supplied local
expectations**. They do not turn every referenced sūtra into a verified whole
rule. Some successful controls correctly return `UNRESOLVED`.

## Findings that change implementation requirements

1. **A scope edge needs a term, not just a parent rule.** Borrowing `dhātoḥ`
   from 3.1.22 into 3.1.68 does not import the `yaṅ` operation. In 6.2.111,
   `uttarapadasya` and `ādi` have different endpoints. 1.4.13 defines *aṅga*;
   it is not the *aṅgasya* heading of 6.4.1.
2. **Keep original teaching-form positions.** `गमॢँ` loses nasal vocalic `ḷ`;
   the resulting `m` must not be reclassified as a newly final it-marker.
3. **Keep compound-marker identity.** `भिदिँ` and `भिदिँर्` have the same
   marker-only projection `bhid`, but their marker units are `i` and `ir`.
   Kāśikā 7.1.58 explicitly excludes the latter from standalone *idit*
   treatment. A string-only test would miss this difference.
4. **Sthānivad is a restricted view.** Kāśikā 1.1.58 restricts the
   svara/dīrgha/y-lopa prohibition to deletion substitutes. 1.1.59 restores
   the original form for its reduplication query and then leaves the actual
   substitute in place. Neither licenses copying every property forever.
5. **Priority requires a witnessed relation.** Domain containment on a small
   sample, later rule number, number of conditions, or a generic
   “phonology before meaning” label does not establish the full priority law.
6. **The same junction needs different outcomes in different contexts.**
   Bare `e+a` and `o+a` in T80 do not encode the padānta condition of 6.1.109;
   bare `a+a` does not encode the apadānta condition of 6.1.97. These are
   limitations on applying that finite carrier to general Sanskrit, not a
   falsification of its stated finite certificate.

## Coverage correction

The pinned edition contains **3,983 numbered records**. Counts such as 3,959
belong to other counting/editorial conventions; do not mix denominators.

Static inspection of the eight declared T58/T63–T68/T80 modules identifies
**61 distinct operational or semantic-mapping IDs**. This is code presence,
not an exhaustive census of all embedded predicates, and not 61 complete rules.
T80 has **five generic sandhi records**, plus five specialized Python word
routines. Because 6.1.78 occurs in both, these ten operation instances have
**nine distinct IDs**. It has no generic raw-Sanskrit-to-word compiler.

The old demonstrations already include at least **bhū, gam, nī, edh, labh**;
“two roots only” describes the earlier T58 carrier. The later finite resolver
also extends beyond the nominal carrier. These corrections do not materially
close the full grammar gap. No “percent grammar verified” is computed here.

## Files and reproduction

- [Scope review](SCOPE_REVIEW.md) and [individual adjudications](SCOPE_ADJUDICATIONS.json).
- [Rule reading and sources](RULE_REVIEW.md), [marker records](MARKER_RULES.json),
  [inheritance contracts](INHERITANCE_RULES.json), [priority witnesses](PRIORITY_WITNESSES.json).
- [Lexicon and oracle limits](LEXICON_AND_ORACLE.md), [independent local cases](ORACLE_CASES.json).
- [Actual results](VERIFICATION_RESULT.json), [source pins](SOURCE_PINS.json),
  [verification command](verify.py), [scope/census reader](source_audit.py),
  [marker review interpreter](marker_review.py).

Use the source repository `https://github.com/ashtadhyayi-com/data` at commit
`5744762f010d677cfb43f347a42d02796cf615d6`. From this repository's root:

```sh
python3.12 research/panini_grammar/verification/verify.py --source-root /path/to/ashtadhyayi-data
```

The command checks source/code hashes, checks the literal citation anchors,
reproduces this stage's controls and compares its result with the committed
report. It does not start CI or replay previous test campaigns. `--write`
explicitly writes only the new PG2 report after a deliberate review change.
The separate [validation record](VALIDATION.md) distinguishes linguistic
controls from repository navigation checks.

The next linguistic obligations are the 339 flagged memberships needing
optional/split-term interpretation, general priority witnesses, and complete
root preprocessing with marker identity retained. Passing these local checks
does not authorize labeling any of those obligations complete.
