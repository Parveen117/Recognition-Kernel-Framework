# PG49 — T155 review and the lost ν operation

Author: Monty. 4 November 2026.

Before PG49 publication, the companion branch advanced to
**921ee1eb10683d5042e6677a05abbb844037d079**. It merges the already written
PG19–PG47 lineage at 3c99bc7536a431497a5a090e9ca20ad89b5b457b, then adds
T155. The 31 commits ahead of the prior checked head include the merged
written history; they are not 31 new theorems. PG48/PG49 are not included
in that merge. The development base remains PG48.

The theorem, its complete certificate module and test file, expected-hash
file, and both relevant PG19 written files were read at this immutable head.
All six file identities are in [SOURCE_PINS.json](SOURCE_PINS.json).
No companion code, test or certificate was executed here.

## CR1. Reported scope, not independently reproduced results

|T155 report|Declared finite scope|
|---|---|
|PG19: 976 positions, 542 replayed, 541 agreeing, one called adjudicated|434 not replayed: 234 causative-passive positions and 200 positions mapped to undeclared roots|
|PG47: 29 history records, 11 reached, 12 comparisons reported agreeing|18 records placed outside scope; B07 has two comparisons|
|3,796 rule contracts; 3,849 distinct IDs in the scanned sources|308 table rows, 250 ledger entries, 3,291 in neither category|

The expected-hash file contains
7d580c51ff6a156127d03099f61b09620112754c438c3fb056fd68e0a5551f19.
Reading this string is not reproducing its certificate. The report's
schema-limited 3,849-ID union is not the pair of full 3,983-member written
unions, and “neither” is not a newly uncovered catalogue gap.

## CR2. The written CK02 form is already kārayāṇi

At the checked companion head, PG19 ENDING_CONSTRUCTION.md E7 explicitly
defines the seventh I_P component as **ν(Bāni)** and identifies ν as the
bounded n→ṇ readout. PARADIGMS.md P3 expressly prints the CK02 tuple with
**kārayāṇi**, and also identifies hārayāṇi/karṣayāṇi for CK06/CK20.

The replay adapter's constructor_endings_from_written removes the
\(\nu(\) wrapper while extracting endings. Its expand function then
concatenates the stem and raw endings without applying that operator.
For I_P(kāray), this expansion produces kārayāni itself. T155's
attribution of that dental form to a slip in the written register is
therefore contradicted by the very written files it reads.

**Handoff:** preserve the owned ν operation in constructor expansion and
compare against the explicitly printed CK02 witness. Keep its bounded
conditions; a global n→ṇ replacement would also be wrong. No PG19 written
form was changed here. No corrected agreement count is asserted without
a later authorized replay.

The table's kārayāṇi and the source's kārayāṇi can agree while the
adapter misrepresents the written expectation. This is a concrete reason
to audit representation fidelity before treating every disagreement as
a missing grammatical rule.

## CR3. Candidate-status and history-comparison boundaries

Read-only inspection finds two further limits in the R4 status gate:

1. The all-check iterates over adjudicated records only; it does not require
   the separate to_adjudicate dictionary to be empty. The test file does
   assert emptiness for the pinned snapshot, but the module's PASS gate alone
   does not guarantee that property for a future changed input.
2. Each adjudicated record is built by merging the observed result and then
   the fixed ADJUDICATED entry. The fixed written/ours values overwrite the
   observed pair before the later equality comparison. That comparison cannot
   independently establish equality of the original observed pair.

A repair should validate the unmodified observed pair and decide explicitly
what unresolved disagreements mean for candidate status. This is a
read-only finding, not a code change or a claim that the published tests
were rerun and failed.

R5 extracts cited step IDs from PG47, but the actual comparison is filtered
through a manually specified TARGETS fires/blocked map. It checks selected
firings, absence of selected blocked rules, a subsequence relation and a
selected witness; it does not execute every written premise and event.
In particular **B06 uses daduḥ as a proxy while the code itself says the
written witness is jagle**, whose root is outside its mapping. Thus “12
comparisons agree” must not become “12 original same-word histories
completely verified.” The theorem's blanket witness-equality wording needs
that qualification.

R6 checks scanned IDs and quoted sūtra text, not the semantic content of
every contract. Its implementation skips rows without an id and compares
text only when the sutra field is nonempty; zero mismatch lists alone do
not establish strict record-schema completeness. Its historical scan does not consume the policy-labelled
PG49 records as a new executable grammar test.

## CR4. Next implementation handoff and preserved boundaries

Repair ν-preserving expansion, preserve the observed adjudication pair,
make unresolved-status handling explicit, and label the B06 proxy and
selected-rule comparison accurately. These repository notes are the
handoff; no collaborator message was sent.

The inherited T154 kṣiṇoti/kṣeṇoti adjudication remains separate. PG49's
main written work remains the two शीर्ष histories and six controls.
Neither this review nor the companion's reported results establish their
runtime execution, general semantic correctness, complete Sanskrit grammar,
or a universal hallucination guarantee. Tests/replay remain deferred here.
