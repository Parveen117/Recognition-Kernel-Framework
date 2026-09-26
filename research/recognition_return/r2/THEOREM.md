# Depth-dependent native returns, finite-coupling cut synthesis, and a boundary-memory criterion

Monty Dabas | Research R2 | 26 September 2026

## Advance relative to R1

R1 treated one constant nonnegative coupling in an EMK excursion family. R2 allows arbitrary positive depth-dependent **paired edge products**, derives the exact condition that preserves the unit response channel, and constructs actual finite-aperture inverses without a primitive Hilbert space. The resulting tail intervals collapse to one response exactly when a reciprocal-coupling series diverges. A depth-periodic profile can synthesize a prescribed return and, in particular, select an exact normalized native cut at finite coupling. This remains an aperture-completion result, not a finite-memory exact result or a full infinite-operator inverse theorem.

The series criterion has the classical Seidel-Stern/Stern-Stolz continued-fraction lineage. The native operator realization, preservation test, and constructive target design are the research integration here. External priority for this combination is not established. Proofs below are written mathematical arguments; executable finite tests are a separate evidence layer.

## 0. Native data and operator class

Work over the characteristic-zero completed cut field K_Sigma of the canonical framework. Exact calculations use its rational subfield. In the internal algebra,

    R^2=-I,  K^2=I,  KR=-RK,  L=KR,  L^2=I.

The native dagger of R1 gives L^dagger=L. There is no assumption of an ordinary inner product, Hilbert space, probability, physical time, or metric.

Retain the seam identities TS=I and ST!=I, p=I-ST, and the mutually disjoint apertures p_h=S^h p T^h. On the algebraic direct sum of finitely supported depth states, declare edge operators

    B_h=b_h R : h -> h+1,
    C_h=c_h K : h+1 -> h,       b_h,c_h>0.

The infinite action is well-defined on finitely supported states because each edge has finite degree. It need not be bounded in a chosen completion. All inversions below initially occur in finite block algebras. Let H be this nearest-neighbour action and P_(2n)=sum_(h=0)^(2n) p_h. The source of the boundary response is at height zero; no hidden nonzero source is silently discarded.

**Paired class.** For j>=0 require

    b_(2j)c_(2j)=b_(2j+1)c_(2j+1)=a_j>0.

The sequence of cells is a_0,a_1,...; the sequence of individual edge products is a_0,a_0,a_1,a_1,... . For example, cells 3,2,3,2,... mean edge products 3,3,2,2,3,3,2,2,... . The individual opening/closing ratios can vary independently while these products remain fixed. A response that sees only those products cannot reconstruct each directional amplitude.

These are supplied operator data. The pairing requirement is justified as an exact closure predicate below, not presented as a universal law of nature. The term depth-dependent does not mean time-dependent.

## RD1. Derive the local preservation condition before choosing the scalar return law

Assume an invertible tail system has first inverse block F=uI+vL, where u,v are radial scalars. Its inverse corner F itself is not required to be invertible. Append two new depth states with products p=b_0c_0>0 and q=b_1c_1>0. Eliminating the invertible tail leaves

    E = [[I,-C_0],[-B_0,I-C_1 F B_1]].

Pivot on the first I, not on the possibly singular lower diagonal block. The remaining block is

    D = I-C_1 F B_1-B_0 C_0
      = (1+qv)I+(p-qu)L.

Put s=1+qv, r=p-qu and Delta=s^2-r^2. When Delta!=0,

    D^-1=(sI-rL)/Delta,
    F_new=I+C_0 D^-1 B_0
         = [1+pr/Delta] I + [ps/Delta] L.                 (R2.1)

**Proof.** Native multiplication gives C_1 F B_1=q(uL-vI), B_0C_0=-pL, C_0LB_0=-pI. Substitute into the block elimination identity and multiply D(sI-rL)=Delta I on both sides. No factor order has been commuted except radial scalars. If Delta=0, D is zero or a scalar multiple of I+L or I-L. Their complementary nonzero factors show that D is not invertible. The original two-state extension is therefore invertible exactly when Delta!=0, under the invertible-tail hypothesis. QED.

**Closure predicate.** Since p>0 and Delta!=0, the coefficient of I in F_new equals one if and only if

    p=q u.                                               (R2.2)

In particular, on the unit response line F=I+xL, it stays on that line exactly when p=q=a. For x>=0,

    D=(1+ax)I,
    F_new=I+f_a(x)L,        f_a(x)=a/(1+ax).              (R2.3)

This scalar pivot is strictly positive. Pairing is thus necessary and sufficient for preserving this response line, not an arbitrary choice motivated only by a desired answer.

An intermediate half-step may be singular even when the complete pair is invertible: p=q=1, x=0 gives lower diagonal I-L singular but D=I. Conversely p=2,q=1,u=1,v=0 makes the full pair singular. Do not extend the matched result to all positive unmatched profiles.

An arbitrary prescribed finite tail corner F can be realized algebraically without requiring F^-1: the block matrices [[F,I],[I,0]] and [[0,I],[I,-F]] are inverses. Thus the stated tail class does not secretly require an invertible corner. This realizes a boundary contract, not necessarily another nearest-neighbour tail of the original paired class.

## RD2. Finite inverses for every positive paired profile

For n cells and the terminal single height 2n, put x_n=0 and compute backwards:

    x_j=f_(a_j)(x_(j+1)),          j=n-1,...,0.            (R2.4)

**Theorem.** I_(P_(2n))-P_(2n) H P_(2n) is invertible in its finite native block algebra, and its first inverse block is I+x_0 L.

**Proof.** The terminal one-state block is I. Append cells from the deepest one outward. RD1 applies at each stage, since its scalar pivot 1+a_j x_(j+1)>0. Induction proves existence and the inverse-corner formula. This proof does not invert a singular intermediate half-step. QED.

In the faithful two-coordinate EMK calibration, the ordinary finite determinant is the product of the squared scalar pivots. The implementation compares this product, the boundary formula, and both inverse identities against direct elimination of the complete block matrices. Those matrices verify the algebraic theorem; they are not its primitive state space.

## RI1. Exact boundary interval and cutoff certificate

Let r_j=1/a_j. Then f_(a_j)(x)=1/(r_j+x). For a fixed prefix of n cells define

    Phi_n=f_(a_0) o f_(a_1) o ... o f_(a_(n-1)),
    M_n=product_(j=0)^(n-1) [[0,1],[1,r_j]]
       =[[A_n,B_n],[C_n,D_n]].

The product order follows depth from the boundary inward. Consequently

    Phi_n(x)=(A_n x+B_n)/(C_n x+D_n),
    det M_n=(-1)^n.

For n>=1, C_n,D_n>0. The closure of the possible responses for all finite nonnegative terminal x is the interval I_n with endpoints B_n/D_n and A_n/C_n. The second endpoint denotes a limit as x tends to infinity, not an infinite scalar input to the executable solver.

**Theorem.**

    I_(n+1) is contained in I_n,
    width(I_n)=1/(C_n D_n),                               (R2.5)
    |Phi_n(x)-Phi_n(y)|
       =|x-y|/[(C_n x+D_n)(C_n y+D_n)].                    (R2.6)

**Proof.** Each next f maps nonnegative inputs into the previous tail class. Nesting follows. Subtract the fractional-linear images and use the determinant identity to prove both exact expressions. QED.

With x^(n)=Phi_n(0), Phi_n(infinity)=x^(n-1). Thus interval endpoints are consecutive actual finite even-aperture responses. Their alternating monotone subsequences need not meet; that is the next theorem, not an assumption.

The midpoint of I_n has certified native coefficient-mass response error at most width(I_n)/2 relative to every admitted deeper response. This enclosure remains valid even when no unique infinite-profile limit exists. A finite prefix cannot establish the reciprocal-series condition for an unknown tail.

**Uniform finite-depth bound.** If all a_j in the prefix are at most Q, then

    width(I_n)<=Q/ceil(n/2)<=2Q/n.                        (R2.7)

To prove it set D_(-1)=0,D_0=1, so C_n=D_(n-1) and

    D_n=D_(n-2)+r_(n-1)D_(n-1).

The even denominators are at least one. Also D_(2m+1)>=sum_(j=0)^m r_(2j)>=(m+1)/Q. Apply the two bounds to consecutive denominators. In particular any bounded positive infinite cell profile has a unique response, and a growing-coupling family with a_j<=gM has vanishing prefix uncertainty when n/g tends to infinity. This is a cutoff-error statement, not yet a universal cut-selection statement.

## RI2. Necessary and sufficient boundary-memory criterion

**Theorem.** For a positive infinite profile a_j, the nested intervals shrink to a point, and all nonnegative boundary-tail choices coalesce, exactly when

    sum_(j>=0) 1/a_j = infinity.                          (R2.8)

When that sum is finite, the adjacent even-aperture approximants have two distinct subsequential limits and boundary influence does not disappear.

**Proof.** Use the denominator recurrence above. Both parity subsequences of D_n are nondecreasing; all D_n>=c=min(1,r_0)>0. Moreover

    D_(n-1)D_n-D_(n-2)D_(n-1)=r_(n-1)D_(n-1)^2.

If sum r_j diverges, these positive increments force C_nD_n to infinity. Equation (R2.5) then gives width tending to zero.

Conversely set m_n=max(D_n,D_(n-1)). The recurrence gives m_n<=(1+r_(n-1))m_(n-1), hence m_n<=product_(j<n)(1+r_j). If sum r_j is finite, this product is bounded. One can establish that without logarithms: take a tail whose sum is less than 1/2, and bound its finite products by the geometric majorant 1/(1-sum tail r_j)<=2. Multiply by the finite preceding product. Thus all C_n,D_n are bounded by a finite K, and width(I_n)>=1/K^2>0. Nested bounded intervals have limiting endpoints; their positive separation proves the two-limit assertion. Formula (R2.6) also retains a positive separation for any two distinct fixed finite tail values. QED.

The scalar convergence criterion is the classical positive continued-fraction theorem, proved directly here and applied to RD2's native inverse corners. It is not claimed as a newly discovered general continued-fraction theorem.

### An explicit retained-memory family

Take a_j=4(j+1)^2. Since 1/n^2<=1/[n(n-1)] for n>=2, telescoping gives sum 1/a_j<=1/2. The product bound gives C_n,D_n<=2 at every depth. Therefore

    width(I_n)>=1/4,
    |Phi_n(1)-Phi_n(0)|>=1/8                              (R2.9)

for every n. All finite apertures are invertible, but the increasing sequence of even-aperture boundary inverses does not have one limit. This is a retained boundary-memory witness, not a failure of the finite algebra.

By contrast a_j=4(j+1) has a divergent reciprocal sum: each dyadic harmonic block contributes at least 1/8. It has a unique boundary response despite unbounded couplings. Thus boundedness of the profile is sufficient but not necessary, and invertibility at every finite cutoff is insufficient.

## SY1. Exact finite-coupling native cut synthesis

Take a positive two-cell period a,b,a,b,... . Its reciprocal sum diverges, so the two phase responses x,y exist uniquely and satisfy

    x=a/(1+ay),       y=b/(1+bx).

Eliminating y gives

    b x^2+x-a=0.                                          (R2.10)

There is one positive solution because this quadratic is strictly increasing on the nonnegative radial axis, is negative at zero and becomes positive. The completion itself, rather than a root choice imposed by a fit, selects it.

**Synthesis theorem.** For any desired x>0 and any free b>0, choose

    a=x+b x^2.                                           (R2.11)

The unique boundary-aperture response is then I+xL. The other phase is y=b/(1+bx). The normalized response Q=(I+xL)/2 has defect

    Q^2-Q=(x^2-1)I/4.

Consequently it is an exact native idempotent precisely when x=1, equivalently

    a=b+1.                                               (R2.12)

Its native dagger symmetry follows from L^dagger=L. No ordinary orthogonal projection or probability interpretation is used.

For cells (a,b)=(3,2), the exact responses are x=1,y=2/3:

    F_infinity=I+KR,
    Q_infinity=(I+KR)/2,       Q_infinity^2=Q_infinity.

This is **finite coupling and infinite aperture completion**. It does not assert exact closure at a finite cutoff. At a finite cutoff the solver instead supplies an exact rational enclosure. Nor is this a gravitational coupling predicted from primitive data: it is a constructive operator-design solution for an explicitly selected target.

### The return power series still diverges in the example

Introduce a central formal pair counter z, equivalent to multiplying H by a formal step and setting z equal to its square. At each depth the paired products become a_j z. Local formal inverses obey the same recursion. In the two-period case,

    b z x(z)^2+x(z)-a z=0,
    x(z)=sum_(m>=0) (-1)^m Cat_m a^(m+1)b^m z^(2m+1).

Formal uniqueness follows coefficient by coefficient; any fixed returning coefficient involves only finitely many depths. The Catalan recurrence verifies the coefficient formula. For a=3,b=2, the first terms are

    3z-18z^3+216z^5-3240z^7+... .

The ratio of absolute successive terms tends to 4ab|z|^2. Thus the radius is 1/(2 sqrt(ab)); at z=1 in this example, the terms do not tend to zero. With all individual opening amplitudes b_h=2, H^n applied to the boundary identity has the unique height-n coefficient 2^n R^n. Its native coefficient burden is at least 2^n. The full Neumann state series cannot converge in the corresponding summable coefficient carrier either. The exact native cut is selected by the finite-aperture inverse completion, not by claiming either divergent series now converges.

## SY2. Design an entire periodic response profile

Let x_0,...,x_(m-1)>0 be a desired periodic sequence of scalar return coordinates. Indices in this theorem are cyclic, including the last-to-first edge. A positive cell design exists exactly when

    x_j x_(j+1)<1             for every j.                (R2.13)

It is then uniquely given at the cell-product level by

    a_j=x_j/[1-x_j x_(j+1)].                              (R2.14)

**Proof.** Rearranging x_j=a_j/(1+a_j x_(j+1)) gives the displayed formula and positivity condition. Conversely those choices solve every recurrence exactly. Their periodic positive profile is bounded, so RI2 proves the finite apertures select that profile independently of the nonnegative tail. QED.

For target (1,2/3,1/2), the designed cells are (3,1,1). The first phase selects a native cut, while the other phases retain distinct non-idempotent responses. Cyclic closure is an actual constraint: testing only neighbouring entries before the wrap would admit false periodic designs.

This gives an inverse-design interface, not merely another forward formula. Individual b_h,c_h can still be varied at fixed cell products, so the design is not unique at the directional-amplitude level.

## SY3. Finite defects, persistent bulk modulation and scale order

A fixed finite prefix a_j=g alpha_j, alpha_j>0, attached to a homogeneous tail with coupling g retains R1's strong-return cut. The tail coordinate d(g) tends to one; recursively

    f_(g alpha)(x)=1/[1/(g alpha)+x] -> 1

whenever x tends to one. Induction across the fixed finite prefix proves the claim. Exact intervals can be transported through that prefix, preserving outward error bounds. The cutoff must still grow with coupling; a first exploratory test with fixed tail depth did not meet the intended accuracy at large coupling, and the final validation uses a coupling-dependent depth and independently known rational tail checks.

An indefinitely repeated modulation behaves differently. Scaling the period to (g a,g b) gives

    b x(g)^2+x(g)/g-a=0,
    x(g)->sqrt(a/b).

Therefore the normalized idempotence defect tends to (a/b-1)I/4. It need not vanish. For the finite-cut design (3,2), multiplying both cells by ten produces (30,20), whose exact return is 6/5 and cut defect 11I/100. Greater coupling alone is not a guarantee of better cut closure.

Two periods can have the same scalar product ab and different recognized responses: (3,2) and (6,1) both have product six but give x=1 and x=2. Moving the aperture by one cell changes (3,2) to (2,3) and gives x=2/3. These statements concern the supplied period product and aperture, not an unproved equality of full spectra.

## ID1. Recover local products from a richer observation

In RD1 assume the tail is known to be I+xL. Suppose both output coordinates u,v are measured algebraically, v!=0. Put

    w=(u-1)/v,
    alpha=v(1-w^2),   beta=alpha-w.

When the nondegenerate positive-input conditions hold, inversion gives

    p=alpha/(1-beta x),     q=beta/(1-beta x).             (R2.15)

To verify, RD1 gives w=(p-q)/(1+qx), alpha=p/(1+qx) and beta=q/(1+qx). Solve and substitute back. The implementation checks the complete round trip and rejects zero/degenerate inputs. This resolves the two neighbouring edge products in a known tail; it does not recover every opening/closing amplitude or an unknown deep profile from one scalar boundary output.

## Scope and method lineage

R2 constructs and proves results for the explicitly paired depth-varying EMK family and the declared nonnegative boundary-response class. Local mismatched pairs have their separate two-coordinate formula and singularity test. Arbitrary complex/negative tails, arbitrary unpaired infinite chains, physical time, an empirical source/probe law, and global infinite inverses are not concluded.

The original R1 theorem and implementation remain unchanged. The new files consume the canonical operator arithmetic and Pāṇinian proof-replay engine; they are not a replacement framework. All primitive inputs are native algebraic objects. Positive radial order enters a stated convergence proof, not an assumed Hilbert geometry.

Comparison source: Alan F. Beardon and Ian Short, *The Seidel, Stern, Stolz and Van Vleck Theorems on continued fractions*, Bulletin of the London Mathematical Society 42 (2010), 457-466, DOI 10.1112/blms/bdq006. The retrieved publisher abstract confirms the established theorem lineage. No hyperbolic-space or Hilbert-space hypotheses from that treatment are imported into the elementary denominator proof above. Catalan and continued-fraction methods have established prior work as recorded in R1. External novelty of this native paired operator synthesis has not been established by the limited literature comparison.
