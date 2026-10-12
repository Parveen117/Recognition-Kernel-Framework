# SE40: cyclic source observer and analytic memory

12 October 2026 (UTC). Owner: Monty.

Written mathematics with exact finite controls. This develops the
quantitative observation machinery needed after SE39. It constructs a
bounded action on the actual native carrier, proves that one seed and
its action tower are dense, compresses the tower's mixed source readings
to a Hankel sequence, and bounds analytic truncation and calibration
transport. These results do not establish that the sequence is positive.
The inherited global eta bound is unchanged.

## 1. Existing carrier and the missing analytic contract

Typed cuts, derived iota, lawful composition, targets and Smriti precede
the admitted T35/T40 representation. Keep SE5/SE21's odd carrier X and
the unchanged bounded source S_b, with s(f,g)=<f,S_b g>_X. Write

\[
 a=3/2,\quad Rf=e^{-a|x|}f,\quad
 \|f\|_X^2=\|f\|_2^2+
 \int_{\mathbb R}(1+|G(\xi)|)|\widehat{Rf}(\xi)|^2\frac{d\xi}{2\pi}.
 \tag{SE40.1}
\]

Here G(xi)=Re psi(1/4+iota xi/2)-log pi, with the inherited positive
Fourier exponent. The half-line h(x)=sqrt(2)f(x), x>0, carries the
transported X norm; it is not supplied with a replacement primitive norm.

For a real calibration tau>a^2 set b=sqrt(tau), d_tau=tau-a^2 and

\[
 v_\tau(x)=\operatorname{sgn}(x)e^{-(b-a)|x|}/\sqrt2,
 \qquad \widehat{Rv_\tau}(\xi)=\frac{\sqrt2\,\iota\xi}{\tau+\xi^2}.
 \tag{SE40.2}
\]

SE21 proves v_tau in X and

\[
 s(v_t,v_u)=2\Phi[t,u],\qquad
 \Phi(t)=\sqrt t\,\xi'(1/2+\sqrt t)/\xi(1/2+\sqrt t).
 \tag{SE40.3}
\]

Calibrations used for Hermitian readings are real. Complex evaluation
below means the analytic continuation of the state or response series;
it does not assert the same Hermitian identity at a complex anchor.
In the displayed disks, v_t uses the square root with Re sqrt(t)>a.

N08 and WC2--WC4 already give geometric inverse and response bounds in
their declared complete algebras. They do not by themselves put an
arbitrary source action in those algebras. The construction below proves
the actual action bound on X; it does not assume R has a bounded inverse
or that this operator belongs to the mass-summable algebra N07. Its
complete operator algebra is the admitted bounded-operator algebra on X.

## 2. Theorem 1: a bounded native action with movable calibration

There is a bounded operator A_tau on X such that

\[
 \widehat{RA_\tau f}(\xi)=\frac{\widehat{Rf}(\xi)}{\tau+\xi^2},
 \qquad \boxed{\|A_\tau\|_{X\to X}\le d_\tau^{-1}.}
 \tag{SE40.4}
\]

Its explicit half-line action is

\[
 (A_\tau h)(x)=\int_0^\infty K_\tau(x,y)h(y)dy,
 \quad K_\tau(x,y)=\frac{e^{a(x-y)}}{2b}
       \left(e^{-b|x-y|}-e^{-b(x+y)}\right).
 \tag{SE40.5}
\]

For any sigma,tau>a^2, delta=sigma-tau,

\[
 \begin{split}
 A_\tau-A_\sigma&=\delta A_\tau A_\sigma,\qquad
 A_\tau A_\sigma=A_\sigma A_\tau,\\
 (I+\delta A_\tau)^{-1}&=I-\delta A_\sigma,\\
 A_\sigma&=A_\tau(I+\delta A_\tau)^{-1},\qquad
 v_\sigma=(I+\delta A_\tau)^{-1}v_\tau.
 \end{split}
 \tag{SE40.6}
\]

These identities hold on the whole X and do not assume a source sign.

**Proof.** K_tau is nonnegative. Direct integration on the two sides
of x=y gives

\[
 \int_0^\infty K_\tau(x,y)dy
     =\frac{1-e^{-(b-a)x}}{d_\tau},\qquad
 \int_0^\infty K_\tau(x,y)dx
     =\frac{1-e^{-(b+a)y}}{d_\tau}.
 \tag{SE40.7}
\]

Both are bounded by 1/d_tau. Cauchy--Schwarz against the nonnegative
kernel followed by integration therefore gives its L2 bound 1/d_tau.
Multiplying by e^(-ax) turns (SE40.5) into the odd Green kernel of
tau-partial_x^2. Fourier transformation on the faithful odd lift gives
the first identity in (SE40.4), first on a smooth core and then in L2.
The weighted Fourier part of the X norm is multiplied by at most 1/tau,
which is smaller than 1/d_tau. The two norm components prove (SE40.4)
and show that the output lies in the same X. No unbounded inverse of R
has been used as an operator-norm argument.

The scalar multiplier identity for two different tau values proves the
first line of (SE40.6); R is injective. Multiplying the two bounded
operators I+delta A_tau and I-delta A_sigma gives the identity in both
orders. The formulas for A_sigma and v_sigma follow from the same
Fourier multipliers. QED.

The reflected term e^(-b(x+y)) is essential: it is the odd-kernel
boundary term. This is an observation action, not a deletion of the
source's separate full pole term F or a change of boundary label.

## 3. Theorem 2: one cyclic tower covers the full source carrier

Define

\[
 \chi_n^{(\tau)}=A_\tau^n v_\tau\quad(n\ge0).
 \tag{SE40.8}
\]

These states are linearly independent and their finite spans have
dense union in X. Locally in |delta|<d_tau,

\[
 v_{\tau+\delta}=\sum_{n\ge0}(-\delta)^n\chi_n^{(\tau)},\quad
 \chi_n^{(\tau)}=\frac{(-1)^n}{n!}\partial_\tau^n v_\tau,\quad
 \|\chi_n^{(\tau)}\|_X\le d_\tau^{-n}\|v_\tau\|_X.
 \tag{SE40.9}
\]

The derivative is a derivative in the X norm. The tower's Fourier
reading and its polynomial half-line realization are explicit:

\[
 \widehat{R\chi_n^{(\tau)}}(\xi)
   =\frac{\sqrt2\,\iota\xi}{(\tau+\xi^2)^{n+1}},\qquad
 h_n(x)=e^{-(b-a)x}p_n(x),
 \tag{SE40.10}
\]

where p_0=1 and, for n>=1, the unique polynomial solution is

\[
 2b p_n'-p_n''=p_{n-1},\qquad p_n(0)=0.
 \tag{SE40.11}
\]

In particular p_1=x/(2b) and p_2=x^2/(8b^2)+x/(8b^3).

**Proof.** For |delta|/d_tau<1, finite geometric multiplication and
the operator bound give the norm-convergent inverse in (SE40.6),
including termwise norm derivatives. This proves (SE40.9)--(SE40.10).
Conjugating the Green equation gives (SE40.11). Its coefficients are
solved downward from the leading degree n to the constant derivative;
the boundary fixes the remaining constant. Equivalently it is the
unique polynomial-exponential Dirichlet solution decaying after R.

A finite relation between the chi_n, after Fourier transformation and
division by xi away from zero, would be a polynomial identity in
(tau+xi^2)^(-1) on an interval. Its coefficients vanish. Thus no
finite tower direction is redundant as a state.

For density, let Y be the closed linear span of this tower. It is
invariant under A_tau. A sufficiently small real change of calibration
uses norm-convergent series in A_tau, so (SE40.6) shows that Y contains
v_sigma and is invariant under A_sigma. Repeat along a compact interval
of calibrations above a^2. The lower bound on d_sigma there is positive,
so finitely many sufficiently small steps reach any prescribed sigma.
Consequently Y contains every v_sigma, sigma>a^2, including every
integer-rate f_j of SE21. Those have dense span in X. Hence Y=X. QED.

The calibration is movable. The theorem does not fix a privileged
physical observer, discard later readings, or assume an invariant
positive pairing for the source.

## 4. Theorem 3: Hankel decoding and source-symmetric action

For k>=0 define the complete-source coefficients

\[
 \mu_k(\tau)=\frac{(-1)^k}{(k+1)!}\Phi^{(k+1)}(\tau).
 \tag{SE40.12}
\]

They determine every mixed reading of the tower:

\[
 \boxed{s(\chi_i^{(\tau)},\chi_j^{(\tau)})=2\mu_{i+j}(\tau).}
 \tag{SE40.13}
\]

Thus the N-dimensional tower Gram uses 2N-1 scalar coefficients, not
N^2 independently acquired entries. This statement concerns this
structured tower, not arbitrary N-dimensional observation banks.
Moreover,

\[
 \boxed{A_\tau^\dagger S_b=S_bA_\tau.}
 \tag{SE40.14}
\]

The dagger here is the existing X-adjoint. Neither S_b>=0 nor ordinary
self-adjointness of A_tau is asserted by (SE40.14).

**Proof.** Expand the two locally convergent state series in
(SE40.3). If Phi(tau+z)=sum_k c_k z^k, its divided difference has
coefficient c_(i+j+1) at z^i w^j. Comparing the two real-variable
series and then complex-polarizing gives (SE40.13), including its
factor two, factorial and alternating sign. Boundedness justifies
coefficient comparison. Shifting either tower index once gives the
same coefficient. This proves s(A_tau x,y)=s(x,A_tau y) on the
tower span; density and boundedness extend it to all X. QED.

Put C_tau=d_tau A_tau, zeta_n=C_tau^n v_tau and
nu_k=d_tau^k mu_k. Then ||C_tau||<=1 and the normalized Gram is
2(nu_(i+j)). The change from chi_n to zeta_n is a positive diagonal
congruence. It removes the known geometric basis scaling without
changing inertia or creating a positive native spectral floor.

Combining density with SE39 gives the exact criterion

\[
 \mathrm{RH}\ \Longleftrightarrow\ S_b\succeq0
 \Longleftrightarrow
 (\mu_{i+j}(\tau))_{i,j=0}^{N-1}\succeq0\quad\hbox{for every }N.
 \tag{SE40.15}
\]

The actual complete-source positivity is still the missing assertion.
There is no finite acceptance rule in this equivalence.

## 5. Theorem 4: quantitative analytic and measurement tails

Let M_tau be any upper bound for ||v_tau||_X and C_s for ||S_b||.
For |delta|<d_tau put q=|delta|/d_tau. The retained state
p_N(delta)=sum_(n=0)^(N-1)(-delta)^n chi_n satisfies

\[
 \boxed{\|v_{\tau+\delta}-p_N(\delta)\|_X
     \le\frac{M_\tau q^N}{1-q}.}
 \tag{SE40.16}
\]

For real delta,epsilon in this disk, q=|delta|/d_tau and
r=|epsilon|/d_tau, its fully decoded mixed reading obeys

\[
 \left|s(v_{\tau+\delta},v_{\tau+\epsilon})
      -2\sum_{i,j<N}(-\delta)^i(-\epsilon)^j\mu_{i+j}(\tau)\right|
 \le C_s M_\tau^2\frac{q^N+r^N}{(1-q)(1-r)}.
 \tag{SE40.17}
\]

For a finite complex combination f=sum_l c_l v_(tau+delta_l), define

\[
 B=\sum_l\frac{|c_l|}{1-q_l},\qquad
 B_N=\sum_l\frac{|c_l|q_l^N}{1-q_l},\qquad
 f_N=\sum_l c_l p_N(\delta_l).
\]

Then

\[
 \|f-f_N\|_X\le M_\tau B_N,\qquad
 |s[f]-s[f_N]|\le2C_sM_\tau^2 B B_N.
 \tag{SE40.18}
\]

If the measured or enclosed coefficients have errors at most e_k,
an additional explicit error on a tower state sum_(i<N) c_i chi_i is

\[
 \left|2\sum_{i,j<N}\overline{c_i}c_j
            (\widetilde\mu_{i+j}-\mu_{i+j})\right|
       \le2\sum_{i,j<N}|c_i||c_j|e_{i+j}.
 \tag{SE40.19}
\]

**Proof.** Sum the geometric norm bound in (SE40.9). Each full or
retained probe has norm at most M_tau/(1-q). Subtract a mixed form
by replacing its two arguments in turn; use boundedness of S_b.
The same estimate for finite linear combinations gives (SE40.18).
The triangle inequality on the finite quadratic form gives (SE40.19).
All cross terms are retained. QED.

These are estimates for specified analytic probes and their supplied
coefficient budgets. B is not bounded uniformly by ||f||_X in this
argument. Hence they are not uniform finite-rank approximation of the
identity on the X unit ball, and their errors are not the spectral
shift eta. A finite-dimensional subspace still has unit vectors in
its native orthogonal complement.

## 6. Theorem 5: actual rational budgets and calibration-memory transport

The actual source and the convenient calibration tau_0=25/4 satisfy

\[
 \|S_b\|<43/12,\qquad \|v_{25/4}\|_X<2,\qquad
 \|A_{25/4}\|\le1/4,\qquad
 |\mu_k(25/4)|\le(43/6)4^{-k}.
 \tag{SE40.20}
\]

In particular, for real |delta|,|epsilon|<=1 the right side of
(SE40.17) is at most

\[
 \boxed{\frac{1376}{27}\,4^{-N}.}
 \tag{SE40.21}
\]

The complete coefficient memory moves with calibration. Whenever
|delta|<d_tau,

\[
 \chi_n^{(\tau+\delta)}
     =\sum_{l\ge0}(-\delta)^l\binom{n+l}{l}\chi_{n+l}^{(\tau)},
 \qquad
 \mu_k(\tau+\delta)
     =\sum_{l\ge0}(-\delta)^l\binom{k+l+1}{l}\mu_{k+l}(\tau).
 \tag{SE40.22}
\]

Both series converge in their stated norms. If q=|delta|/d_tau<1,
L>=1 and theta=q(k+L+2)/(L+1)<1, the second series truncated before
l=L has an absolute remainder at most

\[
 \frac{C_sM_\tau^2}{2}\,d_\tau^{-k}
 \binom{k+L+1}{L}\frac{q^L}{1-\theta}.
 \tag{SE40.23}
\]

**Proof of the source bound.** The Gamma form has absolute value at
most the graph part of (SE40.1). SE4/SE5's complete Hardy prime
pullback has norm at most 2m_p, where m_p=sum_(n>=2)Lambda(n)/n^2<5/4
(SE4.6). On the faithful half-line the full pole is
|integral (e^(-x)-e^(-2x))h(x)dx|^2. Its squared row norm is
1/2-2/3+1/4=1/12. Thus ||S_b||<=1+2m_p+1/12<43/12.

**Proof of the seed bound.** SE5's complete digamma series, with
u=xi/2 and s_j=j+1/4, gives

\[
 |G(\xi)|\le m_\Gamma+4+\tfrac12\log(1+4\xi^2).
 \tag{SE40.24}
\]

Indeed its j=0 increment is at most 4. For j>=1, the positive
decreasing function u^2/[s(s^2+u^2)] is bounded in sum by its
integral from 1/4 to infinity, which is the logarithmic term.
The constant m_Gamma=gamma+pi/2+3log2+log pi is less than 8.

For b>0 elementary rational integration gives

\[
 \int\frac{2\xi^2}{(b^2+\xi^2)^2}\,d\mu=\frac1{2b},\qquad
 \int\frac{\xi^2\log(1+4\xi^2)}{(b^2+\xi^2)^2}\,d\mu
   =\frac{\log(2b+1)}{2b}+\frac1{2b+1}.
 \tag{SE40.25}
\]

For completeness, start with
J(b,c)=integral log(xi^2+c^2)/(xi^2+b^2) dmu.
Differentiation in c reduces to partial fractions and gives
partial_c J=1/[b(b+c)]. The c->infinity constant fixes
J=log(b+c)/b. Substitute c=1/2 and the constant log4 to obtain
integral log(1+4xi^2)/(xi^2+b^2) dmu=log(2b+1)/b.
Applying 1+(b/2)partial_b proves the second integral in (SE40.25).
The integrands and their derivatives are integrable, so these steps
are justified by domination on compact positive b,c intervals.

Consequently

\[
 \|v_\tau\|_X^2\le
 \frac1{2(b-a)}+
 \frac{5+m_\Gamma+\log(2b+1)}{2b}+\frac1{2b+1}.
 \tag{SE40.26}
\]

At b=5/2, log6<2 gives the bound 1/2+3+1/6=11/3<4.
The remaining operator bound follows from Theorem 1, and
2|mu_k|=|s(v_tau,A_tau^k v_tau)|<=C_s M_tau^2 d_tau^(-k).
Substitution in (SE40.17) proves (SE40.21).

**Proof of memory transport.** The two transport formulas in (SE40.6)
give chi_n^(tau+delta)=A_tau^n(I+delta A_tau)^(-n-1)v_tau.
The negative-binomial series gives the first formula of (SE40.22).
Differentiating the scalar Taylor series in (SE40.12) gives the second;
the extra +1 in its binomial coefficient is essential. Its absolute
lth term is bounded by (C_s M_tau^2/2)d_tau^(-k)
binom(k+l+1,l)q^l. For l>=L the ratio of consecutive majorant terms
is at most theta. Summing gives (SE40.23). QED.

One may now explicitly evaluate the formal unit series
sum_(n>=0)(-Lambda)^n C_tau^n v_tau at an admitted scalar lambda_cal
with |lambda_cal|<1. It converges to v_(tau+d_tau lambda_cal), with
the displayed tail. Its typed coefficient cut retains v_tau. This is
a proved analytic adapter for this supplied action; it is not numerical
convergence of every formal unit series in SE38. Neither Lambda nor
lambda_cal is identified with the spectral shift eta.

## 7. Controls, boundary and the next mathematical target

The [Python 3.12 replay](../../../proof_lab/endpoint_cyclic_observer_controls.py)
and [recorded readings](../../../proof_lab/ENDPOINT_CYCLIC_OBSERVER_CONTROLS.json)
exercise the actual polynomial state recurrence and its independent
rational Fourier integrals. Supplied rational response models test
Hankel decoding, normalized congruence, moving calibration, geometric
remainders, uncertainty budgets and source-symmetry without positivity.
These finite controls do not prove an infinite source sign.

For example, C=diag(1/2,1/3), J=diag(1,-1), v=(1,1) has ||C||<1
and C^dagger J=JC. Nevertheless the first two cyclic moments give

\[
 \begin{pmatrix}0&1/6\\1/6&5/36\end{pmatrix},\qquad
 \det=-1/36.
 \tag{SE40.27}
\]

Contractive generation, exact memory and source-symmetry therefore do
not imply source positivity. This is a supplied model, not a negative
reading for the actual arithmetic source.

The new capability is a complete, bounded, movable observation action
on the actual X, with mixed readings and quantitative analytic tails.
The next needed result is a positivity-preserving law for the actual
Hankel sequence, or a global comparison controlling its unobserved
directions. That law must retain the complete arithmetic response;
it cannot be supplied by assuming RH's zero support or by a generic
contraction argument. SE27's global eta=1079/2000, floor 1/492000 and
SE21's V_16 eta-zero result remain unchanged.

See [scope](SE40_SCOPE.md) and [source record](SE40_SOURCE_RECORD.md).
