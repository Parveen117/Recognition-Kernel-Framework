# SE13: Moving-reference index and obstruction theorems

12 October 2026. Owner: Monty.

This note supplies theorem statements, proofs and executable algebraic
controls for the observer-dependent formulations of Atiyah--Singer,
spectral flow/index and Birman--Schwinger. No observer or positive
normalizing reference is privileged. The objects transported between
observers must nevertheless be identified, including their domains,
pairings, gradings, cuts and retained Smriti.

The classical index theorems are already coordinate independent, and
the families theorem already permits varying elliptic operators. The
contribution here is an explicit RKF transport and certification contract,
and its attachment to the actual SE5 source. It is not a new proof of
Atiyah--Singer or an extension beyond the stated Fredholm/elliptic class.
Classical results are cited inputs to the admitted representation.

"Certified" below separates a written conditional theorem, an operator
certificate whose hypotheses must be enclosed, and executed finite
controls. The controls do not formally verify the infinite-dimensional
index theorem. No proof-assistant or external-review status is claimed.

## 1. Native premise order and transport contract

Typed cuts, cut scalars, derived iota, composition, declared targets and
Smriti come first. Hilbert bundles, Sobolev domains and elliptic symbols
enter only through an explicitly admitted adapter. The actual endpoint
application below uses the existing T35/T40 adapter and SE5 identities.

Let alpha and beta denote observer charts of the **same represented
object**. Their state and target identifications U and V are bounded
invertible maps, with the relevant domains mapped onto one another.
Pairings are transported, so these maps are isometries for the
transported metrics, even if their coordinate matrices are nonunitary.
For an arrow D the required equation is
\[
 D_\beta=V D_\alpha U^{-1}.                         \tag{SE13.I1}
\]
On overlaps the transitions satisfy the cocycle identities. This is
descent of charts; it does not require a global trivialization or erase
the holonomy of a connection. A noninvertible physical cut is not a
chart change. Its discarded target information needs a recovery or
relative-index theorem before (SE13.I1) can be used.

An orientation, grading, source-target order or spectral-flow convention
is part of the contract. Changing its coordinate description is allowed;
reversing the mathematical object is a different operation. In
particular, ind(D*)=-ind(D), and reversing a path reverses spectral flow.
The sign of a coordinate entry is not the inertia of a Hermitian form.

## 2. Theorem I: Covariant Atiyah--Singer descent and block certification

**Hypotheses.** Let pi:M -> Lambda be a smooth proper family of closed
manifolds over a compact smooth parameter space. Let E and F be complex
vector bundles over M, and D_lambda:E_lambda -> F_lambda a smooth
family of elliptic operators of one fixed order. Realize D as a bounded
map between its Sobolev domain bundle and target bundle. Observer
charts satisfy (SE13.I1), preserve this domain and identify the principal
symbol classes; geometric charts transport all bundle and orientation
data. Arbitrary Hilbert isomorphisms alone do not supply a symbol map.

Then the observer descriptions determine one index class, with
\[
 \boxed{\operatorname{Ind}_a(D)
       =\operatorname{Ind}_t([\sigma(D)])\in K^0(\Lambda).}
                                                               \tag{SE13.I2}
\]
The equality is natural under the declared observer changes and
pullbacks of the family. No chart, initial point or final point is an
absolute reference. At a single parameter it specializes to the
ordinary Atiyah--Singer equality. Its integer rank is constant on each
connected component of Lambda. A full family index class generally
contains more information than that integer.

There is also a concrete sufficient analytic certificate. Supply finite
vector bundles J_+ and J_- and bounded bundle arrows forming
\[
 \mathscr D=\begin{pmatrix}D&R_-\\R_+&C\end{pmatrix}:
 H_+\oplus J_+\longrightarrow H_-\oplus J_- .        \tag{SE13.I3}
\]
If a proposed inverse Q has certified, uniform operator bounds
\[
 \|I-Q\mathscr D\|<1,\qquad \|I-\mathscr DQ\|<1,
                                                               \tag{SE13.I4}
\]
in the declared pairings, then
\[
 \boxed{\operatorname{Ind}_a(D)=[J_-]-[J_+]
       =\operatorname{Ind}_t([\sigma(D)]).}           \tag{SE13.I5}
\]
For a single operator this is ind(D)=dim J_- - dim J_+.
Transporting the entire block, inverse and pairings preserves the two
residual bounds and this certificate. Sampling a residual is insufficient.

**Proof.** Ellipticity on closed fibers gives a continuous Fredholm
family. Kernels and cokernels at a fixed parameter are carried
isomorphically by U and V, so their difference is chart independent.
Kernel dimensions may jump along the family, so they must not be
assumed to form vector bundles. Instead choose a finite bundle J and
a finite-dimensional supplement so that (D,R):H_+ plus J -> H_- is
surjective. Compactness of the base permits such stabilization from
finitely many local supplements. Its kernel is a finite vector bundle,
and [ker(D,R)]-[J] is the analytic index. Two choices give the same
class: pass to their common supplement and use the resulting split
short exact sequence of finite bundles. The overlap maps transport
this construction, hence it descends without selecting an observer.

The classical families Atiyah--Singer theorem identifies this analytic
class with the topological pushforward of the vertical symbol class.
The symbol identifications and naturality of that pushforward give
(SE13.I2). This invokes the classical theorem; it does not derive its
topological formula from matrix controls.

For the explicit certificate, the two Neumann bounds give a left and
a right inverse for the same block, so mathscr D is invertible. Deleting
its finite blocks changes it by a finite-rank family. Its index is
therefore Ind(D)+[J_+]-[J_-]=0, proving (SE13.I5). Simultaneous transport
conjugates the residual endomorphisms by isometries of the transported
metrics. Their norms and the finite bundle difference are unchanged.
This proves the certificate and its covariance. QED.

For a graded Dirac realization, the index is that of D+:E+ -> E-.
The ungraded self-adjoint Dirac operator has ordinary Fredholm index
zero. A metric-compatible change of connection may change a local
index-density representative by an exact transgression; on closed
fibers its integral does not change. There is no assertion that every
local density or every local integral equals the global integer.
With a boundary, a specified elliptic/APS domain and its boundary
correction are additional data; the closed-fiber theorem cannot simply
omit them.

## 3. Theorem II: Moving-reference Birman--Schwinger obstruction

**Hypotheses.** On an admitted Hilbert carrier let R be bounded,
self-adjoint and R>=mI for some m>0, and let K be compact self-adjoint.
The represented source is exactly F=R-K. R and K may depend on the
observer or other parameters; they are not required to be constant.
Put B=R^(-1/2) K R^(-1/2). Then
\[
 \boxed{F=R^{1/2}(I-B)R^{1/2},\quad
 \kappa(F):=N_-(F)=N_+(B-I)<\infty,\quad
 \dim\ker F=\dim\ker(I-B).}                         \tag{SE13.I6}
\]
Consequently
\[
 \boxed{F\succeq0\quad\Longleftrightarrow\quad
        \kappa(F)=0\quad\Longleftrightarrow\quad B\preceq I.}
                                                               \tag{SE13.I7}
\]
Every positive-reference/compact-defect decomposition of this same F
has the same kappa and kernel dimension. The normalizers, spectra and
relative gaps need not coincide. Under an invertible congruence
F'=T* F T the count and nullity are also unchanged.

If the defect has a supplied factorization K=VV* with V:E -> H compact,
one may instead use B_E=V*R^(-1)V. It has the same eigenvalues above
one and the same threshold multiplicity. It is a finite matrix only
when E is finite dimensional, or a separate finite-rank reduction is
proved. A compact Birman--Schwinger operator can have infinite rank.

In fixed coordinate pairings the simultaneous transformation
\[
 R'=T^*RT,\qquad V'=T^*V
 \quad\Longrightarrow\quad V'^*R'^{-1}V'=V^*R^{-1}V
                                                               \tag{SE13.I8}
\]
allows a nonunitary source change without freezing R. With transported
pairings and label charts, the same assertion is a unitary equivalence
of B_E. The star in this coordinate identity must not be substituted
for a native dagger without its Gram factors.

**Proof.** The displayed factorization is exact. Invertibility of
R^(1/2) bijects negative subspaces of the two forms, proving equality
of negative indices and kernel dimensions. Compact self-adjoint B
has only finitely many eigenvalues above one. The spectral theorem
then proves (SE13.I7). The same negative-subspace argument applies
to every invertible T and every other exact decomposition of F.
For K=VV*, take A=R^(-1/2)V; the positive eigenvalues of AA* and A*A
agree with multiplicity, using the maps A and A*. Direct substitution
of (T*RT)^(-1)=T^(-1)R^(-1)(T*)^(-1) proves (SE13.I8). QED.

**An executable enclosure criterion.** Suppose P is one finite
orthogonal projection, C is a Hermitian matrix on PH, and
\[
 \|B-(C\oplus0)\|\le\varepsilon<1.
\]
Include the diagonal, mixed blocks, infinite complement and arithmetic
errors in this one norm allowance. The min--max principle gives
\[
 N_+\bigl(C-(1+\varepsilon)I\bigr)
 \ \le\ \kappa(F)\ \le\
 N_+\bigl(C-(1-\varepsilon)I\bigr).                 \tag{SE13.I9}
\]
Equal enclosed counts certify the integer. In particular,
C<=(1-epsilon)I certifies zero obstruction, including a non-strict
source. To prove the bound, sandwich B between C plus/minus epsilon I
on the full carrier. The complement has upper value epsilon<1 and
cannot contribute to the upper count. This is the same-projection
discipline of Gold 06, expressed as an integer certificate.

Reference freedom does not mean all numerical readings are invariants.
For F=diag(-1,2), the pairs
\[
 (R_1,V_1)=(\operatorname{diag}(3,6),2I),\qquad
 (R_2,V_2)=(\operatorname{diag}(8,11),3I)
\]
both represent F. Their B matrices are diag(4/3,2/3) and
diag(9/8,9/11). Both have kappa=1, but their relative lower gaps are
-1/3 and -1/8. The invariant is the obstruction, not that normalization.

## 4. Theorem III: Covariant spectral-flow/index and the two-endpoint law

Use the convention that a crossing from negative to positive counts
as +1. Consider a smooth self-adjoint path D_t on an admitted Hilbert
bundle over a compact interval, extended constantly outside it, with
invertible ends. For the unbounded version assume a common transported
dense domain W compactly embedded in H, C1 dependence in L(W,H), and
uniform equivalence of graph norms. These are sufficient standard
spectral-flow/Fredholm hypotheses. Finite-dimensional memory paths
are included. Choose a compatible connection with a parallel
trivialization satisfying these hypotheses.

Then the whole-line suspension with its specified domain obeys
\[
 \boxed{\operatorname{ind}(\nabla_t+D_t)
       =\operatorname{sf}(D_t;0).}                  \tag{SE13.I10}
\]
Its domain is W^(1,2)(R,H) intersect L2(R,W). An interval realization
needs the corresponding boundary conditions; it is not defined by
the differential expression alone. Smooth changes of observer,
bounded with their inverses on the declared domains, obey
\[
 D'_t=U_tD_tU_t^{-1},\qquad
 \Gamma'_t=U_t\Gamma_tU_t^{-1}-\dot U_tU_t^{-1},\qquad
 (\nabla'_t+D'_t)U_t=U_t(\nabla_t+D_t).             \tag{SE13.I11}
\]
Here U is C1 in operator norm on H, with bounded derivative, and
preserves the W domain with uniformly bounded inverse there. Thus
it also preserves the stated suspension domain.
The index and spectral flow agree in all these charts. No
observer is held fixed while the others move.

**Proof.** In a parallel trivialization (SE13.I10) is the standard
spectral-flow/index theorem, applied to the plus-sign suspension.
Robbin--Salamon use d/dt-A and index=-sf(A); take A=-D to obtain the
stated convention. Differentiating U_t times a section gives
(SE13.I11), so the suspensions are conjugate by domain-preserving
isomorphisms. Their kernels and cokernels are isomorphic.

The crossing-form proof makes the local sign precise. At a regular
crossing t0 its form on ker D_(t0) is
\[
 q_{t_0}(x)=\langle x,(\dot D+[\Gamma,D])_{t_0}x\rangle.
                                                               \tag{SE13.I12}
\]
The commutator contributes zero on the kernel. Equation (SE13.I11)
carries q to a congruent form, preserving its signature. Summing the
signatures proves chart invariance at regular crossings; continuous
deformation gives the general case. Reversing the parameter reverses
the crossing form and spectral flow. The scalar model D_t=t has
kernel exp(-t^2/2) for d/dt+t and no adjoint kernel, fixing the +1
convention directly. QED.

For the compact-threshold specialization let B_t be a norm-C1 compact
self-adjoint path with 1 outside the spectra of its two endpoints.
The bounded path D_t=I-B_t is self-adjoint Fredholm and essentially
positive. Define kappa(t)=N_+(B_t-I). Then
\[
 \boxed{\kappa(b)-\kappa(a)
       =-\operatorname{sf}(I-B_t;0).}               \tag{SE13.I13}
\]
This is the existing RKF curvature/seam law, now placed inside the
transport contract. Only finitely many near-threshold directions are
needed on a compact parameter interval: norm compactness of the
family supplies a common finite-rank approximation of B_t, with error
smaller than both endpoint gaps and 1. Interpolation to that finite
path preserves endpoint invertibility and the Fredholm property.
The finite path has spectral flow N_-(D_a)-N_-(D_b), proving the law.

In this bounded compact case the whole-line suspension is Fredholm
and also satisfies (SE13.I10). One direct justification uses the same
finite-rank reduction. Choose the approximation so its error is
smaller than both endpoint gaps throughout the interpolation. The
limiting operators at both ends remain uniformly invertible. Their
constant coefficient whole-line operators have bounded inverses by
Fourier transformation. Retain their common d/dt+I part globally;
the remaining cutoff-parametrix errors contain compact-valued
coefficient or resolvent differences and are supported
in a compact t interval with compact operator values. Such errors
are compact from W^(1,2) to L2 by finite-rank approximation and the
one-dimensional Rellich theorem. This proves Fredholmness along the
interpolation. At its finite-rank end the suspension is the direct
sum of the finite-dimensional formula and d/dt+I, whose index is
zero. Index invariance proves the asserted identity.

Both a and b may move. There is no formula kappa(b)=-sf on an
arbitrary path unless kappa(a)=0 has been established. Alternatively,
the static Theorem II computes kappa(b) without selecting an initial
observer. For the explicitly declared activation path I-tB, t in
[0,1], with 1 outside sigma(B), the start is positive and
\[
 \kappa(F)=-\operatorname{sf}(I-tB;0)
           =-\operatorname{ind}(d/dt+I-tB).          \tag{SE13.I14}
\]
Extend this path constantly at the ends when using the suspension.
It is an auxiliary positive-reference path, not a privileged native
observer. At an endpoint eigenvalue exactly one, the static strict
count in Theorem II remains valid, but this invertible-end formula
requires an explicit one-sided convention or endpoint perturbation.

Zero net spectral flow alone is not positivity. For
B_t=diag(1/4+2t,9/4-2t,1/2), the two crossings cancel, while
kappa(0)=kappa(1)=1. Also a self-adjoint Fredholm source F has ordinary
index zero even when F has negative eigenvalues. The source index,
the suspension index and its negative-direction count are different
typed quantities.

## 5. Theorem IV: Actual source invariant, cofinal observers and eta zero

For the corrected T35/T40 source, retain the established SE5 identities
\[
 S_b=T_0-V,\quad T_0\succeq0,\quad V=V^*\text{ compact},\qquad
 N_*=A_*^\dagger A_*\succeq c_*I,\quad
 S_b=N_*-L_*^\dagger L_* .                         \tag{SE13.I15}
\]
Here V is the signed compact defect, not an assumed five-column map.
For each eta>0 put
\[
 R_\eta=T_0+\eta I,\qquad
 B_\eta=R_\eta^{-1/2}V R_\eta^{-1/2},\qquad
 \kappa_\eta=N_+(B_\eta-I).
\]
Then the actual, reference-independent equality is
\[
 \boxed{\kappa_\eta=N_-(S_b+\eta I)
       =\dim\operatorname{Ran}1_{(-\infty,-\eta)}(S_b)<\infty.}
                                                               \tag{SE13.I16}
\]
The metric identity I and threshold eta are transported as part of
the same state metric. Replacing the metric while keeping coordinate
I fixed would ask a different quantitative question.

For any positive sequence eta_j decreasing to zero,
\[
 \boxed{S_b\succeq0
 \ \Longleftrightarrow\ \kappa_{\eta_j}=0\ (\text{every }j)
 \ \Longleftrightarrow\
 \mathfrak b:=\sup_{f\ne0}\frac{\|L_*f\|^2}{\|A_*f\|^2}\le1.}
                                                               \tag{SE13.I17}
\]
The last scalar equals ||L_* N_*^(-1/2)||^2=||O_*||^2. It is invariant
under simultaneous faithful state, event and target charts with
transported pairings. Its value uses the declared physical analysis
and target; replacing those readings is not a coordinate change.

For the nested supported spaces X_A of the aperture note define
\[
 \kappa_\eta(A)=N_-((S_b+\eta I)|_{X_A}),\qquad
 \mathfrak b(A)=\sup_{0\ne f\in X_A}
                         \frac{\|L_*f\|^2}{\|A_*f\|^2}.
\]
Every restriction is frame independent on its represented subspace.
Along cofinal apertures,
\[
 \boxed{\kappa_\eta(A)\uparrow\kappa_\eta,
 \quad\mathfrak b(A)\uparrow\mathfrak b.}           \tag{SE13.I18}
\]
For each **fixed positive eta**, the integer count is eventually
exact at a sufficiently large finite aperture. This is an existence
statement; it gives no computable cutoff before the negative subspace
has been controlled. There need not be one aperture that works for
every eta, nor equality between different-sized local restrictions.

**Proof.** Apply Theorem II to S_b+eta I=R_eta-V, using its genuine
positive floor eta. This proves (SE13.I16). If every count is zero,
S_b>=-eta_j I for every j, so its quadratic form is nonnegative in
the limit. The converse is immediate. The quotient criterion follows
from the exact source identity; substituting f=N_*^(-1/2)z gives its
norm formula. Chart covariance follows directly from the transported
norms, without choosing an observer extension outside Ran A_*.

For (SE13.I18), restrictions cannot increase the count beyond the full
one. The full negative subspace of S_b+eta I is finite dimensional.
Its unit sphere has a uniform strictly negative upper form bound.
Approximate a basis in the dense compactly supported native core;
boundedness of the form preserves strict negativity and independence
for sufficiently accurate approximants. All approximants lie in one
X_A, proving equality of counts for that and all larger apertures.
For the quotient, density and the positive mismatch floor permit
approximation of each nonzero vector and its denominator, proving
the supremum identity. QED.

SE13's radius-0.820 certificate proves kappa_eta(A)=0 for every
eta>0 and every A<=0.820. It does not yet prove kappa_eta=0 on the
full carrier. SE5 proves that zero is in the essential spectrum of
S_b. Accordingly S_b itself is not Fredholm at eta zero; the ordinary
Atiyah--Singer/suspension theorem cannot be applied there by simply
setting eta=0. The family of positive-eta invariants and (SE13.I17)
provide a lawful endpoint condition without that substitution.

The intrinsic complete criterion can therefore be an invariant-zero
condition, but invariance does not force its value to be zero. This
attachment preserves the historical K0 and RH boundaries. To write
K0>=0 iff kappa=0 for a particular historical reduction requires its
exact source identification and all its hypotheses, not its name.

## 6. Provenance, canvas corrections and evidence

The [SE2 transport theorem](SE2_OBSERVER_PATH_OPERATOR_CERTIFICATE.md),
[T21 cut-memory theorem](../../../theorum/21_cut_memory_spectral_isomorphism.md),
[T02 seam covariance](../../../theorum/02_seam_integer_single_sector_reduction.md),
and [curvature/seam law](../../../theorum/thermodynamics/02_curvature_to_seam_spectral_flow.md)
already establish the relevant recovery, finite-rank and path mechanisms.
Theorem II extends their displayed reference contract to arbitrary
positive references and signed compact defects; Theorem IV attaches
it using SE5's actual corrected source. None of these steps supplies
the still-missing actual rank-five endpoint identification.

Primary classical inputs:

- M. F. Atiyah and I. M. Singer, *The Index of Elliptic Operators I*,
  Annals of Mathematics 87 (1968), 484--530,
  [DOI 10.2307/1970715](https://doi.org/10.2307/1970715),
  [primary paper](https://math.uchicago.edu/~shmuel/tom-readings/ASI.pdf).
- M. F. Atiyah and I. M. Singer, *The Index of Elliptic Operators IV*,
  Annals of Mathematics 93 (1971), 119--138,
  [DOI 10.2307/1970756](https://doi.org/10.2307/1970756),
  [primary paper](https://www.maths.ed.ac.uk/~v1ranick/papers/as4.pdf).
- J. Robbin and D. Salamon, *The Spectral Flow and the Maslov Index*,
  Bulletin of the London Mathematical Society 27 (1995), 1--33,
  [DOI 10.1112/blms/27.1.1](https://doi.org/10.1112/blms/27.1.1),
  [authors' preprint](https://people.math.ethz.ch/~salamon/PREPRINTS/spec.pdf).

The primary papers' bibliographic and indexed theorem material was
checked on 12 October 2026. Full-file retrieval of the IV and
Robbin--Salamon mirrors was blocked; no claim of a complete line-by-line
audit of those external papers is made. The finite-rank and compact
inertia arguments consumed here are proved above.

The attached *Lambda--Atiyah--Singer Index Theorem -- Compact Formal
Canvas* was read in full, with its families page visually inspected.
It is an informal prompt/source, not a certificate. Three corrections
are material: a Fredholm family's index does not jump merely because
an eigenvalue crosses zero; the chiral index must not be confused with
the ungraded self-adjoint index; and a spectral-flow suspension needs
its domain, endpoints and sign convention. The family's K-theory
class, an endpoint negative count and a path spectral flow are not
interchangeable integers. The original PDF is preserved unchanged.

The exact rational [control program](../../../proof_lab/endpoint_observer_index_certificate.py)
checks nonorthonormal chart transport, a three-chart cocycle, an
augmented Fredholm certificate, moving Birman--Schwinger references,
connection covariance, both path orientations, a cancellation control,
threshold brackets and a shifted source example. Its
[result](../../../proof_lab/ENDPOINT_OBSERVER_INDEX_RESULT.json) records
finite controls only. The aperture certificate has its own full
interval replay. See the common [audit](SE13_SCOPE.md) and
[source record](SE13_SOURCE_RECORD.md) for the exact distinction.
