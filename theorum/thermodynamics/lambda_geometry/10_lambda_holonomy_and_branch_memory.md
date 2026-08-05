# Lambda Holonomy, Branch Memory, and Local Spectral Factor

## Provenance

```text
source repository: Parveen117/MP
source PR: #52
source theorem: adapters/common/LAMBDA_HOLONOMY_SPECTRAL_OPERATOR.md
```

This capsule transfers the geometric theorems that follow once a connection is supplied to the thermodynamic-lambda state space. It does **not** claim that the thermodynamic hierarchy uniquely determines that connection.

## 1. Typed lambda hierarchy

The historical source begins with

\[
X^{(0)}=(T,V,S,P),
\qquad
X^{(1)}=(\lambda_p,\lambda_v,\lambda_s,\lambda_t),
\]

and higher response layers

\[
X^{(r+1)}=\mathcal R_r(X^{(r)}).
\]

The later PR #239 typing correction applies: the historical derivative coordinates in the \(s,t\) directions are not silently identified with the uniform entropy-scaled tetrad \(\lambda_X^{\mathrm{th}}=-ST/C_X\).

## 2. Unitary connection and curvature

Let \(E\to\mathcal M_\lambda\) be a Hermitian bundle over the lambda-state manifold and let

\[
\nabla^\lambda=d+A_\lambda,
\qquad
F_\lambda=dA_\lambda+A_\lambda\wedge A_\lambda,
\]

with \(A_\lambda\) skew-adjoint in a unitary frame. For a based loop \(C\),

\[
U_C=\operatorname{Hol}_{\nabla^\lambda}(C)
\]

is unitary.

The response hierarchy and the connection remain distinct typed objects.

## 3. Holonomy-rate self-adjointness theorem

For a differentiable unitary path \(U_t\), define

\[
\mathcal M_t=iU_t^{-1}\dot U_t.
\]

Then

\[
\boxed{\mathcal M_t^*=\mathcal M_t.}
\]

Indeed, differentiating \(U_t^*U_t=I\) shows that \(U_t^{-1}\dot U_t\) is skew-adjoint.

## 4. Static logarithm branch-memory theorem

If

\[
U_C=\sum_j e^{-i\theta_j}P_j,
\qquad \theta_j\in(-\pi,\pi],
\]

then every self-adjoint logarithm compatible with a continuous spectral lift has the form

\[
H_C=\sum_j(\theta_j+2\pi k_j)P_j,
\qquad k_j\in\mathbb Z.
\]

Therefore \(i\log U_C\) is not a single branch-independent datum. The lawful stored object contains

\[
\{(\theta_j,P_j,k_j)\}_j
\]

plus the path or lift fixing the integers. Principal phase alone loses winding memory.

## 5. Complete sector signature

A hierarchy-resolved sector must retain at least

\[
\Sigma_C=
\left(
 r,[C],\{(\theta_j,P_j,k_j)\}_j,
 \mathcal F_C,\mathfrak m_C
\right),
\]

where \(r\) is hierarchy depth, \(\mathcal F_C\) is curvature-flux or transgression data, and \(\mathfrak m_C\) is seam memory.

No theorem may replace \(\Sigma_C\) by one winding integer without proving that the discarded data are irrelevant to the target.

## 6. Winding and spectral-flow theorem

In the scalar case, write

\[
U_t=e^{-i\phi(t)}.
\]

When endpoint holonomies agree,

\[
\phi(t_1)-\phi(t_0)=2\pi\nu,
\qquad \nu\in\mathbb Z.
\]

For a reference angle avoided by the endpoints, the signed eigenphase crossing count satisfies

\[
\boxed{\operatorname{sf}(\mathcal M_t;\theta_*)=\nu.}
\]

In finite rank this becomes the signed sum over continuously lifted spectral branches. Independent sorting of principal angles is not sufficient at degeneracies.

## 7. Composition boundary

For concatenated based paths,

\[
U_{C_1\star C_2}=U_{C_2}U_{C_1}.
\]

In \(U(1)\), or on commuting channels with compatible lifts, phases, winding, and declared curvature flux add. For noncommuting holonomies,

\[
\log(UV)\neq \log U+\log V
\]

in general; Baker-Campbell-Hausdorff commutator terms are part of the sector memory.

## 8. Finite local spectral-factor theorem

Given a supplied positive native length \(\ell_C\), define for \(\Re s>0\)

\[
Z_C(s)=\det\!\left(I-e^{-s\ell_C}U_C\right)^{-1}.
\]

Then

\[
\boxed{
\log Z_C(s)=
\sum_{m\ge1}
\frac{e^{-sm\ell_C}}{m}\operatorname{Tr}(U_C^m).
}
\]

For scalar trivial holonomy and a separately proved \(\ell_C=\log p\), this reduces to \((1-p^{-s})^{-1}\). The theorem does not derive the prime assignment.

## Claim boundary

```text
UNITARY HOLONOMY-RATE SELF-ADJOINTNESS       PROVED
STATIC LOGARITHM BRANCH CLASSIFICATION       PROVED
GAUGE-CONJUGACY SPECTRAL INVARIANTS          PROVED
WINDING / SPECTRAL-FLOW IDENTITY             PROVED IN DECLARED FINITE MODEL
FINITE LOCAL DETERMINANT / TRACE-LOG         PROVED

CONNECTION FROM THERMODYNAMIC HIERARCHY      OPEN
CANONICAL NATIVE POSITIVE LENGTH             OPEN
PRIMITIVE SECTOR TO PRIME IDENTIFICATION     OPEN
INFINITE TRACE-CLASS COMPLETION              OPEN
```
