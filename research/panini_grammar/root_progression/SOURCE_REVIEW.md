# PG3 — Source reasoning and explicit limits

Author: Monty. 1 November 2026.

The source witness is the
[ashtadhyayi.com data repository at 5744762](https://github.com/ashtadhyayi-com/data/tree/5744762f010d677cfb43f347a42d02796cf615d6).
[SOURCE_PINS.json](SOURCE_PINS.json) pins six external files and eleven
historical repository files. Every JSON citation contains its file, source
key, literal anchor and, for lexical records, field. Literal-anchor checks
confirm attribution; interpretation remains a review obligation.

## Root substitutions and their exceptions

[Kāśikā](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/kashika.txt)
at `61064` reads 6.1.64 as replacement of root-initial ṣ by s and states the
subdhātu, ṣṭhivu and ṣvaṣk exclusions. At `61065`, 6.1.65 similarly replaces
root-initial ṇ and excludes subdhātus. Interior sounds are outside these
initial selectors. Root status and origin therefore enter explicitly.

Four pinned lexical IDs are excluded from ṣ → s: `1010105` (ष्वष्कँ),
`1010114` (ष्वक्कँ), and `1010641` / `1040004` (ष्ठिवुँ in two gaṇas).
The second requires a separate attribution:
[Nyāsa](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/nyaas.txt)
at `61064` discusses the ṣvakk reading explicitly, including
`ष्वक्केरप्यज्दन्त्यपरा` and the form ष्वक्कते. It must not be attributed to
the Kāśikā's ṣvaṣk spelling without qualification.

The first unqualified implementation changed the already matching ṣvakk row
to svakk. That diagnostic led back to Nyāsa; the exception was admitted only
after locating this primary textual support. The expected headword itself
is not an exception rule. The four IDs bind the reviewed lexical identities;
the caller remains responsible for supplying the identity of its teaching form.

The consequences for a following retroflex cluster are not implemented here.
For example, ṣṭuc becomes sṭuc in this intermediate state, not the complete
lexical headword stuc. That difference remains in the report.

## Identities, num and placement

Kāśikā `71058` gives num for an idit root at the teaching-root stage. It also
states `इरितां समुदायस्येत्संज्ञा`: ir is designated as a compound, so its i
does not independently make the root idit. PG3 queries complete marker units,
not a set of letters that happened to disappear. The ñi prefix of 1.3.5 is
likewise not a standalone nasal i-it.

Kāśikā `11047` explains अचः as a partitive genitive and places an ordinary
m-marked augment after the last vowel. This is another reason a general
compiler cannot turn every genitive into a replacement target. The same
commentary states the masj qualification, with num before the last consonant
for the relevant 7.1.60 process. PG3 licenses only 7.1.58 num and does not
generalize T82's ordinary placement routine to masj or all augments.

The original teaching records and sound positions survive in the root state.
The n of num has a new identity and records its 7.1.58 license and 1.1.47
placement. T81's ṭi selector finds the last-vowel suffix; T82's `nu~m` contract
provides n and ordinary mit placement. Expected lexical spellings are absent
from this computation.

## A restricted phonetic query

Kāśikā `83024` reads 8.3.24 as anusvāra for non-pada-final n/m before jhal,
and supplies negative contexts such as राजन् भुङ्क्ष्व and रम्यते.
Kāśikā `84058` gives the parasavarṇa continuation, with examples including
शङ्किता and कुण्डिता. PG3 admits only the newly inserted num n followed inside
the same supplied root by jhal. If the following sound is one of the twenty
non-nasal varga stops, the query selects its unique nasal counterpart from
T81's corresponding five-member class. Before ś, ṣ, s or h, this query stops
at anusvāra. It does not transform pre-existing root nasals or supply nasalized
semivowel alternatives.

Kāśikā `82001` identifies the last three pādas as the relevant asiddha domain.
The phonetic result is therefore stored as a separate query result and cannot
be passed back as a successful preprocessing state. This is a limited
interface separation. It does not decide all interactions within Tripādī,
all exceptions to 8.2.1, or the independent 6.4.22 domain.

## Corrections to earlier local expectations

**Lakāras.** Kāśikā `34077` identifies the common l of the ten lakāras after
their distinguishing markers are set aside.
[Tattvabodhinī](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/tattvabodhini.txt)
at the same key explicitly says `लस्येत्संज्ञा तु न भवति`.
[Bālamanoramā](https://github.com/ashtadhyayi-com/data/blob/5744762f010d677cfb43f347a42d02796cf615d6/sutraani/balamanorama.txt)
at `32123` identifies the a and ṭ markers of laṭ. The new fixtures supply
conventional nasal vowels explicitly; their nasal notation is not claimed to
have been parsed from an unmarked printed form.

There are two distinct issues in T82: its raw lakāra inputs omit that nasal
notation, and its non-taddhita rule deletes initial l. With the same annotated
input `la~ṭ`, T82 leaves the empty string whereas the reviewed profile retains
l. The direct probes record both original-input and same-annotated-input
results for all ten lakāras. Agreement with T82's supplied table cannot settle
the source disagreement.

**jh and the related exceptions.** Kāśikā `13007` anticipates later replacements
of jh, ṭh and ḍh. Nyāsa `13007` explicitly describes the cited ch replacement
as `इत्संज्ञापवादम्`. Kāśikā `71003` states the replacement of an affix's jh by
ant and also discusses Uṇādi झच्. PG3 preserves these initial sounds only for
the identified affixes listed in its records. It does not install an
unconditional exception for an arbitrary unknown affix beginning with one
of these letters.

The PG2 `jhi-affix-identity` fixture had removed jh while preserving the affix
identity. Preserving identity was useful, but it did not justify that it
designation. PG3 explicitly supersedes the linguistic reading and keeps the
old fixture/result intact as historical evidence. The current profile retains
jh; a new counterexample probe records the change.

**Savarṇa.** Kāśikā `11009` says that ḷ has no long forms and gives the
supplementary ṛ/ḷ savarṇa relation. T81's finite table includes ḹ and separates
ṛ from ḷ. Its stated table result must therefore remain a table result, not a
complete account of this commentary. PG3 uses only T81's stop-varga classes
and last-vowel selector. A complete vowel, accent and nasalization profile
needs another source-backed stage.

**Aṅga.** Kāśikā `14013` ties the beginning of aṅga to the constituent that
licenses the affix. The whole-prefix result in T82's supplied gam/nī cases
does not establish that the start of an arbitrary string is always the
licensing constituent. PG3 introduces no general aṅga inference.

## Counting and remaining obligations

The inherited ledger contains 171 declaration rows, including 43 merely cited
and two misnumbered rows, with `astadhyayi_total=3959`. The pinned sūtra witness
has 3,983 numbered records. PG2's static T80 inspection found five generic
records and five specialized routines with nine distinct operation IDs; the
ledger's ten `compiled` labels are not ten independent generic records.
Neither source inventory nor headword agreement is a grammatical coverage
denominator.

The 45 local expected cases were authored from this reading and retain their
citations. They have not received independent specialist or cross-edition
review. Inherited-scope parsing, full exception competition, unrestricted
sthānivad, gaṇasūtra/Uṇādi derivation and an independent soundness reference
remain open. The report keeps all unknowns and differences visible.
