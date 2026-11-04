# PG47 — Addressed instruction histories

Author: Monty. 4 November 2026.

These seven written histories instantiate PG47's common interface. They start
from supplied grammatical states on the full operator/history carrier, with
typed cuts, cut field, derived iota, pairing, dagger and ordered history
retained. Token addresses below are local names, not offsets in a rendered
Unicode string. The native continuation gives their typed zero-reading;
the tables here specify the addressed grammatical events it carries.

`APPLIED`, `BLOCKED` and `OPEN` always qualify the named instruction or query.
They are not verdicts on an entire Sanskrit sentence. A blocked proposal adds
an explanatory decision record, not a token mutation. An Open proposal records
its missing evidence and cannot fall through to a default replacement.
Unperformed alternatives remain in the decision record without becoming
events in the chosen derivation. Full source decisions are in
[SOURCE_NOTES_A.md](SOURCE_NOTES_A.md).

## A01 — Whole-root replacement retains the genitive relation

**Sources:** 1.1.49, 1.1.52, 1.1.55, 2.4.52; controls 6.4.89 and the
auxiliary exclusion reported under 2.4.52.

**Given frame.** Root token `r` has lexical identity अस् and active segments
अ-स्. A following suffix token `s` has an admitted आर्धधातुक role. The
request belongs to ordinary root replacement under 2.4.52; `r` is known not
to be the protected अस् auxiliary of the आम् construction. Affix admission,
voice and lexical identity are supplied facts, not inferred from a final word.

|Step|Instruction and address|Retained result|
|---|---|---|
|1|Resolve अस्तेः in 2.4.52 through 1.1.49's otherwise undetermined relation|`original = r`; the instruction prescribes a substitute, not a following extra root|
|2|License भू from 2.4.52 after its domain and exclusion are resolved|The substitute is admitted before extent is selected|
|3|Apply 1.1.55 to the अनेकाल् payload भ्-ऊ|Extent is the whole addressed अस् token; the final-sound default 1.1.52 does not select only स्|
|4|Replace `r.active` by भू; append the owned replacement event|`r.origin = अस्`, the source clause and `s` remain available; no second भू root is appended|

**Result:** `APPLIED` for the whole-root event. The source's भविता,
भवितुम् and भवितव्यम् are downstream witnesses. Their suffix realization,
iṭ, grading, endings and accent are separate obligations; the current event
does not claim all three derivations.

**Controls.** If `r` is instead the अस् auxiliary in the supplied ईहामास
history, 2.4.52's stated exclusion makes this replacement `BLOCKED`. If its
auxiliary status is unknown, the same proposal is `OPEN` pending that fact.
The bare visible string अस् cannot decide the issue.

Nyāsa's 6.4.89 control also prevents a parser error: in उपधाया गोहः,
the root-to-penultimate relation is already fixed as part–whole. 1.1.49
does not overwrite that relation and then replace the whole root or its final
ह्. The prescribed target remains the expressly addressed उपधा. That
control closes the relation query, not all of 6.4.89's realization.

## A02 — A single surviving इ can have two different extents

**Sources:** 1.1.52, 1.1.55, 1.2.50, 7.1.20; marker controls 1.3.8–9.

**Given frames.** In the first frame, `a` is a neuter-base nominal plural
जस् token with its exact case/number identity. In the second, `b` is the
गोणी constituent in the supplied “bought for five गोणी” formation after
the relevant taddhita-luk history. Both frames retain their own admission;
neither is reconstructed merely from an इ in a finished word.

|Step|जस् frame|गोणी frame|
|---|---|---|
|1|7.1.20 licenses शि at `a`|1.2.50 licenses इ at the addressed गोणी constituent `b`|
|2|The recorded श् marker supplies शित् status although its deletion leaves इ|No शित् or अनेकाल् instruction supplies whole-constituent replacement|
|3|1.1.55 chooses the whole `a` token|1.1.52 chooses only `b`'s final ई segment|
|4|Set `a.active = इ`, retaining origin जस् and the शि prescription|Set that final segment's active value to इ, preserving the preceding गोण् segments|

**Results:** both named extent-and-replacement queries are `APPLIED`, on
different owners. The source witnesses कुण्डानि and पञ्चगोणिः do not
collapse those histories into one operation. Their remaining nominal changes,
case endings and accent are downstream obligations.

**Blocked proposals.** Replacing the entire गोणी constituent by इ is
`BLOCKED` by the resolved final-segment extent. Replacing only the last sound
of जस् under the शि instruction is `BLOCKED` by its whole-affix extent.
7.1.20's companion शस् is the nominal ending; the adverbial शस् of
कुण्डशः does not acquire the prescription through spelling equality.

Nyāsa 1.1.55 explicitly excludes marker-created अनेकाल् counting. The
शित् condition is therefore retained as its own reason for whole replacement;
the analysis does not count the deleted श् as an ordinary output sound.
If the marker/origin record is unavailable, the extent query is `OPEN`.

## A03 — आनङ् changes the last sound of its own first member

**Sources:** 1.1.53, 1.1.55, 6.3.25; downstream control 8.2.7.

**Given frame.** The admitted द्वन्द्व has first-member token `m1 = होतृ`
and second-member token `m2 = पोतृ`, with the required विद्यायोनिसम्बन्ध
domain supplied. A licensed आनङ् substitute has its retained ङित् identity
and the source-explained आन् payload. The nasal is part of the replacement
history; it is not silently discarded together with the ङ् marker.

1. Address the first member under 6.3.25; do not target `m2` or the entire
   compound merely because each contains ऋ.
2. Resolve the ङित् extent instruction in 1.1.53. In this domain it selects
   the last ऋ of `m1`, despite the substitute having multiple sounds.
3. Replace that ऋ by आन्. The intermediate first-member value is होतान्,
   with the original होतृ identity and explicit ऋ-to-आन् event retained.
4. Keep the न् until its own deletion instruction is admitted. The source
   explains that its presence prevents the unwanted र् accompaniment.
   A later 8.2.7 event requires the appropriate पद/प्रातिपदिक state; it
   cannot be merged into the replacement event without those prerequisites.

**Result:** `APPLIED` for the final-segment replacement. The source's
होतापोतारौ is a downstream witness, with first-member n-lopa and
second-member dual/grade realization still named obligations in this trace.
The root of those later operations remains distinct from the extent decision.

**Controls.** A proposal to replace all of होतृ or to replace पोतृ under
this event is `BLOCKED`. Missing compound relation or marker provenance makes
the extent-and-substitution request `OPEN`.

This is not a global “ङित् always defeats 1.1.55” policy. Kāśikā and
Nyāsa 1.1.53 separately explain whole replacement by तातङ् because its
ङ् has another relevant function and the competing rules have different
available domains. That different interaction requires its own admitted record.

## A04 — टि is a terminal span; उपधा is one sound

**Sources:** 1.1.64–65, 3.4.79; single-vowel control 1.1.21.

**Given frame.** Expression token `x = अग्निचित्` has an admitted sound
segmentation and an explicitly delimited owner. Number the last three sounds
locally as `c = च्`, `v = इ`, `t = त्`. These are grammatical sounds,
not three adjacent code points. The earlier इ in अग्नि has another address.

|Query|Address calculation|Result|
|---|---|---|
|टि under 1.1.64|Find the last vowel of `x`, then include it and every following sound of this owner|The ordered span `[v,t]`, अर्थात् इत्|
|उपधा under 1.1.65|Find the final sound of `x`, then its immediately preceding sound|The singleton address `v`, अर्थात् इ|
|Earlier-vowel proposal|Use the इ in अग्नि as though it were the last vowel|`BLOCKED`; the requested last-vowel property is false|
|Whole-cluster उपधा proposal|Use `[c,v]` or the whole final इत् span|`BLOCKED`; the designation belongs to one preceding sound|

**Result:** `APPLIED` for the two designation queries. No sound is replaced
by merely computing either address. The shared initial `v` does not make
the two extents interchangeable.

For a separate supplied A-ending token आताम्, 1.1.64 selects its final
आम् span. Under a resolved टित्-lakāra and tiṅ-ending history, 3.4.79
can replace that span by ए, retaining the initial आत् material. The source
gives पचेते as the later word witness. This does not authorize the same
event for a participial आत्मनेपद designation: 3.4.79 expressly keeps the
tiṅ domain and excludes पचमान/यजमान. Stem/ending junction and full
accent realization remain downstream work.

If sound segmentation or the token boundary is missing, both address queries
are `OPEN`; a visual search for the last vowel sign does not fill the gap.
Nyāsa's single-vowel discussion uses 1.1.21, not an invented second vowel.

## A05 — A locative trigger selects the immediately preceding इक्

**Sources:** 1.1.49–50, 1.1.66, 6.1.77.

**Given frame.** The admitted close-junction state is दधि + उदकम्.
The final इ of the left token is `l`; the initial उ of the right token is
`r`. Their adjacency and the ordinary, non-pluta scope are supplied. Both
sounds belong to इक्, so direction is material to the instruction.

|Step|Resolved instruction|Owned result|
|---|---|---|
|1|इकः gives the substitution target class; अचि gives the following environment|The two case relations have different roles|
|2|1.1.66 chooses an eligible sound immediately before the locative environment|`target = l`; `trigger = r`|
|3|6.1.77 admits the यण् family; source-qualified likeness selects य् for the supplied इ|The selector narrows an admitted family; it creates no replacement prescription itself|
|4|Replace `l` by य्, retaining its इ origin|The उ at `r` is unchanged; the local unaccented readout is दध्युदकम्|

**Result:** `APPLIED` for this junction event, matching Kāśikā's 1.1.66
witness. A proposal to change the following उ in this same instruction is
`BLOCKED`: it is the environment, not the preceding target. Other word-level
and accent obligations are not discharged by the junction result.

**Nonadjacency control.** In the source's अग्निचिदत्र witness, the final
इ of the first constituent is separated from अत्र's अ by the intervening
consonant. Its voiced/unvoiced realization does not remove that intervening
address. The attempted इ-to-य् event across it is `BLOCKED`; 1.1.66
cannot skip the consonant. No claim about other legal sound changes follows.

Nyāsa explicitly extends the adjacency condition beyond cases where both
sides create an initial ambiguity. Hence a uniquely recognizable earlier
इ still cannot bypass the intervening sound. Missing boundary or adjacency
evidence yields `OPEN`, not an assumed immediate junction.

## A06 — An ablative selects the following token, then its initial sound

**Sources:** 1.1.54, 1.1.67, 7.2.82–83; background 2.4.72,
3.2.123–124 and the source's आस्/शानच् analysis.

**Given frame.** Root token `r = आस्` means sitting; it is not the अस्
token in A01. The following admitted participial token `s` originates in
शानच् and has the current आन payload. Its A, laṭ and adādi/śap-luk
history is supplied as in Nyāsa 1.1.54. Lexical, participial and register
admission precede this local operation.

1. Read आसः in 7.2.83 as the ablative environment and retain the inherited
   आन target. Under 1.1.67 the candidate is the following `s`, not `r`.
2. Preserve the source's case-relation adjustment: 7.2.83 makes the
   following आन the replacement bearer. Nyāsa distinguishes this setting
   from 7.2.82; it is not a universal rule that either case always wins.
3. Apply 1.1.54 to the prescribed operation on that following bearer.
   The target is only `s`'s initial आ, not the final अ of its आ-न्-अ
   payload under the ordinary final-sound default.
4. Replace this आ by ई, leaving न्-अ in `s` and leaving आस् at `r`.
   The local stem readout is आसीन, with its two owners still distinct.

**Result:** `APPLIED` for the initial-affix substitution. The source
आसीनो यजते is a downstream witness. The participle's full nominal
inflection, external junction and accent remain separately required.

**Controls.** Replacing the root आस्, replacing only the suffix's final अ,
or replacing all of आन by ई is `BLOCKED` by the resolved address/extent.
If the token is known only by the visible letters आन without its licensed
participial history, this request is `OPEN` pending that history.

Direction does not impose one universal operation extent. For the separate
8.1.28 instruction, 1.1.67 targets the following tiṅ-word after an अतिङ्
word, while 8.1.18 supplies whole-word anudātta scope and the non-pāda-initial
condition. The inherited सर्वम् authority prevents misusing the initial-sound
default as an instruction to accent only the first sound. A positive accent
result also requires the remaining local exceptions to be resolved; this
paragraph does not run that accent derivation.

## A07 — Similarity narrows a licensed substitute family

**Sources:** 1.1.50, 7.3.52.

**Given frame.** A root-final च् token `c` in an admitted पच् + घञ्
history is addressed by 7.3.52, with the following affix's घित् identity
retained. Its prescribed replacement family is कवर्ग. The input supplies
the source's phonetic classification of च् as अघोष and अल्पप्राण,
together with the corresponding features of the candidate sounds.

1. Confirm 7.3.52 admission and its exact root-final target. Without this
   prescription there is no replacement family for 1.1.50 to select from.
2. Restrict comparison to its licensed कवर्ग candidates. Keep the
   स्थान/गुण criteria named by the source rather than a numeric string metric.
3. The source's अघोष/अल्पप्राण comparison selects क् for च्. Commit that
   replacement at `c`; retain the पच् origin and the still-owned घञ् token.
4. Record पाकः as the commentary's later witness, not as the output of
   this one consonant operation. Root-vowel grade, suffix realization,
   nominal ending and accent remain named obligations.

**Result:** `APPLIED` for the selected consonant replacement. The prescribed
family was present before similarity selection, and its ownership is unchanged.

**Controls.** A bare दधि or मधु with no independently licensed replacement
prescription cannot receive a substitute merely because 1.1.50 can compare
similar strings: that attempted use is `BLOCKED`. Nyāsa gives this exact
reason against treating 1.1.50 as an independent productive instruction.
If 7.3.52 admission is supplied but the decisive candidate features are
missing, selection is `OPEN`; the first enumerated candidate is not a default.

The other source dimensions remain available in their own domains, including
place priority when likeness dimensions compete. This case does not reduce
all semantic, phonetic or duration comparisons to the च्-to-क् feature test,
and it supplies no termination theorem for an unrestricted grammar.
