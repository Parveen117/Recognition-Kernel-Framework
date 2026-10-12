# SE16: signed return squares and a sharper global shift

12 October 2026. Owner: Monty.

The complete corrected complex odd source satisfies
\[
 S_b+\frac{69}{100}I_X\succeq\frac1{1845}I_X.
                                                               \tag{SE16.1}
\]
Thus the actual global negative count and nullity vanish at eta=0.69
and at every larger shift. The implied nonnegative shift is
25441/36900. This improves SE15's 326/369 certificate without adding
an uncomputed local-aperture hypothesis. The zero-shift sign remains
open, and the positive local aperture remains 21/25.

The mechanism is an exact signed return followed by a weighted square
identity. Opposite-half Gamma contributions cancel before a row bound
is taken. Every prime power remains present. The full-source proof
uses 44 enclosed spatial cells and a complete infinite-exterior bound;
it does not use sampled source eigenvalues.

## 1. Same native source and faithful odd observation

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede all representations. Work in the already admitted
T35/T40 adapter of SE4--SE15, with
\[
 m(x)=e^{-3|x|/2},\quad g=Rf=mf,\quad u=m^2,
 \quad\|f\|_X^2=\|f\|_2^2+\int(1+|G|)|\widehat g|^2d\mu,
 \quad d\mu=d\xi/(2\pi).                          \tag{SE16.2}
\]
The source is exactly the central Gamma form minus the paired prime
term P[f] and the full odd pole F[f] of SE15.2. Write
E_+[f]=integral G_+|g-hat|^2 dmu and m_Gamma=-G(0).
The unchanged enclosed constants give m_Gamma<g_c=269/50 and
\[
 F[f]\le b_c\int(1-u)|f|^2dx,\quad b_c=1/10,
 \qquad D_F[f]:=b_c\int(1-u)|f|^2dx-F[f]\ge0.      \tag{SE16.3}
\]

For an odd f, h(x)=sqrt(2)f(x), x>0, is a faithful L2 half-line
representation. Its missing half is fixed by f(-x)=-f(x); it is not
an arbitrary lossy measurement. Whenever the native source is used
in this chart, its graph pairing travels with the map. No equality
between the native norm and a bare half-line L2 norm is asserted.

## 2. Two Gamma modes with their opposite-half return

**Theorem (exact odd return kernel).** Put beta_k=2k+1/2. The SE5
digamma series gives
\[
 G(\xi)+m_\Gamma
 =\sum_{k\ge0}\frac{2\xi^2}{\beta_k(\beta_k^2+\xi^2)},
 \qquad\frac{2\xi^2}{\beta(\beta^2+\xi^2)}
       =\frac2\beta-\frac{2\beta}{\beta^2+\xi^2}.  \tag{SE16.4}
\]
Keep beta=1/2 and 5/2. The inverse Fourier kernel of
2 beta/(beta^2+xi^2) is exp(-beta|x-y|), by integrating the two
elementary exponential Fourier integrals. On the odd carrier its
weighted half-line kernel is
\[
 k_\beta^-(x,y)=m(x)m(y)
     \{e^{-\beta|x-y|}-e^{-\beta(x+y)}\},\quad x,y>0.
                                                               \tag{SE16.5}
\]
It is pointwise nonnegative. If K_beta^- is this integral operator,
then the full Gamma form obeys the exact identity
\[
 \int G|\widehat g|^2d\mu
 =(24/5-m_\Gamma)\|g\|_2^2
   -\sum_{\beta\in\{1/2,5/2\}}\langle h,K_\beta^-h\rangle
   +E_{\rm rem}[f],\qquad E_{\rm rem}\ge0.         \tag{SE16.6}
\]
Here E_rem is the complete integral of the nonnegative terms k>=2
in (SE16.4). It is finite on X. Proof: expand the four half-line
pieces of the full convolution pairing. The same-side pieces add,
and oddness makes the opposite-side pieces subtract, yielding
(SE16.5) with the sqrt(2) normalization. The two constants 2/beta
sum to 24/5. Monotone convergence handles the remaining modes. QED.

Replacing the difference in (SE16.5) by the sum loses a known signed
return. A later control proves that this loss invalidates the selected
comparison at eta=0.69. This does not mean the original source becomes
negative under a different faithful description.

## 3. Weighted observation defects are explicit squares

**Theorem (weighted row identity).** For a symmetric, nonnegative
kernel k and positive weight q, define
H(x)=q(x)^(-1) integral k(x,y)q(y)dy. Whenever the displayed forms
are finite, direct expansion gives, for complex h,
\[
 \int H|h|^2-\langle h,Kh\rangle
 =\frac12\iint k(x,y)q(x)q(y)
       \left|\frac{h(x)}{q(x)}-\frac{h(y)}{q(y)}\right|^2dxdy
 =:D_k[h]\ge0.                                    \tag{SE16.7}
\]
Proof. Expand the squared difference. Symmetry makes its two diagonal
integrals equal to integral H|h|^2; the two cross terms give the real
part of the kernel pairing. The latter is real for a symmetric real
kernel. Truncation and monotone convergence extend the identity from
compact bounded data whenever the diagonal integral is finite. QED.
This is the elementary weighted Schur mechanism, with its residual
retained; general weighted Schur testing is cited prior art.

For (SE16.5) choose q(x)=exp(-x/2). Splitting the integral at y=x
gives the exact row
\[
 H_\beta(x)=e^{-x}\frac{2\beta}{4-\beta^2}
                 (e^{-\beta x}-e^{-2x}).           \tag{SE16.8}
\]
Both beta values differ from 2. With z=exp(-x/2), their sum is
\[
 H(z)=\frac4{15}(z^3-z^6)+\frac{20}{9}(z^6-z^7),
 \qquad 0<z\le1.                                 \tag{SE16.9}
\]
The apparent negative denominator for beta=5/2 is paired with a
negative exponential difference; each actual row is nonnegative.
Let D_Gamma be the sum of the two nonnegative defects (SE16.7)
applied to h. This gives the Gamma lower potential while retaining
the exact positive remainder D_Gamma+E_rem.

**Theorem (complete prime row and return squares).** On the full line
use the even positive weight q(x)=exp(-|x|/2), and let a_n=Lambda(n)/sqrt(n),
lambda_n=log n. The complete prime term has the exact representation
\[
 P[f]=\int V_P(x)|f(x)|^2dx-D_P[f],                \tag{SE16.10}
\]
where
\[
 \begin{split}
 V_P(x)&=\frac{m(x)}{q(x)}\sum_{n\ge2}a_n
   \{m(x-\lambda_n)q(x-\lambda_n)
       +m(x+\lambda_n)q(x+\lambda_n)\},\\
 D_P[f]&=\sum_{n\ge2}a_n\int m(x)m(x-\lambda_n)q(x)q(x-\lambda_n)
       \left|\frac{f(x)}{q(x)}-
                   \frac{f(x-\lambda_n)}{q(x-\lambda_n)}\right|^2dx
       \ge0.
 \end{split}                                                    \tag{SE16.11}
\]
Proof. Expand each squared difference, change variables in its second
diagonal term, and retain the paired complex cross term. The all-prime
row is bounded by the estimates below. The complete row integral
and the source prime form are therefore finite on L2. Passing from
partial sums to the nonnegative series proves the full identity. QED.

For t=exp(|x|), z=t^(-1/2), N=floor(t), set
\[
 A_N=\sum_{2\le n\le N}\Lambda(n)n^{3/2},\quad
 T_N=\sum_{n>N}\frac{\Lambda(n)}{n^{5/2}},\quad
 p_{5/2}=\sum_{n\ge2}\frac{\Lambda(n)}{n^{5/2}}.
 \qquad V_P(z)=z^6(A_N+p_{5/2})+z^{-2}T_N.         \tag{SE16.12}
\]
The two branches for each individual event agree at z=1/sqrt(n).
This is the exact row; no finite prime catalogue replaces the source.

## 4. Full-source square identity and native return

**Theorem (source bound with retained observation defects).** For
0<eta<1 define the scalar comparison
\[
 Q_\eta(z)=\eta-b_c+
  \{\eta-(1-\eta)(g_c-24/5)+b_c\}z^6
       -(1-\eta)H(z)-V_P(z).                      \tag{SE16.13}
\]
Then the exact source identity is
\[
 \begin{split}
 s[f]+\eta\|f\|_X^2
 &=\int Q_\eta(e^{-|x|/2})|f(x)|^2dx+2\eta E_+[f]\\
 &\quad +(1-\eta)\{D_\Gamma[h]+E_{\rm rem}[f]
                         +(g_c-m_\Gamma)\|g\|_2^2\}
          +D_P[f]+D_F[f].
 \end{split}                                                    \tag{SE16.14}
\]
Every term after the first two is nonnegative. Proof: the pointwise
identity G+eta|G|=(1-eta)G+2eta G_+ retains the native graph weight.
Insert (SE16.3), (SE16.6)--(SE16.12), including the difference between
the enclosed Gamma cap and the true constant. All terms then match.
The half-line integrals of H|h|^2 equal the corresponding full-line
even-potential integrals of |f|^2. No cross term is silently set to
zero. The core identities extend to X by the established finite forms
and nonnegative remainder integrals. QED.

Thus any complete proof Q_eta>=c>0 implies
\[
 s[f]+\eta\|f\|_X^2\ge c\|f\|_2^2+2\eta E_+[f],
 \qquad\|f\|_X^2\le(2+g_c)\|f\|_2^2+2E_+[f].     \tag{SE16.15}
\]
The second inequality uses |G|=2G_+-G, G>=-g_c, and ||mf||<=||f||.
If eta>=c/(2+g_c), it follows that
\[
 S_b+\eta I_X\succeq\frac{c}{2+g_c}I_X.            \tag{SE16.16}
\]
This conversion is necessary; a displayed L2 floor is not automatically
a native floor.

## 5. Complete enclosure over every spatial position

The executed choices are eta=69/100, c=1/250 and M=4096=64^2.
All quantities are enclosed with exact rational or directed 90-digit
Decimal arithmetic. The inherited logarithm routine and exact integer
square-root brackets are unchanged.

**Theorem (prime tail and event-cell envelope).** For integer M>=2,
the complete mass satisfies
\[
 \sum_{n\le M}\frac{\Lambda(n)}{n^{5/2}}
 \le p_{5/2}\le
 \sum_{n\le M}\frac{\Lambda(n)}{n^{5/2}}+\tau_M,
 \qquad \tau_M=\frac{(2/3)\log M+4/9}{M^{3/2}}.    \tag{SE16.17}
\]
This follows from Lambda(n)<=log n and the decreasing integral test.
For a rational cell a<=z<=b in [1/64,1], let
L=floor(1/b^2), U=floor(1/a^2). Then
\[
 V_P(z)\le b^6(A_L+p_{5/2})
  +a^{-2}\left(\sum_{U<n\le M}\frac{\Lambda(n)}{n^{5/2}}+\tau_M\right)
  +\sum_{L<n\le U}\frac{\Lambda(n)}{n^{3/2}}.      \tag{SE16.18}
\]
Proof. Apart from the common z^6 p_(5/2) term, an event has value
Lambda(n) min(n^(3/2)z^6,n^(-5/2)z^(-2)). The first branch applies
below its breakpoint, and the second above. A straddled event is
bounded once by its peak Lambda(n)/n^(3/2). The other events are
monotone on the cell and receive their endpoint bounds. For n>M the
second branch always applies on the entire corridor. QED.

This treatment avoids a false double charge at a prime breakpoint.
Independently maximizing a prefix and tail that both contain that
event can retain a fixed excess even when the cell shrinks to zero.

The certificate encloses the polynomial part of (SE16.13) over each
entire interval, subtracts the upper bound (SE16.18), and bisects
until the resulting lower bound is at least 1/250. The archived 44
cells have exact matching endpoints and cover [1/64,1] without gaps.
Maximum depth is nine. Their minimum enclosed lower value exceeds
0.00425727944. This is an interval cover, not a finite sample test.

**Theorem (entire exterior).** For t=exp(|x|)>=M,
\[
 V_P(x)\le\frac{(16/15)\log t+4/9}{\sqrt t}
              +\frac{2\log t}{t^{3/2}}+\frac{p_{5/2}}{t^3}.
                                                               \tag{SE16.19}
\]
Proof. For the first sum in (SE16.12), monotonicity gives
sum_(n<=t)n^(3/2)<=(2/5)t^(5/2)+t^(3/2). Multiply by log(t)/t^3.
For the noninteger tail, a decreasing function F obeys
sum_(n>t)F(n)<=F(t)+integral_t^infinity F(y)dy. Apply this to
F(y)=log(y)/y^(5/2), and multiply by t. Add p_(5/2)t^(-3).
The two logarithmic coefficients sum to 16/15. QED.

Every term on the right decreases for t>=4096, since log(4096)>2.
Also H(z)<=4z^3/15+20z^6/9. The coefficient of z^6 in the diagonal
part of (SE16.13) is positive. Therefore throughout the exterior
\[
 Q_{69/100}\ge\frac{69}{100}-\frac1{10}
 -\frac{31}{100}\left(\frac4{15M^{3/2}}+\frac{20}{9M^3}\right)
 -\left(\frac{(16/15)\log M+4/9}{\sqrt M}
              +\frac{2\log M}{M^{3/2}}+\frac{p_{5/2}}{M^3}\right)
 >0.44436234456>\frac1{250}.                       \tag{SE16.20}
\]
The complete prime mass enclosure lies in
(0.28873815,0.28876101). The omitted prime powers are bounded by
(SE16.17) both in the cell cover and in the exterior estimate.
No high-frequency Gamma remainder has been neglected with unknown
sign: (SE16.4) proves that every omitted Gamma mode is nonnegative.

## 6. Executed global theorem and loss-of-return control

**Theorem (global certificate).** The complete spatial proof yields
Q_(69/100)>=1/250. Applying (SE16.16) gives (SE16.1), since
(1/250)/(2+269/50)=1/1845. In particular
\[
 \kappa_\eta=0,\qquad\ker(S_b+\eta I_X)=\{0\}
 \quad(\eta\ge69/100),\qquad
 S_b\succeq-\frac{25441}{36900}I_X.                \tag{SE16.21}
\]
The last inequality also gives zero negative count at the implied
shift 25441/36900; the stated positive native margin and nullity
certificate are recorded at the simple anchor eta=69/100. This is
an improved sufficient shift, not the exact spectral edge.

**Theorem (the retained sign matters to this comparison).** If the
opposite-half subtraction in (SE16.5) is erased before bounding, the
two weighted rows increase by
\[
 H_{\rm erase}(z)-H(z)=\frac45z^3+\frac49z^7.
                                                               \tag{SE16.22}
\]
At x=log3, z=1/sqrt3, the complete interval calculation gives
Q_(69/100)>0.00697609 with the return, whereas the erased comparison
has an upper bound below -0.04362828. Proof: integrate the added
2 m(x)m(y)exp(-beta(x+y)) term against q(y)/q(x), yielding
2 exp(-(1+beta)x)/(2+beta), and sum the two modes. For the point
certificate use N=3 in the exact prime formula (SE16.12) with the
complete mass and tail enclosures. QED.

This failed comparison is not a negative witness for the actual
source. It identifies information lost by one particular bound.
It also does not prove that every alternative unsigned estimate
must fail, or that these comparison weights are optimal.

## 7. Observer, reference and remaining boundary

The weight q is a chosen certificate gauge, not a new physical source
or preferred observer. Equation (SE16.14) retains its exact residuals;
another admissible weight changes the comparison and its residuals
together. The source itself does not change. Faithful transport carries
the source, odd involution, weight maps, domains and Gram metric,
preserving the source count as in SE13. The half-line chart is faithful
because oddness supplies its complementary reading. Arbitrary cuts
with unknown complementary data are not covered by this argument.

The result strengthens the global positive-eta certificate from SE15.
It does not execute SE15's radius-6.6 local hypothesis for eta=1/2.
That shift and the cofinal eta-zero signs remain open. The strict
margin belongs to S_b+0.69 I, not to the unshifted completed source
or its critical observer. SE5's essential zero threshold, the
historical five-label boundary, K0 and RH are unchanged.

The written identities and bounds, interval replay, finite controls,
source provenance and external review are distinct evidence categories.
No formal proof-assistant verification or external review is claimed.

See the [replay](../../../proof_lab/endpoint_signed_return_certificate.py),
[result](../../../proof_lab/ENDPOINT_SIGNED_RETURN_RESULT.json),
[independent controls](../../../proof_lab/test_endpoint_signed_return_certificate.py),
[sources](SE16_SOURCE_RECORD.md), [audit](SE16_SCOPE.md), and
[source pins](SE16_SOURCE_PINS.json).
