# SE35 development: active joint readings and singular-cut repair

12 October 2026. Owner: Monty.

**Development draft. Certification remains deferred.** This stage
contains mathematical derivations and worked examples. It adds no
certificate packet, source-pin manifest, executable replay or PASS.

[SE34](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) lifted an available
cut inverse through unit memory. Here the raw cut response may have
several inverse branches, or even a singular linear response. We
construct additional observations of translated inputs, identify
exactly what they still cannot distinguish, and derive a polynomial
decoder for what they can distinguish. When they recover the whole
input, their completed cut operation is the identity, so SE34 applies.

The new ingredient is an observation protocol: the observer can
supply known labelled perturbations to the same unknown input and
read the resulting response. No extra information is inferred from
the original single reading alone.

## 1. Counting carrier and the active observation

Choose a known finite counting sector

\[
 V=\operatorname{span}_{\mathbb Q}\{p_{i_1},\ldots,p_{i_n}\},
 \qquad W=\operatorname{span}_{\mathbb Q}\{p_{j_1},\ldots,p_{j_m}\}.
 \tag{SE35.1}
\]

Its coefficient and joint operations are those of SE30--SE33. A
supplied polynomial response F:V->W has declared degree at most
d>=1 and symmetric multilinear components

\[
 F(x)=b+\sum_{r=1}^{d}T_r(x,\ldots,x).
 \tag{SE35.2}
\]

Zero components are allowed. The symmetric components reproduce
the polynomial diagonal; this does not recover an antisymmetric
part of an original ordered kernel that the diagonal already lost.

The operator description and degree bound are supplied. The unknown
is the input x. This is not simultaneous identification of an unknown
operation, unknown degree and unknown state from finitely many values.

Let c in V be a supplied observer calibration state. For known
perturbation h in V, record

\[
 {\cal A}_c(x;h)=F(x+h)-F(c+h).
 \tag{SE35.3}
\]

The second term is a calibration reading or a value calculated from
the supplied operation. The first requires access to x+h. A passive
observer restricted to F(x) has not thereby acquired these readings.

There is no distinguished c: changing it changes a known calibration
term. If only relative input is the target, the decoder reports x-c.
If an absolute coordinate x is requested, c must be known in that
same coordinate description.

Zero still names a typed cut operation in the framework. Nulls in
the polynomial and vector identities below are the separately
derived additive neutrals. The calibration c is not identified with
the cut, and need not be the neutral state.

## 2. Theorem 1: the exact blind directions of all translated readings

For each homogeneous component define the linear contraction bank

\[
 L_r v=\bigl(T_r(v,e_{a_1},\ldots,e_{a_{r-1}})\bigr)_
                    {1\leq a_1,\ldots,a_{r-1}\leq n},
 \tag{SE35.4}
\]

where e_a=p_(i_a), and L_1=T_1. Each W-valued entry has its
declared m scalar output coordinates. Repeated permutations can
be removed because T_r is symmetric. Put

\[
 K_F=\bigcap_{r=1}^{d}\ker L_r.
 \tag{SE35.5}
\]

This is a linear subspace obtained from the actual response
components, not from a metric, spectral approximation or guessed
symmetry.

**Theorem.** For x,z in V the following are equivalent:

\[
 \begin{aligned}
 &{\cal A}_c(x;h)={\cal A}_c(z;h)\quad\hbox{for every }h\in V;\\
 &F(u+t(x-z))=F(u)\quad\hbox{for every }u\in V,\ t\in\mathbb Q;\\
 &x-z\in K_F.
 \end{aligned}
 \tag{SE35.6}
\]

Thus the fibres of the complete active observation are exactly the
affine cosets x+K_F. Raw nonlinear fibres can be much larger.

**Derivation.** Equality of all translated readings cancels the
calibration and gives F(u+v)=F(u), where v=x-z. Repetition gives
F(u+Nv)=F(u) for every nonnegative integer N. The expression
F(u+t v)-F(u) is a finite polynomial in t with infinitely many
distinct roots, so all its coordinates vanish identically.

Its first t-coefficient is

\[
 \sum_{r=1}^{d}r\,T_r(v,u,\ldots,u).
\]

Separate homogeneous degrees in u and use SE33's finite
polarization to conclude T_r(v,h_1,...,h_(r-1))=0 for every r
and all directions. This is exactly v in K_F.

Conversely if v is in K_F, every term containing v in the finite
expansion of F(u+t v) vanishes. This proves invariance and equality
of readings. The resulting K_F is independent of c.

### A finite bank suffices for this stated polynomial class

As a polynomial in h, (SE35.3) has degree at most d-1: the
degree-d term T_d(h,...,h) cancels. Therefore the finite grid

\[
 {\cal H}_d=
 \left\{\sum_{a=1}^n t_a e_a:\ t_a\in\{0,1,\ldots,d-1\}\right\}
 \tag{SE35.7}
\]

determines the entire translated-response polynomial. There are
d^n W-valued response differences, including one when d=1.

To see this directly, interpolate in one h-coordinate at a time.
Each coordinate degree is at most d-1, so d distinct rational
nodes determine its coefficients. Repeating across the n
coordinates determines the full polynomial. Equal finite banks
therefore have exactly the fibres in (SE35.6).

This is a sufficient bank, not a minimum-query claim. One W-valued
reading can contain m scalar coordinates. The theorem requires a
known finite input sector and a declared degree bound; it is not
a fixed finite-query decoder for the whole unknown infinite module.

## 3. Theorem 2: descending response order constructs a polynomial decoder

The preceding theorem identifies the fibres. The next construction
actually recovers their quotient, using the finite response
coefficients already available in SE33.

For r>=1 define the observed mixed response difference

\[
 R_{r-1}(x,c;h_1,\ldots,h_{r-1})
 =\delta^{r-1}F_x[h_1,\ldots,h_{r-1}]
  -\delta^{r-1}F_c[h_1,\ldots,h_{r-1}],
 \tag{SE35.8}
\]

with R_0=F(x)-F(c). These are coefficients of the polynomial
h -> A_c(x;h), hence are obtained from the finite bank of
Theorem 1. An analytic derivative is not a premise.

Finite multilinear expansion gives

\[
 R_{r-1}
 =\sum_{k=r}^{d}\frac{k!}{(k-r+1)!}
 \left[
 T_k(x^{\,k-r+1},h_1,\ldots,h_{r-1})
 -T_k(c^{\,k-r+1},h_1,\ldots,h_{r-1})
 \right].
 \tag{SE35.9}
\]

Repeated symbols inside T_k denote repeated input slots, not
untyped multiplication of counting states. The k=r-1 term has
cancelled because it contains no x slot.

**Theorem.** The active bank determines every L_r(x-c), by
descending r=d,d-1,...,1. It therefore has a polynomial decoder
for any chosen linear representative of the class (x-c)+K_F.
If K_F is null, it has a polynomial left inverse recovering x
globally, even when the raw F has no inverse.

**Derivation.** At r=d, equation (SE35.9) reduces to

\[
 R_{d-1}=d!\,T_d(x-c,h_1,\ldots,h_{d-1}),
\]

so the highest contraction bank is known.

At a later stage suppose L_k(x-c) has been recovered for all k>r.
Choose a fixed linear section of the stacked higher contraction
map on its image and form a representative a with

\[
 L_k a=L_k x\quad\hbox{for all }k>r.
 \tag{SE35.10}
\]

Explicitly, a is c plus a linear function of the recovered higher
banks. At the initial stage with no higher banks, take a=c.

For k>r, x-a is in ker L_k. Since T_k is symmetric,
T_k annihilates x-a in any slot. Thus every higher term in
(SE35.9) is unchanged if x is replaced by the known a.
Subtract those terms and divide by r!:

\[
 \boxed{
 T_r(x-c,h_1,\ldots,h_{r-1})
 =\frac1{r!}\left[
 R_{r-1}
 -\sum_{k=r+1}^{d}\frac{k!}{(k-r+1)!}
 \{T_k(a^{\,k-r+1},h_1,\ldots,h_{r-1})
   -T_k(c^{\,k-r+1},h_1,\ldots,h_{r-1})\}
 \right].}
 \tag{SE35.11}
\]

Reading basis direction tuples gives all of L_r(x-c), completing
the induction. Stacking these banks gives a linear map L with
kernel K_F. A linear section S of L on its image returns

\[
 \widehat x=c+S L(x-c),\qquad x-\widehat x\in K_F.
 \tag{SE35.12}
\]

All operations used in the descent are polynomial in the observed
bank values: coefficient interpolation, fixed linear sections,
finite evaluations of known T_k and rational factorial division.
Thus the final decoder is polynomial.

Each linear section can be extended linearly to the whole bank
coordinate space once and for all. The resulting decoder is a
polynomial on all bank coordinates, not merely on physically
consistent observations. Its left-inverse identity is asserted
only on the lawful cut banks. This extension permits composition
with the deformed banks in Theorem 4.

When K_F is null, (SE35.12) is x itself. In general, changing the
chosen section changes the representative by a vector in K_F;
every target constant on those cosets is unchanged.

### Why highest-order readings alone can miss recoverable information

Take the scalar response

\[
 F(u,v)=u^3+v.
 \tag{SE35.13}
\]

The cubic component alone ignores v, so its contraction bank
cannot recover both coordinates. But

\[
 F(u+1,v)-2F(u,v)+F(u-1,v)=6u.
 \tag{SE35.14}
\]

Three active readings determine u, after which the existing
reading F(u,v) gives v=F(u,v)-u^3. Relative to calibration
c=(a,b), subtract its corresponding second difference to get
6(u-a), then recover v-b from the residual.

The raw scalar value has infinitely many input pairs with the
same value. The complete active bank has K_F null because the
cubic component reads u and the linear component reads v.
Recovery succeeds by combining response orders, not by assuming
the highest order is already sufficient.

## 4. Theorem 3: exact target recovery and minimum additional linear channels

Let A:V->Z be a supplied linear target. The complete active bank
recovers A(x-c) precisely when

\[
 K_F\subseteq\ker A.
 \tag{SE35.15}
\]

If this fails, the minimum number of additional scalar **linear**
readouts B(x-c) required is

\[
 \boxed{b_{\min}=\operatorname{rank}(A|_{K_F}).}
 \tag{SE35.16}
\]

For full state recovery, this is dim K_F.

**Derivation.** Theorem 1 says exactly which inputs share every
active reading. A target must agree on those fibres, giving
(SE35.15). When it does, Theorem 2's representative supplies the
target value.

With added readout B, the invisible differences become
K_F intersect ker B. Target faithfulness requires this subspace
to lie in ker A. Hence

\[
 \operatorname{rank}(B|_{K_F})
 \geq \dim K_F-\dim(K_F\cap\ker A)
 =\operatorname{rank}(A|_{K_F}).
\]

No smaller bank of scalar linear readouts can work. For
attainability, choose coordinates on
K_F/(K_F intersect ker A), and extend their linear functionals
to V. They use exactly the displayed number of channels.
The active bank already recovers a representative modulo K_F;
the additional linear values recover its target-relevant remainder.

This last rank argument consumes the existing MR-02/NM1
minimum-repair theorem. The extension here is the derivation of
K_F and a constructive decoder from a nonlinear active response.
The count is not an optimum over arbitrary nonlinear encodings,
adaptive experiments or alternative perturbation catalogues.

For F(u,v)=u^2, translations in any direction still give
(u+h_u)^2, independently of v. Thus K_F is the v direction.
Recovering only u needs no new response type; recovering both
coordinates needs one new independent linear channel such as v.
Collecting more values of the same u-only response cannot reveal v.

The minimum statement is about the cut response at the specified
unit depth. A direction absent at the cut can appear in higher
Lambda layers, for example through a Lambda v term. Access to
those extra layers is additional information, not a contradiction
of the cut-level blindness statement.

## 5. Theorem 4: repair the raw cut, then lift the nonlinear observer equation

Now let the measured polynomial family be

\[
 F_\Lambda=F_0+\Lambda B_\Lambda:V\longrightarrow W,
 \tag{SE35.17}
\]

with coefficients in Q[Lambda] and a declared finite total input
degree bound D>=1. Its cut F_0 need not be injective and its
linear response may be singular. Suppose the complete active
cut bank, supplemented by the linear channels from Theorem 3
if necessary, has no remaining invisible input direction.

Choose a finite probe grid large enough for the bound D.
Let C_Lambda(x) denote the resulting finite bank

\[
 \bigl(F_\Lambda(x+h)-F_\Lambda(c+h)\bigr)_h
\]

together with any declared supplementary linear readings. All
operations and calibration values are supplied. Applying Theorem 2
and the added linear recovery gives a polynomial decoder D_0
on the bank coordinate space such that

\[
 D_0(C_0(x))=x.
 \tag{SE35.18}
\]

**Theorem.** The completed observation operation

\[
 \boxed{Z_\Lambda(x)=D_0(C_\Lambda(x))
                  =x+\Lambda E_\Lambda(x)}
 \tag{SE35.19}
\]

has a unique formal unit-memory inverse. For actual observed bank
o=C_Lambda(x), the original input is recovered as

\[
 \boxed{x=Z_\Lambda^{-1}(D_0(o)).}
 \tag{SE35.20}
\]

On each retained cut through degree q, the calculation is finite.
SE34's residual correction and order-doubling construction apply
to Z_Lambda, whose cut linear response is the identity.

**Derivation.** C_Lambda is polynomial in the source coordinates
and Lambda, and D_0 is a polynomial on the whole bank space.
Its cut composition is the identity by (SE35.18). Subtracting
that identity leaves a polynomial divisible by Lambda, proving
(SE35.19). SE34 Theorem 3 supplies the inverse because its cut
inverse is explicitly I. Substituting the lawful observed bank
gives (SE35.20).

For reference, a direct update for target z=D_0(o) is

\[
 x^{(0)}=z,\qquad
 x^{(n+1)}=z-\Lambda E_\Lambda(x^{(n)}).
 \tag{SE35.21}
\]

Each update fixes one more unit layer. The accelerated version
uses the response of Z_Lambda as in SE34 Theorem 4.

A left inverse of an observation into a larger bank space is
not a two-sided inverse onto all arbitrary bank values. An
inconsistent bank can produce a decoded candidate without
matching its full forward readings. The source-recovery identity
above is for data supplied by the declared operation. Different
off-image extensions of D_0 can produce different intermediate
Z_Lambda maps, but all recover the same source from lawful data.

This is a constructive connection that SE34 did not yet supply:
a non-invertible raw cut can acquire an invertible **completed
observation** from additional active readings, before unit lifting.

## 6. Worked singular-cut repair with a moving calibration

### The square response

For Q(x)=x^2 and a known nonzero rational perturbation h,

\[
 Q(x+h)-Q(x-h)=4hx.
\]

Subtract the same reading at arbitrary calibration c:

\[
 \boxed{
 x-c=
 \frac{Q(x+h)-Q(x-h)-Q(c+h)+Q(c-h)}{4h}.}
 \tag{SE35.22}
\]

The raw response has x and -x branches, and its first response
2x vanishes at x=0. The active decoder remains valid there.
Division is by the chosen nonzero probe, not by the unknown x.
The origin need not be selected as observer calibration.
Reversing the probe label h swaps the two readings and reverses
the denominator, leaving the decoded x-c unchanged.

For the componentwise matching square from SE33,

\[
 Q(x)=\sum_{a=1}^n x_a^2 e_a,
\]

the supplied marked probe h=sum_a e_a gives

\[
 Q(x+h)-Q(x-h)=4x.
 \tag{SE35.23}
\]

These are two whole-vector readings, each with n scalar output
coordinates. The result does not claim to recover n free
coordinates from two scalar numbers.

### A deformed square with a genuinely nonlinear correction

Take the supplied family

\[
 F_\Lambda(x)=x^2+\Lambda x^3.
\]

With probe h=1, define the completed reading using calibration c:

\[
 Z_\Lambda(x)=
 c+\frac{F_\Lambda(x+1)-F_\Lambda(x-1)
         -F_\Lambda(c+1)+F_\Lambda(c-1)}4.
\]

Finite expansion gives exactly

\[
 \boxed{Z_\Lambda(x)=
 x+\frac32\Lambda(x^2-c^2).}
 \tag{SE35.24}
\]

Its cut is the identity despite the raw cut being x^2.
For observed z=Z_Lambda(x), the first recovered layers are

\[
 x=z-\frac32\Lambda(z^2-c^2)
       +\frac92\Lambda^2 z(z^2-c^2)
       +O(\Lambda^3).
 \tag{SE35.25}
\]

Substituting the series into (SE35.24) fixes the Lambda
coefficient as -(3/2)(z^2-c^2), then fixes the Lambda^2
coefficient as (9/2)z(z^2-c^2). Earlier coefficients stay
unchanged. Here O(Lambda^3) means discarded unit layers,
not a numerical bound at an assigned nonzero Lambda.

Thus the programme now contains a concrete raw singular cut,
its active observer repair, the completed observer equation and
its continued nonlinear recovery. No inverse of x^2 on its
original single-reading target was falsely declared.

## 7. Calibration movement and frame transport

Changing calibration from c to c' obeys the exact identity

\[
 {\cal A}_{c'}(x;h)=
 {\cal A}_c(x;h)+F(c+h)-F(c'+h).
 \tag{SE35.26}
\]

Only known calibration terms change. The subspace K_F, quotient
dimension and additional-channel count do not depend on c.
For full recovery the reconstructed x is unchanged; relative
coordinates change from x-c to x-c'.

Under supplied invertible linear input and output changes U,V,
put

\[
 \widetilde F(\widetilde x)=V F(U^{-1}\widetilde x),
 \quad \widetilde c=Uc,\quad\widetilde h=Uh.
\]

The contraction banks transport by their tensor slots, giving

\[
 K_{\widetilde F}=U K_F.
 \tag{SE35.27}
\]

Consequently the dimension of unrecovered information and the
rank needed for any transported target are invariant. The
observer's chosen coordinates, signs and reference state do not
alter these counts when the operation, target and probes are
transported together.

A coordinate change without transporting the probes is a change
of experiment. The derivation therefore retains probe labels and
calibration data rather than discarding them as notation.

## 8. Construction order, source use and boundary

| Source read | What is used here |
| --- | --- |
| SE33 joint readings, polarization and response calculus | Finite mixed response coefficients and symmetric multilinear descriptions |
| SE34 unit-memory lifting | Inversion after the completed observation has identity cut |
| Canonical 01_NATIVE_ALGEBRA.md, N03/N05 | Existing distinction between state observation, target and algebra reconstruction |
| Canonical NATIVE_LAURENT_JET_REPAIR.md, NM1 | Target-faithfulness and minimum extra linear readouts |
| Morphic recognition MR-02 | Blind quotient and attainment of the minimum target-relevant memory rank |
| Stratified recognition SR-02 | Existing warning that an unread component is not eliminated by its absence from a retained channel |
| Lambda holonomy/branch-memory capsule | A different branch problem involving supplied spectral lifts; no holonomy or connection premise is imported |

The construction proceeds from the declared finite counting sector,
known polynomial kernels and lawful perturbations; to the exact
translation-blind subspace; to finite response interpolation;
to descending-order decoding; to minimum linear repair if needed;
and finally to the completed observer equation and unit lifting.

Polynomial finite differences, polarization, linear quotient
decoding and formal inverse lifting are established algebraic
mechanisms. This development integrates them in the counting
observer construction and makes no priority claim for those
mechanisms. It assumes no primitive Hilbert metric, analytic
differentiation, spectral inverse or geometric curvature.

The statements require the declared ability to read F(x+h).
They do not provide that ability from a passive measurement,
nor guarantee that a physical system permits arbitrary
perturbations. Scalar versus vector output counts are explicit.
Unknown operator degree, noisy data, unobserved higher terms
and incomplete perturbation catalogues have no blanket recovery
claim here.

The active finite-bank theorem concerns a known finite counting
sector. Applying it uniformly to growing sectors requires a
supplied family of allowed probes and target-compatible decoders.
There is no claim that one finite bank recovers an unknown
infinite counting state.

Certification, executable implementation, replay, new pins and
verification runs are deferred. Earlier certificates and their
table remain unchanged. RH, Yang--Mills and curvature remain
outside this development.

The next mathematical question is the restricted observer:
when only a supplied subset of perturbations or operator actions
is available, determine its actual blind fibres and the smallest
additional actions needed for the chosen target. Full-translation
access must not be silently assumed in that next problem.

