# PG11 — Source readings and explicit decisions

Author: Monty. 1 November 2026.

Primary data: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data),
commit `5744762f010d677cfb43f347a42d02796cf615d6`. The Sanskrit text,
inheritance annotations, Dhātupāṭha entries and named commentaries are
retained separately. [SOURCE_PINS.json](SOURCE_PINS.json) hashes eight
external files and 100 historical repository files against baseline
`a59f8f789ed847b27ca1906e470ca426eef6c87a`. PG11 makes no correction to
the external checkout or the older grammar packets.

The source preflight resolves **623 literal anchor references / 571 unique
anchors**. These anchors bind the new rule records, lexical profiles,
literal word cases and source adjudications. The pinned Vidyut form table
is a separate implementation comparison, not the authority for the rule
interpretations below.

## Occurrences, inheritance and case

[RULE_RECORDS.json](RULE_RECORDS.json) contains 43 source-bound definitions.
Their own and inherited terms carry source occurrence identities. In
3.4.84, the first ब्रुवः is ablative and the later ब्रुवः is genitive.
Binding by spelling alone is therefore ambiguous. PG11 requires the
reviewed occurrence and verifies its source case; missing, duplicate,
unassigned or wrongly cased occurrences leave the record unresolved.

Ten commentary-supported scope overlays apply only in this new view:

| Target | Reviewed scope change |
| --- | --- |
| 6.1.6 | Exclude inherited अजादेः and द्वितीयस्य from 6.1.2 and the copying adhikāra from 6.1.1; this rule designates lexical abhyasta |
| 6.3.111 | Exclude the inherited उत्तरपदे restriction for the explicitly licensed noncompound lengthening |
| 6.4.34, 6.4.37 | Exclude stale नलोपः inheritance from 6.4.23 |
| 7.3.54 | Exclude चजोः from 7.3.52; the rule's own h target governs |
| 8.3.13 | Exclude inherited पदस्य for the reviewed internal ḍh deletion |
| 3.4.84 | Supply वा from 3.4.83 for the optional coupled substitution |
| 7.2.78 | Retain the commentary-supported extension to īś from 7.2.77 |

The overlays retain the displaced annotations and their evidence. They
do not silently edit an older source view or infer a universal priority
queue from sūtra numbers.

## Six adjudications

The literal passages and choices are recorded in
[SOURCE_ADJUDICATIONS.json](SOURCE_ADJUDICATIONS.json).

1. **Cakṣ's nonfinal i.** The modern lexical note calls i pronunciation-only
   and denies it status. Bālamanoramā and Tattvabodhinī at 3.4.112 instead
   explicitly use it status for yuc and explain why a nonfinal i does not
   license num. PG11 adopts that traditional reading for this finite path.
   The raw PG4 preprocessing result `c a k ṣ i`, its original sound identity
   and the conflicting modern note remain visible. This is a commentary
   decision, not a claim that the source spelling automatically marked i
   as nasal. The vowel is removed by recorded marker-lopa; 7.1.58 is blocked.
2. **Āh's dental th.** The pinned Kāśikā field at 8.2.35 describes dh,
   conflicting with the sūtra's थः and Bālamanoramā's dental-th reading.
   PG11 uses th and then the independently recorded contact/devoicing
   operations. It retains the contrary field rather than silently repairing
   it. This also keeps the āh branch separate from brū's īṭ path.
3. **Daridrā's weak i.** Siddhāntakaumudī at 6.4.114 prints दरिद्रतः, while
   the rule and Kāśikā support short i and explicitly give दरिद्रितः.
   PG11 uses short i before the admitted weak consonant endings. The
   shorter conflicting spelling is not counted as a matching word witness.
4. **Brū's displaced commentary field.** The Bālamanoramā field at 7.3.93
   contains a sanvat/caṅ discussion rather than the required brū īṭ
   explanation. The decision uses the direct Kāśikā and Siddhāntakaumudī
   passages. The displaced field is preserved and not treated as evidence
   for īṭ.
5. **Mṛj's second-person spelling.** Bālamanoramā at 7.2.114 prints मार्षि.
   The reviewed sequence of 8.2.36 and 8.2.41 yields मार्क्षि. PG11 records
   the mismatch and does not count the former spelling as a literal witness
   for the latter. Optional weak vowel-initial vṛddhi remains a separately
   sourced branch.
6. **S-lopa before dh.** Kāśikā at 8.2.25 discusses a sic restriction;
   Siddhāntakaumudī gives the broader affix-initial dh reading, with
   Bālamanoramā at 7.2.78 supporting वध्वे. PG11 selects that reading only
   for the five admitted s-final roots. It does not claim that all such
   scope disputes are resolved.

## Ordered morphology

Vid's 3.4.83 option uses the 3.4.82 ending inventory while retaining the
original laṭ request and ending features through the reviewed sthānivad
relation. Brū's 3.4.84 option couples the first five parasmaipada ending
substitutes to āh; it cannot be applied to the sixth slot or ātmanepada.
The original teaching forms, substitute markers and deleted sounds remain
in memory. The final a in the notation āha is pronunciation-only here.

iṭ under 7.2.76 requires a val-initial sārvadhātuka ending: y and vowels
are excluded, but apit is allowed. The five lexical members are rud, svap,
śvas, an and jakṣ. Īś/īḍ have their own se/dhve conditions. Brū's īṭ under
7.3.93 additionally requires pit and hal; it is mandatory where admitted.
All are ṭit augments on the ending, rather than additions to the root.

For śī, 7.1.5 must first produce the actual jh → at substitute. Ruṭ under
7.1.6 is attached to that component, with source UIDs checked against the
ending. Its u is pronunciation-only according to Bālamanoramā, whereas ṭ
is the actual it marker. These are different reasons for nonpronunciation.
Śī's 7.4.21 guṇa does not fabricate a strong/pit ending.

Han retains different deletion targets before weak jhal and before a
vowel. The latter creates the actual n adjacency for 7.3.54, with the
specific Kāśikā non-restoration license recorded. The five 6.1.6 roots
receive an abhyasta designation without invented copied sounds. Daridrā
and śās keep their consonant- and vowel-triggered paths distinct.

Lih's local 8.4.41 visibility permits 8.3.13 deletion; that actual deletion
then licenses 6.3.111 short-i lengthening. Each permission is restricted to
the lexical identity and inspected sound/history conditions. The retained
morphological source is immutable, and readout cannot feed back into it.

## Ṛ's register and copy

Source entry 1030017, short ṛ, retains its छान्दसः tag. The
Siddhāntakaumudī passage at 7.3.87 explicitly licenses its use in classical
language as well. This supports this one classical present profile without
erasing the tag or admitting all tagged juhotyādi entries.

The only copied span admitted here is the sole-vowel root. The copy owns
its source link; 7.4.77 with 1.1.51 introduces i plus r, and 7.4.60 removes
the generated consonant while retaining that history. Copy i → iy under
6.4.78 precedes the root's later vowel junction. Multi-vowel spans and a
general vowel-initial reduplicator remain unimplemented.

## Literal word evidence and its gaps

[REFERENCE_CASES.json](REFERENCE_CASES.json) has 245 literal Sanskrit
word-membership cases across 39 new roots, plus 40 expected refusals.
Matching checks word boundaries using Devanagari letters while allowing
adjacent daṇḍa punctuation. It does not alter the words. Ambiguous वेति and
आह matches are restricted to the relevant lexical commentary context.
These are membership cases; one witnessed optional branch does not certify
the completeness of the entire branch set.

New pṛj, **1020021**, has lexical and rule evidence and nine matching
comparison cells, but no separate exact full-word witness in the selected
passages. The selected Siddhāntakaumudī passage prints पृङ्क्त rather than
पृङ्क्ते. PG11 does not insert the missing vowel and count it as a source
match. Bālamanoramā supports the ṛ-upadhā identity without supplying that
missing literal word.

The six PG10 gaps remain open: **1020036, 1020037, 1020048, 1020052,
1020054 and 1020056**. Neither the new boundary matcher nor cumulative
coverage relabels those older entries as separately word-witnessed.
Implementation agreement is recorded in its own report section.
