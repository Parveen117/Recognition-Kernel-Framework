# Infinite Product of Faces as a Recognition-Complete Limit

Delivers theorum/28 §11's hypothesis list on the product carrier of
theorum/50, with exact budgets.  Primitive carrier, cut-tail mass only.

> **Audit note (ladder audit 50–59, Aug 23 2026).** T5's `sum_mu_diverges` was hard-coded True; now computed (partial sums exceed every N≤50); re-pinned.
## 1. Normalization and packets
`L̃_i = L_i/f0_i = P_i ⊕ B̃_i`, `μ_i := M_Σ(B̃_i)`.  Finite packet
`Z_n = L̃_1⊗…⊗L̃_n ⊗ P_{n+1} ⊗ P_{n+2} ⊗ …` — faces beyond `n` are **declared
recognized** (the Smriti tail).  Every `Z_n` is a finite path element of the
infinite product groupoid: a finite sum over words with finitely many minus
faces, word `w` carrying the block `⊗_{i∈w⁻} B̃_i` of mass `∏_{w⁻} μ_i`
(exactly, theorum/50 T2; re-verified against kron for `n ≤ 3`, T1).

## 2. Theorem 2.1 (recognition-complete infinite product)
Let `sup μ_i =: ρ < 1` and `Σ μ_i < ∞`.  Then:

```text
(1) recovered identity   Z_{n+1} ≡ Z_n on every sheet supported in faces ≤ n   (T2, exact)
(2) channel Cauchy       P Z_n P = P  (ρ^rec_n = 0);  M_Σ(Z_{n+1}−Z_n) = Π_n μ_{n+1},  Π_n = ∏_{i≤n}(1+μ_i)
(3) Smriti tail          tail(n) = Π_∞^bound · Σ_{k>n} μ_k  (declared, closed form, → 0)
(5) floor                Z_n P = P  exactly (floor 1)
(6) outward margin       u = ρ,  e_n = tail(n),  u + e_n < 1  for n ≥ n₀
```
Refinement only **adds** sheets (face `n+1` minus); it never alters a
present one — so the limit is sheet-wise stationary and exists in mass iff
the added-sheet masses are summable.  Certified with `μ_i = (1/2)^{i+1}` up to
`n = 12` (`n₀ = 1`).  The tail-product bound is native:
`∏(1+x_i) = Σ_k e_k(x) ≤ Σ_k s^k = 1/(1−s) ≤ 1+2s` for `s = Σx_i ≤ 1/2`,
verified on the finite instance; no exponential evaluated.

## 3. Theorem 3.1 (separation — the owner's "does not depend on m", sharpened)
```text
uniform gap (theorum/50)              ⟸  sup μ_i < 1
infinite product exists (this)        ⟸  Σ μ_i < ∞
```
Control: constant `μ_i = 1/2`.  The gap is uniform at **every** `n`
(worst memory word mass exactly `1/2`), yet
`M_Σ(Z_{n+1}−Z_n) = (3/2)^n·(1/2)` grows without bound: no mass limit, the
infinite product does not exist as a recognition-complete object.
**Uniformity of the gap is strictly weaker than existence of the infinite
product.**  "Does not depend on m" was the first; "m = ∞ exists" needs
summable badness.

## 4. theorum/28 §11 ledger (written into the certificate)
```text
1 recovered identity          DELIVERED
2 channel Cauchy bounds       DELIVERED (ρ^rec = 0 exactly; memory exact)
3 Smriti tails                DELIVERED (declared closed form, exact rational)
4 target-faithfulness         NOT APPLICABLE / NOT BUILT — no observer T declared here
5 uniform recognized floor    DELIVERED (exactly 1)
6 outward seam margin         DELIVERED (u + e_n < 1 from n₀)
```

## 5. Certificate
```text
python proof_lab/infinite_face_recognition_completion.py
python -m unittest proof_lab.test_infinite_face_recognition_completion -v
```
`PASS_INFINITE_FACE_RECOGNITION_COMPLETION_CANDIDATE`, SHA-256
`f3354b0a69fb7003aa4e7431de3d173d29310fab6a9fde0cc8e7f2289fb93057`.

## 6. Claim boundary
```text
SHEET STATIONARITY / RECOVERED IDENTITY                       PROVED
MEMORY INCREMENT LAW, DECLARED GEOMETRIC TAIL → 0              PROVED
FLOOR 1, OUTWARD MARGIN FROM n₀                               PROVED
SEPARATION sup μ < 1 vs Σ μ < ∞, DIVERGENT CONTROL             PROVED
LIMIT IN ANY TOPOLOGY OTHER THAN CUT-TAIL MASS                NOT CLAIMED
theorum/28 HYP. 4 (OBSERVER FAITHFULNESS)                     NOT BUILT
RH EVENT FAMILY, RH, YM                                       UNTOUCHED
```
