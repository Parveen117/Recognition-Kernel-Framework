# SE30 Constant-lambda counting and the cut operator

12 October 2026. Owner: Monty.

The construction order here is: one fixed unit, repetition, arithmetic,
number theory, a typed cut action, and then counting operators and formula
families. No curvature or source-sign calculation is used. The user's
notation **zero means the cut operator** is implemented as
\(\mathsf{0}_{\rm cut}\), with a stated domain and retained output.
It is never substituted as the scalar value that annihilates every unit.

The positive counting layer has no empty count, additive identity,
subtraction, origin on a number line, metric or geometric cut. Subsequent
algebraic completions are constructed explicitly. Their neutral element
is denoted \(e_+\), to keep it separate from the cut operator. Standard
coefficient and degree notation in the implementation is an adapter;
the executable's scalar zero is not the operator \(\mathsf{0}_{\rm cut}\).

## 1. Definition and Theorem 1: counting with a constant unit

Fix one marked indivisible token \(u_\lambda\). Lambda is a constant
unit label within this arithmetic, not a function of a coordinate. Let
\(\mathcal N_\lambda^+\) consist of nonempty finite strings of this one
token. A string with n tokens is denoted \([n]_\lambda\), or informally
\(n\lambda\). Integers in square brackets record repetition length;
they are not positions supplied on a pre-existing number line.

Define \(a\oplus b\) by concatenation. Define \(a\odot b\) by replacing
each token in a with the entire string b. Thus

\[
 [m]_\lambda\oplus[n]_\lambda=[m+n]_\lambda,\qquad
 [m]_\lambda\odot[n]_\lambda=[mn]_\lambda.
 \tag{SE30.1}
\]

**Theorem 1.** These operations are associative and commutative;
odot distributes over oplus; \([1]_\lambda\) is the multiplicative
unit. Addition and multiplication cancel. No additive identity lies
in this collection. The successor \(s(a)=a\oplus[1]_\lambda\) is
injective, and every object other than the unit is a successor.
Relabeling the fixed unit gives an isomorphism between any two such
counting systems.

**Proof.** There is exactly one string of each positive length. Two
concatenations have the same result exactly when their lengths agree.
Substitution lists one pair (token of a, token of b) for every output
token. Reassociation, exchanging the two factors, and distributing over
concatenation are bijections of these finite lists. Cancellation follows
by deleting equally long initial strings, and by cancelling equally
sized nonempty blocks. An additive identity would have to contribute
no token and is excluded. Removing the final token of a non-unit string
proves the successor assertion. Relabeling preserves both constructions.
QED.

These laws construct a positive counting arithmetic. They do not assert
that all native objects are strings of one kind or alter the existing
framework's primitive order. This is the requested counting subtheory;
its later cut adapter is defined in Section 3.

There are two distinct products when a scalar calibration is subsequently
chosen. If the reading of one token is a positive real a, then

\[
 \operatorname{read}_a([n]_\lambda)=na,\quad
 \operatorname{read}_a([m]\odot[n])=mna,\quad
 \operatorname{read}_a([m])\operatorname{read}_a([n])=mn a^2.
 \tag{SE30.2}
\]

The first product counts groups in one unit; the last multiplies measured
quantities and has two units. The count product is not defined by dividing
by the numerical reading a. It therefore needs no singular division at
the cut. The token and its numerical reading are separate typed data.

## 2. Theorem 2: arithmetic completion and number theory

The strict order is a<b when b=a oplus c for some positive count c.
Divisibility is a|b when b=a odot c. A prime is a non-unit count whose
only divisors are the unit and itself. These definitions require neither
subtraction nor an additive identity.

For later differences, form ordered pairs (a,b) of positive counts and
identify

\[
 (a,b)\sim(c,d)\quad\Longleftrightarrow\quad
 a\oplus d=c\oplus b.
 \tag{SE30.3}
\]

Pair addition is componentwise. Pair multiplication is

\[
 [(a,b)]\,[(c,d)]
 =[(a\odot c\oplus b\odot d,\ a\odot d\oplus b\odot c)].
 \tag{SE30.4}
\]

**Theorem 2.** These classes form the integer ring of count differences.
Every [(a,a)] is the same additive neutral class e_+; swapping a and b
gives the additive inverse. The positive counts embed by
a -> [(a oplus unit,unit)]. Positive ratios (a,b), identified by
a odot d=c odot b, give the positive rational arithmetic. These are
extensions of the counting system, not extra primitive counting tokens.

Every non-unit positive count factors uniquely into primes up to order.
There are infinitely many primes. Divisibility, primes, gcd and lcm
are preserved by a change of unit label and by the faithful degree-one
cut in Section 3, when the count product is retained.

**Proof.** Taking lengths, (SE30.3) is a+d=c+b. It is an equivalence
relation, and the integer difference a-b determines its class exactly.
The pair formulas realize addition and multiplication of these
differences, which proves independence of representatives and all ring
laws. In particular the neutral class is derived from equality of two
counts. It is an element, whereas the cut in Section 3 is a map; they
have different types. Cross multiplication proves the ratio statement.

For completeness, unique factorization follows within this constructed
integer arithmetic. A non-unit either is prime or splits into two
strictly smaller non-units; induction on length gives existence. To prove
Euclid's lemma, choose the least positive integer linear combination d
of two positive lengths a,b. Division with remainder shows that d divides
both: a nonempty remainder would be a smaller positive combination.
Every common divisor divides d, so d is their gcd and is a linear
combination. If a prime p does not divide a, this gcd is the unit; a
linear combination of p,a equals the unit. Multiplying by b proves
p|ab implies p|b. Removing one prime at a time proves uniqueness.
For any finite prime list, its product plus the unit has a prime divisor
outside that list. This proves infinitude. Gcd/lcm follow by minimum/maximum
prime exponents, or by the divisibility order. Unit relabeling and the
faithful cut preserve lengths and the two operations, hence these results.
QED.

This is a construction and transport of familiar number theory from the
counting law, not a new prime distribution or an RH proof. The statement
that the initial counting collection has no additive identity does not
claim that a full ring with additive inverses can lack a neutral class.
The latter has just been derived, without identifying it with a cut.

## 3. Theorem 3: zero as a cut operator that retains the unit

Here is a concrete cut realization. Let R be the constructed integer
ring, its rational extension, or a polynomial ring over that extension.
Let Lambda be a central formal constant, let A=R[Lambda], and let
I=(Lambda). A degree-d quantity is a **typed** pair (d,f), with f in
I^d. The degree records how many units a product carries. Introduce u
as the retained unit symbol in the target and define

\[
 \mathsf{0}_{{\rm cut},d}(f)
  :=[\Lambda^d]f\;u^d,
 \qquad f\in I^d.
 \tag{SE30.5}
\]

In this packet, writing a family "at lambda zero" means applying this
declared cut map to the declared degree. It is an operator application,
not an untyped replacement of a scalar by an operator inside a formula.

**Theorem 3.** The cut identifies I^(d+1) in I^d and retains its entire
degree-d quotient. This quotient is a free R-module with basis [Lambda^d].
It is the unique R-linear reading into R u^d that discards I^(d+1) and
sends the marked unit Lambda^d to u^d.
For f in I^d and g in I^e,

\[
 \begin{aligned}
 \mathsf{0}_{{\rm cut},d}(f+g')
   &=\mathsf{0}_{{\rm cut},d}(f)+\mathsf{0}_{{\rm cut},d}(g')
       &&(g'\in I^d),\\
 \mathsf{0}_{{\rm cut},d+e}(fg)
   &=\mathsf{0}_{{\rm cut},d}(f)
     \mathsf{0}_{{\rm cut},e}(g).
 \end{aligned}
 \tag{SE30.6}
\]

Choosing the marked representative a u^d -> a Lambda^d gives the
idempotent cut operator P_d f=([Lambda^d]f)Lambda^d. It fixes a nonempty
unit packet, so it is not the annihilating operator. In particular

\[
 \boxed{\mathsf{0}_{{\rm cut},1}(n\Lambda)=nu.}
 \tag{SE30.7}
\]

The target positive counts nu inherit addition and the count product
(mu) odot (nu)=(mn)u; this cut is a bijection of positive counting
arithmetics. Its quantity product instead lives in degree two:

\[
 \mathsf{0}_{{\rm cut},2}((m\Lambda)(n\Lambda))=mn u^2.
 \tag{SE30.8}
\]

**Proof.** Write f=Lambda^d(a+Lambda h). Its image is exactly a u^d,
independent of h; its kernel on I^d is I^(d+1), and every a u^d has
the displayed marked lift. Any reading with the stated conditions must
send this decomposition to a u^d, proving uniqueness. Reading and lifting twice has the same
effect as once, proving idempotence. The coefficient of degree d+e
in fg is the product of the leading coefficients because neither
factor has a lower-degree term. This proves (SE30.6). For counts,
the retained integer coefficient distinguishes all n and respects
(SE30.1). QED.

Equivalently, the graded quantity carrier is
direct-sum_d I^d/I^(d+1), with the product in (SE30.6). It retains all
unit degrees. Applying only the degree-one map to a degree-two product
would erase it and is a type error for quantity multiplication.
The coefficient-polynomial presentations (0,Lambda) and (1,Lambda)
have different types: the former is a varying coefficient in degree
zero; the latter is the marked counting unit. Dropping this degree
record confuses a vanishing numerical display with a surviving count.

A single cut retains its stated quotient, not every higher coefficient
of an arbitrary family. Full continuation memory requires the other
coefficient layers, as in the existing native Laurent/jet construction.
This is an explicit algebraic cut model with no Hilbert metric; no
uniqueness claim about every physical or TVSP cut is imposed.

## 4. Theorem 4: counting operators and regular formula transport

After the preceding completion, work in R=Q[Lambda,x], with Lambda
central and constant under changes of x. Define the step operator

\[
 E_\Lambda f(x)=f(x+\Lambda).
\]

The polynomial E_Lambda f-f has a factor Lambda. Define D_Lambda f
by **removing that formal factor**, rather than by dividing a numerical
reading at the cut:

\[
 E_\Lambda f-f=\Lambda D_\Lambda f,\qquad
 D_\Lambda x^n=
 \sum_{j=1}^{n}{n\choose j}x^{n-j}\Lambda^{j-1}.
 \tag{SE30.9}
\]

Set X_Lambda f=x f(x-Lambda). Let

\[
 p_{0,\Lambda}(x)=1,\qquad
 p_{n,\Lambda}(x)=x(x-\Lambda)\cdots(x-(n-1)\Lambda).
 \tag{SE30.10}
\]

For k>=n, p_(n,Lambda)(k Lambda) equals Lambda^n times the count of
ordered choices of n distinct tokens from k. The degree-n cut retains
that count times u^n. Thus the falling-factorial family is selected
by a counting operation, not by a curvature condition.

**Theorem 4.** The family satisfies

\[
 D_\Lambda p_{n,\Lambda}=n p_{n-1,\Lambda},\qquad
 X_\Lambda p_{n,\Lambda}=p_{n+1,\Lambda},\qquad
 [D_\Lambda,X_\Lambda]=I.
 \tag{SE30.11}
\]

The degree-zero cut on coefficient families gives

\[
 \mathsf{0}_{{\rm cut},0}(p_{n,\Lambda})=x^n,\qquad
 \mathsf{0}_{{\rm cut},0}(D_\Lambda f)
   =\partial_x\mathsf{0}_{{\rm cut},0}(f).
 \tag{SE30.12}
\]

Let U_Lambda be the Q[Lambda]-linear map x^n -> p_(n,Lambda).
It is invertible on polynomials, is the identity after the coefficient
cut, and transports differentiation and multiplication by x into
D_Lambda and X_Lambda respectively. Consequently every polynomial
operator identity transports by conjugation. Define a formula product

\[
 f\mathbin{\bullet_\Lambda}g
 :=U_\Lambda\big((U_\Lambda^{-1}f)(U_\Lambda^{-1}g)\big).
 \tag{SE30.13}
\]

It is associative, commutative and unital; D_Lambda is a derivation for
this product. At the coefficient cut it becomes ordinary polynomial
multiplication. For example x bullet_Lambda x=x^2-Lambda x.
This product of formulas is a separate type from the count product odot.

**Proof.** The binomial theorem proves divisibility and (SE30.9) for
monomials, hence all polynomials. Subtracting the two falling-factorial
products at x+Lambda and x leaves n Lambda p_(n-1,Lambda)(x).
The raising formula is immediate from the product. Acting on this basis
gives the commutator. The basis is monic and triangular by degree, so
its change-of-basis matrix has a polynomial inverse, without an inverse
of Lambda. This proves the conjugacies and (SE30.13); associativity
and the derivation law transport with them. The constant coefficients
in Lambda in (SE30.9)--(SE30.10) prove (SE30.12). QED.

The ordinary product still has its own exact rule

\[
 D_\Lambda(fg)=(D_\Lambda f)g+(E_\Lambda f)(D_\Lambda g),
 \qquad [D_\Lambda,M_x]=E_\Lambda.
 \tag{SE30.14}
\]

It follows by adding and subtracting f(x+Lambda)g(x) in the step
difference. Replacing E_Lambda by I before the cut would generally
be false. For example D_Lambda x^2=2x+Lambda, whose cut is 2x.
Applying the coefficient cut to E_Lambda-I before retaining its
first-degree response would erase the derivative information. The
graded cut and formal factor removal preserve that response.

The operator D_Lambda commutes with translations of x, so its definition
does not require a fixed geometric origin. The chosen raising operator
is a declared polynomial chart; changing x to x-b supplies the translated
one. This section constructs operators and their algebra, not curvature.

## 5. Theorem 5: exponential family generated by counting

Define a formal generating function, coefficient by coefficient, by

\[
 \mathcal E_\Lambda(x,t)=
 \sum_{n\ge0}p_{n,\Lambda}(x)\frac{t^n}{n!}
 \quad\hbox{in }\mathbb Q[\Lambda,x][[t]].
 \tag{SE30.15}
\]

**Theorem 5.** It is the unique formal series with initial coefficient
one satisfying

\[
 (1+\Lambda t)\partial_t\mathcal E_\Lambda=x\mathcal E_\Lambda,
 \qquad D_\Lambda\mathcal E_\Lambda=t\mathcal E_\Lambda.
 \tag{SE30.16}
\]

It has the equivalent regular formal expression

\[
 \mathcal E_\Lambda(x,t)
 =\exp\left(x\sum_{j\ge1}
       \frac{(-1)^{j-1}\Lambda^{j-1}t^j}{j}\right).
 \tag{SE30.17}
\]

For a nonzero numerical parameter in a compatible formal/analytic chart,
this is customarily written (1+lambda t)^(x/lambda). The series
(SE30.17), not numerical division by lambda, defines it at the cut:

\[
 \boxed{\mathsf{0}_{{\rm cut},0}(\mathcal E_\Lambda(x,t))
       =\exp(xt).}
 \tag{SE30.18}
\]

It obeys

\[
 \begin{aligned}
 \mathcal E_\Lambda(x+y,t)
   &=\mathcal E_\Lambda(x,t)\mathcal E_\Lambda(y,t),\\
 \mathcal E_\Lambda(x,s)\mathcal E_\Lambda(x,t)
   &=\mathcal E_\Lambda(x,s+t+\Lambda st).
 \end{aligned}
 \tag{SE30.19}
\]

The composition s plus_Lambda t=s+t+Lambda st is associative and
commutative; at the coefficient cut it becomes s+t.

**Proof.** The recurrence p_(n+1)=(x-n Lambda)p_n yields the first
equation of (SE30.16) and uniquely determines each next coefficient.
The lowering identity in Theorem 4 gives the second equation.
The exponent in (SE30.17) is a regular formal series with no negative
Lambda powers. Its t derivative is x/(1+Lambda t), so its exponential
has the same recurrence and initial coefficient. The coefficient cut
retains xt. The first addition law follows from the exponent being
linear in x. For the second, the formal logarithm of
(1+Lambda s)(1+Lambda t) is the sum of their formal logarithms, and
their product is 1+Lambda(s+t+Lambda st). Alternatively both sides
follow coefficientwise from the same formal identity. Expanding the
three-input composition gives s+t+r+Lambda(st+sr+tr)+Lambda^2 str
in either order. QED.

For example, the first terms are

\[
 1+xt+\frac{x^2-\Lambda x}{2}t^2+
 \frac{x^3-3\Lambda x^2+2\Lambda^2x}{6}t^3+\cdots.
\]

Only formal-series statements are needed here. Analytic evaluations
would additionally require convergence and branch choices. No blanket
claim about all classical equations, physical constants, or analytic
continuation is inferred from polynomial transport.

## 6. Result and next admissible use

There is now a fixed-unit positive arithmetic, a derived number theory,
an explicit non-annihilating cut operator, an operator algebra and a
regular lambda family of formulas. At the cut the marked counts survive,
while the degree-zero formula family yields its classical member.
The count layer and the chosen formula deformation have fully specified
products; neither secretly divides by an erased unit.

Curvature has not been developed or used at this stage. A later definition
may be built from declared operators and their composition, after its
carrier and target are fixed. The historical RH source and its eta bound
are unchanged; this arithmetic construction supplies no new RH sign.

See [scope](SE30_SCOPE.md), [sources](SE30_SOURCE_RECORD.md),
[pins](SE30_SOURCE_PINS.json),
[exact application](../../../proof_lab/endpoint_lambda_counting.cjs) and
[finite evidence](../../../proof_lab/ENDPOINT_LAMBDA_COUNTING_RESULT.json).
