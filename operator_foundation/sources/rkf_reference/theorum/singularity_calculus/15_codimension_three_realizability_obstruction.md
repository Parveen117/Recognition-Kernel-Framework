# SC-15 — Codimension-Three Realizability Obstruction Theorem

## 1. Independently declared pairwise junction data

Keep the transverse three-seam geometry of SC-14, but now suppose the pairwise
junction residues

\[
J_{12},\qquad J_{13},\qquad J_{23}
\]

are supplied independently, each with the two one-sided traces required to take
the remaining jump.

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

## Theorem 1.1 — Triple-obstruction no-go theorem

If there exist compatible seam data \(\beta_1,\beta_2,\beta_3\) such that

\[
J_{12}=\Delta_1\beta_2-\Delta_2\beta_1,
\]

\[
J_{13}=\Delta_1\beta_3-\Delta_3\beta_1,
\]

and

\[
J_{23}=\Delta_2\beta_3-\Delta_3\beta_2,
\]

then necessarily

\[
\boxed{T_{123}=0.}
\]

Equivalently,

\[
\boxed{
T_{123}\neq0
\Longrightarrow
\text{no compatible lower-stratum seam realization exists.}
}
\]

### Proof

The forward implication is SC-14. The displayed obstruction statement is its
contrapositive. ∎

## 2. Important converse boundary

The condition

\[
T_{123}=0
\]

is a necessary local normal-crossing compatibility condition. It is **not** by
itself a theorem of global realizability.

A global reconstruction theorem would additionally need topology, regularity,
cohomological, support, and boundary hypotheses. None are silently inserted here.

Thus

```text
T_123 != 0  => definite incompatibility
T_123 == 0  => passes this gate only
```

## 3. Compatibility versus closure

SC-13 gives the pairwise junction residues as part of the Bianchi closure packet.
If the original stratified curvature itself is required to be closed, then one
already demands

\[
J_{12}=J_{13}=J_{23}=0,
\]

and hence \(T_{123}=0\) automatically.

SC-15 addresses a different question: whether a **nonclosed but internally
consistent** lower-stratum packet can be propagated through a triple normal
crossing without violating the next compatibility law.

This distinction matters:

\[
\boxed{
\text{pairwise junction closure}
\neq
\text{triple realizability compatibility}.
}
\]

## 4. Triple Recognition packet

For declared pairwise junction data define

\[
\boxed{
\mathfrak J_3
=
(J_{12},J_{13},J_{23};T_{123}).
}
\]

The first three entries record the pairwise junction channels. The final entry is
the codimension-three realizability obstruction.

The correct fail-closed rule is:

\[
\boxed{
T_{123}\neq0
\Longrightarrow
\operatorname{REJECT\_COMPATIBILITY}.
}
\]

It is not lawful to average the four entries or allow cancellation between them.

## 5. Exact sign control

The alternating sign in

\[
T_{123}
=
\Delta_1J_{23}-\Delta_2J_{13}+\Delta_3J_{12}
\]

is structural. Replacing the middle minus sign by a plus sign generally gives a
nonzero value even for compatible seam-derived data.

The proof lab includes such a negative control, so a sign regression is detected
rather than cosmetically tolerated.

## 6. Relation to the Recognition hierarchy

The current stratified chain is

\[
\boxed{
\text{bulk}
\to
\text{seam}
\to
\text{pairwise junction}
\to
\text{triple compatibility}.
}
\]

SC-11 concerns associator/filler composition. SC-13 concerns pairwise geometric
junction Bianchi closure. SC-14/15 concern the next normal-crossing compatibility
of those junction channels. These are separate typed obligations.

## Status

```text
TRIPLE OBSTRUCTION T_123                         DEFINED
T_123 != 0 => NO COMPATIBLE SEAM REALIZATION     PROVED
T_123 = 0 => GLOBAL REALIZABILITY                 NOT CLAIMED
PAIRWISE CLOSURE VS TRIPLE COMPATIBILITY          SEPARATED
WRONG-SIGN ALTERNATING LAW                        REJECTED BY NEGATIVE CONTROL
HIGHER CODIMENSION GENERALIZATION                 OPEN / NEXT LAYER
```