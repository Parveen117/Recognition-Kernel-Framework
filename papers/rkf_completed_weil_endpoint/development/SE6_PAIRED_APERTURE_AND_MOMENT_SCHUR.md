# SE6: Paired prime-boundary apertures and a certified moment complement

11 October 2026. Owner: Monty Dabas.

This stage closes the critical observer inequality on one explicit
small aperture of the corrected SE4 source. On a larger aperture where
the prime 2 is active, it proves a positive floor on the infinite
complement of fifteen native moment readings. The remaining sign there
is an exact fifteen-dimensional Schur matrix, which is not evaluated
in this packet.

Small-support positivity and positive finite-codimensional complements
have established Yoshida--Suzuki lineage. The contribution here is an
explicit rational calibration, its native observer attachment, and
prime/boundary bookkeeping for the source already fixed in SE4--SE5.
This is not a new general Weil criterion or the historical five-label
Feshbach construction.

## 1. Source and aperture

Retain the typed source/target order, native metric and admitted T35
representation of [SE5](SE5_STABLE_OBSERVER_AND_COMPACT_DEFECT.md).
No Hilbert representation is made primitive. Set a=3/2, m=exp(-a|x|),
g=Rf=mf, and use the positive-exponent Fourier transform and
dmu=dxi/(2pi). The full odd one-boundary form is
\[
 s[f]=\int G(\xi)|\widehat g(\xi)|^2d\mu
      -2\Re\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                              \langle g,T_{\log n}g\rangle
      -2\left|\int g(x)e^{-x/2}\,dx\right|^2 .
                                                        \tag{SE6.1}
\]
Here G=Re psi(1/4+i xi/2)-log pi, g_0=G+m_Gamma, and
\[
 \|f\|_X^2=\|f\|_2^2+\|Cf\|^2,\quad
 \|Cf\|^2=\int(1+|G|)|\widehat g|^2d\mu,\quad
 N_*=A_*^\dagger A_*,\quad
 S=N_*-\mathcal L_*^\dagger\mathcal L_* .
\]
The target L_* includes both SE4 debts and the actual odd boundary.
All operators and adjoints retain this native metric.

For A>0, let X_A be the X-closure of the odd logarithmic test core with
g supported in (-A,A). It is a closed native subspace. Its elements
have that support up to null sets. All inequalities below extend to
X_A by continuity. A denotes the aperture radius, not the mismatch
analysis A_*.

## 2. Prime response and completion must share the aperture

Define the self-adjoint native translation response
\[
 \mathcal T_t=R^\dagger(T_t+T_{-t})R,\qquad t\ge0.
\]
Since m(x)m(x-t)<=exp(-at) and the inclusion X->L2 has norm at most one,
\[
 \|\mathcal T_t\|\le2e^{-at}.                         \tag{SE6.2}
\]
If F_b is the full odd boundary Gram, then on X
\[
 \boxed{F_b=-\int_0^\infty
                       2\cosh(t/2)\mathcal T_t\,dt.} \tag{SE6.3}
\]
This is a norm-convergent operator integral, understood first on the
core and then extended. Norm continuity of the integrand follows from
compactness of R and strong continuity of translations.

Proof of the identity. For odd g, the autocorrelation
q(t)=<g,T_t g> is real and even, including for complex-valued g.
Its bilateral Laplace transform at 1/2 is
\[
 \int_{\mathbb R}e^{t/2}q(t)\,dt
  =\left(\int g(x)e^{x/2}dx\right)
       \overline{\left(\int g(x)e^{-x/2}dx\right)}
  =-\left|\int g(x)e^{-x/2}dx\right|^2.
\]
Evenness of q gives (SE6.3) as a quadratic-form identity; polarization
gives the operator identity. The integral converges by (SE6.2), since
a>1/2. This does not make each integrand positive.

Write P for the full prime cross-operator from SE5. Its combined
prime/boundary contribution is
\[
 \boxed{Z:=P+F_b=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\mathcal T_{\log n}
 -\int_0^\infty2\cosh(t/2)\mathcal T_t\,dt.}           \tag{SE6.4}
\]
Thus the poles and prime events are subtracted at the same translation
distance. The signed pairing is retained, not estimated as two
independent positive losses.

For an integer M>=2, truncate both terms at L=log M, obtaining Z_M.
Using SE5's complete prime tail and integrating (SE6.2),
\[
 \boxed{\|Z-Z_M\|\le
 \frac{2(\log M+1)}{M}+\frac2M+\frac1{M^2}.}         \tag{SE6.5}
\]
This is a conservative absolute bound; cancellation can improve it.
It is not a uniform zero-threshold relative bound.

On X_A all pairings with |t|>2A vanish. Consequently the compression
of Z_M equals that of Z exactly whenever log M>=2A. There is then no
omitted prime or boundary tail in this aperture. The Gamma continuum
still requires control. This exact support rule is used below.

## 3. Why a fixed prime cutoff with the full boundary cannot work globally

Let phi be a nonzero, real, even, nonnegative smooth bump supported in
[-ell,ell], normalized in L2, and choose r>ell. Put
\[
 g_r(x)=\frac{\phi(x-r)-\phi(x+r)}{\sqrt2},\qquad
 f_r=m^{-1}g_r,\qquad I_\phi=\int\phi(x)e^{x/2}dx>0.
\]
These are admissible odd core states. Their boundary Gram is exactly
\[
 F_b[f_r]=I_\phi^2(e^r+e^{-r}-2).                    \tag{SE6.6}
\]
Meanwhile
|hat g_r|^2=(1-cos(2r xi))|hat phi|^2<=2|hat phi|^2.
For every fixed M, both the Gamma form and the prime sum restricted
to n<=M are bounded in absolute value by a constant independent of r.
Thus
\[
 \int G|\widehat g_r|^2d\mu-P_M[f_r]-F_b[f_r]
                    \longrightarrow-\infty.          \tag{SE6.7}
\]
Every such unpaired truncated model has a negative state. This is
not a negative state for the all-prime form (SE6.1).

There is also no finite K with F_b<=K C^\dagger C on the full odd
carrier: the denominator ||Cf_r||^2 is uniformly bounded, whereas
(SE6.6) diverges. Joint prime/boundary control is therefore essential.

More explicitly, if k(t)=<phi,T_t phi> and r>2ell, then
q_r(t)=k(t)-k(t-2r)/2 for t>=0. Define
\[
 \begin{aligned}
 \gamma_\phi&=\int G|\widehat\phi|^2d\mu,\qquad
 c_\phi(r)=\int G|\widehat\phi|^2\cos(2r\xi)d\mu,\\
 d_\phi&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}k(\log n)-I_\phi^2,\\
 \Delta_\phi(r)&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                              k(\log n-2r)
                          -I_\phi^2(e^r+e^{-r}).
 \end{aligned}
\]
All sums here are finite by support. Direct substitution gives
\[
 \boxed{s[f_r]=\gamma_\phi-c_\phi(r)-2d_\phi
                                      +\Delta_\phi(r).} \tag{SE6.8}
\]
The moving prime window is
exp(2r-2ell)<=n<=exp(2r+2ell). Its pole-subtracted response, not a
fixed initial prime list, must balance the boundary. This identifies
an actual family of necessary sign tests without asserting they suffice
for every odd state.

## 4. Quantitative moment blindness at an arbitrary finite aperture

Suppose g is supported in [-A,A] and
\[
 \int x^k g(x)dx=0\qquad(0\le k<d),\quad d\ge1.
\]
Subtract the first d terms of exp(i xi x), apply its real-axis
Taylor remainder and Cauchy--Schwarz, and integrate over |xi|<=T:
\[
 \boxed{\int_{|\xi|\le T}|\widehat g|^2d\mu
 \le\alpha(A,T,d)\|g\|_2^2,\qquad
 \alpha(A,T,d)=
 \frac{2(AT)^{2d+1}}{\pi(2d+1)^2(d!)^2}.}           \tag{SE6.9}
\]
This controls the whole low-frequency mass, not selected Fourier samples.
For odd g the even moments vanish automatically.

Suppose m_Gamma<=m_0, G(T)>=b>0, and let
\[
 p_A=2\sum_{2\le n\le e^{2A}}\frac{\Lambda(n)}{\sqrt n},
 \qquad \beta_A=2(\sinh A-A).
\]
Monotonicity of G in |xi| and G>=-m_0 yield
\[
 \int G|\widehat g|^2d\mu
 \ge[b-(b+m_0)\alpha]\|g\|_2^2.
\]
The prime form has absolute value at most p_A||g||_2^2.
The odd boundary functional is represented on this interval by
sqrt(2)sinh(x/2), whose squared norm is beta_A. Therefore
\[
 \boxed{s[f]\ge q\|g\|_2^2,\quad
 q=b-(b+m_0)\alpha-p_A-\beta_A.}                    \tag{SE6.10}
\]
If q>0, this becomes a native lower bound:
\[
 \boxed{s[f]\ge\sigma\|f\|_X^2,\quad
 \sigma=\frac{q}{q+e^{3A}+1+2m_0+p_A+\beta_A}.}     \tag{SE6.11}
\]
To prove it, use ||f||_2^2<=e^{3A}||g||_2^2 and
||Cf||^2<=s[f]+(1+2m_0+p_A+beta_A)||g||_2^2.
Upper and lower enclosures for the displayed constants can be used
in their adverse directions.

For every fixed A, p_A and beta_A are finite. Choose T so that b exceeds
their sum and then increase d: the factorial forces alpha to zero.
This constructively produces a positive finite-codimensional complement
on every finite aperture. It does not prove the sign of the removed
finite block, nor give one fixed number of moments for all A.

## 5. Exact scalar inputs

Only the following coarse bounds are needed:
\[
 m_\Gamma<11/2,\qquad G(16)>4/5,\qquad G(24)>6/5.
                                                        \tag{SE6.12}
\]
Here m_Gamma=gamma+pi/2+3 log 2+log pi.
For completeness, log 2 is larger than the first three positive terms
of 2 sum_{k>=0}(1/3)^{2k+1}/(2k+1), which exceeds 693/1000.
Then gamma<H_32-log 32<3/5. The exponential series gives log 2<7/10
and log pi<6/5, using pi<22/7. Thus
m_Gamma<3/5+11/7+21/10+6/5=383/70<11/2.

The positive digamma series retained from SE4 gives the exact lower sums
\[
 \begin{aligned}
 \sum_{k=0}^{127}\frac{64}{(k+1/4)((k+1/4)^2+64)}
       &>63/10,\\
 \sum_{k=0}^{127}\frac{144}{(k+1/4)((k+1/4)^2+144)}
       &>67/10.
 \end{aligned}                                       \tag{SE6.13}
\]
Subtracting 11/2 proves the two bounds for G. Every omitted Gamma
term is positive. These finite rational inequalities are replayed
exactly by the accompanying Python program; no floating-point
digamma evaluation or numerical quadrature is used.

The elementary bounds 3<pi<22/7, cosh(1/2)<4/3,
exp(3/2)<5 and exp(3/16)<2 are sufficient below. The latter two follow
from an exponential-series upper tail and a geometric-series bound,
respectively. The replay also checks the rational steps used for them.

## 6. A full aperture with a contractive exact observer

Take A=1/16, T=16 and d=1. Oddness supplies the sole moment condition.
There are no prime translations in the support because 2A<log 2.
Equation (SE6.9) gives alpha<2/27, and hence the Gamma form is at least
\[
 [4/5-(4/5+11/2)(2/27)]\|g\|_2^2
                  =\tfrac13\|g\|_2^2.
\]
Taylor's integral bound
2(sinh A-A)<=A^3 cosh(A)/3 and cosh(A)<2 give
beta_A<1/6144. Applying (SE6.10)--(SE6.11),
\[
 \boxed{s[f]\ge\frac{2047}{6144}\|g\|_2^2,\qquad
        s[f]\ge\frac{2047}{88064}\|f\|_X^2
            \quad(f\in X_{1/16}).}                  \tag{SE6.14}
\]
SE4 gives ||N_*||<=max(m_Gamma,4m_p)<11/2. Therefore
\[
 \boxed{\|\mathcal L_*f\|^2
 \le\left(1-\frac{2047}{484352}\right)\|A_*f\|^2
             \quad(f\in X_{1/16}).}                 \tag{SE6.15}
\]
Restricting A_* and L_* to this closed subspace and using SE5 constructs
an exact observer with squared norm at most 1-2047/484352.
This is an infinite-dimensional aperture theorem, not a finite matrix
sample. It does not conflict with SE4: the escaping full-carrier states
are outside every fixed aperture.

## 7. A prime-active aperture with fifteen observed moments

Now take A=1/2, T=24, d=30. The prime 2 is the only active prime power,
since 2<e<3. Its full cross-form cost obeys
p_A=2 log 2/sqrt(2)<1. Also beta_A<1/16.
The exact rational inequality
\[
 \frac{2\,12^{61}}{3\cdot61^2(30!)^2}<\frac1{500}
\]
bounds alpha because pi>3. With b=6/5 and m_0=11/2, this proves
\[
 q>\frac65-\frac{67}{10}\frac1{500}-1-\frac1{16}
   =\frac{1241}{10000}>\frac1{10}.
\]
Only these fifteen odd moments need to be observed:
\[
 (\mathcal Mf)_j=\int_{-1/2}^{1/2}x^{2j+1}Rf(x)\,dx,
                  \qquad j=0,\ldots,14.             \tag{SE6.16}
\]
They are bounded independent native functionals. Fifteen is a sufficient
count from this estimate, not a minimality assertion. Let Y=ker M in
X_{1/2}. On its infinite-dimensional carrier,
\[
 \boxed{s[f]\ge\frac1{10}\|g\|_2^2,\qquad
 s[f]\ge\frac8{1453}\|f\|_X^2,\qquad
 \|\mathcal L_*f\|^2
 \le\left(1-\frac{16}{15983}\right)\|A_*f\|^2.}
                                                        \tag{SE6.17}
\]
For the middle bound use exp(3/2)<5 and
q/(q+5+12+1+1/16) at q=1/10. The final bound again uses
||N_*||<11/2. Thus the observer restricted to this actual moment-blind
complement is a strict contraction with an explicit reserve.

The fifteen moment functionals are independent: a vanishing linear
combination on all odd smooth core states would force its odd
polynomial to vanish on the interval. Consequently
\[
 \Pi=\mathcal M^\dagger(\mathcal M\mathcal M^\dagger)^{-1}\mathcal M,
 \qquad Q=I-\Pi                                     \tag{SE6.18}
\]
are native orthogonal projections with rank Pi=15 and Ran Q=Y.
This supplies the actual complement through moment seeds, including
their native metric, rather than choosing an unexplained finite space.

## 8. The remaining exact finite matrix

Let S_A be the compression of the corrected completed operator to
X_{1/2}. Equation (SE6.17) proves
D_Q=(QS_AQ)|_Y >=(8/1453)I_Y. Hence its inverse exists with
norm at most 1453/8, without assuming the desired full sign.
Define on Ran Pi
\[
 \boxed{F_{15}=\Pi S_A\Pi
   -\Pi S_AQ\,D_Q^{-1}\,QS_A\Pi.}                   \tag{SE6.19}
\]
The native block completion of squares proves
\[
 \boxed{S_A\succeq0\ \Longleftrightarrow\ F_{15}\succeq0,\qquad
        N_-(S_A)=N_-(F_{15})\le15.}                 \tag{SE6.20}
\]
Indeed for x in Ran Pi and y in Y,
\[
 s[x+y]=\langle x,F_{15}x\rangle_X+
 \langle y+D_Q^{-1}QS_Ax,\,
           D_Q(y+D_Q^{-1}QS_Ax)\rangle_X .
\]
All mixed blocks are retained. Using an orthonormal basis of Ran Pi
or its exact native Gram gives a genuine 15 by 15 matrix.
The positive infinite block has now been certified for this aperture;
F_15 has not been computed or signed.

For an approximate complement solve D_Q y=r, a residual e=r-D_Q y
satisfies ||y-D_Q^{-1}r||_X<=(1453/8)||e||_X.
This removes an eta-dependent solve bound on this particular complement.
It does not provide uniform control as the physical aperture grows.

## 9. What is closed and what remains

The corrected observer is a certified contraction on X_{1/16}, and on
the fifteen-moment blind complement inside X_{1/2}. The latter aperture
includes the first prime event. Its complete odd sign is reduced to
F_15 with a proved positive pivot and an explicit solve-error constant.

The construction is an auxiliary aperture reduction, not an identification
of the historical five-label endpoint. Further work must enclose F_15,
then control enlargement of the aperture with all new prime events and
mixed responses. General finite-codimension existence from Section 4
does not certify the finite Schur blocks or the unbounded-aperture limit.
The full norm-one condition, K0 and RH remain open.

See the [exact arithmetic replay](../../../proof_lab/endpoint_paired_aperture_budget.py),
[recorded result](../../../proof_lab/ENDPOINT_PAIRED_APERTURE_RESULT.json),
[source record](SE6_SOURCE_RECORD.md), [pins](SE6_SOURCE_PINS.json)
and [verification scope](SE6_SCOPE.md).
