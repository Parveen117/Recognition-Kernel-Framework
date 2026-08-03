# MP Gold 02: X3 Channel-Hermite Parseval No-Escape

## Source PR

```text
MP PR #171  Prove native X3 channel-Hermite Parseval frame
```

## Why this is gold

This is one of the cleanest reusable analytic tools in the MP journey. It replaces a speculative Stokes no-escape idea with an exact Parseval frame theorem derived directly from the native `X_3` norm.

## Native channel isometry

The exact analysis map is

```text
C_3 f
  = ( exp(3|x|/2) f,
      (2pi)^(-1/2) sqrt(1+|G|) fhat )
```

from `X_3` into

```text
Y = L2(R_x) direct_sum L2(R_xi).
```

By construction,

```text
||C_3 f||_Y = ||f||_X3,
C_3^* C_3 = I_X3.
```

## Parseval frame

Using normalized Hermite functions `h_n`, define

```text
z_A,n     = C_3^*(h_n,0)
z_Gamma,n = C_3^*(0,h_n).
```

Then

```text
||f||_X3^2
 = sum_n |<f,z_A,n>|^2
 + sum_n |<f,z_Gamma,n>|^2.
```

The lower and upper frame bounds are both exactly one.

## Parity and accepted-memory completion

Because channel weights are even and Hermite parity is exact:

```text
even Hermite modes frame X3_even
odd Hermite modes  frame X3_odd.
```

For any closed accepted memory space `V` and `Q=I-P_V`, the projected family

```text
{Q z_A,n, Q z_Gamma,n}
```

is again Parseval on `QX_3`.

## Target response no-escape

For a whitened channel residual `r`, the exact native response is

```text
z = C_3^* r.
```

Only the compatible part contributes:

```text
||z||_X3 = ||C_3 C_3^* r||_Y <= ||r||_Y.
```

For finite channel-Hermite projection `P_N`,

```text
z_N = C_3^* P_N r,
||z-z_N||_X3 <= ||(I-P_N)r||_Y.
```

Thus global target-response no escape follows from channel-Hermite completeness. Quantitative use still requires explicit coefficient-tail bounds.

## Reuse in RKF

Use this as the canonical no-escape / response-completeness scaffold whenever a finite response packet must be promoted without pretending a finite prefix is automatically complete.

## Claim boundary

```text
channel analysis isometry                  PROVED
channel-Hermite Parseval frame             PROVED, bounds 1,1
parity-resolved global no-escape           PROVED
accepted-memory projected frame            PROVED
target response frame convergence          PROVED
explicit coefficient-tail rate             SEPARATE QUANTITATIVE GATE
RH terminal sign                           NOT CLAIMED HERE
```
