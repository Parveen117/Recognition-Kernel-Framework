# PG58 — T163 review, effective vṛj correction and next obligations

Author: Monty. 4 November 2026.

One companion commit was observed after PG57's cutoff:
**d0c2fa2f2395172bdb2adf44c6b37d711d67bede**, T163, parent
cc7b39bb70aec81579fefa27c8aac5db89480da5. The full T163 capsule,
selected changes to the verbal declarations, modal replay adjudication and
reference replay options were read. The large rebuilt lane files were not
re-audited, and no certificate or cascade script was executed.

## Attributed results and their limit

T163 reports a gaṇa sweep of adādi, juhotyādi, rudhādi and tanādi, with
**29 roots declared from lane agreement and 13 entries retaining residue**.
Its **1,072/1,072** verbal suite is unchanged: the added declarations use
empty suite-cell lists, and their evidence is the seven comparison lanes.
The selected code diff confirms this distinction. The root declarations
are useful implementation progress; they are not 29 newly written proofs
of every lexical sense or all Sanskrit grammar.

The capsule reports modal replay **1,385 positions / 1,382 agreements /
3 adjudicated**, reference replay **734 / 676** with 56 other-option
cases, and kṛt **2,265 / 2,275**. These remain the companion's reported
results. Its current 2.4.54 question still points to T162; PG57 supplies
the written **144 + 8 + 1** source partition, and PG58 adds the alternative
khśā visibility history. Neither packet claims integration into those runs.

## The vṛj correction is accepted with its complete rule condition

[E01](DERIVATIONS.md) replaces PG27's non-num class-2 G = vraj by
**G = varj** and obtains **varjai, varjāvahai, varjāmahai**. T163's
ordinary-loṭ correction is right; the written justification includes
**7.3.86** for the light upadhā, 1.1.2/51 for ar, and 3.4.92 for pit
first-person endings. Its shorthand appeal to 7.3.84 alone does not
specify the consonant-final root's grade operation.

PG27's blessing-loṭ explicitly imports the same ordinary readings, so
the correction has **six existing written positions and three distinct
strings**. No ID, position or extra branch is added. The old parameter
table and derivation remain frozen; the current effective correction is
machine-readable in STATE.json and linked from the current navigation.

The new modal adjudication checks both the observed written-set membership
and actual table output **before** merging in the adjudication metadata.
That ordering is visible in the inspected code and is appropriate for
these records. It does not repair the separately inherited PG19
metadata-merge concern; no change to that other replay is claimed.

## Remaining companion questions

The newly named tṛṇoti/tarṇoti option still needs source adjudication.
The capsule's sweep discussion describes tṛṇoti agreement, while the
reference-replay discussion describes the table's tarṇoti branch; these
claims need exact lexical-key/input reconciliation before they can be
used as one source result. A generator's alternative list does not itself
derive the choice of root-owned उ versus a vikaraṇa. PG58 records this
as the next bounded written task for ṛṇu/tṛṇu/ghṛṇu, without adopting
an unsupported option or changing their historical packets.

The 13 residue entries, bhañj's निष्ठा row, broader gaṇas, the open
kṣiṇoti policy and complete alternative source branches are not closed
by this stage. The new re-pin cascade is reported as tooling, not run here.

## Reviewable implementation handoff

1. Apply PG57's affix-qualified substitution gate, retaining the simple-root
   शानच् control, and add a selected source-policy tag for the khśā path.
2. Keep both root श् and later य् with owner/event addresses. Implement
   the finite consumer-view table and the explicit 3.1.52 exception; do not
   evaluate every rule on one mutable final string.
3. Carry H02's independently owned य् occurrences through the selected
   8.4.64 collapse, and keep the nasal/visarga seams separately addressed.
4. Apply E01 to both I and B first-person bindings for profile 1020022;
   preserve the num and class-7 profiles. Perform the deferred Python 3.12
   integration checks on the changed scope after implementation.

No external message was sent, and no runtime, lane or certificate was
modified. This document is the handoff; the new written claims and actual
document checks are distinct from the companion's reported executions.
