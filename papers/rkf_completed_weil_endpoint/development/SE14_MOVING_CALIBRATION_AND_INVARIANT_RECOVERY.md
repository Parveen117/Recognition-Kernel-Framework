# SE14: Moving source-null calibrations and uniform local recovery

12 October 2026. Owner: Monty.

The structural advance releases the fixed calibration in SE10's local
edge-recovery theorem. At a fixed admitted aperture, any uniformly
bounded family of exactly source-null multipliers has the same limiting
lower comparison edge. The selected multiplier may change at every
frequency refinement and need not converge. The proof retains weakly
escaping mass and controls all calibrations together.

The numerical development certifies radius 21/25=0.840 with three
source-null markers. Its full source floor is 1e-20, its native floor
is 1/2965000000000000000001, and its squared observer reserve is
2/32615000000000000000011. All smaller apertures follow by native
inclusion. The accompanying result and audit record execution and
verification separately from the general written proofs.

The native order remains typed cuts, cut scalars, derived iota, lawful
composition, targets and Smriti, followed by the admitted T35 graph
and T40 source representations. A Fourier multiplier below is a
calibration inside those adapters. It neither supplies a new physical
observation nor silently changes the native source or dagger.

## 1. Theorem: a class of calibrations with exactly the same source

Fix a finite positive scale c, the complex odd carrier
H=L2_odd([-1/2,1/2]), and the closed form q_c and domain D_c from
[SE10](SE10_PRIME_POWER_AND_CERTIFICATE_COMPLETENESS.md), Sections 2--3:
\[
 \begin{split}
 q_c[g]&=\int_{\mathbb R}\Psi_c(t)|\widehat g(t)|^2
                 \frac{dt}{2\pi}-2|\langle h_c,g\rangle|^2,\\
 \Psi_c(t)&=G(t/c)-\sum_{\log n\le c}
                   \frac{2\Lambda(n)}{\sqrt n}\cos(t\log n/c),
 \qquad h_c(y)=\sqrt c\sinh(cy/2),\\
 \lambda_c&=\inf_{g\in\mathcal D_c,\ \|g\|=1}q_c[g].
 \end{split}                                                     \tag{SE14.1}
\]
The symbol is continuous, even, bounded below and tends to infinity
as |t| tends to infinity. Its prime catalogue is finite. The source
domain and native graph identification are unchanged.

Let C>=0 and let M_C be any nonempty class of real even measurable
multipliers satisfying
\[
 \|m\|_\infty\le C,\qquad F^*M_mF=0\quad\hbox{on }H.             \tag{SE14.2}
\]
Here F is the complete Fourier isometry, with measure dt/(2pi).
Equality means the full compressed sesquilinear operator is zero,
not merely that selected diagonal samples vanish. Every such m leaves
q_c, its domain, kernel and inertia exactly unchanged.

For example, extend g by zero outside the unit interval. For |a|>=1,
\[
 \int\cos(at)|\widehat g(t)|^2\frac{dt}{2\pi}
       =\operatorname{Re}\langle g,T_a g\rangle=0.                \tag{SE14.3}
\]
The translated supports intersect on at most a measure-zero boundary.
Polarization proves the operator identity in (SE14.2), also for complex
odd inputs. Thus any real sum m(t)=sum_j alpha_j cos(a_j t), with
|a_j|>=1 and sum_j |alpha_j|<=C, is allowed. Infinite sums converge
uniformly when their coefficients are absolutely summable. This extends
the support identity already proved in [SE12](SE12_SUPPORT_MARKER_AND_PRIME_FIVE.md);
it is not a new translation or Parseval theorem.

Fix a positive cap b. There is U_0 such that Psi_c>=b+C outside U_0.
For T>=U_0 and m in M_C define
\[
 K_{T,m}=bI+F_T^*M_{\Psi_c+m-b}F_T-2h_c\otimes h_c,
 \qquad \ell(T,m)=\inf\sigma(K_{T,m}).                            \tag{SE14.4}
\]
The fixed-support band transform F_T is Hilbert--Schmidt. Hence
K_(T,m) is bI plus a compact self-adjoint operator. By (SE14.2),
\[
 q_c[g]-\langle g,K_{T,m}g\rangle
 =\int_{|t|>T}(\Psi_c(t)+m(t)-b)|\widehat g(t)|^2\frac{dt}{2\pi}
 \ge0,\qquad \ell(T,m)\le\min(b,\lambda_c).                      \tag{SE14.5}
\]
The first identity is on D_c; the second also uses compactness along
an orthonormal sequence to obtain ell<=b. This proves the theorem's
source identity and comparison assertions.

## 2. Theorem: uniform edge recovery without a limiting calibration

With exactly the preceding hypotheses,
\[
 \boxed{\lim_{T\to\infty}
    \sup_{m\in\mathcal M_C}|\ell(T,m)-\min(b,\lambda_c)|=0.}      \tag{SE14.6}
\]
Consequently any choices m_T in M_C recover the same capped lower
source edge. No convergence, continuity or finite-dimensional
parameterization of m_T is assumed. For a fixed m the comparisons
increase for T>=U_0. For varying m_T they need not be monotone.
For instance, m_j(t)=(-1)^j cos(t) has no limiting calibration, but
ell(T_j,m_j) still converges to min(b,lambda_c) whenever T_j tends
to infinity. This is an exact consequence of the theorem, not a
numerical convergence experiment.

**Proof.** The uniform upper bound is (SE14.5). If uniform lower
convergence failed, there would be T_j tending to infinity, m_j in
M_C, a real a<min(b,lambda_c), and unit vectors g_j such that
\[
 \langle g_j,K_{T_j,m_j}g_j\rangle\le a.                          \tag{SE14.7}
\]
Take a subsequence weakly converging to g, with ||g||<=1. Fix any
U>=U_0. Eventually T_j>=U, and positivity of the annular multiplier
gives K_(T_j,m_j)>=K_(U,m_j). Write K_(U,0)=bI+C_(U,0), with
C_(U,0) compact. Its quadratic readings converge under this weak
limit. In addition, compactness gives F_U g_j -> F_U g in norm, and
uniform boundedness of the markers gives
\[
 \begin{split}
 &|\langle F_Ug_j,m_jF_Ug_j\rangle
                 -\langle F_Ug,m_jF_Ug\rangle|\\
 &\hspace{1cm}\le C\|F_U(g_j-g)\|
                    (\|F_Ug_j\|+\|F_Ug\|)\longrightarrow0.
 \end{split}                                                     \tag{SE14.8}
\]
No subsequence of the multipliers needs to converge. The full null
identity applies to g in H even before its form-domain membership is
known. It gives
\[
 \langle F_Ug,m_jF_Ug\rangle
   =-\langle F_{|t|>U}g,m_jF_{|t|>U}g\rangle
   \ge-C\|F_{|t|>U}g\|^2.                                       \tag{SE14.9}
\]
Combining these statements with (SE14.7) and letting j tend to infinity,
\[
 b(1-\|g\|^2)+\langle g,K_{U,0}g\rangle
                         -C\|F_{|t|>U}g\|^2\le a.               \tag{SE14.10}
\]
As U tends to infinity, the last term vanishes by Plancherel. The
unmarked comparison forms increase to q_c, with value +infinity
off D_c, by SE10's domain theorem. The finite upper bound therefore
forces g into D_c. Taking this limit yields
\[
 b+(\lambda_c-b)\|g\|^2
 \le q_c[g]+b(1-\|g\|^2)\le a<\min(b,\lambda_c),                 \tag{SE14.11}
\]
which is impossible for 0<=||g||^2<=1. QED.

Uniform boundedness and exact full-source nullness are substantive
hypotheses. Agreement at finitely many readings is insufficient.
The theorem does not cover unbounded calibrations, changing source
domains or arbitrary changes of physical observation range. It holds
for positive, zero and negative lambda_c; it supplies no missing sign.

## 3. Theorem: uniform mode recovery and strict local completeness

Let P_N be the first N odd Legendre modes. At a fixed T the whole
family of compact corrections has uniformly vanishing head error:
\[
 \sup_{m\in\mathcal M_C}
 \|K_{T,m}-bI-P_N(K_{T,m}-bI)P_N\|\longrightarrow0.               \tag{SE14.12}
\]
**Proof.** The unmarked correction is compact. For E_m=F_T^*M_mF_T,
split E_m-P_N E_m P_N=(I-P_N)E_m+P_N E_m(I-P_N). Then
\[
 \|E_m-P_NE_mP_N\|
       \le2C\|F_T\|\,\|F_T(I-P_N)\|\longrightarrow0              \tag{SE14.13}
\]
uniformly in m. The last limit follows from compactness of F_T and
strong convergence of the projections. Add the unmarked correction.
QED.

If lambda_c>0, choose 0<r<min(b,lambda_c). Equation (SE14.6) gives
a sufficiently large T with ell(T,m)>r for every m in M_C, and
(SE14.12) then gives a sufficiently large common N. For each chosen
marker whose entries and bounds can be effectively enclosed, sufficiently
accurate arithmetic completes a finite strict-positive certificate.
SE7--SE13 provide those bounds for finite rational cosine sums.

Conversely, any valid finite certificate giving K_(T,m)>=rI with
r>0 proves lambda_c>=r by (SE14.5). A true zero edge does not imply
eventual strict positivity. No rate, universal optimizer, algorithm for
arbitrary measurable multipliers, or work bound is supplied. Modes,
frequency and accuracy remain distinct refinement parameters.

The finite-band effect of changing calibration is also exact:
\[
 \begin{split}
 K_{T,m'}-K_{T,m}
   &=F_T^*M_{m'-m}F_T=-F_{|t|>T}^*M_{m'-m}F_{|t|>T},\\
 |\langle g,(K_{T,m'}-K_{T,m})g\rangle|
   &\le\|m'-m\|_\infty\|F_{|t|>T}g\|^2.
 \end{split}                                                     \tag{SE14.14}
\]
This tends to zero for each fixed input and bounded pair of markers.
An operator-norm convergence assertion for this difference is not used.
The finite comparisons can have different inertia; only the complete
source is identical. SE13's faithful chart covariance concerns that
same source and does not identify different capped comparisons.

## 4. The radius-0.840 calibration and its complete tail

Set
\[
 c=42/25,\quad A=c/2=21/25,\quad b=1/10,\quad T=512,
 \qquad m(t)=-\tfrac13\cos t+\tfrac19\cos(2t)-\tfrac18\cos(3t).
                                                                    \tag{SE14.15}
\]
The coefficient norm bound is 41/72. Each shift is at least the
support width, so Section 1 proves the exact null identity. The prime
catalogue is {2,3,4,5}, with Lambda(4)=log 2. Interval logarithms
verify log 5<c<log 7. The old SE13 marker is not copied across the
scale change: at t_*=51819/100 the enclosed readings satisfy
\[
 \Psi_c(t_*)-\tfrac1{10}\cos t_*<0,
 \qquad \Psi_c(t_*)<b<\Psi_c(t_*)+m(t_*).                         \tag{SE14.16}
\]
These are multiplier readings, not negative source witnesses.

Put Xi=Psi_c+m. On [512,2048], SE8's Gamma derivative bound and the
complete prime/marker catalogue give
\[
 |\Xi'(t)|\le\frac5{2\cdot512}
       +\sum_n\frac{2\Lambda(n)}{\sqrt n}\frac{\log n}{c}
       +\tfrac13+\tfrac29+\tfrac38<5.                            \tag{SE14.17}
\]
The replay recursively bisects each unit interval and accepts a cell
with midpoint x and radius r only if its outward reading obeys
Xi(x)_lower-5r>b. Exact covered length must be 1536. The complete
partition, its minimum bound and its deterministic hash are recomputed
on every replay. Finite-grid parameter proposals are not this proof.

For the remaining frequencies, monotonicity of G and the independent
enclosures G(2048/c)>21/4 and sum_n 2Lambda(n)/sqrt(n)<22/5 yield
\[
 \Xi(t)>\frac{21}4-\frac{22}5-\frac{41}{72}
         =\frac{101}{360}>\frac1{10},\qquad t\ge2048.             \tag{SE14.18}
\]
Evenness covers the negative half-line. Thus the finite cover and
analytic far bound establish the complete comparison hypothesis.

## 5. Enclosing every mode, frequency and arithmetic error

Retain N=208 odd Legendre orders 1,3,...,415. With the normalizations
of SE7, the exact head is
\[
 H_{nm}=b\delta_{nm}+\frac1\pi\int_0^{512}
           (\Xi(t)-b)v_n(t)v_m(t)\,dt-2p_np_m,
 \quad p_n=\sqrt{c(2n+1)}\,i_n(c/4).                            \tag{SE14.19}
\]
All mixed entries are retained. The Gamma evaluator is SE12's
shift-128 complex formula with the absolute periodic-Bernoulli
remainder. The Bessel seeds are S_416,S_417, with 480 corrections
and an exact 240-place integer interval grid. The restored values
and node displacements use the unchanged outward interval class.

Gauss-24 uses 1024 panels of width 1/2. Increasing the analytic ellipse
parameter to rho=5 requires a new domain check. Its semimajor and
semiminor radii are 13/20 and 3/5, respectively, so
\[
 |\operatorname{Im}(t/c)|\le5/14<3/8,
 \qquad |t|<513.                                                 \tag{SE14.20}
\]
The gap to 3/8 is 1/56. With beta_k=2k+1/2, the inherited symmetric
digamma majorant is
\[
 M_s=\frac{269}{50}+34\sum_{k<520}\frac1{\beta_k}
 +\frac83\,513^2[(2081/2)^{-3}+\tfrac14(2081/2)^{-2}]
 +10+\frac1{10}<200.                                             \tag{SE14.21}
\]
The prime and marker contribution is bounded by
(22/5)exp(3/5)+(1/3)exp(3/5)+(1/9)exp(6/5)+(1/8)exp(9/5)<10.
The frequencies 2 and 3 must be included here, despite the marker's
zero full compression. The Legendre Fourier integral gives
|v_n v_m|<=exp(3/5)<2, and pi>3; hence M=256 is sufficient for
every analytic matrix integrand. The SE7 Chebyshev remainder gives
\[
 \epsilon_Q=4\cdot512\cdot256\frac{5^{-48}}{1-1/5}
          <1.845\cdot10^{-28}                                   \tag{SE14.22}
\]
per entry. This is over 40,000 times smaller than SE13's rho=4
quadrature bound with the same nodes; it is a bound improvement,
not a measured speedup or a corresponding claim about total error.

SE11's exact signed-Gram integer sums and rank-one operator error
enclose every node. Pole and forty-significant-digit candidate rounding
receive a separate symmetric row-sum allowance. The total head error
is the sum of those terms and N epsilon_Q. An isolated directed
512-digit LDL factorizes only the exact rational candidate, leaving
all source-to-candidate errors charged separately.

For the same projection, the first omitted odd order is 417. Put
\[
 a_f=\frac{256^{417}/833!!}{1-256^2/(835\cdot837)},
 \qquad a_h=\frac{4(c/4)^{417}/833!!}
                    {1-(c/4)^2/(835\cdot837)}.                   \tag{SE14.23}
\]
Rodrigues' bound, the geometric ratios and the real head-vector norm
at most one give the full infinite-complement estimates below. The
pole head norm is below one because
||h_c||^2=sinh(c/2)-c/2<1/8 by the enclosed native boundary budget.
\[
 \begin{split}
 D&\succeq(b-\tau_D)I,&
 \tau_D&=\frac{512\cdot256}{3}a_f^2+2a_h^2<10^{-54},\\
 \|B_{\rm mix}\|&\le\tau_B,&
 \tau_B&=\frac{512\cdot256}{3}a_f+2a_h<10^{-27}.
 \end{split}                                                     \tag{SE14.24}
\]
The executed rational tau_B is below 5.538e-29. No discarded mode
is identified with zero.

## 6. Theorem: the certified source and native invariant return

All 208 interval pivots of the candidate minus 3e-20 I are positive.
The complete leading-matrix operator error is below 2.120e-25,
including node error below 1.737e-25 and pole/archive error below
2.043e-39. Thus it is below 1e-20, the exact head has floor 2e-20,
and (SE14.24) proves
\[
 K_{512,m}\succeq
 [\min(2\cdot10^{-20},b-\tau_D)-\tau_B]I
 \succ10^{-20}I,
 \qquad s[f]\ge10^{-20}\|Rf\|_2^2\quad(f\in X_{21/25}).          \tag{SE14.25}
\]
This is a complete complex odd source statement, not just a head sign.

At A=21/25 the replay verifies exp(3A)<13, 2m_Gamma<11,
p_A<22/5 and 2(sinh A-A)<1/4. SE6's native graph budget is therefore
C_A<13+1+11+22/5+1/4=593/20. Its source-to-graph return gives
\[
 \begin{split}
 s[f]&\ge\delta\|f\|_X^2,
     &\delta&=\frac1{2965000000000000000001},\\
 \|L_*f\|^2&\le(1-\rho)\|A_*f\|^2,
     &\rho&=\frac2{32615000000000000000011}.
 \end{split}                                                     \tag{SE14.26}
\]
Here N_*<=11I/2, so rho=2delta/11. Native inclusion proves these
bounds on every X_A with A<=21/25, including the full passage from
0.820 to 0.840; the multiplier tail need not be re-proved at every
intermediate scale. The restrictions of the same exact observer remain
coherent as in SE13.

For the native compression of the same bounded source S_b, define
kappa_eta(A)=N_-(P_A(S_b+eta I)|X_A). Equations (SE14.25)--(SE14.26)
then give
\[
 \boxed{\kappa_\eta(A)=0\quad
      (0<A\le21/25,\ \eta\ge0),\qquad
      \dim\ker(P_AS_b|X_A)=0.}                                  \tag{SE14.27}
\]
These are actual local source invariants. Faithful coordinate changes
preserve them by [SE13's index theorems](SE13_MOVING_REFERENCE_INDEX_THEOREMS.md).
They are not the ordinary Fredholm index of a self-adjoint operator,
nor an identification of every local count with the uncomputed global
count. Inertia is intrinsic to the source and pairing; it is not
eliminated by choosing a sign convention.

The [replay](../../../proof_lab/endpoint_moving_calibration_certificate.py),
[matrix](../../../proof_lab/ENDPOINT_MOVING_CALIBRATION_MATRIX.json),
[result](../../../proof_lab/ENDPOINT_MOVING_CALIBRATION_RESULT.json),
[controls](../../../proof_lab/test_endpoint_moving_calibration_certificate.py),
[source record](SE14_SOURCE_RECORD.md), [audit](SE14_SCOPE.md) and
[pins](SE14_SOURCE_PINS.json) keep the executed evidence distinct from
the general written proofs.

## 7. What is still required globally

The new theorem removes a fixed marker from local recovery. It does
not remove the fixed-aperture hypothesis from that limit. The finite
radius sequence through 0.840 is bounded and is not a cofinal source
exhaustion. Sufficient local floors are not exact lower edges and
cannot be used as a measured distance to global stabilization.

SE13.I17 still states the complete invariant obligation: the actual
global kappa_eta must vanish along a cofinal sequence eta down to
zero. SE13.I18 guarantees eventual local capture of each fixed positive
eta count, but supplies no effective radius for that capture. Thus
the local zeros above do not finish the global eta-zero condition.
The actual source is non-Fredholm at zero by SE5; an Atiyah--Singer
index substitution does not supply its sign.

Prime 7 at log(7)/2 lies outside this aperture. Cofinal source signs,
global unit contraction, the historical five-label endpoint, K0 and
RH remain open. The present 208-mode comparison is not that five-label
matrix. No new elliptic adapter, priority claim, formal proof-assistant
verification, external review or universal calibration optimizer is
asserted.
