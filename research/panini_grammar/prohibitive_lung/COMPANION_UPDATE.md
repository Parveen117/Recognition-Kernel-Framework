# PG32 — T151/T152 review and the next implementation contract

Author: Monty. 3 November 2026.

The companion has advanced from PG31's T150 head
`1ffd04e61675c719db9e56f78f245d0aba89f1bd` to T152
`751dddec31988299cdd5003ebffcbf701b1b0126`, through T151
`7a7a419dbe36f122a30ec5a6d4608b785e287539`. The new theorem texts,
selected constructor/driver/table clauses, kernel diff and ledger delta
were read **statically**. No module was imported or executed here.

## C1. Useful progress and its evidence grade

| Packet | New scope | Companion-reported comparison |
|---|---|---|
|T151|eight kṛt affixes over 193 declared roots|1,537/1,544; seven named discrepancies|
|T152|śatṛ and śānac, calling the verbal table|212/212 additional; cumulative 1,749/1,756|

T152 reports 78 kṛt rows and 328 distinct sūtras across the three
tables. Those are attributed finite implementation results, not new
PG32 executions, full alternative sets or whole-grammar completeness.
Its call to the existing verbal table is useful reuse; the seven earlier
discrepancies, feminine formation and participle declension remain open.

Static byte comparison confirms that the verbal table, nominal table
and ISA module are unchanged since T150. The kernel and its metadata
have changed to include the kṛt table. Consequently PG31's specific
ISA-owner/ṭit-kit findings are not silently treated as repaired.

The ledger has 1,005 entries: compiled 10, meta 169, hand-coded 434,
cited 390 and misnumbered 2. Its **613 operational-labelled IDs** are
25 more than T150; 21 are new to PG31's combined union. The remaining
four were already present in the independent written stream. PG32's
explicit apṛkta definition and ordinary-past scope add 1.2.41 and
3.2.84 beyond that union, giving **731** bounded-rule IDs. No kṛt
result is added to the finite-word position total.

## C2. Specific interfaces still needed

1. `_lat_anga` consumes `TIN.conjugate(...)[0]`, strips a suffix from
   the resulting word and assigns a new root segment. The donor's
   structured owners, query views and full derivation path are not
   transported by that return value. T152 explicitly labels this
   ending-readback method as an implementation reading. Before broader
   reuse, expose a source-labelled aṅga state and prove which guards
   survive the call; final-word agreement alone does not establish that.
2. K's constructor assigns P for śatṛ and A for śānac. The lane
   restricts its chosen inputs, but the constructor/derive interface does
   not itself supply the source-qualified semantic/pada admission gate.
   Preserve that boundary before generalizing the callable API.
3. `build_certificate` checks a nonempty lane and row load-bearing;
   its PASS condition does not itself demand agreement on every lane
   cell. `t2_load_bearing` also treats an exception as changed behaviour.
   Keep reported word agreement, valid alternative outputs and error
   counts separate when replay is resumed. No new failure is claimed here.
4. Kernel claim-boundary prose still says kṛt beyond T151's eight
   affixes is unclaimed, although T152 adds two. Reconcile that summary
   with the current narrower actual exclusions. Preserve historical pins.

## C3. PG32's concrete complementary queue

Continue the semantic/owner adapter work from PG30/31, now with this
complete additional contract:

| Interface | Required behaviour |
|---|---|
|Request admission|distinguish ordinary L+, māṅ L− and māṅ+sma J−; retain L− with sma|
|Initial augment|6.4.74 rejects only aṭ/āṭ candidates; no first-letter deletion of the final word|
|Augment ownership|retain sic-iṭ, tiṅ-īṭ, original first-singular iṭ ending and root-final vuk as different owners|
|Sic history|whole luk, realized s and later sic-s deletion remain different states; 109/110 and 96 have different source guards|
|A second plural|implement the positive 8.3.79 branch relation for īh, and carry the selected dh-policy parameter|
|Laṅ continuation|recompute śap/u, jha and dual predicates; do not copy sic's A3pl or dh/ḍh behaviour|

The current verbal table already has useful 2.4.77, 3.4.109/110,
7.3.96, 8.2.25/27/28 and 8.3.78 rows. It has no literal 6.4.74
or 8.3.79 `add` row in the inspected file. The latter is mentioned
in a note while one branch is selected. This is a finding about that
table, not an absence claim about every historical helper in the repo.

[P](PARADIGMS.md) supplies 26 new complete profiles, 234 positions
and 236 adopted readings. Reuse the 36 PG30 positions instead of
counting them twice. Do not replay certificates while the owner's
written-first priority remains in force.

The next the construction branch construction is other luṅ families or passive/bhāva
lṛṅ, followed by the remaining temporal and nominal/compound domains.
This file is the handoff; no external message or new agent was dispatched.
