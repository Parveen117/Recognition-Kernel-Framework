# SE46: ordered cell reconstruction with moving observers and retained memory

13 October 2026 (Asia/Kolkata). Author: Monty.

SE45 reconstructs a lifted scalar flux from bounded cell readings in a
common-J sector. This stage supplies the next finite operator step:
transport complete cell returns to a common response fibre and compose
them in a proved order. It recovers an entire noncommuting boundary
return, including any lawfully retained memory in the observation target.
Individual cell spectra do not suffice, even to recover the boundary
trace. The connecting paths are part of the observation data.

Rooted-tree normalization and non-Abelian loop composition are established
mathematical mechanisms. The contribution here is their explicit native
counting/observer contract, source attachment, and detached finite replay;
no external mathematical priority is claimed. The exact statements below
do not require a continuum limit, small cells, a physical clock or a
primitive Hilbert space.

## 1. Theorem 1: complete loop readings without a fixed observer

Begin with typed Cut, derived cut scalars, lawful response composition and
the declared target. Let G be a finite connected graph. At each vertex v
let E_v be a finite free response fibre of the same positive rank over a supplied
native coefficient carrier containing Q_Sigma. Each oriented edge e:u->v
has a supplied invertible linear response U_e:E_u->E_v; its reverse is
U_(bar e)=U_e^(-1). Composition uses the native product, written by
juxtaposition: later actions are on the left. On count-dependent entries
this is the SE42 formula product, not an undeclared ordinary x-product.

These are algebraic transport data. They need not come from a smooth
connection. The counting connection in Theorem 3 supplies one actual
source family. Identity I, an additive-neutral response, and the
primitive typed Cut are distinct objects throughout.

Choose an auxiliary root r and a spanning tree. Let t_v:E_r->E_v be
transport along its unique tree path, with t_r=I. Set

\[
L_e=t_v^{-1}U_e t_u.                                      \tag{46.1}
\]

**Theorem.** All tree edges have L_e=I. Every based-loop response is
exactly the corresponding ordered word in the non-tree L_e and their
inverses. Under arbitrary invertible vertex frames h_v,

\[
U_e^h=h_v^{-1}U_eh_u,\quad
t_v^h=h_v^{-1}t_vh_r,\quad
L_e^h=h_r^{-1}L_eh_r.                                    \tag{46.2}
\]

The non-tree tuple is therefore complete for all based-loop responses,
and its simultaneous conjugacy class is complete for vertex-frame
equivalence of the supplied edge systems. Count each edge/reverse pair
once in |E|. For an unrestricted rank-d edge protocol, its
b=|E|-|V|+1 non-tree matrices may be assigned
independently; omitting any one leaves its fundamental-loop target
undetermined.

**Proof.** A tree edge satisfies U_e t_u=t_v. For a path from u to v,
substitution of U_e=t_v L_e t_u^(-1) cancels every adjacent pair of tree
transports, giving U_path=t_v L_path t_u^(-1). The loop assertion follows
at r. The same cancellation in U_e^h gives (46.2).

For completeness, normalize a second system using t'_v. If
L'_e=C^(-1)L_e C for all non-tree edges, it holds also on tree edges.
The choices h_v=t_v C(t'_v)^(-1) then give
U'_e=h_v^(-1)U_eh_u on every edge. Conversely, (46.2) proves necessity.
Set every tree response to I and prescribe arbitrary invertible matrices
on the b chords to prove independence. With all retained chords I,
changing an omitted chord from I to A!=I changes its fundamental loop
while preserving the retained bank. QED.

The independence count is a matrix-target statement in this protocol,
not a universal scalar sensor lower bound under arbitrary encodings or
additional source equations. Complete cut/complement readings on a
labelled response basis recover U_e by the SE41 observer contract. Merely
recording a conjugacy class for each edge or cell does not supply their
relative calibration.

The root is an auxiliary comparison choice. If c:E_r->E_s is a retained
connector, the corresponding loop at s has response c H c^(-1).
Identity and conjugacy invariants are unchanged. A different spanning
tree generally changes different connectors by different loop words;
the associated cell order must be rederived. It is not generally one
simultaneous conjugation of the same individual cell list.

## 2. Theorem 2: the exact ordered rectangular reconstruction

Take vertices (i,j), 0<=i<=M and 0<=j<=N, with M,N positive integers.
Write A_ij for the edge (i,j)->(i+1,j), and B_ij for
(i,j)->(i,j+1). These are two labelled counting directions, not a
postulated Euclidean geometry of the TVSP plane. Use the comb tree
consisting of all horizontal edges and the left vertical column. Thus
t_ij first follows that column and then row j.

For each cell use the same forward comparison as SE45:

\[
P_{ij}=B_{i+1,j}A_{ij},\quad
Q_{ij}=A_{i,j+1}B_{ij},\quad
H_{ij}=Q_{ij}^{-1}P_{ij},\quad
F_{ij}=t_{ij}^{-1}H_{ij}t_{ij}.                           \tag{46.3}
\]

Here F_ij is a finite **transported cell return**. It is not itself the
infinitesimal curvature coefficient denoted by calligraphic F in SE42.
Let P_boundary go right along the bottom and then up the right column;
let Q_boundary go up the left column and then right along the top.

**Theorem.** With H_boundary=Q_boundary^(-1)P_boundary,

\[
\boxed{
H_{\partial}=
 (F_{0,N-1}F_{1,N-1}\cdots F_{M-1,N-1})\cdots
 (F_{0,0}F_{1,0}\cdots F_{M-1,0}).}                       \tag{46.4}
\]

The complete aligned face bank is equivalent to the MN independent
chord matrices. All faces equal I if and only if every loop of this
supplied discrete graph has identity response. The theorem is covariant
under independently moving vertex frames.

**Proof.** Normalize by the comb tree. Horizontal and left-column
responses become I. Put

\[
K_{ij}=t_{i,j+1}^{-1}B_{ij}t_{ij},\qquad K_{0j}=I.
\]

Equation (46.3), with its intermediate endpoints retained, gives

\[
F_{ij}=K_{ij}^{-1}K_{i+1,j},\qquad
K_{i+1,j}=K_{ij}F_{ij},\qquad
K_{Mj}=F_{0j}F_{1j}\cdots F_{M-1,j}.                     \tag{46.5}
\]

The normalized Q_boundary is I; P_boundary is
K_(M,N-1)...K_(M,0). This proves (46.4). The recursion (46.5) reconstructs
each of the MN chords from arbitrary supplied F_ij, and the first
identity recovers the faces. If every face is I, all normalized edges
are I, hence so is every loop by Theorem 1. Conversely identity of every
loop includes the transported cell loops. Finally (46.2) conjugates all
F_ij and H_boundary by the same h_(0,0), preserving (46.4). QED.

For a 2 by 2 grid the order is explicitly

\[
H_{\partial}=(F_{01}F_{11})(F_{00}F_{10}).                \tag{46.6}
\]

This is an exact finite identity, without a commutativity assumption.
It does not say that identity on finitely many sampled loops implies
flatness of an underlying continuum connection. An edge may already
have forgotten a full turn or another memory coordinate. Nor does one
identity boundary imply that all its cell returns are identity.

**A strict spectral-blindness witness.** Over the derived rational chart,
take

\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

The two 2 by 1 aligned face banks (A,B) and (A,A) have the same
individual conjugacy classes: B=S^(-1)AS for
S=((0,1),(1,0)). Each face has trace 2, determinant 1 and spectrum (1,1).
But (46.4) gives boundary traces tr(AB)=3 and tr(A^2)=2. Thus even a
conjugacy-invariant boundary target is lost by independently discarding
each cell's relative orientation. Complete aligned readings recover it.
This comparison deliberately uses more than AB versus BA, which are
similar when A is invertible.

## 3. Theorem 3: attachment to counting curvature and lawful subdivision

Use SE42's counting algebra B and response lifts
nabla_T=D_T+C and nabla_V=D_V+D, with count-independent response
matrices C,D. Their actual counting curvature is

\[
\mathcal F_{TV}=[C,D].                                   \tag{46.7}
\]

Along a forward line SE44 uses U'=-C U or U'=-D U. For central formal
count steps a,b the edge transports are
X=exp(-aC), Y=exp(-bD). Formal series, or an explicitly admitted
convergent representation, give the intended meaning of these expressions.

**Theorem.** The M by N constant-edge grid has

\[
H_{\partial}=(X^M Y^N)^{-1}Y^N X^M,\qquad
[ab](H_{\partial}-I)=-MN[C,D].                           \tag{46.8}
\]

Source-consistent subdivision leaves H_boundary unchanged. More
precisely, replace each coarse boundary edge by a composable fine path
with the same actual total response. Supply any compatible invertible
interior edges on the resulting rectangular refinement. The fine
ordered formula (46.4) equals the coarse boundary exactly.

**Proof.** Along P_boundary the response is Y^N X^M; along Q_boundary it
is X^M Y^N. Expanding X^M=I-MaC+O(a^2) and
Y^N=I-NbD+O(b^2), their difference P-Q has mixed coefficient
MN(DC-CD). Multiplication by Q^(-1), whose constant term is I, gives
(46.8). A subdivided boundary is obtained by substituting equal edge
products in each of the two paths. Hence P and Q are unchanged; apply
Theorem 2 to the fine grid. QED.

The sign in (46.8) is fixed by this forward horizontal comparison. It
differs from SE42's explicitly displayed positive-flow commutator word;
one cannot copy a sign while dropping its word. The refined interior
readings must describe the same supplied boundary source. Unconstrained
new edge values are not automatically a subdivision of the old source.

For an exact rational instance take C=E12, D=E21. Their squares vanish,
so X=I-aC and Y=I-bD exactly, with no convergence condition. The replay
uses a=1/3, b=1/2 on a 2 by 2 grid and half-steps on a 4 by 4 grid.
Both ordered cell banks recover the same boundary. Although the raw
cell H_ij is constant, the common-root F_ij need not be; the connectors
retain the noncommuting relation between cells.

## 4. Theorem 4: the first unit layer lost by order-blind addition

Use the separated unit-memory completion of SE34 on a fixed finite
response sector. Lambda is the central constant marked unit. For
m>=1 and Lambda-independent response operators X_1,...,X_k define
F_i=exp(Lambda^m X_i), in their **already specified boundary product
order**. All coefficients are interpreted in the native rational
response algebra. Set

\[
\log(I+R)=\sum_{n\geq1}(-1)^{n+1}R^n/n,
\qquad R\in\Lambda\operatorname{End}(E)[[\Lambda]].
\]

**Theorem.** The formal logarithm is well defined coefficient by
coefficient and

\[
\boxed{
\log(F_1\cdots F_k)
=\Lambda^m\sum_i X_i
 +\frac{\Lambda^{2m}}2\sum_{i<j}[X_i,X_j]
 +O(\Lambda^{3m}).}                                     \tag{46.9}
\]

It is equivariant under simultaneous invertible frame conjugation.
The generator sum alone can vanish while the complete product has a
nonzero reading at unit depth 2m.

**Proof.** Put s=Lambda^m and expand the ordered product:

\[
F_1\cdots F_k=I+sA+s^2B+O(s^3),\quad
A=\sum_iX_i,\quad B=\tfrac12\sum_iX_i^2+\sum_{i<j}X_iX_j.
\]

Through degree two the logarithm is sA+s^2(B-A^2/2). Pairing the
off-diagonal terms gives half the displayed commutator sum. Positive
unit order makes only finitely many terms contribute to any retained
coefficient. Conjugation commutes with each finite coefficient
calculation and therefore with the completed series. For the explicit
word exp(-sA)exp(-sB)exp(sA)exp(sB), where A=E12 and B=E21, the generator
sum is neutral but the coefficient of s^2 is
[A,B]=diag(1,-1)!=0. Its lower positive unit coefficients vanish. QED.

Thus a cut through depth less than 2m misses that particular target;
depth 2m recovers its first nonzero coefficient. This is a sharp example,
not a universal bound on the depth of every possible word: other
cancellations may delay the first nonzero coefficient. The logarithm
here is formal near the unit. No arbitrary numerical convergence,
global matrix-log branch, or winding number is inferred from it.

For the actual count lifts C=Lambda^m E12, D=Lambda^m E21,
the curvature is Lambda^(2m)[E12,E21]. Formula (46.8) gives leading
boundary coefficient -MNab[E12,E21] at that same depth. The finite
replay uses m=2 and retains coefficients through degree 8. Setting the
degree-zero cut to identity does not erase the higher recorded layers.

## 5. Theorem 5: retain the memory lift before reconstructing

Let pi:tilde G->G be a supplied homomorphism of response groups, or the
corresponding functor between invertible typed path carriers. Each edge
has a retained lift with a lawful inverse. This includes the invertible
case of MR-03's normalized cocycle extension, with its actual lifted
composition rather than componentwise multiplication by assumption.

**Theorem.** The tree and rectangular identities (46.1)--(46.5) hold in
the lifted carrier, and project to the corresponding identities in G.
If only the projected readings are retained, they do not in general
determine the lifted boundary. In a group extension with central kernel,
a lifted boundary over projected identity lies in that kernel and is
unchanged by conjugating its base frame within the lifted group.

**Proof.** The proofs above use only identities, associativity,
composition of compatible arrows and inverses. They therefore hold for
the lifted arrows themselves. The functor preserves each operation and
so preserves the identities. A nontrivial kernel can contain different
lifts with the same projection. If pi(tilde H)=I, then tilde H is in the
kernel; centrality gives c tilde H c^(-1)=tilde H. QED.

For a concrete collision use GL_2(Q_Sigma) x Z with its declared
additive integer memory; this is MR-03's zero-cocycle specialization.
Its faithful five-channel adapter is

\[
\rho(M,k)=\operatorname{diag}(M,I_3+kE_{13}).             \tag{46.10}
\]

It is a homomorphism because E13^2=0; projection keeps the first block.
Compare aligned 2 by 1 face banks ((A,1),(A^(-1),0)) and
((A,0),(A^(-1),0)). Every projected face and projected edge constructed
by (46.5) agrees; both projected boundaries are I. Their lifted
boundaries are (I,1) and (I,0), distinguished by complete acquired
readings. The integer is declared retained memory, not an automatically
recovered winding number for arbitrary matrices. Neither a formal
logarithm nor a finer multiplication of already projected matrices
recreates a forgotten kernel coordinate.

## 6. Theorem 6: a finite observation budget for the assembled return

Now admit a specified normed response representation with
submultiplicative norm. Let the fixed-order boundary be H=F_1...F_k,
and its measured reconstruction be hat H=hat F_1...hat F_k, with
declared factor error bounds ||hat F_i-F_i||<=epsilon_i.

**Theorem.** One has the exact identity and consequent bound

\[
\widehat H-H=
\sum_i(\widehat F_1\cdots\widehat F_{i-1})
 (\widehat F_i-F_i)(F_{i+1}\cdots F_k),                  \tag{46.11}
\]

\[
\|\widehat H-H\|\leq
\sum_i\left(\prod_{j<i}\|\widehat F_j\|\right)
 \epsilon_i\left(\prod_{j>i}\|F_j\|\right)=:E.         \tag{46.12}
\]

If all true and estimated factors are unitary for the admitted native
positive pairing, their associated operator norm is one and E=sum_i
epsilon_i suffices. For a single transported factor F=t^(-1)Ht with
both true and estimated H,t unitary and with bounds epsilon_H,epsilon_t,

\[
\|\widehat t^{-1}\widehat H\widehat t-t^{-1}Ht\|
\leq\epsilon_H+2\epsilon_t.                            \tag{46.13}
\]

In particular, ||hat H-I||>E certifies H!=I. A residual at most E by
itself does not certify H=I.

**Proof.** Replace product factors one at a time, retaining estimated
prefixes and true suffixes; the intermediate products telescope to
(46.11). Submultiplicativity and the triangle inequality give (46.12).
For unitaries ||hat t^(-1)-t^(-1)||=||hat t-t||. Apply the same three-factor
identity to hat t^(-1) hat H hat t and t^(-1)Ht to obtain (46.13).
Finally H=I would force ||hat H-I||<=E. For failure of the converse,
a nonidentity rational turn arbitrarily close to I has residual below
any supplied positive E. QED.

These are supplied error hypotheses, not errors inferred merely from
successful closure. After changing frames, the pairing and norm must be
transported too; an undeclared fixed coordinate norm is not an invariant.
The replay uses exact rational three-channel turns in a declared positive
pairing, epsilon_H=1/40 and epsilon_t=1/50. Each aligned factor has bound
13/200; two factors have bound 13/100. Exact rational positive-semidefinite
checks verify those inequalities and a measured nonidentity decision.
A separate nonunitary example verifies the full product-weighted bound.

## 7. What this stage permits next

Complete observer readings can now be assembled across a finite family
of noncommuting cells without choosing a physically privileged observer.
The assembly retains calibrated relative orientations, ordered mixed
unit coefficients, and any declared lifted memory. It can therefore feed
the previously derived source-preserving feedback with a full return
target instead of an order-blind scalar sum. This is a reconstruction
interface; it is not a new nonlinear convergence theorem for arbitrary
nonunitary returns or unknown source drift.

See [scope](SE46_SCOPE.md), [source comparison](SE46_SOURCE_RECORD.md),
[pins](SE46_SOURCE_PINS.json), [finite replay](../../proof_lab/ordered_cell_reconstruction.py)
and [recorded readings](../../proof_lab/ORDERED_CELL_RECONSTRUCTION_RESULT.json).
Finite readings, written general proofs, formal verification and external
review remain separate. Lambda is not the RH shift eta. The actual RH
source retains global eta 1079/2000 with floor 1/492000; eta zero is
certified on V_16 only, and universal source positivity remains open.
No Yang--Mills mass gap or universal physical TVSP geometry is proved.
