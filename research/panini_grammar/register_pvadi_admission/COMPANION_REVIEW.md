# PG60 — T164 admission and pvādi implementation handoff

Author: Monty. 5 November 2026.

The companion ref was checked and remains
**d5194a743663c6f1afd63ed848a6d6e33d48cf91**, T164. There are no new
commits since PG59's cutoff. Reuse [that capsule review](../tanadi_guna_ownership/COMPANION_REVIEW.md)
and its exact pins; this stage reads only the root declarations, root-key
resolution, PU_LIST and 7.3.80 guard relevant to the new source claims.
No lanes, certificates, generators or replay were executed or re-audited.

## Register qualification

Nine of T164's newly declared class-5 entries need the source qualification
in H01/H02: pṛ5, spṛ5, smṛ5, ah5, dagh5, cam5, ri5, dāś5 and dṛ5.
The first three lack a Vedic tag in the modern rows but have the explicit
traditional report. The other six have both the tail-scope evidence and
the modern Vedic tag. The displayed declaration tuples carry teaching
form, pada, gaṇa and code; they do not themselves supply a classical
register license. This does not make agreement in a declared software
lane a false result; it limits the grammatical admission that can be
inferred from that agreement. Preserve kṣi's exact, source-qualified
classical exception instead of deleting every Vedic-tagged row.

## Endpoint and vowel-type qualification

The current `PU_LIST` and 7.3.80 guard implement a selected finite
membership set; vrī/bhrī/kṣī/heṭh are outside it. Its final-vowel guard
also accepts only ū/ṝ/ī. PG60's broad profile therefore needs **both**
a policy-qualified membership path and the 1.1.48 ec short substitution
for heṭh. Expanding the set alone cannot derive hiṭhṇāti through that
guard. Root shortness and the later śnā ī/allopa conditions must remain
separately addressed. H07's explicit jñā exception must survive any
through-end interpretation.

The narrow implementation remains a valid selected profile. A broad
profile must be labelled and compared against its own written branch;
it must not quietly replace the old oracle or inflate the position count.

## The distinct śṝñ admission can now be implemented

T164's `śṝ9` tuple is **śṝ / P / 9 / 09.0021**. Its capsule separately
lists śṝñ among entries with remaining present-system residue. H06
provides the independent Kṣīrataraṅgiṇī word pair and full written
P/A derivation for **09.0015 / 1090015**, whose modern row expressly
describes the alternate traditional entry. The source mapping uses
teaching form, meaning, gaṇa, pada and the variant note; printed entry
17 is not a modern numeric-code match.

Declare a distinct key for that U entry and retain ñ through marker
metadata. Do not reuse `śṝ9`, assign an A ending to 09.0021, or join
entries after stripping their teaching markers. The independent scan
resolves PG12's written refusal; it does not claim a runtime pass or a
complete perfect/aorist paradigm. PG59's tanādi guard and replay-pair
obligations remain inherited and unmodified.

## Concrete next implementation steps

1. Add an evidence-addressed register policy before morphology; keep
   withheld, unresolved and positively licensed requests distinguishable.
2. Add NARROW_PLII / BROAD_GANA_END profiles with exact entry membership,
   śit scope and the explicit jā exception. Preserve heṭh's teaching form
   and use the ec short substitution only after its license succeeds.
3. Add the separately keyed KSHIRA_SHRNJ_1090015 profile and its 18 cells.
   Keep the original P-only entry and historical PG12 refusal untouched.
4. Compare the actual source-qualified inputs and observed word pair
   before an option adjudication. Count the 36 broad readings as branches
   at existing positions, and only 18 positions as newly admitted.
5. Perform changed-scope integration checks on Python 3.12 when Claude
   resumes execution. This packet ran document/source checks only.

Next written development: svādi hi's reduplication/san restrictions and
the residue-bearing ṛdh/ciri/jiri/ṛkṣi profiles, with the register gate
constructed here. The new written admission is not a claim that all
those perfects and derived stems have been completed. No external
message was sent and no runtime or certificate was modified.
