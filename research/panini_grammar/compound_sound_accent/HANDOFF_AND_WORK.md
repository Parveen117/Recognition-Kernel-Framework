# PG38 — Work record and implementation handoff

Author: Monty. 4 November 2026.

## W1. Request, scope and result

Continue the user's written Panini grammar development in approximately
300-new-ID batches, keeping grammar tests/replay deferred. The coherent
352-contract range closes 5.4, covers numbered 6.1 contracts and finishes
the early compound/gati accent group through 6.2.54.

|Quantity|Before|New credit|After|
|---|---:|---:|---:|
|Combined distinct bounded IDs|1,658|302|1,960|
|Independent written IDs|1,318|324|1,642|
|Finite written positions|11,552|0|11,552|

Fifty IDs already occur in the combined union; 28 already occur in the
independent written set. [Coverage](COVERAGE.json) enumerates both overlaps
and both exact new-ID sets. Neither source controls nor dependent clauses
earn extra IDs. All six tables have one six-cell row per counted ID:
**75 + 63 + 48 + 47 + 65 + 54 = 352**.

## W2. Verification and limits

All operative Kāśikā fields were read. Targeted Nyāsa/Kaumudī/Vasu
comparisons clarified final-segment substitution, 6.1.93's आ + ओतः,
genitive ङस्, original त्-initial suffixes and क्विन्'s व् residue.
[Source review](SOURCE_REVIEW.md) records damaged readings, variants,
adopted policy and open clauses rather than overwriting the source text.

Document checks verify exact ID ranges, unique six-cell rows, register-to-
authored-line equality, both set unions, 1,095 literal primary fields,
source/file identities, JSON syntax, local links and Git whitespace.
The final packet has **17 files, 28 pinned file identities and 67 checked
local links**, including the two navigation updates in the pin/link counts.
These are provenance/document checks, not execution of the grammar.
The [predecessor review](PREDECESSOR_REVIEW.md) separately checks all
321 PG37 rows, 988 literal fields, 29 pinned file identities and eight
semantic boundaries. It makes no exhaustive soundness claim.

No grammar test suite, independent generator, certificate replay,
navigation suite or operator suite was run. No complete surface realization
or new paradigm was manufactured from a source witness. Runtime code,
frozen predecessor packets and the canonical shared operator engine remain
unchanged. Native continuation is an instance of the inherited construction,
with finite-event typed zero compatibility and the same claim boundary.

## W3. Companion state

The companion branch `shaiva-sources-maheshvara-spanda-pratyabhijna`
remains at
[`751dddec31988299cdd5003ebffcbf701b1b0126`](https://github.com/Parveen117/Recognition-Kernel-Framework/commit/751dddec31988299cdd5003ebffcbf701b1b0126)
(T152), unchanged when checked for this continuation. Reuse
[PG32's static review](../prohibitive_lung/COMPANION_UPDATE.md); its prior
reported test results are not newly executed evidence. This file supplies
the handoff for implementation review.

## W4. Required implementation properties

1. Preserve upadeśa, markers, relation/meaning evidence, compound tree,
   source policy and T/F/? decisions. Unknowns must remain Open.
2. Keep समासान्त inside the actual compound and distinguish inner
   taddhita लुक् from ordinary सुप् deletion. Resolve residual कप् only
   after relevant earlier candidates and prohibitions are known.
3. Address final-segment substitutes, root augments, vowel-owned तुक् and
   अभक्त सुट् separately. Different marker-bearing suffixes are not
   interchangeable even when their final visible अ is identical.
4. Copy qualified one-vowel units, not character prefixes. Distinguish
   अभ्यास from अभ्यस्त and designation-only from copying events.
5. Retain causal sound history, including original/derived एच् and the
   suffix that caused it. Optional इट् can change other rule admission.
6. A joint replacement has two input addresses and one result. Preserve
   constituent membership and observer-specific earlier visibility without
   deleting the actual result or promoting every old letter to active.
7. Treat grammatical पद, ऋक्पाद, मन्त्र, छन्दस् and editorial इति as
   different gates. Accent cannot be reconstructed from plain spelling.
8. Keep accent claims with their owner and priority dependencies. A blocked
   udātta route can leave another svarita route. First-member preservation
   is not always initial-syllable accent.
9. Distinguish optional placements, source-policy alternatives and two
   simultaneous accents. Apply 6.1.158 only after respecting explicit
   multi-accent constructions and qualified priority.
10. Use rule-specific deleted-affix visibility. 6.1.191/198 and 197/199
    provide direct counterexamples to a single universal policy.
11. Treat the JSON as reviewable natural-language contracts. Runtime
    predicates, complete lexical normalization, later phonology and
    independent validation remain separate implementation obligations.

## W5. Next frontier

Continue sequentially at **6.2.55**, then the remaining compound-accent
and 6.3/6.4 families as source dependencies permit. Unclosed 4.1 families,
earlier source-policy questions, complete gaṇa normalization, finite karma
luṅ outside prior third-singular work, and ksa/aṅ/caṅ obligations remain
open. Full word realization and runtime integration must be separately
constructed and verified; the distinct-ID count does not establish them.
