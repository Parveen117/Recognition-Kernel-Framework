# PG1 grammar specification

Author: Monty. 1 November 2026.

This is a specification for reviewing the grammar. It does not introduce a
new executable rule system. References are to the pinned text and commentary
in [SOURCES.md](SOURCES.md); the selected Sanskrit and IAST formulations are
in the [foundation register](FOUNDATION_REGISTER.md).

## 1. The input is richer than a Sanskrit string

A derivation starts with an intended linguistic task: a root or nominal stem,
its lexical identity, the intended meaning and grammatical categories, and a
declared language/recitation domain. Analysis of an unknown sentence is a
different task: it may return multiple such inputs. Generation from an input
does not prove unique analysis of its output.

The required distinctions are:

| Layer | Required information | Why the surface alone is insufficient |
|---|---|---|
| Text witness | Edition, sūtra ID, exact wording, commentary and variant reading | Identically numbered passages may have different readings or scope interpretations |
| Phonetic token | Vowel/consonant identity, duration, accent, nasalization, articulation, positional identity in a pratyāhāra | Unicode letters do not encode the complete teaching or recitation form |
| Morpheme | Stable identity, root/stem/affix/augment type, upadeśa, remaining surface, it designations and their sources | Śap and ac can both leave a, while having different grammatical properties |
| Lexical entry | Root gaṇa, nominal class, gender, meaning, pada/iṭ conditions and gaṇa membership | Matching a sound sequence does not establish membership or sense |
| Structure | Boundaries of root, aṅga, affix, pada, compound, clause and pause | An internal a+vowel junction and a pada boundary can select different rules |
| Semantic features | Kāraka relations, what is already expressed, voice, person, number, time/mood and relevant sense | Kartari, anabhihite and present time are not phoneme predicates |
| Derivation | Ordered events, before/after references, replacement/deletion type, licensing rule and visibility relation | A later asiddha effect can exist while being unavailable to an earlier rule |

Technical labels are evidence-bearing assertions, not permanent booleans
assigned without context. An aṅga is relative to an affix prescription
(1.4.13); *bha*, *pada* and other designations have their own scopes. An
explicit saṃjñā exclusion or inheritance rule may change what a particular
operation can use. Retaining a fact in history does not make every future
rule entitled to use it.

## 2. Rule-reading contract

A reviewed rule record must provide all of the following before it becomes
an implementation candidate:

1. **Identity and evidence:** sūtra number, exact text, commentary witness,
   reading status, and any vārttika/paribhāṣā separately attributed.
2. **Interpretation:** padaccheda, grammatical case, semantic role of each
   expression, and whether it names a literal form, saṃjñā, class or unit.
3. **Inherited conditions:** each anuvṛtti edge names the borrowed expression
   and its source; each adhikāra names its governing region and termination.
   Mere numerical proximity is not evidence of inheritance.
4. **Domain:** lexical and semantic predicates; language/recitation register;
   relevant morpheme/boundary; admissible designations and rule-relative view.
5. **Action:** designation, affix prescription, replacement, augment, lopa,
   restriction, option or scope declaration. The action's object and extent
   must be specified independently of its surface rendering.
6. **Interaction:** source-supported exception/blocking relationships,
   visibility dependencies, genuine competing operations and optional branches.
7. **Witnesses:** a licensed example, a blocked near-example, and unresolved
   cases. A missing interpretation remains an obligation, not a default action.

The output is therefore a source-annotated relation, potentially with several
licensed results. A mandatory unique-normal-form contract is inappropriate
for an unrestricted language containing *vā*, *vibhāṣā*, *anyatarasyām*,
register-dependent usage and alternative analyses. Each option needs its own
scope: these expressions cannot all be replaced by one global coin flip.

### Three readings that expose missing information

| Rule | Expanded reading needed | What a naive record would lose |
|---|---|---|
| 6.1.78, *eco 'yavāyāvaḥ* | *aci* from 6.1.77; saṃhitā from 6.1.72; ordered ec / ay-av-āy-āv correspondence | A replacement unconditionally applied to every e/o/ai/au |
| 3.1.68, *kartari śap* | Root and affix headings; *sārvadhātuke* from 3.1.67; agent-expressing sense | Treating *kartari* as the next sound, or inserting śap into every root-derived formation |
| 6.1.97, *ato guṇe* | *apadāntāt* from 6.1.96; *pararūpam* from 6.1.94; 6.1.84 two-unit scope | Wrong external sandhi, or bhavānti instead of bhavanti |

T80 already supplies records by hand; it does not infer these dependencies
from raw sūtra text. Its interpretation of 6.1.87 restricts the posterior
input to *ik*, whereas the publisher's inherited source condition is *aci*.
That is a local carrier choice to record, not a replacement reading of Pāṇini.

## 3. Sound classes are ordered, contextual objects

Store the fourteen Māheśvara formulas with distinct terminal-marker positions
and both occurrences of ha. A pratyāhāra records its initial position, closing
marker and ordered sound members. Keep a set view only for questions that
depend on membership. 1.3.10 needs ordered correspondence; T79–T80 already
show why set-preserving permutations can change that correspondence.

Savarṇa expansion requires 1.1.9–10, the appropriate reading of 1.1.69,
duration restrictions such as 1.1.70, and the grammatical status of the
referenced item. It is not a Unicode-normalization operation. Long ṝ, the
treatment of ḷ/its lengthened counterpart, pluta, accents and nasalization
need declared phonological domains and source readings; they must not be
silently inferred from T58's ten-vowel carrier.

1.1.50 selects among **already licensed substitutes**. The Kāśikā discusses
several bases of similarity. A source-specific mapping can be reviewed and
then realized by a finite algorithm; choosing a mathematical distance first
does not establish that it is the traditional criterion in every context.

## 4. Four operations that must remain distinct

| Operation | Source | Required record |
|---|---|---|
| It designation and it-lopa | 1.3.2–9 | Which teaching-form token is a marker, designation evidence, protected cases and removed surface position |
| Whole-affix disappearance | 1.1.60–63 and the particular deleting rule | Affix identity, lopa/luk/ślu/lup classification and exactly which affix-conditioned effects remain available |
| Substitution | 1.1.49–56 and the particular vidhi | Sthānin, ādeśa, extent, boundary ownership and restricted inherited properties |
| Augmentation | 1.1.46–47 and the particular vidhi | Augment identity, placement and affected constituent; not an invented replacement of the entire word |

1.3.4 is a concrete guard against overgeneralizing 1.3.3. Final p in *tip*
can be an it marker; final m in inflectional *am* is not removed by that
blanket logic. Likewise, initial ś in the non-taddhita *śap* is treated under
1.3.8, whose non-taddhita restriction must remain present.

The Kāśikā on 1.1.62 distinguishes the lopa of the **whole affix** from that
of one part. Its retained effects are affix-conditioned; this is not a
universal restoration of every sound-triggered operation. 1.1.63 blocks
specified aṅga consequences after lu-marked deletion. A correct history can
retain the deleted affix while a particular rule is prohibited from using it.

Similarly, 1.1.56 does not give a replacement all properties of its original
for every phoneme-dependent operation. Future rule records must specify
which query is licensed to read the original, the replacement or neither.

## 5. Conflict and visibility are separate questions

First determine the candidate rules on the correct views and domains. Then
determine whether their actions actually compete. A saṃjñā assignment and a
sound replacement need not be rivals just because both are applicable.

For a genuine conflict, record the argument that licenses a restriction,
exception or priority relation. Do not infer a universal *apavāda* relation
from finite domain containment. T66 already supplies a counterexample to
that generalization: adding ātmanepada contexts changes the apparent
containment involving 6.1.97. Its exception status needs a source reading.

The Kāśikā on 1.4.2 applies *para* to equal-strength conflicts, excluding the
unequal-strength cases it lists. The repository's finite resolver ladder is
a declared model of selected interactions. PG1 does not promote it to a
complete historical precedence calculus. Definitions, scope and possible
interactions of nitya, antaraṅga/bahiraṅga and particular paribhāṣās remain
review obligations.

| Region | Adopted reading | Required distinction |
|---|---|---|
| 8.2.1, Tripādī | 8.2–8.4 effects are asiddha to the preceding sapādasaptādhyāyī; within Tripādī, later effects are asiddha to earlier rules | Rule-relative direction; actual history is retained; commentary qualifications must be checked |
| 6.4.22, Ābhīya | Kāśikā reading through the end of 6.4, with *samānāśraya* and stated qualifications | Same-support dependence and regional interaction, not a copy of the Tripādī numerical schedule |

Represent a view as `visible(rule, event, constituent, interpretation)`, not
as a single global flag saying a change never happened. The implementation
of that relation is deferred until enough individual readings are closed.
Even “finish all early rules, then all late rules” is only a finite scheduling
strategy; it does not encode every source-level visibility condition.

## 6. The minimum morphological inventories

The following are the teaching-form inventories, not the final spoken
endings. Marker-bearing upadeśa must be recorded separately, including
nasalization that a compact printed list may not show fully.

| Sup row / case | Singular | Dual | Plural |
|---|---|---|---|
| 1 | su | au | jas |
| 2 | am | auṭ | śas |
| 3 | ṭā | bhyām | bhis |
| 4 | ṅe | bhyām | bhyas |
| 5 | ṅasi | bhyām | bhyas |
| 6 | ṅas | os | ām |
| 7 | ṅi | os | sup |

This is 4.1.2, with its governing nominal domain. Vocative treatment is an
additional grammatical condition, not an eighth trio added to the 21-item
inventory. Repeated strings in distinct cells retain distinct identities.

| Tiṅ pada / person | Singular | Dual | Plural |
|---|---|---|---|
| Parasmaipada prathama | tip | tas | jhi |
| Parasmaipada madhyama | sip | thas | tha |
| Parasmaipada uttama | mip | vas | mas |
| Ātmanepada prathama | ta | ātām | jha |
| Ātmanepada madhyama | thās | āthām | dhvam |
| Ātmanepada uttama | iṭ | vahi | mahiṅ |

This is 3.4.78 under 3.4.77, with 1.4.99–102. Sanskrit *prathama* corresponds
to English third person, *madhyama* to second and *uttama* to first. Person
selection also needs 1.4.105–108 and intended agreement. Choosing an ending
does not itself decide the lexical pada, time/mood, voice or vikaraṇa.

## 7. Coverage families and their grammatical contracts

| Family | Input and result contract | Dependencies that cannot be skipped |
|---|---|---|
| Nominal inflection | Stem identity, gender, class, number and case → licensed sup-derived forms | Sarvanāma/saṃkhyā designations, feminine/neuter/consonant stems, aṅga operations, accent and exceptions |
| Verbal inflection | Root entry, sense, gaṇa, pada, voice, lakāra, person/number → tiṅ-derived forms | Vikaraṇas, iṭ/set/aniṭ conditions, augments, reduplication, ablaut, substitutions and alternative roots |
| Derived verbal stems | Root plus desiderative/causative/intensive etc. intent → structured derived stem | Sanādi prescriptions, semantic restrictions, reduplication and subsequent dhātu status |
| Kṛt | Root/derived root plus semantic and syntactic conditions → primary derivative | Individual affix selection, lexical restrictions, kṛt identity, nominal/verbal behavior |
| Taddhita | Nominal input plus specified sense → secondary derivative | Gaṇa membership, stem replacement, gender and the exact semantic heading |
| Samāsa | Meaningfully related padas and compound type → structured compound | Samartha, permitted types, sup deletion/aluk exceptions, head/gender, samāsānta and accent |
| Kāraka/vibhakti | Intended event and discourse relations → designations and licensed case choices | Abhihita accounting, upapada rules, multiple-object constructions and agreement |
| Sandhi | Structured phonetic boundary and register → licensed junction outcomes | Morphological boundary, saṃhitā/pause, optional forms, visibility and recitation conventions |
| Accent/Vedic | Declared textual/recitation tradition and lexical accents → source-licensed accented forms | Chandas-specific rules, lexical accent, pluta and restricted variants |

This table is a contract map. Completing one example in a row does not
complete the family. Chandas and *bahulam* are source-indexed research
domains; they neither license arbitrary output nor prove that an attested
form can never be derived. T66's refusal of *dhīmahi* is a limitation of its
finite system, not a linguistic impossibility theorem.

## 8. Connection to the native full-family carrier

Start with the supplied native typed operator family `C_λ`, its source and
target objects, complementary channels, admissible composition, residue and
pairing/tensor data where declared. Equip grammatical constituents and events
with that data while retaining the discrete source/lexical/grammatical
records above. PG1 does not invent a Hilbert representation or identify a
linguistic operation with a cut-linear relation without an additional proof.

A proposed grammatical step is a typed, possibly branching transformation
on those enriched states. It must preserve its declared arrow type and log
the source-supported action. Rule priority is operational choice, not
algebraic equality of two native operators. Identical spoken outputs do not
identify the complete histories.

For a specialization `π₀`, the required contract is

`π₀(Construct_λ(inputs)) = Construct₀(π₀(inputs))`

on the declared input domain, interpreting results as sets of licensed
branches when appropriate. This is a **requirement**, not an unconditional
new theorem about Pāṇini. A sufficient local condition is that each step's
guards, visibility queries, branch labels, native action and provenance
update commute with `π₀`, with the same available branches on both sides.
Induction on the finite event sequence then proves the displayed equality:
the initial states correspond, and each corresponding next branch has the
same projected state and retained event record. Forward compatibility alone
proves only inclusion; it does not establish that every specialized branch
lifts.

The classical projection must retain grammatical identity and licensed
history queries. Projection to **surface text alone** fails this requirement;
the śap/ac witness in the worked derivations shows why. λ is not a physical
clock or an iteration counter. No clock adapter or quantum-calculator
interpretation is supplied at this grammar stage.
