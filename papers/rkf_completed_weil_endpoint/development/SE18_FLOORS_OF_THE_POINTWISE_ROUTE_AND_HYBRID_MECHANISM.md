# SE18: floors of the pointwise route and the hybrid mechanism toward eta zero

12 October 2026. Owner: Monty. Written stage: general proofs with
direct checks only, following the 10 October verification preference.
No replay, certificate or test suite is added by this stage.

SE15--SE17 certified global anchors 326/369, 69/100 and 59/100 by one
mechanism: a pointwise comparison Q_eta>=c on z=exp(-|x|/2) in [0,1],
with every omitted piece retained as a nonnegative square residual.
This note answers the question those anchors raise: how, along this
line, convergence toward eta zero can and cannot happen.

Results. (1) For fixed comparison weights the certifiable eta set is a
half-line [eta_pw,1); SE17's own archive puts eta_pw>=0.58938 for its
weights, so the anchor 0.59 is tight and no smaller anchor exists on
this route without changing weights. (2) Every comparison that bounds
the odd pole by the constant b_c has the exact exterior value
Q_eta(0)=eta-b_c, hence a floor eta>=1/10 located at the escaping end.
(3) The pole admits a budget law: a density tau certifies the pole iff
4 int v^2/tau<=1, a convex condition; the weight-q0 row
(4/15)(z-z^3) saturates it, vanishes at z=0, and costs more than the
constant bound only on z in (0.48277,0.86415), by at most 0.00765.
(4) At the cut point z=1 the prime row equals 2 sum Lambda(n)n^-2
q(log n)/q(0) for every even weight; for SE17's weights this forces
eta>=0.5784 at x=0, while SE14's exact aperture certificate proves
kappa_eta=0 for all eta>=0 on |x|<=0.84. The pointwise floor therefore
sits inside the region already settled exactly: it is a feature of the
row method, not of the source. (5) For f supported in |x|>=A the SE17
identity alone gives s[f]+eta||f||_X^2>=0 as soon as
eta>=Phi_ext(exp(-A/2)), and Phi_ext(z)=O(z log(1/z)) once the pole is
budgeted. Convergence toward eta zero is therefore an aperture program:
exact local certificates on A_j -> infinity glued to an exterior row
bound that decays like A_j exp(-A_j/2). The global pointwise anchors
cannot deliver it.

Eta=1/2, the cofinal eta-zero sign, K0 and RH remain open. The local
radius remains 21/25. Nothing here changes a certified number.

## 1. Same source; the comparison is affine in eta

Typed cuts, cut scalars, derived iota, lawful composition, targets and
Smriti precede the representations. Use SE17.2--SE17.11 unchanged:
m(x)=exp(-3|x|/2), g=mf, u=m^2=z^6 with z=exp(-|x|/2), the native graph
norm ||f||_X, the complete source s[f]=Gamma[f]-P[f]-F[f], the Gamma
lower potential L_Gamma(z)=A(z)/S_3(z) of SE17.6, the shaped prime row
V_alpha of SE17.9, the pole bound F[f]<=b_c int(1-u)|f|^2 of SE15.4
with b_c=1/10, and the identity
\[
 s[f]+\eta\|f\|_X^2=\int Q_{\eta,\alpha}(z)|f|^2dx+R_{\eta,\alpha}[f],
 \qquad
 Q_{\eta,\alpha}=d_\eta-V_\alpha,
 \quad d_\eta=\eta-b_c+(\eta+b_c)z^6+(1-\eta)L_\Gamma,
                                                               \tag{SE18.1}
\]
where R_{eta,alpha}=2 eta E_+ + (1-eta){D_Gamma+E_16+(g_c-m_Gamma)||g||^2}
+D_{P,alpha}+D_F>=0 collects the retained squares of SE17.11.

**Theorem 1 (floor functional of a fixed comparison).** For fixed
weights, d_eta is affine in eta with slope 1+z^6-L_Gamma(z)>0 on [0,1],
and
\[
 Q_{\eta,\alpha}\ge0\ \text{on }[0,1]
 \iff
 \eta\ge\eta_{\rm pw}(q_\Gamma,q_\alpha):=
 \sup_{0\le z\le1}\Phi(z),\qquad
 \Phi(z)=\frac{V_\alpha(z)+b_c(1-z^6)-L_\Gamma(z)}{1+z^6-L_\Gamma(z)}.
                                                               \tag{SE18.2}
\]
Proof. The slope is positive because L_Gamma<1: its maximum on [0,1]
is L_Gamma(1)=C_16-g_c-sum_k H*_{beta_k}(1)=0.04251950947603122...,
computed exactly from SE17.6, and L_Gamma<=0 on (0,1/2] (direct check,
section 7). Solving d_eta(z)-V_alpha(z)>=0 for eta at each z gives
eta>=Phi(z); the supremum over z is the condition. QED.

**Corollary 1.1 (SE17's anchor is tight).** Let Q_lower(cell) be an
enclosed lower value of Q_{59/100,alpha} on a cell of the SE17 archive.
Since Q_{eta} is affine in eta with the slope above,
\[
 \eta_{\rm pw}\ \ge\ \frac{59}{100}-\frac{Q_{\rm lower}(\text{cell})}
   {\max_{\rm cell}(1+z^6-L_\Gamma(z))}.               \tag{SE18.3}
\]
The archive's weakest cells give eta_pw>=0.58938 (cells at
x in [0.008,0.012], x in [0.580,0.583] and x in [0.495,0.500]; direct
check, section 7). The anchor 59/100 therefore exceeds the route's
floor for these weights by less than 0.0007. A fourth anchor on this
route requires a change of weights, not a finer grid.

Theorem 1 is the structural reason the anchor sequence
0.8835, 0.69, 0.59 moved only when the weights moved (SE16: signed
return and q_0; SE17: separate q_Gamma and shaped q_alpha).

## 2. The exterior floor of every constant-pole comparison

**Theorem 2.** For every admissible Gamma weight and every prime
weight of the SE16--SE17 type,
\[
 Q_{\eta,\alpha}(0)=\eta-b_c .                                  \tag{SE18.4}
\]
Hence a comparison that bounds the pole by b_c int(1-u)|f|^2 certifies
no anchor below b_c=1/10, and none below log 3-1=0.09861... if b_c is
sharpened to its exact SE15.5 constant.

Proof. At z=0 (x -> infinity): L_Gamma(0)=A(0)/S_3(0)=0, since every
monomial of A has positive degree (the lowest is z^3, SE17.6 and the
direct check); V_r(0)=0 for both rows because z^6(A_{r,N}+p_{2+r}) and
z^{-4r}T_{r,N} both tend to zero as t=z^{-2} -> infinity (Theorem 5
proves the rate); so V_alpha(0)=0 by SE17.9. Then d_eta(0)=eta-b_c and
(SE18.4) follows. SE17.16 is this value minus the exterior remainders,
which is why its exterior bound reads 59/100-1/10-small>0.344. QED.

Where the floor lives. z -> 0 is the escaping end: SE5 places zero in
the essential spectrum of S_b through odd packets whose supports leave
every aperture. On such normalized packets the actual pole form
F[f]=2|<mf,sinh(x/2)>|^2 tends to zero, since v=m sinh(x/2) is in L^2,
while the constant bound keeps b_c||f||^2. The retained residual D_F
in (SE18.1) tends to b_c||f||_2^2 along them: the floor is exactly the
slack of the constant pole bound at infinity. It is not a property of
the source.

## 3. The pole as a third independent weight: a budget law

On the odd carrier, f(-x)=-f(x) and v(-x)=-v(x), so with h=sqrt2 f on
x>0,
\[
 F[f]=2\Big|\int_{\mathbb R}fv\,dx\Big|^2
     =8\Big|\int_0^\infty fv\,dx\Big|^2
     =4\Big|\int_0^\infty hv\,dx\Big|^2,
 \qquad v(x)=e^{-3x/2}\sinh(x/2)>0\ (x>0).            \tag{SE18.5}
\]
The pole is a rank-one positive kernel 4v(x)v(y) on the half-line, so
the weighted row identity SE16.7 applies to it exactly as to the Gamma
and prime kernels.

**Theorem 3 (pole budget law).** Let tau>0 be measurable on (0,infinity).
Then
\[
 F[f]\le\int_0^\infty\tau|h|^2dx\quad\text{for all }f\in X
 \iff
 4\int_0^\infty\frac{v^2}{\tau}dx\le1 .                         \tag{SE18.6}
\]
The admissible densities form a convex set. For a positive weight q
with <v,q>:=int_0^infty vq<infinity, the row
tau_q=4v<v,q>/q is admissible and
\[
 F[f]=\int_0^\infty\tau_q|h|^2dx-D_{F,q}[h],
 \qquad D_{F,q}[h]=2\iint v(x)v(y)q(x)q(y)
 \Big|\frac{h(x)}{q(x)}-\frac{h(y)}{q(y)}\Big|^2dxdy\ge0.      \tag{SE18.7}
\]

Proof. By Cauchy--Schwarz with weight tau,
4|int hv|^2<=4 int (v^2/tau) int tau|h|^2, which gives the forward
implication when the budget holds. For the converse take h=v/tau
(truncated and then extended by monotone convergence): both sides equal
4(int v^2/tau)^2 and int v^2/tau respectively, so the inequality forces
4 int v^2/tau<=1. Convexity: tau -> int v^2/tau is convex because
1/tau is convex and v^2>=0. For the row, (SE18.7) is SE16.7 with
k=4vv; integrating the row against q gives
int tau_q q=4<v,q>^2 and 4 int v^2/tau_q=4 int v q/(4<v,q>)=1, so the
row saturates the budget exactly. QED.

Two admissible densities are already in the line. SE15.4 is
tau=(log3-1)(1-u) with 4 int v^2/tau=1 exactly (SE15.5). With
q_0=exp(-x/2),
\[
 \langle v,q_0\rangle=\frac12\Big(\frac23-\frac25\Big)=\frac2{15},
 \qquad
 \tau_0(z)=\frac{4}{15}(z-z^3),\quad
 \tau_0(0)=\tau_0(1)=0,\quad
 \max\tau_0=\frac{8}{45\sqrt3}=0.10264\ldots\ \text{at }x=\log3.
                                                               \tag{SE18.8}
\]
Direct check: 4 int v^2/tau_0=(15/4) int_0^infty e^{-3x/2}(1-e^{-x})dx
=(15/4)(2/3-2/5)=1.

**Corollary 3.1 (where the row costs more than the constant).**
tau_0(z)>b_c(1-z^6) exactly on the band where
3z^6-8z^3+8z-3<0, i.e.
\[
 (z-1)(3z^5+3z^4+3z^3-5z^2-5z+3)<0,\qquad
 z\in(0.48277\ldots,\,0.86415\ldots),
 \quad x\in(0.2921\ldots,\,1.4563\ldots),                          \tag{SE18.9}
\]
with maximal excess 0.00765 at z=0.6466 (x=0.872). Elsewhere, and in
particular for all z<0.48277 up to the escaping end, the row is cheaper.
Since the excess exceeds SE17's spatial floor 1/1000, replacing b_c by
tau_0 at eta=59/100 is not free on the band; a shaped admissible tau,
or a slightly larger eta on the band, is the executable lever. Because
the pole kernel is positive on the half-line, the convex-cone theorem
SE17.12 extends verbatim to triples (q_Gamma,q_alpha,q_F): certifying
two pole weights certifies every positive combination.

With any admissible tau vanishing at z=0 the exterior value becomes
Q(0)=eta, and the floor of Theorem 2 disappears. The pole is thereby
the third independent reading of the source, on the same footing SE17
gave the primes.

## 4. The cut-point floor and translate charging

**Theorem 4 (prime row at the cut point).** For every positive even
weight q on the line, the SE16.10 prime row at x=0 is
\[
 V_q(0)=2\sum_{n\ge2}\frac{\Lambda(n)}{n^2}\,\frac{q(\log n)}{q(0)} .
                                                               \tag{SE18.10}
\]
For q_0 this is 2p_{5/2}; for SE17's q_alpha it is
(2p_{5/2}-2 alpha p_{11/2})/(1-alpha), which the certified masses place
in [1.17471,1.17481] at alpha=21/40 and in [1.18681,1.18692] at
alpha=53/100. Together with L_Gamma(1)=0.0425195... this forces, at the
single point x=0,
\[
 \eta\ \ge\ \frac{V_\alpha(1)-L_\Gamma(1)}{2-L_\Gamma(1)}
 \ \ge\ 0.57839\quad(\alpha=21/40),\qquad \ge0.58457\quad(\alpha=53/100).
                                                               \tag{SE18.11}
\]
Proof. In SE16.10, at x=0, m(0)=q(0)^{-1}q(0)=1 and the two translates
contribute m(log n)q(log n) each, with m(log n)=n^{-3/2} and
a_n=Lambda(n)n^{-1/2}; (SE18.10) follows. At z=1 both prime rows of
SE17.8 reduce to 2p_{2+r}, and SE17.9 gives the quotient. The floor is
(SE18.2) evaluated at z=1, where b_c(1-z^6)=0. QED.

**Lemma 4.1 (translate charging).** For any positive weight q and any
prime p,
\[
 V_q(0)\,V_q(\log p)\ \ge\ 2\,\Lambda(p)^2\,p^{-4},
 \qquad\text{so}\qquad
 \max\{V_q(0),V_q(\log p)\}\ \ge\ \sqrt2\,\Lambda(p)\,p^{-2},
                                                               \tag{SE18.12}
\]
which for p=2 is 0.2450... Proof. Keep only the n=p term of
(SE18.10) at x=0, and at x=log p keep only the term of the SE16.10 row
whose translate returns to the origin, m(log p)q(log p)^{-1}a_p m(0)q(0)
=Lambda(p)p^{-2}q(0)/q(log p). Thus V_q(log p)>=Lambda(p)p^{-2}q(0)/q(log p)
and V_q(0)>=2Lambda(p)p^{-2}q(log p)/q(0). Multiply. QED.

Why this matters for convergence. SE14 proves, by an exact matrix
certificate with all 208 pivots, kappa_eta=0 for every eta>=0 on the
aperture |x|<=21/25: the actual source is nonnegative at eta zero
throughout |x|<=0.84. Theorems 1 and 4 show that the pointwise route's
floor for SE17's weights is attained at x in [0.008,0.012] and
x in [0.495,0.583] -- inside that aperture. The row method charges, at
x=0, the potential of translates by log n>=log 2=0.693, which a
function supported in |x|<0.34 never meets; Lemma 4.1 shows no choice
of weight removes this charge from both x=0 and x=log 2. The interior
floor of the pointwise route is therefore an artifact of pointwise
comparison against a translation kernel, not information about S_b.

## 5. Exterior decay and the hybrid mechanism

**Theorem 5 (exterior requirement decays).** Let the pole be read by an
admissible density tau with tau(z)<=c_F z on z<=1/2 (tau_0 has
c_F=4/15). For 0<z<=1/2,
\[
 V_{1/2}(z)\le\frac{4}{5}\,(1.746)\,(-z\log z)+\frac{2}{3}(1.54)\,
 z(-2\log z+\tfrac23)+p_{5/2}z^6
 \le 3.46\,(-z\log z)+0.69\,z+0.29\,z^6,                      \tag{SE18.13}
\]
\[
 V_\alpha(z)\le\frac{V_{1/2}(z)}{1-\alpha}\le\frac{V_{1/2}(z)}{47/100},
 \qquad -L_\Gamma(z)\le C_\Gamma z^3,\quad C_\Gamma=\sum_{j\ge3}|a_j|2^{-(j-3)}=0.7559\ldots
                                                               \tag{SE18.14}
\]
Consequently the exterior floor function
Phi_ext(z_A):=sup_{z<=z_A}[V_alpha(z)+tau(z)-L_Gamma(z)]/(1+z^6-L_Gamma(z))
satisfies
\[
 \Phi_{\rm ext}(z_A)\le 7.37\,(-z_A\log z_A)+1.75\,z_A+0.62\,z_A^6+0.76\,z_A^3
 \quad(z_A\le\tfrac12),
 \qquad z_A=e^{-A/2},                                            \tag{SE18.15}
\]
and for every f in X supported in |x|>=A,
\[
 s[f]+\eta\|f\|_X^2\ \ge\ 0\qquad\text{whenever}\quad \eta\ge\Phi_{\rm ext}(e^{-A/2}).
                                                               \tag{SE18.16}
\]
In particular Phi_ext(e^{-A/2})=O(A e^{-A/2}) -> 0.

Proof. In SE17.8 with t=z^{-2}, N=floor t: Lambda(n)<=log n gives
A_{1/2,N}<=log N sum_{n<=N}n^{3/2}<=(2/5)(N+1)^{5/2}log t, and for
z<=1/2, (N+1)^{5/2}<=(z^{-2}+1)^{5/2}<=(5/4)^{5/2}z^{-5}=1.746 z^{-5};
hence z^6A_{1/2,N}<=(2/5)(1.746)(-2 z log z). The tail obeys the
decreasing integral test for n>=2:
T_{1/2,N}<=int_N^infty log t\,t^{-5/2}dt=(2/3)N^{-3/2}(log N+2/3), and
N>=t-1>=(3/4)z^{-2} gives N^{-3/2}<=(4/3)^{3/2}z^3=1.54 z^3, so
z^{-2}T_{1/2,N}<=(2/3)(1.54)z(-2log z+2/3). Adding p_{5/2}z^6<=0.2888 z^6
proves (SE18.13). SE17.9 and (1-alpha)q_0<=q_alpha give the first part
of (SE18.14); the second is the triangle inequality on A(z) with
S_3>=1 and z^{j}<=z^3 2^{-(j-3)} for z<=1/2. The denominator in Phi is
at least 1 because L_Gamma<=0 on (0,1/2] (section 7). For f supported
in |x|>=A, the integral in (SE18.1) sees only z<=z_A, so
int Q|f|^2>=inf_{z<=z_A}Q(z)||f||_2^2>=0 when eta>=Phi_ext(z_A); the
residual is nonnegative. QED.

The constants are crude: the 604-entry catalogue gives
V_{1/2}(z)/z between 1.01 and 1.08 on [1/20,1/2] (direct check), so the
actual exterior requirement there is closer to 2.6 z_A than to (SE18.15). The written rate
uses only Lambda(n)<=log n and integral tests, as SE17.13 does; a
Chebyshev-type bound on sum_{n<=N}Lambda(n) is deliberately not
imported. For z<1/64 the certified exterior estimate SE16.19 (decreasing
beyond M=4096) already bounds the prime row; (SE18.13) is the written
general argument for the rate.

**Theorem 6 (the hybrid mechanism).** Let A_j -> infinity and put
eta_j:=max{eta_loc(A_j), Phi_ext(e^{-A_j/2})}, where eta_loc(A) is the
smallest eta for which an executed local certificate gives
kappa_eta(A)=N_-((S_b+eta I)|_{X_A})=0. Then:
(i) by SE15's effective local-to-global inertia transfer (SE15 section 6)
with (SE18.16) as the exterior budget, kappa_{eta_j}=0 on the whole
source for every j;
(ii) by SE13.I17, S_b>=0 iff such a sequence exists with eta_j -> 0;
(iii) since Phi_ext(e^{-A/2}) -> 0, eta_j -> 0 iff eta_loc(A_j) -> 0:
the entire convergence question toward eta zero is the local aperture
question, with an exterior cost that decays like A e^{-A/2}.

Proof. (i) is the cited transfer with the exterior budget supplied by
Theorem 5 instead of SE15's crude remainders; (ii) is SE13.I17 verbatim;
(iii) is Theorem 5. QED.

SE14 has eta_loc(21/25)=0 exactly. What is missing for convergence is
eta_loc(A)=0 (or -> 0) for A beyond 0.84, which SE13--SE14 state needs
recalibration at each new radius, and which no global pointwise anchor
can supply (Theorems 1, 2, 4). This locates the remaining work: the
moving-calibration matrix certificates of SE14 on growing apertures,
each glued to (SE18.16).

## 6. What is and is not established

Established in this note (written proofs; direct checks in section 7):
the affine floor functional and the tightness of SE17's anchor; the
exact exterior value eta-b_c and the resulting floor of every
constant-pole comparison; the pole budget law and its convexity; the
q_0 pole row, its band and its maximal excess; the cut-point row formula
and the SE17 cut-point floor 0.5784; translate charging; the exterior
decay rate and the hybrid criterion.

Not established: any new anchor below 59/100; any local certificate
beyond radius 21/25; eta=1/2; the cofinal eta-zero sign; global
critical contractivity; K0; RH. No optimal weight, exact spectral edge
or rate for eta_loc is claimed. Weighted Schur testing, Cauchy--Schwarz
with weights and integral tests are elementary prior art; the new
content is the exact location and size of this route's floors on this
source, the pole budget law, and the reduction of eta-zero convergence
to the aperture program with an explicit exterior rate.

## 7. Direct checks performed for the changed claims

Computed exactly or with outward rounding from the SE17 archive
(proof_lab/ENDPOINT_WEIGHT_FAMILY_RESULT.json at commit 2e556a1a):

```text
L_Gamma(1) = 0.04251950947603122...       (rational, from SE17.6)
lowest power of A(z): z^3, a_3 = -0.2031746...   =>  L_Gamma(0) = 0
max L_Gamma on (0,1/2] at 1000 rational points: -2.5e-11 < 0
C_Gamma = sum_{j>=3}|a_j| 2^{-(j-3)} = 0.75594999...
<v,q_0> = 2/15;  4 int v^2/tau_0 = (15/4)(2/3-2/5) = 1 exactly
max tau_0 = 8/(45 sqrt3) = 0.10264004785...  at z = 1/sqrt3
band 3z^6-8z^3+8z-3 < 0: z in (0.48277029..., 0.86415086...)
   factor (z-1)(3z^5+3z^4+3z^3-5z^2-5z+3); max excess 0.0076448 at z = 0.6466
V_alpha(1): alpha=21/40 -> [1.1747110565, 1.1748072612]; alpha=53/100 -> [1.1868130778, 1.1869103059]
cut-point floors: 0.578392... (21/40), 0.584574... (53/100)
archive route floor: 0.589384 (cell x in [0.008,0.012], lower 0.001216),
                     0.589278 (cell x in [0.580,0.583], lower 0.001013),
                     0.589259 (cell x in [0.495,0.500], lower 0.001102)
V_{1/2}(z) from the 604-entry catalogue vs (SE18.13): z=1/2: 0.50726 <= 1.5487;
   z=1/10: 0.10687 <= 0.8657; z=1/20: 0.05235 <= 0.5528  (bound holds, 3-10x loose);
   V_{1/2}(z)/z in [1.01,1.08] on [1/20,1/2] (catalogue complete there: t <= 400 << 4096)
digamma slack: m_Gamma = ln pi - psi(1/4) = 5.3721834192..., g_c - m_Gamma = 0.0078165...
```

Not run: any replay, the Node engine gate, the Python test suites, Lean.
Reported as such. No pin, archive or earlier proof is modified.

See [SE17](SE17_INDEPENDENT_WEIGHTS_AND_GLOBAL_FAMILY.md),
[SE16](SE16_SIGNED_RETURN_AND_GLOBAL_SHIFT.md),
[SE15](SE15_EFFECTIVE_LOCALIZATION_AND_GLOBAL_ETA.md),
[SE14](SE14_MOVING_CALIBRATION_AND_INVARIANT_RECOVERY.md),
[SE13 index theorems](SE13_MOVING_REFERENCE_INDEX_THEOREMS.md),
[sources](SE18_SOURCE_RECORD.md) and [scope](SE18_SCOPE.md).
