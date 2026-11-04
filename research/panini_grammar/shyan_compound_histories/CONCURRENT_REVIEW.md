# PG51 — T157–T159 source and adapter review

Author: Monty. 4 November 2026.

The companion advances two commits from PG50's checked
9fc4399b9a785ca830b7c9c507f95fc684a242fd to
**1f2453fca40d5fd152684018e6cb0bfc17e17225**: T157 adds another register
comparison, and T158 corrects the verbal table on śās. This review reads
the full two capsules, new comparison module, its test, the table's test,
the affected table diff, the cited PG23 register/derivation/source review,
and selected primary fields. The entire table was byte-pinned, not reviewed
line by line. No grammar module was imported or executed.

## CR1. Reported results and selected scope

|Report|Attributed result|Boundary|
|---|---|---|
|T157 at 98c91c3|999 selected positions; 702 replayed; 692 agree; 10 śās discrepancies adjudicated to the written forms|Selected PG23/25/31/32 registers; 297 undeclared positions and 189 causal lṛṅ positions separately outside|
|T158 at the checked head|702/702 selected T157 comparisons agree after the table correction; adjudication list empty|Upstream report and updated snapshot assertions, not reproduced here|
|T158 verbal-table suite|914/914, with six new śās witness cells|A finite surface suite; other lanes and kṛt results are reported unchanged|
|PG32 comparison|54 augmentless cells obtained by withholding 6.4.71/72 rows|An explicit adapter for supplied māṅ cases, not a general semantic māṅ-context implementation|

The current expected strings are:

|File|Stored certificate string|
|---|---|
|PG_MODAL_REGISTERS_II_EXPECTED.sha256|632be289b106ca469df3de3bb845052750b1e80a84a8332fc03297260f052705|
|TING_RULE_TABLE_ENGINE_EXPECTED.sha256|4cf5530af6beda30b4392092d9d31f2c059b0de35cbda748250cf344cf3931ca|
|PG_WRITTEN_REPLAY_EXPECTED.sha256|c98d6ba3fcffd8ed8e2b997ad43440eb9fb6b3b8fefe2dcde9550923e9337b17|
|PANINI_KERNEL_EXPECTED.sha256|210031924ed15c2828bb5ef637f06df5478d385e1b65d968fa0fe3489a6fa5bf|

These strings were read, not regenerated. Certificate payload hashes and
source-file hashes are different objects. PG51 gets zero runtime-verification
credit from the reports.

## CR2. Useful correction, but surface and history evidence differ

The changed rows add 6.4.35, exclude the competing 6.4.34 operation before
ordinary hi, extend the latter's guard to the P-liṅ case, and remove the
overly narrow following-context exclusion from śās's 8.3.60 row. The
source-grounded target forms śādhi and śiṣyāt were already in PG23.
Kāśikā 6.4.34 and 8.3.57/60 support the stated vowel/ṣ changes on their
qualified domains. This does not establish all roots or moods outside the
table's guards.

Two source/representation qualifications remain:

1. **The adopted śādhi event orders differ.** T158 attributes a dhi-first
   order to Kāśikā and puts 6.4.35 after 6.4.101 in the table. The pinned
   Kāśikā 6.4.22 instead explicitly permits dhi after completed शाभाव
   because that change is असिद्ध for the qualified query; Kaumudī 6.4.35
   says the same. PG23 E2 retains that earlier-s view. Thus agreement on
   śādhi does not by itself replay PG23's written event history, and the
   attribution of the engine's order as “Kāśikā's order” needs correction
   or a separately identified source. The present review does not declare
   the alternative engine schedule universally invalid.
2. **The ṅit feature has an owner.** Kāśikā 3.4.103 expressly assigns
   operative ङित्त्व to liṅ, not to the yāsuṭ augment itself. The new
   `liṅ and P` guard reaches the intended bounded context, but a faithful
   grammatical record should preserve that feature owner rather than turn
   “ṅit yāsuṭ” into an unrestricted augment-property rule.

T158 labels 6.4.35 surface-coincident with a later s-deletion on its suite.
That disclosure is useful: absence of a changed surface when one row is
withheld does not prove equality of the two derivational histories. Its
six explicit oracle cells also differ from T157's addendum wording that
all ten śās cells are in that table suite; ten comparisons are corrected,
while the newly inserted `W_ORACLE` names six.

## CR3. The PG23 tātaṅ count drops śiṣṭāt

The full PG23 P3 table contains **eight named tātaṅ words**, one each for
han, śās, rud, svap, śvas, an, jakṣ and brū. Its own P4 counts their
sixteen profile additions across 3sg and 2sg.

The new module counts PG23's words using a row pattern ending in literal
`tāt`. **śiṣṭāt ends in ṭāt**, so that spelling is excluded even though
it belongs to the same tātaṅ construction. The resulting report of seven
words is an extractor/counting defect, not a missing word in the written
register. The ordinary 999/702 comparison scope excludes these words, so
this finding alone does not alter those reported selected-position counts.

**Handoff:** count the declared P3 records and retain their suffix identity,
allowing the actual dental/retroflex surface consequences. Do not repair the
written śiṣṭāt spelling to satisfy a literal-string pattern. No corrected
certificate has been generated here.

## CR4. Candidate gates and the unchanged earlier adapter issue

The new T157 adjudication path checks the actual observed pair against the
declared historical pair **before** accepting its adjudication metadata.
That is stronger than the earlier T155 overwrite-before-comparison issue.
The module's PASS gate still does not itself demand an empty unresolved map
or exact agreement totals. Its snapshot test separately asserts 999/702/702,
zero unresolved/adjudicated cases and the 54 augment-withheld cells. Those
tests were read, not run.

As in T156, broad `Exception` handling converts any replay failure to
`pada_not_declared`, and tuple-uniformity bookkeeping contains only agreeing
cells. Preserve error identity and require a complete tuple before treating
that flag as a full branch result on future inputs.

The T155 adapter and test remain byte-unchanged from PG50's checked head.
Its expected pin changes because the engine/placement ledger changed; that
is not a repair of the lost ν operation recorded in
[PG50's review](../uduloman_dependency_history/CONCURRENT_REVIEW.md).
T158 reports its scan categories as **309 table rows / 250 ledger /
3,290 neither**, still within the same limited 3,849-ID scan. These are
not missing IDs in the complete 3,983-member written sets.

## CR5. Later T159 snapshot

The final branch check observed **b1059b0bcb4bf157b1f4618599cf29c879e7f602**,
one further commit adding T159. Its full capsule, module, test and expected
hash file were read. The PG24/26/27 input packets were not all freshly
audited in this late review, so no full source-to-adapter certification is
claimed for them.

T159 reports **1,457 selected positions, 953 replayed/agreeing, 504 outside
the declared table, and 69 option cells**. Its expected string is
`ea798cd7bd8be047db6dd937c4a718f39bbe5f9c464184a8a47a35b88dcc158c`.
The module separates several class-specific root identities and reads PG26's
explicit first-person column when expanding its constructors. Its PASS gate
again differs from the stronger exact-total snapshot test; neither was run.

The T158 table, T157 adapter, T155 adapter and the four earlier expected-hash
files above are byte-unchanged in this additional commit. Thus it does not
repair CR2/CR3's source/counting qualifications or the earlier T155 ν finding.
All T159 results remain attributed reports, with zero execution credit for
PG51. This is the last observed companion snapshot for publication.

This packet changes no companion code, written PG23 form, old certificate
or engine. The review is a repository handoff only; no collaborator message
was sent. Grammar tests, generators, certificate replay and operator/navigation
suites remain deferred.
