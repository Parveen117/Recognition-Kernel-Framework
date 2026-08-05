# Thermo-Weil Provenance, Five-Source, and Boundary-Schur Theorem

## 1. Provenance contract

Let

\[
C_{\mathrm{th}}:\mathbb C^5\to\mathbb C^4
\]

be a proposed boundary-plus-tetrad thermodynamic coupling and let

\[
R_{\mathrm W}:\mathbb C^5\to\mathbb C^4
\]

be the finite Weil response synthesis.

The statement

\[
C_{\mathrm{th}}^*H_{\mathrm{th}}C_{\mathrm{th}}
=R_{\mathrm W}^*R_{\mathrm W}
\]

may be promoted from finite matching to a source theorem only when the following are independently certified:

1. physical thermodynamic source lineage;
2. normalization and units;
3. positive response metric \(H_{\mathrm{th}}>0\);
4. event-resolved five-source assignment;
5. native source-chain identification;
6. covariance under admissible coordinate changes.

## Theorem 1.1 (finite five-source Gram equivalence)

Put

\[
G_{\mathrm{th}}=H_{\mathrm{th}}^{1/2}C_{\mathrm{th}}.
\]

If

\[
G_{\mathrm{th}}^*G_{\mathrm{th}}=R_{\mathrm W}^*R_{\mathrm W},
\]

then there exists a partial isometry \(U\) from the final range of \(R_{\mathrm W}\) to the final range of \(G_{\mathrm{th}}\) such that

\[
\boxed{G_{\mathrm{th}}=UR_{\mathrm W}.}
\]

If both maps have full row rank four, \(U\in U(4)\).

### Proof

Two finite synthesis maps with the same Gram define the same seminorm on the common coefficient space. Quotienting by the shared kernel gives an isometry between their ranges, which extends to the stated partial isometry. Full row rank makes the final ranges equal to \(\mathbb C^4\), so the partial isometry is unitary. QED.

This theorem proves finite unitary equivalence. The provenance contract determines whether that equivalence represents the same physical source.

## 2. Boundary Schur realization

Let the total finite cost matrix be written as

\[
\mathcal Q=
\begin{pmatrix}
A&B\\
B^*&D
\end{pmatrix},
\qquad D>0.
\]

Define the boundary Schur complement

\[
\boxed{S_\partial=A-BD^{-1}B^*.}
\]

## Theorem 2.1 (thermo-Weil boundary Schur theorem)

The block matrix \(\mathcal Q\) is positive semidefinite if and only if

\[
D>0
\quad\text{and}\quad
S_\partial\ge0.
\]

Moreover,

\[
\operatorname{inertia}(\mathcal Q)
=
\operatorname{inertia}(D)
+
\operatorname{inertia}(S_\partial).
\]

### Proof

Use the exact congruence

\[
\begin{pmatrix}I&-BD^{-1}\\0&I\end{pmatrix}
\mathcal Q
\begin{pmatrix}I&0\\-D^{-1}B^*&I\end{pmatrix}
=
\begin{pmatrix}S_\partial&0\\0&D\end{pmatrix}.
\]

Congruence preserves inertia. QED.

## Claim boundary

```text
PROVENANCE INPUT CONTRACT                    DECLARED
FINITE SAME-GRAM PARTIAL ISOMETRY            PROVED
FULL-RANK U(4) INTERTWINER                   PROVED
BOUNDARY SCHUR POSITIVITY                    PROVED
SCHUR INERTIA SPLITTING                      PROVED
PHYSICAL THERMO / WEIL SOURCE IDENTITY       OPEN WITHOUT PROVENANCE
COFINAL CONTINUUM LIMIT                      OPEN
```
