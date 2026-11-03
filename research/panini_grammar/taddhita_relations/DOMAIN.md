# PG35 — Domain of the taddhita relation constructor

Author: Monty. 4 November 2026.

## D1. What is constructed

PG35 constructs a source-relative **semantic admission → nominal affix
selection → addressed modification/elision** relation for the 313 numbered
entries of 4.2 and 4.3 in the pinned edition. The five rule tables specify
each entry's gate, action, inherited meaning, priority/boundary and a source
witness or control. This is new written construction, not operational
credit for copying a catalogue. Some rows select affixes; others restrict
scope, block a selection, transfer a construction, stipulate a formation,
or act on a selected affix. All are counted once by source ID.

The output is an owned derivational record. Complete surface phonology,
accent assignment, feminine formation, nominal declension, unrestricted
compound formation and sentence interpretation are later layers. Source
words in the tables illustrate the contracts; they are not new executed
or independently completed word positions. The finite-position total
therefore stays **11,552**. PG35 adds **zero** counted paradigm positions.

## D2. Input with evidence, not a bare string

An input is a finite record

\[
q=(x,\mathsf{sense},\mathsf{relation},\mathsf{support},
   \mathsf{target},\mathsf{register},\mathsf{policy},\mathsf{evidence}).
\]

- **x:** prātipadika identity, original source spelling, current phonemes,
  original accent, derivational tree and owned affixes. A compound retains
  its actual pada boundaries and class; an apparent suffix in a string is
  not proof of an original affix.
- **sense:** the particular lexical reading. Village Kāśi and patronymic
  Kāśi, pronoun bhavat and the bhū participle, and a deity and a homonymous
  human are separate inputs.
- **relation/support:** the intended semantic edge, its participants, and
  the appropriate first-mentioned case relation in the explanatory phrase.
  This is not a claim that every supplied surface case ending is retained
  after nominal derivation.
- **target:** denotation and source restrictions, including name-status,
  human/non-human, fruit, food, clothing, book, school, chapter, river, well,
  ornament, debt or place. These predicates need witnesses; suffix selection
  does not manufacture them.
- **register/policy:** bhāṣā or Chandas, the adopted Kāśikā reading, and
  explicitly selected commentary extensions. A Vedic-only row does not
  become a modern-language default.
- **evidence:** exact rule/source key, gaṇa ordinal and literal membership,
  case/meaning evidence, scope/exception decisions, and named predecessor
  derivation when a rule transfers another construction.

A predicate has T, F or ?. F means evidence against admission to that rule;
? means missing or disputed evidence. A missing accent, historical geography,
gaṇa membership, name-status or semantic relation is not F. It must not
silently unlock the residual affix. Return **Open** for that unresolved
selection. F for this constructor is not a universal rejection of Sanskrit.

## D3. Inherited foundation

4.1.76 supplies taddhita status. 4.1.82 supplies semantic compatibility,
selection of the first-mentioned supporting member, and optional derivative
formation versus the analytic phrase. Its option is distinct from an
optional affix or optional lopa. 4.1.83 supplies residual अण् up to its
प्राग्दीव्यत् boundary, after exceptions have been excluded. These three
IDs were already in the baseline union and add no new breadth here.

The supplied nominal foundation also owns prātipadika identity, it markers,
replacement/lopa distinction and compound structure. PG35 does not recount
such dependencies as newly completed rules merely because a table mentions
them. Original markers survive as history even when their pronunciation
will later disappear. In particular अण्/अञ्, वुन्/वुञ्, ठक्/ठञ्/ठप्,
छ/छण्/छस् and य/यत्/यन्/यञ् cannot be merged by a surface suffix observer.

## D4. Scope is typed and bounded

| Family | Meaning admission | Shared selector scope | Important reset |
|---|---|---|---|
|Colour/time/sāman/chariot|4.2.1,3,7,10|Separate instrumental relations through 12|A special lexical row inherits only its own relation|
|Prepared/placed food and observance|4.2.14–20|Locative support|4.2.21 switches to a nominal full-moon relation|
|Devatā|4.2.24|Through 35|Saṃjñā from 21 does not carry into 24|
|Collection|4.2.37|Through 51|4.2.52 retains GEN but changes the meaning to territorial sphere|
|Study/Know|4.2.59|Through 66|The inner PromulgatedBy record is independently supplied|
|C: named places|4.2.67–70|Selectors/modifiers 71–91|Four meanings are a disjoint union of witnessed relations|
|S: śeṣa|4.2.92|Lexical selectors 4.2.93–4.3.24 and admitted relations through 4.3.133|4.3.134 closes S; its suffixes do not leak into M|
|Time selectors|4.3.11–24|Apply to qualified S meanings|Time-only meanings at 43–52 do not restrict general 53|
|Commentary/Existing in subject|4.3.66|Two case-labelled meanings through 73|74 starts ablative ArrivedFrom|
|Promulgation|4.3.101|102–111 with each text/register restriction|112 resets to SameDirection|
|Belonging|4.3.120|Through 133|Not itself ModificationOf|
|M: material|4.3.134–135|136–168, with source-specific part/product gates|145 is explicitly dung; not a forced M classification|

For scope-only rows such as 4.2.92, the constructed effect is to open/close
the indicated rule view. It does not append a suffix. For 4.3.25/38/53 etc.,
the effect is semantic admission followed by the already qualified selector,
not an invented new upadeśa. This avoids crediting a copied heading as a
word-generation rule.

## D5. Lexical classes and variant policy

Gaṇa admission uses `(source commit, source file, rule key, gaṇa ordinal,
literal member, attached member condition)`. The head member and quoted
positive examples in each table are finite witnesses. Other literal members
can enter only with their own source witness and qualifications. This is a
bounded lexical interface, **not** a newly normalized complete Gaṇapāṭha.
Ākṛtigaṇa and bahulam require a witnessed usage; resemblance is insufficient.

Historical regional predicates, vṛddha designation and accent are supplied
with evidence. No modern map lookup, accent predictor or semantic classifier
is claimed. Damaged or competing lexical spellings are retained in the
archive; an unresolved identification remains Open rather than selecting
whichever affix increases coverage.

The ordinary Kāśikā exposition is adopted. Vasu is a useful historical
translation, but a damaged English affix label does not override the sūtra
and Sanskrit commentary. At 4.3.27 the *kecit* extension of saṃjñā through
37 is a separate policy. At 4.3.22 Kāśikā's explicit three-way Hemanta
reading, including the bhāṣā extension of ठञ्, is retained. At 4.3.159,
the वा of 158 does not continue. See [source decisions](SOURCE_REVIEW.md).

## D6. Admission and completion are separate statuses

The constructed output includes base history, semantic edge, original
selected affix, clause/branch label, augment/substitution/lopa targets,
scope and precedence witnesses, and pending realization obligations.
An admitted affix record is `WRITTEN_SELECTION`; it is not `COMPLETE_WORD`
and is not `EXECUTED_PASS`. An unresolved input is `OPEN`; a ruled-out
candidate is `NOT_THIS_RULE`. These statuses are part of the handoff.

Optionality creates a finite set of positive histories only after the
input is admitted. It is neither probabilistic selection nor uncertainty.
The analytic phrase option of 4.1.82 is retained separately and does not
multiply the affix inventory or inflate the 313-ID count.
