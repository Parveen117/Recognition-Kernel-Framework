# Scope Exclusions and False-Positive Audit

This archive includes only results whose mathematical content is genuinely thermodynamic-response, Onsager, susceptibility, entropy-production, or thermodynamic-curvature based.

## 1. Eta-descent margin barrier

The MP file

```text
proof_lab/clock_free_recognition/ETA_DESCENT_MARGIN_BARRIER.md
```

proves a certificate-descent obstruction. If

\[
\eta_{j+1}=\frac{\eta_j}{1+q_j}
\]

and

\[
\sum_j\log(1+q_j)<\infty,
\]

then

\[
\eta_\infty
=\eta_0\prod_j(1+q_j)^{-1}>0.
\]

This is a convergence/certificate theorem, not a thermodynamics theorem. It is related only because a direct thermodynamic response-curvature identity was proposed as one possible alternative to repeated eta descent.

## 2. Native energy-channel exterior rates

The MP file

```text
papers/rh_initial_journey/NATIVE_ENERGY_CHANNEL_EXTERIOR_RATES.md
```

uses the word `energy` for operator and source-channel norms. Its exponential exterior estimates concern multiplicative carriers, prime dilations, Gamma channels, and finite-rank augmentation. They are functional-analytic energy estimates, not caloric or thermodynamic energy laws.

## 3. Raw Hessian positivity

The raw Hessian of a thermodynamic potential is not automatically a positive response metric in the chosen coordinates. For example, on a stable material,

\[
\frac1S\left(\frac{\partial V}{\partial P}\right)_S
=-\frac{V}{SK_S}<0.
\]

Therefore this archive uses a positive metric obtained from stable susceptibilities or compatibility-Gram whitening. It does not import an indefinite raw Hessian as a Riemannian metric.

## 4. Smooth-scalar curvature warning

A smooth scalar potential has commuting mixed partial derivatives. Path dependence alone does not make its Hessian noncommutative. Nonzero curvature requires a non-exact connection, singular structure, non-smoothness, or an explicitly operator-valued transport law.

## 5. Speculative extensions

Claims involving quantum field theory, gauge unification, gravity, black holes, or cosmology are not part of this theorem archive unless separately derived from declared Recognition Kernel objects and proved with typed source maps.

## Claim boundary

```text
ETA-DESCENT BARRIER                         EXCLUDED: NOT THERMODYNAMICS
OPERATOR ENERGY EXTERIOR RATES              EXCLUDED: NOT THERMODYNAMICS
RAW HESSIAN AS AUTOMATIC POSITIVE METRIC    REJECTED
PATH DEPENDENCE AS SMOOTH-SCALAR CURVATURE  REJECTED
SPECULATIVE QFT / GRAVITY EXTENSIONS        QUARANTINED
```
