# Mīmāṃsā Carrier — obligation closure on the kāraka frame

Source: owner's Vedic repo `VRG_Mimamsa_Rule_Priority_Interpretation_Engine_v1.tex`
(R = (type, agent, action, object, condition, authority); vidhi → obligation;
niṣedha → prohibition closure; Exception / Conflict / Scope Smṛti; authority
scale; Ṛta closure K_M(R) = 0; "written rule ≠ closed obligation"). Made
executable on a finite situation carrier, with Mīmāṃsā's own resolver:
```text
scope      sāmānya-viśeṣayor viśeṣo balīyān — cond(A) ⊊ cond(B) on the carrier   (= theorum/63 apavāda rung)
authority  1.3.3 virodhe tv anapekṣyaṃ syāt — śruti > smṛti > ācāra
vikalpa    tulya-bala-virodhe vikalpaḥ — equal strength → lawful OPTION
```
One structural difference from the Pāṇinian ladder: **a tie is a closure,
not a refusal** — it is recorded in the ledger as an option. K_M counts only
unresolved contradictions.

## Instances (classical)
- **T1** na hiṃsyāt (niṣedha, general) vs agnīṣomīyaṃ paśum ālabheta (vidhi,
  specific) → scope; the vidhi stands, Exception-Smṛti recorded, K_M = 0.
- **T2** vrīhibhir / yavair yajeta (same scope, same authority) → vikalpa, K_M = 0.
- **T3** audumbarī: śruti veṣṭana vs smṛti sparśa → authority, śruti stands;
  planted equal authority → vikalpa instead.
- **T4** two śruti statements, same scope, contradictory, single non-repeatable
  performance (no vikalpa) → **K_M = 1**, witness returned. Closure is not
  assumed.

## T5 Gāyatrī
Classified from its **own grammar**: dhīmahi is āśīrliṅ uttama puruṣa
(theorum/66) — the speaker's wish, not an injunction to another → type
**mantra** → no obligation by itself. With a referencing vidhi (smṛti,
"gāyatrīṃ japet", dvija, sandhyā) the closure contains exactly the japa
obligation, whose object is the mantra and whose kāraka frame is theorum/68's.
Its *meaning* is not claimed; its normative status is.

## Certificate
```text
python proof_lab/mimamsa_obligation_closure.py
python -m unittest proof_lab.test_mimamsa_obligation_closure -v
```
`PASS_MIMAMSA_OBLIGATION_CLOSURE_CANDIDATE`, SHA-256 `294e7e927c1f3b2989ff8f23e801fa98341bd0986b584caa471a084b8f87a127`.

## Claim boundary
```text
OWNER'S MĪMĀṂSĀ KERNEL EXECUTABLE; K_M CLOSURE COMPUTED, NOT ASSUMED        PROVED
RESOLVER = 63's LADDER SHAPE; TIE = LAWFUL vikalpa                          PROVED (instances)
GĀYATRĪ = MANTRA BY ITS LAKĀRA; OBLIGATION ONLY VIA A REFERENCING VIDHI     PROVED
SIX aṅgatva PRAMĀṆAS (3.3.14); ARTHA OF ANY STATEMENT                       NOT MODELLED / NOT CLAIMED
STATEMENT SET AND CONDITION FEATURES ARE DECLARED INPUT                    DECLARED
RH, YM                                                                     UNTOUCHED
```
