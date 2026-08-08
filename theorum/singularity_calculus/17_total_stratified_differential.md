# SC-17 — Total Stratified Differential Theorem

## 1. Bigraded normal-crossing carrier

Let the finite normal-crossing jump complex of SC-16 carry differential forms on
each stratum. Write

\[
C^{p,q}
=
\bigoplus_{|I|=q}\Omega^p(A_I),
\]

where \(p\) is ordinary form degree and \(q\) is codimension/jump degree.

Let

\[
d:C^{p,q}\to C^{p+1,q}
\]

be the stratumwise exterior derivative and

\[
D_\Delta:C^{p,q}\to C^{p,q+1}
\]

be the alternating jump differential of SC-16.

Assume jump/restriction commutes with exterior differentiation on every
normal-crossing square:

\[
\boxed{dD_\Delta=D_\Delta d.}
\]

This is the ordinary compatibility of pullback/trace with \(d\).

## 2. Total differential

For a homogeneous element \(c\in C^{p,q}\), define

\[
\boxed{
\mathbb D c
=
dc+(-1)^pD_\Delta c.
}
\]

The total degree is \(p+q\).

## Theorem 2.1 — Total nilpotence

Under

\[
d^2=0,
\qquad
D_\Delta^2=0,
\qquad
dD_\Delta=D_\Delta d,
\]

one has

\[
\boxed{\mathbb D^2=0.}
\]

### Proof

Let \(c\in C^{p,q}\). Since \(dc\) has form degree \(p+1\),

\[
\mathbb D(dc)
=
d^2c+(-1)^{p+1}D_\Delta dc.
\]

Since \(D_\Delta c\) still has form degree \(p\),

\[
\mathbb D((-1)^pD_\Delta c)
=
(-1)^pdD_\Delta c+D_\Delta^2c.
\]

Therefore

\[
\mathbb D^2c
=
(-1)^{p+1}D_\Delta dc
+(-1)^pdD_\Delta c.
\]

Using \(dD_\Delta=D_\Delta d\), the two cross terms cancel, so

\[
\mathbb D^2c=0.
\]

∎

## Corollary 2.2 — One differential controls smooth and stratified compatibility

The total complex

\[
\boxed{
\operatorname{Tot}^r
=
\bigoplus_{p+q=r}C^{p,q}
}
\]

with differential \(\mathbb D\) packages ordinary differential closure and
normal-crossing compatibility into one nilpotent operator.

Thus the chain

```text
bulk exterior derivative
+ seam jump
+ junction jump
+ higher normal-crossing jumps
```

is not a collection of unrelated rules. It is a single total complex under the
declared compatibility hypotheses.

## 3. Sign necessity

The sign \((-1)^p\) is structural. If one instead uses

\[
\mathbb D_{\rm bad}=d+D_\Delta,
\]

then for a form of even degree the cross terms add:

\[
\mathbb D_{\rm bad}^2c
=2dD_\Delta c
\]

in characteristic different from two, which is generally nonzero.

The proof lab contains a negative control that detects this wrong-sign totalization.

## 4. Recognition interpretation

The total differential separates two independent questions while preserving their
compatibility:

\[
\boxed{
\text{smooth nonclosure}
\quad\text{and}\quad
\text{stratified nonclosure}.
}
\]

A valid representation must preserve both components. A vanishing scalar summary
cannot replace \(\mathbb D\)-closure.

## 5. Boundary

This theorem is algebraic/differential-geometric. It does not assert:

- that every closed total cochain comes from a global process potential;
- exactness of the total complex;
- a universal physical meaning for total cohomology;
- validity at nontransverse singular intersections;
- infinite-dimensional analytic closure without extra hypotheses.

## Status

```text
BIGRADED STRATIFIED CARRIER                    DEFINED
STRATUMWISE d                                  STANDARD
JUMP DIFFERENTIAL D_DELTA                      SC-16
COMMUTATION d D_DELTA = D_DELTA d              ASSUMED NORMAL-CROSSING COMPATIBILITY
TOTAL DIFFERENTIAL mathbb D                    DEFINED
mathbb D^2 = 0                                 PROVED
WRONG-SIGN TOTALIZATION                        REJECTED / NEGATIVE CONTROL
GLOBAL EXACTNESS                               NOT CLAIMED
```