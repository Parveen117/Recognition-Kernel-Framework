# SE47: the existing five-source operator with its source, metric and correlations retained

13 October 2026 (Asia/Kolkata). Author: Monty.

This returns to the programme's existing **one boundary plus four accepted
columns** construction. The repair is to construct every column from the
same corrected source, retain its label metric, and preserve correlations
when reading a small gap. It is not a new five-number prime generator.

The historical object was K=diag(1,A_3)-W^dagger S^(-1)W. SE5 explicitly
left its corrected-source attachment open. We derive that architecture
directly from the current source form, then execute it on SE21's complete
arithmetic readings at eta=0. The finite instantiation uses the declared
accepted space E=span(f_2,f_3,f_4,f_5); equality with the historical raw
E_3 packet is not asserted. The five-channel architecture and actual
source are retained, while this explicit accepted-space choice is stated.

Typed Cut, derived scalars and iota, lawful composition, declared targets
and response memory precede the admitted native positive pairing. Every
dagger below uses the specified domain and target pairing. A coordinate
matrix is a representation of those data, not a primitive Hilbert space.
Schur reduction and inverse updates are standard algebra; no priority
claim is made for their general mechanisms.

## 1. Theorem 1: derive all five columns from the same source

Let s be the bounded Hermitian form of the corrected SE5/SE21 source S_b
on its native completion X. Let ell be its actual boundary functional,
so the pure, pole-restored form is

\[
p[f]=s[f]+|\ell(f)|^2.                                  \tag{47.1}
\]

Choose a four-dimensional accepted space E with s|_E>0, and a bounded
direct-sum splitting X=E dotplus Y. Orthogonality in X is not required.
With an ordered basis of E, write

\[
s[e+y]=e^\dagger A e+2\operatorname{Re}\langle y,Ce\rangle_Y
                      +\langle y,Dy\rangle_Y,
\qquad \ell(y)=\langle b,y\rangle_Y.                    \tag{47.2}
\]

The X pairing restricted to Y defines b,C,D by Riesz representation.
Thus C's four columns are actual cross readings of s, and b is the
boundary reading restricted to the same Y. Set

\[
\boxed{
 R=D+bb^\dagger,\qquad
 W=[\,b\; C\,],\qquad
 G=\begin{pmatrix}1&0\\0&A\end{pmatrix}.}                \tag{47.3}
\]

R is the restriction of the pole-restored form (47.1) to Y. It is not
defined to be positive by notation. The accepted Schur form is exactly

\[
\boxed{F=D-CA^{-1}C^\dagger=R-WG^{-1}W^\dagger.}          \tag{47.4}
\]

**Theorem.** Suppose R is boundedly positive on Y. Then, with

\[
H=W^\dagger R^{-1}W,\qquad K=G-H,\qquad
B=G^{-1/2}HG^{-1/2},                                    \tag{47.5}
\]

Writing A=(a_ij) for i,j=1,...,4 and H=(h_ij) for i,j=0,...,4,
the explicit five-channel gap is

\[
K=\begin{pmatrix}
1-h_{00}&-h_{01}&-h_{02}&-h_{03}&-h_{04}\\
-h_{10}&a_{11}-h_{11}&a_{12}-h_{12}&a_{13}-h_{13}&a_{14}-h_{14}\\
-h_{20}&a_{21}-h_{21}&a_{22}-h_{22}&a_{23}-h_{23}&a_{24}-h_{24}\\
-h_{30}&a_{31}-h_{31}&a_{32}-h_{32}&a_{33}-h_{33}&a_{34}-h_{34}\\
-h_{40}&a_{41}-h_{41}&a_{42}-h_{42}&a_{43}-h_{43}&a_{44}-h_{44}
\end{pmatrix}.
\]

Here a_ji=conjugate(a_ij) and h_ji=conjugate(h_ij); the first
label is the boundary channel. The remaining four labels refer to
the accepted source states and their actual complementary couplings.

one has

\[
s\succeq0\ \Longleftrightarrow\ F\succeq0
\ \Longleftrightarrow\ K\succeq0
\ \Longleftrightarrow\ B\preceq I_5.                    \tag{47.6}
\]

Negative index and nullity of s equal those of K. The index may be read
as N_+(B-I_5). These conclusions also hold for finite matrices with
R>0, using their actual coordinate forms without choosing an orthonormal
basis.

**Proof.** Completing the accepted square in (47.2) gives

\[
s[e+y]=\|A^{1/2}(e+A^{-1}C^\dagger y)\|^2+
        \langle y,Fy\rangle_Y.
\]

Identity (47.4) follows by multiplying W G^(-1) W^dagger. Consider the
augmented block form

\[
J=\begin{pmatrix}R&W\\W^\dagger&G\end{pmatrix}.
\]

Eliminating G gives diag(F,G); eliminating R gives diag(R,K).
Both eliminated blocks are positive and both congruences are invertible.
Consequently the negative indices and nullities agree. Finally
K=G^(1/2)(I-B)G^(1/2). QED.

This theorem supplies the precise missing-column construction, rather
than inserting four arbitrary columns beside the known pole. It also
exposes the remaining global reference question. Positivity of R on
the infinite complement cannot be inferred from the size of W. For
example R=diag(1,-1), with W supported only on its first coordinate,
can give K>0 while F retains the unseen negative direction. A finite
five-matrix test is lawful only with its reference hypothesis retained.

At a noncoercive endpoint an inverse-half version needs b and C in the
positive-support energy domain, with all kernel residues retained. SE1
already states that contract. No such global endpoint regularity or
reference positivity is newly asserted here.

## 2. Theorem 2: the invariant five-channel operator and its comparison seam

The square-root-free operator on the five-label fibre is

\[
\boxed{T=G^{-1}H,\qquad
\Delta=(I+T)^{-1}(I-T)=(G+H)^{-1}(G-H).}                 \tag{47.7}
\]

H is a response Gram, whereas T is its action relative to the acquired
metric G. T is self-adjoint for the pairing <u,v>_G=u^dagger Gv; it is
similar to the Hermitian B of (47.5). G+H>0, so Delta exists.

**Theorem.** For every invertible change L of the five labels, transport

\[
W'=WL,\quad G'=L^\dagger GL,\quad H'=L^\dagger HL.
\]

Then K'=L^dagger K L, T'=L^(-1)TL and
Delta'=L^(-1)Delta L. In particular the generalized spectrum, sign
decision and comparison-seam kernel are invariant, and

\[
\boxed{\ker\Delta=\ker K=\{z:Hz=Gz\}.}                \tag{47.8}
\]

An eigenvalue beta of B gives the contrast (1-beta)/(1+beta).
Thus the neutral contrast identifies the unit threshold, not a coordinate
axis chosen beforehand.

**Proof.** The transformations follow by substitution in (47.5)--(47.7).
Also GT=H=T^dagger G; every real rational function of T is self-adjoint
in the same pairing, including Delta. The invertible left factor G+H
gives the kernel equality. Similarity to B and scalar evaluation prove
the spectral formula. QED.

This is a precise finite version of the proposed diagonal comparison:
the two complete readings Hz and Gz agree there. It is not a statement
that individual diagonal entries of H are primes, or that positive
diagonal entries of K imply K>=0. A positive Gram with upper-left block
((3/4,1/2),(1/2,3/4)) gives two positive diagonal entries of I-H but
also one negative eigenvalue. Mixed readings remain essential.

An explicit lawful marked-unit frame family is
L_Lambda=I+Lambda N with N^2=0. Its inverse is I-Lambda N, and the above
covariance holds coefficientwise. Its degree-zero cut recovers the same
original G,H,K; it does not set K to the neutral operator. Lambda and
the RH regularizing shift eta remain different parameters.

There is a second metric correction for shifted source calculations.
If the chosen E dotplus Y splitting is not X-orthogonal, the matrix of
eta I_X in these coordinates is **eta times the full native metric**,
including its mixed blocks. One must form A_eta,C_eta,D_eta from
s+eta<.,.>_X before applying (47.3). Replacing only the two diagonal
blocks by an identity shift silently changes the source. The executable
arithmetic run below is at eta=0 and makes no such substitution.

## 3. Theorem 3: retain correlations when the five-gap subtraction is small

For a finite source matrix of size n>=5, write

\[
M=\begin{pmatrix}A&C^\dagger\\C&D\end{pmatrix},
\quad b\in\mathbb C^{n-4},\quad A>0.
\]

Use exactly the R,W,G,K of (47.3)--(47.5). In the order (e,y,t), the
augmented form obeys

\[
\begin{aligned}
J[e,y,t]
 &=M[e,y]+|t+b^\dagger y|^2,\\
J&\sim_{\rm congruence}\operatorname{diag}(M,1)
 \sim_{\rm congruence}\operatorname{diag}(R,K).
\end{aligned}                                           \tag{47.9}
\]

**Theorem.** If M>0, then R>0 and K>0. This conclusion is valid for
every actual M in a positive source interval box, even if independently
boxed entries of G-H fail to give a positive interval LDL test.
Furthermore, let E_0 be the inclusion of the first four coordinates and
let b_0=(0,b)^T. With Z=[-b_0,E_0],

\[
\boxed{K^{-1}=e_0e_0^\dagger+Z^\dagger M^{-1}Z.}          \tag{47.10}
\]

This reciprocal reading retains the complete source correlations and
does not form a small gap by subtracting two nearly equal matrices.

**Proof.** The first identity in (47.9) is a direct expansion. Its
change of variables (e,y,t)->(e,y,t+b^dagger y) is invertible. If M>0,
then its principal D>0, so R=D+bb^dagger>0. The second Schur congruence
therefore gives K>0. All statements refer to the same M, C, D and b;
discarding this dependence is not part of the inference.

To prove (47.10), invert the first triangular change of variables in
(47.9), then take the inverse block indexed by (t,e). It equals the
right-hand side, while block inversion using R identifies it with
K^(-1). If M=L D_M L^dagger is a positive LDL factorization, the same
reading is e_0e_0^dagger+(L^(-1)Z)^dagger D_M^(-1)(L^(-1)Z), a positive
sum of retained response products. QED.

No numerical conditioning guarantee for every inversion is asserted.
The claim is an exact correlation-preserving identity and a sound
source-level positivity certificate. In particular the inverse matrix
formula is not used to estimate global endpoint energy without data.

## 4. Theorem 4: a new observation updates the same 5 by 5 matrix

Fix the accepted four states, the boundary functional, and a nested
family Y_n of observed complementary states. On Y_n let the positive
reference matrix be R_n and the five-source readout W_n. When one new
state is acquired, write

\[
R_{n+1}=\begin{pmatrix}R_n&u\\u^\dagger&r\end{pmatrix},
\qquad W_{n+1}=\begin{pmatrix}W_n\\w\end{pmatrix},
\]

and set d=r-u^dagger R_n^(-1)u, z=w-u^dagger R_n^(-1)W_n.

**Theorem.** If R_(n+1)>0, then d>0 and the exact retained update is

\[
\boxed{H_{n+1}=H_n+z^\dagger d^{-1}z,\qquad
       K_{n+1}=K_n-z^\dagger d^{-1}z.}                  \tag{47.11}
\]

The five-label output does not grow in size. The full mixed outer product
is required; five independent scalar diagonal updates are insufficient.

**Proof.** Eliminate u by the triangular block factorization of
R_(n+1). The same elimination changes W_(n+1) to (W_n,z)^T.
Its inverse-reference Gram is H_n+z^dagger d^(-1)z. Positivity gives
d>0, and G is unchanged because the accepted states are fixed. QED.

Consequently more observations can reveal an additional obstruction:
H increases and K decreases in form order. A sequence of successful
finite observations alone supplies no universal lower bound for K.
Maintaining the reference solve may require growing internal data; a
fixed output size is not a claim of constant computational cost.

For the global application, positivity of the reference on the complete
Y and a bound on the whole increasing response family remain substantive
requirements. They are not supplied by the 5 by 5 shape or by a change
of Lambda frame.

## 5. Actual corrected-source instantiation

Take SE21's states

\[
f_j(x)=\operatorname{sgn}(x)e^{-j|x|}/\sqrt2,\quad
V_N=\operatorname{span}\{f_1,\ldots,f_N\},\quad
E=\operatorname{span}\{f_2,f_3,f_4,f_5\}.                \tag{47.12}
\]

E is positive for the actual source by SE21's V_16 certificate. Define
a **fixed**, bounded projection Pi:X->E by the four L2 moment readings
against these accepted states. This is a representation-level observer
choice, not a change of the native source pairing. Explicitly,

\[
J_{ij}=\langle f_i,f_j\rangle_{L^2}=\frac1{i+j},\quad
c_{aj}=\sum_{i=2}^5(J_E^{-1})_{ai}\frac1{i+j},\quad
y_j=f_j-\sum_{a=2}^5c_{aj}f_a.                          \tag{47.13}
\]

Here j belongs to {1,6,7,...}. The four moments of y_j vanish. J_E>0
because the four exponentials are linearly independent. The inclusion
X->L2 is bounded, so these moment functionals and Pi are bounded on X;
Pi|_E=I. Thus X=E dotplus ker Pi is a genuine fixed splitting. SE21's
density theorem implies that the increasing Y_N=(I-Pi)V_N are dense in
ker Pi. Merely taking an unprojected moving remainder basis would not
establish this fixed global complement.

The actual boundary reading is known exactly:

\[
\ell(f_j)=\frac1{(j+1)(j+2)},\qquad
b_j=\ell(y_j)=\ell(f_j)-\sum_{a=2}^5c_{aj}\ell(f_a).
                                                               \tag{47.14}
\]

In particular b_1=1/450 is nonzero. All source entries, including
the four coupling columns, are obtained from the unchanged SE21 kernel

\[
s(f_r,f_q)=2\Phi[(r+3/2)^2,(q+3/2)^2],
\quad
\Phi(t)=\sqrt t\,\xi'(1/2+\sqrt t)/\xi(1/2+\sqrt t).
                                                               \tag{47.15}
\]

The execution consumes SE21's positive-real Gamma/prime/pole evaluation
with its full remainder bounds. It does not use a list of zeta zeros or
an RH premise. Equations (47.13)--(47.15), followed by (47.3), specify
every entry of the five-source object. Finite coordinate matrices of
R and W here are form and functional matrices; W^dagger R^(-1)W is the
coordinate-invariant energy Gram, not a silently Euclidean native adjoint.

The executed results are:

| Source space | Direct entrywise LDL of K | Same-source correlated conclusion |
| --- | --- | --- |
| V_5 | Positive; least lower pivot about 1.34533e-18 | K>0 |
| V_8 | Positive; least lower pivot about 2.43798e-28 | K>0 |
| V_12 | Positive; least lower pivot about 2.11411e-40 | K>0 |
| V_16 | Inconclusive after entrywise subtraction | K>0 by (47.9) and the unchanged full-source enclosure |

These pivots are not invariant eigenvalue gaps. The V_16 conclusion is
a new faithful five-channel representation of the already proved V_16
sign, not new positivity beyond V_16. The separately boxed five entries
have lost useful dependencies; the source reading retains them.

The boundary burden H_00 also rises sharply in this family: approximately
0.0230843, 0.993459, 0.999999999996831 and a value within 7e-22 below 1
at the four respective cutoffs. The exact enclosures are recorded. This
is one labelled channel, not the largest generalized eigenvalue and not
an estimate of eta. It illustrates why rounding to a few digits cannot
resolve the endpoint.

Five labels are not automatically minimal. Choosing E=span(f_1,...,f_4)
with this same moment construction absorbs the boundary functional:
its L2 Riesz function is f_1-f_2, so ell|_Y=0 and the first column
vanishes. The replay checks this controlled rank loss. The selected
E in (47.12) retains a nonzero boundary column without declaring five
to be an invariant lower bound for every possible accepted space.

## 6. What is now repaired, and what remains

The existing 1+4 operator now has an explicit current-source realization,
a fixed complement, an acquired five-label metric, an invariant
comparison seam, a correlation-preserving inverse reading and an exact
update from the next observation. It has been exercised on actual full
arithmetic source data, with separate rational negative controls.

It is not yet an evaluated global five-source endpoint. The historical
raw E_3 identification, global reference/energy-domain conditions and
the unobserved complement retain their boundaries. No theorem places
ordinary primes or zeta zeros on the five eigenvalues. Prime arithmetic
enters through the actual source in (47.15); diagonalization does not
generate it.

See [scope](SE47_SCOPE.md), [sources](SE47_SOURCE_RECORD.md),
[pins](SE47_SOURCE_PINS.json), [replay](../../../proof_lab/five_source_operator_repair.py)
and [readings](../../../proof_lab/FIVE_SOURCE_OPERATOR_REPAIR_RESULT.json).
RH remains open; global eta remains 1079/2000 with floor 1/492000.
The formal Lambda cut and the global spectral endpoint eta=0 are not
identified by a label change.
