# Generalized Euler / EMK Dock (binding the exchange law to R, K, RK)

Closes the three "same shape, dock open" items left by theorum/51 and
theorum/53, on the EMK 2×2 primitives of theorum/48 (`I, K, R, RK`) embedded
in `C_Σ`.  Primitive carrier; exact algebra; nothing Hilbert.

## T1 Which EMK elements generate the flow
Anti-self-dagger (theorum/51) generators inside the EMK span:
`R` is the pure **even** (B-type, real antisymmetric) generator; `ιI, ιK, ιRK`
are the pure **odd** (A-type, turn-symmetric) generators; `K, RK, I` alone are
not flow generators.  The dagger grading and theorum/48's `J_E := K` grading
are certified **different** (`R` is K-odd but dagger-even; `ιK` is K-even but
dagger-odd) — two gradings, not one.

## T2 Dock (a): the GE connection obeys the exchange law
For `D = αR + ιβK` (de4 §4, `∇^{RK} = ∇ + αR + βK + Γ_μ`, `Γ_μ` declared
residue):
```text
rad  ←  α[R_S, R] + β[K, T]
turn ←  α[T, R]   + β[R_S, K]
```
**Lawful phase rotation `αR` acts by commutator inside each channel; seam
transport `βK` (carrying turn) exchanges the channels.**  Exact on random
cut squares.  This is the binding that lets theorum/51 be read as the DE
transport law.

## T3 Dock (b): the RK mixed channel is the loop residue
`[αR, ιβK] = 2ιαβ·RK` exactly (EMK bracket `[R,K] = 2RK`), and the Cayley
commutator loop of the two flows has residual `loop − I − h²[D₁,D₂]` whose
mass scales cubically on dyadic `h ∈ [1/512, 1/16]` (ratio ≤ 1/6 per halving;
commuting control `loop = I` exactly).  de4's "mixed phase–seam event" is the
leading non-commutativity of composing R-flow and K-flow.  *Build note:* the
first draft tested `h = 1/2..1/8` with generator mass ≈ 3 — outside the
asymptotic range — and was refused; the certified window is stated.

## T4 Dock (c): EMK-1's determinant channels are an exchange pair
For `M = aI + bK + cR + dRK`: `det(M†★M) = (Δ∥ + Δ⊥)²` exactly.  Under the
rational R-flow `M ↦ M·C_h(R)` (no trigonometry) the **total** `Δ∥ + Δ⊥` is
invariant (theorum/53 T6) while `Δ∥` and `Δ⊥` individually **exchange**.
EMK-1's additive split is the channel pair of theorum/51; their sum is the
flow invariant.

## T5 GE false-residue prevention, executable
`residue(S→S′; α,β) = S′ − transport_{α,β}(S)`.  A lawful transition is closed
under its declared pair only (open under all 24 other grid pairs); an
unlawful transition is open under every pair — de4's "lawful motion before
error" as a verdict, not a principle.

## Certificate
```text
python proof_lab/generalized_euler_emk_dock.py
python -m unittest proof_lab.test_generalized_euler_emk_dock -v
```
`PASS_GENERALIZED_EULER_EMK_DOCK_CANDIDATE`, SHA-256
`bcddc7a3a622deae64a469489e39eeaf9ed72f093d3f2e71beb1323a045d4a7c`.

## Claim boundary
```text
EMK FLOW GENERATORS, TWO GRADINGS SEPARATED                      PROVED
DOCK (a) GE CONNECTION ⟹ EXCHANGE LAW                            PROVED
DOCK (b) RK BRACKET = LEADING LOOP RESIDUE (dyadic window)       PROVED / SCALING WITNESSED
DOCK (c) Δ∥+Δ⊥ INVARIANT, Δ∥,Δ⊥ EXCHANGE                          PROVED
GE FALSE-RESIDUE VERDICT                                         PROVED
EXACT ORDER-3 LOOP IDENTITY                                      NOT CLAIMED
Γ_μ MODELLED / PHYSICAL REALIZATION UNIQUE                       NOT CLAIMED
GE MEASUREMENT / BORN / DEVICES                                  NOT TOUCHED
RH, YM                                                           UNTOUCHED
```

With this dock in place, the theorum/51 law carries its name honestly:
**the Aghora exchange law** — odd sector created from and returned to the even
sector by seam transport, phase rotation leaving each sector to itself.
