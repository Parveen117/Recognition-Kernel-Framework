# SE33: joint readings and nonlinear counting calculus

12 October 2026. Owner: Monty.

This continues SE32 on P=direct-sum_(n>=0) R p_n, R=Q[Lambda].
Lambda is central and constant. The counting actions Xp_n=p_(n+1),
Dp_n=n p_(n-1) and the separately typed cut are retained. RH and
curvature are deferred.

Coordinate nulls written as 0 below are derived additive neutrals in
their stated modules. The separately typed symbol mathsf0_cut denotes
the cut operation; it is not identified with those neutral elements.

The new objects are joint responses to labelled inputs and polynomial
operations built from those responses. The proofs use finite expansion
and counting actions; no analytic derivative, metric, clock or contraction
theorem is assumed. Existing normed nonlinear results keep their settings.

**Certification is the observer reading decoded for its target.** The
archive includes joint responses, diagonal/order repair and a nonlinear
inverse decoded from a saved kernel bank. Finite banks certify their
stated input sectors; general results have the written proofs below.

## 1. Theorem 1: multi-input reading calculus

For a positive arity k, prescribe a finite output y_(i_1,...,i_k) in P
for every ordered tuple of nonnegative count indices. There is a unique
R-multilinear map T:P^k->P with these basis readings:

\[
 \boxed{T(v_1,\ldots,v_k)=
 \sum_{i_1,\ldots,i_k}
 (v_1)_{i_1}\cdots(v_k)_{i_k}\,y_{i_1,\ldots,i_k}.}
 \tag{SE33.1}
\]

Every evaluation is finite because each input has finite support. A bank
on a finite Cartesian basis grid determines T on the corresponding
product of finite counting sectors, without a global count-order bound.
Compatible banks exhaust the full action. Eventual agreement on every
finite grid defines a separated complete reading space.

Joint composition is adaptive: after inner maps A_1,...,A_k have
returned finite states w_1,...,w_k, request T on the Cartesian product
of their recorded count supports and use (SE33.1). Repeated substitution
builds finite trees of compatible operations. Disjoint labelled input
blocks give a multilinear composite; reusing an input may give a
nonlinear diagonal map. These are different types.

**Proof.** Multilinearity forces (SE33.1); finite support makes its right
side well-defined and multilinear. This proves existence and uniqueness.
A reading-Cauchy sequence assigns each tuple an eventual finite output,
giving completeness; a differing tuple separates maps. Expand the read
inner states in the counting basis to obtain composition. All sums are
finite, so successive expansions yield the same coefficient products
for each parenthesization of a fixed tree. QED.

Two distinct joint operations are the counting formula product
mu(p_i,p_j)=p_(i+j), reproducing SE30's transported product, and matching:

\[
 M(p_i,p_j)=
 \begin{cases}p_i&i=j,\\0&i\ne j.\end{cases}
 \tag{SE33.2}
\]

Their extensions follow from (SE33.1). Neither identifies every product
with concatenation, quantity multiplication or operator composition.

## 2. Theorem 2: diagonal blindness and ordered recovery

For bilinear T, put q(v)=T(v,v) and split by **input order**:

\[
 T_s(u,v)=\frac{T(u,v)+T(v,u)}2,\qquad
 T_a(u,v)=\frac{T(u,v)-T(v,u)}2.
\]

Then

\[
 T_s(u,v)=\frac{q(u+v)-q(u)-q(v)}2,
 \tag{SE33.3}
\]
\[
 \boxed{T(u,v)=
 \frac{q(u+v)-q(u)-q(v)+r(u,v)}2,\quad
 r(u,v)=T(u,v)-T(v,u).}
 \tag{SE33.4}
\]

All diagonal readings determine exactly the symmetric part. The kernel
of diagonal observation on bilinear maps is precisely the antisymmetric
maps. The ordered-difference reading r repairs the missing part; it is
independent information, not inferable from the diagonal alone.

For symmetric k-linear T and the specified homogeneous diagonal
q_k(v)=T(v,...,v),

\[
 \boxed{T(v_1,\ldots,v_k)=\frac1{k!}
 \sum_{S\subseteq\{1,\ldots,k\}}(-1)^{k-|S|}
 q_k\left(\sum_{i\in S}v_i\right).}
 \tag{SE33.5}
\]

For general k-linear T this recovers its permutation average. The
arity and homogeneous component are specified; the formula does not
identify an arbitrary mixed-degree unknown function.

**Proof.** Expand q(u+v) to obtain (SE33.3)--(SE33.4). A zero diagonal
implies T(u,v)=-T(v,u); conversely antisymmetry gives 2T(v,v)=0.
For (SE33.5), expand into ordered k-tuples of input labels. A term
using a proper subset J has coefficient
sum_(S containing J)(-1)^(k-|S|)=0, by pairing subsets differing in an
unused label. The surviving terms use every label once: k! terms,
equal under symmetry. Without symmetry they sum to the permutation
average. Rational factorials are units in R. QED.

For example,

\[
 T(p_i,p_j)=p_{i+j}+\Lambda(i-j)p_0.
 \tag{SE33.6}
\]

Its diagonal agrees with mu for every state. The ordered readings on
(p_1,p_2) and (p_2,p_1) are p_3-Lambda p_0 and p_3+Lambda p_0. Their
difference supplies the missing unit layer. This is algebraic order
memory; no physical quadrant or orientation is inferred.

## 3. Theorem 3: nonlinear response rules by finite expansion

A polynomial counting operation has a supplied finite description

\[
 F(v)=c+\sum_{r=1}^{d}T_r(v,\ldots,v),
 \tag{SE33.7}
\]

with R-multilinear finite-output kernels. Replacing a kernel by its
permutation average leaves F unchanged. Composing finite polynomial
operations gives another such operation, of degree at most the product
of their degree bounds. Each finite input has finite output; its output
count degree need not equal its input degree.

For a central formal parameter t define

\[
 \delta F_v[h]=[t]F(v+t h).
 \tag{SE33.8}
\]

For symmetric kernels this equals sum_r r T_r(v,...,v,h). Define the
jth mixed response as the coefficient of t_1...t_j in
F(v+sum_i t_i h_i). It is symmetric and multilinear in its j directions:

\[
 F(v+h)=\sum_{j=0}^{d}\frac1{j!}
        \delta^jF_v[h,\ldots,h],\qquad \delta^0F_v=F(v).
 \tag{SE33.9}
\]

For polynomial operations F,G,

\[
 \boxed{\delta(G\circ F)_v[h]
       =\delta G_{F(v)}[\delta F_v[h]].}
 \tag{SE33.10}
\]

For a fixed bilinear response B, the product rule preserves both slots:

\[
 \delta\{B(F,G)\}_v[h]
 =B(\delta F_v[h],G(v))+B(F(v),\delta G_v[h]).
 \tag{SE33.11}
\]

With an unsymmetric kernel, replacing these terms by twice one term
generally changes the answer.

**Proof.** Multilinearly expand (SE33.7). Choosing one h slot yields
(SE33.8). Choosing j distinct slots gives the jth mixed response and
its j! multiplicity in (SE33.9). In G(F(v+t h)), first t-degree terms
choose one first-degree inner response and constant inner responses
elsewhere, proving the chain rule. Expanding both bilinear slots gives
(SE33.11). Distributive expansion also proves closure under composition.
All coefficients use finite sums; no limit is taken. QED.

A response polynomial of declared t-degree at most d is also determined
by d+1 distinct rational t-readings. The polynomials

\[
 \ell_i(t)=\prod_{j\ne i}\frac{t-t_j}{t_i-t_j}
\]

interpolate those values. Their difference from the response has degree
at most d and vanishes at every node, so each of its finitely many
counting/unit coordinates vanishes. Denominators are rational units.
This implements [t] by finite readings. The degree bound comes from
the constructed operation, not from assuming samples reveal all
unread higher terms.

## 4. Theorem 4: joint operations descend through the unit cut

Use SE32's quotient Q_q:P->overline P_q, retaining unit coefficients
modulo Lambda^(q+1). Every R-multilinear T descends uniquely to an
R_q-multilinear map T_q satisfying

\[
 T_q(Q_qv_1,\ldots,Q_qv_k)=Q_q T(v_1,\ldots,v_k).
 \tag{SE33.12}
\]

Hence every polynomial operation F descends to F_q. Joint composition,
diagonal/order decomposition, finite polarization and response
coefficients commute with retaining these unit layers:

\[
 (G\circ F)_q=G_q\circ F_q,\qquad
 (\delta F)_q=\delta(F_q).
 \tag{SE33.13}
\]

**Proof.** Replacing one input by v+Lambda^(q+1)w changes a multilinear
response by a multiple of Lambda^(q+1). Replacing the slots successively
proves well-definedness and uniqueness. Every stated operation uses
finite sums, central coefficient products and rational factorials,
which commute with this quotient. QED.

The degree-zero formula operation is the typed cut
\(\mathsf0_{\rm cut}:F\mapsto F_0\). Unit degree and input order are
separate labels: retaining one does not recover information lost in
the other. SE30's degree-one count-preserving cut n Lambda->n u
remains a different operation with its own target.

## 5. Theorem 5: exact nonlinear inversion by descending readings

Let H(v)=sum_(r=1)^d T_r(v,...,v), d>=2 allowed, with no constant term.
Suppose each basis kernel reading is supported strictly below
**every** input index:

\[
 [p_k]T_r(p_{i_1},\ldots,p_{i_r})\ne0
 \quad\Longrightarrow\quad k<\min(i_1,\ldots,i_r).
 \tag{SE33.14}
\]

This observable kernel property makes H_k(v) depend only on coordinates
v_i with i>k. For F(v)=v-H(v), each y in P_m has a unique solution in P_m:

\[
 \boxed{v_m=y_m,\qquad
 v_k=y_k+H_k\left(\sum_{i=k+1}^{m}v_i p_i\right),
 \quad k=m-1,\ldots,0.}
 \tag{SE33.15}
\]

The finite-sector inverses agree on overlaps and give a bijection
G=F^(-1):P->P. The kth inverse coordinate on P_m has total degree
at most d^(m-k). There need not be a global degree bound: G is locally
polynomial on finite sectors.

Unit cuts preserve the inverse recursion. If v=G(y), put L_v=delta H_v.
It strictly lowers counting degree, so its linear response is also exact:

\[
 \boxed{\delta G_y=(I-L_v)^{-1}=\sum_{j=0}^{m}L_v^j
        \quad\hbox{on }P_m.}
 \tag{SE33.16}
\]

**Proof.** The top coordinate of F(v) is v_m. Once coordinates above
k are determined, the kth equation uniquely forces (SE33.15), since
no unresolved lower coordinate occurs in it. Descending induction
proves existence, uniqueness and F(G(y))=y; applying uniqueness to
y=F(v) gives G(F(v))=v. If y has no higher coordinates, the same
descent assigns zero to every higher solution coordinate, proving
compatibility and global uniqueness among finite states. Each step
uses monomials with at most d already recovered factors, each of degree
at most d^(m-k-1), proving the degree bound. Unit reduction preserves
the recursion. In delta H_v, every output index is below the varied
input's index, so L_v strictly lowers. The finite-sector chain rule
and SE32's finite inverse sum prove (SE33.16). QED.

### Generated example from count matching

Let N=XD and S=(N+I)^(-1)D. SE32 supplies the inverse count-profile
of N+I; thus S p_i=p_(i-1) for i>=1 and S p_0 is null. With
phi(i)=1+Lambda i and the matching M from (SE33.2), define

\[
 K=S F_\phi M,\qquad
 K(p_i,p_j)=
 \begin{cases}(1+\Lambda i)p_{i-1}&i=j\ge1,\\0&\text{otherwise}.\end{cases}
 \tag{SE33.17}
\]

Its nonlinear map F(v)=v-K(v,v) is inverted by

\[
 \boxed{v_m=y_m,\qquad
 v_k=y_k+(1+\Lambda(k+1))v_{k+1}^{\,2}.}
 \tag{SE33.18}
\]

For y=p_3 the saved response is

\[
 v_3=1,\quad v_2=1+3\Lambda,\quad
 v_1=(1+2\Lambda)(1+3\Lambda)^2,\quad
 v_0=(1+\Lambda)(1+2\Lambda)^2(1+3\Lambda)^4.
 \tag{SE33.19}
\]

The degree-zero cut still has this nonlinear cascade. On y=t p_m,
its p_0 response has t-degree 2^m and a nonnull unit-polynomial
coefficient, so the global inverse has no bounded polynomial degree.

### Output-degree lowering alone is insufficient

For H(v)=v_0 v_1 p_0, one has H(P_m) contained in P_(m-1) for m>=1
and H(P_0)=0. But its output depends on v_0 itself. The equation
v-H(v)=p_0+p_1 forces v_1=1 and then v_0-v_0=1, impossible. This
kernel violates (SE33.14). The missing dependency is visible in the
joint reading, not supplied by an external certification rule. Mere
decrease of output degree does not prove generic nonlinear invertibility.

## 6. Result and boundary

The construction now has multilinear banks, adaptive joint composition,
input-order recovery, finite polynomial response rules and a generated
nonlinear inverse with an exact linear response. The inverse can have
unbounded global degree while each finite input is fully decoded.

These extend this framework's counting construction. Finite multilinear
expansion, polarization and triangular inversion are not claimed as
unprecedented mechanisms. Their analytic counterparts are not premises
here. No noisy-data stability, arbitrary nonlinear invertibility,
physical sector mapping, RH result or curvature theorem is claimed.

See [scope](SE33_SCOPE.md), [sources](SE33_SOURCE_RECORD.md),
[pins](SE33_SOURCE_PINS.json),
[application](../../proof_lab/lambda_joint_readings.cjs) and
[saved readings](../../proof_lab/LAMBDA_JOINT_READINGS_RESULT.json).

