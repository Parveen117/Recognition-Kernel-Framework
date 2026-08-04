# Cut-Graded Universal Generator Theorem

## 1. Purpose

The uploaded universal-generator manuscript proposes a primitive exponential
flow \(e^{tG}\), derived cut/join operators, an eight-step closure condition, a
four-component Hyperoperator, and an Eye fixed point. The Recognition-Kernel
Framework changes the order of construction:

```text
carrier and primitive cut
-> closed generator
-> cut-even / cut-odd decomposition
-> bilateral exponential reconstruction
-> cut-loop memory and seam curvature
-> periodic / antiperiodic closure spectrum
-> clock-free Eye
-> target-faithful component observer.
```

The theorem below does not declare a physical generator to be universal. It
identifies the exact algebra that every lawful cut-graded generator
representation must satisfy.

---

## 2. Cut-graded generator

Let \(\mathcal H\) be a Hilbert space. Let

\[
J=J^*=J^{-1}
\]

be a unitary self-adjoint involution. Let \(G\) be a bounded operator. For an
unbounded generator, assume throughout that

\[
J\operatorname{Dom}(G)=\operatorname{Dom}(G)
\]

and that all products below are evaluated on a common invariant core before
closure.

Define

\[
\boxed{
G_{\mathrm e}
=\frac12(G+JGJ),
\qquad
G_{\mathrm o}
=\frac12(G-JGJ).
}
\tag{2.1}
\]

### Theorem 2.1 (Unique cut grading)

One has

\[
\boxed{G=G_{\mathrm e}+G_{\mathrm o},}
\tag{2.2}
\]

\[
\boxed{
JG_{\mathrm e}J=G_{\mathrm e},
\qquad
JG_{\mathrm o}J=-G_{\mathrm o}.
}
\tag{2.3}
\]

This decomposition is unique.

If

\[
P_\pm=\frac{I\pm J}{2},
\]

then

\[
P_+G_{\mathrm e}P_-=P_-G_{\mathrm e}P_+=0,
\tag{2.4}
\]

and

\[
P_+G_{\mathrm o}P_+=P_-G_{\mathrm o}P_-=0.
\tag{2.5}
\]

Thus \(G_{\mathrm e}\) preserves the two cut sheets and \(G_{\mathrm o}\)
transports between them.

#### Proof

Equations (2.2)--(2.3) follow directly from \(J^2=I\). If
\(G=A+B\) with \(JAJ=A\) and \(JBJ=-B\), then

\[
A=\frac12(G+JGJ),
\qquad
B=\frac12(G-JGJ),
\]

so the decomposition is unique. Equations (2.4)--(2.5) follow from
\(JP_\pm=\pm P_\pm\). \(\square\)

---

## 3. Bilateral exponential reconstruction

Assume now that the generator is cut odd:

\[
JGJ=-G.
\tag{3.1}
\]

Let \(U_t=e^{tG}\). Functional calculus gives

\[
\boxed{JU_tJ=U_{-t}.}
\tag{3.2}
\]

Define the even and odd flow channels

\[
E_t=\frac12(U_t+U_{-t})=\cosh(tG),
\tag{3.3}
\]

\[
O_t=\frac12(U_t-U_{-t})=\sinh(tG).
\tag{3.4}
\]

### Theorem 3.1 (Bilateral flow reconstruction)

The channels satisfy

\[
JE_tJ=E_t,
\qquad
JO_tJ=-O_t,
\tag{3.5}
\]

\[
\boxed{
U_t=E_t+O_t,
\qquad
U_{-t}=E_t-O_t,
}
\tag{3.6}
\]

and

\[
\boxed{E_t^2-O_t^2=I.}
\tag{3.7}
\]

#### Proof

Equations (3.5)--(3.6) follow from (3.2). Since \(E_t\) and \(O_t\) are
functions of the same generator, they commute. Therefore

\[
E_t^2-O_t^2
=
\frac14\left[(U_t+U_{-t})^2-(U_t-U_{-t})^2\right]
=
U_tU_{-t}
=
I.
\]

\(\square\)

Define the derived finite channels

\[
\widehat J_t=U_t+U_{-t}=2\cosh(tG),
\qquad
\widehat C_t=U_t-U_{-t}=2\sinh(tG).
\tag{3.8}
\]

### Corollary 3.2 (Exponential cut-square identity)

\[
\boxed{\widehat J_t^2-\widehat C_t^2=4I,}
\tag{3.9}
\]

and

\[
\boxed{
\widehat J_t\widehat C_t
=
\widehat C_t\widehat J_t
=
U_{2t}-U_{-2t}
=
2\sinh(2tG).
}
\tag{3.10}
\]

The two products are equal. A formula assigning a different value to
\(\widehat C_t\widehat J_t\) is incompatible with both operators being
functions of the same generator.

---

## 4. Cut-loop memory and seam curvature

For a general bounded generator, define the cut loop

\[
\boxed{
\mathscr H_J(t)
=
JU_tJU_t
=
e^{tJGJ}e^{tG}.
}
\tag{4.1}
\]

### Theorem 4.1 (Cut-loop extraction theorem)

The cut loop has the exact local expansion

\[
\mathscr H_J(t)
=
I
+
2tG_{\mathrm e}
+
t^2\left(
2G_{\mathrm e}^2
+
[G_{\mathrm e},G_{\mathrm o}]
\right)
+
O(t^3).
\tag{4.2}
\]

Equivalently,

\[
\boxed{
\log\mathscr H_J(t)
=
2tG_{\mathrm e}
+
t^2[G_{\mathrm e},G_{\mathrm o}]
+
O(t^3).
}
\tag{4.3}
\]

Hence

\[
\boxed{
G_{\mathrm e}
=
\frac12
\left.\frac{d}{dt}\right|_{t=0}
\mathscr H_J(t),
}
\tag{4.4}
\]

and the first noncommutative seam-curvature coefficient is

\[
\boxed{
\mathcal R_{\mathrm{seam}}
=
[G_{\mathrm e},G_{\mathrm o}].
}
\tag{4.5}
\]

Moreover,

\[
\boxed{
\mathscr H_J(t)=I
\text{ for all sufficiently small }t
\iff
G_{\mathrm e}=0.
}
\tag{4.6}
\]

#### Proof

Write \(JGJ=G_{\mathrm e}-G_{\mathrm o}\) and
\(G=G_{\mathrm e}+G_{\mathrm o}\). Multiplying the two exponential series
gives (4.2). The second-order logarithm identity

\[
\log(I+tA+t^2B+O(t^3))
=
tA+t^2\left(B-\frac12A^2\right)+O(t^3)
\]

gives (4.3). Equation (4.4) follows. If the loop is locally the identity,
its first derivative vanishes, hence \(G_{\mathrm e}=0\). Conversely,
\(G_{\mathrm e}=0\) gives \(JGJ=-G\), so
\(\mathscr H_J(t)=U_{-t}U_t=I\). \(\square\)

Interpretation:

```text
G_even                    seam-preserving memory, cost, or dissipation
G_odd                     reversible trans-cut motion
[G_even,G_odd]            first non-Abelian memory/transport coupling
cut-loop identity         exact cut reversibility
```

---

## 5. Periodic and antiperiodic closure spectrum

Let \(G\psi=i\omega\psi\), with \(\omega\in\mathbb R\). For a step number
\(N\ge1\),

\[
U_N\psi=e^{iN\omega}\psi.
\]

### Theorem 5.1 (Closure-character classification)

\[
U_N\psi=+\psi
\iff
N\omega\in2\pi\mathbb Z,
\tag{5.1}
\]

and

\[
U_N\psi=-\psi
\iff
N\omega\in(2\mathbb Z+1)\pi.
\tag{5.2}
\]

Equivalently, for

\[
D_{N,\sigma}=U_N-\sigma I,
\qquad
\sigma\in\{+1,-1\},
\tag{5.3}
\]

the positive closure source

\[
\boxed{
S_{N,\sigma}
=
D_{N,\sigma}^*D_{N,\sigma}
\ge0
}
\tag{5.4}
\]

satisfies

\[
\boxed{
\ker S_{N,\sigma}
=
\ker(U_N-\sigma I).
}
\tag{5.5}
\]

The \(+1\) and \(-1\) sectors are distinct. A proof using only
\(N\lambda=2\pi i m\) covers the periodic sector but omits the antiperiodic
sector.

---

## 6. Clock-free Eye theorem

Suppose \(U_t=e^{-itH}\), where \(H=H^*\).

### Theorem 6.1 (Stroboscopic versus clock-free Eye)

The one-step fixed space is

\[
\boxed{
\operatorname{Fix}(U_1)
=
E_H(2\pi\mathbb Z)\mathcal H.
}
\tag{6.1}
\]

The all-time fixed space is

\[
\boxed{
\bigcap_{t\in\mathbb R}\operatorname{Fix}(U_t)
=
\ker H.
}
\tag{6.2}
\]

The mean-ergodic Eye projector is

\[
\boxed{
P_{\mathrm{Eye}}
=
\operatorname*{s-lim}_{T\to\infty}
\frac1T\int_0^T U_t\,dt
=
E_H(\{0\}).
}
\tag{6.3}
\]

Therefore

\[
\operatorname{Fix}(U_1)=\ker H
\]

only when the spectral support contains no nonzero integer multiple of
\(2\pi\).

The quotient

\[
\boxed{
\mathfrak B_{\mathrm{clock}}
=
\operatorname{Fix}(U_1)/\ker H
}
\tag{6.4}
\]

is the stroboscopic recognition-blind sector.

---

## 7. Component observer theorem

Let \(P_1,\ldots,P_m\) be pairwise orthogonal projections with

\[
\sum_{a=1}^mP_a=I.
\]

Define

\[
G_a=P_aG,
\qquad
\mathcal A_Gx=(G_1x,\ldots,G_mx).
\tag{7.1}
\]

### Theorem 7.1 (Faithful orthogonal component observer)

\[
\boxed{
\mathcal A_G^*\mathcal A_G
=
\sum_{a=1}^mG_a^*G_a
=
G^*G.
}
\tag{7.2}
\]

Consequently,

\[
\boxed{\ker\mathcal A_G=\ker G.}
\tag{7.3}
\]

Thus a complete orthogonal output decomposition creates no additional blind
kernel.

If the named components are not known to arise from pairwise orthogonal
complete projections, the lawful observer is still the direct sum
\(\mathcal A_G\), not merely the aggregate \(\sum_aG_a\). The aggregate can
vanish by cancellation while the direct-sum energy remains positive. The
negative control in the exact certificate verifies this distinction.

---

## 8. Relation to the Recognition-Kernel Theorem

For an observer \(B:\mathcal H\to\mathcal Y\) and sample times
\(\mathbf t=(t_1,\ldots,t_N)\), define

\[
\mathcal A_{\mathbf t}x
=
(BU_{t_1}x,\ldots,BU_{t_N}x).
\tag{8.1}
\]

For a target functional \(L\), define

\[
\beta_{\mathbf t}(L)
=
\sup_{\mathcal A_{\mathbf t}x\ne0}
\frac{|Lx|^2}{\|\mathcal A_{\mathbf t}x\|^2}.
\tag{8.2}
\]

Whenever \(\beta_{\mathbf t}(L)<\infty\), the Recognition-Kernel Theorem gives
a unique minimum decoder

\[
c_L\in\overline{\operatorname{Ran}\mathcal A_{\mathbf t}}
\]

such that

\[
Lx=\langle\mathcal A_{\mathbf t}x,c_L\rangle,
\qquad
\|c_L\|^2=\beta_{\mathbf t}(L),
\tag{8.3}
\]

and

\[
\boxed{
\mathcal A_{\mathbf t}^*\mathcal A_{\mathbf t}-L^*L\ge0
\iff
\beta_{\mathbf t}(L)\le1.
}
\tag{8.4}
\]

This is the precise target-relative meaning of the cost required to recognize
a flow state.

---

## 9. Correction of the proposed generator tower

The recursion

\[
G_{n+1}=2\sinh(G_n)
\tag{9.1}
\]

does not converge to zero for a general real initial value. The scalar map has

\[
f'(0)=2>1,
\]

so zero is repelling. Its lawful use is as the finite cut-response coordinate

\[
C(G)=2\sinh(G/2),
\tag{9.2}
\]

with inverse, wherever the functional calculus permits,

\[
\boxed{
G=2\operatorname{arsinh}(C(G)/2).
}
\tag{9.3}
\]

Repeated application has no convergence meaning unless a separate
renormalization theorem is supplied.

---

## 10. Exact certificate

The deterministic proof-lab packet verifies with exact rational arithmetic:

```text
unique cut-even/cut-odd decomposition;
cut-diagonal and trans-cut block support;
cut-loop linear memory coefficient;
cut-loop quadratic seam-curvature coefficient;
exact odd nilpotent bilateral flow;
exponential cut-square identity;
equality of the two derived cut/join products;
periodic and antiperiodic closure characters;
single-step versus all-time Eye;
orthogonal component Gram preservation;
nonorthogonal aggregate cancellation negative control.
```

No NumPy, floating point, fitted unitary, source inverse, or post-hoc Gram
factor is used.

Expected status:

```text
PASS_CUT_GRADED_UNIVERSAL_GENERATOR_CANDIDATE
```

Expected certificate hash:

```text
34afc44543cd83cacd96cbced32b77f5fdd765c28fbaf81105d0d2063cf5f36e
```

---

## 11. Claim boundary

```text
CUT-GRADED BOUNDED-OPERATOR THEOREM                    PROVED
BILATERAL EXPONENTIAL RECONSTRUCTION                   PROVED
EXPONENTIAL CUT-SQUARE                                 PROVED
CUT-LOOP MEMORY / SEAM-CURVATURE EXPANSION             PROVED
PERIODIC / ANTIPERIODIC CLOSURE CLASSIFICATION         PROVED
CLOCK-FREE EYE DISTINCTION                             PROVED
ORTHOGONAL COMPONENT OBSERVER                         PROVED
EXACT FINITE CERTIFICATE                               IMPLEMENTED / USER RUN REQUIRED

UNBOUNDED UNIVERSAL-GENERATOR DOMAIN THEOREM           REQUIRES DOMAIN PINS
PHYSICAL IDENTIFICATION OF ONE UNIVERSAL GENERATOR     NOT CLAIMED
MASTER COST/MEMORY FLOW AS ONE CLOSED GENERATOR        NEXT DEVELOPMENT
CENTRAL MANUSCRIPT PROMOTION                           HELD UNTIL USER PASS
```
