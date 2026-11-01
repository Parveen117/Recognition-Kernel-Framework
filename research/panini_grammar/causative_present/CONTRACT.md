# PG13 — Finite construction and ownership contract

Author: Monty. 2 November 2026.

## Domain and primitive state

The domain is the twelve lexical records in
[LEXICAL_ENTRIES.json](LEXICAL_ENTRIES.json), their exact listed meanings,
and a separately supplied causative and P-context license. Present,
classical kartari, an explicit absence of prefixes, internal saṃhitā and
pause after the word are required. The nine person-number choices are
finite. Other requests return `UNRESOLVED` rather than being assigned an
unreviewed word.

The inherited linguistic carrier consists of identified teaching sounds,
visible sounds with unique UIDs, owned morphemes, feature and marker
evidence, ordered events and a separate pronunciation projection. PG13
adds a root constituent and a derived-dhātu constituent over those existing
owners. These are explicit adapter assumptions, not a construction of the
framework's full native operator carrier.

There is exactly one lexical root and one ṇic affix. When prescribed,
exactly one puk/yuk augment belongs to the root constituent. Outer śap
and tiṅ follow the complete derived dhātu. Contiguous order is checked;
an augment cannot move after ṇic or become its member.

## Stage domains

| Required input phase | Operation | Result phase |
| --- | --- | --- |
| ROOT_AND_NIC | Root vṛddhi or guṇa, licensed mit shortening, root ayādi | ROOT_STRENGTH |
| ROOT_STRENGTH | Optional presence of the prescribed root-final augment; build root constituent | ROOT_AUGMENT |
| ROOT_AUGMENT | 3.1.32 on the root constituent plus ṇic | DERIVED_DHATU |
| DERIVED_DHATU | Śap and the requested tiṅ; relative aṅga declaration | OUTER_AFFIXES |
| OUTER_AFFIXES | Guṇa of ṇic i, then its own ayādi | STEM_READY |
| STEM_READY | Ending substitution, śap lengthening or vowel junction | COMPLETE |
| COMPLETE | Independent immutable pause readout | Pronunciation result |

Each mutating stage requires its exact preceding phase and validates the
constituent structure. Repetition, wrong order and projection feedback are
excluded. Ordered event count is derivation history, not physical time.

## Preservation argument on this domain

**Initial state.** Source identity and teaching-form preprocessing select
one reviewed root. Ṇic designation retains ṇ and c separately from its
visible i. Independent meaning and pada licenses are checked before any
derivation. Ordinary root requests take the unchanged predecessor route.

**Sound replacement.** Each replacement stores the previous sound objects
in an event and assigns new UIDs using its target owner and event index.
The root or affix remains the same owner. Thus a change in visible spelling
does not erase its original source or collapse root and affix histories.
The two r-accompanied operations retain the source ṛ and resulting r.

**Mit shortening.** The selected gam entry has a source-bound gaṇasūtra
license. 7.2.116 first produces gām; 6.4.92 consumes that actual long
upadhā and records its shortening. The second event points to the first
event's result. The final m remains a root sound; it is not inferred to
be an it marker from the term *mit*.

**Augmentation.** Puk/yuk carry their own three teaching sounds. K is the
final marker, u is the separately retained pronunciation aid, and only
p/y is visible. The visible sound keeps the augment's source UID. The
root constituent contains the root followed by this augment; 1.1.46
records its final-member placement. This operation creates no second root
and changes no ṇic sound. Pā in drinking has yuk's specific exception;
protecting pā is a different lexical identity and is refused here.

**Derived dhātu and outer effects.** 3.1.32 includes every root constituent
member and ṇic exactly once. Śap is prescribed on this composite, not on
the original lexical gaṇa. The aṅga before śap ends in ṇic's i, so guṇa
and the subsequent ayādi act on ṇic. Earlier root substitutions and
augments remain unchanged. Ending rules act on tiṅ or the final śap a.

**Readout.** The projection begins from a deep copy of the completed
morphology. Pause changes do not rewrite that morphology or feed a sound
back into an earlier stage. UIDs, membership, original teachings and the
event ledger therefore survive the pronunciation query. The direct checks
exercise these premises and all 108 generated branches.

This establishes the stated preservation argument for the declared stage
operations. The checked spellings are finite evidence, not a universal
soundness or completeness proof for Pāṇini's grammar. The adapter does not
construct a full operator family or establish the typed requirement
`pi_0(Construct_lambda(inputs)) = Construct_0(pi_0(inputs))`; that native
lift and quantum-calculator integration remain **OPEN**.
