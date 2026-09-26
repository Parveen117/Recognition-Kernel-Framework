# SC-11 — Seam-Filler Cocycle and Curvature-Interaction Theorem

## 1. Comparison fillers for path composition

Let \(\mathcal C\) be a category of declared path morphisms in a region carrying
the finite multi-seam process structure of SC-10. For each arrow \(a\), choose a
representative oriented path \(\gamma_a\).

For each composable pair

\[
a:x\to y,
\qquad
b:y\to z,
\]

choose an oriented comparison 2-chain \(F(b,a)\) satisfying

\[
\boxed{
\partial F(b,a)
=
\gamma_b+\gamma_a-\gamma_{ba}.
}
\]

Assume the fillers are transverse to the seams. Define their seam memory by

\[
\boxed{
\omega_\Sigma(b,a)
=
\sum_j
\int_{F(b,a)\cap\Sigma_j}R_j.
}
\]

The value lies in an additive coefficient group; the scalar case is displayed
for simplicity.

## 2. Associator comparison cycle

For a composable triple \((c,b,a)\), define

\[
\boxed{
\mathcal A(c,b,a)
=
F(c,ba)+F(b,a)-F(cb,a)-F(c,b).
}
\]

### Lemma 2.1 — The associator comparison is closed

\[
\boxed{
\partial\mathcal A(c,b,a)=0.
}
\]

### Proof

Using the filler boundary law,

\[
\partial(F(c,ba)+F(b,a))
=
\gamma_c+\gamma_b+\gamma_a-\gamma_{cba},
\]

and the same boundary is obtained from

\[
F(cb,a)+F(c,b).
\]

Their difference is therefore a closed 2-chain. ∎

## Theorem 2.2 — Exact seam-memory associator law

The defect of the MR-03 cocycle identity is exactly the seam flux through the
associator comparison cycle:

\[
\boxed{
\begin{aligned}
&\omega_\Sigma(c,ba)+\omega_\Sigma(b,a)
-\omega_\Sigma(cb,a)-\omega_\Sigma(c,b)\\
&\qquad=
\sum_j\int_{\mathcal A(c,b,a)\cap\Sigma_j}R_j.
\end{aligned}
}
\]

### Proof

Substitute the definition of \(\omega_\Sigma\) and use additivity of integration
on oriented chains. The signed sum of the four filler contributions is exactly
the seam-memory functional evaluated on \(\mathcal A(c,b,a)\). ∎

## 3. Curvature interaction term

Define the bulk curvature flux of the associator cycle by

\[
\boxed{
\mathcal B(c,b,a)
=
\sum_k
\int_{\mathcal A(c,b,a)\cap U_k}\Omega_k,
\qquad
\Omega_k=d\alpha_k.
}
\]

Because \(\mathcal A(c,b,a)\) is closed, the multi-seam Stokes law of SC-10 gives

\[
0
=
\int_{\mathcal A(c,b,a)}d\alpha
=
\mathcal B(c,b,a)
+
\sum_j\int_{\mathcal A(c,b,a)\cap\Sigma_j}R_j.
\]

Hence:

## Theorem 3.1 — Cocycle defect equals negative bulk interaction

\[
\boxed{
\omega_\Sigma(c,ba)+\omega_\Sigma(b,a)
-\omega_\Sigma(cb,a)-\omega_\Sigma(c,b)
=
-\mathcal B(c,b,a).
}
\]

This is the exact composition law sought by the multi-seam theory.

## Corollary 3.2 — Flat-bulk seam memory is an MR-03 cocycle

If every bulk region is flat,

\[
\Omega_k=0\qquad\forall k,
\]

then

\[
\boxed{
\omega_\Sigma(c,ba)+\omega_\Sigma(b,a)
=
\omega_\Sigma(cb,a)+\omega_\Sigma(c,b).
}
\]

With normalized identity fillers, \(\omega_\Sigma\) is therefore a normalized
MR-03 memory cocycle and defines an associative memory-lifted category.

Thus:

```text
flat bulk + declared seam fillers
    => seam memory composes cocyclically.
```

## Corollary 3.3 — Curved-bulk interaction is the associativity obstruction

When \(\mathcal B(c,b,a)\neq0\), the seam-memory coordinate alone is not an
associative MR-03 lift. Its failure is not arbitrary:

\[
\boxed{
\delta\omega_\Sigma=-\mathcal B.
}
\]

A faithful Recognition carrier must therefore either:

1. retain the bulk interaction channel together with seam memory; or
2. restrict to a sector in which the associator bulk flux vanishes.

Discarding \(\mathcal B\) and still declaring associative closure is a typed
information loss.

## 4. Relation to gauge memory

The associator cycle is closed. Therefore exact seam-gauge changes from SC-08 do
not change its closed-cycle seam period. The cocycle defect above is consequently
invariant under such gauge re-presentations.

Individual filler values may change by boundary/cochain terms, exactly as in the
MR-03 coboundary picture; the associator defect is the invariant obstruction.

## 5. Exact algebraic calibration

For the one-object integer composition calibration, let

\[
\omega(b,a)=ba.
\]

Then

\[
\delta\omega(c,b,a)=0.
\]

This is the flat-bulk control.

For the deliberately noncocyclic rule

\[
\omega_{\rm bad}(b,a)=ba^2,
\]

the triple \((a,b,c)=(2,3,5)\) gives

\[
\delta\omega_{\rm bad}=60.
\]

The interaction law requires the compensating bulk associator flux

\[
\mathcal B=-60.
\]

The proof lab checks both controls exactly.

## Recognition interpretation

The result answers the composition question in three layers:

\[
\boxed{
\begin{array}{c}
\text{individual disjoint seams}\to\text{additive memory},\\
\text{flat bulk composition}\to\text{MR-03 cocycle},\\
\text{curved bulk composition}\to\text{explicit interaction defect}.
\end{array}
}
\]

So cocyclic path memory is not imposed by vocabulary. It is derived from the
flatness of the bulk associator channel.

## Status

```text
ASSOCIATOR FILLER CYCLE CLOSED                  PROVED
SEAM COCYCLE DEFECT = ASSOCIATOR SEAM FLUX      PROVED
DEFECT = NEGATIVE BULK ASSOCIATOR FLUX           PROVED
FLAT BULK => MR-03 COCYCLE                       PROVED
CURVED BULK INTERACTION TERM                     PROVED
NORMALIZED LIFT UNDER NORMALIZED FILLERS          PROVED VIA MR-03
INTERSECTING-SEAM CODIMENSION-2 JUNCTION LAW      NOT CLAIMED HERE
```
