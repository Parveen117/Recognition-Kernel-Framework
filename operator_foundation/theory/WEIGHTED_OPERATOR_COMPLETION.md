# Weighted native operator completion and certified response calculus

**Monty Dabas | Operator mathematics development 0.5 | 26 September 2026**

## Purpose and source order

This chapter closes a specific gap between the existing Pāṇinian normal-form
algebra and the existing completion, resolvent and memory results. A presentation
may have infinitely many irreducible words, so the finite regular-matrix backend
cannot represent it completely. We construct a class of completed algebras
**directly from certified rewrite rules**, then obtain convergent functional
calculus, inverse and response certificates, and nonlinear stationary solutions
on that class. The infinite object is justified by the proofs below, not by
claiming a sufficiently large finite search is infinite verification.

The primitive data remain the completed cut field, typed algebraic composition,
declared relations, retained residue labels and recognition targets. No ordinary
Hilbert space, positive pairing, spectral measure, physical clock or spacetime
metric is a premise. A weight measures algebraic coefficient burden, not physical
mass. Weights and the operator/source family are explicit choices, not derived
physical laws.

Dependencies in this same folder are `PANINIAN_OPERATOR_COMPILER.md` (checked
monic presentations), `AUTOMATIC_REGULAR_MODEL.md` (finite/infinite word-language
separation), `02_COMPLETION_AND_MEMORY.md` N07-N10, and
`01_NATIVE_ALGEBRA.md` (observers and compression). Corrected native T50/T52/T54
remain predecessors, not new discoveries of this edition.

## WC1. A finite rule certificate constructs an infinite normed algebra

**Data.** Work first with one object and unit 1. Let K be the *completed*
cut-complex field with scalar gauge

    D(r+iota s)=|r|+|s|,   D(zw)<=D(z)D(w),   D(z^dagger)=D(z).

The executable coefficients lie in its exact rational subfield. Infinite limits
are taken in K, not incorrectly in the incomplete rational subfield. Because D
is a real norm, the completion below is described as a real Banach algebra with
bounded central K-action, not as a C*-algebra in this gauge.

Let G be a finite generator alphabet and let the monic rules

    u_r -> sum_v c_(r,v) v

strictly decrease a multiplicative well-order. Assume every overlap and inclusion
ambiguity is resolved as in the local compiler theorem. Thus irreducible words
I form a basis of the polynomial quotient, and its normal-form map NF is unique.
The current executable class uses the already checked degree-lex order. It does
not infer confluence from priority selection.

Assign strictly positive real weights w_g, and extend multiplicatively:

    w(1)=1,   w(g1...gk)=product_j w_(gj).

**Finite certificate (W).** For each defining rule require

    sum_v D(c_(r,v)) w(v) <= w(u_r).

For a polynomial f=sum a_u u define its raw mass sum D(a_u)w(u). For a normal
polynomial use the same formula on its irreducible coordinates and call it M_w.

**Theorem WC1.** Under (W):

1. NF is contractive from the raw word mass to normal-word mass.
2. M_w(ab)<=M_w(a)M_w(b) on the normal-form algebra.
3. B_w=l1(I,w;K), with multiplication extended from NF(ab), is a complete unital
   normed algebra. The norm of 1 is exactly 1, even when I is infinite.
4. The completed free-word algebra maps continuously onto B_w. Its kernel is
   exactly the **norm closure** of the algebraic ideal of the declared relations.
5. Left regular action on B_w is faithful, and its least admissible real action
   bound is exactly M_w(a):

       sup_(M_w(x)<=1) M_w(ax)=M_w(a).

**Proof.** A reduction of a term alpha p u_r q has replacement burden at most
D(alpha)w(p)w(u_r)w(q), by (W) and submultiplicativity of D. Combining equal words
can only lower this estimate. Termination therefore proves (1). The raw mass of
a product is at most the product of raw masses; normalize to obtain (2).

The space of absolutely weighted-summable normal coordinates is complete by
coordinatewise limits of Cauchy sequences and the usual finite-tail estimate.
Finite-support vectors are dense. Bound (2) makes products of Cauchy sequences
Cauchy and independent of their presentations. Associativity on the dense
polynomial subalgebra extends by continuity. The empty normal word is a unit
of mass 1, proving (3). This construction differs from total-entry kernel mass,
where an infinite diagonal unit has to be adjoined separately.

The contractive NF map extends from the complete free-word algebra. It fixes
normal vectors and remains multiplicative into the NF product by continuity.
Every defining relation maps to zero, so its closed ideal lies in the kernel.
Conversely, for f in the kernel choose finite f_n tending to f. Then
f_n-NF(f_n) belongs to the algebraic relation ideal and tends to f. This proves
(4). Finally submultiplicativity bounds regular action by M_w(a), while evaluation
on 1 attains M_w(a). The same evaluation proves faithfulness, giving (5). QED.

**What the certificate does not say.** Failure of (W) rejects these weights for
this completion, not the underlying native algebra. For example a relation
DX=XD+1 cannot satisfy (W) with multiplicative letter weights: the right side
has weight w_D w_X+1. This does not reject an unbounded differential realization
or a different topology. Different admitted weights can give genuinely different
completions. No weight-independent canonical topology is claimed.

## WC2. Native dagger, approximation, and functional calculus

**Dagger extension theorem.** Suppose a specified conjugate-linear involutive
anti-homomorphism already descends to the polynomial quotient. If
M_w(g^dagger)<=w_g on every generator, dagger extends isometrically to B_w.

**Proof.** Reverse each word and apply the generator inequalities and WC1 to
obtain M_w(a^dagger)<=M_w(a). Applying the same inequality to a^dagger proves the
reverse bound. Isometric continuity gives the extension. QED. There is no
assertion that this is a coordinate transpose or that a positive pairing exists.

**Product-tail theorem.** If M_w(a-a_n)<=epsilon_a and
M_w(b-b_n)<=epsilon_b, then

    M_w(ab-a_n b_n)
      <= epsilon_a M_w(b_n)+M_w(a_n)epsilon_b+epsilon_a epsilon_b.

**Proof.** Expand using a=a_n+delta_a and b=b_n+delta_b, retaining factor order,
and apply WC1 to the three error products. QED.

**Functional-calculus theorem.** If r>=M_w(a) and
sum_(n>=0) D(c_n)r^n is finite, then

    f(a)=sum_(n>=0) c_n a^n

exists in B_w and the mass error of its N-th partial sum is at most
sum_(n>N) D(c_n)r^n. Absolutely convergent scalar-series products are respected.
Assume the majorant converges at r+epsilon_0 for some epsilon_0>0. For
perturbations with M_w(h)<=epsilon<=epsilon_0, differentiation is noncommutative:

    Df(a)[h]=sum_(n>=1) c_n sum_(j=0)^(n-1) a^j h a^(n-1-j).

If the second-derivative majorant converges, the remainder is bounded by

    epsilon^2 sum_(n>=2) binomial(n,2) D(c_n)(r+epsilon)^(n-2).

**Proof.** Completeness and the summable scalar majorant give convergence.
Absolute convergence justifies regrouping Cauchy products. Expanding (a+h)^n,
the words with precisely one h give the derivative. Words with at least two h
have total mass bounded by the second-order scalar Taylor remainder of
(r+epsilon)^n, at most binomial(n,2)epsilon^2(r+epsilon)^(n-2). Summation proves
both the bound and differentiability. QED.

For exp(a), one entirely rational finite tail bound is

    r^(N+1)/(N+1)! * 1/(1-r/(N+2)),     provided r/(N+2)<1.

The successive omitted scalar terms have ratios at most r/(N+2). Failure of this
particular tail gate at a small N does not imply that exp(a) diverges.

## WC3. A posteriori two-sided inverse certification

Let a,x belong to a unital complete algebra of WC1, with x a proposed inverse.
Compute **both** residuals

    e_L=1-xa,   e_R=1-ax,
    q_L=M_w(e_L), q_R=M_w(e_R).

**Theorem WC3.** If q_L<1 and q_R<1, a is invertible, and

    K=min(M_w(x)/(1-q_L), M_w(x)/(1-q_R))

bounds M_w(a^-1). Moreover

    M_w(a^-1-x)
      <= min(M_w(x)q_L/(1-q_L), M_w(x)q_R/(1-q_R)).

**Proof.** Geometric convergence gives (1-e_L)^-1 and (1-e_R)^-1.
Then (1-e_L)^-1 x is a left inverse of a and x(1-e_R)^-1 is a right inverse.
A left inverse and a right inverse of the same element coincide by associativity.
Subtracting x from the two convergent series gives the error bounds. QED.

One residual is insufficient in a general infinite algebra. The confluent native
presentation TS=1, with no relation ST=1 and weights one, has T as a left inverse
of S but 1-ST!=0. Its normal-word mass is 2. The two-sided certificate correctly
refuses to promote that one-sided inverse. This is an algebraic control, not a
Hilbert-space argument.

For a=1-b and x_N=sum_(j=0)^N b^j both residuals equal b^(N+1). If M_w(b)<1,
the prior tail bound is M_w(b)^(N+1)/(1-M_w(b)). Alternatively, the exact reduced
mass of b^(N+1) may satisfy the a posteriori gate even when M_w(b)>=1. For example
b=5N with N^2=0 has mass 5 but x_1=1+5N is its exact inverse. Native T52 already
contains power sharpening; this edition makes it available on infinite
normal-word completions without a finite matrix representation.

## WC4. Resolvent sensitivity and an ordered response derivative

Suppose M_w(a^-1)<=K and M_w(h)<=epsilon with K epsilon<1.
Then a+h is invertible and

    M_w((a+h)^-1) <= K/(1-K epsilon),
    M_w((a+h)^-1-a^-1) <= K^2 epsilon/(1-K epsilon),
    M_w((a+h)^-1-a^-1+a^-1 h a^-1)
      <= K^3 epsilon^2/(1-K epsilon).

**Proof.** Factor a+h=a(1+a^-1 h). The geometric series for the second factor
converges. Its first two terms give a^-1-a^-1 h a^-1, in that order. Bound the
remaining products with WC1. QED.

Thus the derivative of the inverse map is h -> -a^-1 h a^-1. Substituting h as a
central scalar variation gives the local resolvent derivative already present
in N08. The noncentral formula is needed for actual changes of source/interaction
operators; replacing it by -a^-2 h generally changes the answer.

This is a bound inside the declared mass completion, not a physical uncertainty
estimate until a source/measurement map is bound to that mass.

## WC5. Eliminate hidden operators without erasing their source

In the two-block algebra over B_w consider

    A=[[a,b],[c,d]],             A [u;v]=[f;g].

Assume d is invertible and define

    S=a-b d^-1 c,               f_eff=f-b d^-1 g.

**Theorem WC5.** A is invertible exactly when S is invertible, and then

    u=S^-1 f_eff,               v=d^-1(g-cu).

Its inverse has blocks

    [[S^-1, -S^-1 b d^-1],
     [-d^-1 c S^-1, d^-1+d^-1 c S^-1 b d^-1]].

**Proof.** The exact factorization is

    A = [[1,b d^-1],[0,1]] diag(S,d) [[1,0],[d^-1 c,1]].

The triangular factors are invertible by changing the off-diagonal sign.
Multiply to verify the inverse and solve the hidden equation to obtain v.
Substitution into the visible equation gives f_eff. No commutations, pairing
or positivity are used. QED.

The term b d^-1 c is the returning-memory operator. The term b d^-1 g is the
**hidden-source dressing**. Retaining the first but forgetting the second can
change the problem when g is nonzero; dropping it is harmless only when
b d^-1 g=0.

**Nested-cut corollary.** Elimination of several hidden blocks in any order
with all required inverses present yields the same retained operator and dressed
source. This does not assert that all pivot orders are possible. To prove it,
solve the same invertible hidden subsystem for its unique hidden state and
substitute; sequential admissible block solves are substitutions into that same
system. This is a transitivity statement for elimination, not for an arbitrary
lossy observer.

## WC6. Certified response from imperfect hidden and visible solves

This is the integration theorem: finite exact certificates now control a
solution involving potentially infinite native operators.

Suppose WC3 certifies x as an approximation to d^-1, with

    M_w(d^-1-x)<=eta,           M_w(d^-1)<=K_d.

Compute finite/native approximations

    S_hat=a-bxc,                f_hat=f-bxg.

Suppose WC3 certifies y as an approximate inverse of S_hat and returns a bound
K_hat on M_w(S_hat^-1). Set

    delta=M_w(b) eta M_w(c),
    theta=K_hat delta.

If theta<1, let K_S=K_hat/(1-theta) and choose any computed u_hat. Then

    M_w(u-u_hat) <= K_S [
      M_w(S_hat u_hat-f_hat)
      + delta M_w(u_hat)
      + M_w(b) eta M_w(g)
    ].                                                     (WC6)

The three bracketed terms are separately the finite solver residual,
the hidden-memory operator error acting on u_hat, and the hidden-source error.
For v_hat=x(g-cu_hat),

    M_w(v-v_hat)
      <= eta M_w(g-cu_hat)+K_d M_w(c) M_w(u-u_hat).

**Proof.** WC1 gives M_w(S-S_hat)<=delta and
M_w(f_eff-f_hat)<=M_w(b)eta M_w(g). Apply WC4 to S_hat to obtain invertibility
of S and its bound K_S. The exact equation

    S(u-u_hat)=(f_eff-f_hat)+(f_hat-S_hat u_hat)+(S_hat-S)u_hat

gives WC6. Subtract the two hidden solutions and expand

    v-v_hat=(d^-1-x)(g-cu_hat)-d^-1 c(u-u_hat)

to obtain the final estimate. QED.

**Target transport.** Any separately justified bounded linear target L with
D(Lz)<=beta M_w(z) has output error at most beta times WC6. For an irreducible
word w, coefficient extraction has exact bound beta=1/w(w). A nonzero
coefficient can be certified when its computed scalar gauge exceeds this error.
The bound does not establish completeness of a physically chosen observer.

The software computes all finite residuals itself. It does not trust caller-
supplied PASS flags, inverse norms or zero-tail declarations.

## WC7. Nonlinear native recognition equations in a controlled ball

Let

    F(z)=b + sum_i l_i z r_i + sum_j a_j z b_j z c_j

in B_w. Define

    beta=M_w(b),
    ell=sum_i M_w(l_i)M_w(r_i),
    q=sum_j M_w(a_j)M_w(b_j)M_w(c_j).

Choose r>0 satisfying

    beta+ell r+q r^2 <= r,      kappa=ell+2q r < 1.

**Theorem WC7.** There is a unique z_* in the closed mass ball M_w(z)<=r with
F(z_*)=z_*. Every iterate from that ball converges to z_*. For any z_hat in the
ball,

    M_w(z_*-z_hat) <= M_w(F(z_hat)-z_hat)/(1-kappa).

**Proof.** WC1 gives the displayed ball-invariance bound. For two points x,y in
the ball, expand x b_j x-y b_j y=(x-y)b_j x+y b_j(x-y). Summation yields
M_w(F(x)-F(y))<=kappa M_w(x-y). Successive iteration differences therefore
have summable geometric tails; completeness gives a limit, and continuity
makes it a fixed point. Two fixed points in the ball have distance at most
kappa times their distance and so are equal. Comparing z_hat with z_* and
moving kappa M_w(z_*-z_hat) to the left proves the residual bound. QED.

This is local uniqueness in the certified ball, not global uniqueness or an
automatic solver for every nonlinear equation. It uses the framework's existing
contraction/tail discipline in the new completed operator algebra. The iteration
index is an algorithmic continuation label, not an external physical clock.

## Exact demonstrations and claim boundary

The infinite presentation YX=(1/2)XY has irreducible words X^iY^j and satisfies
(W) at unit weights. For b=(X+Y)/4, (1-b)^-1 exists in B_w. The N=8 geometric
approximation has 45 distinct normal monomials and a prior mass tail at most
1/256. The exact residual provides a stricter rational a posteriori bound;
its value is generated in `audit/WEIGHTED_COMPLETION_CERTIFICATE.json`.
The algebraic dagger X^dagger=Y, Y^dagger=X is compatible with these relations
and weights, but no positive faithful representation is inferred.

An independent EMK block solve checks WC6 against exact full-system solutions,
including nonzero hidden sources. A nonlinear EMK fixture checks the contraction
certificate and successive approximation bounds. Gate failures, one-sided
inverses, omitted source dressing, wrong derivative order and weight violations
have explicit controls. Finite tests validate calculations; the proofs, not
finite sampling, establish the infinite conclusions under the stated hypotheses.

This is a constructive synthesis/extension of this framework's toolchain, not a
claim of first discovery of norm completion, Neumann series, Schur elimination
or the contraction principle. External method references (not primitive-space
inputs): George M. Bergman, *The Diamond Lemma for Ring Theory* (1978), with the
author's corrections and acknowledgement of the Shirshov/Bokut lineage at
`https://math.berkeley.edu/~gbergman/papers/updates/diamond.html`; Genevieve Dusson,
Israel Michael Sigal and Benjamin Stamm, *The Feshbach-Schur map and perturbation
theory*, arXiv:2105.02058. The latter's self-adjoint spectral setting is not
assumed by the block-algebra proofs WC5-WC6.

Open next extensions: weights found by an algorithm rather than supplied;
multi-object completed categories; general unbounded-generator domains;
positive native representation selection where needed; certified spectral
separation beyond sufficient resolvent gates; and problem-selected physical
sources, distances, propagation and detector targets. The operator family and
weights must not be fitted retrospectively to manufacture a desired conclusion.
