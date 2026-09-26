# Refinement-Stable and Continuum Native Length

## Provenance

```text
source repository: Parveen117/MP
source PRs: #55 and #56
source theorems:
  adapters/common/REFINEMENT_INVARIANT_NATIVE_LENGTH.md
  adapters/common/CONTINUUM_HOMOTOPY_DESCENT.md
```

## 1. Positive collinear refinement

A macro increment \(A\in\mathfrak{su}(2)\) may be subdivided by positive weights

\[
a_k>0,
\qquad
\sum_{k=1}^r a_k=1,
\]

into ordered micro-increments \(a_1A,\ldots,a_rA\). Since they commute,

\[
e^{a_rA}\cdots e^{a_1A}=e^A.
\]

The macro hierarchy endpoints, winding increment, and memory token remain attached to the macro segment. Artificial discretization boundaries are not promoted into new hierarchy-return cuts.

## 2. Directed refinement category

Objects are positive partitions of each macro segment. A morphism is breakpoint inclusion from a coarser partition to a finer one. The union of breakpoint sets gives a common refinement, so the finite refinement category is directed.

## 3. Native length-rigidity theorem

Let

\[
\lambda:\mathfrak{su}(2)\to[0,\infty)
\]

be continuous, nonnegative, invariant under constant \(SU(2)\) conjugation, and additive under every positive collinear split:

\[
\lambda(A)=\lambda(tA)+\lambda((1-t)A),
\qquad 0<t<1.
\]

Adjoint invariance makes \(\lambda\) radial:

\[
\lambda(A)=f(\|A\|).
\]

The split law gives the continuous Cauchy equation, hence

\[
\boxed{\lambda(A)=c\|A\|,\qquad c\ge0.}
\]

Therefore the sector length is rigid up to an overall scale:

\[
\boxed{L_c(\Sigma)=c\sum_j\|A_j\|.}
\]

Within the declared axioms, nonlinear radial alternatives such as \(\|A\|^2\) and \(\|A\|^{1/2}\) fail subdivision invariance.

## 4. Finite refinement consequences

The theorem gives:

- exact holonomy preservation;
- common-refinement directedness;
- subdivision invariance of \(L_c\);
- constant-gauge invariance;
- additivity at admissible macro return cuts;
- refinement invariance of composition-primitivity;
- nondegeneracy on active connection sectors when \(c>0\).

Pure winding or memory sectors with zero connection increments may still have zero geometric length unless separate ledger terms are lawfully introduced.

## 5. Continuum length

For a continuous coefficient

\[
A(t)=-i\,a(t)\cdot\sigma,
\]

define

\[
L_c[A]=c\int_0^1\|a(t)\|\,dt
\]

and transport by

\[
U'(t)=A(t)U(t),
\qquad U(0)=I.
\]

For midpoint samples \(t_k=(k+1/2)/N\),

\[
L_N=\frac cN\sum_{k=0}^{N-1}\|a(t_k)\|,
\]

and the ordered exponential product converges to the continuum transport.

If \(a\) is Lipschitz with derivative bound \(M\),

\[
\boxed{|L_N-L_c[A]|\le \frac{cM}{4N}.}
\]

## 6. Reparameterization theorem

For an orientation-preserving \(C^1\) diffeomorphism \(\phi\) fixing the endpoints, define

\[
\widetilde A(s)=\phi'(s)A(\phi(s)).
\]

Then

\[
\boxed{L_c[\widetilde A]=L_c[A],
\qquad
\widetilde U(1)=U(1).}
\]

Orientation reversal preserves length but reverses transport:

\[
U_{\mathrm{rev}}(1)=U(1)^{-1}.
\]

Constant gauge conjugation preserves the length and conjugates the endpoint holonomy.

## 7. Unrestricted homotopy no-go

For contractible circles

\[
\gamma_r(t)=r(\cos 2\pi t,\sin 2\pi t,0),
\]

one has

\[
L(r)=2\pi r.
\]

Homotopic loops can therefore have distinct positive lengths and collapse continuously to zero. Hence

\[
\boxed{L_c\text{ descends to oriented reparameterization classes, not unrestricted homotopy classes}.}
\]

## Claim boundary

```text
REFINEMENT CATEGORY DIRECTEDNESS           PROVED
LOCAL LENGTH RIGIDITY c||A||               PROVED
SUBDIVISION AND GAUGE INVARIANCE           PROVED
CONTINUUM RIEMANN-SUM CONVERGENCE          PROVED
EXPLICIT LIPSCHITZ ERROR                   PROVED
ORIENTED REPARAMETERIZATION INVARIANCE     PROVED
ORIENTATION-REVERSAL TRANSPORT LAW         PROVED
UNRESTRICTED HOMOTOPY INVARIANCE           DISPROVED

ABSOLUTE SCALE c                           EXTERNAL / OPEN
PURE MEMORY-SECTOR POSITIVE LENGTH         OPEN
CONSTRAINED HOMOTOPY COMPLETION            NEXT THEOREM LAYER
```
