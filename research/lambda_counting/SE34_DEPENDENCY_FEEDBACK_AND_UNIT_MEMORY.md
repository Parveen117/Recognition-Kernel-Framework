# SE34 development: dependency, nonlinear feedback and unit-memory lifting

12 October 2026. Owner: Monty.

**Status: development draft with written derivations. Observer-reading
certification is deferred at the user's request.** No new executable
certificate, source-pin manifest, replay archive or verification PASS
is issued in this stage. The SE33 reading certificates remain unchanged.

This continues [SE33](SE33_JOINT_READINGS_AND_NONLINEAR_COUNTING.md).
The immediate advance is to release its fixed counting-index order:
dependencies can be ordered differently, and actual feedback cycles
can be solved through successive unit layers when the cut operation
has an available inverse. The residual supplies the next correction.
A second update doubles the order of the retained exact information.

## 1. Objects before algorithms

Keep the central constant marked unit Lambda, the rational coefficient
ring R=Q[Lambda], and the finite counting module

\[
 P=\bigoplus_{n\geq0}R p_n,\qquad
 P_{\mathbb Q}=\bigoplus_{n\geq0}\mathbb Q p_n.
 \tag{SE34.1}
\]

The p_n are the existing counting-basis labels. They do not impose a
mandatory processing order. Zero-as-cut remains a separately typed
operation. Any 0 in a coefficient identity below denotes the derived
additive neutral of its stated carrier.

For a finite label set U, write P_U for its coordinate sector. Call
an operation **locally polynomial with finite output** if, on each
P_U, its output lies in some finite P_V and its coordinates there
are supplied polynomials over R in the finitely many input coordinates.
Different U may have different degree bounds and output sets V.

This includes every SE33 finite-arity polynomial operation, every
SE32 finite-column linear action, and SE33's nonlinear inverse: its
degree may grow with the input sector, but each sector still has a
finite polynomial description. Compositions remain in this class,
since the first operation supplies a finite output sector for the next.
All equalities between such operations mean polynomial identities on
each finite input sector, so that coefficient substitutions are lawful.

Use the existing typed retained-memory cut

\[
 Q_q:P\longrightarrow P/\Lambda^{q+1}P,\qquad q\geq0.
 \tag{SE34.2}
\]

The compatible family of these cuts defines a further carrier:

\[
 \widehat P=\varprojlim_q P/\Lambda^{q+1}P
 =\left\{\sum_{r\geq0}\Lambda^r v_r:
                  v_r\in P_{\mathbb Q}\right\}.
 \tag{SE34.3}
\]

Each v_r has finite counting support. There need not be one finite
support containing every v_r. Thus this carrier is generally larger
than the direct sum of Q[[Lambda]] p_n: that direct sum would impose
one finite count-support set for the entire series.

This completion retains unit layers, not infinite numerical sums at
a chosen nonzero value of Lambda. Lambda remains central and constant;
no physical clock or numerical limit Lambda->0 is introduced. The cut
Q_0 extracts the degree-zero member as an operation on coefficients.

**Why every admitted operation extends.** To calculate its output
through unit degree q, take the input through degree q. That input
has finite count support, so its finite polynomial description applies.
If two inputs agree through degree q, expansion of a monomial shows
their outputs also agree through degree q: each difference contains at
least one differing input factor. Consequently the calculation is
independent of higher input layers. It defines a unique compatible
extension to the tower. Every finite requested output layer is still
a finite counting state.

We write E=O(Lambda^r) to mean exactly that Q_(r-1)E is null,
or equivalently that its unit coefficients below r vanish. This is
an algebraic divisibility statement, not a numerical error estimate.

## 2. Theorem 1: dependency order replaces counting order

Work first in a specified finite sector with s labels. Let

\[
 F(x)=x-H(x)
 \tag{SE34.4}
\]

be polynomial there. Draw j->i when a surviving monomial of H_i
depends on x_j, after collecting equal monomials. Constants need no
incoming edge. A joint bank with labelled slots gives a sufficient
dependency graph; symmetrization and cancellation can remove edges
when the target is the diagonal operation.

**Theorem.** If this graph has no directed cycle, F has a polynomial
inverse over R. Solve coordinates in any order which puts every
parent before its dependent coordinate:

\[
 x_i=y_i+H_i(\hbox{already recovered parent coordinates}).
 \tag{SE34.5}
\]

All valid orders give the same inverse. The statement is preserved
under arbitrary permutations of the counting labels.

**Derivation.** A finite acyclic graph has a vertex with no incoming
edge: otherwise following predecessors would eventually repeat a
vertex and form a cycle. Remove such vertices successively. At each
step the displayed equation fixes one coordinate using previously
fixed values; constants are already known. This constructs polynomial
coordinates and proves uniqueness by the same induction. Substituting
the construction gives F(G(y))=y; uniqueness applied to F(x) gives
G(F(x))=x. Relabelling transports the equations and the graph together.
No numerical comparison between label values occurs.

For labels 0,2,5, for example,

\[
 H_0=0,\quad H_5=(1+\Lambda)x_0^2,\quad
 H_2=x_5x_0.
\]

The recovery order is 0,5,2, and

\[
 x_0=y_0,\quad
 x_5=y_5+(1+\Lambda)y_0^2,\quad
 x_2=y_2+x_5y_0.
 \tag{SE34.6}
\]

This includes a dependency from a smaller count label to a larger one.
SE33's k<min(input indices) condition is a special supplied ordering.

The finite-sector qualification matters. An infinite acyclic graph
can contain an endless dependency chain and need not preserve finite
support under inversion. For instance I-X on P has no finite-support
inverse image of p_0. The unit-memory construction below provides a
different carrier when such a continuation is intended.

## 3. Theorem 2: feedback cycles with positive unit memory

Remain in a finite closed sector with s labels. Collect the coordinate
polynomials of H. For each present dependency j->i, give its edge
weight w_ij equal to the least Lambda-degree of any nonzero monomial
coefficient of H_i containing x_j. These are nonnegative integers.
The graph of edges of weight zero is the dependency graph at the cut.

For a directed walk, add its edge weights. Repeated vertices are
allowed; feedback is represented by actual walks around a cycle.

**Theorem.** Suppose every directed cycle has positive total weight,
equivalently the zero-weight graph is acyclic. On the retained
unit quotient through degree q, the iteration

\[
 x^{(n+1)}=y+H(x^{(n)})
 \tag{SE34.7}
\]

reaches the same exact fixed point from any starting state after at
most

\[
 N=s(q+1)
 \tag{SE34.8}
\]

updates. It therefore gives a two-sided polynomial inverse of I-H
on that quotient. Its inverses commute with passing to shallower
unit cuts, and define a unique inverse on the compatible unit tower.

A sharper bound is 1+L_q, where L_q is the maximum length of a directed
walk of total edge weight at most q; include the length-zero walk.

**Derivation.** For a monomial, expand the difference at x and z by
changing one factor at a time. Each term contains a coordinate
difference x_j-z_j multiplied by the original coefficient, so passage
along j->i adds at least w_ij to its unit order. Iterating this identity
shows that a difference after n updates is a sum of terms indexed by
length-n dependency walks, with at least the total walk weight.

Any length-s walk contains a repeated vertex. The intervening closed
walk contains a directed cycle of positive integer weight, so the
whole length-s walk has weight at least one. Partition a length
s(q+1) walk into q+1 such blocks: its weight is at least q+1.
Every resulting difference therefore vanishes under Q_q.

Apply this to the two seeds x^(0) and x^(1). After N updates their
iterates agree, giving x^(N)=x^(N+1). Apply it to two fixed points
to prove uniqueness. Thus each target y has a unique source. The
finite iteration is polynomial in y if the chosen seed is polynomial,
and uniqueness gives both inverse identities and compatibility with
cuts. For the sharper bound, length L_q+1 already forces total
weight greater than q. The preceding block argument ensures L_q
is finite.

There is also an exact linear response at the recovered state x.
Let J=delta H_x, using SE33's coefficient-response operation. Its
entries obey the same edge divisibilities, hence J^N=0 after Q_q.
Consequently

\[
 \delta G_y=(I-J)^{-1}=\sum_{j=0}^{N-1}J^j
 \quad\pmod{\Lambda^{q+1}}.
 \tag{SE34.9}
\]

Finite geometric multiplication verifies the inverse. The chain rule
identifies it as the inverse response.

This replaces "cycles are excluded" by a precise statement: cycles
may feed information into higher retained unit layers. It says
nothing about convergence of (SE34.7) after substituting a nonzero
numerical unit value.

### A two-label cycle that SE33 did not cover

On labels 0 and 2, take

\[
 F(x_0,x_2)=(x_0-x_2^2,\ x_2-\Lambda x_0).
 \tag{SE34.10}
\]

There is a weight-zero edge 2->0 and a weight-one return edge 0->2.
The graph has a cycle, and one edge raises the count label, but its
cut graph is acyclic. For target (a,b), set c=a+b^2. Direct coefficient
substitution gives

\[
 \begin{aligned}
 x_0={}&c+2bc\Lambda+(4b^2c+c^2)\Lambda^2\\
       &+(8b^3c+6bc^2)\Lambda^3+O(\Lambda^4),\\
 x_2={}&b+c\Lambda+2bc\Lambda^2
                +(4b^2c+c^2)\Lambda^3+O(\Lambda^4).
 \end{aligned}
 \tag{SE34.11}
\]

Indeed x_2=b+Lambda x_0 and
x_0=c+2b Lambda x_0+Lambda^2 x_0^2 determine each successive
coefficient. Both expressions solve the retained equations exactly
through degree three.

At the cut the inverse is already nonlinear:
(x_0,x_2)=(a+b^2,b). The next layers record repeated returns around
the cycle, rather than forcing the cycle to disappear.

## 4. Theorem 3: lift an available cut inverse through arbitrary nonlinear layers

The graph condition is sufficient but not necessary. For example
H_0(x)=2x has a zero-weight self-cycle, yet F_0(x)=-x has the explicit
inverse -y. Solving an available cut operation first is more general
than demanding an acyclic cut graph.

Let F:P->P be locally polynomial with finite output. Write its
coefficient expansion as

\[
 F=F_0+\Lambda B,
 \tag{SE34.12}
\]

where F_0 consists of the degree-zero coefficients, extended
coefficientwise from P_Q. Suppose a locally polynomial finite-output
operation G_0 is supplied with

\[
 F_0G_0=G_0F_0=I.
 \tag{SE34.13}
\]

These are composition identities, not an inference from a nonzero
Jacobian determinant. SE33 and Theorem 1 supply concrete families
of such cut inverses.

**Theorem.** F has a unique two-sided inverse G on the unit-memory
completion P-hat. Each Q_q G is calculated by finitely many
polynomial operations on every finite input sector. Starting with

\[
 x^{(0)}=G_0(y),\qquad
 x^{(n+1)}=G_0\!\left(y-\Lambda B(x^{(n)})\right),
 \tag{SE34.14}
\]

the nth iterate agrees with G(y) through unit degree n:

\[
 x^{(n)}-G(y)=O(\Lambda^{n+1}).
 \tag{SE34.15}
\]

In particular, q updates from the initial cut-inverse response suffice
for the exact retained target Q_q G(y). The output count support may
grow with q. No single global degree or count-support bound is needed.

**Derivation.** Every locally polynomial operation preserves congruence
modulo Lambda^r, by the monomial-difference argument in section 1.
The map on the right of (SE34.14) therefore improves agreement by one
unit layer:

\[
 x-z=O(\Lambda^r)\ \Longrightarrow\
 \Phi_y(x)-\Phi_y(z)=O(\Lambda^{r+1}).
 \tag{SE34.16}
\]

The first update differs from x^(0) by O(Lambda), since its argument
differs from y by O(Lambda). Successive updates then differ by
O(Lambda^(n+1)). Each coefficient stabilizes after finitely many
updates; these finite-support coefficients define x in P-hat.
Continuity of polynomial substitution on each retained quotient
gives x=Phi_y(x), equivalent to F(x)=y using (SE34.13).

Every other fixed point has the same degree-zero response G_0(y_0).
Repeated use of (SE34.16) makes it agree at every unit layer, proving
uniqueness. Applying that uniqueness to y=F(z) gives G(F(z))=z;
the construction gives F(G(y))=y. The same argument proves (SE34.15).
All statements can instead be carried out on each finite quotient,
where stabilization is exact, and then assembled by compatibility.

On a fixed finite coordinate sector with polynomial F and polynomial
G_0, this has a useful exact converse: F is a polynomial automorphism
over every Q[Lambda]/(Lambda^(q+1)) precisely when F_0 is a polynomial
automorphism over Q. Necessity is the q=0 case; the preceding finite
iteration proves sufficiency. This is not a theorem that every map
with invertible linearization is a global polynomial automorphism.

### New support can be retained, not silently truncated

For the existing raising action X, take F=I-Lambda X. Its cut is I,
so the theorem yields

\[
 G(p_0)=\sum_{r\geq0}\Lambda^r p_r,\qquad
 Q_qG(p_0)=\sum_{r=0}^{q}\Lambda^r p_r.
 \tag{SE34.17}
\]

Multiplication by I-Lambda X leaves only
p_0-Lambda^(q+1)p_(q+1), which is exactly p_0 at the retained cut.
The full response belongs to P-hat and not to P. This is why the
new carrier was declared before the inverse.

### A nonlinear self-return and its counted coefficients

For one coordinate,

\[
 F(x)=x-\Lambda x^2,\qquad y=1.
\]

Let x=sum_(n>=0)c_n Lambda^n. Its cut response is c_0=1 and the
remaining equation gives

\[
 c_n=\sum_{a+b=n-1}c_a c_b,\quad n\geq1.
 \tag{SE34.18}
\]

Hence

\[
 x=1+\Lambda+2\Lambda^2+5\Lambda^3+14\Lambda^4+\cdots.
 \tag{SE34.19}
\]

The products count the two branches of a return. This recurrence is
already present in the programme's R1/R2 return work; its appearance
here is a specialization, not a new claim about those numbers.
For general y its nth coefficient is c_n y^(n+1).
Every retained quotient is solved by a finite polynomial inverse.

Even the linear example F(x)=(1-Lambda)x shows the boundary between
carriers: the formal inverse is 1+Lambda+Lambda^2+..., while assigning
the numerical value Lambda=1 gives a null map. A compatible tower
is not an all-numerical-unit invertibility theorem.

## 5. Theorem 4: turn the residual into the next reading, then double the order

Let y be the target, x_* its formal inverse response, and
x_0=G_0(y_0) its degree-zero source. Define the cut linear response

\[
 A_0=\delta F_0|_{x_0},\qquad
 A_0^{-1}=\delta G_0|_{y_0}.
 \tag{SE34.20}
\]

SE33's chain rule applied to both inverse identities proves the
displayed inverse relation, including its multiplication order.
These are finite-output linear operations on each finite input,
extended to unit memory.

### One new layer from one residual coefficient

Suppose x agrees with x_* through degree r-1, with r>=1, and let

\[
 e_r=[\Lambda^r]\{y-F(x)\}.
\]

Then

\[
 \boxed{x_{\rm new}=x+\Lambda^r A_0^{-1}e_r}
 \tag{SE34.21}
\]

agrees through degree r. No previously recovered coefficient changes.

**Derivation.** Finite polynomial expansion gives

\[
 F(x+\Lambda^r h)
   =F(x)+\Lambda^r A_0h+O(\Lambda^{r+1}).
\]

Terms with at least two changed inputs have degree at least 2r>=r+1;
the degree-zero part of the first response is A_0. Choosing
h=A_0^{-1}e_r cancels exactly the next residual coefficient.
Uniqueness from Theorem 3 identifies the new coefficient with x_*.

This gives a precise meaning to "error carries information" for this
construction: the residual's next unit coefficient, transported by
the cut response inverse, is exactly the missing source coefficient.
It does not turn arbitrary unmodelled measurement noise into truth.

### A correction that doubles the known order

Suppose y-F(x)=O(Lambda^r), with r>=1. Set

\[
 A=\delta F|_x,\qquad E=A-A_0,\qquad C=A_0^{-1}E.
\]

Since E raises unit order by at least one, on Q_q the exact inverse is

\[
 \boxed{A^{-1}=
 \left(\sum_{j=0}^{q}(-C)^j\right)A_0^{-1}.}
 \tag{SE34.22}
\]

The order of these operator factors is essential. Applying

\[
 \boxed{x_{\rm new}=x+A^{-1}\{y-F(x)\}}
 \tag{SE34.23}
\]

leaves residual O(Lambda^(2r)). Its source error has the same order.

**Derivation.** A=A_0(I+C), and C^(q+1) is null in Q_q even when
C changes counting support. Finite geometric multiplication on both
sides proves (SE34.22). Let h=A^{-1}(y-F(x)); then h=O(Lambda^r).
The finite response expansion from SE33 gives

\[
 F(x+h)=F(x)+Ah+\hbox{terms containing at least two }h.
\]

The first two terms equal y, while every remaining term has unit
degree at least 2r. The inverse map preserves congruence, so this
residual order also implies x_new-x_*=O(Lambda^(2r)).

Starting at G_0(y), the residual is divisible by Lambda. After k such
corrections it is divisible by Lambda^(2^k). Thus a retained target
through degree q needs at most ceil(log_2(q+1)) corrections, with
zero corrections for q=0. This counts outer correction steps; each
step still includes response evaluation and the finite inverse action.
It is not a computational complexity estimate independent of support
size, polynomial degree or coefficient size.

For x-Lambda x^2=1, start x=1. The first correction is

\[
 h=\frac{\Lambda}{1-2\Lambda}
   =\Lambda+2\Lambda^2+4\Lambda^3+\cdots.
\]

After cutting at degree three, the new state is
1+Lambda+2Lambda^2+4Lambda^3 with residual Lambda^3. The next
correction supplies one additional Lambda^3, producing
1+Lambda+2Lambda^2+5Lambda^3. The derivation makes no numerical
division at a singular chosen value: the denominator here has the
invertible cut coefficient 1.

## 6. Frame transport and the remaining singular cut

Let U and V be supplied locally polynomial finite-output changes of
input and output coordinates, each with an inverse and no unit
dependence. Define

\[
 \widetilde F=V\circ F\circ U^{-1}.
\]

Its cut inverse is U composed with G_0 composed with V^(-1).
Uniqueness of the lifted solution gives

\[
 \widetilde G=U\circ G\circ V^{-1},\qquad
 Q_q\widetilde G=
 Q_q(U\circ G\circ V^{-1}).
 \tag{SE34.24}
\]

This follows by substitution in the two inverse identities. A graph
drawn in new coordinates may have different edges, but the existence
of the supplied cut inverse and its transported lifted solution are
unchanged. The intrinsic target is the operation and its response;
one chosen count order is an algorithmic convenience.

What if the cut response really loses information? For F(x)=Lambda x,
the degree-zero operation is null. No formal solution exists for
target 1. For target Lambda z a formal solution is x=z, but at fixed
depth q the equation Lambda x=Lambda z determines x only modulo
Lambda^q: its highest retained layer is unread. This is visible
missing information, not a reason to declare a fictitious inverse.

Similarly, nonlinear cut maps with multiple inverse branches require
branch information before the present global inverse construction
applies. Theorems 3--4 extend an available cut inverse; they do not
manufacture it from a failed or incomplete reading.

## 7. Relation to work already present

| Earlier source actually read | Relation to this development |
| --- | --- |
| SE32 reading calculus | Finite-output linear actions, coefficient cuts and locally finite geometric inversion |
| SE33 joint/nonlinear calculus | Locally polynomial operations, response coefficients, chain rule and triangular inverse |
| Canonical AUTOMATIC_REGULAR_MODEL.md, WB1 | Finite acyclic graph ordering in a different target: normal-word languages |
| Canonical NATIVE_LAURENT_JET_REPAIR.md, NL1/NJ1--NJ3 | Formal unit towers and retained jet-memory modules; a different linear quotient target |
| Canonical WEIGHTED_OPERATOR_COMPLETION.md, WC7 | Nonlinear contraction in a specified mass ball, with analytic bounds |
| research/recognition_return/THEOREM.md, RR1--RR2 | Ordered return coefficients and quadratic recurrence already present |
| research/recognition_return/r2/THEOREM.md, formal-return subsection | Coefficientwise uniqueness distinguished from numerical series convergence |

SE34's contribution within this workstream is the combined extension:
read dependency rather than demand a fixed numeric order; allow
positive-memory cycles; lift supplied nonlinear cut inverses on the
counting module's unit completion; decode each missing coefficient
from the residual; and accelerate recovery by doubling the unit order.

The proofs above are finite polynomial and composition arguments.
Triangular inversion, formal inverse lifting and the correction that
doubles order are established algebraic mechanisms; no priority claim
is made for them. Existing analytic contraction and return theorems
retain their own carriers and targets. They are comparison sources,
not imported premises replacing these derivations.

## 8. Development boundary and next work

This stage provides the derivations and worked examples. Certification,
an executable reading decoder, archived packets, source pins and replay
are deferred. The application and whole-engine verification suites were
not run for SE34; no earlier mismatch is repaired or reclassified.

The next mathematical target is a cut operation with unresolved fibres:
derive which extra joint readings separate its branches, then apply
the lifting construction to the recovered branch. That requires
declared target fibres, rather than choosing a branch merely because
its expansion is convenient.

No RH, Yang--Mills, curvature, numerical convergence at arbitrary
nonzero Lambda, noisy-data recovery or general singular-cut inverse
is claimed here. The [chapter index](INDEX.md) preserves the route
back to the already recorded SE30--SE33 developments.

