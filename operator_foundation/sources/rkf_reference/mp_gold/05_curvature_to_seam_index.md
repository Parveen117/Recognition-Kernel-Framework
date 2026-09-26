# MP Gold 05: Curvature-to-Seam-Index Law

## Source PR

```text
MP PR #239  Restore thermodynamic curvature provenance of Lambda response
```

## Why this is gold

This PR prevents the seductive but illegal shortcut

```text
Gamma_c Gamma_m = k_Sigma.
```

A positive scalar cannot simply be declared equal to an integer seam charge. The useful result is the typed path/spectral-flow law that says how curvature may influence a seam integer through an operator path.

## Response tetrad

The signed caloric-mechanical tetrad is

```text
C_th = (C_p, C_v, C_s, C_t),
C_s = V(dP/dV)_S,
C_t = V(dP/dV)_T.
```

It is separated from the conventional positive bulk moduli

```text
K_S = -C_s,
K_T = -C_t.
```

Uniform entropy-scaled coordinates are

```text
lambda_X^th = -ST/C_X.
```

## Closure ratios

The audited orientations are

```text
Gamma_c = lambda_p^th/lambda_v^th = C_v/C_p,
Gamma_m = lambda_t^th/lambda_s^th = C_s/C_t = K_S/K_T = kappa_T/kappa_S.
```

Thus the flat equilibrium identity is

```text
I_th = Gamma_c Gamma_m = 1.
```

## Curvature form

The response tetrad defines

```text
omega_th = sum_X lambda_X^th dx_X,
Omega_th = d omega_th.
```

`Omega_th=0` is local response flatness. The scalar

```text
delta_th = log(Gamma_c Gamma_m)
```

is only a dimensionless sector projection, not the full curvature tensor.

## Lawful seam bridge

For a norm-continuous compact self-adjoint response path,

```text
k_Sigma(eta;u_1)-k_Sigma(eta;u_0)
 = -sf(I-K_eta(u_s);0).
```

Thus curvature can generate seam-index change only through an explicit operator representation and threshold spectral flow.

## Quantitative margin rule

If an intertwiner proves

```text
||K_eta(u)-K_eta(u_0)|| <= L_eta |log(Gamma_c Gamma_m)|
```

and the flat reference has margin `m_eta`, then

```text
L_eta |log(Gamma_c Gamma_m)| < m_eta
```

preserves zero seam charge.

## Reuse in RKF

Use this as the type-safe bridge between physical/UGD/thermodynamic curvature language and integer seam charge. It says what must be proved before curvature can speak to the seam integer.

## Claim boundary

```text
thermodynamic tetrad provenance             ESTABLISHED
scalar=integer shortcut                      REJECTED BY TYPE
general curvature-path/spectral-flow law     PROVED
explicit thermo-arithmetic intertwiner        OPEN
Lipschitz constant L_eta                      OPEN
RH                                            NOT CLAIMED HERE
```
