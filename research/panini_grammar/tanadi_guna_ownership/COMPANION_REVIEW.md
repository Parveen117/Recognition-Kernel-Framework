# PG59 — T164 review and the tanādi source-policy handoff

Author: Monty. 5 November 2026.

The observed companion head is
**d5194a743663c6f1afd63ed848a6d6e33d48cf91**, T164, parent T163
`d0c2fa2f2395172bdb2adf44c6b37d711d67bede`. The T164 capsule was
read in full. The review of code was limited to the changed declarations,
relevant guard changes, root/marker initialization and reference-replay
selection/classification. Large rebuilt lanes and certificate contents
were not re-audited. No engine, generator, worker pool, cascade or replay
was run in this stage.

## Reported progress

T164 reports 28 additional svādi/kryādi roots and the closure/declaration
of the earlier vij and sṛ residues, giving **59 lane-only roots** across
the two sweeps. Its verbal suite remains **1,072/1,072**; the added
roots rely on the comparison lanes, not new populated suite cells.
The new declaration guard forbids a key from shadowing ROOTS or NASAL.
The separate vṝ/kṝ P entries consequently use distinct keys from their
existing U entries.

The capsule attributes vij's change to 1.2.2 in the kit test, sṛ's
aorist to 3.1.56 and 7.4.16, and śās's aṅ path to 6.4.34. The selected
diff supports that implementation description; this packet does not
independently prove all those cells. It reports open 7,865/7,865,
ārdhadhātuka 16,237/16,291, karmaṇi 10,008/10,080, ṇic 20,016/20,160,
san 13,320/13,536, kṛt 2,531/2,546 and kṛdanta 72,710/74,400.
The reference replay is reported as 736 replayed / 678 agreeing; the
second written replay as 742/739. The claimed `--jobs` dictionary/digest
invariance remains T164's reported execution result, not a PG59 test.

## Exact tanādi inputs and what the inspected code establishes

At this head the declarations are:

| Lexical entry | Engine key | Teaching input | Pada | Gaṇa |
| --- | --- | --- | --- | --- |
| 08.0006 / 1080006 | tṛṇu8 | tṛṇu~ | U | 8 |
| 08.0007 / 1080007 | ghṛṇu8 | ghṛṇu~ | U | 8 |
| 08.0005 / 1080005 | — | — | — | Undeclared in the reported replay scope |

No second tṛṇu declaration preserving an unmarked root-final u was
found in ROOTS/NASAL/DHATUPATHA_ROOTS. The common initializer calls
`its(up, "dhatu")["remaining"]`. Its parser marks a vowel followed by
`~` as nasal; 1.3.2 marks it and 1.3.9 excludes it from the remainder.
The 3.1.79 row then supplies a separate `s.v = ["u"]`.

Thus the inspected input path does **not** implement the hypothesized
two-way choice of keeping root u versus introducing only affix u. The
reference replay maps by Dhātupāṭha code and then chooses a compatible
pada key; the actual declarations supply the same marked input above.
The historical T163 prose describing tṛṇoti in one place and the
tarṇoti branch in another cannot be explained by two such declarations
at this inspected head. No execution is claimed to resolve the exact
outputs of that historical run.

The current 7.3.86 guard contains `(s.v == ["u"] and s.strong())`,
plus the actual consonant-final/light-upadhā test. On the P 3sg input
it admits root guṇa. On the weak-ending input this u clause fails.
It therefore does not represent the complete G source policy established
by **अर्णुतः** and **तर्णुते**. The u-affix 7.3.84 grade still needs
the separate tiṅ-strength test. Simply removing every strong/weak check
would conflate these two targets and would be an incorrect fix.

## Effective explanation and replay classification

The unchanged `OPTIONS["1080006"]` explains the option as root-final
u versus vikaraṇa u and cites 3.1.79. [E01](DERIVATIONS.md) supplies the
effective written correction: both selected teaching markers undergo
lopa; the affix is present in both branches; the difference is the
source-qualified 7.3.86 root-guṇa policy documented in Kaumudī and
Bālamanoramā. PG12 had already adopted this account. It is not a new
discovery about Pāṇini or a form correction to PG12.

The inspected replay currently assigns an `options` record to a mismatch
when its lexical ID is in OPTIONS. That branch does not first check the
actual observed pair against a finite source-qualified option relation.
Adding the right explanation alone would therefore be insufficient:
the classification must also check lexical identity, sense/admission,
lakāra, pada, slot and membership of both observed readings. A valid
laṭ tṛṇoti/tarṇoti option is not authority for every mismatch of that
lexical ID, and a missing N or G runtime branch remains distinguishable
from an implemented set-valued result.

This is separate from the inherited PG19 metadata-merge concern. The
PG58 vṛj correction, PG57 substitution/śānac boundary and their pending
integration obligations are inherited, not asserted repaired here.

## Reviewable implementation work

1. Preserve the two u occurrence IDs and marker memory. Add a source-policy
   selector N/G with the precise commentarial authority and qualified roots.
2. Evaluate root ṛ grade against u₁ independently of the final tiṅ.
   Evaluate u₁ grade against the tiṅ separately. Keep the actual target and
   nimitta in each trace.
3. Re-evaluate the cluster condition after root grading. Emit three H05
   branches, retaining the blocked G/lopa request, and use ordinary yaṇ
   for H04. Do not transfer śnu's uvaṅ eligibility to tanādi u.
4. Replace the explanatory option label and qualify replay's observed
   pair before classifying it. Record incomplete option enumeration
   separately from agreement with one admissible form.
5. Integrate the 54 existing positions and their 120 written branch
   readings under Python 3.12 when Claude resumes implementation checks.
   No new root/position count should be credited for this restatement.

The next written review is the svādi/kryādi admission boundary exposed
by T164: in particular PG12's source-qualified pṛ/spṛ/smṛ register and
the two śṝ entries/pvādi endpoint. Declaring a row without a Vedic tag
does not settle a conflicting commentary register statement. This packet
does not decide that next question or reject all T164 lane results.

No runtime, lane, frozen packet or certificate was modified. This file
is the handoff; no external message was sent.
