# SE24: three independent weights and an exact pole row; global eta 0.56

12 October 2026. Owner: Monty.

The entire corrected complex odd source satisfies
\[
 S_b+\frac{14}{25}I_X\succeq\frac1{7380}I_X .
                                                               \tag{SE24.1}
\]
The sufficient global anchor improves from SE23's 113/200=0.565 to
14/25=0.56, by a mechanism different from SE22--SE23: those keep SE17's
weights and absorb the pole through the reciprocal budget of the whole
remaining comparison; this stage changes all three weights and reads the
pole through an explicit row that saturates its own budget. The proof
reads the three kernels of the source through three independent
positive weights: a Gamma weight that does not vanish at the odd
boundary, a steeper prime weight with four exponents, and -- new -- a
pole weight whose row saturates the pole budget law of SE18. Because the
pole is read by a row rather than the constant b_c, the exterior value
of the comparison is eta itself and the constant-pole floor at infinity
identified in SE18 (as corrected by the SE19 audit, section 2) is gone. The spatial cover therefore starts at z=1/512 with a 2^18
prime-power catalogue.

The positive local aperture remains 21/25. Eta zero, the unshifted
critical observer, the historical five-label endpoint, K0 and RH remain
open. The weights were found by an exploratory float search that is not
an input to the replay; the exploratory minima over wider exponential-sum
families lay near 0.55. No route-floor or tightness claim is inferred
from interval lower bounds (SE19 audit, section 1).

## 1. Same source, three readings, three weights

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the representations. Use SE17.2 unchanged: m=e^{-3|x|/2},
g=mf, u=m^2=z^6, z=e^{-|x|/2}, the native graph norm, and
s[f]=Gamma[f]-P[f]-F[f]. With h=sqrt2 f on x>0, the pole is the rank-one
positive half-line kernel 4v(x)v(y), v=e^{-3x/2}sinh(x/2)=(z^2-z^4)/2
(SE18.5). The three weights are
\[
 \begin{split}
 q_\Gamma(x)&=e^{-x/2}-\tfrac1{10}e^{-5x/2}=z-\tfrac1{10}z^5,\qquad x>0,\\
 q_P(x)&=\tfrac1{12}e^{-|x|/2}+e^{-3|x|/2}-\tfrac75e^{-5|x|/2}+\tfrac25e^{-7|x|/2}
        =\tfrac1{12}z+z^3-\tfrac75z^5+\tfrac25z^7,\\
 q_F(x)&=e^{-x/2}+\tfrac14e^{-3x/2}=z+\tfrac14z^3,\qquad x>0.
 \end{split}                                                    \tag{SE24.2}
\]
q_Gamma>=(9/10)z and q_F>=z on (0,1]. q_P/z is the cubic
p(u)=(2/5)u^3-(7/5)u^2+u+1/12 in u=z^2, positive on [0,1] (its interior
minimum is 0.286 at u=0.44, and p(0)=p(1)=1/12); the replay certifies
positivity on every cell by interval evaluation and on the exterior by
q_P>=(1/12-(7/5)z^4)z. None of the weights changes the source, its odd
carrier or its native pairing: each enters only through the weighted
row identity SE16.7 with its own retained square residual.

## 2. Gamma reading with a non-vanishing boundary weight

**Theorem (sixteen-mode rows for an exponential-sum weight).** For
q_Gamma=sum_j g_j e^{-s_j x}, a_j=s_j+3/2 and beta_k=2k+1/2, the exact
half-line rows of SE17.4 give
\[
 \sum_{k<16}H_{\beta_k}(z)=\frac{z^3N(z)}{q_\Gamma(z)},\qquad
 N(z)=\sum_{k<16}\sum_j g_j\,\frac{2\beta_k}{a_j^2-\beta_k^2}
      \big(z^{2\beta_k}-z^{2a_j}\big),
 \qquad
 L_\Gamma(z)=(C_{16}-g_c)z^6-\frac{z^3N(z)}{q_\Gamma(z)}.           \tag{SE24.3}
\]
Proof. Integrate the kernel against e^{-a y} as in SE17.5; for
a=s+3/2 the three pieces combine to (e^{-beta x}-e^{-ax}) 2beta/(a^2-beta^2),
and m(x)=z^3. All denominators are nonzero since a_j in {2,4} and beta
is a half-integer. QED.

Since q_Gamma(0)=1 the row vanishes at the cut point: L_Gamma(1)=C_16-g_c
=1.6044617488... exactly. This is the opposite of SE17's choice, whose
boundary-vanishing weight left L_Gamma(1)=0.0425 and, by the exact
cut-point row of SE18 Theorem 4 (retained by the SE19 audit for even
weights), forces eta>=0.5784 at x=0 for those weights. The price is paid
elsewhere; the comparison is a global trade.

## 3. Prime reading with four exponents

**Theorem (rows for a four-exponent even weight).** For q_P=sum_i c_i
e^{-r_i|x|} with r_i=k_i/2, k_i in {1,3,5,7}, SE17.8 gives for each
exponent, with t=e^{|x|}, N=floor t,
\[
 W_k(z)=z^{k+6}\Big(\sum_{2\le n\le N}\Lambda(n)n^{(k+2)/2}+p_{(k+4)/2}\Big)
        +z^{-k}\sum_{n>N}\Lambda(n)n^{-(k+4)/2},
 \qquad
 V_P(z)=\frac{\sum_ic_iW_{k_i}(z)}{q_P(z)},
 \qquad P[f]=\int V_P|f|^2dx-D_P[f],\ D_P\ge0.                   \tag{SE24.4}
\]
Every event n contributes Lambda(n) min(n^{(k+2)/2}z^{k+6},
n^{-(k+4)/2}z^{-k}) from the -log n translate, with peak Lambda(n)/n^2 at
z^2=1/n for every k, plus the constant z^{k+6}Lambda(n)n^{-(k+4)/2} from
the +log n translate. Linearity before division (SE17.12) applies to the
signed combination: on a cell the positive coefficients take the row's
upper bound and the negative coefficient takes the row's lower bound,
then one divides by the cell's lower bound of q_P.

**Lemma (higher rows under the base row).** For k>=1 and 0<z<=1,
W_k(z)<=W_1(z). Proof. On the head branch the ratio of events is
(nz^2)^{(k-1)/2}<=1 since n<=z^{-2}; on the tail branch it is
(nz^2)^{-(k-1)/2}<=1 since n>z^{-2}; and z^{k+6}p_{(k+4)/2}<=z^7p_{5/2}.
QED. This is what lets the exterior use SE16.19 alone. (The individual
higher rows V_k=W_k z^{-k} are unbounded, as the SE19 audit notes for
V_{7/2}; only the W_k, which carry their own weight, are compared.)

The complete masses p_{5/2}, p_{7/2}, p_{9/2}, p_{11/2} are enclosed by
the 2^18 catalogue plus the decreasing integral test with Lambda(n)<=log n:
tail_k<=M^{-(k+2)/2}(2 log M/(k+2)+4/(k+2)^2), each below 10^-6 at
M=262144 (the largest, k=1, is 6.53e-8).

## 4. Pole reading: the budget law executed

By SE18 Theorem 3 a density tau certifies the pole iff 4 int v^2/tau<=1,
and the row of any positive weight saturates it. For q_F=z+z^3/4,
\[
 \langle v,q_F\rangle=\frac2{15}+\frac14\Big(\frac15-\frac17\Big)=\frac{31}{210},
 \qquad
 \tau(z)=\frac{2(z^2-z^4)\,(31/210)}{z+z^3/4}
       =\frac{31}{105}\,\frac{z-z^3}{1+z^2/4},
 \qquad 4\int_0^\infty\frac{v^2}{\tau}dx=1 .                      \tag{SE24.5}
\]
tau(0)=tau(1)=0 and tau<=(31/105)z. The pole is thereby the third
independent reading; its residual D_{F,q}[h] is the explicit square
SE18.7. The constant bound b_c(1-u) of SE15.4 is no longer used.

## 5. Full source identity and the exterior

With the three rows,
\[
 s[f]+\eta\|f\|_X^2=\int Q_\eta(z)|f|^2dx+R_\eta[f],
 \qquad
 Q_\eta=\eta(1+z^6)+(1-\eta)L_\Gamma-V_P-\tau,
 \qquad R_\eta\ge0,                                                \tag{SE24.6}
\]
where R_eta=2 eta E_+ +(1-eta){D_Gamma+E_16+(g_c-m_Gamma)||g||^2}+D_P+D_{F,q}
is SE17.11's residual with the pole square in place of D_F. Proof: as
SE17.11, substituting the three exact decompositions. QED.

**Exterior.** For z<=1/512: L_Gamma(0)=0 and |L_Gamma|<=(C_16-g_c)z^6
+(10/9)z^2 sum|N_j|z^j<2e-9; tau<=(31/105)/512<6e-4; and by the lemma
and SE16.19 at M=262144,
\[
 V_P\le\frac{(1/12+1+2/5)\,W_1(z)}{(1/12-\tfrac75 512^{-4})\,z}
     \le\frac{(89/60)}{(1/12-\tfrac75 512^{-4})}\Big(\frac{(16/15)\log M+4/9}{\sqrt M}
        +\frac{2\log M}{M^{3/2}}+\frac{p_{5/2}}{M^3}\Big)<0.47814 .      \tag{SE24.7}
\]
Hence Q_{14/25}>0.0812929 on the whole exterior, including the limit at
infinity. With the constant pole bound this exterior would have read
eta-b_c; the steep prime weight (small z-coefficient 1/12) is affordable
only because the pole row removed that floor and because the catalogue
was extended from 2^12 to 2^18, which divides the SE16.19 base by 5.4.

## 6. Executed global certificate and control

**Theorem (executed three-weight certificate).** The replay covers
[1/512,1] with 1214 dyadic cells of maximal depth 12, every cell lower
value exceeding 1/1000 (the smallest is above 0.00100206, at
x in [0.325,0.328]), and the analytic exterior (SE24.7). Therefore
\[
 s[f]+\frac{14}{25}\|f\|_X^2\ge\frac1{1000}\|f\|_2^2,\qquad
 \|f\|_X^2\le(2+g_c)\|f\|_2^2+2E_+[f],\qquad
 S_b+\frac{14}{25}I_X\succeq\frac1{7380}I_X,
                                                               \tag{SE24.8}
\]
so kappa_eta=N_-(S_b+eta I_X)=0 and ker(S_b+eta I_X)={0} for every
eta>=14/25, and S_b>=-(20659/36900)I_X. Neither number is asserted to
be the spectral edge.

**Theorem (the SE17 weights do not reach this anchor).** With SE17's
Gamma and prime weights and the q_0 pole row, the exact enclosure at the
cut point z=1 is
\[
 Q_{14/25}(1)=\frac{28}{25}+\frac{11}{25}L_\Gamma^{\rm SE17}(1)-V_\alpha^{\rm SE17}(1)
 <-0.0360131<0 ,                                                  \tag{SE24.9}
\]
using L_Gamma^SE17(1)=0.04251950947603122 and the certified masses
(V_alpha(1)>=1.1747110 at alpha=21/40). The same expression is positive
at eta=59/100. This is SE18 Theorem 4 executed: the cut-point floor of
SE17's weights is 0.5784, above the new anchor. QED.

## 7. What is and is not released

Three readings, three weights, one exact source identity. The pole
budget law is executed rather than cited: the row saturates it, and the
replay's budget check would refuse a density scaled below it. The
exterior no longer carries the constant-pole floor.

This is a sufficient positive-eta certificate. It establishes neither
eta=1/2 nor a sequence of certified shifts tending to zero. For fixed
weights the certifiable set is a half-line (SE18 Theorem 1 with the
SE19 audit's valid slope), but no value of its floor is inferred here:
the weakest interval cells (x in [0.23,0.41]) locate enclosure loss, not
the true minimum of Q. The exploratory search over exponential-sum
families with up to eleven coefficients found no pointwise floor below
0.5496; that search is not evidence. A natural next executable stage
combines these weights with SE22's reciprocal pole test (the pole
absorbed by the whole remaining comparison rather than by a fixed row),
which is never more demanding than the fixed row at the same eta.

General weighted Schur testing, rank-one Cauchy--Schwarz and the
integral test are prior art. The new content is the executed pole row
and budget, the four-exponent signed prime row with its cell bounds,
the row-domination lemma, the 2^18 catalogue exterior, and the anchor
14/25 with its cut-point control.

See the [replay](../../../proof_lab/endpoint_three_weight_certificate.py),
[result](../../../proof_lab/ENDPOINT_THREE_WEIGHT_RESULT.json),
[controls](../../../proof_lab/test_endpoint_three_weight_certificate.py),
[sources](SE24_SOURCE_RECORD.md) and [audit](SE24_SCOPE.md).
