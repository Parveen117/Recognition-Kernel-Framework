# Verified Singularity Calculus — Triple Normal-Crossing Extension

## Status

```text
THEORY EXTENSION STATUS:
RNKE_VERIFIED_SINGULARITY_THEORY_V4_WITH_EXCLUSIONS
```

This extension consumes SC-01 through SC-13 and adds the first transverse
codimension-three compatibility layer.

## 1. Three-seam normal crossing

Let

\[
\Sigma_i=\{\rho_i=0\},\qquad i=1,2,3,
\]

meet transversely, so

\[
d\rho_1\wedge d\rho_2\wedge d\rho_3\neq0
\]

on the triple intersection

\[
K=\Sigma_1\cap\Sigma_2\cap\Sigma_3.
\]

The one-sided jump operators commute on compatible normal-crossing trace data.

## 2. Pairwise junction layer

For seam coefficient forms \(\beta_i\), define

\[
J_{12}=\Delta_1\beta_2-\Delta_2\beta_1,
\]

\[
J_{13}=\Delta_1\beta_3-\Delta_3\beta_1,
\]

\[
J_{23}=\Delta_2\beta_3-\Delta_3\beta_2.
\]

These are the pairwise junction channels from the SC-13 hierarchy, now retained
simultaneously in a three-seam geometry.

## 3. Triple alternating residue

Define

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

SC-14 proves that for compatible seam-derived junction data,

\[
\boxed{T_{123}=0.}
\]

The proof is exact cancellation of mixed jumps using

\[
\Delta_i\Delta_j=\Delta_j\Delta_i.
\]

Thus the codimension ladder continues as

```text
seam coefficients beta_i
        ↓
pairwise junction residues J_ij
        ↓
triple alternating compatibility T_123.
```

## 4. Where the triple object lives

There is still no independent triple-delta term in the first curvature
\(d\alpha\).

For a genuine piecewise process form, the first derivative produces bulk and
codimension-one seam terms. The next stratified derivative can produce pairwise
codimension-two junction terms. Differentiating those junction terms through the
third seam gives the potential codimension-three coefficient \(T_{123}\), which
cancels for compatible derived data.

So the theory does not manufacture a new singularity merely because three seams
cross. It identifies the compatibility law that prevents a false one.

## 5. Independent-data obstruction

SC-15 reverses the question. Suppose \(J_{12},J_{13},J_{23}\) are declared
independently. Then

\[
\boxed{
T_{123}\neq0
\Longrightarrow
\text{no compatible seam data }\beta_i\text{ can realize them.}
}
\]

The converse is intentionally not claimed. The condition \(T_{123}=0\) passes
this local compatibility gate but does not prove global reconstruction.

## 6. Recognition packet

The triple-junction compatibility packet is

\[
\boxed{
\mathfrak J_3
=(J_{12},J_{13},J_{23};T_{123}).
}
\]

This packet is not a scalar score. Pairwise junction values may be nonzero while
the triple compatibility residue vanishes. Likewise a nonzero \(T_{123}\) may
not be hidden by cancellation with the pairwise channels.

The fail-closed rule is

\[
\boxed{
T_{123}\neq0
\Rightarrow
\operatorname{REJECT\_COMPATIBILITY}.
}
\]

## 7. Relation to previous versions

```text
v1: single seam -> distributional curvature -> typed closure
v2: disjoint seams -> additive memory -> cocycle / bulk interaction
v3: two transverse seams -> pairwise junction Bianchi residue
v4: three transverse seams -> alternating triple compatibility obstruction
```

The composition/filler cocycle of SC-11 and the geometric junction hierarchy of
SC-12 through SC-15 remain separate typed structures.

## 8. Verification

The v4 theorem/proof head is

```text
e392b4ae69aa3b058ec88ff66bc7635857922e0b
```

GitHub Actions run `31260404317` passes on Python 3.11 and 3.12.

Combined executable verification:

```text
23/23 unit tests PASS
21 exact controls PASS
legacy calibration PASS
triple normal-crossing calibration PASS
```

The triple controls include:

1. nonzero pairwise \(J_{ij}\) with exact \(T_{123}=0\);
2. a wrong-sign alternating formula that fails on the same compatible data;
3. independently corrupted pairwise junction data with \(T_{123}=5\), correctly
   rejected.

## 9. Boundary

This extension does not claim:

- nontransverse or singular triple intersections;
- quadruple or arbitrary higher-normal-crossing formulas;
- global reconstruction from \(T_{123}=0\);
- an independent triple-delta term in \(d\alpha\);
- automatic topological, thermodynamic, microscopic, atomic, chemical, or
  device interpretation of \(T_{123}\).

Those remain separate theorem or domain-adapter problems.
