# Clock-Free Cut-Memory Development Plan

## Governing rule

Recognition-Seam Calculus is the foundation.

```text
No external clock defines the derivative.
No classical operator decomposition defines the native objects.
No target matrix is fitted after the sign is known.
```

Classical operator algebra and spectral theory may be consulted only as a
shadow: they suggest the shape of a map after the cut-derived construction has
already produced it.

---

## Stage 1: generalized clock-free examples

### Written objects

```text
theorum/24_clock_free_recognition_seam_cut_calculus.md
proof_lab/clock_free_cut_memory_general_example.py
```

### Exact examples

1. nonlinear phase-seam holonomy with local closure and global memory;
2. nonzero composition residue from cut-corner multiplication;
3. target-blind stable repair with memory ranks 2 -> 1 -> 2;
4. cut-generated five-memory packet with exact finite seam reduction.

### Stage-1 claim boundary

```text
GENERAL CALCULUS AND EXAMPLES       WRITTEN
EXACT TEST SUITE                    NEXT STAGE
RH EVENT LIFT                       NOT STARTED
RH CERTIFICATE                      NOT CLAIMED
```

---

## Stage 2: exact theorem tests

Write a fail-closed test module for:

```text
transition differential;
composition-residue identities;
clock-free chain rule;
local ledger closure;
nonzero loop holonomy;
stable repair index additivity;
cut decomposition S=R+D;
target-faithful rank <= 5;
full/five-matrix inertia equality;
relative-gap equality;
threshold-kernel equality;
positive-determinant negative control.
```

Freeze one deterministic JSON packet only after all exact tests pass.

---

## Stage 3: native completed-Weil event lift

Construct the RH specialization from the cut:

\[
Z_{\rm Weil}f
\]

using declared prime, Gamma, completion-boundary and compatibility events.

Prove coefficientwise:

\[
S_{0,-}^{\rm full}=Z_{\rm Weil}^*Z_{\rm Weil},
\]

\[
L_\partial(f)=\langle p_\partial,Z_{\rm Weil}f\rangle,
\]

and therefore

\[
S_{0,-}^{\rm full}-L_\partial^*L_\partial
=Z_{\rm Weil}^*QZ_{\rm Weil}.
\]

No classical explicit formula is allowed to define \(Z_{\rm Weil}\).

---

## Stage 4: native five-label faithfulness

Construct the five-label observer from declared target labels and prove

\[
QZ_{\rm Weil}
=T_\Sigma^*T_\Sigma QZ_{\rm Weil}
\]

on the adverse target-relevant module.

Then derive

\[
B_\Sigma
=T_\Sigma QZ_{\rm Weil}
R^{-1}
Z_{\rm Weil}^*QT_\Sigma^*
\]

from the cut-generated objects and certify

\[
\lambda_{\max}(B_\Sigma)<1
\]

with outward bounds.

Only after Stages 3 and 4 are complete may the classical completed-Weil formula
recognize the native construction as its shadow.

---

## Current status

```text
STAGE 1 THEORY                     WRITTEN
STAGE 1 GENERALIZED IMPLEMENTATION WRITTEN
STAGE 2 TESTS                      NOT YET WRITTEN
STAGE 3 RH SPECIALIZATION          NOT YET STARTED
STAGE 4 OUTWARD CERTIFICATE        NOT YET STARTED
```
