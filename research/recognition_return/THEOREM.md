# Native graded-aperture resummation and coupling-dependent cut selection

Monty Dabas | Research result R1 | 26 September 2026

## Result in one paragraph

For a declared EMK-valued excursion operator, the recognized boundary response has a constructive limit for **every finite nonnegative coupling**, although both the uncut Neumann series and, at stronger coupling, even the recognized moment series can diverge. The limit is obtained from actual inverses on a cofinal sequence of native even apertures. Its recursion, exact rational enclosure, boundary-class independence, and joint cutoff/coupling bound are derived below from typed composition and the EMK sign relations. No Hilbert space, positive pairing, physical time, spectral theorem or physical metric is a primitive input. This is a theorem about a specified native family and readout, not a claim that every divergent equation has thereby been solved.

## 0. Data, identities, and the meaning of recognition convergence

Let K_Sigma be the completed characteristic-zero cut field used in RKF; all executable coefficients are in its exact rational subfield. The internal EMK algebra is presented by

    R^2=-1,   K^2=1,   KR=-RK.

Its normal basis is 1,R,K,RK. Put L=KR. Then L^2=1; with the native source dagger R^dagger=-R and K^dagger=K, L^dagger=L. These are native algebra identities, not a choice of an external metric.

The independent seam algebra has two generators S,T with

    TS=1,    ST is NOT identified with 1.

Declare S,T to commute with the internal coefficient algebra. Assign charges +1,-1 to S,T. Its normal words are S^i T^j, i,j>=0. The finite presentation, including the cross commutations, is terminating and confluent; the supplied compiler also checks its overlaps. All rule coefficients have absolute gauge one. Thus WC1 from the canonical workbench supplies a normal-word mass completion with unit letter weights when that completion is needed.

Define the recognition aperture p=1-ST. Native multiplication gives

    p^2=p,    pS=0,    Tp=0.

The aperture is nonzero: on the algebraic module freely spanned by e_0,e_1,..., let S e_h=e_(h+1), T e_0=0 and T e_(h+1)=e_h. Then p e_0=e_0. This module construction requires no pairing. The identity TS=1 and failure of ST=1 hold on it.

For b,c>=0 define B=bR, C=cK, q=bc, and the declared linear excursion operator

    H = B S + C T.

This family, its amplitudes and half-line memory geometry are inputs. They are not claimed to follow uniquely from the framework's earliest primitives or to be a gravitational source.

There are three different limits:

1. the full series sum_n H^n in a native word-mass completion;
2. the boundary moment series sum_n pH^n p;
3. the boundary corner of finite-aperture inverses, with aperture size tending to infinity.

Their convergence is not equivalent. An aperture-limit response is not silently called a full inverse or an infinite stationary state. It does not claim invariance under every imaginable regulator or observation map.

## RR1. Exact first-return law, with multiplication order retained

Adjoin a central formal variable z that counts pairs of excursions; it is not a clock. Odd powers of H have zero p-to-p corner. Define Q_n by

    p H^(2n) p = Q_n p,    Q_0=1.

Then the formal response F(z)=sum_(n>=0) Q_n z^n satisfies

    F = 1 + z C F B F,                                      (1)
    Q_n = sum_(j=0)^(n-1) C Q_j B Q_(n-1-j).                 (2)

**Proof.** In a normal seam word S^i T^j, sandwiching by p annihilates every word except the identity. Equivalently, in the algebraic stack module a returning word never crosses below height zero. A nonempty return decomposes uniquely into an initial matched T ... S excursion and a subsequent return, reading the product from left to right. Its internal coefficient is C Q_j B Q_(n-1-j), in that order. Summing over the possible interior length proves (2). Equation (1) follows coefficientwise. The same argument is available using the direct action on the freely generated stack states; no probabilistic interpretation is used. Uniqueness of the formal solution with F(0)=1 follows recursively because the coefficient of degree n uses only lower degrees. QED.

For general coefficients the sign and order cannot be replaced by a scalar norm. In particular the two length-four histories have coefficients C^2B^2 and CBCB. They may cancel in the chosen return target while remaining different, nonzero tagged histories.

## RR2. All-order anticommuting cancellation

This statement holds in any unital associative cut algebra with BC=-CB. Put X=CB. Then

    C X^j B = (-1)^j X^(j+1).

By (2), Q_n is a scalar multiple of X^n. If a(x) is its scalar generating series, (1) becomes

    a(x)=1+x a(-x)a(x).

Replacing x by -x and adding gives a(x)+a(-x)=2. Writing a=1+d yields

    d=x(1-d^2).

Consequently, with Cat_m=(2m)!/(m!(m+1)!),

    Q_(2m)=0                     for m>=1,
    Q_(2m+1)=(-1)^m Cat_m X^(2m+1).                         (3)

**Proof of the coefficient formula.** The recurrence Cat_0=1 and Cat_(m+1)=sum_(j=0)^m Cat_j Cat_(m-j) verifies d=sum_m (-1)^m Cat_m x^(2m+1) in the last equation. Its formal uniqueness gives (3). The relation C X^j=(-1)^j X^j C proves the preceding reduction. QED.

For the EMK family, X=qL and L^2=1, so

    F(z)=1+d(qz)L,
    d(u)=u-u^3+2u^5-5u^7+14u^9-... .                       (4)

The scalar coefficient majorant converges for |u|<1/2. The ratio of successive absolute terms tends to 4u^2, so the terms fail to tend to zero for |u|>1/2. No claim of divergence is made at the boundary from this strict ratio test.

At b=2,c=3/5, q=6/5, the recognized moment series therefore diverges at z=1. Moreover the full H^n contains the unique charge-n term B^n S^n, of native mass 2^n. Hence the full Neumann series cannot converge in the unit-weight word-mass completion either. This is actual term divergence, not merely failure of a sufficient norm estimate.

## RA1. Native finite apertures and an all-coupling inverse theorem

Let p_h=S^h p T^h. Direct multiplication gives p_h p_j=0 for h!=j and p_h^2=p_h. The finite aperture is P_N=sum_(h=0)^N p_h, with compressed operator H_N=P_N H P_N. Its native block coordinates have B on the lower neighboring diagonal and C on the upper one. Compression introduces the top boundary defect; one must not impose TS=1 at that finite top boundary.

Consider A_N=1_(P_N)-H_N. Define polynomials

    C_0(x)=C_1(x)=1,
    C_k(x)=C_(k-1)(x)+x C_(k-2)(x)   (k>=2).

These C_k are continuants, not the Catalan numbers Cat_m.

**Theorem.** For every finite q>=0 and k>=0, A_(2k) is invertible in its finite native block algebra and

    p A_(2k)^-1 p = F_k p,
    F_k = 1+d_k L,
    d_0=0,
    d_k=q C_(k-1)(q^2)/C_k(q^2)   (k>=1).                  (5)

In particular

    d_(k+1)=q/(1+q d_k).                                   (6)

**Proof.** When b>0, B is algebraically invertible. In the finite block module use the diagonal change of variables x_h=B^h y_h. The lower neighboring coefficient becomes 1 and the upper coefficient in row h becomes (-1)^h X, with X=CB=qL. All coefficients now lie in the commutative subalgebra generated by X. This is an algebraic similarity, not a unitary or norm-preserving claim.

For a tridiagonal chain of length m, its determinant D_m in that commutative algebra obeys

    D_0=D_1=1,
    D_m=D_(m-1)-(-1)^(m-2)X D_(m-2).

Induction eliminates the alternating step and gives

    D_(2k+1)=C_k(X^2)=C_k(q^2)1.

Every coefficient of C_k is nonnegative and its constant is 1, so this determinant is a nonzero positive radial scalar for every q>=0. The adjugate identity therefore constructs an inverse over the commutative coefficient algebra, and the finite similarity transports it back. The cofactor for the first diagonal block is C_k(X^2)+X C_(k-1)(X^2), which yields (5). Equation (6) follows from the continuant recurrence. For k=0 the inverse is 1. If b=0 or c=0, the chain is triangular with diagonal 1, q=0 and the same formula follows directly. QED.

This result does not claim that every aperture is nonsingular. At b=c=1, the height-one chain is singular whereas the height-two chain is invertible. The even apertures form a specified cofinal refinement sequence that avoids these spurious finite poles.

## RA2. Exact recognition-Cauchy completion for every nonnegative q

Let f_q(x)=q/(1+qx), x>=0. Starting d_0=0 and d_(k+1)=f_q(d_k), consecutive values bracket a common limit:

    I_k=[min(d_k,d_(k+1)), max(d_k,d_(k+1))],
    I_(k+1) subset I_k.

**Theorem.** For every finite q>=0, their widths tend to zero and their unique limit d satisfies

    0<=d<1,
    d=q/(1+qd),
    d=q(1-d^2).                                           (7)

The boundary responses converge in the native finite-coefficient mass to

    F_infinity=1+dL.                                      (8)

**Proof.** The case q=0 is immediate. For q>0 the map f_q is continuous and decreasing, sending [0,q] into itself. The even subsequence increases and the odd subsequence decreases. They have finite limits l,u, satisfying l=f_q(u), u=f_q(l). These identities give l+qlu=q and u+qlu=q, hence l=u. Their common value is the unique nonnegative root of qd^2+d-q=0, so d<1. Completeness here is only the already established radial completion and the finite coefficient span {1,L}. It does not require convergence of a full infinite operator. QED.

**Exact enclosure.** Continuant identities, or subtraction of (6) at consecutive steps, give

    width(I_k)=q^(2k+1)/(C_k(q^2) C_(k+1)(q^2)).            (9)

Thus midpoint d_hat has absolute error at most width(I_k)/2. Since M(L)=1 in the declared EMK normal-word gauge, the same bound controls M((1+d_hat L)-F_infinity). The executable solver uses exact rational recurrences and this enclosure. It does not evaluate a floating-point square root or use the desired answer as a stopping rule.

**Boundary-class independence.** For any finite nonnegative radial seed x, f_q(x) is in [0,q]. Therefore f_q^k(x) belongs to I_(k-1) for k>=1 and converges to the same d. This is robustness within a stated boundary-response class. It is not regulator independence for arbitrary negative/complex boundary conditions. For example x=-1/q makes the denominator vanish and lies outside the admitted class.

## RA3. A nonlinear recognized law derived from a linear operator

In this example the nonlinear equation is not chosen as a phenomenological ansatz. The primitive operator H is linear; the boundary response law is a consequence of ordered excursions and refinement. Indeed

    C(1+dL)B=q(L-d),
    C(1+dL)B(1+dL)=q(1-d^2)L.

Equations (7) and (8) verify F_infinity=1+C F_infinity B F_infinity exactly. If one erases the anticommutation and replaces the two coefficients by commuting positive scalars with product q, the corresponding law is f=1+qf^2, not (7). At q=6/5 its discriminant 1-4q is negative, so it has no finite real solution. The native sign is doing mathematical work; the change is not a relabelled scalar norm.

The pair b=2,c=3/5 gives q=6/5 and the exact recognized answer

    d=2/3,   F_infinity=1+(2/3)KR=1-(2/3)RK.

The full-series, unsigned-Catalan and paired-moment strict convergence gates all fail here; both moment series actually diverge as explained in RR2. The finite even-aperture response nevertheless has the convergent rational enclosure of RA2.

This is not an infinite inverse existence theorem. An inconsistent or nonconvergent global source equation must not be reported as solved merely because one target converges. The target here is explicitly defined as the even-aperture inverse corner, and its boundary class is declared.

## RC1. Strong-return selection of a native internal aperture

Let

    Q(q)=(1+d(q)L)/2,    Q_+=(1+L)/2.

The internal aperture Q_+ is already algebraically definable because L^2=1. The result here is its **selection by the response limit**, not creation of an idempotent from no premises.

From (7), for q>0,

    Q(q)^2-Q(q)=-(d(q)/(4q))1,
    M(Q(q)^2-Q(q))<=1/(4q).

Also d(q) tends to 1 as q tends to infinity, so Q(q) tends to Q_+. Reversing the native internal orientation L selects the complementary aperture instead. No probability interpretation, Born rule, external inner product or physical strong-coupling law is inferred.

## RC2. The cutoff and coupling limits do not commute

Finite aperture response Q_k(q)=(1+d_k(q)L)/2 need not itself be idempotent or positive. From the leading terms of the continuants, at fixed m>=1,

    d_(2m)(q) ~ m/q              as q -> infinity,
    d_(2m+1)(q) ~ q/(m+1)        as q -> infinity.

Hence taking q to infinity at a fixed cutoff does not give the selected cut Q_+. The recognition completion must control how cutoff grows with coupling.

**Theorem (joint-limit bound).** For every q>0 and integer k>=1,

    |d_k(q)-d(q)| <= 2q/k,
    M(Q_k(q)-Q_+) <= q/k+1/(4q).                           (10)

Consequently any joint refinement with q -> infinity and k/q -> infinity selects Q_+. A sufficient explicit choice is k=ceil(q^2) as q grows. The implementation uses the much sharper exact intervals (9); (10) is a simple uniform theorem, not the recommended numerical tolerance estimator.

**Proof.** The continuant roots can be written using d as lambda_+=1/(1-d^2), lambda_-=-d^2/(1-d^2). Substitution into their recurrence gives

    d_k=d [1-(-d^2)^k]/[1-(-d^2)^(k+1)].

This identity is also checked by induction from (6), so no spectral argument is needed. Therefore

    |d_k-d| <= 2 d^(2k)/(1-d^(2k+2)).

The positive quadratic root satisfies d<=u=2q/(1+2q). Bernoulli's finite binomial inequality gives

    u^(-2k)=(1+1/(2q))^(2k)>=1+k/q,
    u^(2k)<=q/(q+k).

Replacing d by u and bounding the denominator below by 1-u^(2k) proves |d_k-d|<=2q/k. Finally (7) gives 1-d=d/[q(1+d)]<=1/(2q). Since M(L)=1,

    M(Q_k-Q_+)=|d_k-1|/2 <= q/k+1/(4q).

QED.

## Recognition and information boundaries

Zero Q_(2m) in RR2 is cancellation of a target, not absence of its constituent paths. For n=2 the nested coefficient is -q^2 and the serial coefficient is +q^2; a tagged two-channel observation distinguishes them although their sum vanishes. The engine retains this witness rather than interpreting the zero as deletion of native history.

The response depends on bc, not on b and c separately. It can identify that product from d=q(1-d^2), but cannot recover both amplitudes without a further observer. As d approaches 1, inversion q=d/(1-d^2) becomes ill-conditioned; saturation must not be advertised as unlimited parameter sensitivity.

The half-line stack height in this model is not the full UGD integer winding ledger. The existing native path engine retains that separate ledger; this construction does not assert that a net height or a total response reconstructs every intermediate history.

## Lineage and what is a breakthrough candidate

The source inputs are native RKF T48/T55 (EMK relations), the declared typed cut/observer architecture, and the canonical Pāṇinian compiler. WC1 and WC3-WC7 are the preceding completion/response route. No private historical source is imported.

The mathematical advance **relative to the current workbench** is the derived all-coupling graded-aperture response, its exact rational error certificate, and the quantitative coupling/cutoff selection law (10). It reaches a target regime outside both earlier whole-operator convergence gates and the target's own moment-series radius. These are proposed and proved here for this family, with independent finite tests and source pins.

Catalan recursions, noncommutative quadratic equations, continuants, and analytic continuation are established mathematical methods. External priority for their combination here has not been established by the limited literature check. In particular Berenstein and Retakh's *Noncommutative Catalan numbers* (arXiv:1708.03316) and Miana and Romero's *Catalan generating functions for bounded operators* (arXiv:2401.16415; Annals of Functional Analysis 14, 69, 2023) provide relevant prior method families. They are comparisons, not primitive-space hypotheses used in these proofs.

A broader theorem for non-EMK couplings, nonstationary memory, arbitrary boundary classes, or a physical quantum-gravity observable remains a research task. Nothing here identifies physical curvature, derives a metric, or solves quantum gravity. Finite verification does not replace the written all-order arguments or external review.
