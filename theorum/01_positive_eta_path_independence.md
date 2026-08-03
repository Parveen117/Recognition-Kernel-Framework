# Theorum 01: Positive-Eta Path Independence by Amplitude Lift

## Source provenance

```text
source repository: Parveen117/MP
primary PR:        #246 Reset RH route onto rotation-generated recognition topology
source branch:     agent/rh-rotation-metric-topology-reset
```

## Statement

On the fixed five-label event-response carrier, every positive-eta normalization/continuation rectangle is an identity loop.

Equivalently, for any admissible positive eta values `eta_1, eta_2`,

```text
normalize then eta-continue
=
eta-continue then normalize.
```

No rank-one seam compensation is required for the positive-eta family itself.

## Native factorization

The state-locked construction has the factorization

```text
A_chart  = A U,
Theta_eta = Q_chart G_eta^(1/2),
G_eta = 1 + (A_+ + eta I_4),    eta > 0.
```

Here:

```text
A          raw native event amplitude, eta-independent;
U          one fixed unitary accepted chart;
Q_chart    the polar orientation of the charted amplitude;
G_eta      positive metric/scale factor for eta > 0.
```

Because right multiplication by a unitary is polar-covariant and right multiplication by a strictly positive factor does not change the polar orientation,

```text
polar(A U) = polar(A) U,
polar(Q_chart G_eta^(1/2)) = Q_chart.
```

Thus the frame transport data are exactly

```text
raw eta transport                 I_5
normalized eta transport          I_5
raw-to-normalized transport       U*
based loop                        I_5
```

for every positive eta in the fixed five-label family.

## Finite state-locked rectangle evidence

The user-local rectangle at

```text
eta     = 0.010
eta + h = 0.011
```

used the four actual amplitudes

```text
raw(eta)          normalized(eta)
raw(eta+h)        normalized(eta+h)
```

and reported

```text
status                          PASS_STATE_LOCKED_UGD_ETA_NORMALIZATION_RECTANGLE_EVALUATION
loop classification             FINITE_ACTUAL_TWO_PATH_EQUALITY_PROVED
path transport difference       3.0669860554696173e-15
loop identity residual          3.1396725820594018e-15
defect phase                    1.0705180635847342e-40
defect-to-accepted leakage      1.7140530928543942e-17
accepted-block residual         3.139637946219698e-15
endpoint scale difference       0
maximum pairing return residual 6.071532165918825e-18
false checks                    none
```

These numbers are the floating-point shadow of the exact positive-eta family theorem.

## What this closes

```text
positive-eta raw amplitude path equality       CLOSED
positive-eta normalization path equality       CLOSED
fixed five-label UGD rectangle                 CLOSED
need for new observer label at positive eta    REMOVED
rank-one seam compensation at positive eta     NOT NEEDED
```

## What this does not close

At eta zero,

```text
G_0 = 1 + A_+.
```

If `A_+` has a kernel, the normalized response can lose support. Therefore the next eta problem is support/Fredholm descent, not another path-holonomy problem.

```text
eta-zero support descent                  OPEN
kernel-line target visibility             OPEN
continuum UGD/Fredholm identification      OPEN
actual RH target map                       OPEN
odd/even or single-sector terminal sign    NOT DECIDED BY THIS THEOREM
```

## Use in the framework

Consume this theorem only as the positive-eta path-equivalence adapter:

```text
positive eta family
-> no normalization/path-order ambiguity
-> fixed five-label carrier is lawful
-> eta-zero problem becomes support descent
```
