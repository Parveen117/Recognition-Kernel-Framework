# PG2 — Scope evidence and editorial contradictions

Author: Monty. 1 November 2026.

The source is the pinned publisher's `sutraani/data.txt`. Its `an` field
encodes `term$source-key` and its `ad` field encodes `term$chapter$pāda$number`.
`type=AD` supplies a declared heading endpoint. These are editorial
annotations. Parsing them is useful progress beyond supplying each scope by
hand in a rule routine; it is not discovering scope from raw Sanskrit.

Every parsed edge retains its original annotation, kind, borrowed term,
source and target. The reader never imports an ancestor's whole action,
silently fixes a reference, or treats a heading's self-declaration as a
derivation cycle.

## Whole-source structural result

| Quantity | Observed |
|---|---:|
| Numbered records | 3,983 |
| Anuvṛtti edges | 9,266 |
| Adhikāra edges | 14,323 |
| Declared AD headings | 73 |
| Heading self-declarations | 73 |
| Missing referenced sūtras | 0 |
| Forward edges in this witness | 0 |
| Self-anuvṛtti edges | 0 |
| Adhikāra memberships outside the declared interval | 344 |
| Adhikāra sources without an AD tag | 2 |

The absence of forward edges is an observation about this annotation witness,
not a universal ban on other traditional readings of scope.

## Requested scopes

| Source | Declared endpoint | Annotated members, including declaration |
|---|---|---:|
| 3.1.1 प्रत्ययः | 5.4.160 | 1,821 |
| 3.1.2 परश्च | 5.4.160 | 1,820 |
| 3.1.91 धातोः | 3.4.117 | 541 |
| 6.4.1 अङ्गस्य | 7.4.97 | 613 |
| 1.4.13 यस्मात्प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम् | A saṃjñā, not AD | 0 |

For 3.1.68, the witness borrows `sārvadhātuke` from 3.1.67 and `dhātoḥ`
from 3.1.22. The latter edge does not carry the source rule's `yaṅ` action.
For 6.1.87, the inherited term is **aci**, not **iki**. T80's `ik`
restriction is a restriction of its authored record/carrier, not the literal
inherited condition in this source.

## Adjudication of all six flag groups

| Flag group | Count | Commentary reading and disposition |
|---|---:|---|
| 4.1.82 `vā` after 5.2.140 | 279 | Kāśikā ends the heading before 5.3.1 and says some subsequent svārthika affixes are obligatory. Quarantine automatic import of uniform optionality; review later rules individually. |
| 6.2.111 `uttarapadādiḥ` after 6.2.137 | 60 | Kāśikā continues **uttarapadasya** to the pāda end but **ādi** only through 6.2.137. Split the inherited term before interpreting later accent rules. |
| 6.1.135 memberships at 6.1.155–157 | 3 | The endpoint field says 6.1.154; Kāśikā explicitly continues through 6.1.157. The longer interval is supported by this commentary. |
| 6.1.84 memberships at 6.1.110–111 | 2 | The endpoint field says 6.1.109; Kāśikā ends before 6.1.112. Commentary at 110 and 111 also explicitly replaces both members by one. |
| 4.2.92 → 4.3.23, missing AD tag | 1 | Kāśikā expressly calls **śeṣe** an adhikāra. The incomplete type tag does not invalidate the cited inheritance. |
| 6.2.14 → 6.2.144, `antaḥ` | 1 | 6.2.14 has a different sūtra. 6.2.143 is **antaḥ**, explicitly a heading in Kāśikā. Record 6.2.143 as the suggested correction while preserving the original erroneous reference. |

Every raw flagged edge is present in `VERIFICATION_RESULT.json`; every group
has a citation anchor in `SCOPE_ADJUDICATIONS.json`. No correction is silently
written back into the source. A structural flag is not automatically a
grammatical error: the two longer-interval cases demonstrate why commentary
adjudication is necessary.

The graph is also not a complete semantic account even where it is
structurally consistent. Kāśikā 1.1.59 explicitly describes an **aj-ādeśa**;
the review contract retains this vowel-substitution condition rather than
assuming that the graph's listed terms are an exhaustive interpretation.

## Primary reading links

All references use the pinned Kāśikā witness, with per-file SHA-256 in
[SOURCE_PINS.json](SOURCE_PINS.json). Human-readable source pages:
[4.1.82](https://ashtadhyayi.com/sutraani/4/1/82),
[6.2.111](https://ashtadhyayi.com/sutraani/6/2/111),
[6.1.135](https://ashtadhyayi.com/sutraani/6/1/135),
[6.1.84](https://ashtadhyayi.com/sutraani/6/1/84),
[4.2.92](https://ashtadhyayi.com/sutraani/4/2/92),
[6.2.143](https://ashtadhyayi.com/sutraani/6/2/143).

These conclusions belong to this textual reading. They do not claim that all
commentaries assign identical scopes or that a Sanskrit syntactic parser now
exists in the repository.
