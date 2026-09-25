# SR-04 — Physical Observer Blindness and Minimum Sensor Repair Theorem

## Public theorem surface

This file publishes the theorem statement, assumptions, consequences, and claim boundary only. The canonical derivation and proof controls are retained in the private IEL proof vault.

Private-proof digest:

```text
IEL3_FINAL_UPGRADED private proof blob: 0c147edcec7eb5df39892491de280c8670bbe894
proof status: PRIVATE_CANONICAL_PROOF
```

## 1. Setup

Let \(V\) be a finite-dimensional response-state space over \(\mathbb F\in\{\mathbb R,\mathbb C\}\). Let

\[
S:V\to Y
\]

be the currently installed physical sensor/observer map, and let

\[
\Pi:V\to T
\]

be the declared technical target. The target may retain independently typed quantities such as endpoint response, thermal response, spectral response, seam memory, junction compatibility, higher-stratum obstruction, or another explicitly declared linear device quantity.

## Theorem 1 — Physical target-faithfulness

The sensor architecture is target-faithful exactly when

\[
\boxed{\ker S\subseteq\ker\Pi.}
\]

Equivalently, there exists a unique linear decoder

\[
L:\operatorname{ran}S\to T
\]

such that

\[
\boxed{\Pi=LS.}
\]

Thus identical sensor output can imply identical declared target only when the sensor representation is target-faithful.

## Theorem 2 — Exact physical blind dimension

Define

\[
\mathcal B_{\rm phys}(S,\Pi)
=
\ker S/(\ker S\cap\ker\Pi).
\]

Then

\[
\boxed{
 b_{\rm phys}
 =\dim\mathcal B_{\rm phys}(S,\Pi)
 =\operatorname{rank}(\Pi|_{\ker S}).
}
\]

For matrix representatives,

\[
\boxed{
 b_{\rm phys}
 =
 \operatorname{rank}
 \begin{pmatrix}S\\\Pi\end{pmatrix}
 -\operatorname{rank}S.
}
\]

## Theorem 3 — Minimum sensor repair

Let

\[
G:V\to\mathbb F^m
\]

be \(m\) supplemental scalar sensing channels. The smallest number of added channels for which the repaired observer \((S,G)\) is target-faithful is

\[
\boxed{
 m_{\min}
 =b_{\rm phys}
 =\operatorname{rank}(\Pi|_{\ker S}).
}
\]

Therefore the theory does not merely report sensor blindness; it gives the exact minimum independent linear sensing burden needed to remove that blindness.

## Corollary 4 — Blind physical witness

If

\[
\ker S\not\subseteq\ker\Pi,
\]

then there exists a nonzero response direction \(v\) such that

\[
\boxed{Sv=0,\qquad \Pi v\neq0.}
\]

Hence two states \(x\) and \(x+v\) may be indistinguishable to the installed sensor architecture while remaining different for the declared technical target.

## Corollary 5 — Differential-obstruction sensor test

For a declared compatibility operator

\[
\partial:V\to W,
\]

set \(\Pi=\partial\). Then the device observer is compatibility-faithful iff

\[
\boxed{\ker S\subseteq\ker\partial.}
\]

If this fails, a sensor-invisible false-closure direction exists:

\[
\boxed{Sv=0,\qquad \partial v\neq0.}
\]

The exact minimum added sensing rank is

\[
\boxed{\operatorname{rank}(\partial|_{\ker S}).}
\]

Important framework instances are \(\partial=D_\Delta\) and, in a finite totalized model, \(\partial=\mathbb D\).

## Corollary 6 — Higher-stratum truncation

If

\[
V=\bigoplus_{k=0}^{n}V^{(k)}
\]

and the installed hardware observes only strata through degree \(r\), then the omitted carrier is

\[
V_{>r}=\bigoplus_{k=r+1}^{n}V^{(k)}.
\]

The truncated sensor is target-faithful iff

\[
\boxed{\Pi|_{V_{>r}}=0,}
\]

and the exact minimum repair burden is

\[
\boxed{m_{\min}=\operatorname{rank}(\Pi|_{V_{>r}}).}
\]

## Device interpretation

This theorem gives the public mathematical contract for a bench device that deliberately demonstrates:

```text
sensor collision
-> hidden target distinction
-> exact blind dimension
-> theorem-minimum sensor repair
-> same specimen/path re-tested after repair.
```

## Claim boundary

```text
FINITE-DIMENSIONAL LINEAR OBSERVER THEORY        PROVED
FAITHFULNESS = DECODABILITY                      PROVED
EXACT BLIND DIMENSION                            PROVED
MINIMUM INDEPENDENT SENSOR REPAIR RANK           PROVED
BLIND FALSE-CLOSURE WITNESS WHEN UNFAITHFUL      PROVED
D_DELTA / mathbb D DEVICE SPECIALIZATION         PROVED AS LINEAR COROLLARY

CONCRETE SENSOR LINEARITY                        REQUIRES DEVICE ADAPTER
REAL-WORLD SENSOR NOISE / UNCERTAINTY             REQUIRES BENCH MODEL
NONLINEAR / TOPOLOGICAL SENSOR COMPLETENESS       NOT CLAIMED
COMPUTATIONAL HARDNESS                            NOT CLAIMED
PRODUCTION SAFETY CERTIFICATION                   NOT CLAIMED
```
