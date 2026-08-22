# Ātmanepada Sector — laṭ of edh and labh (18 forms); dhīmahi's honest status; two ladder findings

## T1 Soundness
18/18: edhate edhete edhante edhase edhethe edhadhve edhe edhāvahe edhāmahe;
labhate labhete labhante labhase labhethe labhadhve labhe labhāvahe labhāmahe.
Sūtras added: 1.3.12 (declared), 3.4.78 ātmanepada tiṅ, **3.4.79 ṭita
ātmanepadānāṃ ṭer e**, 3.4.80 thāsaḥ se, **7.2.81 āto ṅitaḥ**, 6.1.66 lopo
vyor vali, 6.1.87 at the seam.

*Build notes (certificate refusals):* "ṭitaḥ" in 3.4.79 was first read as the
ending being ṭit → edhadhvam; the sūtra qualifies the **lakāra** (laṬ) →
edhadhve. 3.4.80 was missing (edhathe → edhase).

## T2 Chain 7.2.81 → 6.1.66 → 6.1.87 is load-bearing
Dual forms: ātām → iy-ātām → y-lopa → guṇa → edhete. Without 6.1.66: \*edheyte.

## Two findings about the resolver ladder (both recorded in theorum/63's resolver)
1. **Containment-apavāda is blind for 6.1.97 on this carrier.** edha+e (1s,
   via ṭer e) is in dom(6.1.97) but not in dom(6.1.101), so 6.1.97 ⊄ 6.1.101
   even grammar-wide — and para then gives \*edhānte. The tradition's
   relation is *yena nāprāpte yo vidhir ārabhyate sa tasya bādhakaḥ*: 6.1.97
   is enacted for a+a which 6.1.101 already covers (Kāśikā ad 6.1.97). This is
   a **declared** bādhaka relation, not a computed one. Added as a named rung
   `apavāda(declared)` with its source; theorum/64's computed containment
   held there only because a+e never occurred. Declared relations are listed
   in one place (`DECLARED_BADHAKA`) so the claim boundary is visible.
2. **The antaraṅga rung is missing and it shows.** 1s: iṭ → the engine applies
   6.1.87 guṇa on a+i before 3.4.79 (para); the tradition applies ṭer e first
   because it depends only on the lakāra (antaraṅga) while guṇa depends on the
   seam. The **form coincides** (edhe), the **path does not**. Recorded as a
   check, not hidden.

## dhīmahi — still REFUSED, now with the reason
The Vedic form needs *chandasi bahulam* / vyatyaya to suppress the juhotyādi
ślu-reduplication of dhā (classical vidhiliṅ 1p = dadhīmahi). A "bahulam"
rule has no deterministic domain, so no certificate can produce dhīmahi as a
unique normal form. Pieces that are sūtra-deterministic: the ending is 3.4.78
mahiṅ (liṅ is not ṭit, so no ṭer e); ā → ī is 6.4.66 ghumāsthā… hali.
Gāyatrī line 1 therefore stays at 5/6 **by the grammar's own admission**.

## Certificate
```text
python proof_lab/lat_atmanepada.py
python -m unittest proof_lab.test_lat_atmanepada -v
```
`PASS_LAT_ATMANEPADA_CANDIDATE`, SHA-256 `2ab0cf226c593e1533f38b4c466db17fa8246d913d9826f42c81a465a4e9aa23`.

## Claim boundary
```text
18/18 laṭ ĀTMANEPADA FORMS (edh, labh) = ORACLE                              PROVED
7.2.81 → 6.1.66 → 6.1.87 CHAIN LOAD-BEARING                                PROVED
6.1.97 ⊐ 6.1.101 NOT COMPUTABLE BY CONTAINMENT; DECLARED BĀDHAKA RUNG     PROVED (finding) / DECLARED
ANTARAṄGA RUNG MISSING (1s path), FORM COINCIDES                           RECORDED
dhīmahi                                                                    REFUSED (chandasi bahulam)
liṅ/laṅ/lṛṭ; NON-a AṄGAS (7.1.5); ACCENT                                   NOT CLAIMED
RH, YM                                                                     UNTOUCHED
```
