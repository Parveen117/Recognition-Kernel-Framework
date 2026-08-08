# RT-01 - Winding-Sector Stability and Seam-Event Theorem

## 1. Phase carrier

Let
\[
F:[0,1]\times S^1\longrightarrow \mathbb C^\times
\]
be continuous, where
\[
\mathbb C^\times=\mathbb C\setminus\{0\}.
\]

For each \(t\in[0,1]\), define
\[
F_t(z):=F(t,z).
\]

Normalize to the unit circle:
\[
\widehat F_t(z)
=
\frac{F_t(z)}{|F_t(z)|}
\in S^1.
\]

Define the winding sector
\[
\boxed{
\nu(t):=\deg(\widehat F_t)\in\mathbb Z.
}
\]

For a piecewise \(C^1\) representative this agrees with
\[
\nu(t)
=
\frac{1}{2\pi i}
\oint_{S^1}
F_t^{-1}\,dF_t.
\]

## 2. Theorem - winding-sector stability

If \(F\) is continuous and never vanishes, then
\[
\boxed{
\nu(t)=\nu(0)
\qquad
\text{for every }t\in[0,1].
}
\]

### Proof

The map
\[
\widehat F:[0,1]\times S^1\to S^1,
\qquad
\widehat F(t,z)=F(t,z)/|F(t,z)|
\]
is a homotopy between \(\widehat F_0\) and \(\widehat F_t\).
Degree is invariant under homotopy of maps \(S^1\to S^1\).
Therefore
\[
\deg(\widehat F_t)=\deg(\widehat F_0)
\]
for all \(t\). QED.

## 3. Corollary - seam-event necessity

Suppose two admitted phase states have
\[
\nu(0)\ne \nu(1).
\]

Then there is no continuous interpolation
\[
F:[0,1]\times S^1\to\mathbb C^\times
\]
between them.

Equivalently, every continuous interpolation in \(\mathbb C\) must fail the
nonvanishing condition somewhere:
\[
\boxed{
\exists(t_*,z_*):
F(t_*,z_*)=0,
}
\]
or else leave whatever stronger admissible carrier the domain has declared
(for example a spectral-gap, bundle-chart, or invertibility condition).

### Recognition interpretation

A topological sector change is therefore not an ordinary smooth update inside
one admitted sector. It requires an event at which the previous recognition
carrier ceases to be valid.

This event is called a **Recognition-topology seam event**.

The theorem is clock-free: \(t\) is only a homotopy parameter. Any other
continuous parameterization gives the same conclusion.

## 4. Explicit seam witness

The two phase maps
\[
f_0(z)=z,
\qquad
f_1(z)=1
\]
have winding \(1\) and \(0\).

The naive linear interpolation
\[
F(t,z)=(1-t)z+t
\]
hits
\[
F(1/2,-1)=0.
\]

This is not the proof of the theorem; it is a concrete witness of the required
seam in one attempted interpolation.

## 5. Curvature boundary

Nonzero curvature, a large holonomy rate, or a large local response does not by
itself imply
\[
\Delta\nu\ne0.
\]

As long as the phase family remains a continuous map into \(\mathbb C^\times\),
the winding sector is frozen by the theorem above.

Thus any domain-specific trigger of the form

```text
large local detector => integer topological jump
```

requires an additional theorem proving that the trigger forces exit from the
admitted nonvanishing/gapped carrier.

## 6. Claim status

```text
WINDING HOMOTOPY INVARIANCE              PROVED
SEAM-EVENT NECESSITY                     PROVED
CLOCK INDEPENDENCE OF THE STATEMENT      PROVED
EXPLICIT LINEAR-INTERPOLATION SEAM        VERIFIED
CURVATURE ALONE FORCES WINDING JUMP      REJECTED WITHOUT EXTRA HYPOTHESES
PHYSICAL MEANING OF THE SEAM             DOMAIN-DEPENDENT
```
