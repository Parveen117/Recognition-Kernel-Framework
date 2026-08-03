# Theorum 04: Zero-Cut T03 Endpoint Completion

## Source provenance

```text
source repository: Parveen117/MP
primary PR:        #254 Close the five-dimensional completed-Weil endpoint by explicit zero-cut T03 completion
support PRs:       #242, #247, #255, #256
main objects:      R_Sigma, P_src, S_(0,-), W_Sigma, A3, K_0
```

## Purpose

This theorem package records the endpoint completion of the five-dimensional completed-Weil packet after the seam-integer and single-sector reductions have fixed the terminal object.

It should not be confused with the earlier exploratory finite eta sequence. The T03 theorem is the endpoint source-readout theorem.

## Native T03 specialization

The zero-cut theorem fixes, before any lift is chosen:

```text
projected native observer;
completed-Weil target;
actual target-relevant blind quotient.
```

The two spectral inputs are:

```text
Spectral I:
  exact five-dimensional defect;
  minimal five-observer repair.

Spectral II:
  target-relative lift count;
  positive uniform repair margin;
  a posteriori response-defect control;
  matched visible/blind/cross certification;
  strong completion.
```

## Six-block Gram decomposition

For transported finite source maps `Y_n` and `T_n`, the five-label Gram defect is decomposed into

```text
visible compression
+ five-dimensional blind response
+ both cross blocks
+ omitted prime/Gamma tails
+ quadrature/window/solve/rounding errors
+ native/Feshbach/prime-torus chart transport.
```

The theorem records that the six directed bounds have total error tending to zero.

## Invariant source-Gram identity

Strong completion proves the invariant source-Gram identity

```text
R_Sigma^* P_src R_Sigma
  = (S_(0,-)^(dagger/2) W_Sigma)^*
    (S_(0,-)^(dagger/2) W_Sigma).
```

Literal equality of ambient source maps is not assumed. Equal Grams give a canonical partial-isometry identification of the final ranges. The endpoint sign needs only the invariant Gram identity.

## Projection-defect positivity

The independently constructed total-response Gram is

```text
R_Sigma^* R_Sigma = diag(1,A3).
```

Therefore the endpoint projection defect is

```text
K_0 = R_Sigma^*(I-P_src)R_Sigma >= 0.
```

The endpoint Schur equivalence then transfers this projection-defect positivity to the completed-Weil endpoint sign in the declared normalization.

## Terminal membrane

The theorem uses the classical completed explicit-formula identification and Weil criterion as the final classical membrane.

```text
native endpoint Schur sign
+ classical completed explicit formula / Weil criterion
-> RH in the declared normalization.
```

This folder records the native theorem and its stated terminal interface. It does not pretend that the classical membrane was independently rederived inside this capsule.

## Claim boundary

```text
zero-cut quotient                              FIXED
five-label lift                                SUPPLIED BY SPECTRAL I-II
six-block Gram decomposition                   SUPPLIED
vanishing total error                           SUPPLIED
orientation-free source readout                 SUPPLIED
K_0 = R_Sigma^*(I-P_src)R_Sigma >= 0            PROVED IN SOURCE THEOREM
endpoint Schur closure                          PROVED IN SOURCE THEOREM
classical Weil terminal membrane                CITED/CONSUMED WHERE STATED
```

## Use in the framework

Consume this theorem as the endpoint closure adapter:

```text
single-sector / five-label source packet
-> invariant source-Gram identity
-> K_0 >= 0
-> endpoint completed-Weil sign
-> classical membrane if invoked
```

Do not reopen M3, path equality, or seam integer while using T03. They are upstream adapters already transferred into this folder.
