# Stem Classes for the First Śloka Line — ṛ-stem, s-stem, neuter sarvanāma — and the Gāyatrī coverage test

Owner's direction: śloka test first. Target: *tat savitur vareṇyam bhargo devasya dhīmahi*.

## New sūtras (on theorum/63's carrier type)
7.1.23 svamor napuṃsakāt (luk), **1.1.63 na lumatāṅgasya** (luk blocks
pratyaya-lakṣaṇa — 7.2.102 tyadādīnām aḥ does not fire), 8.2.39 jhalāṃ
jaśo'nte, 8.4.56 vāvasāne (pause form), 6.1.68 halṅyābbhyo… (su-lopa after
hal), 8.2.24 rāt sasya, 8.2.7 nalopaḥ, 6.1.111 ṛta ut + 1.1.51 ur aṇ
raparaḥ, 7.1.94 anaṅ, 6.4.11 upadhā-dīrgha.

## T1 Forms
savitā / savituḥ (ṛ-stem 1s/6s), bhargaḥ / bhargasaḥ (s-stem), tat (neuter
tad, 1s = 2s), devasya, vareṇyam — all = oracle. **1.1.63 is load-bearing**:
a planted tyadādyatva that ignores luk gives \*taa, not tat.
*Build notes:* (i) 8.2.39 re-fired on 8.4.56's output — within the tripādī a
later rule's output is asiddha to an earlier one (8.2.1 again); encoded for
the pair. (ii) theorum/63's ruḥ had a hard-coded exclusion on "as" that
blocked bhargasaḥ — replaced by the jit/śit feature guard; 63/64 re-pinned,
forms unchanged.

## T2 Gāyatrī line 1 — coverage
```text
tat        DERIVED   (7.1.23 luk, 1.1.63, 8.2.39, 8.4.56)
savituḥ    DERIVED   (6.1.111 + 1.1.51, 8.2.24, 8.3.15)
vareṇyam   DERIVED   (a-stem, 6.1.107)
bhargaḥ    DERIVED   (6.1.68, 8.2.66, 8.3.15)
devasya    DERIVED   (7.1.12)
dhīmahi    REFUSED   liṅ ātmanepada + chandas (3.4.6) not modelled
```
**5/6.** Inter-pada sandhi of the line (savitur v-, bhargo d-: 8.3.15 / 6.1.113–114)
is not claimed — pada-level only.

## Certificate
```text
python proof_lab/stem_classes_gayatri_coverage.py
python -m unittest proof_lab.test_stem_classes_gayatri_coverage -v
```
`PASS_STEM_CLASSES_GAYATRI_COVERAGE_CANDIDATE`, SHA-256 `6f6f988e2a6b6b19ef5c5d57654f1021093ace5d5964f763594e4cea9fff6414`.

## Claim boundary
```text
ṛ-STEM 1s/6s, s-STEM 1s/6s, NEUTER tad FROM CANONICAL SŪTRAS = ORACLE   PROVED
1.1.63 LOAD-BEARING (planted control)                                  PROVED
GĀYATRĪ LINE 1: 5/6 PADAS DERIVED, 6th REFUSED WITH SECTORS NAMED       PROVED (coverage)
FULL ṛ-/s-STEM PARADIGMS; INTER-PADA SANDHI; ĀTMANEPADA/liṅ; ACCENT     NOT CLAIMED
RH, YM                                                                 UNTOUCHED
```
