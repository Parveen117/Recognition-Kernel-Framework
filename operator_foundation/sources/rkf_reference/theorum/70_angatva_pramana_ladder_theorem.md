# The Six Pramāṇas of Aṅgatva (MS 3.3.14) as a Delay-Ordered Resolver

*śruti-liṅga-vākya-prakaraṇa-sthāna-samākhyānāṃ samavāye pāradaurbalyam
artha-viprakarṣāt.* The sūtra's own reason — **artha-viprakarṣa**, remoteness
of purport — is made the mechanism: a weaker pramāṇa establishes aṅgatva only
by inferring the stronger ones in turn, so each has an inferential **delay**
(śruti 0, liṅga 1, vākya 2, prakaraṇa 3, sthāna 4, samākhyā 5); resolution is
minimal delay; equal delay with different candidates is vikalpa (theorum/69).

## Instances (Bhāṣya)
- aindryā gārhapatyam upatiṣṭhate — liṅga (Indra) vs śruti (gārhapatya) → śruti.
- syonaṃ te sadanaṃ kṛṇomi — vākya vs liṅga → liṅga.
- prayāja — prakaraṇa vs vākya → vākya; prakaraṇa alone assigns to darśapūrṇamāsa.
- hautra — sthāna vs samākhyā → sthāna; samākhyā alone assigns to hotṛ.
- **Monotonicity** (T5): on every subset of every instance, removing evidence
  moves the assignment only to the next delay level — a weaker pramāṇa never
  beats a stronger present one.

## Gāyatrī
Evidences: śruti — the referencing vidhi "gāyatrīṃ japet" (sandhyā-japa);
liṅga — content *savitur … dhīmahi* → Savitṛ-rite; samākhyā — the name
*sāvitrī* → Savitṛ-rite. With the vidhi: aṅgatva = sandhyā-japa (delay 0).
Without it: liṅga and samākhyā **agree** on the Savitṛ rite (delay 1), K = 0.
theorum/69's declared "referencing vidhi" is now this resolver's śruti
evidence: **the assignment is derived; the evidences remain input.**

## Certificate
```text
python proof_lab/angatva_pramana_ladder.py
python -m unittest proof_lab.test_angatva_pramana_ladder -v
```
`PASS_ANGATVA_PRAMANA_LADDER_CANDIDATE`, SHA-256 `8a31fe5abc6966d64ebd2463882ddcf96ec6a3f0012cd37cc850ef4e77651dbe`.

## Claim boundary
```text
3.3.14 AS DELAY-ORDERED RESOLVER; BHĀṢYA INSTANCES; MONOTONICITY          PROVED
GĀYATRĪ AṄGATVA DERIVED FROM EVIDENCE (with / without the vidhi)           PROVED
EVIDENCES ARE INPUT; SUB-RULES OF EACH PRAMĀṆA NOT MODELLED                DECLARED
ARTHA OF ANY MANTRA                                                        NOT CLAIMED
RH, YM                                                                     UNTOUCHED
```
