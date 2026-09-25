# Theorum 03: Certified M3 Positivity and the Odd Accepted Block

## Source provenance

```text
source repository: Parveen117/MP
primary PRs:       #181, #182, #196, #198, #199, #200, #202
main objects:      G3, b3, e3, M3, A3, E3
```

## Target-local scalar

The reduced anti-seam scalar is

```text
M3 = q(e3,e3) - b3* G3^(-1) b3.
```

It is the Schur complement of the finite completed-Weil Gram block over

```text
V3 = span{u, |x|u, |x|^2u}.
```

The accepted odd block is

```text
E3 = span{u, |x|u, |x|^2u, e3}.
```

## Certified coupling signs

The strong-residual Krylov packet certifies the exact native coupling signs

```text
sgn(b3) = (-,+,+).
```

The final certified intervals recorded there are

```text
-8.4429782348e-6 < (b3)_u < -8.1644107492e-7
 3.0255175052e-7 < (b3)_h <  2.3045071878e-6
 3.6746554244e-8 < (b3)_k <  4.0310126099e-7
```

This solved the sign of the coupling vector, but did not by itself solve `M3`.

## Correlated Schur rule

Independent coordinate-box propagation through `G3^(-1)` is prohibited because `G3` is nearly singular. The M3 calculation must keep

```text
self channel;
coupling vector;
Schur compensation;
prime/Gamma truncation;
state transfer
```

inside one correlated ledger.

The source-seam invariance theorem gives

```text
q_/V3(e+v,e+v)=q_/V3(e,e),    v in V3,
```

and since

```text
e3 = r_odd - r3,
s3 = r_odd - u,
e3 - s3 = u - r3 in V3,
```

we may compute

```text
M3 = q_/V3(s3,s3).
```

## State-local ledger separation

The exact/fixed-state arithmetic is separated as

```text
M(x)-M_N(x_m)
=
[M(x)-M(x_m)]
+
[M(x_m)-M_N(x_m)].
```

The exact-to-state term is paid through

```text
|M(x)-M(x_m)| <= 2 eta_p eta_d + (157/30) eta_p^2.
```

The finite-state arithmetic term uses

```text
q = q_N + delta_q
b = b_N + delta_b
a_N = G3^(-1) b_N
```

and the Schur identity

```text
M(x_m)-M_N(x_m)
= delta_q - 2 Re<a_N,delta_b> - delta_b*G3^(-1)delta_b.
```

This route removes the older need to prove the whole exact-state `A_4.74` norm directly.

## Final certified interval

The fixed-state primal transfer closes the last formal transfer and records

```text
continuum eta_p                       < 1.4e-7
continuum eta_d                       < 1.83e-6
fixed-state pivot transfer            < 1.1e-14
state-local omitted-prime arithmetic  < 6.565652843015687e-13
finite packet guard                    7.1e-14
```

Around the canonical center

```text
1.651058994316351e-12
```

the exact target-local interval is

```text
3.08520376681449e-13
< M3 <
2.993597611951253e-12.
```

Therefore

```text
M3 > 0.
```

## Positive accepted block

The accepted block uses `G3>0` and `M3>0`. PR #202 records

```text
lambda_min(G3) = 2.0838177120437723e-13 > 0
3.08520376681449e-13 < M3 < 2.993597611951253e-12.
```

Since `M3` is the Schur complement of `G3` in the bordered block, the completed-Weil form is positive definite on

```text
E3 = span{u, |x|u, |x|^2u, e3}.
```

## Claim boundary

```text
exact native b3 signs                    CERTIFIED (-,+,+)
source-seam correlated Schur route        PROVED
state-local ledger separation             PROVED
fixed-state transfer                      CERTIFIED
exact target-local M3                     CERTIFIED POSITIVE
odd accepted finite block E3              CERTIFIED POSITIVE

signed infinite complement                NOT CLOSED BY M3 ALONE
full global Weil sign                      NOT CLOSED BY M3 ALONE
RH                                         NOT CLAIMED FROM THIS CAPSULE ALONE
```

## Use in the framework

Consume this theorem as the accepted-block certificate:

```text
G3 > 0 and M3 > 0
-> A3 > 0 / E3 positive
-> finite accepted block no longer missing
-> downstream obstruction is outside the accepted block
```
