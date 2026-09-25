# Canonical Thermodynamic Response-Cost and Barrier Theorem

## 1. Canonical response frame

Let the four thermodynamic response columns be

\[
\rho_X(x)\in\mathcal Y,
\qquad X\in\{p,v,s,t\},
\]

with synthesis map

\[
T_x:\mathbb C^4\to\mathcal Y,
\qquad T_xe_X=\rho_X(x).
\]

Define the compatibility Gram matrix

\[
M_x=T_x^*T_x.
\]

On

\[
\mathcal S_{\mathrm{th}}(x)=(\ker M_x)^\perp,
\]

define

\[
\boxed{
J_{\mathrm{th}}(x)=T_xM_x^{-1/2}.
}
\]

Then

\[
J_{\mathrm{th}}(x)^*J_{\mathrm{th}}(x)=I_{\mathcal S_{\mathrm{th}}(x)}.
\]

## 2. Canonical source-to-response coupling

Let \(J_q\) be an isometric reconstruction of a declared native source block and let \(\mathcal C\) be the native channel isometry. Define

\[
\boxed{
B_q(x)=J_{\mathrm{th}}(x)^*\mathcal C J_q.
}
\]

Let

\[
H_{\mathrm{th}}(x)>0
\]

be a stable response metric obtained from positive susceptibilities or compatibility-Gram whitening.

Define the response cost

\[
\boxed{
Q_q(x)=B_q(x)^*H_{\mathrm{th}}(x)B_q(x)\ge0.
}
\]

## Theorem 2.1 (bounded thermodynamic response barrier)

Define

\[
A_q=e^{-Q_q/2},
\qquad
\boxed{
W_q=I-e^{-Q_q}.
}
\]

Then

\[
\boxed{0\le W_q<I}
\]

and

\[
\boxed{
\ker W_q=\ker Q_q=\ker B_q.
}
\]

### Proof

Since \(H_{\mathrm{th}}>0\),

\[
Q_q=(H_{\mathrm{th}}^{1/2}B_q)^*(H_{\mathrm{th}}^{1/2}B_q)\ge0,
\]

and

\[
\ker Q_q=\ker(H_{\mathrm{th}}^{1/2}B_q)=\ker B_q.
\]

Functional calculus on the nonnegative operator \(Q_q\) gives

\[
0<e^{-Q_q}\le I,
\]

hence \(0\le W_q<I\). The scalar function \(1-e^{-t}\) vanishes exactly at \(t=0\), so

\[
\ker W_q=\ker Q_q.
\]

QED.

## 3. Basis invariance

Under unitary changes of source and response coordinates,

\[
B_q\mapsto V^*B_qU,
\qquad
H_{\mathrm{th}}\mapsto V^*H_{\mathrm{th}}V.
\]

Therefore

\[
Q_q\mapsto U^*Q_qU,
\qquad
W_q\mapsto U^*W_qU.
\]

Spectrum, rank, kernel, and positivity are invariant.

## 4. Barrier interpretation

The spectrum of \(Q_q\) measures response cost. The bounded defect \(W_q\) is the corresponding response barrier. Radial response magnitude changes the barrier strength; unitary angular changes rotate its orientation without changing its spectrum.

## Claim boundary

```text
CANONICAL RESPONSE-FRAME WHITENING         PROVED
CANONICAL COUPLING B_q                     PROVED ON DECLARED SOURCE RANGE
POSITIVE RESPONSE COST Q_q                 PROVED
BOUNDED BARRIER W_q                        PROVED
KERNEL IDENTITY                            PROVED
UNITARY BASIS INVARIANCE                   PROVED
PHYSICAL SOURCE IDENTIFICATION             OPEN
CONTINUUM RESPONSE-CURVATURE IDENTITY       OPEN
```
