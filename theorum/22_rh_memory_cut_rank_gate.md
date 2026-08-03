# RH Target Gate: Native Cut-Generated Objects and Five-Memory Faithfulness

## Permanent doctrine

The completed-Weil source, boundary, memory bridge and finite seam matrix are
not imported as independent operator-theoretic objects.  They must be generated
from one native cut-event lift.

Classical operator algebra is allowed only as a shadow which tells us what an
already constructed map should resemble.  It does not define the map.

The primitive data are

```text
exact exponential change flow;
cut projector pair P,Q;
native event lift Z;
declared target observer T_Sigma.
```

Everything else must be derived.

---

## 1. Primitive cut system

Let \(\mathcal F\) be the native generator core and \(\mathcal K\) the event
carrier.  Let

\[
\alpha_t(a)=U_t^*aU_t,
\qquad
U_t=e^{itG},
\]

be the exact exponential change flow.  The finite-time flow is primitive; no
infinitesimal truncation is used to define the event family.

Let

\[
Z_t:\mathcal F\longrightarrow\mathcal K
\]

be the cut-generated event lift.  In an event representation one may write

\[
Z_t f=\pi(\alpha_t(a_f))\Omega,
\]

but \(a_f\), \(\pi\), and \(\Omega\) are bookkeeping for the native event
construction, not classical imports.

Let

\[
P=P^*=P^2,
\qquad
Q=I-P,
\qquad
PQ=QP=0,
\]

be the recognized and cut-memory projectors.  Define the cut involution

\[
\mathfrak j_{\rm cut}=P-Q.
\]

Then

\[
\mathfrak j_{\rm cut}^*=\mathfrak j_{\rm cut},
\qquad
\mathfrak j_{\rm cut}^2=I.
\]

---

## 2. Objects derived from the cut

The single lift \(Z_t\) generates four canonical forms:

\[
S_t=Z_t^*Z_t,
\]

\[
R_t=Z_t^*PZ_t,
\]

\[
D_t=Z_t^*QZ_t,
\]

and

\[
F_t=Z_t^*\mathfrak j_{\rm cut}Z_t=R_t-D_t.
\]

The exact cut decomposition is

\[
\boxed{S_t=R_t+D_t.}
\]

Thus source energy, recognized energy, cut-memory energy and signed cut form
are not separately postulated.  They are shadows of the same event lift under
\(I,P,Q,P-Q\).

If \(P=|p\rangle\langle p|\) has rank one and

\[
L_t(f)=\langle p,Z_tf\rangle,
\]

then

\[
R_t=L_t^*L_t
\]

and therefore

\[
\boxed{S_t-L_t^*L_t=D_t=Z_t^*QZ_t\ge0.}
\]

This is the infinite-dimensional Cut-Square Identity before coordinates are
chosen.

---

## 3. Exact exponential covariance

Transport the cut with the exact flow:

\[
Z_t=U_tZ_0,
\qquad
P_t=U_tP_0U_t^*,
\qquad
Q_t=U_tQ_0U_t^*.
\]

Then

\[
Z_t^*P_tZ_t=Z_0^*P_0Z_0,
\qquad
Z_t^*Q_tZ_t=Z_0^*Q_0Z_0.
\]

Thus the cut-generated forms are exactly path-covariant under finite exponential
change.  The classical Lax or unitary-conjugation formula is merely a coordinate
shadow of this native transport.

---

## 4. Full memory versus target-relevant memory

The full cut bridge

\[
C_t=Q_tZ_t
\]

may have infinite rank.  The framework does **not** claim that the full cut
carrier is five-dimensional.

Let

\[
T_\Sigma:\mathcal K\longrightarrow\mathbb C^\nu,
\qquad
\nu\le5,
\]

be the declared target observer.  It is required to be a coisometry on its
range:

\[
T_\Sigma T_\Sigma^*=I_\nu.
\]

Define the target-visible cut bridge

\[
A_\Sigma=T_\Sigma C_t.
\]

The exact target-faithfulness condition is

\[
\boxed{C_t=T_\Sigma^*T_\Sigma C_t}
\]

on the adverse target-relevant cut module.  Equivalently, the hidden residual

\[
H_\Sigma=(I-T_\Sigma^*T_\Sigma)C_t
\]

vanishes there.

This condition, not unitary covariance and not numerical rank thresholding,
is the theorem which licenses the five-dimensional reduction.

---

## 5. Native target-memory rank theorem

### Theorem A (Cut-derived target-memory rank)

If

\[
C_t=T_\Sigma^*T_\Sigma C_t
\]

on the target-relevant adverse module, then

\[
\operatorname{rank}C_t\le\nu\le5
\]

on that module, and

\[
D_t=C_t^*C_t=A_\Sigma^*A_\Sigma.
\]

Moreover, the nonzero spectrum of \(D_t\) is exactly the nonzero spectrum of

\[
B_\Sigma^{\rm cut}=A_\Sigma A_\Sigma^*
\in M_\nu(\mathbb C).
\]

### Proof

The faithfulness identity factors the cut bridge through
\(T_\Sigma^*:\mathbb C^\nu\to\mathcal K\):

\[
C_t=T_\Sigma^*A_\Sigma.
\]

Hence its target-relevant range has dimension at most \(\nu\).  Since
\(T_\Sigma T_\Sigma^*=I_\nu\),

\[
C_t^*C_t
=A_\Sigma^*T_\Sigma T_\Sigma^*A_\Sigma
=A_\Sigma^*A_\Sigma.
\]

The shared nonzero spectrum follows from the cut-bridge spectral isomorphism
for \(A_\Sigma^*A_\Sigma\) and \(A_\Sigma A_\Sigma^*\).  ∎

---

## 6. Native signed reduction

Let \(R_0>0\) be the accepted reference generated from the recognized cut
channel and the native carrier metric.  Define

\[
\mathcal W_{\rm cut}=R_0-D_t.
\]

Under target faithfulness,

\[
\mathcal W_{\rm cut}
=R_0-A_\Sigma^*A_\Sigma.
\]

Set

\[
V_\Sigma=A_\Sigma^*:
\mathbb C^\nu\longrightarrow\mathcal F^{\rm comp}
\]

and

\[
B_\Sigma
=A_\Sigma R_0^{-1}A_\Sigma^*
=V_\Sigma^*R_0^{-1}V_\Sigma.
\]

The universal cut-memory spectral theorem then gives

\[
N_-(\mathcal W_{\rm cut})=N_+(B_\Sigma-I),
\]

\[
\ker\mathcal W_{\rm cut}\cong\ker(I-B_\Sigma),
\]

and

\[
\inf_{f\ne0}
\frac{\langle f,\mathcal W_{\rm cut}f\rangle}
     {\langle f,R_0f\rangle}
=
\lambda_{\min}(I-B_\Sigma).
\]

The determinant identity

\[
\det_F(I-R_0^{-1/2}D_tR_0^{-1/2})
=
\det(I-B_\Sigma)
\]

locates threshold memory, but determinant sign alone is not the positivity
criterion.  The lawful sign certificate is

\[
\lambda_{\max}(B_\Sigma)<1.
\]

---

## 7. RH-specific construction gate

The remaining theorem is not to import \(S_{0,-}^{\rm full}\), \(L_\partial\),
\(R_0\), or \(V_\Sigma\) from a classical operator decomposition.

It is to construct one native event lift

\[
Z_{\rm Weil}f
\]

coefficientwise from the declared prime, Gamma, completion-boundary and
compatibility cut events and then prove:

### Gate 1: source and boundary are cut moments

For a cut-recognized vector \(p_\partial\),

\[
S_{0,-}^{\rm full}=Z_{\rm Weil}^*Z_{\rm Weil},
\]

\[
L_\partial(f)=\langle p_\partial,Z_{\rm Weil}f\rangle,
\]

and hence

\[
S_{0,-}^{\rm full}-L_\partial^*L_\partial
=Z_{\rm Weil}^*QZ_{\rm Weil}.
\]

### Gate 2: target observer is native and faithful

Construct \(T_\Sigma\) from the five declared target labels before whitening or
Gram fitting and prove

\[
QZ_{\rm Weil}
=T_\Sigma^*T_\Sigma QZ_{\rm Weil}
\]

on the adverse target-relevant module.

### Gate 3: no hidden adverse complement

If full cut memory contains a target-null complement, prove that its form is
nonnegative and does not contribute to the threshold count.  Equivalently,
only the target-visible cut memory may enter the negative inertia ledger.

These are native coefficient identities.  The classical explicit formula may
later recognize their shadow, but it does not define them.

---

## 8. Numerical development plan

The numerical packet must be built from the same cut-generated data:

```text
1. construct Z from declared event amplitudes;
2. construct P,Q and verify P+Q=I, PQ=0;
3. verify S=Z*Z, R=Z*PZ, D=Z*QZ and S=R+D;
4. verify the rank-one boundary identity where applicable;
5. construct T_Sigma from declared target labels;
6. enclose the faithfulness residual ||QZ-T*TZ||;
7. reject a target map which misses one cut-memory direction;
8. build B_Sigma from the cut-derived R0 and A_Sigma;
9. certify lambda_min(I-B_Sigma), inertia and determinant identities;
10. enclose refinement and off-bank tails before any RH promotion.
```

A favorable five-matrix is not terminal unless Steps 3, 6 and 10 are proved.

---

## 9. Claim boundary

```text
source/recognized/memory forms derived from one cut lift    PROVED ABSTRACTLY
rank-one first/second-moment covariance identity            PROVED ABSTRACTLY
exact exponential cut covariance                            PROVED ABSTRACTLY
target-faithful rank <= 5 theorem                            PROVED ABSTRACTLY
finite seam spectral reduction                              PROVED ABSTRACTLY

native completed-Weil event lift Z_Weil                     NEXT
coefficientwise source/boundary moment identities            NEXT
native target observer T_Sigma                              NEXT
target-faithfulness residual with outward bounds             NEXT
no-hidden-adverse-complement theorem                         NEXT
RH                                                          NOT CLAIMED
```