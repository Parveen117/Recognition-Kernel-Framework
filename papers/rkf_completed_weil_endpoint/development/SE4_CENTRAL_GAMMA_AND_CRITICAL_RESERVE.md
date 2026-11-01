# SE4: central Gamma repair and the critical observer reserve

Owner: Monty Dabas. 11 October 2026, Asia/Kolkata.
Parent: `b119dd608cd6b1004e73a32b709348647bb5da92`.
Status: written counterexample, corrected source factorization and
critical-reserve theorem. The actual endpoint contraction remains open.

## 1. Decision: retain the target and correct its representation

The SE3 compatibility projector, boundary pullback and abstract
regularized-observer theorem remain valid. Its proposed full two-sheet
Gamma source cannot satisfy the desired contraction. This note proves
that statement with an explicit odd sine packet, then repairs the source
placement using the already declared T40 completed-Weil form.

This is a substantial reason to correct an adapter inside the existing
route, not to replace the recognition target. The owner's prime-axis
intuition is retained as a research suggestion, not used as a hypothesis
or substituted for the current endpoint task.

The native order remains: typed carrier, lawful arrows, target, pairing,
observer and retained residue, followed by the admitted representation.
We use the T35 graph carrier and SE3 notation. All adjoints on X use its
native graph metric; pairings here are conjugate-linear in the first slot.

Fix a=3/2. Write f for the T35 graph coordinate and g=mf for the physical
logarithmic test function, where m(x)=exp(-a|x|). Set
\[
 Rf=mf=g,\qquad Bf=\sqrt{2\cosh(2ax)}\,g=h,
 \qquad Jf=U_aBf.
\]
The Fourier convention is
\(\widehat g(\xi)=\int g(x)e^{i\xi x}\,dx\), with measure
dmu=dxi/(2pi). T40 sections 4--7 specify, on the odd test core,
\[
 W_\xi^-[g]
 =\int G|\widehat g|^2\,d\mu-P_{1/2}[g]
   -|L_\partial g|^2,\qquad
 L_\partial g=\sqrt2\widehat g(i/2),                 \tag{SE4.1}
\]
\[
 P_{1/2}[g]
 =2\operatorname{Re}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
    \langle g,T_{\log n}g\rangle_{L^2}.
\]
For a diagonal quadratic form the pairing-convention change from T40
does not change this real expression. Mixed forms follow by polarization.
The sum is finite on compactly supported g.

The prime term is represented correctly by the SE3 Hardy sheets.
The Gamma term in (SE4.1) reads the **central** Fourier transform of g.
It does not read the sum of the two transforms of exp(+/-ax)g.

## 2. An exact negative witness for the SE3 two-sheet source

Let \(g_0=G+m_\Gamma\), \(d_0=m_\Gamma+m_p\), with the SE3 constants.
In normalized Hardy coordinates the SE3 completed form is
\[
 s_{\rm 2sh}[h]
 =-m_\Gamma\|h\|^2+E_\Gamma[h]-\langle h,K_{p,a}h\rangle,
\quad
 E_\Gamma[h]=\sum_{\sigma=+,-}
   \int g_0|\mathcal F(u_\sigma h)|^2\,d\mu.          \tag{SE4.2}
\]
Here \(u_\pm=e^{\pm ax}/\sqrt{2\cosh(2ax)}\) and K_p,a is exactly
SE3.15. No arithmetic event is omitted in (SE4.2).

### Gamma upper estimate for a translated packet

The digamma difference series gives
\[
 0\le g_0(\xi)
 =\sum_{k\ge0}\frac{(\xi/2)^2}
 {(k+1/4)((k+1/4)^2+(\xi/2)^2)}
 \le c_\Gamma\xi^2,\qquad c_\Gamma=131/8.            \tag{SE4.3}
\]
Indeed \(\sum_{k\ge0}(k+1/4)^{-3}
\le64+\sum_{k\ge1}k^{-3}<64+3/2\).
The elementary derivative identities
\(\sum u_\sigma^2=1\), \(\sum u_\sigma u'_\sigma=0\), and
\(\sum |u'_\sigma|^2=a^2\operatorname{sech}^2(2ax)\) yield
\[
 E_\Gamma[h]\le c_\Gamma\left(
 \|h'\|^2+a^2\int\operatorname{sech}^2(2ax)|h|^2dx
 \right).                                                   \tag{SE4.4}
\]
This is an H1 estimate, justified directly by Parseval and (SE4.3).

### Prime estimate retaining the infinite tail

Suppose \(\|h\|=1\) and h is supported in \(|x|\ge r>0\).
Introduce only for this estimate the half-line isometry
\(U_0h=(\mathcal F(1_{x>0}h),\mathcal F(1_{x<0}h))\).
Pointwise,
\(\|(u_+,u_-)-(1_{x>0},1_{x<0})\|^2
\le e^{-4a|x|}\), hence
\[
 \|(U_a-U_0)h\|\le e^{-2ar}.
\]
For \(\log N<2r\), no translation with n<=N joins the two half-line
supports. Its U_0 prime cross-pairing is zero. Since the complete prime
symbol has norm at most m_p, and the remaining symbol norm is at most
\(\tau_N=\sum_{n>N}\Lambda(n)/n^2\), it follows that
\[
 |\langle h,K_{p,a}h\rangle|
 \le2m_p e^{-2ar}+\tau_N,
 \qquad \tau_N\le\frac{\log N+1}{N}\quad(N\ge2).     \tag{SE4.5}
\]
The tail bound uses Lambda(n)<=log n and the decreasing integral test
for log(x)/x^2 on [2,infinity). Also
\[
 0<m_p\le\frac{\log2}{4}+\frac{\log2+1}{2}<5/4,
 \qquad m_\Gamma>\pi/2>3/2.                          \tag{SE4.6}
\]
Thus no prime-number theorem, prime-density model or finite-prime
approximation is needed for this obstruction.

### The supplied odd sine packet

Let \(\varphi(t)=\cos(\pi t/2)1_{[-1,1]}(t)\). It is an H1
zero-boundary standing wave with \(\|\varphi\|^2=1\) and
\(\|\varphi'\|^2=\pi^2/4\). For R>L define
\[
 h_{R,L}(x)=\frac1{\sqrt{2L}}
 \left[\varphi\!\left(\frac{x-R}{L}\right)
       -\varphi\!\left(\frac{x+R}{L}\right)\right].   \tag{SE4.7}
\]
It is odd, has norm one, derivative energy pi^2/(4L^2), and support
in |x|>=R-L. Its native graph state is f=h/r_a, with the SE3 multiplier
\(r_a=\sqrt{1+e^{-4a|x|}}\). It is admissible: mf and u_+/-h are
compactly supported H1 functions, so all the displayed source forms
and the T35 graph norm are finite. Smooth odd core approximations retain
the strict negative sign by these same H1 bounds.

Choose **L=16, R=32, N=256**. Then r=16 and log N<8<2r. Using
pi^2<10, e>2 and sech(t)<=2e^(-t), equations (SE4.4)--(SE4.6) give
\[
 E_\Gamma[h]+|\langle h,K_{p,a}h\rangle|
 <\rho:=\frac{655}{4096}+\frac9{256}
         +\frac5{2^{49}}+\frac{1179}{2^{99}}<\frac14.
                                                               \tag{SE4.8}
\]
Therefore the completely specified SE3 form obeys
\[
 \boxed{s_{\rm 2sh}[h_{32,16}]<-\frac54.}             \tag{SE4.9}
\]
This is an analytic bound with an exact rational last comparison, not a
floating-point eigenvalue or a finite-event sign guess.

For the SE3 native mismatch A and debt factor sqrt(d_0)B on this f,
\(\|Af\|^2<m_p+1/4\) and \(d_0\|Bf\|^2=d_0\). Any bounded
observer recovering even the debt alone would consequently require
\[
 \boxed{\|O\|^2\ge\frac{d_0}{\|Af\|^2}
 >\frac{m_p+m_\Gamma}{m_p+1/4}>\frac{11}{6}>1.}      \tag{SE4.10}
\]
Adding boundary targets cannot repair that failed contraction. This does
not assert that every possible recovery map has infinite norm; it rules
out the unit contraction required by the SE2 sign certificate for this
particular source model.

## 3. The obstruction persists after a fixed finite-dimensional removal

Take L_j tending to infinity and R_j=4L_j. The packets (SE4.7) then have
r_j=3L_j tending to infinity. Use (SE4.4) and (SE4.5), with any N_j
tending to infinity such that log N_j<2r_j, to obtain
\[
 E_\Gamma[h_j]\longrightarrow0,\qquad
 \langle h_j,K_{p,a}h_j\rangle\longrightarrow0,
 \qquad s_{\rm 2sh}[h_j]\longrightarrow-m_\Gamma.     \tag{SE4.11}
\]
For f_j=h_j/r_a, the L2 norm tends to one and f_j converges weakly to
zero in L2. Moreover Cf_j tends strongly to zero. To verify the last
assertion, put g_j=mf_j. On its support,
\[
 \|g_j\|\le e^{-ar_j},\qquad
 \|g'_j\|\le e^{-ar_j}(\|h'_j\|+3a),
\]
using r_a>=1 and |r'_a|<=2a. Since
\(1+|G|\le1+m_\Gamma+c_\Gamma\xi^2\), Parseval proves
\(\|Cf_j\|\to0\). Consequently
\[
 \|f_j\|_X\longrightarrow1,\qquad f_j\rightharpoonup0
 \text{ in }X,\qquad \|Af_j\|^2\longrightarrow m_p.  \tag{SE4.12}
\]

Let Q be the orthogonal projection off a fixed finite-dimensional space
spanned by vectors v_i in Dom A. The coefficients of (I-Q)f_j tend to
zero, so both its X norm and its A-image norm tend to zero. B is bounded.
Therefore s_2sh[Qf_j]-s_2sh[f_j] tends to zero. The negative limit in
(SE4.11) survives this restriction.

Thus a finite-rank source-regular complement alone cannot rescue the SE3
two-sheet Gamma placement. This is a statement about that placement;
it is not a counterexample to the actual normalized Weil form (SE4.1).

## 4. Repair: central Gamma, two-sheet prime events, their own debts

Let Gamma_0 denote the scalar oscillator analysis with rows
\[
 (\Gamma_0\Phi)_k(t,\xi)
 =2^{-1/2}e^{-(k+1/4)t/2}(1-e^{i\xi t/2})\Phi(\xi).
\]
Its squared norm is \(\int g_0|\Phi|^2d\mu\).
Let M_p be the SE3 prime mismatch analysis, so
\(M_p^\dagger M_p=m_pI_2-\mathcal Q\). Define on the native graph
\[
 \boxed{A_*f=\binom{\Gamma_0\mathcal F Rf}{M_pJf},
 \qquad L_df=\binom{\sqrt{m_\Gamma}Rf}{\sqrt{m_p}Bf}.} \tag{SE4.13}
\]
The two debt channels follow their own analyses. They are not merged
into d_0 times the Hardy identity. In particular
\[
 D_*=L_d^\dagger L_d
 =m_\Gamma R^\dagger R+m_pB^\dagger B.               \tag{SE4.14}
\]

**Exact normalization theorem.** On the declared odd logarithmic core,
and by bounded extension on its native completion,
\[
 \boxed{\|A_*f\|^2-\|L_df\|^2
 =\int G|\widehat g|^2d\mu-P_{1/2}[g],
 \qquad g=mf.}                                      \tag{SE4.15}
\]

Proof. The Gamma difference in (SE4.13) is exactly
\(\int(g_0-m_\Gamma)|\widehat g|^2=\int G|\widehat g|^2\).
The prime difference is \(-\langle Jf,\mathcal QJf\rangle\).
For each lambda=log n, the first off-diagonal translation satisfies
\[
 \langle e^{ax}g,T_\lambda(e^{-ax}g)\rangle
 =e^{a\lambda}\langle g,T_\lambda g\rangle.
\]
Multiplication by Lambda(n)/n^2 gives Lambda(n)/sqrt(n) at a=3/2;
the other block supplies its conjugate. Hence the paired sum is exactly
P_1/2[g]. These identities prove (SE4.15) with all signs and measures
retained. QED.

The normalized comparison is now:

| Term | SE3 two-sheet model | T40 target and SE4 repair |
| --- | --- | --- |
| Gamma input | Jf, both shifted sheets | F(Rf), central transform |
| Gamma debt | m_Gamma times norm(Bf)^2 | m_Gamma times norm(Rf)^2 |
| Prime input | M_p Jf | Same M_p Jf |
| Prime debt | m_p times norm(Bf)^2 | Same m_p times norm(Bf)^2 |
| Odd boundary | Native T35 Riesz vector | Same vector, up to evaluation-height sign |

The exact difference between the two completed sources is
\(\int G(|\widehat{e^{ax}g}|^2+|\widehat{e^{-ax}g}|^2
-|\widehat g|^2)d\mu\). It is not a harmless chart rotation or an
extra prime-density estimate.

## 5. Bounded native realization and the corrected observer equation

The repaired analysis is bounded on the existing T35 graph carrier.
Indeed m_Gamma>1, and
\[
 \|\Gamma_0\mathcal F Rf\|^2\le m_\Gamma\|Cf\|^2,
 \qquad \|M_pJf\|^2\le2m_p\|Bf\|^2\le4m_p\|f\|_2^2.
\]
Therefore
\[
 \|A_*\|^2\le\max(m_\Gamma,4m_p),\qquad
 0\preceq D_*\preceq(m_\Gamma+2m_p)I_X.              \tag{SE4.16}
\]
Also \(|s_*[f]|\le\|Cf\|^2+2m_p\|f\|_2^2\), which supplies the
bounded extension of (SE4.15). No unproved common unbounded-operator core
is required for this repaired realization. Gamma_0 has a multiplier
positive almost everywhere away from xi=0, and R is injective; hence
\(\ker A_*=\{0\}\). This does not imply positivity after debt.

The boundary identity from SE3.8--SE3.9 is retained:
\(L_\partial(mf)=\pm\langle r_\partial,f\rangle_X\), with
\(r_\partial=M_X^{-1}q_b\). Thus, for the full odd one-boundary target,
the complete form (SE4.1) is exactly
\[
 W_\xi^-[mf]=\|A_*f\|^2-\|L_df\|^2
                     -|\langle r_\partial,f\rangle_X|^2.
                                                               \tag{SE4.17}
\]
This constructs a source-bound observer problem without presupposing
the sign being sought.

For a supplied finite endpoint label space E, positive G_E and actual
W:E->X, the correct joint target is
\[
 \boxed{\mathcal L_*f=
 \begin{pmatrix}\sqrt{m_\Gamma}Rf\\\sqrt{m_p}Bf\\
                 G_E^{-1/2}W^\dagger f\end{pmatrix},
 \qquad O_*A_*=\mathcal L_*,\quad O_*^\dagger O_*\preceq I.}
                                                               \tag{SE4.18}
\]
SE2 applies to any debt factor with Gram D_*, not only to a square root
whose target is X. With \(N_*=A_*^\dagger A_*\), the SE3 construction
becomes
\[
 O_{*,\epsilon}=\mathcal L_*(N_*+\epsilon I)^{-1}A_*^\dagger,
 \qquad K_{*,\epsilon}
 =\mathcal L_*\frac{N_*}{(N_*+\epsilon I)^2}\mathcal L_*^\dagger.
                                                               \tag{SE4.19}
\]
The recovery residual, monotonicity and uniform-contraction equivalence
proved in SE3 hold for these corrected data. No bound K_*,epsilon<=I
is asserted here. For the five-label endpoint one must still transport
the actual complement, four further source columns and its finite metric.
Since A_* is bounded, its restriction to a closed complement is bounded
without the previous unbounded-domain issue.

## 6. A strict global reserve is impossible even after the repair

Use the same escaping packets f_j from Section 3. Their central transforms
satisfy
\(\|Rf_j\|\to0\) and
\(\|\Gamma_0\mathcal F Rf_j\|\to0\), by the bounds for g_j and g'_j.
Their prime cross-pairings tend to zero and \(\|Bf_j\|=1\). Hence
\[
 \boxed{\|A_*f_j\|^2\to m_p>0,\quad
         \|L_df_j\|^2\to m_p,\quad s_*[f_j]\to0.}    \tag{SE4.20}
\]
Because f_j converges weakly to zero in X, any fixed finite-dimensional
boundary target obeys \(W^\dagger f_j\to0\). Thus
\[
 \frac{\|\mathcal L_*f_j\|^2}{\|A_*f_j\|^2}\to1.    \tag{SE4.21}
\]
Consequently there is **no** delta>0 for which
\(\|\mathcal L_*f\|^2\le(1-\delta)\|A_*f\|^2\) on the full
native carrier. Every bounded exact observer has norm at least one.
If a contractive exact observer exists, its norm must be exactly one.
This excludes a strict global reserve, not the critical inequality <=1.

The conclusion persists on a fixed finite-codimensional complement:
subtract its finite projection from f_j and use boundedness of A_*, L_d
and the finite target. The limits in (SE4.20)--(SE4.21) do not change.

The boundary remains quantitatively quiet on the escape. For
\(b_{a,y}\) from SE3 and a unit h supported in |x|>=r,
\[
 |\langle b_{a,y},h\rangle|^2
 \le\int_{|x|\ge r}|b_{a,y}(x)|^2dx
 \le\frac{e^{-2(a-y)r}}{2(a-y)}.
\]
At a=3/2, y=1/2 this is \(\tfrac12 e^{-2r}\). The infinite debt
channel can approach saturation while this boundary signal vanishes.
This does not itself bound the boundary relative to the small completed
source s_*; that source-relative estimate is still needed.

## 7. What this changes and what remains

The failed search for a contraction of the SE3 two-sheet Gamma model is
closed by the negative witness, not left as an indefinitely open task.
The actual T40 normalization now has the explicit factorization
(SE4.13)--(SE4.17), with Gamma on the central line and prime events on
the Hardy sheets. The native metric, boundary state, phase memory and
SE2 moving-observer approach are retained.

The stabilization task is the critical full-operator inequality for the
corrected data (SE4.18)--(SE4.19), allowing zero reserve on limiting
directions. A certificate that demands a uniform strict reserve on the
whole debt carrier would reject this target regardless of its sign.
The five boundary directions require their actual source-relative bound;
their small raw norm is not that bound.

Neither the failed two-sheet model nor the repaired factorization settles
RH. T40's expression is the declared target; its historical positivity
assertions and the classical zero-sum membrane are not independently
certified here. The corrected full odd source is identified; the actual
five-source Feshbach sign and critical joint contraction remain open.

See [source record](SE4_SOURCE_RECORD.md), [source pins](SE4_SOURCE_PINS.json)
and [written audit](SE4_SCOPE.md). Historical SE1--SE3 source files remain
unchanged; current navigation records this correction explicitly.
