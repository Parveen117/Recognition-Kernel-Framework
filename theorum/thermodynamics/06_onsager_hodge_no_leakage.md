# Onsager-Hodge No-Leakage Theorem

## 1. Response-space decomposition

Let the finite thermodynamic response space admit an orthogonal Hodge decomposition

\[
\mathcal H_{\mathrm{th}}
=
\mathcal H_{\mathrm{ex}}
\oplus
\mathcal H_{\mathrm{coex}}
\oplus
\mathcal H_{\mathrm{har}}.
\]

Let \(P_{\mathrm{ex}},P_{\mathrm{coex}},P_{\mathrm{har}}\) be the corresponding orthogonal projections.

Let \(A\) denote the accepted response sector and \(D\) a declared defect sector. Assume:

1. the Hodge projections reduce the accepted response metric;
2. accepted and defect syntheses are typed into declared orthogonal Hodge sectors;
3. the response intertwiner respects the Hodge grading;
4. all source maps used below are bounded on the finite packet.

## Theorem 1.1 (finite Onsager-Hodge no-leakage)

If

\[
A\subseteq\mathcal H_{\mathrm{ex}}\oplus\mathcal H_{\mathrm{har}},
\qquad
D\subseteq\mathcal H_{\mathrm{coex}},
\]

then

\[
\boxed{P_A P_D=0}
\]

and every accepted-defect cross Gram block vanishes:

\[
\boxed{S_A^*S_D=0.}
\]

Consequently the total response Gram splits orthogonally:

\[
(S_A\oplus S_D)^*(S_A\oplus S_D)
=
S_A^*S_A\oplus S_D^*S_D.
\]

### Proof

The Hodge sectors are mutually orthogonal. Hence the orthogonal projections onto the accepted and defect ranges have zero product. The synthesis ranges lie in these orthogonal sectors, so

\[
\langle S_Aa,S_Dd\rangle=0
\]

for all coefficients \(a,d\), which is equivalent to \(S_A^*S_D=0\). QED.

## Corollary 1.2 (no hidden defect cancellation)

Under the theorem's assumptions, a nonzero defect energy cannot be cancelled by an accepted response vector, because

\[
\|S_Aa+S_Dd\|^2
=
\|S_Aa\|^2+
\|S_Dd\|^2.
\]

Thus zero total response forces both orthogonal components to vanish separately.

## 2. Claim discipline

This theorem is exact on a declared finite response packet. It does not prove that a physical thermodynamic response, a continuum native source, and an arithmetic Weil source share the required Hodge grading. That identification is a separate provenance theorem.

## Claim boundary

```text
FINITE HODGE ORTHOGONAL SPLITTING             ASSUMED / DECLARED
ACCEPTED-DEFECT CROSS BLOCK                   PROVED ZERO
ORTHOGONAL ENERGY SPLITTING                   PROVED
NO HIDDEN CROSS-SECTOR CANCELLATION           PROVED
PHYSICAL HODGE GRADING OF NATIVE SOURCE       OPEN
CONTINUUM NO-LEAKAGE                          OPEN
```
