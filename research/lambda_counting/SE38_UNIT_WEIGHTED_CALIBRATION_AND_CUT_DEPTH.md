# SE38: unit-weighted calibration and the exact memory depth

12 October 2026. Owner: Monty.

**Certified observer readings.** Five theorem groups below have written
derivations and worked examples. The [observer certificate](SE38_SCOPE.md)
decodes recorded relative and calibration readings for their stated
targets and passes 25 exact checks, including 8 negative controls,
against 156 source pins.

[SE37](SE37_TARGET_ALGEBRA_AND_CALIBRATION_MEMORY.md) closed the relative
observer for a particular matching of unit order and source degree. Its
counterexample x -> x+Lambda x^3 required more calibration than Lambda c.
Here that counterexample is repaired, and a finite calibration bank is
constructed for every finite polynomial action catalogue with affine cut
on a known finite counting sector.

There are two useful versions. Polynomial updates on one retained carrier
use a bank of weighted calibration monomials. The existing labelled unit
readings permit a second version using a calibration vector at a shallower
depth. For a relative reading beginning at unit order s and a nonlinear
action beginning at order w, its required calibration depth is q-w-s
when the requested output depth is q. A scalar example attains this bound.

Lambda remains the central marked unit. Zero names the typed cut; a null
coefficient or additive-neutral vector is a separately typed object.
RH and curvature remain deferred. No metric, physical clock or spectral
theorem is used to obtain the results below.

## 1. Carriers and acquired information

Work in a known finite counting sector with n coordinates and base ring
R=Q[Lambda]. Let c be an arbitrary known or recorded calibration state.
The relative reading is

\[
 \Delta=x-c.
 \tag{SE38.1}
\]

It is assumed already acquired or decoded from an available bank. This
stage does not infer the original source coordinates from a blind sensor.
The same construction can be applied to acquired observer coordinates
whose descended action has the polynomial form specified below.

Source and calibration undergo the same supplied action g_i. Their
relative update is g_i(c+Delta)-g_i(c), as derived in SE37. Only listed
actions are used; an inverse or an additional source probe is not assumed.

The retained coefficient carrier is

\[
 R_q=\mathbb Q[\Lambda]/(\Lambda^{q+1}),
 \qquad \pi_q:R[c]\longrightarrow R_q[c].
 \tag{SE38.2}
\]

The operator pi_q retains labelled unit coefficients through q. It is
the existing unit-memory cut, not evaluation of Lambda at a nonzero
numerical value. Polynomial identities are first derived in R[c,Delta]
and then passed to this declared cut where appropriate.

## 2. Theorem 1: finite monomial calibration algebra

For an integer D>=1 define

\[
 U_\alpha(c)=\Lambda c^\alpha,
 \quad 1\leq|\alpha|\leq D,
 \qquad
 A_D=R[U_\alpha:1\leq|\alpha|\leq D]\subseteq R[c].
 \tag{SE38.3}
\]

These are finitely many recorded functions of the calibration, with

\[
 K_{n,D}=\binom{n+D}{D}-1
 \tag{SE38.4}
\]

displayed coordinates. D bounds total counting degree, without giving
the counting sector a geometric metric.

**Theorem.** A polynomial belongs to A_D exactly when every nonzero
monomial Lambda^r c^alpha in its collected expression satisfies

\[
 \boxed{|\alpha|\leq Dr.}
 \tag{SE38.5}
\]

Consequently membership and a polynomial expression in the U_alpha
have a direct finite construction from the collected monomials.

**Derivation.** Each generator has unit degree one and counting degree
at most D. A product of generators, multiplied by an element of R,
satisfies (SE38.5). Sums cannot create monomials outside that bound.

Conversely, take Lambda^r c^alpha satisfying the bound. If alpha is
null it is already a coefficient in R. Otherwise partition the
|alpha| labelled factors of c^alpha into

\[
 \ell=\lceil |\alpha|/D\rceil\leq r
\]

nonempty groups of size at most D. Let their multi-indices be
alpha_1,...,alpha_ell. Then

\[
 \Lambda^r c^\alpha
 =\Lambda^{r-\ell}
    U_{\alpha_1}\cdots U_{\alpha_\ell}.
 \tag{SE38.6}
\]

Every unit exponent is nonnegative. Applying this to each monomial
constructs the required expression, without division by Lambda.

The U_alpha are constrained readings, not independent free variables.
For example, with n=1 and D=2,

\[
 a=\Lambda c,\quad b=\Lambda c^2,
 \qquad a^2=\Lambda b.
 \tag{SE38.7}
\]

Different partitions in (SE38.6) give the same actual calibration
function. An update may use any of them, provided the lawful relations
are retained. No radical reduction of nilpotent unit relations is used.

## 3. Theorem 2: the degree/unit-order rule for closed calibration

Write a finite supplied catalogue, after collecting equal monomials, as

\[
 g_i(x)=A_i(\Lambda)x+b_i(\Lambda)
       +\sum_{r\geq1,\ |\alpha|\geq2}
            v_{i,r,\alpha}\Lambda^r x^\alpha,
 \tag{SE38.8}
\]

where the displayed sum is finite and v_(i,r,alpha) is a rational
output vector. Thus the cut action is affine. Coefficients of A_i,b_i
may themselves contain positive unit powers.

**Theorem.** The condition

\[
 \boxed{|\alpha|-1\leq Dr
   \quad\text{whenever }v_{i,r,\alpha}\ne0}
 \tag{SE38.9}
\]

is necessary and sufficient for every coefficient, in free Delta, of
g_i(c+Delta)-g_i(c) to belong to A_D. Under this condition, substitution
by every g_i also preserves A_D. There are therefore polynomial maps
Psi_i and F_i giving the closed relative observer

\[
 \boxed{U'=\Psi_i(U),\qquad
 \Delta'=F_i(\Delta,U).}
 \tag{SE38.10}
\]

The same finite tuple U and the same formulas work at every retained
unit depth. They compose in the actual order of any finite action word.

**Derivation of sufficiency for the relative reading.** Expand a
nonlinear monomial using the finite multivariable binomial rule:

\[
 (c+\Delta)^\alpha-c^\alpha
 =\sum_{0<\beta\leq\alpha}
      \binom{\alpha}{\beta}c^{\alpha-\beta}\Delta^\beta.
 \tag{SE38.11}
\]

Its calibration coefficient has total counting degree
|alpha-beta|<=|alpha|-1<=Dr. Theorem 1 puts it in A_D and gives its
explicit expression. The affine part contributes only A_i(Lambda)Delta.

**Derivation of necessity.** For an output component and an input
coordinate j, the coefficient of Delta_j is the polynomial partial
derivative of that output component at c. A collected monomial with
alpha_j>0 contributes the nonzero coefficient

\[
 \alpha_j v_{i,r,\alpha}\Lambda^r c^{\alpha-e_j}.
\]

For fixed j no distinct collected monomial gives the same pair of
unit and counting exponents. Since rational positive integers are
invertible, membership of this coefficient in A_D requires
|alpha|-1<=Dr. This proves necessity in the untruncated polynomial
carrier. At a fixed shallower cut, terms beyond its depth are invisible
and need not satisfy a condition for an all-depth presentation.

**Derivation of calibration closure.** For a generator U_alpha with
|alpha|<=D, substitute g_i(c) in Lambda c^alpha. In a resulting monomial,
let t be the total added unit degree from the selected action terms.
Each selected nonlinear term has counting degree at most one plus D
times its unit degree. Affine or constant terms satisfy the same bound.
Hence the resulting counting degree is at most

\[
 |\alpha|+Dt\leq D(1+t).
 \tag{SE38.12}
\]

The outer Lambda gives unit degree 1+t. Theorem 1 therefore expresses
every resulting monomial in the original generators. Substitution
preserves products and sums, so it preserves all of A_D. The formulas
(SE38.10) are obtained by this finite expansion and partition procedure.

### Every finite affine-cut polynomial catalogue is covered

If the nonlinear part is nonempty, choose

\[
 D_* =\max_{i,r,\alpha:v_{i,r,\alpha}\ne0}
             \left\lceil\frac{|\alpha|-1}{r}\right\rceil.
 \tag{SE38.13}
\]

It is finite and at least one. This gives a uniform nonlinear memory
bank with K_(n,D_*) coordinates. It is the smallest D for this family
of monomial banks satisfying the relative-coefficient criterion.
It is not a minimum among all possible observers or all decoder types.
If every action is affine, the relative update needs no calibration.

SE36's finite linear response bank can grow with q. Here finitely many
nonlinear coordinates carry the update uniformly in q. Their retained
coefficient content still grows with q; uniform coordinate count is
not finite information at infinite depth.

### Dependence on the counting frame

Let c'=S c+t with S invertible over Q and t a rational vector. Every
Lambda(c')^alpha of degree at most D is a linear combination of the
old U_beta and a known multiple of Lambda. The inverse affine change
gives the reverse containment. Thus A_D is the same algebra under
these affine counting-frame changes, and the observer updates transport
accordingly. No preferred calibration origin is selected. Arbitrary
nonlinear frame changes require their own degree and decoder analysis.

## 4. Theorem 3: an exact least bank for a monomial action

Take the scalar action

\[
 g(x)=x+h\Lambda^w x^{d+1},
 \quad h\in\mathbb Q\setminus\{0\},\quad w,d\geq1.
 \tag{SE38.14}
\]

Define u_j=Lambda^w c^j for j=1,...,d and
B_(w,d)=R[u_1,...,u_d]. The coefficient of Delta^k in the relative
increment, for k=1,...,d, contains exactly the corresponding nonconstant
calibration function h binom(d+1,k) u_(d+1-k), with the identity term
included when k=1. The last coefficient is h Lambda^w.

**Theorem.** B_(w,d) is the least R-algebra containing the calibration
coefficients of this relative update and preserved by g. It has the
closed polynomial formulas

\[
 \boxed{\begin{aligned}
 u_j'&=u_j(1+h u_d)^j,\qquad 1\leq j\leq d,\\
 \Delta'&=\Delta+
 h\sum_{k=1}^{d}\binom{d+1}{k}u_{d+1-k}\Delta^k
       +h\Lambda^w\Delta^{d+1}.
 \end{aligned}}
 \tag{SE38.15}
\]

Exactly d generators are required to generate this algebra over R.
The same algebra-generator minimum holds for its actual retained image
over R_q when q>=w. It concerns polynomial generators on that carrier,
not the minimum number of physical measurements or of typed coefficient
readings.

**Derivation.** Each u_j is a nonzero rational multiple of one of the
nonconstant increment coefficients. Any algebra containing those
coefficients must contain B_(w,d). Since g(c)=c(1+h u_d), substitution
gives the first line of (SE38.15); the binomial expansion gives the
second. Thus this required algebra is already action-preserved, which
proves leastness for every future relative increment.

For the generator count, remove the known c-independent part of each
proposed generator. Every remaining term begins at unit order at least
w. At the quotient retaining only through unit degree w, any product
of two such terms vanishes, because 2w>=w+1. The nonconstant leading
coefficients of polynomial expressions in k generators consequently
span at most k rational directions. But the d monomials

\[
 \Lambda^w c,\ldots,\Lambda^w c^d
 \quad\bmod\Lambda^{w+1}
\]

are linearly independent. Hence k>=d, and the displayed tuple attains
the bound. The same quotient is available at every depth q>=w. At
q<w the nonlinear action and all these memories disappear under the cut.

This statement does not prevent a larger information algebra from
having fewer generators. For example, for w=d=2 the least algebra is
R[Lambda^2 c,Lambda^2 c^2], with two polynomial generators. The larger
algebra R[gamma], gamma=Lambda c, has one: its functions include
Lambda gamma and gamma^2. Gamma itself is not in the least algebra.
Theorem 5 below gives a different compression using the already available
labelled coefficient readings instead of same-carrier polynomial maps.

### The cubic obstruction from SE37 is repaired

For g(x)=x+Lambda x^3, put a=Lambda c and b=Lambda c^2. Equations
(SE38.15) become

\[
 \boxed{\begin{aligned}
 a'&=a(1+b),\\
 b'&=b(1+b)^2,\\
 \Delta'&=(1+3b)\Delta+3a\Delta^2+\Lambda\Delta^3.
 \end{aligned}}
 \tag{SE38.16}
\]

They hold before truncation and preserve a^2=Lambda b. This supplies
the missing calibration coefficient Lambda c^2 without retaining c as
a cut-level coordinate. It is exact for every finite word of this action.

### One bank supports ordered quadratic and cubic actions

Supply both g_2(x)=x+Lambda x^2 and g_3(x)=x+Lambda x^3. The same (a,b)
supports g_3 by (SE38.16), and supports g_2 by

\[
 a'=a(1+a),\qquad b'=b(1+a)^2,\qquad
 \Delta'=(1+2a)\Delta+\Lambda\Delta^2.
 \tag{SE38.17}
\]

Order is retained. Direct expansion gives

\[
 g_3(g_2(x))-g_2(g_3(x))
   =\Lambda^2 x^4\pmod{\Lambda^3}.
\]

Subtracting the corresponding calibration outputs yields the difference
between the two relative readings:

\[
 \boxed{4ab\Delta+6\Lambda b\Delta^2+
              4\Lambda a\Delta^3+\Lambda^2\Delta^4
       \pmod{\Lambda^3}.}
 \tag{SE38.18}
\]

An effect absent at the first unit layer becomes visible at the second.
The same closed bank reads it; no commutation of the catalogue is assumed.
This is an ordered counting calculation, with no curvature claim.

## 5. Theorem 4: apply the cut to the actual memory algebra

There is a distinction between a displayed algebra presentation and the
unit degree of its actual readings. Define the induced filtration

\[
 F^{q+1}A_D=A_D\cap\Lambda^{q+1}R[c].
 \tag{SE38.19}
\]

**Theorem.** The actual retained memory algebra is

\[
 \boxed{A_{D,q}=\pi_q(A_D)
       \simeq A_D/F^{q+1}A_D.}
 \tag{SE38.20}
\]

It has a rational basis consisting of the distinct monomials
Lambda^r c^alpha with 0<=r<=q and |alpha|<=Dr, and hence

\[
 \boxed{\dim_{\mathbb Q} A_{D,q}
      =\sum_{r=0}^{q}\binom{n+Dr}{Dr}.}
 \tag{SE38.21}
\]

The action updates and relative readings of Theorem 2 commute with the
maps to every shallower retained depth. The quotient in (SE38.20) must
not be replaced without justification by A_D/Lambda^(q+1)A_D.

**Derivation.** The kernel of the restricted map pi_q on A_D is exactly
the intersection in (SE38.19). The monomials from Theorem 1 remain
independent in R_q[c] when r<=q, and all higher-r monomials vanish.
Counting their multi-indices gives (SE38.21). Polynomial substitution
does not lower unit order and Theorem 2 preserves A_D, so it preserves
this intersection filtration. It therefore descends to the retained
images, with the same formulas at compatible depths.

For the quotient distinction, take any nonconstant generator
U_alpha=Lambda c^alpha. It vanishes under the actual degree-zero cut,
but it does not lie in Lambda A_D: that would require c^alpha in A_D,
which violates (SE38.5) at unit degree zero. Thus the abstract class of
U_alpha in A_D/Lambda A_D is nonzero, while pi_0(U_alpha) is null.
More generally Lambda^q U_alpha lies in F^(q+1)A_D and need not lie in
Lambda^(q+1)A_D, by the same argument.

The actual cut retains coefficient constants at q=0 and removes all
these positive-unit calibration readings. It cannot be implemented by
forgetting the unit degree carried by a generator's definition. This
derives the correct quotient from the observer reading itself.

The dimension in (SE38.21) is the dimension of a polynomial-function
algebra, not the number of independent state measurements. Relations
among the displayed coordinates and between attainable values remain.
Their compatible all-depth presentation does not claim that one finite
packet contains an infinite tower of coefficient information.

## 6. Theorem 5: exact and sharp calibration depth from unit readings

The same-carrier polynomial condition in Theorem 3 is not a restriction
on all available native operations. SE30--SE32 already supply labelled
coefficient readings and cuts with explicitly retained targets. Those
readings give a second construction which needs fewer stored calibration
coordinates while changing their target depth.

Let the catalogue have a common positive lower unit order w for its
nonlinear terms:

\[
 g_i(x)=A_i(\Lambda)x+b_i(\Lambda)
                    +\Lambda^w H_i(\Lambda,x),\qquad w\geq1.
 \tag{SE38.22}
\]

The H_i are supplied polynomials. Suppose the acquired relative reading
satisfies Delta in Lambda^s R_q^n, with s>=0. This is a bound on its
labelled unit order, not a numerical smallness assumption. Put k=w+s.

For q>=k record

\[
 \gamma=\Lambda^k c\in\Lambda^k R_q^n.
 \tag{SE38.23}
\]

There is a typed coefficient-shift map

\[
 \begin{aligned}
 L_{k,q}:\Lambda^k R_q&\longrightarrow R_{q-k},\\
 \sum_{r=k}^{q}z_r\Lambda^r
   &\longmapsto\sum_{r=k}^{q}z_r\Lambda^{r-k}.
 \end{aligned}
 \tag{SE38.24}
\]

It is the inverse of the labelled module embedding R_(q-k) -> Lambda^k R_q
given by multiplication by Lambda^k. It is not an inverse of Lambda
on the whole R_q carrier. Its codomain records the lost depth; no
unavailable coefficient is recovered.

**Theorem.** Let h=L_(k,q)(gamma), componentwise, and let tilde h be
any lift of h to R_q^n. The joint update

\[
 \boxed{\begin{aligned}
 \gamma'&=\Lambda^k g_i(\widetilde h),\\
 \Delta'&=A_i(\Lambda)\Delta+
    \Lambda^w\{H_i(\Lambda,\widetilde h+\Delta)
                       -H_i(\Lambda,\widetilde h)\}
 \end{aligned}}
 \quad\text{in }R_q
 \tag{SE38.25}
\]

is independent of the lift and equals the actual update of
(Lambda^k c,x-c). It preserves Delta in Lambda^s R_q^n and thus works
for every future word without increasing the required calibration depth.
Only c through unit degree q-w-s is needed. If q<w+s, the nonlinear
relative contribution vanishes and no calibration is needed for the
relative update at that depth.

**Derivation.** The labelled map gives h=pi_(q-k)(c). Thus c-tilde h
has unit order at least q-k+1. Substitution into a polynomial preserves
this congruence, so multiplying by Lambda^k makes
g_i(c)-g_i(tilde h) vanish at depth q. This proves the first equation.

For the second, expand the mixed difference

\[
 H(c+\Delta)-H(c)-H(\widetilde h+\Delta)+H(\widetilde h).
 \tag{SE38.26}
\]

For each monomial, every surviving term contains at least one factor
from c-tilde h and at least one factor from Delta. To see this directly,
write c=tilde h+e and expand in the independent labelled increments
e and Delta: the two subtractions remove all terms missing either
increment. Its unit order is therefore at least q-k+1+s. The outer
Lambda^w increases that to

\[
 w+(q-k+1)+s=q+1.
\]

It vanishes in R_q, proving the second equation and lift independence.
Every term of any polynomial difference g(c+Delta)-g(c) contains a
factor from Delta, so unit order s is preserved by each action.
Induction gives the assertion for all future words. If q<w+s,
Lambda^w[H(c+Delta)-H(c)] already has order greater than q.

The construction commutes with retained cuts as long as the stored
bound s is used with its declared target depths. A deeper reading
can reveal additional coefficients; it is not reconstructed from a
shallower one. If a later relative reading has larger unit order,
its newly read order permits the calibration depth to be reduced again.

### Sharpness of the calibration-depth bound

For q>=w+s, take the scalar action g(x)=x+Lambda^w x^2 and the same
relative reading Delta=Lambda^s at two calibrations

\[
 c=0,\qquad d=\Lambda^{q-w-s}.
\]

They agree through every degree below q-w-s. Their next relative
readings differ by

\[
 2\Lambda^w(d-c)\Delta=2\Lambda^q\ne0\quad\text{in }R_q.
 \tag{SE38.27}
\]

Thus the last retained calibration coefficient in Theorem 5 can be
necessary. Dropping it fails for this action and target. This proves
sharpness of the uniform depth guarantee, not that every individual
action or target uses every coefficient in the bound.

### Cubic action with a typed shorter calibration record

For g(x)=x+Lambda x^3 and a general relative reading, use w=1,s=0.
At q>=1 the one scalar calibration packet gamma=Lambda c supplies
h=pi_(q-1)(c) through its labelled coefficients. Equation (SE38.25) is

\[
 \begin{aligned}
 \gamma'&=\Lambda\widetilde h+\Lambda^2\widetilde h^3,\\
 \Delta'&=\Delta+
       \Lambda(3\widetilde h^2\Delta
                    +3\widetilde h\Delta^2+\Delta^3).
 \end{aligned}
 \tag{SE38.28}
\]

This is a single calibration channel with q rational coefficients,
not one scalar of finite precision encoding arbitrary data. It also
does not contradict the two-generator statement for B_(1,2): the
decoder now uses a map to a shallower carrier and a lift-independent
formula, not a polynomial endomorphism in gamma on the original R_q.

At q=3 and with Delta beginning at unit order s=1, the required
calibration depth falls to one. The packet gamma=Lambda^2 c retains
only c_0 and c_1. Its omitted c_2 and c_3 cannot affect future relative
readings through depth three under the supplied catalogue. Theorem 5
proves this for every finite word, not just the first update.

## 7. Construction choices and what is actually retained

| Required operation | Retained calibration | Derived guarantee |
| --- | --- | --- |
| Uniform polynomial updates on one carrier | U_alpha=Lambda c^alpha, 1<=|alpha|<=D_* | Finite bank for every finite polynomial affine-cut catalogue |
| Least coefficient algebra for x+h Lambda^w x^(d+1) | u_j=Lambda^w c^j, 1<=j<=d | Exact least algebra; d same-carrier polynomial generators |
| Labelled coefficient readings, relative order s | gamma=Lambda^(w+s)c at depth q, decoded to depth q-w-s | Exact closed updates with a sharp uniform calibration-depth bound |

An absolute target can require calibration information that its relative
transport does not. For example, Delta alone with a shortened reference
does not reconstruct every coefficient of x=c+Delta. Such a target must
be added to the retained information using SE37's target-algebra rule.

The finite monomial construction gives an explicit sufficient bank.
Its generally least all-depth calibration subalgebra is not asserted to
be finitely generated merely because it sits inside A_D. The exact
least-algebra statement here is proved for the declared monomial family.

The depth law counts unit coefficients. It makes no claim about noisy
measurement, numerical conditioning, numerical convergence at nonzero
Lambda, or physical acquisition cost. A calibration known from its
definition can be computed; an unknown one must actually be supplied
by the stated readings.

## 8. Sources, status and continuation

| Source read | Role |
| --- | --- |
| [SE30](../../papers/rkf_completed_weil_endpoint/development/SE30_CONSTANT_LAMBDA_COUNTING_AND_CUT.md), section 3 | Typed coefficient cuts and marked retained targets |
| [SE31](../../papers/rkf_completed_weil_endpoint/development/SE31_COUNTING_OPERATOR_RECOVERY_AND_ORDERED_FLOW.md), sections 3--4 | Labelled unit-memory readings and ordered actions |
| [SE32](SE32_READING_COMPLETION_AND_COUNTING_CALCULUS.md), section 4 | Retained coefficient carriers and lawful descent |
| [SE33](SE33_JOINT_READINGS_AND_NONLINEAR_COUNTING.md) | Finite polynomial response and joint-increment expansion |
| [SE34](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) | Unit-order propagation through polynomial operations |
| [SE36](SE36_RESTRICTED_PROBES_AND_ACTION_CLOSURE.md) | Finite affine-cut polynomial action catalogues and available-bank scope |
| [SE37](SE37_TARGET_ALGEBRA_AND_CALIBRATION_MEMORY.md) | Relative calibration equation, target algebras and decoder distinctions |

The five theorem groups derive finite monomial memory, the exact
degree/unit-order criterion, least memory algebra for a monomial action,
the correct induced unit cut, and the sharp relative calibration-depth
law using labelled readings. All proofs use finite expansions, monomial
independence and the existing typed coefficient operations. No novelty
priority is claimed for those algebraic mechanisms.

This is an additive research derivation in the counting chapter. The
single shared operator engine remains in operator_foundation/. The
published SE34--SE37 observer certificates are preserved. The SE38
observer certificate is
[proof_lab/lambda_calibration_depth.cjs](../../proof_lab/lambda_calibration_depth.cjs)
with its read-only archive
[LAMBDA_CALIBRATION_DEPTH_RESULT.json](../../proof_lab/LAMBDA_CALIBRATION_DEPTH_RESULT.json),
[scope](SE38_SCOPE.md), [source record](SE38_SOURCE_RECORD.md) and
[pins](SE38_SOURCE_PINS.json). No application bound, RH eta, Yang--Mills
gap or curvature claim is changed.

A next development can apply the depth rule to a specified nonlinear
target rather than the entire relative coordinate, and derive when
newly read unit cancellations allow its observer memory to shrink.
