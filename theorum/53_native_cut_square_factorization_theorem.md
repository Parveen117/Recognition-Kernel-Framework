# Native Cut-Square Factorization (replacement for the spectral theorem)

Primitive carrier of theorum/50; exact inverse theorum/51; resolvent region
theorum/52.  On a Hilbert space the spectral theorem diagonalizes `L†L` into
eigenvalues.  On the primitive carrier the object is not eigenvalues but
**weighted native squares**:

```text
S = L†★L  (self-dagger)   =   C†★Dg★C   =   Σ_k d_k · c_k†★c_k
```

with `d_k ∈ R_Σ` turn-free, `C` unit upper triangular over `K_Σ`, computed by
exact elimination with the native scalar inverse — no square root, no inner
product, no eigenvalue.

## Certified

- **T1 Existence/separation.** Every cut square factors exactly; all weights
  turn-free and nonnegative.  Rebuilding `S` from the *radial parts* of the
  factors with the same weights kills the odd channel: **the odd sector
  (Aghora) lives entirely in the phases of the squares; positivity lives
  entirely in the weights.**
- **T2 Native Parseval.** `E_Σ(L) = tr rad(S) = Σ_k d_k E_Σ(c_k)` exactly.
- **T3 Negative witness.** A self-dagger non-square yields a negative weight
  and an exact vector `v` with `v†★T★v` negative radial, turn-free (SOS-1's
  witness, native); a zero pivot with a nonzero row is refused.
- **T4 Seam faces.** Factorization splits along `P ⊕ Q`; recognized weight
  exactly `f0²`; every memory weight obeys
  `d_k ≤ S_kk ≤ E_Σ(B) ≤ M_Σ(B)² ≤ (ρf0)²` — pivots are Schur complements,
  bounded by the diagonal they refine.  The seam gap is visible **weight by
  weight**.  *Build note:* a first draft claimed an individual weight could
  exceed the bound; the certificate refused it; the corrected, stronger
  statement is what is certified.
- **T5 Product.** `S_ab = S_a ⊗ S_b` and the factorization tensors exactly
  (`C_ab = C_a⊗C_b`, `Dg_ab = Dg_a⊗Dg_b`); the odd channel is theorum/50's
  Leibniz law read through the factor phases.
- **T6 Flow invariant.** Under theorum/51's unitary Cayley step the
  individual weights change, but `∏ d_k = det S` (radial) is exactly
  invariant — the native determinant channel is the flow invariant of the
  square (EMK-1 determinant-identity shape; dock open).

## Certificate
```text
python proof_lab/native_cut_square_factorization.py
python -m unittest proof_lab.test_native_cut_square_factorization -v
```
`PASS_NATIVE_CUT_SQUARE_FACTORIZATION_CANDIDATE`, SHA-256
`2079f98d0aa2565ec99c8b33ee3fd21c024a919aad65d5e2e2b8193f20ddc725`.

## Claim boundary
```text
EXACT FACTORIZATION, TURN-FREE NONNEGATIVE WEIGHTS, ODD IN PHASES     PROVED
NATIVE PARSEVAL                                                       PROVED
NEGATIVE WITNESS / REFUSAL OF NON-SQUARES                             PROVED
SEAM FACES: WEIGHTS BOUNDED BY (ρf0)² WEIGHT BY WEIGHT                PROVED
PRODUCT TENSORS EXACTLY                                               PROVED
det S = ∏ WEIGHTS FLOW-INVARIANT                                      PROVED
UNIQUENESS OF THE FACTORIZATION                                       NOT CLAIMED (basis-ordered)
WEIGHTS = EIGENVALUES                                                 NOT CLAIMED
det S ≡ EMK-1 DETERMINANT CHANNEL                                     DOCK OPEN
RH, YM                                                                UNTOUCHED
```
