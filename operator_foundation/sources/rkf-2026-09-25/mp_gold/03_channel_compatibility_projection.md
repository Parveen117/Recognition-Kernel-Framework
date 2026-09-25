# MP Gold 03: Channel Compatibility Projection

## Source PR

```text
MP PR #178  Prove native X3 channel-compatibility graph projection
```

## Why this is gold

This theorem prevents a subtle but dangerous error: using raw split-channel coefficients as if they were native `X_3` coefficients. The MP journey found an exact sign-reversal witness, which is the kind of small demon that later eats whole proofs for breakfast.

## Closed graph theorem

Write

```text
A0 f = exp(3|x|/2) f
B0 f = (2pi)^(-1/2) sqrt(1+|G|) fhat.
```

The native analysis range is exactly the closed graph of

```text
T = B0 A0^(-1)
```

on its natural domain. The native norm is the graph norm.

## Variational compatibility projection

For a split channel residual

```text
r = (r_A, r_Gamma),
```

the compatible spatial coordinate `a_r` is the unique solution of

```text
<a_r,v> + <T a_r,Tv>
  = <r_A,v> + <r_Gamma,Tv>.
```

Then

```text
C3* r = A0^(-1) a_r
P_comp r = (a_r, T a_r).
```

## Raw sign-reversal no-go

The exact finite witness gives

```text
raw channel pairing       = 15/4 > 0
native compatible pairing = -1/4 < 0.
```

Therefore even a complete exact raw channel packet cannot be used directly as a native center.

## Error transfer

For a finite channel packet and finite graph solve,

```text
||z-z_NM||_X3 <= eta_channel + rho_compatibility
```

and hence

```text
|b3-b3_NM| <= ||epsilon_3|| (eta_channel+rho_compatibility).
```

Both terms are mandatory.

## Reuse in RKF

Use this theorem whenever channel packets are imported into native `X_3` response coordinates. Any future RKF proof that updates `b3`, `M3`, source readouts or endpoint Grams from split-channel data must pass through this compatibility projection.

## Claim boundary

```text
channel range as closed graph          PROVED
variational compatibility projection   PROVED
raw channel center                     EXCLUDED
channel-tail + solve-error transfer    PROVED
numerical lifts                        SEPARATE PACKETS
RH terminal sign                       NOT CLAIMED HERE
```
