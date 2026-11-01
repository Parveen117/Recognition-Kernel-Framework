# PG15 — Primary-source decisions and evidence boundaries

Author: Monty. 2 November 2026.

Primary edition: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data),
commit `5744762f010d677cfb43f347a42d02796cf615d6`. The local reading uses
the numbered text, Kāśikā, Siddhāntakaumudī, Bālamanoramā,
Tattvabodhinī, selected Mahābhāṣya, and Dhātupāṭha records. The retained
passages in [SOURCE_EXCERPTS.json](SOURCE_EXCERPTS.json) keep the published
strings, including problematic readings. [SOURCE_PINS.json](SOURCE_PINS.json)
identifies the edition and predecessor bytes; it is provenance, not a
grammar execution report.

## S1. The double-karman policy is a commentary passage, not 7.1.69

The publisher indexes a substantial end-of-bhāva/karma discussion in its
[7.1.69 page](https://ashtadhyayi.com/sutraani/7/1/69). The sūtra itself,
*vibhāṣā ciṇṇamuloḥ*, concerns its inherited num context. After discussing
that rule, Siddhāntakaumudī turns to **dvikarmakāṇāṃ tu** and states the
principal/secondary karman policy used in K3/K6.

Bālamanoramā expressly identifies that latter verse as a summary of the
vārttika/Mahābhāṣya discussion at **1.4.51**, and its final words mark
the close of the bhāva/karma procedure. Accordingly:

* The raw database key for these excerpts is 71069.
* Their intellectual source is the named commentary's role-selection
  discussion and its stated relation to 1.4.51.
* PG15 does **not** label the selector as “Pāṇini 7.1.69's passive rule,”
  or make the num rule's ciṇ/ṇamul guard apply to present yak.

This is a source-attribution decision with grammatical consequences.
Treating every paragraph stored under one number as that sūtra's literal
guard would exclude the present examples the commentary is discussing.

## S2. Two textual variants are preserved and adjudicated locally

| Published location | Reading | PG15 decision |
|---|---|---|
| Siddhāntakaumudī 71069 | `बोध्यते माणवकं धर्मः । माणवके धर्ममिति वा ।` | Preserve the locative-looking `माणवके` in the extract; do not silently repair the source file. |
| Bālamanoramā 71069, explanation of the same alternative | `माणवको धर्ममिति वेति` and an explanation that either learner or content is expressed | Adopt the nominative learner in the alternative clause. This agrees with its own explanation of tiṅ-expression and case. |
| Siddhāntakaumudī 71069, duration/bhāva comparison | `मासो मासं वा आस्यते देवदत्तेन` | Temporal/spatial extensions are outside K1. Preserve the text without treating both printed forms as established here. |
| Bālamanoramā on that comparison | `मास इति सप्तमी । मासमिति त्वपपाठः ।` | Record its explicit correction to a locative in that **basic bhāva** contrast. Do not apply that correction to the separate causative example. |

The separate causal *māsam āsyate māṇavakaḥ* has an unexpressed temporal
karman in that commentary's analysis, and its accusative is explicitly
explained. Conflating the two discussions would manufacture a contradiction.
Neither temporal construction is smuggled into the narrower bhū/sthā
domain merely because it appears on the same page.

## S3. The selected commentary reading and the Mahābhāṣya dialogue

Mahābhāṣya at 1.4.51 discusses kathita/akathita and competing descriptions,
including a passage introduced by *apara āha*. It contains the cow/milk,
goat/destination and causal gam examples. The retained excerpt is evidence
of this discussion, not a license to concatenate every voice as if it
were one list of unconditional prescriptions.

K3 adopts the explicit Siddhāntakaumudī/Bālamanoramā presentation:

* Basic duh-group frames express their secondary karman; basic nī/hṛ/kṛṣ/vah
  frames express the principal karman.
* Causal cognition/ingestion/word-object frames permit either karman.
* The other stated causative frames express the causee-karman.

K2 independently determines whether that causee is karman at all. Kāśikā
1.4.52 supplies nī's exception, the cognition examples, the base-intransitive
cases, and a cooking contrast. Kāśikā 1.4.53 supplies optional causee
karman for hṛ/kṛ. Therefore K3 cannot be used as an independent rule
turning a retained kartṛ into karman. The hṛ/kṛ construction has precisely
the dependent branches proved in K5, within this adopted reading.

The word-object class in the general commentary is outside the twelve
causative roots. The list of basic duh-group roots and its full exceptional
case system is also not declared complete by the five comparison examples.

## S4. Ṇic-lopa and what survives it

Kāśikā 6.4.51 states the aniṭ ārdhadhātuka guard and expressly gives
*kāryate/hāryate*. Its *kārayitā/hārayitā* contrast proves that niC loss
is not an unconditional causative-to-passive string operation.
Yak's ārdhadhātuka status is obtained from 3.4.113–114; its y-initial
form fails the val condition of 7.2.35.

Kāśikā 1.1.63 uses *kāryate/hāryate* again as its non-lumat comparison.
Thus ordinary 6.4.51 lopa must remain distinct from luk/ślu/lup. At the
same time Kāśikā 1.1.62 explicitly limits what follows from
pratyayalakṣaṇa: a phoneme-dependent ayādi operation is not automatically
restored merely because an affix was erased.

L4 consequently uses an ordered pre-yak formation and a narrowly stated
1.1.57 visibility argument for the alternate local nī schedule. The
1.1.58 exception list is retained too. This is neither a blanket
“all deleted sounds remain visible” policy nor an erasure of the affix's
historical effects. The scope of 6.4.22 and possible dependencies in
other suffix environments still require their own argument.

6.4.51's commentary calls it an exception to several operations. L2
does not infer that every listed competitor has a true guard before yak.
The local lengthening question is separated from root changes caused
earlier by ṇic. This avoids both *kārīyate* and the mistaken reversion
of causal kār to basic kṛ.

## S5. The two doubled-y paths

The pre-yak nī and pā constituents are inherited from the separately
source-pinned PG13 construction. Their first y occurrences have different
owners. Their following y is yak, which is outside val and therefore
does not meet 6.1.66. Kāśikā's *ūyyate/knūyyate* examples witness that
guard boundary; they are not presented as nī/pā examples.

Kāśikā 8.4.64 explains the preceding-hal condition and discusses multiple
y occurrences in *śayyā*. In nāyya/pāyya the first y is preceded by ā;
the second is followed by a. The rule therefore supplies no deletion
of either member of this pair in the displayed state. A two-letter-to-one
cleanup would be an added, unsourced operation.

The optional repetition of 8.4.46–47 is a different question:
Siddhāntakaumudī explicitly says *dve vā* in both rules. The word tables
select their non-doubling branches. If the first y is duplicated by
8.4.47, a new triple-y state admits 8.4.64's middle-y lopa; its target
again has two y occurrences. L5 records this extension rather than
asserting that a two-y word is the only possible phonetic realization.

Exact *nāyyate/pāyyate* word quotations were not located in the selected
primary passages during this reading. PG15 claims the displayed owned
rule derivations and their explicitly stated premises, not a newly found
standalone witness for every cell. A search result for the distinct root
*pay* is not evidence for drinking pā and is not included in the source
pins or the argument.

## S6. Lexical identity, especially the source's kṛṣ

The twelve causal inputs keep PG13's exact lexical IDs. Drinking pā
1011074 is not protecting pā 1020051; the yuk/puk distinction is inherited
with that identity. Likewise PG13's specified vid/budh meanings, gam mit
license and short-vowel guṇa profiles are not inferred anew from a word
ending in *yate*.

The additional basic comparison uses duh 1020004 and vah 1011159. The
source's unqualified kṛṣ word requires a more careful statement:
the pinned dictionary contains both 1011145 (class 1) and 1060006
(class 6), each with *vilekhane*. The quoted goat-drawing example does
not itself distinguish those IDs. K6 declares the 1060006 binding as
an input choice when applying the generic source frame; it does not
claim the quotation independently proves that unique binding. This
contextual drawing reading is separate from K1's causal furrowing frame.

The basic passive's kit path kṛṣ+ya does not use the competing present
vikaraṇas which distinguish those two gaṇa entries. Its printed word
therefore cannot resolve that lexical ambiguity. An input requiring the
historical quotation's unique gaṇa assignment remains open pending
additional evidence. This does not change the stated conditional
derivation for a supplied lexical/frame choice, and it does not close
PG13's separate exact causal-word gap for 1060006.

## S7. Evidence classes for the new forms

| Evidence class | Examples and exact scope |
|---|---|
| Literal causal-passive word in the relevant passage | kāryate/hāryate at Kāśikā 6.4.51 and 1.1.63; bodhyate and causal gamyate in the adopted double-karman discussion |
| Literal word in a larger commentary procedure | bhāvyate after an explicit ṇi-lopa statement in Siddhāntakaumudī stored under 3.1.66; this is not a claim that the sūtra 3.1.66 itself introduces present yak |
| Literal basic comparison | duhyate, nīyate, hriyate, kṛṣyate and uhyate in the stated double-karman examples, with S6's lexical qualification |
| Inherited formation plus new local rules | All twelve pre-yak constituents from PG13, followed by L2–L6 and the PG14 ending construction |
| Newly constructed full clauses | The plural-learner and plural-servant contrasts in D4/D5; examples of the stated rules, not quotations |
| Written paradigm expansion | D2's 12 × 9 positions; not independent word attestations, implementation comparisons or executed coverage |

The preserved Sūtrapāṭha contains 3,983 numbered records. Source-excerpt
counts, theorem numbers, displayed paradigms and finite branch counts
are different measures. This stage changes none of the historical
implemented-rule, root or cell totals, and assigns no whole-grammar
completion percentage.

## S8. Reproducibility boundary

SOURCE_EXCERPTS stores the selected commentary strings verbatim from the
pinned edition and full selected lexical records. The source pins also
identify PG13 formation records, PG14 theorem text and the current
read-only companion snapshot. This makes each editorial decision and
dependency reviewable without modifying any frozen evidence.

The passage extraction and hashing use file/JSON operations only. They
do not execute the grammar, companion modules, unit suites or certificate
generators. The work record reports those layers separately. Formal
verification and runtime implementation are later work, as requested by
the owner; the mathematical propositions here carry written arguments.
