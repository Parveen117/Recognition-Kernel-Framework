# Constrained Homotopy Groupoid and Variational Length

## Provenance

```text
source repository: Parveen117/MP
source PR: #57
source theorem: adapters/common/CONSTRAINED_HOMOTOPY_GROUPOID.md
```

## 1. Constrained state

A continuum sector carries

\[
(A,\varphi;
\text{hierarchy itinerary},
\nu,
\mathfrak m,
\Phi,
\text{seam class}),
\]

where \(A\) is the connection path, \(\varphi\) is a lifted phase, \(\nu\) is winding, \(\mathfrak m\) is memory, and \(\Phi\) is lifted curvature flux.

The endpoint transport is

\[
U_A=\mathcal P\exp\!\int A(t)\,dt,
\]

and the phase lift obeys

\[
\varphi(1)-\varphi(0)=2\pi\nu.
\]

## 2. Guarded groupoid

A declared morphism may combine:

- orientation-preserving reparameterization;
- constant \(SU(2)\) gauge conjugation;
- an admissible homotopy preserving the complete ledger;
- endpoint holonomies related by gauge conjugacy.

Identity, inverse, and composition laws hold for the declared finite compatibility packet. The theorem does not claim existence of a smooth constrained homotopy for every formally compatible pair.

## 3. Variational functional

For nonnegative coefficients \(c,\alpha,\beta,\gamma\), define

\[
\mathcal L
=c\int\|A(t)\|\,dt
+\alpha\int|\dot\varphi(t)|\,dt
+\beta W(\mathfrak m)
+\gamma\|\Phi\|.
\]

The coefficients are calibrations, not canonical universal constants.

## 4. Universal lower-bound theorem

Let \(\theta(U)\) denote the principal \(SU(2)\) conjugacy angle. Then

\[
\boxed{
\mathcal L
\ge
c\,\theta(U_A)
+2\pi\alpha|\nu|
+\beta W(\mathfrak m)
+\gamma\|\Phi\|.
}
\]

The proof uses:

- the geodesic-distance lower bound for connection length;
- total variation of the lifted phase;
- nonnegativity of the protected memory and curvature terms.

The bound is saturated in the declared principal-geodesic, monotone-phase calibration class.

## 5. Positivity boundary

The constrained infimum is strictly positive whenever at least one protected invariant entering the lower bound is nonzero with a positive coefficient.

A sector with

```text
identity holonomy
zero winding
empty memory
zero curvature flux
```

may still have zero lower bound. Composition-primitivity alone does not prohibit collapse.

## 6. Composition subadditivity

For compatible sectors,

\[
\ell_{\min}(C_2\circ C_1)
\le
\ell_{\min}(C_1)+\ell_{\min}(C_2).
\]

The explicit lower-bound expression is also subadditive by the triangle inequalities for the conjugacy angle, integer winding, and curvature norm.

## 7. Ledger-preserving obstruction

An identity-holonomy sector with nonzero winding cannot be constrained-equivalent to the trivial zero-winding sector because

\[
\mathcal L\ge2\pi\alpha|\nu|.
\]

Thus a visible endpoint may close while a protected lifted ledger prevents contraction.

## Claim boundary

```text
DECLARED CONSTRAINED GROUPOID LAWS        PROVED IN FINITE AUDIT
VARIATIONAL LOWER BOUND                  PROVED
WINDING / MEMORY / FLUX POSITIVITY       PROVED WHEN WEIGHTED
COMPOSITION SUBADDITIVITY                PROVED
ZERO-LEDGER COLLAPSE POSSIBILITY        RETAINED

CANONICAL COEFFICIENTS                  NOT PROVED
ALL SMOOTH CONSTRAINED HOMOTOPIES       NOT CLASSIFIED
GENERAL MINIMIZER EXISTENCE             OPEN AT THIS STAGE
CURVATURE-DERIVED NO-COLLAPSE           NEXT THEOREM LAYER
```
