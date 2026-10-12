# SE11: A finer local certificate and an actual cutoff obstruction

12 October 2026. Owner: Monty.

The corrected full odd source is certified on the physical aperture
of radius 4/5. In the radius-1/2 reference chart the scale is C=8/5.
The executed bounds are
\[
 \boxed{s[f]\ge\frac1{250000000000000}\|Rf\|_2^2,
 \qquad s[f]\ge\frac1{6600000000000001}\|f\|_X^2,
 \quad f\in X_{4/5}.}                              \tag{SE11.1}
\]
The exact local joint observer has squared reserve
2/72600000000000011. All smaller apertures follow by native inclusion.
Prime 5 activates at radius log(5)/2, approximately 0.804719, and is
not crossed by this certificate.

A second executed result identifies a real obstruction in the current
comparison, before that event. At c=8047/5000 and T=256 an explicit
32-mode vector has a negative reading in the valid lower comparison.
Thus increasing modes or precision alone at that fixed cutoff cannot
prove positivity there. This is a failure of the comparison, not a
negative full-source value. It makes the next refinement decision
concrete rather than assuming that a larger matrix must work.

## 1. Source, native order and contribution boundary

The typed-cut, cut-scalar, derived-iota, composition, target and Smriti
order is unchanged. Fourier analysis and the Hilbert carrier below
are in the admitted T35/T40 logarithmic representation; coordinate
adjoints do not replace the native pairing or dagger.

[SE4](SE4_CENTRAL_GAMMA_AND_CRITICAL_RESERVE.md) supplies the corrected
Gamma--prime--pole source. [SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md)
and MP Gold 06 supply same-projection compact certification;
[SE6](SE6_PAIRED_APERTURE_AND_MOMENT_SCHUR.md) supplies native return;
[SE7](SE7_FULL_PRIME_ACTIVE_APERTURE.md) supplies the frequency minorant;
[SE8](SE8_MOVING_OBSERVER_AND_SIGNED_TRANSPORT.md) supplies actual
dilation; and [SE9](SE9_PRIME_EVENT_AND_NATIVE_CONTINUITY.md) supplies
the fixed catalogue and continuity. [SE10](SE10_PRIME_POWER_AND_CERTIFICATE_COMPLETENESS.md)
already proves completeness when frequency, modes and accuracy may
all vary. Those general results are reused, not renamed as new ones.

The additions here are the executed radius-4/5 certificate, an exact
integer assembly with an explicit signed rank-one error bound, and
an executed cutoff-failure witness. Compact-window positivity at this
radius has published prior art; this is a source-pinned RKF replay,
not a new general Weil criterion or a claimed record aperture.

## 2. The unchanged complete source and its lower comparison

Let H be the complex odd L2 carrier supported in [-1/2,1/2]. For
c between 1 and 8047/5000 use the catalogue {2,3,4}, with
\[
 \begin{split}
 \Psi_c(t)&=G(t/c)-\sqrt2\log2\cos(t\log2/c)
 -\frac{2\log3}{\sqrt3}\cos(t\log3/c)
 -\log2\cos(2t\log2/c),\\
 h_c(y)&=\sqrt c\sinh(cy/2),\\
 q_c[g]&=\int\Psi_c(t)|\widehat g(t)|^2\frac{dt}{2\pi}
                    -2|\langle h_c,g\rangle|^2 .
 \end{split}                                       \tag{SE11.2}
\]
Inactive catalogue entries have zero full correlation by support.
Lambda(4)=log 2, and the outside scale factor in the pole is retained.
The form domain and its identification with the native aperture are
those proved in SE10. Put b=1/10 and
\[
 K_{c,T}=bI+F_T^*M_{\Psi_c-b}F_T-2h_c\otimes h_c,
 \qquad T=256.                                    \tag{SE11.3}
\]
The star in this displayed chart is the L2 adjoint.

Both replays verify that the sum of prime weights is below 59/20
and m_Gamma<269/50. At each endpoint, the first 512 positive Gamma
terms give
\[
 G(T/c)\ge\sum_{k=0}^{511}
 \frac{y^2}{(k+1/4)((k+1/4)^2+y^2)}-\frac{269}{50}
 >\frac{16}{5},\qquad y=\frac{128}{c}.              \tag{SE11.4}
\]
Monotonicity of G therefore gives Psi_c(t)>1/4>b outside the band.
At the larger endpoint the same envelope also covers all smaller c
in this range. Thus K_(c,256)<=q_c is a genuine full-carrier minorant,
including at the later negative-comparison witness.

## 3. Exact signed-Gram assembly with a norm error

The normalized odd Legendre readings are
\[
 v_n(t)=(-1)^{(n-1)/2}\sqrt{2n+1}\,j_n(t/2),
 \qquad \widehat\phi_n(t)=i v_n(t).
                                                        \tag{SE11.5}
\]
For real t, Bessel's inequality applied to exp(ity) on an interval
of length one gives ||v(t)||_2<=1 for any finite collection of modes.
This unit bound is independent of the number retained.

At a quadrature node let M be the exact real measure including its
signed symbol, and v the exact real vector. Choose rational proposals
mu and u with |M-mu|<=delta and ||v-u||_2<=e. Then
\[
 \boxed{\|Mvv^*-\mu uu^*\|
       \le\delta+|\mu|e(2+e).}                     \tag{SE11.6}
\]
Indeed decompose the difference as (M-mu)vv*+mu(vv*-uu*), use
||v||<=1, ||u||<=1+e and
||vv*-uu*||<=||v-u||(||v||+||u||). The absolute value of mu is
essential: Gamma-minus-prime node measures need not be positive.
No cancellation between uncertain nodes is assumed.

The [assembler](../../../proof_lab/endpoint_precision_frontier_certificate.py)
chooses each proposal on the grid 10^(-50), enclosing its distance
to the entire outward interval. It uses the sum of coordinate error
bounds for e. If W and V_i are the integer numerators, each matrix
sum is evaluated exactly as
\[
 \frac1{10^{150}}\sum_{\text{nodes}} W V_iV_j .      \tag{SE11.7}
\]
Consequently these potentially cancelling sums have no accumulated
rounding error. The sum of (SE11.6) bounds their point-evaluation
operator error. The pole, conversion of exact rational sums and
forty-significant-digit archive rounding are enclosed separately
by a symmetric row-sum bound. This is an arithmetic improvement to
the same comparison, not a change of source or a second operator engine.

## 4. Refined constants, quadrature and the whole complement

The old 90-digit outward interval class, pi/log enclosures, cosine,
Hurwitz power sums and interval LDL are imported unchanged. The old
Gamma-ground enclosure has width about 1.516e-14; retaining it would
exhaust the new margin. Only the new stage refines that constant.
For k=1024, Euler--Maclaurin gives
\[
 \gamma=H_k-\log k-\frac1{2k}
       +\sum_{j=1}^{6}\frac{B_{2j}}{2j k^{2j}}+r,
 \qquad |r|\le\frac{|B_{12}|}{12k^{12}}.             \tag{SE11.8}
\]
The conservative last-included-term bound follows from the periodic
Bernoulli remainder; the usual real-positive next-term bound is even
smaller. With m_Gamma=gamma+pi/2+3log2+log(pi), the new enclosure
has width below 3.174e-38. No earlier constants or certificates are
overwritten. An independent shifted complex digamma computation at
shift 2048 checks this enclosure and four Gamma values.

At C=8/5 retain N=116 odd orders 1,3,...,231. Gamma uses 128 direct
positive terms and 64 alternating Hurwitz terms; for y=t/(2C)<=80,
the omitted signed tail lies in [0,y^130 zeta(131,513/4)]. Each
power sum has its own inherited Euler--Maclaurin enclosure. Bessel
seeds j_232,j_233 use 240 corrections, with a decreasing alternating
tail, then enclosed downward recurrence for 0<z<=128. Direct j_1,j_3
trigonometric controls check the larger range; no 90-digit accuracy
claim is made for a recurrence that loses working digits.

Gauss-24 on 512 panels of width 1/2 has exactness through degree 47.
Every root has a disjoint rational sign bracket refined by 260 exact
bisections; weights are enclosed by 2/((1-x^2)P'_24(x)^2).
For rho=4 the panel ellipse has semimajor radius 17/32, and
|Im(t/C)|<3/8, |t|<257. With beta_k=2k+1/2, the bound is
\[
 M_s=\frac{269}{50}+34\sum_{k<300}\frac1{\beta_k}
 +\frac83\,257^2[(1201/2)^{-3}+\tfrac14(1201/2)^{-2}]
 +6+\frac1{10}<200.                                \tag{SE11.9}
\]
For the initial Gamma summands use 34/beta_k; in the remaining
tail beta_k>2*257. Prime cosines contribute less than 6 since their
imaginary arguments are below 1/2. Also |v_n v_m|<2 and pi>3.
Thus M=256 bounds the analytic matrix integrands. The inherited
Chebyshev quadrature argument gives
\[
 \epsilon_Q=4\cdot256\cdot256\frac{4^{-48}}{1-1/4},
 \qquad116\epsilon_Q<5.118\cdot10^{-22}.             \tag{SE11.10}
\]

The first discarded odd order is n=233. The complete Fourier and
pole vector tails are bounded by
\[
 a_f=\frac{128^{233}/465!!}{1-128^2/(467\cdot469)},
 \qquad
 a_h=\frac{4(C/4)^{233}/465!!}{1-(C/4)^2/(467\cdot469)}.
                                                        \tag{SE11.11}
\]
These are the same Rodrigues/factorial bounds used earlier. For the
same head projection, use the sufficient head norm bound sqrt(116)<12
and pole norm below one. Then
\[
 D\succeq(b-\tau_D)I,\quad\|B_{\rm mix}\|\le\tau_B,
 \quad\tau_D=\frac{256^2}{3}a_f^2+2a_h^2<10^{-48},
 \quad\tau_B=\frac{256^2\cdot12}{3}a_f+2a_h<10^{-24}.
                                                        \tag{SE11.12}
\]
Numerically tau_B is below 5.477e-25. No mixed block or infinite
complement is discarded without a bound.

## 5. Executed full-source and native observer bounds

The [rational candidate](../../../proof_lab/ENDPOINT_PRECISION_FRONTIER_MATRIX.json)
has the following distinct error contributions:
\[
 \begin{split}
 E_{\rm nodes}&<2.959\cdot10^{-22},\\
 E_{\rm pole/archive}&<1.095\cdot10^{-39},\\
 \|A-A_{\rm candidate}\|&<8.077\cdot10^{-22}.
 \end{split}                                       \tag{SE11.13}
\]
The last line also includes (SE11.10). Interval LDL certifies all
116 pivots of A_candidate-6*10^(-15)I. Thus
\[
 A\succeq5\cdot10^{-15}I,\qquad
 K_{C,256}\succeq
 [\min(5\cdot10^{-15},b-\tau_D)-\tau_B]I
 \succ4\cdot10^{-15}I.                             \tag{SE11.14}
\]
The [result](../../../proof_lab/ENDPOINT_PRECISION_FRONTIER_RESULT.json)
records every pivot and error. Its matrix SHA-256 is
b16fb99b197b4a6afa3f17bc37bad206eec4940186b5670e2607145fe361924f.
This certifies every complex odd state, rather than just the retained
Galerkin modes.

At physical radius A=4/5, the exact budgets give
\[
 e^{3A}<45/4,\quad 2m_\Gamma<11,\quad p_A<59/20,
 \quad2(\sinh A-A)\le\frac{A^3}{3(1-A^2/20)}<1/5.
                                                        \tag{SE11.15}
\]
SE6's graph return and (SE11.14) imply
\[
 \|f\|_X^2\le s[f]+\frac{132}{5}\|Rf\|_2^2
                  \le6600000000000001\,s[f].         \tag{SE11.16}
\]
With N_*<=11I/2 this gives
\[
 \|\mathcal L_*f\|^2\le
 \left(1-\frac2{72600000000000011}\right)\|A_*f\|^2,
 \qquad f\in X_{4/5}.                              \tag{SE11.17}
\]
The exact local observer A_*f->L_*f and its zero extension therefore
exist as in SE9. Its restrictions to nested smaller event ranges
agree on shared vectors. Smaller-aperture SE7--SE10 bounds remain
valid; these sufficient constants are not measurements of the true
lower source edge.

## 6. A fixed cutoff really fails before the next prime

Take c_*=8047/5000=1.6094, so log4<c_*<log5. The physical radius
is 8047/10000=0.8047. Let a be the exact 32-entry rational decimal
vector in the [witness replay](../../../proof_lab/endpoint_cutoff_obstruction.py),
and g_a=sum a_j phi_(2j+1). No accuracy of its original floating-point
eigensolver is assumed: any rational vector is a legitimate trial.
The exact norm satisfies 0.99<||g_a||^2<1.01. A supported polynomial
has O(1/|t|) Fourier decay, so this trial belongs to the full form
domain identified in SE10.

The scalar reading is enclosed directly, not inferred from a
floating-point spectrum. Use 256 width-one panels, Gauss-24, rho=2.
The ellipse has semimajor 5/8 and semiminor 3/8; hence
|Im(t/c_*)|<1/4. Replacing 34 by 10 and the prime bound 6 by 9 in
(SE11.9) gives a symbol bound below 100, even with dormant prime 5
included. Since |g_a-hat(z)|^2<=||g_a||^2 exp(|Im z|)<4,
M=256 bounds both scalar integrands after division by pi. Each
reading has quadrature remainder at most
\[
 \epsilon_* =4\cdot256\cdot256\frac{2^{-48}}{1-1/2}.
                                                        \tag{SE11.18}
\]
All node, special-function and pole intervals are additional errors.
The [executed witness](../../../proof_lab/ENDPOINT_CUTOFF_OBSTRUCTION_RESULT.json)
proves
\[
 \boxed{\frac{\langle g_a,K_{c_*,256}g_a\rangle}
                    {\|g_a\|^2}<-\frac3{100000}.}   \tag{SE11.19}
\]
Equation (SE11.4) still makes this K a valid lower comparison. Its
negative sign is therefore a genuine limitation of this particular
minorant, not a false tail envelope. Every head space containing
these 32 modes has the same negative Rayleigh witness. Enlarging
that head or tightening arithmetic cannot make K positive. The
fixed-catalogue continuity of SE9 and (SE11.14), (SE11.19) also show
that this comparison loses its positive lower edge somewhere between
c=8/5 and c=c_*. No exact first-loss location is asserted.

## 7. The cancellation lost by a finite-band observer

At c_* the shift a_5=log5/c_* exceeds one, so support gives
\[
 \int\cos(a_5t)|\widehat g(t)|^2\frac{dt}{2\pi}=0,
 \qquad g\in H.                                    \tag{SE11.20}
\]
Thus adding the dormant prime to the complete source changes nothing.
It does change its capped finite-band reading. If w_5=2log5/sqrt5
and tilde K denotes the same formula (SE11.3) with that extra cosine,
polarization of the support identity gives the operator equality
\[
 \widetilde K-K
 =-w_5F_T^*M_{\cos(a_5t)}F_T
 =w_5F_{|t|>T}^*M_{\cos(a_5t)}F_{|t|>T}.             \tag{SE11.21}
\]
This is SE9's existing full-versus-band support distinction made
explicit on the present obstruction. The same interval witness gives
\[
 \langle g_a,\widetilde K g_a\rangle>10^{-4},        \tag{SE11.22}
\]
while its original reading is negative. Only this one modified
reading is certified positive. The larger catalogue's tail condition
Psi>=b at T=256 is not certified, and tilde K is not promoted to a
valid positive full-source minorant. Neither changing the catalogue
nor ignoring its tail is an automatic repair.

The observer metaphor is precise here: the full source sees a
cancellation between the retained band and its complement. The capped
observer replaces the complement by a scalar and can lose that
cancellation. This is why better decimal accuracy alone is insufficient
at the witnessed scale. The next source-preserving routes are a larger
frequency band, or a different comparison with its own proved tail.

Prime 5, cofinal all-scale source signs, the global eta=0 sign,
historical five-label closure, K0 and RH remain open. No uniform
strict global observer reserve is asserted; SE4's escape obstruction
still applies. No proof-assistant verification or external review is
claimed. See [sources](SE11_SOURCE_RECORD.md), [audit](SE11_SCOPE.md)
and [pins](SE11_SOURCE_PINS.json).
