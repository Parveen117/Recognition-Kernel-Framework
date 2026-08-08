# Source Audit

This file records what was accepted, corrected, rejected, or left open from the
source draft.

| Source item | Audit status | Canonical treatment |
|---|---|---|
| TVSP space is complete and needs no other variables | POSTULATE / unsupported | not promoted |
| seam ratios are always invariant | AXIOM / domain assumption | not promoted as universal theorem |
| seam rotation preserves ratios | conditional geometric statement | not needed for singularity core |
| closed exact thermodynamic form gives Maxwell relations | useful after correction | SC-02 |
| `(T,V) -> (V,T)` has rank drop / determinant zero | **false** | SC-01 proves determinant `-1` |
| orientation reversal creates the singularity | **false as stated** | SC-01 no-singularity theorem |
| `d(d Phi)=Omega !=0` | **false for smooth Phi** | SC-02 replaces with `Omega=d alpha` |
| Maxwell-defect 2-form | useful | SC-02 |
| curvature directly generalizes Onsager as `L_pv-L_vp=Omega(Gamma)` | unsupported typing/representation | not promoted |
| seam derivative `d theta/d tau` is coordinate-free/native | overbroad; parameter dependent | existing clock-free calculus supersedes |
| seam rotation alone guarantees continuity | unsupported | not promoted |
| winding change requires seam event | already proved more carefully | Recognition Topology, not duplicated |
| curvature threshold automatically updates winding | unsupported | explicitly not promoted |
| atomic shell/periodic table from seam capacity | unsupported | not promoted |
| `2n^2` derived from seam geometry | derivation absent | not promoted |
| bond/valence theorems | definitions/speculation | not promoted |
| device examples | engineering examples only | not theorem-certified |

## New mathematics extracted from the source intuition

The most useful development did **not** survive verbatim. It emerged by asking
what a mathematically lawful "singularity 2-form" should be.

For a piecewise-smooth process form

\[
\alpha=\alpha_-+H(\rho)(\alpha_+-\alpha_-),
\]

the correct distributional curvature is

\[
d\alpha
=
d\alpha_-+H(\rho)(d\alpha_+-d\alpha_-)
+\delta(\rho)d\rho\wedge(\alpha_+-\alpha_-).
\]

This formula gives the source's intended "singularity curvature" a precise
meaning without violating \(d^2=0\).

## Build audit of raw source

The raw source also fails a direct LaTeX build before theorem content is reached:
it redeclares `\div`, which is already defined. Therefore the source was not
treated as a publication-ready manuscript.

That build issue is secondary to the mathematical corrections above.
