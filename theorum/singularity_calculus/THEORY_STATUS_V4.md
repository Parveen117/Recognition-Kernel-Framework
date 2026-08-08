# Singularity Calculus Theory v4 Status

```text
STATUS: RNKE_VERIFIED_SINGULARITY_THEORY_V4_WITH_EXCLUSIONS
```

The v4 extension adds two certified results to the SC-01 through SC-13 theory:

- **SC-14** — Triple Normal-Crossing Alternating-Junction Theorem;
- **SC-15** — Codimension-Three Realizability Obstruction Theorem.

Central compatibility law:

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

For compatible seam-derived junction data,

\[
\boxed{T_{123}=0.}
\]

For independently declared pairwise junction data,

\[
\boxed{
T_{123}\neq0
\Rightarrow
\text{no compatible lower-stratum seam realization exists.}
}
\]

The triple Recognition packet is

\[
\boxed{
\mathfrak J_3=(J_{12},J_{13},J_{23};T_{123}).
}
\]

Verification at theorem/proof head `e392b4ae69aa3b058ec88ff66bc7635857922e0b`:

```text
legacy suite: 19/19 PASS
triple suite: 4/4 PASS
combined: 23/23 PASS
legacy exact controls: 18 PASS
triple exact controls: 3 PASS
combined exact controls: 21 PASS
Python 3.11 PASS
Python 3.12 PASS
GitHub Actions run 31260404317 PASS
```

Boundary retained:

- transverse regular three-seam normal crossings only;
- no triple-delta term is asserted in first curvature `d alpha`;
- `T_123 = 0` is necessary local compatibility, not a global reconstruction theorem;
- nontransverse intersections remain open;
- quadruple and arbitrary higher-normal-crossing hierarchy remains open;
- no automatic topological, thermodynamic, microscopic, atomic, chemical, or device interpretation is claimed.
