# PG1 — Pāṇini: grammar before implementation

Author: Monty. 1 November 2026.

This stage establishes the Sanskrit grammar specification before extending its
software or applying it in the quantum calculator. It integrates the existing
T78–T80 research and records the linguistic obligations that their finite
carriers leave open. PG1 is a source and specification packet, not a claim that
the entire Aṣṭādhyāyī has been interpreted, proved complete or implemented.

**Follow-up verification:** [PG2](verification/README.md) audits the pending
scope, priority, sthānivad, it-marker, lexical and soundness-reference layers.
It records source contradictions and bounded positive/negative checks while
leaving full grammar completeness open. Its results do not change PG1's
historical source pins or the frozen T58–T80 packets.

**After T81/T82:** [PG3](root_progression/README.md) develops source-bounded
root substitutions, idit num placement and a separate phonetic query over
2,229 root records. It explicitly corrects the PG2 jhi reading and T82 lakāra
expectations, records the T81 vowel-table limitation, and preserves all earlier
packet bytes. Its 2,081 headword agreements are a lexical diagnostic, not a
grammar-completeness score.

**Executable scope and further derivation:** [PG4](scoped_derivations/README.md)
binds reviewed rule records to inherited terms, applies seven commentary scope
policies, and extends root contact, augmentation and length readings. The
root-headword diagnostic reaches 2,219 agreements, with eight differences and
two unresolved entries retained. Full grammar obligations are listed in its
[remaining-work register](scoped_derivations/REMAINING.md).

**Vikaraṇa selection and complete bounded laṭ:** [PG5](vikarana_lat/README.md)
adds 39 source-bound records and witnessed selection across ten gaṇas.
Thirteen identified roots have complete unaccented laṭ paths: 162 cells and
198 branches across 18 pada paradigms. Literal commentary cases and retained
history checks are kept separate from comparison with another implementation.
Non-thematic stems, infixes and reduplication lead its
[remaining-work register](vikarana_lat/REMAINING.md).

**Non-thematic laṭ and visibility:** [PG6](non_thematic_lat/README.md) completes
ten more identified śnu/u/śnā roots: 153 cells and 167 branches across 17
pada paradigms. It distinguishes strong/weak guṇa, cluster-sensitive junctions,
optional/mandatory u-loss, and earlier ṇatva from later restored dental n.
Its [remaining register](non_thematic_lat/REMAINING.md) targets śnam infix
ownership and class 7 derivation next.

**Owned śnam infixes and class 7:** [PG7](snam_lat/README.md) adds 23 identified
roots / 288 cells / 330 branches, keeping root and affix ownership through
insertion, strong/weak deletion and ordered phonetic changes. Its
[PG7 coverage audit](snam_lat/COVERAGE.md) separates the text inventory,
bounded records, root preprocessing and 46 completed root entries / 603 laṭ
cells across PG5–PG7. [Remaining work](snam_lat/REMAINING.md) includes
bhuj/tṛh, adādi/juhotyādi and the wider grammar packages.

**Sense selection, nested im and initial adādi:** [PG8](exception_lat/README.md)
adds bhuj/tṛh and ad/as: four roots / 45 cells. Distinct bhuj meanings select
pada; im retains its own owner inside the root-with-śnam host; a cited local
visibility exception supports ḍh-lopa. The [PG8 coverage](exception_lat/COVERAGE_STATUS.json)
is 50/2,229 root entries and 648 laṭ cells, with overall grammar completion
still undefined. [Remaining work](exception_lat/REMAINING.md) begins with
reduplication and more adādi paths. [Claude's T86/T87 review](exception_lat/CONCURRENT_REVIEW.json)
remains separately identified; CI and main merging are deferred.

**Owned abhyāsa and strong/weak juhotyādi:** [PG9](abhyasa_lat/README.md)
adds hu, dā and dhā: three roots / 45 cells. Copied sound identities,
collective abhyasta, ghu-conditioned ā-lopa and dhā's specific visibility
permission are retained in the derivation. [PG9 coverage](abhyasa_lat/COVERAGE_STATUS.json)
is 53/2,229 root entries and 693 present cells, with no overall grammar
percentage. [Validation](abhyasa_lat/VALIDATION.md) separates 38 literal
word witnesses, 18 refusals and 63 controls from the 45-cell implementation
comparison. [Claude's T89 review](abhyasa_lat/CONCURRENT_REVIEW.json) records
five stage-removal checks hidden in a comment. [Remaining work](abhyasa_lat/REMAINING.md)
includes the other class-3 roots, further adādi and the native operator lift.

**Further juhotyādi and vowel-final adādi:** [PG10](present_expansion/README.md)
adds 38 roots / 396 cells / 438 branches. Owned copies retain lexical i,
copy guṇa and r-accompanied replacement history. Bhī/hāk and ūrṇu preserve
their options; ru/tu/stu īṭ belongs to the following ending and includes
the licensed apit cases. [PG10 coverage](present_expansion/COVERAGE_STATUS.json)
is 91/2,229 roots and 1,089 present cells. [Validation](present_expansion/VALIDATION.md)
records 153 literal word witnesses across 32 roots, 35 refusals, 94 direct
controls and zero differences across all 396 new cells. Six entries have
no separate full-word witness in the selected commentary passages.
[Remaining work](present_expansion/REMAINING.md) keeps the tagged/vowel-initial
class-3 entries, further class 2, wider grammar and native operator lift
open. Earlier certificates remain frozen; CI and main merging stay deferred.

**Lexical present paths and owned ending substitutions:**
[PG11](lexical_present/README.md) adds 40 roots / 405 cells / 420 branches:
39 further adādi entries plus the explicitly classical-use ṛ profile.
iṭ/īṭ/ruṭ retain their ending hosts; optional vid endings and coupled
brū/āh substitutions preserve the present request and source features.
Repeated source words bind to their own occurrences and cases, and six
source disagreements remain recorded. [PG11 coverage](lexical_present/COVERAGE_STATUS.json)
is 131/2,229 roots, 166 paradigms and 1,494 present cells.
[Validation](lexical_present/VALIDATION.md) separates 245 primary-word
cases across 39 roots, 40 refusals and 107 controls from the zero-difference
405-cell comparison. New pṛj and the six PG10 word-witness gaps remain
open. [Remaining work](lexical_present/REMAINING.md) includes class-2
prefix/context entries, tagged roots, wider grammar and native operator
integration. PG1–PG10 evidence is frozen; CI and main merging stay deferred.

**Further śnu, u and śnā present paths:** [PG12](nasal_present/README.md)
adds 97 roots / 1,116 cells / 1,316 branches: 22 svādi, eight tanādi and
67 kryādi entries. Owned n-lopa, grah/jyā saṃprasāraṇa, khav's ūṭh and
optional tanādi root guṇa preserve their intermediate sounds and branch
conditions. Ṇatva retains tṛp/kṣubh's prohibitions and kṣubh's local śnā
identity query. [Source review](nasal_present/SOURCE_REVIEW.md) records
seven source decisions, including a declared pvādi endpoint and register
boundaries. [PG12 coverage](nasal_present/COVERAGE_STATUS.json) is
228/2,229 roots, 290 paradigms and 2,610 present cells, with 208 bounded
definitions / 152 distinct sūtra IDs. The admitted profiles cover 26/38
class-5, 10/10 class-8 and 70/71 class-9 entries; all contexts of those
classes remain outside that count. [Validation](nasal_present/VALIDATION.md)
separates 109 literal-word cases across 73 roots, 37 refusals and 124
controls from the zero-difference comparison. Twenty-four new exact-word
gaps and the seven earlier gaps remain open.
[Remaining work](nasal_present/REMAINING.md) includes other present
classes, coupled substitutions, wider grammar and the full native operator
lift with typed zero-specialization compatibility and quantum-calculator
integration. PG1–PG11 evidence is frozen; CI and main merging stay deferred.

**Causative presents with owned root constituents:**
[PG13](causative_present/README.md) develops twelve identified roots /
108 causative P cells, extending T105's useful three-cell examples to full
nine-cell paradigms. Root substitutions, gam's intermediate gām and mit
shortening, and puk/yuk ownership remain explicit. K is the augment's it
marker; u is pronunciation-only. The full root constituent plus ṇic is
the derived dhātu, and śap then acts on ṇic's own i → e → ay.
[Validation](causative_present/VALIDATION.md) records 11 literal-word cases,
31 refusals, 74 controls, a zero-difference 108-cell comparison and 36
matching companion expectations. Kṛṣ's exact-word witness remains open.
[Current coverage](causative_present/COVERAGE_STATUS.json) preserves
228 simple-present roots / 2,610 cells and counts the 108 causative cells
separately: 2,718 cells distinguished by formation. The
[concurrent review](causative_present/CONCURRENT_REVIEW.json) confirms the
T89 repair statically; no companion certificate is replayed.
[Remaining work](causative_present/REMAINING.md) includes semantic pada
contexts, further formations and native integration. PG1–PG12 evidence
is frozen; CI and main merging stay deferred.

**Mathematical construction before further test batches:**
[PG14](grammar_construction/README.md) connects interpreted events to kāraka,
voice, pada, agreement and owned word derivations. Its written twelve-root
causative domain derives ṇic/pada permission from the frame, including
1.3.77 optionality and 1.3.86–89 exceptions. It separates patient agreement
from bhāva's default 3sg, derives thematic A endings and adds the written
kriyate/hriyate paths. The [native construction](grammar_construction/NATIVE_OPERATOR_LIFT.md)
supplies a noncommutative cut-path operator instance with pairing,
complementary channels and a proof of exact history-bearing zero-recovery.
This is an explicit model, not an implementation of all grammar rules or
all native operator families. [Claude review](grammar_construction/CLAUDE_REVIEW.md)
uses T110/T112–117 and records the bhāva agreement and asādṛśya qualifications.
[Work record](grammar_construction/WORK_RECORD.md) states that Python tests
are deferred under the owner's grammar-first instruction; prior executable
coverage and frozen packets are unchanged. [Remaining mathematical work](grammar_construction/REMAINING.md)
starts with wider causative frames and derived-stem passives.

**Causative passive, expressed karman and retained ṇic:**
[PG15](causative_passive/README.md) constructs twelve causal passive
root/sense paths with owned ṇic-lopa, explicit double-karman selection,
residual cases and agreement. Its [written derivations](causative_passive/DERIVATIONS.md)
give nine slots per aṅga and distinguish kriyate/kāryate/kārayate,
bhāva versus causal patient agreement, and nī/pā's doubled-y ownership.
The word reading selects the non-doubling options of 8.4.46–47. The
[native extension](causative_passive/NATIVE_EXTENSION.md) retains PG14's
pairing/zero-recovery and proves a surface-observation obstruction and
one-extra-channel repair for simple versus causal gamyate. The
[source review](causative_passive/SOURCE_REVIEW.md) preserves commentary
attribution and variants. A [targeted T118 review](causative_passive/CLAUDE_T118_REVIEW.md)
informs [Claude's independent next samāsa task](causative_passive/PARALLEL_WORK.md).
[Work and frontier](causative_passive/WORK_RECORD.md)
record written proofs, deferred tests and unchanged historical implementation
counts; wider grammar and runtime integration remain open.

**Future meaning and complete bounded lṛṭ/luṭ paradigms:**
[PG16](future_construction/README.md) develops eight exact roots and twelve
pada profiles into 216 written positions. Its [semantic domain](future_construction/SEMANTIC_DOMAIN.md)
retains word-level future vivakṣā, temporal-adapter evidence and
principal-result pada selection. [Affix and iṭ construction](future_construction/AFFIX_AND_IT.md)
distinguishes sya/tās from their tiṅ endings and resolves the gam and
ṛ-final exceptions. [Ending paths](future_construction/ENDING_CONSTRUCTION.md)
include luṭ A's 2du/2pl/1du and the owned ḍā/rau/ras procedure;
[derivations](future_construction/DERIVATIONS.md) give all positions and
the bounded factorization proof. [Source review](future_construction/SOURCE_REVIEW.md)
records selected commentary readings and publisher attachment errors.
The [native extension](future_construction/NATIVE_EXTENSION.md) preserves
pairing and exact zero-recovery, then repairs twelve restricted luṭ P/A
word collisions with an explicit size bound at zero. [Work record](future_construction/WORK_RECORD.md)
keeps tests deferred and implemented counts unchanged. [Claude's lane](future_construction/CLAUDE_HANDOFF.md)
remains samāsa/nominal development while Codex extends verbal formations.

**Dependent future options and retained causative ṇic:**
[PG17](future_extension/README.md) extends futures by nine basic-root
entries and twelve inherited causal frames. Its [branch relation](future_extension/DOMAIN_AND_BRANCHES.md)
derives pada-conditioned iṭ options and exclusions; [root derivations](future_extension/ROOT_DERIVATIONS.md)
retain the exact lexical and phonetic history. [Causative futures](future_extension/CAUSATIVE_FUTURES.md)
keep PG14's 21 causal pada profiles, establish outer iṭ and distinguish
the retained ṇic-i→e→ay operation from augment protection. The
[paradigm register](future_extension/PARADIGMS.md) specifies 79 branch rows
and their nine-slot expansions: 612 positions and 711 factorized written
morphological readings, with no new executed coverage. The [native proof](future_extension/NATIVE_BRANCH_CONSTRUCTION.md)
constructs the dependent three-branch kṛp operator and proves that even
the whole P future paradigm fails to separate vṛt/vṛdh, while a forward
A query separates this pair. [Source review](future_extension/SOURCE_REVIEW.md)
preserves edition and commentary qualifications; [work and frontier](future_extension/WORK_RECORD.md)
keep tests deferred and identify bhāva/karma futures as the next domain.

**Bhāva/karma futures and source-sensitive ciṇvat:**
[PG18](future_voice/README.md) extends the meaning-to-form construction
to sixteen basic entries and thirteen causal frames. [Semantics](future_voice/SEMANTIC_DOMAIN.md)
separates default Bhāva 3sg from expressed-karman agreement. The
[ciṇvat procedure](future_voice/CINVAT_AND_VISIBILITY.md) couples its
augment to the choice, restricts aṅga transport and distinguishes the
ordinary versus ciṇvat iṭ views for ṇic-lopa and grah lengthening.
[Basic](future_voice/BASIC_DERIVATIONS.md) and [causal derivations](future_voice/CAUSATIVE_DERIVATIONS.md)
specify all interfaces, including han/grah/dṛś and the mit length option.
The [register](future_voice/PARADIGMS.md) gives 458 positions and 895
factorized written branch readings, with no new executed coverage.
The [native proof](future_voice/NATIVE_QUERY_CONSTRUCTION.md) preserves
pairing/cuts and typed zero-recovery and proves why an origin-free
letter display cannot decide the lopa query. [Source review](future_voice/SOURCE_REVIEW.md)
and [work record](future_voice/WORK_RECORD.md) retain the declared limits;
[Claude's update](future_voice/COMPANION_UPDATE.md) records T121–T124,
the accepted source repairs and remaining independent nominal work.
Grammar tests remain deferred.

**Loṭ and vidhiliṅ from intended meaning:**
[PG19](imperative_optative/README.md) constructs their shared modal senses
and bounded context restrictions, then derives ending ownership, loṭ's
first-person pit āṭ, vidhiliṅ's explicit ṅit and the resulting stem choices.
[Thematic](imperative_optative/THEMATIC_DERIVATIONS.md),
[kṛ/krī](imperative_optative/ATHEMATIC_DERIVATIONS.md) and
[causal/voice](imperative_optative/VOICE_AND_CAUSATIVES.md) derivations feed
a [976-position written register](imperative_optative/PARADIGMS.md).
The [native proof](imperative_optative/NATIVE_MODAL_CONSTRUCTION.md)
preserves pairing/cuts and typed zero-recovery, and proves the displayed
modal-information and boundary-query obstructions. [Source review](imperative_optative/SOURCE_REVIEW.md)
and [work record](imperative_optative/WORK_RECORD.md) retain the claim limits
and deferred tests. [Companion review](imperative_optative/COMPANION_UPDATE.md)
reads Claude's T125–T130, records the 90-position T96/T99 modal overlap
and a 3.4.92 pit-state integration gap, without replaying certificates.

**Āśīrliṅ and blessing loṭ:**
[PG20](benediction/README.md) derives their distinct affix classes,
P kit/A conditional-kit, all owned endings, basic and causal/voice
continuations, ciṇvat/mit and dh/ḍh choices, and optional tātaṅ.
The [register](benediction/PARADIGMS.md) has **1,057 positions / 1,292
word-branch readings**, including inherited/overlapping morphology explicitly
identified there. [Native proofs](benediction/NATIVE_BENEDICTION.md) give
typed zero-recovery and the marker, stem-order and person-information
boundaries. [Sources](benediction/SOURCE_REVIEW.md) and
[work record](benediction/WORK_RECORD.md) distinguish written derivations
from unrun tests. [Claude through T135](benediction/COMPANION_UPDATE.md)
records the useful laṭ expansion and remaining integration tasks.

**Nasal-class modal expansion:**
[PG21](nasal_modals/README.md) completes loṭ, vidhiliṅ and blessing-loṭ
for seventeen exact roots / twenty-seven pada profiles. It retains both
3.1.82 affixes and the separately identified tanādi guṇa source policies,
derives actual-cluster hi-luk and augment-sensitive u-loss exclusion, and
adds fifty-two tātaṅ branch readings. The [register](nasal_modals/PARADIGMS.md)
has **729 positions / 1,159 source-family readings** (935 after fixing
the guṇa policies). [Native proofs](nasal_modals/NATIVE_TRANSPORT.md)
give typed recovery and the finite three-to-two laṭ/loṭ comparison.
[Sources](nasal_modals/SOURCE_REVIEW.md), [work](nasal_modals/WORK_RECORD.md)
and [Claude handoff](nasal_modals/COMPANION_UPDATE.md) retain evidence,
overlap, deferred tests and the non-overlapping next tasks.

**Adādi/juhotyādi/rudhādi modal continuation:**
[PG22](athematic_modals/README.md) constructs twelve exact roots /
eighteen qualified pada profiles, including hi→dhi, dehi/dhehi/edhi,
owned copy lopa, dhā's exception and ordered consonant/nasal readout.
Its [register](athematic_modals/PARADIGMS.md) has **486 positions /
558 written branch readings**, with all ordinary collapse sites and
thirty added tāt readings. [Native proofs](athematic_modals/NATIVE_ATHEMATIC.md)
give the typed zero-law, the original-s visibility obstruction and a
dependent ending/sound-fibre construction. [Sources](athematic_modals/SOURCE_REVIEW.md),
[work](athematic_modals/WORK_RECORD.md) and [Claude through T138](athematic_modals/COMPANION_UPDATE.md)
preserve exact evidence, the actual-marker handoff and deferred tests.

**Lexical modal exceptions and combined progress:**
[PG23](lexical_modals/README.md) adds han/śās, rudādi, brū and śī:
nine exact roots /ten qualified pada profiles and **270 positions /
286 written readings**. It derives whole-root hi exceptions, effective
pit, distinct iṭ/īṭ/ruṭ hosts and śī's weak-context guṇa. The
[native construction](lexical_modals/NATIVE_LEXICAL.md) proves typed
zero-recovery and finite source/marker/owner observation obstructions.
[Sources](lexical_modals/SOURCE_REVIEW.md) preserve literal anomalies;
[Claude through T142](lexical_modals/COMPANION_UPDATE.md) credits useful
runtime repairs and gives the remaining integration assignment.
[Combined progress](lexical_modals/PROGRESS.md) includes written work
awaiting verification: **569 bounded-rule IDs and 7,759 verbal positions**,
with overlapping cells and merely cited rules kept out of the developed
totals. The 569/3,983 ratio is rule reach, not whole-grammar completion.
[Work record](lexical_modals/WORK_RECORD.md) retains the deferred-test boundary.

**Consonant modals and directed ending descent:**
[PG24](consonant_modals/README.md) adds dviṣ, duh/dih/lih, īḍ/īś,
vas and mṛj: eight exact roots /twelve qualified pada profiles and
**324 positions /336 written readings**. It constructs host-qualified
iṭ, the weak-vowel mṛj option, dhv-sensitive bhaṣ and mandatory
root-owned ḍh-lopa/lengthening. The [native theorem](consonant_modals/NATIVE_CONSONANT.md)
proves typed zero-recovery and a sharp three-coordinate linear repair
bound for its stated six-history observer.
[Coverage](consonant_modals/COVERAGE.json) raises the written verbal
inventory to **8,083 positions** while bounded rule-ID reach stays
**569**; new contexts reuse those IDs. [Sources](consonant_modals/SOURCE_REVIEW.md)
and [T142 handoff](consonant_modals/COMPANION_UPDATE.md) keep primary
adjudication separate from runtime comparison labels.
[Work and the full-grammar queue](consonant_modals/WORK_RECORD.md)
retain the owner's written-first priority and deferred verification.

**Abhyasta modals and reusable family interfaces:**
[PG25](abhyasta_modals/README.md) closes I/O/B for **15 exact roots /19
qualified profiles**, adding **513 positions /570 written readings**.
It derives hāk's separate hi/y/tāt fibres, bhī's short/long options,
daridrā's short i, pṝ/pṛ and the target-specific guṇa boundary.
The [native construction](abhyasta_modals/NATIVE_FAMILIES.md) proves
source-qualified block assembly, dependent choice counting and typed
zero-recovery. [Coverage](abhyasta_modals/COVERAGE.json) reaches **8,596
written verbal positions /574 bounded-rule IDs**. All fifteen class-3
roots admitted in PG8/10/11 now have these three modal constructions:
21 profiles /567 positions already included in the cumulative total.
[Sources](abhyasta_modals/SOURCE_REVIEW.md) retain lexical qualifications
and literal conflicts. [Claude through T143](abhyasta_modals/COMPANION_UPDATE.md)
credits useful repairs and assigns the remaining option sets/adapters;
its comparison totals remain attributed reports.
[Work/frontier](abhyasta_modals/WORK_RECORD.md) keeps the written-first
priority and deferred tests. The rule ratio is bounded reach, not a
whole-grammar completion percentage.

**Adādi vowel modals and augment-dependent queries:**
[PG26](vowel_modals/README.md) supplies I/O/B for **30 exact roots /32
qualified profiles**, adding **864 positions /991 written readings**.
The [stem construction](vowel_modals/STEMS_AND_AUGMENTS.md) resolves
optional īṭ before strengthening and distinguishes ūrṇu, sū, iṇ/vī
and the fourteen ā roots. The [native theorem](vowel_modals/NATIVE_GUARD_TRANSPORT.md)
proves dependent query transport, a sharp linear observer repair and
typed zero-recovery on the full history carrier.
[Coverage](vowel_modals/COVERAGE.json) reaches **9,460 written verbal
positions /609 bounded-rule IDs**. PG25/26 now cover all 38 exact roots
/44 profiles admitted by PG10 in these three moods, a subtotal of 1,188
positions already counted. [Sources](vowel_modals/SOURCE_REVIEW.md)
retain literal conflicts and the selected source schedule.
[Claude through T145](vowel_modals/COMPANION_UPDATE.md) credits T144/T145's
extensions and identifies remaining branch/history work and a report
count discrepancy. [Work/frontier](vowel_modals/WORK_RECORD.md) keeps
grammar tests, certificate replay and formal verification deferred.
These bounded constructions do not claim whole-grammar completion.

**Consonant inventory modals and coupled auxiliary ownership:**
[PG27](consonant_inventory_modals/README.md) disposes of I/O/B for
**32 exact roots /37 profiles**, adding **997 admitted positions /1,145
readings and two source exclusions**. [Stem construction](consonant_inventory_modals/STEMS_AND_NASALS.md)
preserves num/śnam and root-n ownership; [readout](consonant_inventory_modals/OWNED_CONSONANT_READOUT.md)
retains the source-time niṃssva obstruction through late collapse.
[Admission and auxiliary construction](consonant_inventory_modals/AUXILIARY_AND_ADMISSION.md)
selects vac's usage policy and assembles vidām with matching kṛ,
external nasal alternatives and blessing-tāt.
The [native theorem](consonant_inventory_modals/NATIVE_COUPLED_EXPANSION.md)
proves the controller cut, query transport and typed zero-recovery.

[Coverage](consonant_inventory_modals/COVERAGE.json) reaches **10,456
admitted written verbal positions /639 bounded-rule IDs**, explicitly
reconciling **9,460−1+997** after the vac-present scope correction.
All **68 exact adādi roots /75 profiles** admitted by PG8/10/11 now
have a written modal disposition: **2,023 admitted plus two exclusions**.
All **23 regular PG7 rudhādi roots /32 profiles** have **864 modal
positions** across PG22/27. These are overlapping subtotals already
included, not new counts. Bhuj/tṛh was this stage's next exception
block and is developed in PG28 below.
[Sources](consonant_inventory_modals/SOURCE_REVIEW.md) preserve conflicting
views and frozen historical evidence. [Claude through T147](consonant_inventory_modals/COMPANION_UPDATE.md)
credits luṅ and passive development, attributes the results and records the lane-label
and liṭ-count discrepancies. [Work/frontier](consonant_inventory_modals/WORK_RECORD.md)
keeps verification deferred. The approximately **16.04%** rule ratio
does not measure whole-grammar completion.

**Bhuj/tṛh exceptions, contextual liṅ and actor identity:**
[PG28](exception_modal_contexts/README.md) adds **117 positions /123
readings** on two exact roots /four sense-pada profiles, including one
new upabhoga/A bhuj sense. [Domain](exception_modal_contexts/DOMAIN_AND_ADMISSION.md)
and [construction](exception_modal_contexts/EXCEPTION_CONSTRUCTION.md)
preserve sense-qualified pada, śnam/im ownership and a local sourced
hi-collapse route for tṛṇḍḍhi/tṛṇḍhi.
[Contexts](exception_modal_contexts/MODAL_CONTEXTS.md) and
[desire/actor binding](exception_modal_contexts/DESIRE_AND_ACTOR_BINDING.md)
develop nine operations, 3.3.152–160: supplied semantic fields, clause
addresses, same-actor tumun/liṅ and a separate outer-desire choice.
[Native arguments](exception_modal_contexts/NATIVE_ACTOR_AND_QUERY_TRANSPORT.md)
prove why person labels cannot replace actor identity and derive local
cut transport, a rank repair and typed zero-specialization.

[Paradigms](exception_modal_contexts/PARADIGMS.md) and
[coverage](exception_modal_contexts/COVERAGE.json) reach **10,573 admitted
written finite positions /652 bounded-rule IDs**. All inherited PG8
profiles now have I/O/B; all inherited PG7+PG8 class-7 profiles total
**25 roots /35 profiles /945 modal positions**, extended to 36 profiles
/972 by upabhoga. These are overlapping subtotals. Context requests
and nonfinite bhoktum do not add finite positions. The approximately
**16.37%** bounded-rule ratio is not whole-grammar completion.
[Sources](exception_modal_contexts/SOURCE_REVIEW.md) retain textual
anomalies and the still-open universal scheduling question.
[Claude through T148](exception_modal_contexts/COMPANION_UPDATE.md) credits
the closing causative extension and its four new combined IDs, with a
concrete adapter handoff; [work/frontier](exception_modal_contexts/WORK_RECORD.md)
keeps grammar tests and replay deferred and identifies the next context block.

**Opportunity, kṛt expressions and meaning-sensitive case:**
[PG29](opportunity_necessity/README.md) develops **3.3.167–171** on
four exact roots. [Domain](opportunity_necessity/DOMAIN_AND_DISCOURSE.md)
and [opportunity/eligibility](opportunity_necessity/OPPORTUNITY_AND_WORTHINESS.md)
retain praiṣādi, time-head and relevant-yad dependencies, local bhāva-lyuṭ
alternatives and PG19's previously unbuilt kṛtya projection.
[Necessity/cases](opportunity_necessity/NECESSITY_AND_CASES.md) preserve
the semantic difference between necessity and debt without requiring
an overt avaśyam, and distinguish tṛc kartā from finite luṭ kartā.

[Kṛt construction](opportunity_necessity/KRT_CONSTRUCTION.md) and the
[register](opportunity_necessity/EXPRESSION_REGISTER.md) give **23 nonfinite
base targets** (22 constructed here plus reused bhoktum), **39 nominal
readout targets** and **18 new qualified vah O positions/readings**.
[Coverage](opportunity_necessity/COVERAGE.json) reaches **10,591 admitted
written finite positions /681 bounded-rule IDs**. Nonfinite, nominal
and finite counts stay separate; the approximately **17.10%** rule
ratio does not measure whole-grammar completion.

The [native argument](opportunity_necessity/NATIVE_TYPED_CHOICE.md)
constructs dependent expression fibres and proves that two addressed
scalar channels are necessary and sufficient for its four-history case
cut, where one pooled coordinate fails. Typed zero-specialization keeps
suffix and semantic history. [Source review](opportunity_necessity/SOURCE_REVIEW.md),
[literal archive](opportunity_necessity/SOURCE_EXCERPTS.json) and
[pins](opportunity_necessity/SOURCE_PINS.json) retain the exact source
boundaries. [Claude through T149](opportunity_necessity/COMPANION_UPDATE.md)
credits san and records complementary admission, alternatives and case
work. [Work/frontier](opportunity_necessity/WORK_RECORD.md) keeps grammar
tests/replay deferred and selects 3.3.172 and 3.3.174–176 next.

**Capability, blessing-names and owned prohibitive augmentation:**
[PG30](capability_naming_prohibition/README.md) develops **3.3.172 and
3.3.174–176** in their actual source sequence. Its
[domain](capability_naming_prohibition/DOMAIN_AND_SCOPE.md) corrects
PG29's prospective subject labels, while [capability/naming](capability_naming_prohibition/CAPABILITY_AND_NAMING.md)
retain semantic capacity and the whole-expression appellative condition.
[Prohibition](capability_naming_prohibition/PROHIBITION_AND_AUGMENTS.md)
distinguishes lexical māṅ, associated sma and the separate owners of
blocked aṭ/āṭ and retained ending īṭ.

[Finite construction](capability_naming_prohibition/FINITE_CONSTRUCTION.md)
adds complete kṛ/hṛ P luṅ/laṅ paradigms: **36 positions /36 readings**,
cumulative **10,627 admitted written finite positions**.
[Nominal construction](capability_naming_prohibition/NOMINAL_CONSTRUCTION.md)
and the [register](capability_naming_prohibition/EXPRESSION_REGISTER.md)
give six local construction targets /eight base readings /eight selected
nominal readouts, including all three san/ktic alternatives and Devadatta.
The grades are not added together.

The [native argument](capability_naming_prohibition/NATIVE_OWNERS_AND_BRANCHES.md)
derives owner-selective suppression, an observer obstruction, a one-channel
context repair and retained-source branch multiplicity with typed zero-recovery.
[Sources](capability_naming_prohibition/SOURCE_REVIEW.md),
[literal fields](capability_naming_prohibition/SOURCE_EXCERPTS.json) and
[pins](capability_naming_prohibition/SOURCE_PINS.json) preserve source limits.
[Coverage](capability_naming_prohibition/COVERAGE.json) reaches
**693/3,983 bounded-rule IDs**; approximately **17.40%** is not a whole-
grammar completion fraction. [Claude's handoff](capability_naming_prohibition/COMPANION_UPDATE.md)
records the unchanged T149 head and concrete ownership/admission work.
[Work/frontier](capability_naming_prohibition/WORK_RECORD.md) keeps tests
and replay deferred; 3.3.139–151 and broader word adapters remain open.

**Effective counterfactual admission and conditional words:**
[PG31](counterfactual_contexts/README.md) constructs **3.3.139–151**.
Its [contexts](counterfactual_contexts/CONTEXT_RELATIONS.md) and
[admission](counterfactual_contexts/COUNTERFACTUAL_ADMISSION.md) retain
effective liṅ-nimitta after exceptions, qualified kriyātipatti and
the exclusive 152 boundary. Surprise+yadi has a separately justified route.

[Sya transport](counterfactual_contexts/SYA_TRANSPORT.md) and
[conditional endings](counterfactual_contexts/ENDING_CONSTRUCTION.md)
give 17 basic roots and 12 inherited causal formations, 48 qualified
profiles and 53 branches. The [complete register](counterfactual_contexts/PARADIGMS.md)
adds **432 positions /477 readings**, cumulative **11,059 written
finite positions**, with aṭ/āṭ, dependent iṭ and preserved ṇic owners.

The [native argument](counterfactual_contexts/NATIVE_ADMISSION_AND_TRANSPORT.md)
establishes staged eligibility, the local observer minimum, restricted
transport and typed zero-recovery. [Sources](counterfactual_contexts/SOURCE_REVIEW.md),
[literal archive](counterfactual_contexts/SOURCE_EXCERPTS.json) and
[pins](counterfactual_contexts/SOURCE_PINS.json) retain exact evidence limits.
[Coverage](counterfactual_contexts/COVERAGE.json) is **708/3,983 bounded-rule
IDs**; approximately **17.78%** is not whole-grammar completion.
[Claude's handoff](counterfactual_contexts/COMPANION_UPDATE.md) records
the new T150 and complementary semantic/owner work.
[Work/frontier](counterfactual_contexts/WORK_RECORD.md) keeps tests/replay
deferred and identifies broader prohibitives, passive/bhāva R and nominal
coverage as remaining construction.

**Prohibitive A, bhū-luk and ordinary luṅ:**
[PG32](prohibitive_lung/README.md) adds **234 positions /236 readings**,
cumulative **11,293**, across eight roots and 26 qualified profiles.
Its [domain](prohibitive_lung/DOMAIN_AND_SCOPE.md) separates ordinary
luṅ, māṅ-luṅ and māṅ+sma-laṅ while reusing PG30's 36 completed
kṛ/hṛ P prohibitive positions.

[Luṅ](prohibitive_lung/LUNG_CONSTRUCTION.md) distinguishes sic-iṭ,
tiṅ-īṭ, the A1sg ending and bhū-vuk; historical sic-luk has different
effects under 7.3.96 and 3.4.109–110. [Laṅ](prohibitive_lung/SMA_LANG_CONSTRUCTION.md)
rebuilds thematic and owned-u endings. The [full register](prohibitive_lung/PARADIGMS.md)
retains īh's two 2pl alternatives, with the adopted and rival commentary
policies separated in [source review](prohibitive_lung/SOURCE_REVIEW.md).

[Native continuation](prohibitive_lung/NATIVE_OWNED_CONTINUATION.md)
preserves the full history carrier, addressed augment cuts and typed
zero-recovery. [Literal sources](prohibitive_lung/SOURCE_EXCERPTS.json),
[pins](prohibitive_lung/SOURCE_PINS.json) and [coverage](prohibitive_lung/COVERAGE.json)
record **731/3,983 bounded-rule IDs**; about **18.35%** is not overall
grammar completion. [Claude's T151/T152 review and handoff](prohibitive_lung/COMPANION_UPDATE.md)
credits the new kṛt work without rerunning it. [Work/frontier](prohibitive_lung/WORK_RECORD.md)
keeps tests/replay deferred and names other luṅ families, passive/bhāva
continuations and full nominal/compound coverage as remaining work.

**Conditional bhāva/karma and ciṇvat:**
[PG33](conditional_voice/README.md) adds **229 positions /448 readings**,
cumulative **11,522**. Its [domain](conditional_voice/DOMAIN_AND_ADMISSION.md)
retains independent conditional-admission and expressed-controller evidence.
[Construction](conditional_voice/CONSTRUCTION.md) and the complete symbolic
[register](conditional_voice/PARADIGMS.md) preserve sourced iṭ, ṇic-lopa,
grah i/ī, basic/causal gam and the three-way causal mit relation.
[Native continuation](conditional_voice/NATIVE_CONTINUATION.md) proves
the bounded transport and zero-reading while retaining formation history.

[Sources](conditional_voice/SOURCE_REVIEW.md), [archive](conditional_voice/SOURCE_EXCERPTS.json),
[pins](conditional_voice/SOURCE_PINS.json) and [coverage](conditional_voice/COVERAGE.json)
keep the union at **731/3,983**. Three already-authored IDs are restored
to the independent-written inventory (373); no new rule breadth is claimed.
[Claude handoff](conditional_voice/COMPANION_HANDOFF.md) records the unchanged
T152 head. [Work/frontier](conditional_voice/WORK_RECORD.md) preserves the
written-first priority and deferred tests/replay.

**Actual ciṇ in bhāva/karma luṅ:**
[PG34](cin_aorist/README.md) adds **30 positions /33 readings**, cumulative
**11,552**. [Domain](cin_aorist/DOMAIN.md) restricts the constructor to
original A3sg ta. [Construction](cin_aorist/CONSTRUCTION.md) separates
ciṇ-i, ṇic-lopa and ta-luk, original-accent guards, optional labh num
and causal mit length. The [register](cin_aorist/PARADIGMS.md) prints
all thirty-three readings; [native continuation](cin_aorist/NATIVE_CONTINUATION.md)
retains source/target histories and proves typed zero-recovery.

[Sources](cin_aorist/SOURCE_REVIEW.md), [archive](cin_aorist/SOURCE_EXCERPTS.json),
[pins](cin_aorist/SOURCE_PINS.json) and [coverage](cin_aorist/COVERAGE.json)
record **734/3,983** combined bounded-rule IDs and 381 independently
written IDs, including one explicitly identified inventory restoration.
[Handoff/work](cin_aorist/HANDOFF_AND_WORK.md) records the unchanged T152
head and deferred grammar tests/replay. Other karma luṅ slots and
ksa/aṅ/caṅ constructions remain open.

**Taddhita relations and the 1,000-ID milestone:**
[PG35](taddhita_relations/README.md) constructs **313 written rule contracts**
across all of 4.2–4.3. Combined bounded reach is **1,046/3,983** (+312,
because 4.3.120 was already in the union); independent written reach is
**694**. This is the semantic/affix-selection and owned-operation layer.
Full nominal realization is separate; the existing **11,552 finite
positions** remain unchanged.

[Domain](taddhita_relations/DOMAIN.md),
[construction](taddhita_relations/CONSTRUCTION.md) and the
[complete structured register](taddhita_relations/RULE_REGISTER.json)
retain case/meaning evidence, original affixes, gaṇa ordinals, scope,
exceptions and distinct लुक्/लुप् targets. [Native continuation](taddhita_relations/NATIVE_CONTINUATION.md)
proves dependent branching, scope separation and zero-recovery at this
selection layer. [Source decisions](taddhita_relations/SOURCE_REVIEW.md),
[literal archive](taddhita_relations/SOURCE_EXCERPTS.json),
[pins](taddhita_relations/SOURCE_PINS.json) and
[coverage](taddhita_relations/COVERAGE.json) keep the count auditable.
[Handoff/work](taddhita_relations/HANDOFF_AND_WORK.md) records the unchanged
Claude T152 head, deferred tests/replay and the remaining realization work.

**Next 300: functional taddhita contracts:**
[PG36](taddhita_functional/README.md) adds **303 contracts** across all of
4.4, all of 5.1 and 5.2.1–23. Combined bounded reach rises
**1,046 → 1,348/3,983** (+302; overlap 5.1.122); independent written
reach is **997**. Full nominal realization is separate, and **11,552
finite positions** remain unchanged.

[Domain](taddhita_functional/DOMAIN.md),
[construction](taddhita_functional/CONSTRUCTION.md) and
[register](taddhita_functional/RULE_REGISTER.json) specify case/meaning
gates, causal द्विगु, measurement and temporal types, affix identity,
dependent alternatives and addressed deletion.
[Native continuation](taddhita_functional/NATIVE_CONTINUATION.md) retains
these histories under typed zero-recovery. [Source review](taddhita_functional/SOURCE_REVIEW.md),
[archive](taddhita_functional/SOURCE_EXCERPTS.json),
[pins](taddhita_functional/SOURCE_PINS.json) and
[coverage](taddhita_functional/COVERAGE.json) preserve literal evidence,
adopted corrections, open variants and exact counts.
[Handoff/work](taddhita_functional/HANDOFF_AND_WORK.md) records unchanged
Claude T152, deferred tests/replay and that packet's frontier at **5.2.24**.

**Quality review and next 300: possession and adverbials:**
[PG37](possession_adverbials/README.md) constructs **321 contracts** for
5.2.24–140, all of 5.3 and 5.4.1–85. Eleven overlaps leave **310 new IDs**:
combined bounded reach **1,348 → 1,658/3,983**, independent written reach
**997 → 1,318**. Finite positions stay **11,552**; this remains the written
selection/operation layer, with grammar tests and replay deferred.

[Predecessor review](possession_adverbials/PREDECESSOR_REVIEW.md) checks
616 prior rows, 1,870 literal fields, 46 pinned file records and selected
semantic boundaries without claiming exhaustive correctness.
[Domain](possession_adverbials/DOMAIN.md),
[construction](possession_adverbials/CONSTRUCTION.md) and
[register](possession_adverbials/RULE_REGISTER.json) retain ordinal augment
ownership, pronominal designation, source-dependent choices, transformation
relations and compound classes.
[Native continuation](possession_adverbials/NATIVE_CONTINUATION.md) supplies
addressed-history and compound-fibre propositions with typed zero-reading.
[Source review](possession_adverbials/SOURCE_REVIEW.md),
[archive](possession_adverbials/SOURCE_EXCERPTS.json),
[pins](possession_adverbials/SOURCE_PINS.json) and
[coverage](possession_adverbials/COVERAGE.json) preserve evidence and counts.
[Handoff/work](possession_adverbials/HANDOFF_AND_WORK.md) records the
implementation requirements and next frontier at **5.4.86**.

## Read in this order

1. [Sources and editorial policy](SOURCES.md): editions, commentary attribution,
   Dhātupāṭha, Gaṇapāṭha, phonetics and the distinction from Śaiva philosophy.
2. [Sūtrapāṭha](SUTRAPATHA.tsv): all **3,983 numbered records in the pinned
   ashtadhyayi.com edition**, in Sanskrit, across all eight chapters and 32 pādas.
   This is a text catalogue; presence here does not mean operational coverage.
3. [Foundation register](FOUNDATION_REGISTER.md): selected foundational sūtras,
   Sanskrit, IAST, grammatical function, source links and scope cautions.
4. [Grammar specification](GRAMMAR_SPEC.md): inputs, inherited conditions,
   lexical dependencies, lopa, replacement, conflicts and rule-relative visibility.
5. [Worked derivations](WORKED_DERIVATIONS.md): source-grounded positive cases,
   blocked alternatives and an explicit instance of information lost by a
   surface-only representation.
6. [Coverage and completion gates](COVERAGE_AND_GATES.md): the actual T58–T80
   coverage, the complete chapter inventory and what must be resolved before
   an implementation can be described as grammar-complete.
7. [Validation](VALIDATION.md) and [source pins](SOURCE_PINS.json): what was
   actually checked and which original source bytes were retained.

## What changes in the reading of the earlier work

- **It-lopa is not pratyaya-lopa.** 1.3.2–9 designate and elide markers;
  1.1.62 concerns the disappearance of an entire affix, with the restriction
  1.1.63. Retaining a marker in a software ledger is a useful model, but is not
  itself a derivation from 1.1.62.
- **Pāṇini does not prescribe a universal numerical priority queue.** The
  Kāśikā on 1.4.2 treats equal-strength conflicts; exception relations and
  other priority conditions must be established first.
- **Asiddha is relative to a rule's view.** 8.2.1 and 6.4.22 have different
  scopes. Neither means deleting the actual derivation history.
- **The T80 place-set/Jaccard calculation is a modern finite model.** Its
  agreement with selected substitutions does not make that metric the general
  historical meaning of 1.1.50.
- **A Sanskrit case ending needs interpretation.** The locative *kartari* in
  3.1.68 is an agent/voice condition, not a following phoneme. T80's manually
  supplied records cannot be generalized by mapping every locative to a
  right-hand sound context.

These are additive reading boundaries. Earlier theorem files, result hashes
and source packets remain unchanged. Their exact finite findings remain
findings about their stated models, rather than proof of unrestricted Sanskrit
correctness. The Māheśvara phonetic sūtras are distinguished from Vasugupta's
Śivasūtras. The [SP1 research](../spanda_recognition/README.md) remains a separate
mathematical/philosophical route.

## Immediate result and next research obligation

The text inventory, foundational grammar contract, source interpretation notes
and worked controls are now available together. The next grammar work is to
close each family's inherited scopes, exceptions, lexical classes and
attested alternatives against the chosen commentary. The inventory explicitly
keeps unreviewed material open. No new Sanskrit runtime, calculator feature or
automatic parser is added by PG1.
