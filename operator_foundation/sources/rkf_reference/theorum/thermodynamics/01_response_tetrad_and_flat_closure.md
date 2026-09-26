# Thermodynamic Response Tetrad and Flat Closure Theorem

## 1. Signed response tetrad

Let

\[
C_{\mathrm{th}}=(C_p,C_v,C_s,C_t),
\]

where the caloric channels are the usual heat capacities and the signed mechanical channels are

\[
C_s=V\left(\frac{\partial P}{\partial V}\right)_S,
\qquad
C_t=V\left(\frac{\partial P}{\partial V}\right)_T.
\]

For stable materials the conventional positive bulk moduli are

\[
K_S=-C_s,
\qquad
K_T=-C_t.
\]

Define the entropy-scaled response coordinates uniformly by

\[
\boxed{
\lambda_X^{\mathrm{th}}=-\frac{ST}{C_X},
\qquad X\in\{p,v,s,t\}.
}
\]

The mechanical coordinates are therefore not silently identified with unrelated derivative coordinates. Their sign and type are retained.

## 2. Caloric and mechanical ratios

Define

\[
\Gamma_c
=\frac{\lambda_p^{\mathrm{th}}}{\lambda_v^{\mathrm{th}}}
=\frac{C_v}{C_p},
\]

and

\[
\Gamma_m
=\frac{\lambda_t^{\mathrm{th}}}{\lambda_s^{\mathrm{th}}}
=\frac{C_s}{C_t}
=\frac{K_S}{K_T}
=\frac{\kappa_T}{\kappa_S}.
\]

## Theorem 2.1 (flat caloric-mechanical closure)

On a constitutive chart where the standard equilibrium response identities hold,

\[
\boxed{
I_{\mathrm{th}}:=\Gamma_c\Gamma_m=1.
}
\]

### Proof

The equilibrium caloric identity gives

\[
\frac{C_p}{C_v}=\frac{\kappa_T}{\kappa_S}.
\]

Taking the reciprocal of the caloric ratio and multiplying by the mechanical ratio gives

\[
\Gamma_c\Gamma_m
=\frac{C_v}{C_p}\frac{\kappa_T}{\kappa_S}=1.
\]

QED.

## 3. Interpretation

The scalar

\[
\delta_{\mathrm{th}}=\log(\Gamma_c\Gamma_m)
\]

vanishes on the flat equilibrium sector. It is a dimensionless sector projection, not the full thermodynamic curvature tensor.

## Claim boundary

```text
SIGNED RESPONSE TETRAD                    DEFINED
ENTROPY-SCALED LAMBDA COORDINATES         DEFINED
CALORIC RATIO ORIENTATION                 PROVED
MECHANICAL RATIO ORIENTATION              PROVED
FLAT CLOSURE Gamma_c Gamma_m = 1          PROVED
FULL NONEQUILIBRIUM CURVATURE             NOT IDENTIFIED BY THIS SCALAR ALONE
```
