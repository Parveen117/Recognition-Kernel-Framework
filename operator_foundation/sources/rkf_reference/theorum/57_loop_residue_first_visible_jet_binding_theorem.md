# Loop-Residue / First-Visible-Jet Binding (Γ_μ resolved as a seam quotient)

Binds the declared residue `Γ_μ` of theorum/55 (the Cayley commutator loop of
the R-flow and the K-flow, `∇^{RK} = ∇ + αR + βK + Γ_μ`, de4 §4) to the
first-visible-jet seam quotient of theorum/46.  The declared seam is the flow
step `h`; the carrier is `C_Σ` (theorum/50 scalars); the steps are the Cayley
steps of theorum/51.  Primitive carrier; exact algebra; nothing Hilbert.

> **Audit note (ladder audit 50–59, Aug 23 2026).** Renaming test (TAUT-1 R1): a₂=[D₁,D₂] and a₃=½[D₁+D₂,[D₁,D₂]] hold for ARBITRARY matrices — they are lemmas about the Cayley map, not odd-sector content. Carrier content here is the typing of Γ as a 46 seam observable, the false-residue rule (visible before order 2), and the EMK evaluation 2ιαβRK.
## Seam observable
`Γ(h) := loop(h) − I`, `loop(h) = C_h(D₁) C_h(D₂) C_h(D₁)⁻¹ C_h(D₂)⁻¹`.
Jets are computed in the exact truncated ring `C_Σ[h]/h⁵`: `(I − hD/2)⁻¹` is
the terminating geometric series of the nilpotent jet `hD/2` (native
approximant shape, F00E), so every jet coefficient `a_k` is an exact `C_Σ`
matrix — theorum/45 zero arithmetic radius, no remainder hypothesis to admit.

## T1 Γ ⊙_S h² = [D₁, D₂]
`Γ(0) = 0` (46 (2.1)); `a₀ = a₁ = 0`, `a₂ = [D₁, D₂]` exactly (EMK pair and
random anti-self-dagger generators, n = 2, 3).  With denominator `B(h) = h²`
(`b₂ = 1 ≠ 0`), theorum/46 Thm 3.1 case 2 — applied entry by entry, rad and
turn channel, through 46's own classifier — gives
```text
Γ ⊙_S h²  =  [D₁, D₂]  =  2ιαβ·RK          FINITE_SEAM_QUOTIENT
Γ vs h¹                                     FINITE_QUOTIENT_ZERO
Γ vs h³                                     DIVERGENT_NO_FINITE_QUOTIENT
```
theorum/55 T3's "RK channel is the leading loop residue, cubic scaling on a
dyadic window" is now an exact jet identity, not a scaling witness.

## T2 Exact order-3 loop identity (theorum/55's refused item)
```text
a₃ = ½ [D₁ + D₂, [D₁, D₂]]
```
exact on random anti-self-dagger generators (n = 2, 3, 4); on the EMK pair
`a₃ = 2αβ²·R − 2ια²β·K` (e.g. α=2, β=3: `36R − 24ιK`).  The residual
`loop − I − h²a₂ − h³a₃` has first-visible order ≥ 4 — this is what 55's
ratio ≤ 1/6 per halving was seeing.  Reading: the second-order residue is the
bracket transported by the *sum* generator, i.e. the exchange residue
`[R, K]` is itself exchanged once more by `αR + ιβK`.

## T3 The seam is part of the type (46 §4, Thm 5.1)
Regular reparameterization `h = c·s` (`c = 2, −1/3, 7/5`): leading jets scale
by `c²` on both sides, quotient invariant.  Non-regular seam `h = s²`
(`φ′(0) = 0`): `Γ(s²)` has first-visible order 4, verdict against `s²`
becomes `FINITE_QUOTIENT_ZERO` — a different seam is a different quotient.

## T4 False residue = residue visible before the bracket order
theorum/55 T5's verdict restated in jet order:
```text
flow-generated (lawful)  ⟺  first-visible order ≥ 2  and  a₂ = [D₁, D₂]
planted order-0 obstruction (55's unlawful perturbation)   DIVERGENT vs h²
planted order-1 drift (a generator entering at order 1)    DIVERGENT vs h²
```
Commuting control (`αR` vs `ιγI`): all jets zero to depth 4 **and** exact
identity `loop = I` at five rational `h` — recorded as
`IDENTICALLY_ZERO_BY_EXACT_ALGEBRA`, kept distinct from 46's
`INCOMPLETE_FLAT_OR_UNRESOLVED` (46 §8: zero jets alone do not decide; here
the exact algebra does).

## T5 Corroboration against the exact loop
`loop(h) − P₄(h)` (theorum/55's exact rational loop minus the jet polynomial)
halves by ≤ 1/2⁵ per halving on `h ∈ [1/512, 1/16]`; jets of `C(D)` and
`C(−D)` are mutually inverse in the jet ring.

## Certificate
```text
python proof_lab/loop_residue_first_visible_jet_binding.py
python -m unittest proof_lab.test_loop_residue_first_visible_jet_binding -v
```
`PASS_LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_CANDIDATE`, SHA-256
`712c272d3e1a1d1dadc869045130226f42da11f1ca20b6c98584305234e502a6`.

## Claim boundary
```text
Γ = loop − I IS A 46 SEAM OBSERVABLE, Γ ⊙_S h² = [D₁,D₂] = 2ιαβRK        PROVED
EXACT ORDER-3 LOOP IDENTITY a₃ = ½[D₁+D₂,[D₁,D₂]]                       PROVED
REGULAR REPARAMETERIZATION INVARIANCE; NON-REGULAR SEAM CHANGES VERDICT  PROVED
FALSE RESIDUE ⟺ VISIBLE BEFORE ORDER 2 (planted order 0, 1 DIVERGENT)     PROVED
COMMUTING CONTROL IDENTICALLY ZERO BY EXACT ALGEBRA                      PROVED
CLOSED FORM FOR a₄ / ALL-ORDERS SERIES                                   NOT CLAIMED
SEAM-INVARIANCE ACROSS GENUINELY DIFFERENT SEAMS (46's own boundary)      NOT CLAIMED
Γ_μ HAS NO COMPONENT BEYOND THE LOOP RESIDUE                             NOT CLAIMED
RH, YM                                                                   UNTOUCHED
```
The binding types the loop residual as **the 46-resolvable part** of the
declared residue `Γ_μ`: its value is not declared, it is the seam quotient
`[D₁, D₂]`.  Any further declared term in `Γ_μ` remains declared.
