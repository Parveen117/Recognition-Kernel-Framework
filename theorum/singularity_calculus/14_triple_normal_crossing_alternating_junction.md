# SC-14 — Triple Normal-Crossing Alternating-Junction Theorem

## 1. Transverse three-seam setup

Let a smooth manifold contain three regular cooriented hypersurfaces

\[
\Sigma_i=\{\rho_i=0\},\qquad i=1,2,3,
\]

with

\[
d\rho_1\wedge d\rho_2\wedge d\rho_3\neq0
\]

on the triple intersection

\[
K=\Sigma_1\cap\Sigma_2\cap\Sigma_3.
\]

Assume all one-sided traces are compatible in the ordinary normal-crossing
sense, so the finite jump operators commute whenever both are defined:

\[
\boxed{\Delta_i\Delta_j=\Delta_j\Delta_i.}
\]

Let \(\beta_i\) be the seam coefficient carried by \(\Sigma_i\), with one-sided
traces across the other two seams.

## 2. Pairwise junction residues

On the pairwise intersections define

\[
\boxed{
J_{12}=\Delta_1\beta_2-\Delta_2\beta_1,
}
\]

\[
\boxed{
J_{13}=\Delta_1\beta_3-\Delta_3\beta_1,
}
\]

and

\[
\boxed{
J_{23}=\Delta_2\beta_3-\Delta_3\beta_2.
}
\]

Each \(J_{ij}\) may itself have two traces across the remaining seam.

## 3. Triple-junction alternating residue

Define on \(K\)

\[
\boxed{
T_{123}
=
\Delta_1J_{23}
-
\Delta_2J_{13}
+
\Delta_3J_{12}.
}
\]

The signs correspond to the ordered normal orientation
\(d\rho_1\wedge d\rho_2\wedge d\rho_3\).

## Theorem 3.1 — Triple compatibility

For pairwise junction residues generated from compatible seam data \(\beta_i\),

\[
\boxed{T_{123}=0.}
\]

### Proof

Expand the definition:

\[
\begin{aligned}
T_{123}
={}&
\Delta_1(\Delta_2\beta_3-\Delta_3\beta_2)
-
\Delta_2(\Delta_1\beta_3-\Delta_3\beta_1)\\
&+
\Delta_3(\Delta_1\beta_2-\Delta_2\beta_1).
\end{aligned}
\]

Therefore

\[
\begin{aligned}
T_{123}
={}&
\Delta_1\Delta_2\beta_3
-
\Delta_1\Delta_3\beta_2
-
\Delta_2\Delta_1\beta_3
+
\Delta_2\Delta_3\beta_1\\
&+
\Delta_3\Delta_1\beta_2
-
\Delta_3\Delta_2\beta_1.
\end{aligned}
\]

The terms cancel in pairs by commutativity of the normal-crossing jump operators.
Hence \(T_{123}=0\). ∎

## 4. Distributional interpretation

SC-13 shows that differentiating a stratified curvature packet produces pairwise
codimension-two terms of the form

\[
\delta(\rho_i)\delta(\rho_j)
 d\rho_i\wedge d\rho_j\wedge J_{ij}.
\]

Differentiating those pairwise terms across the third seam produces a possible
codimension-three coefficient. With the ordered orientation above, that coefficient
is exactly

\[
\boxed{T_{123}.}
\]

Thus the triple-delta contribution cancels for compatible lower-stratum data.
This is the codimension-three normal-crossing manifestation of the nilpotent
boundary/derivative law. It does **not** place a triple-delta term in the first
curvature \(d\alpha\).

## 5. Nontriviality

The theorem does not require every pairwise junction residue to vanish. One may
have

\[
J_{12}\neq0,\qquad J_{13}\neq0,\qquad J_{23}\neq0
\]

while their alternating triple boundary still satisfies

\[
T_{123}=0.
\]

Therefore pairwise defect and triple incompatibility are different typed notions.

## Recognition interpretation

The hierarchy is now

```text
seam data beta_i
    -> pairwise junction residues J_ij
    -> triple compatibility residue T_123.
```

A faithful Recognition packet must not replace this hierarchy by one scalar total.

## Status

```text
THREE-SEAM TRANSVERSALITY                     ASSUMED
COMMUTING NORMAL-CROSSING JUMPS               ASSUMED/GEOMETRIC
PAIRWISE JUNCTION RESIDUES                    DEFINED
TRIPLE ALTERNATING RESIDUE                    DEFINED
T_123 = 0 FOR DERIVED COMPATIBLE DATA         PROVED
TRIPLE-DELTA IN FIRST CURVATURE d alpha       REJECTED
NONTRANSVERSE / SINGULAR TRIPLE INTERSECTION  NOT CLAIMED
```