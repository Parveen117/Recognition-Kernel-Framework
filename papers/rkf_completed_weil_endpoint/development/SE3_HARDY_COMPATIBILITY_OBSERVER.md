# SE3: explicit Hardy compatibility and an arithmetic observer path

Owner: Monty Dabas. 11 October 2026, Asia/Kolkata.
Parent: Recognition commit `f234fcd52f7a2f72b1d60a6eaebca4b82598777d`.
Status: written constructions and proofs in the declared representation;
the joint RH contraction and endpoint sign remain open.

## 1. Decision and native order

SE2 gives an exact joint recovery condition. This stage supplies the
two-sheet compatibility projector, the minimum boundary representative,
the native metric pullback, and a regularized observer family for the
pinned prime--Gamma events. The construction uses the positive mismatch
normal operator; it does not invert or assume positivity of the completed
source after debt subtraction.

Typed cuts, derived iota, dagger, lawful arrows, target and Smriti remain
prior to the admitted positive representation used below. The Hardy chart
is the T37 adapter; the native graph is T35 and MP Gold 03. We retain both
carriers and the arrow between them. Their identity operators are not
interchangeable. Inner products here are conjugate-linear in the first
slot. Physical time is not introduced.

The exact arithmetic input is MP commit
`25ba21cc5148a10ada96faec721f00df419ea869`,
`proof_lab/clock_free_recognition/NATIVE_PRIME_GAMMA_RESPONSE_FACTORIZATION.md`.
That source explicitly says its unnormalized completed symbol is
indefinite near the seam. Its positive mismatch is a different form.
The [source record](SE3_SOURCE_RECORD.md) specifies the reading scope.

## 2. A concrete projector joining the two sheets

Fix a declared strip half-width a>0. Use
\(\mathcal Ff(\xi)=\int f(x)e^{i\xi x}\,dx\), unitary from
\(L^2(dx)\) to \(L^2(d\xi/(2\pi))\). Set
\[
 w_a(x)=2\cosh(2ax),\qquad
 u_+(x)=\frac{e^{ax}}{\sqrt{w_a(x)}},\quad
 u_-(x)=\frac{e^{-ax}}{\sqrt{w_a(x)}}.
\]
For \(g\in L^2(w_a dx)\), write \(h=\sqrt{w_a}g\). Then
\[
 U_a h=\binom{\mathcal F(u_+h)}{\mathcal F(u_-h)}
       =\binom{\widehat g(\xi-ia)}{\widehat g(\xi+ia)},
 \qquad U_a^\dagger U_a=I.                         \tag{SE3.1}
\]
The last equality follows from \(u_+^2+u_-^2=1\) and Parseval.
Interior strip analyticity follows by Cauchy--Schwarz against the
exponential weight; the two boundary values exist in L2. Conversely, the
declared Fourier Hardy realization is this range. Thus it is closed.

Let \(\mathcal F_2=\mathcal F\oplus\mathcal F\). Its compatibility
projector is the explicit operator
\[
 \boxed{P_a=U_aU_a^\dagger
 =\mathcal F_2 M_{p_a}\mathcal F_2^{-1},\qquad
 p_a(x)=\frac1{2\cosh(2ax)}
 \begin{pmatrix}e^{2ax}&1\\1&e^{-2ax}\end{pmatrix}.}   \tag{SE3.2}
\]
Indeed \(p_a=u u^\dagger\), \(u=(u_+,u_-)^{\mathsf T}\), and
\(u^\dagger u=1\). This proves idempotence, self-adjointness and the
range assertion. The off-diagonal entry connects the sheets. It is a
multiplier in the x representation, generally a nonlocal operator in
the frequency representation.

For any chart vector b,
\[
 \langle b,U_a h\rangle=\langle P_ab,U_a h\rangle,
 \qquad \|b\|^2=\|P_ab\|^2+\|(I-P_a)b\|^2.           \tag{SE3.3}
\]
Thus P_ab is the unique minimum chart-norm representative of that
functional. The complementary vector is retained as chart-null memory.
This makes the T35 quotient mechanism explicit for the T37 Hardy sheets.
It is not the separate debt-removing compatibility factor D_comp.

## 3. Exact odd boundary and its return to T35

For \(0<y<a\) define the odd evaluation
\[
 B_y(g)=\frac{\widehat g(-iy)-\widehat g(iy)}{\sqrt2}
       =\sqrt2\int\sinh(yx)g(x)\,dx.
\]
On odd g this equals \(\sqrt2\widehat g(-iy)\). The other evaluation
height gives the opposite sign, with the same norm. In normalized h
coordinates its Riesz vector and minimum two-sheet representative are
\[
 b_{a,y}(x)=\frac{\sqrt2\sinh(yx)}{\sqrt{w_a(x)}},
 \qquad b_{\mathrm{Hardy}}=U_ab_{a,y}.                 \tag{SE3.4}
\]
Both formulas follow directly by substitution in the pairing. If an
ambient Cauchy density represents the same odd functional, its projection
onto the odd compatible range is exactly b_Hardy. If it already
represents the odd evaluation on the whole compatible range, P_a alone
is that projection.

The exact chart norm is
\[
 \boxed{\|b_{a,y}\|^2
 =\int\frac{\sinh^2(yx)}{\cosh(2ax)}\,dx
 =\frac{\pi}{4a}
   \left(\sec\frac{\pi y}{2a}-1\right).}              \tag{SE3.5}
\]
For completeness, substituting \(t=e^{2cx}\) in the integral of
\(e^{bx}/\cosh(cx)\), for \(|b|<c\), gives
\(c^{-1}\int_0^\infty t^{(c+b)/(2c)-1}/(1+t)\,dt
=\pi/[c\cos(\pi b/(2c))]\). Apply this with c=2a, b=2y and b=0,
using \(\sinh^2(yx)=(\cosh(2yx)-1)/2\).
At the actual strip/evaluation widths a=3/2, y=1/2,
\[
 \|b_{3/2,1/2}\|^2
 =\frac\pi6\left(\frac2{\sqrt3}-1\right)
 \approx0.08100101247977.                            \tag{SE3.6}
\]
This is a Hardy chart norm, not a prime--Gamma source burden.

Now use T35's spatial graph coordinate f, with
\(g=m_af\), \(m_a=e^{-a|x|}\), and graph metric
\(M_X=I+C^\dagger C\). At a=3/2, C is exactly the T35 operator
\(Cf=(2\pi)^{-1/2}\sqrt{1+|G|}\,\widehat{m_af}\)
with its stated target measure. Define
\[
 B:X=\operatorname{Dom}C\longrightarrow L^2(dx),\qquad
 Bf=r_af,\qquad
 r_a=\sqrt{w_a}m_a=\sqrt{1+e^{-4a|x|}}.               \tag{SE3.7}
\]
X carries the graph inner product, so \(\|B\|\le\sqrt2\).
In this paragraph the adjoint defining C^dagger C is the underlying
T35 L2 adjoint; adjoints of arrows with domain X use the graph metric.
B is injective. In underlying L2 coordinates its graph adjoint is
\(B^\dagger=M_X^{-1}M_{r_a}\): this follows from the defining Riesz
pairing, not from replacing the graph dagger by a coordinate transpose.
The actual two-sheet chart on X is \(J=U_aB\), and
\[
 J^\dagger J=B^\dagger B=M_X^{-1}M_{r_a^2},\qquad
 \boxed{B^\dagger b_{a,y}
 =M_X^{-1}\bigl(\sqrt2m_a\sinh(yx)\bigr).}           \tag{SE3.8}
\]
At a=3/2, y=1/2 the right side is exactly T35's
\(r_\partial=M_X^{-1}q_b\). Consequently
\[
 \langle b_{\mathrm{Hardy}},Jf\rangle
 =\langle r_\partial,f\rangle_X
 =\langle J_Xr_\partial,J_Xf\rangle.                 \tag{SE3.9}
\]
This is an explicit boundary connection across the two representations.
It does not identify the Hardy chart norm in (SE3.6) with the graph
norm of r_partial or its completed-source inverse-half norm.

In particular, J is not declared isometric in the T35 metric. An identity
\(JD=(JDJ^\dagger)J\) would require \(JD(I-J^\dagger J)=0\);
it cannot follow merely from writing a chart adjoint. The isometric U_a
and the separate B avoid that step. This qualifies the use of T37's
equations (4.1)--(4.2) in the present metric without editing its archive.

## 4. Assemble the pinned arithmetic events on the compatible carrier

Write \(a_n=\Lambda(n)/n^2\), \(\lambda_n=\log n\),
\(m_p=\sum a_n\), \(q(\xi)=\sum a_ne^{i\lambda_n\xi}\),
\(\mathcal Q=\left(\begin{smallmatrix}0&q\\\bar q&0\end{smallmatrix}\right)\).
Use the pinned functions
\[
 g_0(\xi)=G(\xi)+m_\Gamma\ge0,\quad
 m_\Gamma=\gamma+\pi/2+3\log2+\log\pi,\quad
 d_0=m_\Gamma+m_p>0.
\]
Define the chart mismatch analysis \(\mathcal M\) by the actual rows
\[
 (\mathcal M_p\Psi)_n(\xi)
 =\sqrt{a_n}\,[\Psi_1(\xi)-e^{i\lambda_n\xi}\Psi_2(\xi)],
                                                               \tag{SE3.10}
\]
\[
 (\mathcal M_\Gamma\Psi)_{k,j}(t,\xi)
 =2^{-1/2}e^{-(k+1/4)t/2}
    (1-e^{i\xi t/2})\Psi_j(\xi),\quad j=1,2.          \tag{SE3.11}
\]
The event norms use counting measure, dt and dxi/(2pi). The direct sum
of these rows has closed natural domain and Gram
\[
 \mathcal M^\dagger\mathcal M
 =\mathbf M(\xi)=(g_0+m_p)I_2-\mathcal Q,
 \qquad \Omega_0=\mathbf M-d_0I_2=GI_2-\mathcal Q.     \tag{SE3.12}
\]
The identities follow by summing the prime outer products and integrating
the Gamma oscillator squares. They use all prime powers and all Gamma
events; no numerical event truncation is inserted.

On normalized Hardy coordinates put \(A_H=\mathcal M U_a\), and on the
native graph put
\[
 \boxed{A=\mathcal M U_aB,\qquad D=d_0B^\dagger B.}    \tag{SE3.13}
\]
Composing the closed analysis with these bounded maps gives closed
operators on their inverse-image domains. Use the native test-core
completion in which states with smooth compactly supported g are dense;
they belong to these domains. For a more general closed-C realization,
density of this common domain is an explicit additional hypothesis.
No claim that an arbitrary sine sequence is an A-graph core is needed
here. The completed form defined by the pinned chart is
\[
 s[f]=\|Af\|^2-d_0\|Bf\|^2
     =\int (Jf)^\dagger\Omega_0(Jf)\,\frac{d\xi}{2\pi}.
                                                               \tag{SE3.14}
\]
Its debt is bounded, \(0\preceq D\preceq2d_0I_X\).
Thus (SE3.13) supplies a concrete factor of the debt. It need not be
written as a square root on X: \(\sqrt{d_0}B\) has the same Gram.
The positive mismatch is not the completed source.

Because \(g_0(\xi)>0\) for \(\xi\ne0\), Gamma mismatch zero implies
\(Jf=0\) almost everywhere. Injectivity of U_a and B then gives
\(\ker A=\{0\}\). This is mismatch injectivity only. It proves neither
\(A^\dagger A\succeq D\) nor injectivity of the completed source.

### A concrete prime action, with the phase retained

Let \(T_\lambda h(x)=h(x-\lambda)\). On L2(dx),
\[
 \boxed{K_{p,a}=U_a^\dagger\mathcal Q U_a
 =\sum_{n\ge2}a_n
 [M_{u_+}T_{\lambda_n}M_{u_-}
  +M_{u_-}T_{-\lambda_n}M_{u_+}].}                   \tag{SE3.15}
\]
Fourier conjugation proves the identity; the series converges in operator
norm and \(\|K_{p,a}\|\le m_p\), by isometric compression of Q.
For each first translation its coefficient at x is
\[
 a_nu_+(x)u_-(x-\lambda_n)
 =\frac{\Lambda(n)n^{a-2}}
        {\sqrt{w_a(x)w_a(x-\log n)}}.                \tag{SE3.16}
\]
At a=3/2 this displays the coefficient Lambda(n)/sqrt(n), with both
confinement weights still attached. Removing these weights would change
the operator and invalidate the norm-summability argument.

The Gamma compression is the form
\(K_{\Gamma,a}=\sum_{\sigma=+,-}
 M_{u_\sigma}\mathcal F^{-1}G\mathcal F M_{u_\sigma}\).
Thus the compatible completed form is
\(K_{\Gamma,a}-K_{p,a}\) and its positive mismatch adds d_0 I.
This is a weighted translation/oscillator problem with explicit coefficients.
Since P_a need not commute with the multipliers, taking a pointwise inverse
and then projecting is not the same as inverting this compression.

## 5. Construct an observer path without assuming the desired sign

The following theorem applies to the closed injective A just constructed,
and to a closed endpoint restriction when supplied. Let E be the declared
finite boundary-source space, \(G_E>0\), \(W:E\to X\) bounded. Put
\[
 \mathcal L=\binom{\sqrt{d_0}B}{G_E^{-1/2}W^\dagger},
 \qquad N=A^\dagger A\ge0.
\]
The first component is the actual debt factor (SE3.13). It has an
infinite-dimensional target. E has dimension five only after the existing
five-source endpoint contract, including its complement, is supplied.

For every regularization parameter \(\epsilon>0\) define
\[
 \boxed{\mathcal O_\epsilon
  =\mathcal L(N+\epsilon I)^{-1}A^\dagger.}           \tag{SE3.17}
\]
The product denotes its bounded extension from Dom A^dagger. Polar
decomposition \(A=V N^{1/2}\) gives
\(\mathcal O_\epsilon=\mathcal L
 [N^{1/2}(N+\epsilon)^{-1}]V^\dagger\), so
\(\|\mathcal O_\epsilon\|\le\|\mathcal L\|/(2\sqrt\epsilon)\).
The extension is defined for every epsilon, independently of completed
source positivity or an inverse at zero.

For every f in Dom A its exact recovery residual is
\[
 \boxed{\mathcal Lf-\mathcal O_\epsilon Af
       =\epsilon\mathcal L(N+\epsilon I)^{-1}f.}     \tag{SE3.18}
\]
Although f need not be in Dom N, the identity follows from the bounded
spectral multiplier N/(N+epsilon) applied to f via polar decomposition.
Injectivity makes (SE3.18) tend strongly to zero. For the finite boundary
component it tends to zero in operator norm: take adjoints and use strong
convergence on the finitely many columns of WG_E^{-1/2}.

The **full target Gram** is explicit:
\[
 \boxed{\mathcal K_\epsilon
 =\mathcal O_\epsilon\mathcal O_\epsilon^\dagger
 =\mathcal L\,\frac{N}{(N+\epsilon I)^2}\,
             \mathcal L^\dagger.}                   \tag{SE3.19}
\]
It includes the debt block, the five-boundary block and both cross blocks.
For example its upper-right block is
\(\sqrt{d_0}B\,[N/(N+\epsilon)^2]WG_E^{-1/2}\).
Testing the five-boundary block alone does not test this Gram.

Norm differentiation for epsilon>0 gives
\[
 \frac{d\mathcal K_\epsilon}{d\epsilon}
 =-2\mathcal L\frac{N}{(N+\epsilon I)^3}
       \mathcal L^\dagger\preceq0.                  \tag{SE3.20}
\]
Thus its burden increases monotonically as epsilon decreases. This
monotonicity is on the target Gram; no unjustified commutation is used to
assert the same ordered derivative for O_epsilon^dagger O_epsilon.

### Exact endpoint test for the constructed path

For injective A the following are equivalent:

1. A contraction O satisfies OA=L.
2. K_epsilon <= I on the full joint target for every epsilon>0.
3. That inequality holds along any supplied sequence epsilon_j decreasing
   to zero.

Proof. Under 1, polar decomposition gives
\(\mathcal O_\epsilon=\mathcal O V
 [N/(N+\epsilon)]V^\dagger\), a contraction, proving 2.
Then 2 implies 3. Under 3, (SE3.18) gives
\(\|\mathcal Lf\|=\lim_j\|\mathcal O_{\epsilon_j}Af\|
\le\|Af\|\). The SE2 range-extension argument constructs O.
This proves 1 and hence positivity of the joint endpoint form for these
same A,D,W,G_E. QED.

This criterion gives a computable functional-calculus candidate, not a
proof of its unresolved uniform bound. A pass at one positive epsilon
does not control smaller epsilon. Small recovery error alone is also
insufficient. For example on ell2 let A=diag(1/n) and let the single
boundary row have coefficients 1/n. Its recovery error tends to zero in
norm, but the observer rows have coefficients 1/(1+epsilon n^2), whose
squared sums diverge as epsilon tends to zero. There is no bounded exact
decoder for that example. This is a control example, not the RH operator.

## 6. Moving references, endpoint restriction and next concrete target

Under unitary changes of the native, event and target frames U,V,R,
\(A'=VAU^\dagger\), \(L'=RLU^\dagger\), the constructed family obeys
\(O'_\epsilon=RO_\epsilon V^\dagger\),
\(K'_\epsilon=RK_\epsilon R^\dagger\). Hence it can travel with the
SE2 full-operator path laws without selecting an absolute initial or final
reference. Nonunitary coordinates require the transported metric.
Epsilon is an observer regularization parameter at the fixed arithmetic
eta-zero source. It is neither physical time nor the earlier eta shift.
Changing a changes the declared Hardy carrier unless a separate transport
is supplied; it is not an arbitrary means of reducing a burden.

For an odd Feshbach complement with inclusion \(I_Q:X_Q\to X\), pull back
the complete forms: \(A_Q=AI_Q\), \(B_Q=BI_Q\),
\(D_Q=d_0B_Q^\dagger B_Q\). Use the actual W and G_E on that complement.
Do not replace this compression by the Schur complement of an unrelated
full-space inverse. Closedness and dense domain must be checked for the
chosen restriction. The known full odd boundary column is r_partial;
the other four endpoint columns are not computed in this stage.

The explicit construction closes the boundary/pairing connection in
(SE3.9) and the debt pullback of the pinned chart in (SE3.13). It does not
settle every historical source normalization. In particular it does not
prove that a legacy formula with native debt d_0 I equals the derived
debt d_0 J^dagger J, or that the compressed two-sheet Gamma form equals
every other completed-Weil presentation. Those identities must be supplied
on the selected endpoint carrier before transferring an endpoint sign.

The next estimate is the full joint operator bound (SE3.19) for this
arithmetic construction on that identified endpoint carrier, or an
equivalent source-relative correction bound from SE2.8. The explicit
Hardy projector and weighted prime translations are now available to
build it. The positive T21 mismatch profile and the small Hardy norm
(SE3.6) are useful inputs, but neither pays the completed-source debt.

No RH sign, actual joint contraction, new outward numerical certificate,
Lean proof or external review is claimed. Strip Hardy projection and
regularized inverse methods have established mathematical lineage; the
new work here is their explicit source-bound integration into SE2.

See [sources](SE3_SOURCE_RECORD.md), [pins](SE3_SOURCE_PINS.json),
and [verification scope](SE3_SCOPE.md).
