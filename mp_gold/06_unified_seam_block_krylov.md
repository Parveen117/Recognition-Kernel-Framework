# MP Gold 06: Unified Seam Block-Krylov Machinery

## Source PR

```text
MP PR #240  Add matrix-free unified seam block-Krylov acceleration
```

## Why this is gold

This is reusable computational proof machinery for the seam response. It is not terminal by itself, but it gives the correct same-projection certificate and prevents the old error of enlarging a finite space blindly while the dangerous eigenvector hides in the complement.

## One global compact seam response

The active numerical object is

```text
K_Sigma,eta
 = K_+,eta direct_sum Lambda_-,eta^dir,

k_Sigma(eta)
 = rank 1_(1,infinity)(K_Sigma,eta).
```

The even and odd blocks are internal coordinates of one operator. The stopping rule and eta descent are global.

## Response-generated finite space

For finite-rank seed map `S`, define

```text
V_m = span{K_Sigma,eta^j Ran(S): 0<=j<=m}.
```

Every eigenspace above a declared threshold is captured by the cyclic space provided the seed projections span that eigenspace. Since a compact operator has only finitely many eigenvalues above a positive threshold, finite block-Krylov levels converge on the high-risk spectral subspace.

Seeds are generated from declared response channels:

```text
completion-boundary vectors;
low native standing-wave directions;
images under the compact defect;
curvature-response images only after an intertwiner is proved.
```

No vector is manufactured from a naked scalar such as `Gamma_c Gamma_m`.

## Same-projection certificate

For `P_m` onto the response space, define

```text
a_m = sup spectrum(P_m K P_m)
b_m = ||(I-P_m)K P_m||
d_m >= sup spectrum((I-P_m)K(I-P_m)).
```

Then

```text
sup spectrum(K)
 <= U(a_m,b_m,d_m),

U(a,b,d)
 = (a+d+sqrt((a-d)^2+4b^2))/2.
```

Every quantity must use the same projection.

## Two-stage native transfer

For standing-wave envelope `P_N`, if

```text
||K-P_N K P_N|| <= tau_N,
```

and `P_m <= P_N`, then

```text
b_m <= b_hat_(m,N)+tau_N
d_m <= d_hat_(m,N)+tau_N
```

and

```text
sup spectrum(K)
 <= U(a_m, b_hat_(m,N)+tau_N, d_hat_(m,N)+tau_N).
```

## Inexact response-action ledger

For finite generalized problem

```text
G_N v = lambda R_N v,
```

if the approximate solve has residual

```text
r = G_N x - R_N y,
```

then

```text
||y-R_N^(-1)G_N x||_(R_N)
 = ||r||_(R_N^(-1))
 <= eta^(-1/2)||r||_2.
```

This types iterative solve error directly into the proof ledger.

## Reuse in RKF

Use this as the standard numerical spectral-certificate machinery for any future RKF compact seam operator. The phrase to keep pinned is:

```text
same projection or no promotion.
```

## Claim boundary

```text
target-eigenspace cyclic capture       PROVED
same-projection two-block upper         PROVED
two-stage envelope transfer             PROVED
inexact response-solve ledger           PROVED
matrix-free backend                     IMPLEMENTED IN MP
actual large K=1920 certificate          NOT TRANSFERRED AS CLOSED RESULT
eta descent / RH                         NOT CLAIMED HERE
```
