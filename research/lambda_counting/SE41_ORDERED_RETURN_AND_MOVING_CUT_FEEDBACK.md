# SE41: ordered return recovery with a moving cut and retained Smriti

13 October 2026 (Asia/Kolkata). Owner: Monty.

This develops the useful correction idea in the supplied sine/curvature
notes after reading the actual thermodynamic curvature construction.
The target is a fixed **ordered return operator**, not a scalar assigned
the name curvature. A moving observer learns that operator; its relative
residue converges to the identity while its calibration retains the
original return. No physical connection is flattened by this calculation.

The source record distinguishes the additive thermo response, NT's native
connection and the proposed sine recurrence. The recurrence is not used
as a historical or physical theorem. The new feedback is an exact rational
composition of the existing native Cayley operations.

## 1. Native objects, source, and observation contract

Start with the existing typed cuts, cut scalars, derived central iota,
lawful composition and dagger. Let E be a finite free module of rank d
over the complex cut scalars. I is its identity morphism; additive-neutral
residues have their own type and are not substituted for the primitive Cut.
For quantitative convergence, admit a positive pairing h, for example the
declared native response pairing of NT-1. Dagger and operator norm below
are relative to h. Compatible coordinates may represent that pairing;
they do not create it. The formal unit-depth result in section 6 needs
no numerical norm or analytic evaluation of Lambda.

Let U_1,...,U_m be acquired or lawfully specified, invertible native
arrows around a closed protocol, each preserving the appropriate pairing.
Later arrows multiply on the left. Their actual return is

\[
U_*=U_m\cdots U_1:E\longrightarrow E,
\qquad U_*^\dagger U_*=I.                         \tag{41.1}
\]

Keep the ordered word and its source identity in Smriti. U_* is fixed
throughout this stage. No trace, eigenvalue list or diagram permutation
is silently substituted for that word.

In the smooth thermo realization, the declared open connection is C=A-M,
where M is the **prior** same-carrier, tensorially transforming Smriti form.
NT-2 and NT-5 give

\[
F^C=F^A-D_AM+M\wedge M.                           \tag{41.2}
\]

The present norm theorem applies when C preserves h. In particular,
if A is h-compatible and M is h-skew, C is h-compatible. Its closed
parallel transport is then an admissible U_* in (41.1). A general M in
NT-5 need not have that property. The discrete theorem also applies
directly to specified unitary arrow words without a continuous material
model. It does not identify Cayley steps with a particular physical flow.

Let B_n be the observer's unitary calibration, starting from any declared
B_0. Define the measured relative return

\[
W_n=B_n^{-1}U_* .                                  \tag{41.3}
\]

The observer must actually recover the required W_n readings by the
protocol below, or by a separately proved faithful decoder. Their
availability is not inferred from a drawing or from the desired answer.
With an exact full bank, B_n W_n already determines U_* and permits the
direct reset B_{n+1}=B_n W_n. The iterative theorem below instead proves
a particular incremental correction, its error bound and its retained
unit-depth behavior. It is not a claim of recovering the source from
less information than that bank supplies.

## 2. Theorem 1: full return readings and finite branch repair

For any h-orthogonal cut P and Q=I-P, the complete block bank is

\[
PWP,\quad PWQ,\quad QWP,\quad QWQ.                 \tag{41.4}
\]

Its sum is W. Equivalently, for a declared input basis e_j, acquiring
both PWe_j and QWe_j for every j recovers each column We_j and hence W.
This is a sufficient bank, not a universal minimum sensor count.

The two ordered return readings

\[
E(W)=(W-W^{-1})/2,\qquad S(W)=(W+W^{-1})/2         \tag{41.5}
\]

satisfy W=S+E. E alone does not distinguish W=I from W=-I. Moreover,
PWP alone can hide orientation even away from that branch: for
R=[[0,-1],[1,0]], P=diag(1,0) and
W_\pm=(3/5)I\pm(4/5)R, both accepted compressions are (3/5)P.
Their complementary readings QW_\pm P differ. P E(W_\pm) P=0
does not certify W_\pm=I.

The rational return chart is

\[
T(W)=(W-I)(W+I)^{-1}.                             \tag{41.6}
\]

It requires W+I invertible. If this fails, finite native central-phase
calibration repairs the chart as follows. For j=0,...,d set

\[
q_j=\frac{1+\iota j}{1-\iota j},\quad
B'=Bq_j I,\quad W'=q_j^{-1}W.                     \tag{41.7}
\]

At least one j has W+q_j I invertible, and therefore W'+I invertible.
Every candidate preserves B'W'=BW and unitarity. In particular an
antipodal return is detected and recharted, rather than declared closed.

**Proof.** Expanding (P+Q)W(P+Q) proves the block identity. The displayed
two-dimensional examples prove the collisions. Each q_j has unit norm,
and cross multiplication shows that distinct real j give distinct q_j.
In any faithful d-dimensional coordinate representation,
det(W+zI) is a monic polynomial of degree d. It cannot vanish at d+1
distinct scalar points. Finally W'+I=q_j^{-1}(W+q_j I).
These are finite algebraic invertibility tests on the decoded return;
the central iota is not the internal, possibly noncentral EMK element R.
QED.

No lower noise margin follows from that root count alone. If a numerical
implementation cannot distinguish singularity from a small singular value,
it needs an enclosure or a measured chart margin. The exact controls use
rational rank and inverses. The finite d+1 proof is not claimed for an
infinite-dimensional carrier.

## 3. Theorem 2: rational feedback and quantitative convergence

Assume W is h-unitary and W+I is invertible. Write T=T(W), E=E(W) and

\[
Q(W)=(I+E/2)^{-1}(I-E/2).                         \tag{41.8}
\]

Then T^dagger=-T, E^dagger=-E, Q is unitary, and every inverse in
(41.8) exists. The feedback and calibration updates are

\[
\boxed{W_+=WQ(W),\qquad B_+=BQ(W)^{-1}.}          \tag{41.9}
\]

They obey the exact identities

\[
\boxed{T(W_+)=-T^3(I-2T^2)^{-1}=:\Psi(T),}
\qquad \boxed{B_+W_+=BW=U_*}.                    \tag{41.10}
\]

For r=||T||,

\[
\|\Psi(T)\|\le\frac{r^3}{1+2r^2},\qquad
\|\Psi(T)\|\le r^3,\qquad
\|\Psi(T)\|<r/2\quad(r>0).                       \tag{41.11}
\]

Thus iteration stays in the chart, T_n tends to the additive-neutral
operator, W_n tends to I, and B_n tends to the unchanged U_*. In fact

\[
\|U_*-B_n\|=\|W_n-I\|\le 2\|T_n\|.             \tag{41.12}
\]

**Proof.** Unitarity gives W^dagger=W^{-1}. Taking the adjoint of
(41.6), with its ordered factors, gives T^dagger=-T. A skew-adjoint
operator D has I+D invertible in the finite positive carrier because
||(I+D)x||^2=||x||^2+||Dx||^2. This also bounds its inverse norm by 1.
It applies to I-T and I+E/2. The inverse Cayley expression is

\[
W=(I+T)(I-T)^{-1},\qquad E=2T(I-T^2)^{-1}.
\]

All the displayed rational functions of this one T commute. Substituting
in (41.8), multiplying, and taking (W_+-I)(W_++I)^(-1) gives
(41.10). In particular I-2T^2=I+2T^dagger T is positive and invertible.
The result Psi(T) is skew-adjoint, so its inverse Cayley image has no
antipodal eigenvalue. The Cayley factor of skew E is unitary. Since
Q(W) commutes with W, BQ^(-1)WQ=BW proves the reconstruction identity.

For the bound set S=-T^2=T^dagger T, with 0<=S<=r^2I. Finite positive
spectral calculus, or diagonalization in the admitted pairing, gives

\[
0\le S(I+2S)^{-1}\le\frac{r^2}{1+2r^2}I.
\]

Since Psi(T)=T S(I+2S)^(-1), this proves (41.11). Iteration gives
||T_n||<=2^(-n)||T_0||. The identity
W-I=2T(I-T)^(-1), together with the inverse bound above, proves
(41.12). B_n is unitary, so multiplication by it preserves the norm.
QED.

This imports only the stated finite positive spectral calculus for the
norm estimate; the feedback and reconstruction identities follow directly
from the native associative algebra. It does not assume that independently
ordered protocol arrows commute.

### The phase sector and the supplied sine idea

On a supplied rotational subalgebra R^2=-I, R^dagger=-R, write T=rR.
Then (41.10) becomes

\[
\boxed{r_+=r^3/(1+2r^2)}.                          \tag{41.13}
\]

The exact sequence from r=1 begins 1,1/3,1/33,1/36003.
If an analytic angular chart is admitted, r=tan(e/2) and
W=cos(e)I+sin(e)R. Then (41.9) is

\[
e_+=e-2\arctan(\sin(e)/2),\qquad -\pi<e<\pi.
\]

This rational Cayley correction is not the identical sine iteration.
The notes' theta_+=theta+sin(theta), near an odd-pi target, instead gives
e_+=e-sin(e)=e^3/6+O(e^5). Both have a cubic local residual; the rational
operation above has its own exact native reconstruction and norm proof.
Neither sine nor that analogy defines the whole curvature two-form.

## 4. Theorem 3: moving calibration, cut, and retained return

Let g_n be any invertible change of native frame. Transport the pairing,
central iota, cut, target and readings consistently. In coordinates put

\[
h'_n=g_n^* h g_n,\quad
P'_n=g_n^{-1}P_ng_n,\quad
B'_n=g_n^{-1}B_ng_n,\quad W'_n=g_n^{-1}W_ng_n.
\]

Here star denotes conjugate transpose of a coordinate matrix; it is
distinct from the h-adjoint dagger used above. The h'_n-adjoint is
(h'_n)^{-1}(\cdot)^*h'_n.

Here P_n may itself be any available h-orthogonal cut at step n; it is
not required to remain constant. Every step must retain its full bank
(41.4). If Z_n=g_n^{-1}g_{n+1}, the update in moving coordinates is

\[
\begin{split}
W'_{n+1}&=Z_n^{-1}W'_nQ(W'_n)Z_n,\\
B'_{n+1}&=Z_n^{-1}B'_nQ(W'_n)^{-1}Z_n,\\
T'_{n+1}&=Z_n^{-1}\Psi(T'_n)Z_n.
\end{split}                                      \tag{41.14}
\]

The product B'_n W'_n is g_n^{-1}U_*g_n. All norm estimates hold in
the transported pairing. The cut may move because full labelled readings
recover the same current relative return before its update.

**Proof.** Sums, products and inverses commute with conjugation. Therefore
E,Q,T and Psi all intertwine with g. Insert g_{n+1}=g_n Z_n in (41.9).
The transported pairing makes g_n an isometry between the represented
carriers. The block-bank identity holds for each P_n separately. QED.

Keep the actual source word, chart changes and (B_n,W_n) in Smriti.
The limiting calibration stores U_*; it does not establish U_*=I.
Even the full endpoint U_* does not recover an arbitrary winding lift
or the original ordered word. For example R^4=I and the empty word have
the same endpoint but distinct declared paths. A recorded path/lift must
therefore remain separate when the target distinguishes it.

The algorithmic B_n is not NT-5's prior constitutive M. Changing B_n
learns an unchanged return. It does not retrospectively choose M=A,
delete raw curvature, or assert that a measured physical loop has healed.

### Why the complement term belongs to the retained target

NT-6 proves, for the same-carrier connection and a smooth moving cut,

\[
F^P_{ij}=PF_{ij}P+P[D_iP,D_jP]P,\quad
D_iP=\delta_iP+[A_i,P].                           \tag{41.15}
\]

For a constant cut this correction is
-PA_iQA_jP+PA_jQA_iP. It contains both ordered complement returns.
Thus a certificate of the compressed F^P is not a certificate of the
full F. The finite example A_1=R,A_2=RK,P=(I+K)/2 in NT's diagonal
K chart has F=-2K and F^P=0. The controls replay this cancellation.
Equation (41.15) is consumed from NT-6, not claimed as a new theorem.

## 5. Theorem 4: reading-error bound for one feedback step

Let the actual W be unitary. Suppose the retained readings supply a
skew-adjoint estimate Ehat of E(W), with ||Ehat-E||<=epsilon. Apply
the unitary calibration update using Qhat=Q(Ehat), where
Q(E)=(I+E/2)^(-1)(I-E/2). The actual new residue is

\[
\widetilde W_+=\widehat Q W,
\]

not in general W Qhat; Ehat need not commute with W. The actual source
still satisfies (B Qhat^(-1)) Wtilde_+=BW. The ideal residue is
W_+=Q(E)W=WQ(E), and

\[
\|\widetilde W_+-W_+\|\le\epsilon.                \tag{41.16}
\]

If ||T(W)||<=r, set q=r^3/(1+2r^2) and m=2/sqrt(1+q^2).
When epsilon<m, the noisy return stays in the Cayley chart and

\[
\|T(\widetilde W_+)-T(W_+)\|
\le\frac{2\epsilon}{m(m-\epsilon)}.              \tag{41.17}
\]

**Proof.** Q(E)=2(I+E/2)^(-1)-I, so the resolvent identity gives

\[
Q(Ehat)-Q(E)=-(I+Ehat/2)^{-1}(Ehat-E)(I+E/2)^{-1}.
\]

Both inverse norms are at most one. Multiplication by W proves (41.16).
The inverse Cayley formula gives sigma_min(I+W_+)>=2/sqrt(1+q^2)=m
in the admitted finite positive representation. A perturbation of norm
epsilon<m leaves an inverse with norm at most 1/(m-epsilon).
Finally T(W)=I-2(I+W)^(-1) and a second resolvent identity prove (41.17).
QED.

A raw noisy E-reading can be projected to (Ehat-Ehat^dagger)/2, a
norm-contractive operation relative to the true skew E. The removed
self-adjoint reading must be retained as an incompatibility channel.
These bounds do not infer epsilon from closure or promise convergence
to an exact answer under fixed nonzero measurement error.

## 6. Theorem 5: at least triple unit-depth correction

Let T belong to Lambda^m A[[Lambda]], m>=1, in the established associative
unit-memory completion. Formal inverses have their unit cut, so

\[
\Psi(T)=-\sum_{j\ge0}2^j T^{2j+3}
          \in\Lambda^{3m} A[[\Lambda]].           \tag{41.18}
\]

After k steps T_k has order at least 3^k m. If the initial cut
calibration has been recovered, the exact identity B_k W_k=U_*
therefore gives B_k=U_* modulo Lambda^(N+1) whenever 3^k m>N.

**Proof.** The factor 2T^2 has positive unit order, so its formal
geometric inverse exists. Every displayed term has order at least 3m.
Iteration proves the bound. Since W-I=2T(I-T)^(-1), the same order
controls the reconstruction error. Products keep their native order;
coefficient commutation has not been assumed. QED.

Equality of the leading order requires that the leading coefficient's
cube not vanish. Nilpotent coefficients may give faster correction.
An arbitrary initial cut mismatch has order zero and does not satisfy
this theorem. Lambda is the retained counting unit, not an RH shift eta.
Formal depth completion alone is not numerical convergence at a chosen
nonzero Lambda; section 3 supplies a separate analytic, unitary contract.

## 7. Scope and countermodels

The source-reading certificate is the detached bank decoded for its
stated ordered return and reconstruction target. The implementation uses
Python 3.12 and existing exact rational matrix helpers solely as an
admitted finite representation; no replacement native engine is built.

Important controls are actual mathematical distinctions:

- W=-I has E=0 and fails the unshifted chart; section 2 repairs it.
- Opposite turns have the same accepted compression, and distinct
  complementary readings.
- Reordering noncommuting loop arrows changes the source return.
- Dropping the moving frame or updating B without its inverse factor
  breaks source reconstruction.
- Unitary/skew typing is load-bearing. For T=(2/3)K, K^2=I,
  the same rational expression gives Psi(T)=-(8/3)K, an expansion.
- Closed corrected residue retains raw return in B. It is not evidence
  that raw curvature or a negative RH source sector disappeared.

This stage does not prove a universal sine/curvature isomorphism,
atomic-shell quantization, physical stabilization, or RH. It supplies
an observer calibration and memory theorem for finite unitary ordered
returns, a formal unit-depth result, and a finite-error step estimate.
The actual RH source and SE39/SE40 analytic requirements are unchanged.

See [scope](SE41_SCOPE.md), [sources](SE41_SOURCE_RECORD.md),
[source pins](SE41_SOURCE_PINS.json),
[replay](../../proof_lab/ordered_return_feedback.py) and
[readings](../../proof_lab/ORDERED_RETURN_FEEDBACK_RESULT.json).
