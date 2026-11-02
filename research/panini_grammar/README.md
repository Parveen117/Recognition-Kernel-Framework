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
