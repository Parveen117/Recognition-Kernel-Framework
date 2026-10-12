# SE13: Aperture growth and the correct observer limit

12 October 2026. Owner: Monty.

The next certified physical radius is 41/50=0.820, beyond SE12's
0.805. The complete odd source satisfies
\[
 \boxed{s[f]\ge\frac1{2500000000000000}\|Rf\|_2^2,
 \qquad s[f]\ge\frac1{71500000000000001}\|f\|_X^2,
 \quad f\in X_{41/50}.}                            \tag{SE13.1}
\]
The squared local joint-observer reserve is
2/786500000000000011. Native inclusion covers the entire interval
between the old and new radii. Prime 7 is the next event outside it.

The convergence result distinguishes two questions which cannot be
combined into a numerical stopping rule. Canonical aperture observers converge
on every fixed event vector as the apertures exhaust the carrier.
For the actual full debt observer, however, the operator-norm distance
to its global limit is at least one at every finite aperture. If the
global observer is contractive, that distance is exactly one. Thus
uniform operator-norm convergence of these zero-extended aperture truncations would
be the wrong requirement. The remaining sign question is whether the
increasing local observer norms have limit at most one.

## 1. Existing foundation and the new contribution

Typed cuts, cut scalars, derived iota, composition, declared targets
and Smriti precede all representations. We use the admitted T35/T40
native graph and its stated pairings. A chart transpose is not substituted
for native dagger; physical dilation is not assumed native-unitary.

[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) supplies the corrected
source and escaping odd packets. [SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md)
supplies the bounded exact global observer, a positive mismatch floor,
and the compact decomposition below. SE2/T28 already supply general
compatible observer joining and strong limits. SE6--SE9 supply native
return, frequency comparisons, dilation, support identities and inclusion.
[SE10](SE10_PRIME_POWER_AND_CERTIFICATE_COMPLETENESS.md) proves local
frequency-edge recovery, including zero or negative local edges.
[SE11](SE11_PRECISION_FRONTIER_AND_CUTOFF_OBSTRUCTION.md) supplies
exact signed-Gram arithmetic; [SE12](SE12_SUPPORT_MARKER_AND_PRIME_FIVE.md)
supplies support calibration and normalized Bessel enclosures.

The new written deduction is the actual aperture observer's persistent
operator-norm error, proved using the existing escaping packets and
compact mismatch remainder. The strong-limit and sign criteria are
explicit applications of the existing results, not renamed general
theorems. The new executed result is the radius-0.820 certificate with
a recalibrated support marker and a sharper inherited head-vector bound.

## 2. The canonical aperture observer and its monotone norm

Use the actual full odd boundary target, with its single supplied pole
row. Write A_* for the corrected analysis, L_* for the joint debt and
boundary target, and
\[
 N_*=A_*^\dagger A_*\succeq c_*I_X,\qquad
 S_*=N_*-L_*^\dagger L_*,\qquad
 O_*=L_*N_*^{-1}A_*^\dagger,\qquad O_*A_*=L_* .      \tag{SE13.2}
\]
Here c_*>0 exists by SE5; no numerical value is assumed. O_* is bounded
and vanishes off Y=Ran(A_*), which is closed. Existence and stability
of this exact inverse do not imply ||O_*||<=1.

Let X_A be the closed native subspace of states supported in [-A,A].
Let Y_A=A_*X_A and let P_A be the orthogonal projection onto Y_A in the
declared event metric. The mismatch lower bound makes Y_A closed.
The canonical aperture observer is
\[
 O_A=O_*P_A .                                       \tag{SE13.3}
\]
Indeed it recovers L_*f for every f in X_A and is zero on Y_A's
orthogonal complement. This characterization is unique. Consequently
for B>=A,
\[
 Y_A\subseteq Y_B,\qquad O_B P_A=O_A,
 \qquad\|O_A\|\le\|O_B\|.                          \tag{SE13.4}
\]
The nesting concerns the actual native source and event ranges. It
does not compare entries of differently sized numerical matrices or
assert an order between recalibrated frequency comparisons.

Compactly supported odd core states are dense in X. Since A_* is
bounded, the union of Y_A is dense in Y as A tends to infinity.
Therefore P_A tends strongly to P_Y and
\[
 \boxed{O_Ay\longrightarrow O_*y\quad\text{for every event }y,
 \qquad\|O_A\|\uparrow\|O_*\|.}                    \tag{SE13.5}
\]
For the norm limit, the increasing norms are bounded above by ||O_*||;
strong convergence on each unit vector gives the reverse supremum.
If y=A_*f and f is already supported in [-A_0,A_0], its recovery is
exactly L_*f for every A>=A_0, not merely asymptotically correct.
For arbitrary f and any f_A in X_A,
\[
 \|(O_*-O_A)A_*f\|
 \le\|O_*\|\,\operatorname{dist}(A_*f,Y_A)
 \le\|O_*\|\sqrt{11/2}\,\|f-f_A\|_X.              \tag{SE13.6}
\]
This is a state-dependent approximation bound. It supplies no uniform
tail rate for all unit inputs. Strong convergence in (SE13.5) already
holds before the unresolved contraction condition is known.

## 3. Actual obstruction to operator-norm convergence in aperture

Retain SE5's native graph map C_X and inclusion Gram E:
\[
 \langle f,v\rangle_X=\langle f,v\rangle_{L^2}
       +\langle C_Xf,C_Xv\rangle,
 \quad\|C_X\|\le1,
 \quad N_*=I_X+(m_p-1)E+K_N,                       \tag{SE13.7}
\]
where E satisfies <Ef,v>_X=<f,v>_(L2) and K_N is compact.
SE4's actual odd packets f_j have supports escaping to infinity and
\[
 f_j\rightharpoonup0\text{ in }X,\qquad
 \|C_Xf_j\|\to0,\qquad
 \|A_*f_j\|^2\to m_p>0,\qquad
 \frac{\|L_*f_j\|}{\|A_*f_j\|}\to1.                \tag{SE13.8}
\]
Their X norms tend to one, and their construction is source-pinned in
SE4.7 and SE4.11--SE4.21; no new escape hypothesis is introduced.

Fix any finite A. Eventually f_j and every v in X_A have disjoint L2
supports. The E pairing vanishes, while their native inner product
retains only the C_X pairing. Equations (SE13.7) and compactness give
\[
 \begin{split}
 |\langle A_*f_j,A_*v\rangle|
 &\le(\|C_Xf_j\|+\|K_Nf_j\|)\|v\|_X,\\
 \|P_A A_*f_j\|
 &\le\frac{\|C_Xf_j\|+\|K_Nf_j\|}{\sqrt{c_*}}
 \longrightarrow0 .
 \end{split}                                       \tag{SE13.9}
\]
The second line takes the supremum over ||A_*v||=1 in Y_A and uses
the actual mismatch floor. Weak nullness and compactness imply
||K_Nf_j||->0; small support overlap is not used as an L2 operator-norm
continuity assumption.

Put y_j=A_*f_j/||A_*f_j||. These are unit event vectors with
P_A y_j->0 and ||O_*y_j||->1. Hence
\[
 \|(O_*-O_A)y_j\|
 \ge\|O_*y_j\|-\|O_*\|\,\|P_Ay_j\|\longrightarrow1
 \quad\text{in the lower-limit sense}.
\]
It follows that
\[
 \boxed{\|O_*-O_A\|\ge1\quad(A<\infty).}           \tag{SE13.10}
\]
If the global source is nonnegative, SE5 gives ||O_*||<=1 and SE4
gives ||O_*||>=1. Since ||O_*(I-P_A)||<=||O_*||, in that case
\[
 \boxed{\|O_*-O_A\|=1\quad\text{at every finite aperture}.}
                                                        \tag{SE13.11}
\]
Thus even successful global closure would not make these aperture
observers converge in operator norm. The moving escaping vector
differs with the aperture; there is no contradiction with exact
recovery on already included states or with strong convergence.

For the finite boundary component O_b, compactness instead gives
||O_b-O_bP_A||->0: apply strong projection convergence to its finitely
many adjoint columns. This reuses SE2's finite-target argument. Also,
SE5's regularized global observers O_(*,epsilon) do converge in operator
norm as epsilon->0. That limit changes the inverse regularization,
whereas (SE13.10) changes the spatial aperture; they are distinct.

## 4. What a global convergence check must establish

For any sequence A_j tending to infinity, (SE13.2)--(SE13.5) give
\[
 \boxed{S_*\succeq0
 \ \Longleftrightarrow\ \sup_j\|O_{A_j}\|\le1.}     \tag{SE13.12}
\]
The forward implication restricts the global contraction. Conversely,
strong convergence passes every unit-norm bound to O_*, and SE5's
exact source identity gives nonnegativity. SE4 then makes the limiting
norm exactly one. The local sufficient reserves may tend to zero;
a positive uniform reserve is neither required nor possible.

Unbounded coverage is essential. For example, radii
\[
 A_j=0.805+0.020(1-2^{-j})<0.825                    \tag{SE13.13}
\]
produce infinitely many strictly increasing steps but never exhaust
the carrier. As a general counterexample to inferring global signs
from such coverage, take a unit odd L2 state u supported outside that
limiting interval and the bounded self-adjoint operator I-2u tensor u.
Its form is the identity on every one of those supported subspaces,
yet its value on u is negative. This is a logical control example,
not a counterexample to the RKF source.

Strict positive floors are also not necessary for a convergence
protocol. Suppose A_j->infinity and epsilon_j->0, and the actual source
has certified inequalities
\[
 s[f]\ge-\epsilon_j\|Rf\|_2^2
 \quad\text{for every }f\in X_{A_j}.               \tag{SE13.14}
\]
Every compactly supported core state eventually belongs to these
subspaces. Passing j to infinity proves s[f]>=0; boundedness of S_*
extends the sign to X. Thus small certified negative allowances can
approach zero without demanding a strictly positive local margin.

This route is complete for the existing finite-comparison family:
\[
 \boxed{S_*\succeq0
 \ \Longleftrightarrow\
 \text{for every integer }j\ge1,\ \text{a finite enclosed comparison}
 \text{ certifies }s[f]\ge-j^{-1}\|Rf\|_2^2
 \text{ on }X_j.}                                  \tag{SE13.15}
\]
For necessity, global nonnegativity gives lambda_(2j)>=0 in SE10's
physical L2 chart. Its frequency lower edge tends to
min(b,lambda_(2j))>=0. Choose frequency so that its edge is greater
than -1/(3j), then modes and all arithmetic errors so that the
complete lower certificate remains greater than -1/j. An interval
LDL test uses the candidate shifted by a negative floor, equivalently
a positive addition to that matrix. The scalar cap stays positive.
For sufficiency use (SE13.14). The unmarked family is already complete,
so this argument does not assume a universal marker-selection rule.

This is a precise reduction of the remaining all-scale obligation,
not evidence that every member passes. A finite table of successful
radii or decreasing errors cannot verify its universal quantifier.

## 5. The next actual source and why recalibration is necessary

The new endpoint uses reference radius 1/2, scale c=41/25 and physical
radius A=c/2=41/50. Since log 5<c<log 7, retain exactly the active
prime powers {2,3,4,5}, with the SE12 weights, including Lambda(4)=log 2.
The full pole is h_c(y)=sqrt(c) sinh(cy/2), not a scale-free substitute.

Use the exact support-null identity from SE12 with coefficient -1/10:
\[
 \Xi_c(t)=\Psi_c(t)-\frac1{10}\cos t,\qquad
 b=3/100,\quad T=512,
 \quad K=bI+F_T^*M_{\Xi_c-b}F_T-2h_c\otimes h_c.     \tag{SE13.16}
\]
The full source is unchanged because the compressed full cosine
operator is zero. The coefficient is recalibrated rather than copied
from SE12. At the exact frequency t_*=78769/100 the replay proves
\[
 \Psi_c(t_*)<3/100<\Xi_c(t_*),\qquad
 \Psi_c(t_*)+\cos(t_*)<0.                           \tag{SE13.17}
\]
Thus the unmarked input fails this chosen cap, and the former +cos(t)
marker does not even have a nonnegative tail there at T=512. The
corrected source has not acquired a negative value; these are readings
of alternative comparison symbols. Endpoint and marker changes do not
preserve the tail condition automatically.

The whole corridor [512,2048] is covered by outward midpoint readings
with a global derivative bound
\[
 |\Xi_c'(t)|\le\frac5{2\cdot512}
     +\sum_nw_n\frac{\log n}{c}+\frac1{10}<4.        \tag{SE13.18}
\]
Each accepted interval with midpoint x and radius r proves
Xi_c(x)_lower-4r>3/100 on the entire interval. Exact covered lengths,
the minimum lower bound and the partition hash are archived. Beyond
2048, monotonicity of Gamma and the replayed inequalities
G(2048/c)>5 and sum w_n<22/5 give
\[
 \Xi_c(t)>5-22/5-1/10=1/2>3/100.                  \tag{SE13.19}
\]
Evenness covers negative frequencies. Therefore K is a legitimate
minorant of the unchanged full source on its complete form domain.

## 6. Numerical refinement with the entire complement retained

Retain N=196 odd Legendre orders 1,3,...,391. Gauss-24 on 1024
width-half panels uses the unchanged rational root brackets and
outward weights. The shifted digamma evaluator uses SE12's
shift-128 formula with its absolute periodic-Bernoulli remainder.
The normalized Bessel recurrence uses seeds S_392,S_393, 480 series
corrections, and an exact 240-place integer interval grid for z<=256.
The real derivative bound transfers every point to its complete
node interval. These are working precisions, not unproved final
accuracy claims. Every error is propagated.

The analytic panel ellipses have rho=4, semimajor 17/32 and
semiminor 15/32. With beta_k=2k+1/2,
\[
 M_s=\frac{269}{50}+34\sum_{k<520}\frac1{\beta_k}
 +\frac83\,513^2[(2081/2)^{-3}+\tfrac14(2081/2)^{-2}]
 +9+\frac3{100}<200.                               \tag{SE13.20}
\]
Here |Im(t/c)|<3/8, |t|<513, and the prime plus marker contribution
is below (22/5+1/10)exp(15/32)<9. As in SE12, M=256 is sufficient
for every analytic matrix integrand. The per-entry quadrature error is
\[
 \epsilon_Q=4\cdot512\cdot256
                \frac{4^{-48}}{1-1/4}.             \tag{SE13.21}
\]
Exact signed-Gram sums retain node uncertainty in operator norm.
Integer proposal entries equal to zero may be skipped in the sums:
their proposed products are exactly zero, and their distance to the
true readings is still included in the node error. Pole and final
candidate rounding are separately enclosed.

For the same head projection, the first omitted order is n=393. Put
\[
 a_f=\frac{256^{393}/785!!}{1-256^2/(787\cdot789)},
 \qquad a_h=\frac{4(c/4)^{393}/785!!}
                    {1-(c/4)^2/(787\cdot789)}.      \tag{SE13.22}
\]
SE11's Bessel inequality gives ||v_head(t)||<=1 for every real t,
independently of N. Applying that already proved information to the
mixed-block bound, instead of the looser sqrt(N) bound, gives
\[
 \begin{split}
 D&\succeq(b-\tau_D)I,&
 \tau_D&=\frac{512\cdot256}{3}a_f^2+2a_h^2<10^{-36},\\
 \|B_{\rm mix}\|&\le\tau_B,&
 \tau_B&=\frac{512\cdot256}{3}a_f+2a_h<10^{-16}.
 \end{split}                                       \tag{SE13.23}
\]
In the executed rational bounds tau_B<5.667e-17. This improves the
certificate's sufficient coupling estimate without inventing a new
observer theorem. A larger head could make these tails smaller, but
fixed quadrature or fixed arithmetic errors would not thereby vanish.

The rational candidate is factorized using a separate 320-digit
directed interval LDL. Its contexts are local; inherited 90-digit
point arithmetic and earlier certificates are unchanged. A first
90-digit LDL attempt was inconclusive at pivot 106, whose enclosure
straddled zero. An inconclusive interval is not a negative source
witness. The refined verifier has an independent exact rank-one
control with diagonal regularization 10^(-45) and rejects an indefinite control.

All 196 refined interval LDL pivots of the candidate minus 8e-16 I
are positive. The complete leading-matrix error is less than 2e-16,
so the exact head has floor 6e-16. Therefore
\[
 K\succeq[\min(6\cdot10^{-16},b-\tau_D)-\tau_B]I
       \succ4\cdot10^{-16}I.                       \tag{SE13.24}
\]
This proves the first part of (SE13.1) for every complex odd state,
not merely the finite head. The
[matrix](../../../proof_lab/ENDPOINT_APERTURE_CONVERGENCE_MATRIX.json),
[full result](../../../proof_lab/ENDPOINT_APERTURE_CONVERGENCE_RESULT.json)
and [replay](../../../proof_lab/endpoint_aperture_convergence_certificate.py)
record every pivot and error.

At A=41/50, the exact scalar budgets give
\[
 e^{3A}<12,\quad2m_\Gamma<11,\quad p_A<22/5,
 \quad2(\sinh A-A)<1/5,\quad C_A<143/5.             \tag{SE13.25}
\]
The native graph return from SE6 yields
\[
 \|f\|_X^2\le s[f]+(143/5)\|Rf\|_2^2
           \le71500000000000001\,s[f].             \tag{SE13.26}
\]
Together with N_*<=11I/2 this proves
\[
 \|L_*f\|^2\le
 \left(1-\frac2{786500000000000011}\right)\|A_*f\|^2
 \quad(f\in X_{41/50}).                            \tag{SE13.27}
\]
Native subspace inclusion establishes the whole passage from 0.805
to 0.820. There is no interpolation of sampled matrix eigenvalues.

## 7. Current convergence status

At a fixed aperture and a fixed bounded support marker, SE10's
frequency-edge recovery still applies: the marker leaves the full
form unchanged, while the comparisons increase after their tail
condition holds. Modes and arithmetic must be refined with the
frequency. The present sequence of different apertures, caps and
markers is not itself that fixed-aperture convergence experiment.

The executed frontier is now 0.820. Its finite list of source floors
and observer upper bounds neither proves unbounded coverage nor
estimates a rate to the global norm-one target. The next event is
prime 7 at log(7)/2. The remaining obligation is cofinal actual source
control as in (SE13.12) or (SE13.14), or another global sign argument.
The global eta=0 sign, historical five-label endpoint, K0 and RH remain
open. The actual full-source pole row is not a construction of the
four other historical columns.

## 8. Moving observers and the invariant formulation

The companion [moving-reference index theorems](SE13_MOVING_REFERENCE_INDEX_THEOREMS.md)
give the precise observer-independent reading of this development.
They state covariant Atiyah--Singer descent and a block inverse
certificate, moving-reference Birman--Schwinger inertia, and the
covariant spectral-flow/suspension theorem. The actual-source
Theorem IV proves that kappa_eta=N_-(S_b+eta I) is finite for every
positive eta, is unchanged by faithful observer charts, and vanishes
for a cofinal eta sequence exactly when the global source is nonnegative.

This is the invariant-zero form of the remaining proof condition.
The same theorem identifies the intrinsic recovery burden with
||O_*||^2. It also proves that, for each fixed positive eta, cofinal
aperture negative counts eventually recover the entire finite count.
Different apertures need not already have the same count or burden.
An arbitrary change of reference that preserves the represented form
preserves its inertia; it need not preserve its relative numerical gap.

The new radius proves zero local obstruction on X_(41/50); no global
integer value is inferred. The actual source is not Fredholm at its
essential zero threshold. Its positive-eta family, rather than a
direct eta=0 substitution into the classical index theorem, supplies
the justified endpoint criterion.

See [source lineage](SE13_SOURCE_RECORD.md),
[verification scope](SE13_SCOPE.md) and [pins](SE13_SOURCE_PINS.json).
Written proofs, finite computation, source integrity, proof-assistant
verification and external review remain separate evidence classes.
