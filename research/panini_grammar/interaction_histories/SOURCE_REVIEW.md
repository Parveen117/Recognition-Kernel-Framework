# PG47 — Sources for addressed interactions

Author: Monty. 4 November 2026.

The primary edition is [ashtadhyayi-com/data at 5744762f](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6),
full commit `5744762f010d677cfb43f347a42d02796cf615d6`. Its 3,983-record
catalogue remains the denominator. The five complete primary files are
rehashed from immutable objects; their byte lengths, SHA-256 and Git blob
identities are in [SOURCE_PINS.json](SOURCE_PINS.json).

## S1. Reading ledger and archive

|Material|Archived fields|Commentary fields read in full|
|---|---:|---:|
|Sūtra texts|132|—|
|Kāśikā|132|132|
|Siddhāntakaumudī|39|39|
|Nyāsa|30|30|
|Vasu English|0|0|
|Total|333|201|

The archive contains exactly the reported nonempty commentary readings plus
the corresponding sūtra texts, deduplicated by source and ID. The 132 IDs
include 103 referenced by the history register and additional read controls.
Every one already belongs to the inherited combined and written sets.
Archive presence adds no catalogue credit.

Nyāsa **7.1.9** and **7.3.102** were inspected and are empty. They are
recorded separately and excluded from nonempty-field counts. No other field
is manufactured to fill these keys, and no Vasu semantic review is implied
by rehashing its complete primary file.

## S2. Decisions that affect the interface

|Source notes|Principal distinctions|
|---|---|
|[A](SOURCE_NOTES_A.md)|Fixed genitive relations, whole versus segment replacement, marker identity, directional adjacency and admitted comparison|
|[B](SOURCE_NOTES_B.md)|Same-rule clause origins, deleted-affix cause, base versus पद consumers, ordinary exclusivity and Vedic dual use|
|[C](SOURCE_NOTES_C.md)|Source-supported strength, conflict through dependencies, reapplication policies and consumer-relative visibility|
|[D](SOURCE_NOTES_D.md)|Coupled optional branches, inner/outer suffix ownership, preserved origin and prerequisite टि deletion|

**Clause-level designation identity.** Nyāsa 1.2.44 distinguishes the main
एकविभक्ति clause's nonordering designation for कौशाम्बी from the च
supplement's ordering support for निस्. A designation keyed only by sūtra ID
would lose that distinction. The interface therefore records rule, clause,
policy, cause and consumer. This refines PG46's summary while preserving its
original files and the valid main-clause restriction.

**Current and historical evidence.** Kāśikā 7.1.9 explicitly allows the
भूतपूर्व basis used in its नित्य relation. That source permission does not
allow every previously present sound to satisfy every current query. The
वृक्षेभ्यः continuation reassesses 7.3.102 rather than replaying its old
proposal. Nyāsa's जाति/द्रव्य accounts remain distinct policies; the present
example gives different reasons for the same blocked continuation, not a
source-attested pair of divergent forms.

**Dependent realization.** All three commentaries at 4.1.38 support औ with
ङीप्, ऐ with ङीप्, or neither. No independent suffix choice supplies a
fourth branch. At 4.1.78, whole-base syllable weight and inner-affix descent
origin are different predicates. Nyāsa's औडुलोम्या discussion requires the
earlier टि deletion before the heaviness gate and ष्यङ् replacement; later
heaviness cannot circularly license an earlier event.

## S3. Local source corrections and literal retention

|Locus|Literal issue|Adopted treatment|
|---|---|---|
|Nyāsa 3.4.117|एतेर्लिङि 7.4.24 is cited for etva in उपस्थेयाम|Use 6.4.67 एर्लिङि for the qualified स्था → स्थे consumer; retain the printed reference|
|Kāśikā 4.1.78 control|The आर्तभागी continuation is labelled ङीप्|Retain Nyāsa's explicit correction to ङीन् under 4.1.73, as already recorded in PG45|
|Nyāsa 6.3.25|Damaged text and an incorrect number accompanying उरण् रपरः|Retain the literal field; use its explicit n-retention explanation for the addressed आनङ् history|
|Kāśikā 4.1.96 / Nyāsa 4.1.78|Damaged औङुलोमिः display, repetitions and other reference slips|Use the corroborated औडुलोमि/औडुलोम्या witness and explicit ordered explanation, without repairing archive bytes|

For the first correction, Kāśikā/Kaumudī/Nyāsa **7.4.24** describe prefixed
इण् shortening. The separate **6.4.67** fields describe the qualified
घु/मा/स्था/गा/पा/जहाति/सा etva domain; Kāśikā gives स्थेयात् and Kaumudī
retains the आर्धधातुक condition. The wrong reference is therefore localized;
the source's dual-consumer argument at 3.4.117 remains usable.

All markup, spelling, accent displays and embedded references remain unchanged
in [SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json). A legible written witness is
not silently substituted for a missing derivation. Each history names which
input was supplied, which step is constructed and what remains downstream.
Source examples, authored evidence-omission controls and mathematical
preservation arguments are distinguished. No manuscript collation or general
semantic review of all 3,983 interpretations is claimed.

## S4. Provenance checks and evidence limit

The **39-pin** manifest has five primary, thirteen predecessor/adapter,
one companion and twenty authored-file identities; it excludes itself.
Static checks compare every registered history heading/line and source ID,
every literal field, file identities, exact inherited coverage sets, local
document links and changed-file scope. These are transcription and provenance
checks. No grammar generator, runtime test or certificate replay supplies
the written outcomes.
