# Verified Theory Status — Singularity Calculus

```text
STATUS: RNKE_VERIFIED_SINGULARITY_THEORY_WITH_EXCLUSIONS
```

The current verified theory is the integrated SC-01 through SC-09 chain in
`VERIFIED_THEORY.md`.

The central typed closure packet is

\[
\boxed{
\mathfrak C_{\rm sing}
=
(\Omega_-,\Omega_+,R_\Sigma).
}
\]

The master theorem is

\[
\boxed{
d\alpha=0
\iff
\Omega_-=0,\quad
\Omega_+=0,\quad
R_\Sigma=0.
}
\]

Additional verified theory consequences include:

- seam-supported distributional curvature from non-smooth gluing;
- removability iff the tangential seam residue vanishes;
- seam residue gauge class modulo exact seam forms;
- gauge-invariant closed-cycle seam periods;
- exact Seam-Stokes memory;
- regular/singular typed non-cancellation;
- piecewise-enthalpy bulk/seam decomposition.

Validation at theory issue time:

```text
12/12 unit tests PASS
11 exact calibration controls PASS
Python 3.11 CI PASS
Python 3.12 CI PASS
validated workflow run: 31258495202
```

This is not a formal proof-assistant certificate and is not a claim of a universal
physical theory. Topological, operator-spectral, microscopic, chemical, atomic,
and device interpretations require separate adapters.
