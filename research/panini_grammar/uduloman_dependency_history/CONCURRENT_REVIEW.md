# PG50 — T156 register review and the still-open T155 adapter finding

Author: Monty. 4 November 2026.

The companion advanced one commit from the previously checked
921ee1eb10683d5042e6677a05abbb844037d079 to
**9fc4399b9a785ca830b7c9c507f95fc684a242fd**, adding T156.
This review reads the complete theorem, module, test and expected-hash
files, all six PG20–PG22 files consumed by that module, the imported
comparison module, and the relevant T155/PG19 source files at that
immutable head. File identities are pinned in SOURCE_PINS.json.

**Independently executed here: zero grammar cells, tests, generators and
certificate replays.** File reads, source comparison and byte hashes do
not reproduce the companion certificate.

## CR1. Reported finite scope

|T156's selected register|Positions|Reported replayed / agreeing|Reported outside the table|
|---|---:|---:|---:|
|PG20 basic active āśīrliṅ, 24 rows|216|171 / 171|45|
|PG21 ordinary loṭ and vidhiliṅ, 27 profiles × two moods|486|306 / 306|180|
|PG22 ordinary loṭ and vidhiliṅ, 18 profiles × two moods|324|216 / 216|108|
|Total selected scope|1,026|693 / 693|333|

The 333 positions concern the report's 15 undeclared roots within this
selected scope. They are not a whole-grammar remainder. PG20's causal,
karma/bhāva and blessing-loṭ sectors are separately placed outside;
PG21/PG22 blessing profiles and tātaṅ additions are not silently covered
by their ordinary loṭ words. Position, reading and distinct-word counts
remain different.

T156 reports 85 option-bearing cells, eight branch rows, six uniform
rows and **two mixed kṣiṇ loṭ rows**. Its `to_adjudicate = 0` counts
cellwise disagreements only. Each selected cell may belong to a written
branch while the complete nine-cell tuple belongs to no single fixed
G0/G1 policy. The module separately records precisely this mixed-row
question, and the theorem leaves its source adjudication open.

The expected certificate string is
`158912ce8cd72587710474fc19a4257780c99e8755aba2e4e837ac16c5c2ccbf`.
The newly recorded kernel string is
`f569ee6a8b097c5c4bb97825a1cbab0d1b380660e7af693327797cdea7fc1ee2`.
Neither hash was regenerated here.

## CR2. Constructor and branch fidelity

Direct comparison finds that the ten quoted constructor formulas match
their stated PG20–PG22 written formulas. PG20 uses the supplied R/Z
factors; PG21 supplies Q/J/H and S from its explicit interface tables;
PG22 reads complete loṭ tuples and resolved vidhiliṅ factors. The
adapter keeps PG21's complete branch tuples before taking cellwise unions,
and records whether a uniform branch can explain the compared row.
The imported `PGR.same` only normalizes the two anusvāra spellings ṃ/ṁ;
it does not conceal a dental/retroflex difference.

PG21 MODAL_ENDINGS.md E3 explicitly retains dental first-person n in
its admitted Q domain, including **śṛṇavāni**. Consequently its Qavāni
constructor does not require PG19's ν operation to be appended globally.
PG22's explicit tuples already contain their specified dental/retroflex
readings. This bounded check finds no analogous discarded ν wrapper in
the new selected constructors; it does not certify their entire source
derivations or every future input accepted by the parser.

One metadata inconsistency is visible without execution: T156 says the
table realizes sku's **śnu** branch, giving skunotu, while
`OPTIONS["sku"]` says it realizes **śnā**, giving skunāti. Both are
named alternatives of 3.1.82, but the reported realized branch should
have one consistent label. This review does not choose the engine's
actual output by rerunning it.

## CR3. Candidate-status and error-classification limits

The module's PASS gate checks quoted formulas, a nonzero replay count,
PG20/PG21 row counts, a PG22 count of at least 18, and sūtra-labelled
options. It does not by itself require an empty `to_adjudicate`, the
exact 1,026/693 totals, or uniformity of every branch row. The test file
does assert the reported totals, empty per-packet disagreement maps,
eight branch rows, the two named mixed rows, and the certificate pin.
The candidate status and those stronger snapshot assertions must not be
treated as interchangeable evidence. No failure of the unexecuted tests
is asserted here.

`replay` catches every Exception and returns None; `compare` then counts
that result as `pada_not_declared`. An unexpected engine error would
therefore receive the same classification as a genuine missing-pada case.
Preserving a separate error result would make the stated outside-scope
reasons auditable. Also, `branch_of_each_cell` is populated only for
agreeing cells; a future partially failing row's uniform flag alone would
not prove a complete nine-slot branch match. The reported all-agree
snapshot is narrower than these possible future-input limitations.

## CR4. T155's ν finding remains unresolved

The T155 adapter, its test and expected pin, and the two PG19 written
files are byte-unchanged from 921ee1e. T155's theorem receives only the
forward note about T156; its attribution of kārayāni to the written
register remains. Rereading the actual files confirms the earlier finding:
PG19 ENDING_CONSTRUCTION.md E7 writes **ν(Bāni)**, and PARADIGMS.md
P3 explicitly prints **kārayāṇi**. `pg_written_replay.py` removes the
ν wrapper while extracting endings, then concatenates the unmodified
āni ending in `expand`. T156 adds a separate module; it does not repair
that source-to-adapter loss.

Preserve the bounded ν operation, validate the original observed pair
before fixed adjudication metadata can overwrite it, and keep PG49's
selected-history/proxy qualifications. No corrected T155 replay count
is asserted here. The new T156 results also do not execute PG50's
औडुलोम्या histories, close the kṣiṇ source-policy question, or establish
complete Sanskrit grammar or a universal hallucination guarantee.

This is a written handoff only. No companion code or prior packet was
changed, and the user-deferred grammar tests/replay remain deferred here.
