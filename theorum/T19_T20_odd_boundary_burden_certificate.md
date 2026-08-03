# T19/T20 Odd Boundary-Burden Certificate

## Source provenance

```text
source repository: Parveen117/MP
primary PRs:       #276, #277
main objects:      beta_partial^cut, S_(0,-)^full, L_partial, W_3^-
```

## Why this capsule exists

The zero-cut T03 route is the current terminal endpoint route in the cleaned paper.  However, T19 and T20 are still important: they give an independent odd-sector sign certificate and an alternate single-sector route.

They should not be deleted or treated as irrelevant.  They are not the same theorem as T03.

## T19 burden inequality

T18 proves the boundary-burden equivalence

```text
full odd sign  <=>  beta_partial^cut <= 1.
```

T19 proves the endpoint bound

```text
beta_partial^cut <= 0.9998319617060448 < 1.
```

The strict reserve is

```text
1 - beta_partial^cut >= 0.0001680382939552.
```

The proof uses the exact endpoint-difference identity

```text
beta_0 - beta_eta
  = sum_j m_j eta / (s_j (s_j + eta)).
```

The reconstructed Arb cut profile has

```text
active cells                 2400
prime-power events           78734
step                         0.005
near-zero slope-gap lower    28.96922744937062
minimum positive source floor 0.0003621153431171327
far-ray floor                0.15683586289723883
```

At

```text
eta                 1.5625e-5
beta_eta^+          0.999773667408463
shifted reserve     2.2633259153703733e-4
```

the correction ledger is

```text
first-cut correction    2.4184691966571344e-6
active-band correction  2.9454791518469324e-6
far-ray correction      5.293034923330094e-5
total correction        5.829429758180501e-5
```

Thus T19 proves

```text
S_(0,-)^full - L_partial^dagger L_partial >= 0.
```

on the declared native source carrier.

## T20 strict odd single-sector chain

T20 consumes T19 and adds source injectivity:

```text
unshifted covariant cut flow
+ endpoint C1 regularization
+ Hardy active-band no-blindness
    -> ker S_(0,-)^full = {0}
```

Together with T18/T19:

```text
T18 cut-square identity
+ T19 beta_partial^cut < 1
    -> W_3^- is strictly positive on every nonzero odd core state.
```

T20 then records the optional classical membrane:

```text
strict odd Weil positivity
+ pinned odd-parity Weil implication
    -> RH under the declared classical explicit-formula normalization.
```

## Relationship to the cleaned endpoint paper

T19/T20 are not required if the paper uses the zero-cut T03 endpoint as its terminal native theorem:

```text
T03 source-Gram identity
-> K_0 = R_Sigma^*(I-P_src)R_Sigma >= 0
-> endpoint Schur closure.
```

But T19/T20 are still valuable and should be included as an independent odd-burden certificate, because they show that the adverse odd boundary packet is subcritical by a direct cut/refinement estimate.

## Correct dependency placement

```text
Main terminal route:
  positive-eta path equality
  -> seam integer / five-matrix reduction
  -> M3 accepted block
  -> one-sector reduction
  -> zero-cut T03 endpoint

Independent odd-burden certificate:
  T18 equivalence
  -> T19 beta_partial^cut < 1
  -> full odd sign
  -> T20 strict odd positivity if ker S_(0,-)^full = 0
```

## Claim boundary

```text
T19 beta_partial^cut < 1                 PROVED IN SOURCE PR
T19 full odd completed-Weil sign          PROVED ON DECLARED NATIVE SOURCE CARRIER
T20 strict odd positivity                 PROVED UNDER ITS SOURCE-INJECTIVITY CHAIN
T20 odd-parity RH implication             CLASSICAL/PINNED INPUT WHERE USED
T19/T20 as zero-cut T03 replacement       NOT IDENTIFIED
T19/T20 as independent support            RETAINED
```
