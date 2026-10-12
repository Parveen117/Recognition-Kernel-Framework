# SE39: direct RH bridge and exact zero-sector readings

12 October 2026 (UTC). Owner: Monty.

Status: written derivation using the stated classical analytic inputs;
exact rational model controls. No proof of RH, global eta-zero certificate,
formal verification or independent review is claimed.

The user has reopened the RH application after SE38. The result here is
a direct equivalence between RH and the actual SE21 source sign, without
identifying the unresolved historical five-label attachment. It also
separates the source response into critical-line and off-line zero
sectors. The latter is an analytic identity, not a measured catalogue
of all zeta zeros. The remaining inequality is still unproved.

## 1. Native source, readings and explicit analytic adapter

Keep typed cuts, derived iota, lawful composition and Smriti before the
admitted T35/T40 graph representation. Use SE5's bounded self-adjoint
source S_b on X, with precisely SE21's normalization. For r>0 put

\[
 f_r(x)=\operatorname{sgn}(x)e^{-r|x|}/\sqrt2,
 \qquad t_r=(r+3/2)^2>9/4.
 \tag{SE39.1}
\]

SE21 proves that these states belong to X and that

\[
 s(f_r,f_q)=2\Phi[t_r,t_q],\qquad
 \Phi(t)=\sqrt t\,\frac{\xi'(1/2+\sqrt t)}{\xi(1/2+\sqrt t)},
 \tag{SE39.2}
\]

where Phi[t,u]=(Phi(t)-Phi(u))/(t-u) and Phi[t,t]=Phi'(t).
Both the mixed and diagonal readings include the complete Gamma, prime
and pole terms. SE21 also proves that V_N=span_C{f_1,...,f_N} has dense
union in X. Thus this is an adapter of an existing native source; it is
not a new primitive metric or a replacement source.
The scalar zero of an admitted analytic reading and the typed cut
operator have different types; no equality between them is assumed.

The classical inputs used below are explicit:

* The completed function xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 is
  entire of order one, obeys xi(s)=xi(1-s) and conjugation symmetry,
  and its zeros are the nontrivial zeta zeros. See [R1] and [R2].
* Hadamard factorization for entire functions of order less than one
  gives a genus-zero product with a constant prefactor [R3].
* Positivity of every finite divided-difference matrix on an open
  interval is equivalent to operator monotonicity. Such a function
  has a holomorphic upper-half-plane continuation with nonnegative
  imaginary part. These are Hansen's Theorems 3.2 and 5.4 [R4].

The last input is a classical analytic continuation theorem applied to
decoded native readings. It is not claimed to follow from formal unit
memory or from a definition of the cut. No mathematical priority for a
general zeta/Lowner criterion is asserted.

## 2. Theorem 1: entire response and exact zero-sector decomposition

There is an entire function H with real Taylor coefficients such that

\[
 H(w^2)=\xi(1/2+w),\qquad H(0)\ne0,
 \qquad \Phi(t)=2t\frac{H'(t)}{H(t)}.
 \tag{SE39.3}
\]

H has order at most 1/2. Let Z_H be its zeros, counted with
multiplicity. Then

\[
 H(t)=H(0)\prod_{a\in Z_H}(1-t/a),\qquad
 \sum_{a\in Z_H}|a|^{-1}<\infty,
 \tag{SE39.4}
\]

and, for t,u>9/4, including the continuous diagonal,

\[
 \boxed{\quad 2\Phi[t,u]
       =-4\sum_{a\in Z_H}\frac{a}{(t-a)(u-a)}.\quad}
 \tag{SE39.5}
\]

Each critical-line pair rho=1/2 plus/minus iota gamma, gamma>0,
with multiplicity m gives a=-gamma^2 of multiplicity m in H and
contributes

\[
 K_\gamma(t,u)=\frac{4m\gamma^2}{(t+\gamma^2)(u+\gamma^2)}.
 \tag{SE39.6}
\]

This is a positive rank-one kernel. Each off-line quartet gives a
nonreal conjugate pair a=x+iota y and conjugate(a), y!=0, in H.
Its real kernel is

\[
 K_a(t,u)=-8m\,\operatorname{Re}
                    \frac{a}{(t-a)(u-a)}.
 \tag{SE39.7}
\]

For any two distinct real points t_1,t_2>9/4 its determinant is

\[
 \boxed{\det\big(K_a(t_i,t_j)\big)_{i,j=1}^2
 =\frac{-64m^2|a|^2y^2(t_2-t_1)^2}
 {|t_1-a|^4|t_2-a|^4}<0.}
 \tag{SE39.8}
\]

**Proof.** The functional equation makes g(w)=xi(1/2+w) even. Its
even power series defines H, independently of a square-root branch.
The order-one growth bound for g implies the order-at-most-half bound
for H. There is no real zero of xi: for 0<s<1 the alternating series
E(s)=sum_{n>=1}(-1)^(n-1)n^(-s) is positive (group adjacent terms),
and zeta(s)=E(s)/(1-2^(1-s))<0. The endpoints xi(0)=xi(1)=1/2,
the positive-real Euler product, and reflection cover the remaining
real axis. In particular H(0)=xi(1/2)!=0. Zeta's nontrivial zeros
lie in the critical strip [R1]. A zero rho corresponds to
a=(rho-1/2)^2; since rho-1/2!=0, its multiplicity is preserved.

Hadamard's theorem now gives (SE39.4). Its zero-count estimate with
any exponent strictly between 1/2 and 1 proves the displayed absolute
summability. Logarithmic differentiation gives
Phi(t)=2 sum_a t/(t-a). This series and its derivatives converge
uniformly on compact sets avoiding the zeros: each large-|a| term
and each kernel term is O(1/|a|). Taking the divided difference
gives (SE39.5), with no omitted exponential term or prime cutoff.

Real zeros of H must be negative; positive ones would correspond to
real zeros of xi. A critical-line pair gives (SE39.6) directly. A
nonreal pair gives (SE39.7). To verify (SE39.8), set
v_i=1/(t_i-a). The two-by-two matrix is
-4m a vv^T-4m conjugate(a) conjugate(v) conjugate(v)^T. Its
determinant is 16m^2|a|^2(v_1 conjugate(v_2)-v_2 conjugate(v_1))^2.
The expression in parentheses equals
2 iota y(t_2-t_1)/(|t_1-a|^2|t_2-a|^2), proving the formula. QED.

An indefinite sector need not make a chosen finite full Gram indefinite.
Positive sectors can mask its negative direction at those probes.
The theorem does not permit discarding other sectors or replacing their
sum by the maximum of separate bounds.

## 3. Theorem 2: direct actual-source RH equivalence

The following statements are equivalent:

1. RH holds for the classical completed xi in (SE39.2).
2. The actual native source S_b is nonnegative on all of X.
3. M_N=(s(f_j,f_k))_(j,k=1,...,N) is positive semidefinite for every N.
4. Every finite matrix (Phi[t_i,t_j]) is positive semidefinite for
   arbitrary t_i>9/4.
5. Phi is operator monotone on (9/4,infinity).

If these conditions hold, M_N is in fact positive definite for every
finite N. None of the equivalent universal conditions is established
unconditionally by this theorem.

**Proof of 1 implies 2.** Under RH all zeros of H are negative. Write
them -gamma^2 with positive gamma and retain their multiplicities.
For any finite family of rates r_j and complex coefficients c_j,
Theorem 1 gives

\[
 s\!\left[\sum_j c_j f_{r_j}\right]
   =4\sum_{\gamma>0}m_\gamma\gamma^2
       \left|\sum_j\frac{c_j}{t_{r_j}+\gamma^2}\right|^2\ge0.
 \tag{SE39.9}
\]

The sum converges by (SE39.4). Positivity on the dense integer-rate
union extends to X by boundedness of s. For distinct rates, equality
would make the rational function sum_j c_j/(t_{r_j}+u) vanish at
infinitely many distinct positive u=gamma^2. Its numerator is a
polynomial, so it is identically zero; its distinct simple partial
fractions then give every c_j=0. There are infinitely many distinct
nontrivial zeros [R1], each of finite multiplicity. This proves the
strict finite assertion. This argument uses RH only in the stated
direction and is not an unconditional positive factorization.

**Proof of 2 implies 4 implies 5.** Any t>9/4 equals t_r for a unique
r>0. Equation (SE39.2) makes its divided-difference Gram half an
actual source Gram, so 2 implies 4. Apply the divided-difference
criterion of [R4] to the real analytic Phi to obtain 5.

**Proof of 5 implies 1.** By [R4], Phi has a holomorphic Pick
continuation F to the upper half-plane, agreeing analytically across
the interval (9/4,infinity). The globally meromorphic function
2tH'(t)/H(t) agrees with F near that interval. By the meromorphic
identity theorem they agree throughout the connected upper half-plane.
Consequently the former has no pole there.

If RH failed, a zero rho=beta+iota gamma would have beta!=1/2
and gamma!=0. Its image a=(rho-1/2)^2 is nonreal, with imaginary
part 2(beta-1/2)gamma. Conjugation supplies such an a in the upper
half-plane. If its multiplicity is m, write H(t)=(t-a)^m h(t),
h(a)!=0. Then 2tH'/H has residue 2ma!=0 at a. That pole cannot
be cancelled by another zero, since multiplicities add. This
contradicts the holomorphic continuation. Thus RH holds.

Finally, 2 and 3 are equivalent by SE21's native density theorem;
1 implies 2 implies 4 implies 5 implies 1 closes the cycle. QED.

This proves a direct classical attachment for the actual full odd
source. It does not prove equality with the historical five-label K_0,
construct its four missing columns, or validate its old abstract.
Those separate claims keep their previous boundary.

## 4. Theorem 3: the missing curvature branch and finite detection

Retain SE29's actual observer Gram T, diagonal Delta and curvature K:

\[
 \Delta=(I-T)(I+T)^{-1},\quad K=T(I+T)^{-2},\quad
 E_-=\mathbf1_{(-\infty,0)}(\Delta).
 \tag{SE39.10}
\]

Then the direct RH criterion can be written

\[
 \boxed{\mathrm{RH}\ \Longleftrightarrow\ S_b\succeq0
 \ \Longleftrightarrow\ E_-=0
 \ \Longleftrightarrow\ \|O_{*,0}\|=1.}
 \tag{SE39.11}
\]

In contrast, the canonical curvature has norm and essential norm
exactly 1/2 on the actual source, regardless of the unresolved sign.
Thus flatness of this particular connection is not the RH condition.

If RH is false, a finite integer-rate source reading has a strictly
negative result: there are N and c in (Q+iota Q)^N such that
c^dagger M_N c<0. This is an existence statement with no supplied
upper bound on N or coefficient size. It does not produce an actual
negative zeta-source reading.

**Proof.** SE29's bounded invertible congruence gives S_b>=0 iff
Delta>=0 iff E_-=0. SE5 gives S_b>=0 iff ||O_{*,0}||<=1 and also
||O_{*,0}||>=1, because 1 is in the essential spectrum of T.
Theorem 2 proves (SE39.11). The curvature norm is SE29 Theorem 3.

If RH fails, S_b is not nonnegative. Choose f with s[f]<0. Native
density and continuity give g in some V_N with s[g]<0. Rational
approximation of its finitely many complex coefficients preserves a
strict negative margin. QED.

In exact arithmetic, enumeration of all such rational coefficient
readings with successively sharper certified entry enclosures would
eventually detect any existing negative witness. A proof that the
enumeration never finds one is still the universal sign problem.
The current finite interval result supplies no finite stopping rule
for acceptance of RH.

## 5. Exact controls and the remaining development target

For the supplied model H_0(t)=(t+1)^2+1, the pair a=-1 plus/minus iota
has, at t_1=3,t_2=4, the source reading matrix

\[
 \begin{pmatrix}184/289&112/221\\112/221&68/169\end{pmatrix},
 \qquad \det=-32/48841.
 \tag{SE39.12}
\]

Every individual diagonal reading is positive, yet the mixed reading
detects a negative direction. For the same two probes, multiplying
H_0 by (t+1)^10(t+2)^10 adds two positive sectors and produces

\[
 \begin{pmatrix}18313/2890&3430/663\\3430/663&32128/7605\end{pmatrix},
 \qquad \det=57532/10989225>0.
 \tag{SE39.13}
\]

That model still has the nonreal pair. It shows explicitly why a
finite positive bank cannot exclude a hidden indefinite sector.
These are supplied polynomial models, not computations of xi zeros.
The [rational replay](../../../proof_lab/endpoint_rh_bridge_controls.py)
and [saved readings](../../../proof_lab/ENDPOINT_RH_BRIDGE_CONTROLS.json)
check the two independent response formulas, diagonal limits,
sector determinant and masking example using exact fractions.

The strongest inherited full-carrier numerical statement remains

\[
 S_b+\frac{1079}{2000}I_X\succeq\frac1{492000}I_X.
 \tag{SE39.14}
\]

It supplies the sufficient nonnegative shift 265433/492000 and is
not an enclosure of the exact optimal shift. The actual eta-zero
certificate remains restricted to V_16. Neither number changes here.

To finish by the present route one must prove all-order positivity of
the actual response (SE39.2), or construct an unconditional positive
factorization with analytic control of the complete source. Assuming
the zero support in (SE39.9) would assume RH. Choosing the positive
square root in Delta^2=I-4K would assume the missing branch. SE38's
finite formal unit-depth recovery supplies neither analytic estimate.
Its marked unit Lambda is not the spectral shift eta, and setting a
formal unit to its cut does not prove (SE39.14) at eta=0.

The useful advance is the explicit source-to-RH bridge and the sector
signal identity, with the precise branch still to be established.
See [scope and validation](SE39_SCOPE.md) and [source record](SE39_SOURCE_RECORD.md).

## References

[R1] NIST DLMF, [25.4](https://dlmf.nist.gov/25.4) (completed xi and
reflection), [25.10](https://dlmf.nist.gov/25.10) (zero location and
symmetry). Inspected 12 October 2026.

[R2] Noam D. Elkies, Math 229 (2022),
[The product formula for xi and zeta](https://people.math.harvard.edu/~elkies/M229.22/zeta2.pdf),
opening growth lemma. His xi lacks s(s-1)/2; the entire function in
that lemma is twice the completed xi used here.

[R3] Noam D. Elkies, Math 229 (2022),
[Functions of finite order](https://people.math.harvard.edu/~elkies/M229.22/prod.pdf),
opening Hadamard theorem and its logarithmic derivative.

[R4] Frank Hansen, *The fast track to Lowner's theorem*, Linear Algebra
and its Applications 438 (2013), 4557-4571,
[author preprint, Theorems 3.2 and 5.4](https://arxiv.org/pdf/1112.0098),
[DOI](https://doi.org/10.1016/j.laa.2013.01.022).
