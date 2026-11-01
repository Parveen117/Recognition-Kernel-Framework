# Sanskrit grammar coverage after PG7

Author: Monty. 1 November 2026.

**The full grammar is still largely open. There is no defensible single
completion percentage yet.** The reproducible [coverage audit](COVERAGE_STATUS.json)
keeps text, rule contracts, root preprocessing and complete word paths separate.
It reads predecessor reports without replaying their certificates.

| Layer | What is actually present | What that leaves open |
| --- | --- | --- |
| Sūtrapāṭha | 3,983 records, 8 chapters, 32 pādas, catalogued in the pinned edition | Text inclusion is not interpretation or execution; replacing the historical 3,959 denominator is not a full cross-edition concordance |
| PG4–PG7 source-bound records | 86 record definitions referring to **80 distinct sūtra IDs** | Bounded contracts, including local visibility obligations; 3,903 inventory IDs have no record in these four packets, although some have earlier notes/contracts/code |
| Historical review-branch ledger | Baseline snapshot: 171 declarations (10 compiled, 70 hand-coded, 46 meta, 43 cited, 2 misnumbered) | Historical labels, not current companion-branch totals or independently verified coverage; they cannot simply be added to the 80 IDs |
| Scope | 23,589 publisher edges audited; bounded commentary decisions applied | Raw Sanskrit scope inference, general priority and general visibility remain open |
| Root preprocessing | 2,229 root entries; frozen PG4 comparison has 2,219 agreements, 8 differences, 2 unresolved | Headword agreement does not provide conjugations or a Sanskrit soundness oracle |
| Complete PG5–PG7 laṭ profile | **46 root entries**, 67 pada paradigms, **603 cells**, **695 branches** | **2,183 root entries** have no complete path in this PG generator; other lakāras and contexts remain open |

The narrow root-entry fraction is **46 / 2,229 ≈ 2.064%**. Its complement is
about 97.936% **of root entries without this complete PG laṭ path**, not a
measurement of the percentage of Sanskrit grammar unverified. In particular,
the preprocessing and shared rules already cover more than those 46 entries.
Conversely, closing one present paradigm does not close all grammar of that root.

PG5 contributes 13 roots / 162 cells, PG6 adds 10 / 153, and PG7 adds 23 / 288.
The completed lexical ID sets are disjoint. There are completed examples in
eight gaṇas, but no claim that eight entire gaṇas are closed. Adādi (class 2)
and juhotyādi (class 3) still lack complete paths in this generator.

The concurrent [theorem branch at 7802a35](CONCURRENT_THEOREM_SNAPSHOT.json)
has an updated **187-entry ledger** using the 3,983-record edition, with
zero reported missing pinned IDs or curated IAST mismatches. Its **T86**
reports **11 kta stems and 242 nominal outputs** through the bounded T63
ladder. The capsule, code and ledger were read; their certificates were not
replayed. This progress is preserved separately, not omitted or added to the
603 verb cells. Aniṭ is declared there, and hu remains nāma-only rather than
a completed PG present-root path. No merge of that branch is included in PG7.

## The major remaining packages

- **Verb grammar:** remaining present roots, the two excluded class-7 entries,
  reduplication, sense/pada and prefix interactions; other lakāras, voices,
  augments, iṭ and derived verbal stems.
- **Nominal grammar:** full stem and gender classes, pronouns, numerals and
  irregular paradigms beyond the bounded T63/T86 examples and related packets.
- **Derivation and syntax:** kṛt, taddhita, samāsa, semantic selection,
  kāraka relations and agreement.
- **General interpretation:** adhikāra/anuvṛtti inference from text, general
  apavāda/nitya/antaraṅga resolution, 1.1.56–59 and 6.4.22 visibility, and
  complete sound-rule exceptions.
- **Lexica and validation:** gaṇa/Uṇādi semantics, independent editions and
  corpus evidence, accent/Vedic domains, soundness and completeness.

The earlier “90%+ pending” concern cannot be replaced with an optimistic
completion percentage from example counts. Future progress should be tracked
by explicitly closed rule domains, lexical/pada/lakāra matrices and independent
evidence. Quantum-calculator integration retains its separate operator-family
and zero-specialization obligations.
