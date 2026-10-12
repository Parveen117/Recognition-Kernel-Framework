# SE9: Prime-event crossing and continuity in the native pairing

12 October 2026. Owner: Monty Dabas.

The corrected source is now certified beyond the activation of prime 3.
Keeping the reference aperture 1/2, take c=9/8 and physical radius 9/16.
The complete odd carrier, with both primes and the negative pole retained,
satisfies
\[
 \boxed{s[f]\ge\frac1{500000}\|Rf\|_2^2,
 \qquad s[f]\ge\frac1{9906251}\|f\|_X^2,
 \quad f\in X_{9/16}.}                              \tag{SE9.1}
\]
The resulting exact local joint observer has squared reserve
2/108968761. Every smaller aperture inherits these bounds, including the
whole passage through c=log 3. This is one certified event crossing;
the next prime-power event, c=log 4, and a cofinal sign rule remain open.

There is also an exact event-continuity result. A new prime contribution
can have nonvanishing L2 operator norm immediately after activation,
however small its overlap. Its norm in the native graph pairing tends
to zero, with an explicit frequency bound. A fixed finite catalogue
keeps the actual source equation unchanged across the event. A smooth
lower comparison then permits a full signed-operator certificate.

## 1. Source and contribution boundary

Use [SE4's corrected central-Gamma source](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md),
[SE5's native graph estimates](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md),
and [SE8's actual dilation](SE8_MOVING_OBSERVER_AND_SIGNED_TRANSPORT.md).
SE2 already proves the general observer equation, transport cocycle and
cofinal completion criterion. None of those general statements is new
in SE9. SE7 supplies the frequency-comparison method and interval
primitives; their literature provenance is retained.

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the admitted T35 logarithmic representation. Its native
pairing remains fixed on the reference carrier X_(1/2). Write
\[
 g=Rf,\quad (D_cg)(x)=c^{-1/2}g(x/c),\quad
 \Phi_c=R^{-1}D_cR,\quad
 G(t)=\Re\psi(1/4+it/2)-\log\pi.                     \tag{SE9.2}
\]
D_c is L2-unitary; Phi_c is bounded and invertible between the relevant
native apertures, with the transported metric proved in SE8. It is
generally not native-unitary. The parameter c is a dilation label,
not the regularization parameter eta.

## 2. One source equation through an activation event

For any fixed C>=1, retain the finite catalogue
\(\mathcal P_C=\{n\ge2:\Lambda(n)>0,\log n\le C\}\).
For every 1<=c<=C the exact transported form is
\[
 \begin{split}
 s_c[g]={}&\int G(t/c)|\widehat g(t)|^2\frac{dt}{2\pi}
 -\sum_{n\in\mathcal P_C}w_n\Re\langle g,T_{a_n(c)}g\rangle\\
 &-2|\langle h_c,g\rangle|^2,\qquad
 w_n=\frac{2\Lambda(n)}{\sqrt n},\quad
 a_n(c)=\frac{\log n}{c},\quad
 h_c(y)=\sqrt c\sinh(cy/2).
 \end{split}                                          \tag{SE9.3}
\]
Here g is odd, supported in [-1/2,1/2], and T_a g(x)=g(x-a).
The inner-product convention does not affect the squared pole term.
If a>=1 the supports overlap only on a null set, so the correlation
is exactly zero. Thus retaining a not-yet-active catalogue entry does
not alter the full source. Equality at an event causes no boundary
atom for these L2 states. The core identity extends by native continuity.

For C=9/8 the replay encloses
\[
 \log2<1<\log3<9/8<\log4,
 \quad \mathcal P_C=\{2,3\},\quad
 w_2+w_3<9/4.                                       \tag{SE9.4}
\]
Prime 3 is therefore already present in (SE9.3) on both sides of its
activation, with its actual translated position. Gamma and both the
argument and prefactor of the pole move as well.

## 3. A small new overlap is not a small L2 operator

Consider a single catalogue entry with 1/2<a<1. Put
I_a=[a-1/2,1/2] and write u for the positive-half restriction of an odd
g. Direct substitution gives the real correlation
\[
 \langle g,T_ag\rangle
 =-\int_{I_a}\overline{u(x)}u(a-x)\,dx,
 \qquad \|g\|_2^2=2\|u\|_2^2.                      \tag{SE9.5}
\]
The reflection x->a-x is a self-adjoint unitary on L2(I_a). Under the
unitary identification g->sqrt(2)u, the negative prime contribution
is (w_n/2) times that reflection, extended by zero off I_a. It has
both eigenvalues +w_n/2 and -w_n/2: choose respectively symmetric or
antisymmetric nonzero functions supported in I_a. Consequently
\[
 \|B_{n,c}\|_{L^2_{\rm odd}\to L^2_{\rm odd}}
 =\frac{w_n}{2}=\frac{\Lambda(n)}{\sqrt n},
 \qquad 1/2<a_n(c)<1.                               \tag{SE9.6}
\]
At a=1 the compressed operator is zero. Shrinking overlap alone
therefore does not imply L2 norm continuity. This is a statement about
one compressed prime term, not a negative witness for the full source.

## 4. Native continuity and an explicit event modulus

The native norm contains the exact Fourier weight 1+|G(t)|, and
||R||<=1. SE5 proves G(U)->infinity by its positive series. For U
with G(U)>=0, put w_U=1+G(U). For every f in X_(1/2),
\[
 \int_{|t|>U}|\widehat {Rf}(t)|^2\frac{dt}{2\pi}
 \le w_U^{-1}\|f\|_X^2.                            \tag{SE9.7}
\]
Let C_a=(T_a+T_(-a))/2, and let R_0 denote the restriction of R to
this reference carrier. Fourier transformation gives multiplier cos(at).
On |t|<=U its change is at most U|a-b|; on the complement it is at
most 2. Since the multiplier preserves the two frequency bands,
there are no cross blocks to discard. The self-adjoint quadratic-form
bound is
\[
 \boxed{\|R_0^\dagger(C_a-C_b)R_0\|
 \le U|a-b|+\frac2{1+G(U)}.}                        \tag{SE9.8}
\]
The dagger is the adjoint to the native reference pairing. First fix
large U, then let a approach b. This proves native operator-norm
continuity. In particular, at c_n=log n, for c just above c_n,
\[
 \|R_0^\dagger B_{n,c}R_0\|
 \le w_n\inf_{U:G(U)\ge0}
 \left(U\left|\frac{\log n}{c}-1\right|
              +\frac2{1+G(U)}\right)\longrightarrow0.
                                                        \tag{SE9.9}
\]
Here B_(n,c) denotes the L2 compressed prime operator from Section 3;
at c_n it vanishes. Functions concentrated in the shrinking interval
have a graph cost that the L2 estimate (SE9.6) does not include.

This also proves norm continuity of the complete pulled-back native
source S_c=Phi_c^dagger S_(c/2) Phi_c on every compact c-interval.
Indeed, the finite catalogue gives (SE9.8) for each prime. SE8 proves
|G(t/c)-G(t/d)|<=(5/2)|log(c/d)| uniformly in t. Finally h_c is
L2-continuous, with
\[
 \|h_c\otimes h_c-h_d\otimes h_d\|
 \le(\|h_c\|+\|h_d\|)\|h_c-h_d\|.                 \tag{SE9.10}
\]
These three bounds control every term of (SE9.3). No L2 differentiability
of translation, quantitative rate for every later source gap, or
differentiability of a local observer is inferred. Continuity alone
does not prevent an eigenvalue from reaching zero.

## 5. A fixed-band lower comparison through prime 3

For 1<=c<=C=9/8 define
\[
 \Psi_c(t)=G(t/c)-w_2\cos(t\log2/c)-w_3\cos(t\log3/c),
 \quad T=96,\quad b=1/5.
                                                        \tag{SE9.11}
\]
The prime-3 cosine remains in this comparison even before activation.
Its low-band part need not vanish: the cancellation in (SE9.3) uses
all frequencies. We do not identify a frequency-restricted prime
term with the whole physical event.

The enclosed constant satisfies m_Gamma<27/5. At t/c>=T/C=256/3,
the first 128 positive Gamma summands alone give
\[
 G(256/3)\ge
 \sum_{k=0}^{127}\frac{(128/3)^2}
 {(k+1/4)((k+1/4)^2+(128/3)^2)}-\frac{27}{5}
 >\frac52.                                         \tag{SE9.12}
\]
G is increasing in |t|. Equations (SE9.4) and (SE9.12) imply
Psi_c(t)>1/4>b whenever |t|>=96, uniformly in the whole c-interval.
With F_T the Fourier restriction, define on odd L2[-1/2,1/2]
\[
 K_c=bI+F_T^*M_{\Psi_c-b}F_T-2h_c\otimes h_c,
 \qquad s_c[g]\ge\langle g,K_cg\rangle.             \tag{SE9.13}
\]
The star here is the L2 adjoint; native return uses R_0^dagger and
the metric in SE8. The domination holds on the source form domain.

This fixed-catalogue comparison is real analytic in c>0 locally along
the stated interval, in bounded-operator norm. On a compact frequency
band the half-sum digamma extension, the prime cosines and h_c have
uniformly convergent local power series in c; the digamma poles stay
away from a sufficiently small complex neighborhood of each positive c.
The bounded band transform and rank-one product preserve those series.
Thus the event creates no forced discontinuity in K_c. Only K_C is
certified positive below; we do not assert positivity of every K_c.

## 6. The executed full-carrier certificate

Use the same normalized Legendre basis as SE7, now retaining the
52 odd orders n=1,3,...,103. Write
\[
 \phi_n(y)=\sqrt{2n+1}P_n(2y),\quad
 v_n(t)=(-1)^{(n-1)/2}\sqrt{2n+1}\,j_n(t/2),\quad
 q_n=\sqrt{C(2n+1)}\,i_n(C/4).
                                                        \tag{SE9.14}
\]
Here i_n is the modified spherical Bessel function. The exact leading
block A of K_C is
\[
 A_{nm}=b\delta_{nm}
 +\frac1\pi\int_0^{96}(\Psi_C(t)-b)v_n(t)v_m(t)\,dt
 -2q_nq_m.                                          \tag{SE9.15}
\]
All mixed entries are retained. This is a lower-comparison matrix,
not the historical five-label Feshbach matrix or SE6's F_15.

The standard-library [replay](../../../proof_lab/endpoint_prime_event_certificate.py)
uses the immutable SE7 outward interval arithmetic, constants, Gamma,
cosine and Gauss primitives. The ambient precision is guarded at 90
digits as in SE8. The larger Bessel range uses enclosed j_104 and
j_105 series followed by the exact downward recurrence. Ninety series
corrections are retained; the first omitted term bounds the alternating
tail because its subsequent absolute ratios decrease and are below one
for z<=48. The pole uses a positive series with a geometric tail and
retains the exact outside factor C in its Gram.

There are 768 Gauss-8 panels of width 1/8. Their rho=7 ellipses satisfy
|Im t|<1/4 and |t|<97. For beta_k=2k+1/2, a uniform analytic bound
for |Psi_c-b| is
\[
 M_s=\frac{27}{5}+10\sum_{k<100}\frac1{\beta_k}
 +\frac83\,97^2[(401/2)^{-3}+\tfrac14(401/2)^{-2}]
 +3+\frac15<100.                                   \tag{SE9.16}
\]
The Gamma proof is SE7's rational-series argument with 100 initial
terms. For the prime part, |Im(t log p/c)|<9/32 and
exp(9/32)<4/3; together with w_2+w_3<9/4 this gives the bound 3.
The Legendre integral gives |v_n v_m|<4/3 and pi>3. Thus M=100
also bounds every analytic integrand in (SE9.15). The same
Chebyshev-remainder proof as SE7 gives per-entry quadrature error
\[
 \epsilon_Q=4\cdot96\cdot100\,
                   \frac{7^{-16}}{1-1/7}.           \tag{SE9.17}
\]
Node/weight enclosures and all evaluation remainders are included
separately. In particular the Gamma tail uses y=t/(2C), so
y<=128/3<513/4, within the proved domain of its alternating expansion.

The complete complement starts at n=105. Set
\[
 a_f=\frac{48^{105}/209!!}{1-48^2/(211\cdot213)},\quad
 a_h=\frac{4(C/4)^{105}/209!!}{1-(C/4)^2/(211\cdot213)}.
                                                        \tag{SE9.18}
\]
Rodrigues' bound and decreasing successive odd-order ratios make
these bounds for the entire discarded vectors. The head Fourier
vector has norm at most sqrt(52)<8. The full pole vector has norm
squared sinh(C/2)-C/2<1. The tail block and mixed block therefore obey
\[
 D\ge(b-\tau_D)I,\quad \|B_{\rm mix}\|\le\tau_B,
 \quad \tau_D=3200a_f^2+2a_h^2<10^{-30},\quad
 \tau_B=25600a_f+2a_h<10^{-16}.                     \tag{SE9.19}
\]

Let A_tilde be the exact rational decimal matrix in the
[archive](../../../proof_lab/ENDPOINT_PRIME_EVENT_MATRIX.json).
The maximum row sum of interval radii plus 52 epsilon_Q gives
\[
 \|A-A_{\rm tilde}\|<7.011\cdot10^{-8}.
                                                        \tag{SE9.20}
\]
Interval LDL certifies 52 positive pivots of
A_tilde-(3/10^6)I. It follows that A>=I/400000. Including (SE9.19),
\[
 K_C\ge[\min(1/400000,b-\tau_D)-\tau_B]I
 >\frac1{500000}I.                                  \tag{SE9.21}
\]
The [result](../../../proof_lab/ENDPOINT_PRIME_EVENT_RESULT.json)
records every pivot, exact rational error/tail budgets and the matrix
SHA-256. This is a replayed infinite-carrier implication from a finite
interval certificate, not a floating-point eigenvalue claim.
The bijection Phi_C and the L2 unitarity of D_C turn (SE9.21) into
the physical source bound (SE9.1) on every state of X_(9/16).

## 7. Native observer and coverage of the entire passage

For A=C/2=9/16 the replay checks
\[
 e^{3A}<11/2,\quad m_\Gamma<11/2,\quad p_A<9/4,
 \quad\beta_A=2(\sinh A-A)
 \le\frac{A^3}{3(1-A^2/20)}<1/16.                  \tag{SE9.22}
\]
The last estimate sums the sinh tail using its largest successive
ratio A^2/20. SE6's graph bound then gives
\[
 \|f\|_X^2\le s[f]+\frac{317}{16}\|Rf\|_2^2
 \le9906251\,s[f].                                  \tag{SE9.23}
\]
Together with N_*<=11I/2, this proves the joint-target inequality
\[
 \|\mathcal L_*f\|^2
 \le\left(1-\frac2{108968761}\right)\|A_*f\|^2,
 \qquad f\in X_{9/16}.                              \tag{SE9.24}
\]
Thus A_*f->L_*f defines a unique contraction on the closed range
Y_C=A_*(X_(C/2)). Its zero extension is the local exact observer O_C.
For c<=C, put Y_c=A_*(X_(c/2)) and O_c=O_C P_(Y_c). On shared
event vectors these observers agree exactly. Nested native subspaces
and the endpoint bound cover every c between 1 and C, including
c=log 3; no unverified interpolation of comparison eigenvalues is used.

The stronger SE7 and SE8 constants on their smaller apertures are
preserved. This weaker common floor on a larger range is sufficient
to cross the event. It is not evidence that the true floor varies
monotonically under the chosen lower comparisons.

The remaining global obligation is a proved cofinal sequence of such
full-source certificates, or another sign-preserving rule that covers
the entire odd core. Native continuity and a smooth comparison do
not supply that rule. SE4's escape obstruction to a uniform strict
global reserve remains. No global eta=0 sign, historical five-label
closure, K0 or RH proof is claimed.

See [sources](SE9_SOURCE_RECORD.md), [scope](SE9_SCOPE.md) and
[pins](SE9_SOURCE_PINS.json).
