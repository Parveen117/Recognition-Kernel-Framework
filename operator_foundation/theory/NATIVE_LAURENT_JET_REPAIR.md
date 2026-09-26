# Native Laurent residues and target-faithful jet-memory repair

Author: Monty Dabas. Reconciled development edition 0.2, 26 September 2026.
Status: written algebraic theorems with explicit hypotheses and independent exact finite verification. No proof-assistant verification or physical claim is made.

## 1. Source and purpose

MP's native path algebra supplies cut scalars, typed composition, dagger and local identity paths. Its principal-part programme supplies Laurent coefficients and their marked observation. This continuation connects those two existing lines **before** any ordinary Hilbert representation or analytic contour is installed.

The historical source is MP commit `506ddd72ede419bd68f941e11cf9bdd5645a4129`, manuscript `programmes/native_spectral_determinant_principal_parts/NATIVE_SPECTRAL_DETERMINANT_PRINCIPAL_PARTS_THEOREM.md`, blob `9752c511ff441c52d7a285906396271ae1cc0221`. Section 11's coefficient formula survives; its generic projector interpretation does not. The current document is a corrective continuation, not a retraction of the other identities in that source.

## NL1. Formal principal coefficients in a native algebra

**Definition.** Let A_Sigma be an associative native algebra with an admitted local unit e. Let K_Sigma be its central characteristic-zero cut field. Adjoin one central **formal continuation indeterminate** t. It is not a clock. A formal Laurent series has finitely many negative powers but can have infinitely many nonnegative coefficients. Cauchy products are well-defined because each coefficient receives finitely many contributions.

Suppose

    A(t)=sum_(r>=0) A_r t^r,
    B(t)=A(t)^-1=sum_(j=1)^q R_-j t^-j + sum_(r>=0) B_r t^r,
    AB=BA=e.

**Theorem (left/right chain relations).** For s=1,...,q,

    sum_(r=0)^(q-s) A_r R_-(s+r)=0,
    sum_(r=0)^(q-s) R_-(s+r) A_r=0.

**Proof.** These are the negative coefficients of AB=e and BA=e respectively. Order of factors is preserved; commuting coefficient matrices is not assumed. QED.

**Theorem (logarithmic residues).** With formal derivative A'=sum_(r>=1) r A_r t^(r-1), define

    J_R=[t^-1](B A'),    J_L=[t^-1](A' B).

Then

    J_R=sum_(j=1)^q j R_-j A_j,
    J_L=sum_(j=1)^q j A_j R_-j.

**Proof.** A product t^-j * t^(r-1) contributes to degree -1 exactly when r=j. Holomorphic/formally nonnegative terms do not contribute. QED.

These are coefficient identities in a potentially noncommutative native algebra. They need no contour, pi, trigonometric period, metric, positive pairing or adjoint theorem. An analytic contour may later realize coefficient extraction; it does not define this algebraic construction.

## NL2. Residue and native aperture are different types

**Proposition.** A logarithmic residue need not be idempotent, hence need not be a native aperture.

**Proof.** For a nonzero native identity p in its corner, take A(t)=t^m p and B(t)=t^-m p. NL1 gives J_R=J_L=mp, while

    J_R^2-J_R=m(m-1)p.

For m=2 this is 2p != 0 in the cut field. Source NR10 and F06 require p^2=p before an object is admitted as an aperture/projection. The counterexample fails that internal condition before questions about positivity or orthogonality arise. QED.

A label such as 'multiplicity residue' does not erase its value. It prevents an operation with the wrong type from being used in the next theorem. Nor does accidental idempotence on one calibration prove a universal projector theorem.

## NJ1. The native local jet-memory module

For this theorem, specialize to a finite free module V=K_Sigma^n, where K_Sigma is the exact cut field or its established completion. Let O=K_Sigma[[t]], and suppose A(t) is an n-by-n formal matrix with det A not identically zero. Define

    Q_A = O^n / A(t) O^n.

This is a **module quotient**. Its invisible part is the image of A acting on column germs, not a two-sided ideal asserted for the entire operator algebra. Multiplication by t descends because t is central:

    N_A [x(t)] = [t x(t)].

Let delta=ord_t det A.

**Theorem (finite length and exact continuation).** Q_A has cut-field dimension delta. There are nonnegative integers s_1,...,s_n with sum s_i=delta such that

    Q_A is isomorphic to direct-sum_i O/(t^s_i).

Consequently N_A is nilpotent and, in those coordinates, retains one chain of length s_i for each s_i>0. Its nilpotence index is max s_i, or zero when Q_A=0.

**Proof without a Hilbert premise.** In O, every nonzero scalar is t^s u(t) for an invertible formal unit u. Select an entry of A with least t-valuation, move it to position (1,1), and multiply its row by its unit inverse. Every other entry is divisible by that pivot t^s. Elementary row and column operations over O clear the remaining pivot column and row. These operations are invertible and preserve the presented module up to isomorphism. The remaining submatrix is nonsingular over K_Sigma((t)); induction diagonalizes it into powers of t. A zero exponent produces a zero quotient. The residue classes 1,t,...,t^(s-1) form a basis for O/(t^s), proving the length and chain statements. Determinants of the elementary unit transformations have valuation zero, so the sum of the exponents equals delta. QED.

This is a finite formal-module theorem. Infinite-dimensional Fredholm pencils, noncentral parameters and determinants of general path algebras require separate contracts. Local Smith-form mechanisms are standard algebraic lineage; no priority is claimed for them.

## NJ2. Exact finite algorithm, with a certified stopping rule

At depth L>=1, identify (O/(t^L))^n with L coefficient layers of V. The relation operator is the lower block Toeplitz matrix

    (T_L)_(i,j)=A_(i-j) for 0<=j<=i<L, and 0 otherwise.

Let S_L multiply these truncated coefficient vectors by t. Since S_L T_L=T_L S_L, multiplication preserves the relation space. Choose a full-row-rank algebraic observer C_L whose kernel equals image(T_L). Exact nullspace/rank elimination supplies it; there is no appeal to orthogonal projection. Then

    Q_(A,L)=K_Sigma^(nL)/image(T_L),
    C_L S_L = N_L C_L,
    dimension(Q_(A,L)) = nL-rank(T_L).

A right inverse H_L of C_L computes N_L=C_L S_L H_L. The full intertwining equation is checked; merely calculating a compression is not enough.

**Theorem (truncation ledger).**

    d_L=dimension(Q_(A,L))=sum_i min(L,s_i),
    delta-d_L=sum_i max(s_i-L,0).

In particular L>=delta always suffices, and any smaller L with d_L=delta is already complete.

**Proof.** Reduce the diagonal module of NJ1 modulo t^L. Each summand retains exactly min(L,s_i) basis coefficients. The natural map Q_A -> Q_(A,L) is surjective; equality of their finite dimensions implies it is an isomorphism. The displayed remainder is the number of missing independent jet coordinates. QED.

The implementation obtains delta from an exact finite polynomial determinant and rejects an identically singular pencil. It never declares completion from a temporarily unchanged rank sequence alone. The explicit determinant routine is limited to at most five coefficient coordinates, to bound permutation cost; the written theorem has no such artificial dimension limit.

**Corollary (chain recovery without eigenvalue approximation).** For the completed N,

    rank(N^(k-1))-rank(N^k)

counts chains of length at least k. Successive differences recover the number of chains of each length. This follows directly by evaluating a nilpotent shift on each summand O/(t^s).

## NJ3. Covariance under lawful pencil re-presentations

**Theorem.** Let E(t),F(t) be formally invertible matrices and A_tilde=EAF. The map

    [x] in Q_A -> [E x] in Q_A_tilde

is an isomorphism and intertwines N_A with N_A_tilde.

**Proof.** Right multiplication by F does not change A's image because F is surjective over O. Left multiplication by E maps image(A) bijectively onto image(A_tilde). Central t commutes with E, so the continuation actions intertwine. QED.

Thus length and chain structure do not depend on a chosen label basis. Specific coefficient values, source channels and marker meanings still depend on their declared calibration/embedding. An abstract module isomorphism does not recover those operational data, just as equal scalar color does not recover native residue paths.

## NJ4. The multiplicity residue has an exact preserved meaning

In the finite commutative-scalar matrix sector of NJ1, formal determinant differentiation gives

    tr(A^-1 A')=(det A)'/(det A).

To prove it, differentiate the permutation expression for the determinant, collect cofactors, and use adj(A)=det(A) A^-1 over the Laurent field. Writing det A=t^delta u(t), with u a formal unit, gives

    tr J_R = tr J_L = delta = dimension(Q_A).

The term u'/u has no negative powers, so it contributes no residue. This does not assert that the operator J_R itself is invariant under all parameter-dependent left/right re-presentations, nor that it is a projection. Its trace is the retained multiplicity count in this finite sector.

## NJ5. Constructive replacement for the scalar quadratic case

For A(t)=t^2:

    J_R=2,                  not idempotent;
    Q_A=O/(t^2),            dimension 2;
    basis = ([1],[t]);
    N_A=[[0,0],[1,0]],      N_A^2=0 but N_A!=0;
    identity_Q=I_2,         identity_Q^2=identity_Q.

The factor two is now carried by two independent continuation-memory coordinates. It is not forced to be a projection on the original one-coordinate carrier.

The formal resolvent of N_A is

    (s I-N_A)^-1=s^-1 I+s^-2 N_A,

so its coefficient at s^-1 is the genuine identity on Q_A. More generally, for nilpotent N^q=0 the finite sum sum_(k=0)^(q-1) s^(-k-1) N^k is verified by multiplication. This construction uses no analytic contour or spectral theorem.

No canonical idempotent on the original pencil carrier is claimed. A positive pairing on Q_A and a physical readout of its chains are separate questions. The identity is already an algebraic idempotent independent of those choices.

## NM1. Marked principal coefficients and minimum observation repair

For a finite matrix coefficient R, the calibrated markers E_ji read

    tr(E_ji R)=R_ij.

Thus a complete entry-marker bank recovers each coefficient without a Hilbert-Schmidt norm. More generally, for linear observation C and target L on the declared coefficient space, exact recovery exists precisely when ker(C) is contained in ker(L). The minimum extra cut-scalar readouts are

    rank([C;L])-rank(C).

**Proof.** A target factors through C exactly when it is constant on each fibre of C, which is the kernel condition. Stacking independent target rows attains the necessary rank increase. This consumes the framework's existing target-faithfulness line rather than relabelling it as a new principle.

Future jet observations are repaired by closing row(C)+row(L) under right multiplication by N. Finite rank saturation gives the minimum future-complete observer. A particular two-coordinate scalar-quadratic fixture with C=(0,1) requires one additional cut-scalar channel.

Retain the historical family A_c(t)=[[t,c],[0,t]]:

    det A_c=t^2,
    R_-1=I for every c,
    R_-2=[[0,-c],[0,0]].

For c=0 the jet module has chains [1,1]; for c!=0 it has chain [2]. The scalar determinant and simple residue cannot distinguish them. A single calibrated marker tr(E21 R_-2)=-c detects and quantifies the missing coefficient. Abstract chain type alone does not recover the magnitude of nonzero c.

## NP1. Integer sheet memory is not jet depth

The independent sparse path kernel implements a declared finite-support submodel of the countable source groupoid. The arrow e_(x,y)^k has target x, source y and integer residue k; composition and dagger are

    e_(x,y)^k star e_(u,v)^l = delta_(y,u) e_(x,v)^(k+l),
    (z e_(x,y)^k)^dagger = z^dagger e_(y,x)^(-k).

For Phi extracting the sum of stationary identity coefficients,

    Phi(a^dagger star a)=sum_gamma N_Sigma(a_gamma).

The only way a product of reversed and forward arrows is the identity arrow is that the entire typed arrow, including k, matches. This proves the finite coefficient-square identity directly.

The endpoint map sends every e_(x,y)^k to the same matrix unit E_xy and is an algebra/dagger map, but not faithful. In particular

    w=e_(b,a)^1-e_(b,a)^0 != 0,
    endpoint(w)=0,
    Phi(w^dagger star w)=2.

No new jet operation erases k or reduces it modulo L. Conversely, an integer net residue is not a record of every intermediate word in a free path history; this submodel retains exactly the information it declares.

## Scope, lineage and next use

The new development adds a native formal realization and a constructive module replacement to the recovered principal-part programme. It is not an empirical gravity result, a global analytic linearization of every nonlinear pencil, or an automatic solution of all problem adapters.

For a source-selected finite pencil, the usable outputs are the full marked principal packet, exact multiplicity, jet-memory carrier, continuation action, source-frame intertwiner, and target-faithfulness/minimum-repair calculation. Physical length, clock, universal coupling and a metric must enter later through separately tested native-to-observable contracts.

Method lineage, not primitive dependencies: local Smith-form/root-chain and Toeplitz constructions are established mathematical mechanisms. For an external comparison see Matthias Stiefenhofer, *Formal and Analytic Diagonalization of Operator functions*, arXiv:2305.14228, and Wolf-Juergen Beyn, *An integral method for solving nonlinear eigenvalue problems*, arXiv:1003.1580. The algebraic proofs above do not invoke their analytic or operator-space hypotheses; no general priority claim is made.
