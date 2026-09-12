# Singularity Calculus Theory v3 — Junction Status

```text
STATUS: RNKE_VERIFIED_SINGULARITY_THEORY_V3_WITH_EXCLUSIONS
```

The v3 extension adds the first certified transverse codimension-two junction layer.

New results:

- **SC-12** — normal-crossing mixed-jump compatibility and proof that `d alpha` has no independent double-delta junction term;
- **SC-13** — stratified Bianchi decomposition with the junction residue
  \[
  J_{12}=\Delta_1\beta_2-\Delta_2\beta_1.
  \]

The central typed Bianchi packet is

\[
\boxed{
\mathfrak B_{\rm strat}
=(d\Omega_{\rm bulk};B_1,B_2;J_{12}).
}
\]

Under the declared transverse regularity assumptions,

\[
\boxed{
d\Omega=0\iff\mathfrak B_{\rm strat}=0.}
\]

For a genuine four-sector piecewise process potential,

\[
\Omega=d\alpha
\]

forces

\[
\boxed{J_{12}=0}
\]

through mixed-jump commutativity and \(d^2\alpha=0\).

Validated theorem head:

```text
431408ff4dadfe13cb917c96e0c46dd3cd8ab048
```

Verification:

```text
19/19 unit tests PASS
18 exact calibration controls PASS
Python 3.11 PASS
Python 3.12 PASS
GitHub Actions run 31259516097 PASS
```

Boundary retained:

- transverse two-seam normal crossings only;
- no independent `delta(rho1) delta(rho2)` term is claimed in `d alpha`;
- nontransverse intersections remain open;
- triple/higher normal-crossing hierarchy remains open;
- global reconstruction of a process potential from arbitrary closed stratified data is not claimed;
- no automatic topological, microscopic, thermodynamic, atomic, chemical, or device interpretation of the junction residue is claimed.
