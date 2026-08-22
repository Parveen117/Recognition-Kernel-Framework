# Native Seam Resolvent and Spectral Region (no inner product)

Primitive carrier of theorum/50; exact inverse over `C_Σ` of theorum/51.
The classical pair (resolvent, spectrum) is rebuilt from three framework
tools only: T01 Thm 2.2 / Lemma 2.1 (mass and gauge submultiplicativity),
theorum/28 §3–4 (recognition-Cauchy with *declared* Smriti tails), and exact
`K_Σ` field arithmetic.  No eigenvalue is approximated anywhere.

## 1. Definitions

```text
mass-Neumann ratio       q(λ)   = M_Σ(L)·D_Σ(λ)/N_Σ(λ)           (= M_Σ(L)·D_Σ(λ⁻¹))
partial resolvent        R_N(λ) = λ⁻¹ Σ_{k≤N} (λ⁻¹L)^k
declared Smriti tail     τ_N    = D_Σ(λ⁻¹)·q^{N+1}/(1−q)
certified resolvent set  {λ : q(λ) < 1}   (or q_k(λ) = M(L^k)D(λ)^k/N(λ)^k < 1)
native singular locus    det_{K_Σ}(λI − L) = 0                   (exact)
```

## 2. Theorem 2.1 (recognition-complete resolvent)
Where `q(λ) < 1`, the exact inverse `(λI − L)⁻¹` exists and
`M_Σ((λI−L)⁻¹ − R_N(λ)) ≤ τ_N` for every `N`, `τ_N → 0` geometrically.
The partial resolvents are a recognition-Cauchy sequence with declared
tails — theorum/28 §3–4's hypotheses *delivered with budgets*, not asserted.
Proof: `M((λ⁻¹L)^k) ≤ q^k` by Lemma 2.1 + Thm 2.2; sum the geometric tail. ∎
(Certified N = 0..6 on 10 instances; a budget declared with `q/2` is violated.)

## 3. Theorem 3.1 (seam gap = native spectral region)
For a seam-compatible face `L = f0 P ⊕ B` with `M_Σ(B) ≤ ρ f0`:

```text
det(λI − L) = (λ − f0)·det(λI − B)                            (exact)
N_Σ(λ) > ρ f0 D_Σ(λ)   ⇒   λ regular for B
```

so the singular locus of `L` is `{f0} ∪ (a subset of G_ρ)`, with the
**native gap region** `G_ρ = {λ : N_Σ(λ) ≤ ρ f0 D_Σ(λ)}`, and `f0 ∉ G_ρ`.
On the radial axis `G_ρ` is exactly `|t| ≤ ρ f0`; off-axis it is the
framework's own shape (a `D`-gauge region, not a disk).  Certified on the
three flow faces of theorum/50 over a 17×17 grid of `K_Σ` points.

## 4. Further certified facts
- **Exact locus (T3).** Triangular memory block: characteristic polynomial
  over `K_Σ` (Faddeev–LeVerrier, exact) factors as `∏(λ − b_ii)`; each root
  singular, grid elsewhere regular.  A non-triangular block with
  `λ² − 2` shows the locus need not lie in `K_Σ`: then only the region
  statement is made — never a located root.
- **Powers sharpen (T4).** `q₁ ≥ 1` but `q₂ < 1` with an exact resolvent
  recovered through the `L²`-Neumann route `(λ−L)⁻¹ = (λ+L)(λ²−L²)⁻¹`:
  the certified region shrinks with powers, from Thm 2.2 alone.
- **Product (T5).** `f0^m` singular and isolated; every memory sheet is
  regular outside `G_ρ` at scale `f0^m` for `m = 1..3` (consumes
  theorum/50's exact sheet-mass law, so uniform in `m`); the product
  resolvent is sheet-block-diagonal but **not** a tensor product of face
  resolvents (control) — like the Cayley step in theorum/51, the resolvent
  is not local even though the generator is.

## 5. Certificate
```text
python proof_lab/native_seam_resolvent.py
python -m unittest proof_lab.test_native_seam_resolvent -v
```
`PASS_NATIVE_SEAM_RESOLVENT_CANDIDATE`, SHA-256
`c813f2a4797ebdf426ebe84309d87fe6ad177e23e85828c2050fda23d9242afe`.
Source-guarded against Hilbert verdicts.

## 6. Claim boundary
```text
MASS-NEUMANN RESOLVENT WITH DECLARED GEOMETRIC SMRITI TAILS          PROVED
det FACTORIZATION + NATIVE GAP REGION G_ρ, f0 OUTSIDE                PROVED
EXACT SINGULAR LOCUS (TRIANGULAR), REGION-ONLY OTHERWISE             PROVED / DECLARED
POWER-SHARPENED REGION                                               PROVED
PRODUCT LOCUS UNIFORM IN m, RESOLVENT NON-LOCAL                      PROVED (m ≤ 3)
SHARPNESS OF G_ρ                                                     NOT CLAIMED
LOCATION OF ROOTS OUTSIDE K_Σ                                        NOT CLAIMED
COMPLEX-ANALYTIC RESOLVENT PROPERTIES                                NOT CLAIMED
RH, YM                                                               UNTOUCHED
```
