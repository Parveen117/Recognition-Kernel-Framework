# PG2 — Lexical data and the limit of a Sanskrit oracle

Author: Monty. 1 November 2026.

## The data layers were audited, not merely named

| Source | Records | Identity/schema result |
|---|---:|---|
| Dhātupāṭha | 2,259 | Unique source IDs; **2,229 root entries plus 30 explicitly tagged gaṇasūtra directives**. The root entries have 1,688 distinct spellings, 402 repeated across multiple records. |
| Gaṇapāṭha | 262 | Unique IDs; all sūtra links resolve. Tags are P:214, A:42, empty:6. Sixty member fields contain markup, and one includes `ityādi`. |
| Uṇādi | 748 | Unique source IDs and nonempty affix fields. Its numbering and domain are separate from the Aṣṭādhyāyī. |
| Paribhāṣenduśekhara | 133 | Separate later metagrammatical source; selected priority clauses reviewed with explicit attribution. |

For the 2,229 roots, the dataset supplies pada tags P:1,132 / A:517 / U:580
and seṭ-status tags S:1,882 / V:41 / A:306. These are supplied
lexical classifications. The it-marker audit does not independently derive
them, and this witness's unaccented teaching strings cannot establish every
accent-dependent decision.

The other 30 rows have `tags=ganasutra` and `-` in the teaching-form and
classification fields. They include **घटादयो मितः** and **आ कुस्मादात्मनेपदिनः**.
These are grammatical directives with scope obligations, not defective root
spellings to feed to an it-lopa routine. Their source identities and text are
retained separately in the report; their scopes are not yet interpreted.

Homonymous roots must retain source ID, gaṇa, sense and teaching form. For
example, the source distinguishes multiple **bhū**, **kṛ** and **mid** entries.
A dictionary keyed only by visible root spelling would collapse distinctions
needed for valid derivations. The existing five named demonstration roots
are not an adequate replacement for that lexical layer.

The Gaṇapāṭha `words` field is not a uniform array of literal strings. Keep
markup, explanatory material, ellipsis and scope pending interpretation.
This review reports the P/A tags literally; it does not assume a verified
membership algorithm or silently expand an open class. The six untyped
records are retained by ID in the result. Uṇādi texts and commentary likewise
need interpreted root/affix domains, not just a JSON import.

## Whole-Dhātupāṭha marker-only diagnostic

| Result | Records |
|---|---:|
| It-only projection exactly matches the publisher headword's phoneme labels | 1,703 |
| Projection differs | 524 |
| Root teaching convention unresolved | 2 |
| Root-entry subtotal | 2,229 |
| Non-root gaṇasūtra directives, retained separately | 30 |
| Source-record total | 2,259 |

The two unresolved root teaching units have an ayogavāha convention outside
this review (`छदिः`, `दुःख`). Anusvāra and
visarga in **ordinary text/headwords** are preserved by the tokenizer; they
are not silently treated as ordinary final hal markers in teaching units.

All differences, unresolved root records and non-root directives are written to
`VERIFICATION_RESULT.json`, not dropped from the denominator. The diagnostic
assumes the publisher's explicit nasal flags as input. It does not prove that
every teaching form is independently complete or correctly recited.

Examples explain why marker erasure cannot be an entire root preprocessor:

| Teaching form | It-only result | Publisher headword | Further grammatical issue |
|---|---|---|---|
| णीञ् | ṇī | नी | Initial ṇ → n under 6.1.65, with its domain restrictions. |
| ष्वदँ | ṣvad | स्वद् | Initial ṣ → s under 6.1.64, also with stated exceptions. |
| स्कुदिँ | skud | स्कुन्द् | Id-marked root and num under 7.1.58; placement and subsequent phonology need their own account. |
| उर्दँ | urd | ऊर्द् | Further normalization/variant review; not explained away as it-lopa. |
| भिदिँ / भिदिँर् | bhid / bhid | भिन्द् / भिद् | Identical projections with different marker units and subsequent obligations. |

Sixty differences have the mechanical signature “initial ṣ only” and thirty
“initial ṇ only.” That observation does not establish the applicability of
6.1.64/65 to all those entries. In particular, Kāśikā supplies exceptions:
do not normalize every occurrence blindly. The remaining 434 differences
are not yet fully classified. The exact-match count is neither an accuracy
score for a Sanskrit generator nor a count of complete root derivations.

Primary readings:
[6.1.64](https://ashtadhyayi.com/sutraani/6/1/64),
[6.1.65](https://ashtadhyayi.com/sutraani/6/1/65),
[7.1.58](https://ashtadhyayi.com/sutraani/7/1/58).

## What the independent reference cases do

The 79 local expectations were read against pinned commentaries/lexical
records, independently of the old `proof_lab` output tables. This means
independence from the existing implementation's expected-output source;
it does **not** mean review by an independent Sanskrit specialist.

Each case records its grammatical inputs, source key, literal textual
anchor, expected local decision and limited verification level. The marker
review preserves teaching identity, sounds, nasality, accent and compound
marker units. The sthānivad review preserves the actual history and asks
only which view the stated operation may use. Priority uses conditional
source witnesses; absent evidence returns `UNRESOLVED`.

A source-anchor match proves that the cited passage exists. The linguistic
interpretation remains a human-readable claim supported by that passage.
A passed local case does not validate all the preceding and following steps
of the example word's full derivation.

## Three probes show why a bare junction is insufficient

| Bare input | Actual T80 result | Reviewed contextual result | Missing input |
|---|---|---|---|
| a + a | ā | a in *pacanti*, 6.1.97 | Apadānta thematic a before guṇa |
| e + a | ay + a | e in *agne'tra*, 6.1.109 | Padānta and following short a |
| o + a | av + a | o in *vāyo'tra*, 6.1.109 | Padānta and following short a |

These are three direct calls of the existing five-rule interface, not a
replay of T80's campaign. They confirm a missing interface/context layer
when trying to apply that finite model to general Sanskrit. The original
finite theorem remains untouched and is not reclassified as claiming
the missing contextual grammar.

An eventual reference interface must distinguish **licensed under declared
inputs**, **blocked under declared inputs**, and **unresolved/outside the
reviewed domain**. It must include lexical identity/sense, morphology,
boundary, rule-relative visibility, optionality, register and accent where
applicable. A boolean judgment on a bare string cannot supply that evidence.

No end-to-end “valid Sanskrit” oracle, soundness theorem or completeness
theorem is claimed by PG2. These are explicit open obligations, even when
all the local checks agree.
