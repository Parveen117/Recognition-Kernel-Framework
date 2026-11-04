# PG55 — Bounded review of companion T161

Author: Monty. 4 November 2026.

Observed companion head: **6469a927b8c75dcd7629a85e8ee84d96e0ebd2be**,
one commit after PG54's fe99fa94b79caeb5a00d218fafd6b78b1c51f488
cutoff. The development branch is shaiva-sources-maheshvara-spanda-pratyabhijna.
The T161 capsule and selected code changes/current guards were read. No
companion module, lane generator, test suite or certificate replay was run.

## Reported results and their scope

T161 reports five added root declarations—sthā, pā, kṛp, iṣ and tṛh—
with missing rule rows; **1,038/1,038** suite cells and **1,217/1,217**
new-root verbal-lane cells agreeing. It separately reports a rebuilt kṛt
lane **1,977/1,985** and kṛdanta-declension lane **56,870/58,036**.
These are attributed companion results, not fresh PG55 execution evidence.
The capsule leaves syand's ktvā and other undeclared-root/policy issues open.
The entire lane payload and every new verbal row were not re-audited here.

## Directly inspected correction

The nominal table's 7.2.112, 7.2.113 and 7.2.109 guards now require
`s.sarva()` as well as the current `id` prefix; the corresponding 7.1.9
exception has the same class qualification. `sarva()` reads the supplied
`sarvanāma` flag. This removes the displayed broad prefix-only condition
that the capsule reports affected iddha/iddhavat forms. It is a useful
implementation example of the class-versus-spelling distinction in PG55.

That inspection establishes the changed guard in the source, not a complete
proof of lexical recognition or a fresh check of every idam cell. Caller
classification and later historical identity remain separate obligations.
The capsule itself says the nominal certificate's own suite contained no
other id-initial stem; its unchanged pin alone would not have exposed this
overreach. The newly rebuilt lane supplied the reported contrasting examples.

## Remaining review limits

The tiṅ suite still checks a set-valued expected form by membership:
one returned form agreeing with one written alternative does not establish
generation of every optional branch. The PG19 adapter still constructs its
adjudicated records by merging `ADJUDICATED` metadata over the observed
disagreement record, then compares the resulting fields with that metadata.
The previously recorded evidence-limit concern therefore remains; adding
sthā/pā declarations does not by itself close it.

PG53/PG54's older review is not replayed or relabelled as an audit of all
T161 changes. Four exact companion files are pinned for this bounded review:
the T161 capsule, nominal module, PG19 adapter and tiṅ module. The latter
was read only for the selected expected-set guard and relevant changed
snippets, not as a complete module audit. No PG55 runtime coverage is claimed.

## Written implementation handoff

Carry the lexical identity evidence, selected class-use policy, internal
compound boundary, complete सुप-लुक witness, consumer-specific नलोप view,
and distinct I/D/Y/F owners into an implementation. Reuse PG49's existing
written continuation without treating Q4's first-member deletion as a repair
of its rejected शीर्षन् branch. Missing name/lineage evidence stays OPEN.
This file is the handoff; no external collaborator message is sent.
