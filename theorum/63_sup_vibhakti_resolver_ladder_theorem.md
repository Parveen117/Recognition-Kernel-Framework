# Sup-Vibhakti Carrier and the Resolver Ladder (rāma paradigm, 21 forms, soundness oracle)

Owner's direction: complete the important sūtras of the grammar before moving
to Mīmāṃsā. Two pieces a grammar needs before any śloka: the **nominal sector**
(4.1.2 sup, 1.4.14 padam) and the **resolver ladder** of the paribhāṣā
*pūrva-para-nitya-antaraṅga-apavādānām uttarottaraṃ balīyaḥ* plus 8.2.1
pūrvatrāsiddham — each rung made executable on the carrier.

> **Revised the same day (theorum/64 build).** The first resolver compared every applicable rule against every other; the tiṅ carrier refused that (a saṃjñā rule 3.4.113 blocked the apavāda rung at bhū+a+anti). Resolver v2, now shared by 63/64: (1) **8.2.1 first** — while any sapādasaptādhyāyī rule is applicable, tripādī rules wait; (2) **nirvirodha** — a rule that conflicts (theorum/60 order-0 residue) with no other applicable rule is order-free and acts first; (3) among conflicting rules the **pairwise** ladder apavāda > nitya > para picks the rule that beats every rival it conflicts with; ties refused. Apavāda domains are **grammar-wide** (union over the nominal and verbal carriers) — on one paradigm alone dom(6.1.97)=dom(6.1.101) and the rung is blind. Re-pinned; 21/21 unchanged.

## Resolvers (executable)
```text
8.2.1     tripādī (8.2–8.4) rules are asiddha: an applicable earlier rule acts first
apavāda   A beats B iff dom(A) ⊊ dom(B)   (applicability sets over the PARADIGM carrier)
nitya     A beats B iff A applies before and after B while B does not survive A
para      1.4.2 later sūtra wins
antaraṅga NOT modelled
```
Ladder: 8.2.1 > apavāda > nitya > para. *Build note:* apavāda domains must be
computed over the whole paradigm carrier, not one derivation — on a single
derivation dom(6.1.107) = dom(6.1.101) and the rung is blind.

## T1 Soundness on the paradigm
All 21 forms of rāma (su…sup + sambuddhi) derived from canonical sūtras match
the declared oracle: rāmaḥ rāmau rāmāḥ rāmam rāmau rāmān rāmeṇa rāmābhyām
rāmaiḥ rāmāya rāmābhyām rāmebhyaḥ rāmāt rāmasya rāmayoḥ rāmāṇām rāme rāmeṣu
rāma. Every path passes 1.3.9.
Sūtras: 1.3.9, 6.1.69, 6.1.78, 6.1.87, 6.1.88, 6.1.101, 6.1.102, 6.1.103,
6.1.107, 6.4.3, 7.1.9, 7.1.12, 7.1.13, 7.1.54, 7.3.102, 7.3.103, 7.3.104,
8.2.66, 8.3.15, 8.3.59, 8.4.2 (+8.4.37 padāntasya block), with 4.1.2, 1.4.14,
1.3.2/3/7/8 as declarations.
*Build notes:* first run gave rāmāṇ (8.4.37 was missing), rāmebhyas (ruḥ
wrongly excluded on bhyas) — fixed from the certificate's refusals.

## T2 Memory in the nominal sector
Erasing it-marker memory breaks the ṅit/ṭit-conditioned forms (3s, 4s, 5s, 6s
at least): 7.1.12/7.1.13 go silent. 1.1.62 again load-bearing.

## T3 Resolver census — para alone is NOT enough on real data
*The draft guessed "para would agree on this carrier"; the census refused it.*
- **8.2.1 load-bearing at 8 states** (e.g. rāmās: 6.1.103 vs 8.2.66; rāmaina:
  6.1.87 vs 8.4.2) — by number the tripādī rule would win and the form would
  be wrong.
- **apavāda load-bearing at 7 states** — domain-containment pairs exhibited:
  6.1.102 ⊊ 6.1.101, 6.1.107 ⊊ 6.1.101, 7.1.12 ⊊ 6.1.101, 7.1.13 ⊊ 6.1.88,
  7.3.104 ⊊ 6.1.88, 7.3.104 ⊊ 8.2.66.
- nitya never reached on this paradigm (present, untested by data).
- Planted control: 6.1.107 renumbered earlier than 6.1.101 → ladder still
  gives rāmam, para-only gives rāmām.

## T4 8.2.1 on every path
ruḥ / visarga / ṇatva / ṣatva never act before a sapādasaptādhyāyī rule.

## T5 No invented forms
Every ladder normal form is a free normal form of the system.

## Certificate
```text
python proof_lab/sup_vibhakti_resolver_ladder.py
python -m unittest proof_lab.test_sup_vibhakti_resolver_ladder -v
```
`PASS_SUP_VIBHAKTI_RESOLVER_LADDER_CANDIDATE`, SHA-256 `49671feae1f92cd65fac0fe37fb109f128f4dc38e5cfb3dd69e13a3bdabc6d31`.

## Claim boundary
```text
21/21 rāma FORMS FROM CANONICAL SŪTRAS = ORACLE (soundness on paradigm)     PROVED
MEMORY LOAD-BEARING (ṅit/ṭit forms)                                        PROVED
apavāda = DOMAIN CONTAINMENT, EXECUTABLE; 8.2.1 + apavāda LOAD-BEARING      PROVED (census)
para ALONE INSUFFICIENT ON REAL DATA                                       PROVED (15 states)
nitya RUNG                                                                 PRESENT, NOT EXERCISED
antaraṅga/bahiraṅga; ACCENT; OTHER STEM CLASSES; FEM/NEUTER                NOT MODELLED
COMPLETENESS OF THE AṢṬĀDHYĀYĪ                                             NOT CLAIMED (27 sūtras)
RH, YM                                                                     UNTOUCHED
```
