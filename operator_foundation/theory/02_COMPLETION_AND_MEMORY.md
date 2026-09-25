# Native mass completion, local resolvent calculus, and dynamical memory

Author: Monty Dabas. Development edition: 26 September 2026.
This continuation uses the native cut field and path algebra of `01_NATIVE_ALGEBRA.md`. It supplies written proofs for a **specified completion class**, not a theorem covering every possible operator topology or every unbounded generator.

## N07. A complete native operator algebra without a primitive Hilbert space

Assume the already-established Archimedean completed radial field R_Sigma and its cut field C_Sigma. Use the scalar gauge

    D(a+iota b)=|a|+|b|.

It is submultiplicative and dagger-invariant. It is a real norm; it is not homogeneous with respect to the modulus of every complex scalar. We therefore describe the first completion as a complete **real normed dagger algebra with bounded central cut-complex scalar action**, not a complex C*-algebra with this gauge.

Choose a countably infinite labelled face set I. Let K_fin be finite-support matrices indexed by I x I with entries in C_Sigma. Define

    M(k)=sum_(i,j) D(k_ij).

For finite matrices,

    M(kl) <= M(k) M(l),     M(k^dagger)=M(k).

The first inequality follows by the scalar triangle inequality, summing over i,j,r, and bounding the restricted matching-index sum by the full nonnegative product sum. The second is index reversal.

Complete this space in M. Concretely it is

    K_1={k : sum_(i,j) D(k_ij)<infinity}.

To prove completeness, view radial and turn entries as two absolutely summable coordinate families. A Cauchy sequence has coordinate limits; finite partial sums bound their total absolute sum, and the Cauchy tail bound passes to that limit. Finite truncations are dense because the omitted absolute sum tends to zero. Products extend continuously by the bound. Absolute summability justifies associativity and reordering of sums, and dagger extends isometrically.

The infinite diagonal identity is not in K_1. Adjoin it explicitly:

    A_Sigma = C_Sigma 1 direct-sum K_1,
    (a,k)(b,l)=(ab, a l+b k+kl),
    (a,k)^dagger=(a^dagger,k^dagger),
    ||(a,k)||_Sigma=D(a)+M(k).

The preceding estimates prove submultiplicativity. Completeness follows from completeness of the two summands. The unit (1,0) has norm one. This corrects a common infinite-limit error: appending more finite diagonal entries is not a Cauchy construction of a unit in total-entry mass.

There is a faithful bounded native action on the mass-completed vector carrier

    X_1={x : sum_i D(x_i)<infinity},
    (a,k)x = a x+kx.

Absolute summability gives ||(a,k)x|| <= ||(a,k)||_Sigma ||x||. If this action vanishes on all basis vectors, off-diagonal k entries vanish and every diagonal entry equals -a. Infinitely many such entries can be summable only if a=0; then k=0. Hence the action is faithful. No Hilbert norm, probability interpretation, or physical clock is needed for this construction.

**Important class restriction.** The completion has been constructed for absolutely mass-summable path kernels plus a scalar identity. It is not the whole bounded-operator algebra, and does not contain arbitrary differential Hamiltonians. Another native completion needs its own norm and domain proof.

### The mass algebra is not automatically a C*-algebra

For the finite-support rank-two diagonal projection p,

    p^dagger p=p,
    M(p^dagger p)=2,     M(p)^2=4.

Thus the C*-norm identity fails. This is a property of the chosen gauge, not a defect in associativity or completion. A positive representation and its induced operator norm form a later, separately typed construction (N11 below).

## N08. Native local resolvent calculus

In the unital complete algebra A_Sigma, let a be fixed and let lambda be a central cut scalar. If lambda 1-a is invertible, write R(lambda) for its inverse. Invertibility is not defined by one sufficient Neumann bound.

If ||b||<1, finite geometric multiplication gives

    (1-b) sum_(k=0)^N b^k = 1-b^(N+1).

Completeness and submultiplicativity give convergence of the series to a two-sided inverse of 1-b, with

    ||sum_(k>N)b^k|| <= ||b||^(N+1)/(1-||b||).

Now let R_0=R(lambda_0) and h=lambda-lambda_0. Because h is central,

    lambda 1-a=(lambda_0 1-a)(1+h R_0).

If q=D(h)||R_0||<1,

    R(lambda)=R_0 sum_(k>=0)(-h R_0)^k,

and the truncation remainder is bounded by

    ||R_0|| q^(N+1)/(1-q).

This proves an open invertible neighborhood and a native convergent local power series. Multiplying the two inverse identities proves

    R(lambda)-R(mu)=(mu-lambda)R(lambda)R(mu).

Dividing by nonzero h gives

    [R(lambda_0+h)-R_0]/h = -R(lambda_0+h)R_0 -> -R_0^2.

Thus the native scalar derivative exists and equals -R_0^2. This advances T52's explicitly unbuilt complex-analytic-resolvent gate within the concrete N07 completion. It does not locate every spectral point or prove a spectral theorem for arbitrary nonnormal operators.

For the finite executable comparison, T52's partial sum is lambda^-1 sum_(k=0)^N(lambda^-1 a)^k. Its tail starts at k=N+1>=1, so M((lambda^-1 a)^k)<=q^k gives the stated bound even though the entry-mass of a finite matrix identity is n, not one. The code does not silently replace M(I_n) by 1.

## N09. Exact memory before a clock or a force interpretation

A continuation index n is an ordered protocol label, not yet physical time. Let one admitted finite step, or a bounded step on a completed direct sum, have blocks

    U = [[A,B],[C,D]],
    x_(n+1)=A x_n+B y_n,
    y_(n+1)=C x_n+D y_n.

Induction gives

    y_n=D^n y_0 + sum_(j=0)^(n-1) D^(n-1-j) C x_j.

Substitution yields the exact visible equation

    x_(n+1)=A x_n + B D^n y_0
             + sum_(j=0)^(n-1) B D^(n-1-j) C x_j.

The kernel B D^r C and initial-memory term B D^n y_0 are derived from the same declared U. They cannot be chosen after seeing a desired residual. For time-varying steps the powers become chronological products of hidden blocks, so no stationarity assumption is necessary to preserve the memory identity.

A closed visible step independent of **all** hidden initial states requires B=0: at n=0 compare two states with identical x_0 and arbitrary different y_0. This is stronger than observing a zero memory kernel on one prepared trajectory. If the preparation enforces y_0=0, closure of that special response has a weaker, preparation-dependent condition.

For a complex spectral parameter z, when z-D is invertible, block elimination gives

    [(z-U)^-1]_visible
       = [z-A-B(z-D)^-1 C]^-1,

provided the Schur term is invertible. Solve the hidden block equation for y and substitute into the visible equation to obtain the formula. For U=K and z=2, the visible resolvent is 2/3, not the naive corner value 1/2. This is the same memory-return mechanism as N06 at the level of response rather than individual products.

These are operator identities related to classical projection/memory methods. They are not new physical laws, and a resemblance to an open-system master equation does not identify the native blocks with a quantum environment.

## N10. Uniform observer control is the missing completion contract

Let X_0 be a native normed linear space, Y a normed readout space, and Z a complete target space. Let C:X_0->Y and L:X_0->Z be linear. There exists a bounded decoder D on closure(C X_0) satisfying D C=L if and only if there is a finite b such that

    ||Lx|| <= b ||Cx||    for every x in X_0.

The least such b is the decoder norm.

**Proof.** A bounded D gives the inequality. Conversely the inequality implies Cx=0 -> Lx=0, so D(Cx)=Lx is well-defined and bounded by b on the range. For a Cauchy sequence of readouts the corresponding targets are Cauchy; completeness of Z supplies a unique extension to the closure. Taking the supremum of the ratio gives the exact norm. QED.

For nested finite carriers with compatible C_n and L_n, a uniform b establishes this estimate on their union. Finite kernel inclusion at every stage is not enough. On the native summable vector carrier take

    C(x_1,x_2,...) = (x_1,x_2/2,x_3/3,...),    L=identity.

Every finite restriction of C is invertible and the infinite C is injective, but x=e_n has ||Lx||/||Cx||=n. No bounded decoder exists. This is an explicit counterexample to promoting finite faithfulness into stable infinite recovery.

N10 makes the missing observer obligation in T54 operational, but does not certify it for a particular RH, Yang-Mills, or gravity observer that has not been supplied. A measured output error delta can be propagated to b delta only after this uniform bound is established. This is the same factorization/majorization family as classical bounded-operator recovery, expressed in the framework's own declared norms and targets.

## N11. A positive native representation can be built, but must be supplied honestly

This is a later representation theorem, not a primitive premise of N01-N10. Let A be a unital cut-complex dagger algebra and omega:A->C_Sigma a complex-linear functional with

    omega(1)=1,
    omega(a^dagger a) >= 0 in the radial field.

Require also, for each a, an independently established finite M_a such that

    omega(b^dagger a^dagger a b) <= M_a^2 omega(b^dagger b)

for all b. Positivity gives the Cauchy-Schwarz inequality by evaluating omega((x+t y)^dagger(x+t y)) for central cut scalars t and minimizing its radial quadratic expression; a zero diagonal value is handled by varying t before division.

Let N={b:omega(b^dagger b)=0}. Cauchy-Schwarz makes N the radical of the pairing omega(x^dagger y). The displayed bound makes N a left ideal. Hence

    <[x],[y]> = omega(x^dagger y),
    pi(a)[b]=[ab]

are well-defined on A/N, and ||pi(a)||<=M_a. Completing the positive pairing gives a Hilbert representation with pi(a^dagger)=pi(a)^dagger and cyclic vector [1]. This is the native presentation of the standard positive-functional representation construction; its method is not claimed as new.

Faithfulness is a separate condition: pi(a)=0 precisely when omega(b^dagger a^dagger a b)=0 for every b. For example, omega(x,y)=x on C_Sigma direct-sum C_Sigma erases the entire second summand. Positivity alone therefore does not identify the full native algebra with its represented image.

Taking the operator-norm closure of the represented image gives a C*-algebra. The C*-identity belongs to that positive bounded-operator norm, not to T50's cut-mass gauge. The choice of omega, its boundedness contract, and faithfulness are not a derivation of detector frequencies or of the Born rule.

## Remaining development gates

The constructed native mass completion and the conditional positive representation are concrete usable foundations. A full application still needs its operator carrier, graph or generator selection, observation and target, and convergence/error budget. For unbounded generators, specify a dense domain, closability, the closure, boundary conditions, adjoint or self-adjointness obligations, and a common invariant core where needed. A finite matrix certificate cannot settle those by notation.

The gravity-specific chi-to-seam-two-jet proposal remains a constitutive adapter. Chi is unchanged by a common nonzero scaling of its two response columns, so it cannot by itself recover source amplitude. The same local two-jet admits different quartic extensions; it does not select a global metric. The next physical theorem must supply information that distinguishes those alternatives, using source/probe data rather than declaring the desired field equation.

## Source and method references

- RKF F00-E; T24, T28, T31, T32; corrected T50; T52-T55. Pinned source snapshot: `../sources/rkf-2026-09-25/` in the GitHub canonical folder.
- Publications U36 source-response and QB/GP bridges; QG v1.8 is a conditional adapter, not an input axiom.
- R. G. Douglas (1966), *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the AMS 17, 413-415. Related classical factorization lineage, not a claim that every normed-space statement above requires Hilbert structure.
- C. Widder, J. Zimmer, T. Schilling, *On the generalized Langevin equation and the Mori projection operator technique*, arXiv:2503.20457. Related projection/memory and domain-sensitive semigroup literature; the discrete block identity above is proved directly.
- Positive-functional Hilbert representation and C*-closure are standard representation-theory constructions. Their role here is an explicit optional layer and a faithfulness gate, not a novelty claim.
