# Thermodynamic Curvature to Seam-Index Spectral-Flow Theorem

## 1. Response connection

Let the entropy-scaled response coordinates define the one-form

\[
\omega_{\mathrm{th}}
=\sum_{X\in\{p,v,s,t\}}
\lambda_X^{\mathrm{th}}\,dx_X,
\]

with curvature

\[
\boxed{
\Omega_{\mathrm{th}}=d\omega_{\mathrm{th}}.
}
\]

Local response flatness means

\[
\Omega_{\mathrm{th}}=0.
\]

## 2. Type obstruction

A positive real scalar such as

\[
\Gamma_c\Gamma_m
\]

cannot be canonically identical to a nonnegative integer seam rank on a connected constitutive domain. A continuous scalar and an integer-valued threshold count have different types.

Thus the discarded identity

\[
\Gamma_c\Gamma_m=k_\Sigma
\]

is not a lawful theorem without an explicit operator representation and a threshold-crossing mechanism.

## 3. Curvature path represented by compact operators

Let

\[
u\mapsto K_\eta(u)
\]

be a norm-continuous path of compact self-adjoint response operators, and define the threshold rank

\[
k_\Sigma(\eta;u)=N_+\bigl(K_\eta(u)-I\bigr).
\]

Assume the endpoints are noncritical:

\[
1\notin\sigma(K_\eta(u_0))\cup\sigma(K_\eta(u_1)).
\]

## Theorem 3.1 (curvature-path / seam-index law)

For any continuous path \(u_s\) from \(u_0\) to \(u_1\),

\[
\boxed{
k_\Sigma(\eta;u_1)-k_\Sigma(\eta;u_0)
=-\operatorname{sf}\bigl(I-K_\eta(u_s);0\bigr).
}
\]

### Proof

The integer \(k_\Sigma\) changes only when an eigenvalue of \(K_\eta(u_s)\) crosses the threshold \(1\). Equivalently, an eigenvalue of \(I-K_\eta(u_s)\) crosses zero. Counting signed zero crossings gives the spectral flow. The sign is reversed because an upward crossing of \(K_\eta\) through \(1\) is a downward crossing of \(I-K_\eta\) through zero. QED.

## Corollary 3.2 (quantitative no-crossing criterion)

Suppose the flat reference \(K_\eta(u_0)\) has margin

\[
m_\eta=\operatorname{dist}\bigl(1,\sigma(K_\eta(u_0))\bigr)>0,
\]

and an explicit response intertwiner yields

\[
\|K_\eta(u)-K_\eta(u_0)\|
\le L_\eta\,|\log(\Gamma_c\Gamma_m)|.
\]

Then

\[
\boxed{
L_\eta\,|\log(\Gamma_c\Gamma_m)|<m_\eta
}
\]

prevents threshold crossing and preserves the seam rank.

## Claim boundary

```text
RESPONSE ONE-FORM AND CURVATURE                  DEFINED
SCALAR = INTEGER IDENTIFICATION                  REJECTED BY TYPE
CURVATURE-PATH / SPECTRAL-FLOW LAW               PROVED
QUANTITATIVE NO-CROSSING CRITERION                PROVED
EXPLICIT PHYSICAL CURVATURE -> NATIVE OPERATOR   OPEN
OUTWARD VALUE OF L_eta                           OPEN
```
