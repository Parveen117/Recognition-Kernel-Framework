# O15 — Native Cut/Seam Object Certification and Repair Theorems

**Author:** Monty Dabas

**Classification:** mixed `PROVED / CONDITIONAL / OPEN`, itemized below

**Source draft:** `NEW maths objects(1).tex`, SHA-256
`68316205bd169a7b6592dadef3e0d1f909b6240e29e2b8a6ad94e7297bdf21ea`

## 0. Certification boundary

Let the native cut-complex field be

\[
\mathbb C_\Sigma=\mathbb R_\Sigma\oplus\iota_\Sigma\mathbb R_\Sigma,
\qquad \iota_\Sigma^2=-1,
\qquad (a+\iota_\Sigma b)^\dagger=a-\iota_\Sigma b.
\]

This is inherited from the proved foundation sequence F00-E through F00-I.
The seam is a declared distinguished locus or typed subobject; it is not, by
notation alone, a metric, Hilbert space, physical detector, or spectral model.

Every theorem below names its hypotheses.  Classical differential topology and
complex analysis appear only in explicitly labelled bridge statements.

---

## O01. Normalized seam Jacobian

### Definition O01-D

Let `f=(f_1,...,f_n)` be nonvanishing and diagonally separated in seam
coordinates, and let

\[
L_{jk}(f):=f_j^{-1}\partial_{\theta_k}f_j,
\qquad
\varepsilon:=\frac{w^2}{h},\quad h>0.
\]

Define

\[
\boxed{J_\Sigma(f;\varepsilon)=\det(L(f)+\varepsilon I_n).}
\]

### Theorem O01-T — `PROVED_REPAIRED`

If `partial_{theta_k} f_j = iota_Sigma f_j delta_jk`, then

\[
J_\Sigma=(\iota_\Sigma+\varepsilon)^n,
\qquad
J_\Sigma^\dagger J_\Sigma=(1+\varepsilon^2)^n,
\qquad
\lim_{h\to\infty}J_\Sigma=\iota_\Sigma^n.
\]

**Proof.** The normalized logarithmic derivative is
`L=iota_Sigma I_n`; hence the determinant is the product of the diagonal
entries.  Multiplication by the dagger gives
`(-iota+epsilon)(iota+epsilon)=1+epsilon^2`.  The limit follows from
`epsilon=w^2/h -> 0`.  ∎

**Repair.** Without normalization by `f_j`, the source determinant is
`prod_j(iota_Sigma f_j+epsilon)`, not `(iota_Sigma+epsilon)^n`.

---

## O02. Rank-one winding metric

### Definition O02-D

For a radial vector `w in R_Sigma^n` and `h>0`, define

\[
\boxed{g_w=I_n+\frac{1}{h^2}ww^\top.}
\]

### Theorem O02-T — `PROVED_REPAIRED`

The form is symmetric and positive definite, with

\[
\det g_w=1+\frac{w^\top w}{h^2},
\]

\[
g_w^{-1}=I_n-
\frac{ww^\top}{h^2+w^\top w}.
\]

**Proof.** For nonzero `v`,

\[
v^\top g_wv=v^\top v+\frac{(w^\top v)^2}{h^2}>0.
\]

The determinant and inverse follow by the rank-one determinant lemma and a
direct multiplication.  ∎

**Refuted source subclaim.** This `g_w` is not indefinite.  An indefinite
signature needs a separately declared base form or a negative rank-one sign.
The contour formula `oint dw_i/dtheta_j dtheta` does not by itself imply
symmetry or this rank-one formula.  A geometric geodesic equation therefore
remains `OPEN` until a connection is derived from a specified coordinate
dependence `w(theta)`.

---

## O03. Cut cohomology of a seam complex

### Definition O03-D

Let `(C_cut^bullet,delta_Sigma)` be a graded native module with
`delta_Sigma^2=0`.  Define

\[
\boxed{H^q_{\rm cut}:=\ker(\delta_\Sigma:C^q\to C^{q+1})/
\operatorname{im}(\delta_\Sigma:C^{q-1}\to C^q).}
\]

### Theorem O03-T1 — `PROVED_ABSTRACT`

The quotient is well defined.  If the complex is finite-dimensional and only
finitely many degrees are nonzero, then

\[
\sum_q(-1)^q\dim H^q_{\rm cut}
=
\sum_q(-1)^q\dim C^q_{\rm cut}.
\]

**Proof.** Nilpotence gives `im delta subset ker delta`.  Apply rank-nullity in
each degree; the boundary dimensions cancel in the alternating sum.  ∎

### Bridge O03-B — `CONDITIONAL`

If a seam differential complex is proved chain-isomorphic to the relative de
Rham complex `Omega^bullet(M,Sigma)`, then

\[
H^q_{\rm cut}(M)\cong H^q_{\rm dR}(M,\Sigma).
\]

The isomorphism is not obtained merely by saying that differentiation is
"perpendicular to the seam"; a chain map and its inverse or quasi-isomorphism
must be supplied.

---

## O04. Cyclic information tensor

### Definition O04-D

For one-forms `alpha,beta,gamma`, set

\[
\boxed{\mathcal T(\alpha,\beta,\gamma)
=\alpha\otimes\beta+\beta\otimes\gamma+\gamma\otimes\alpha.}
\]

### Theorem O04-T — `PROVED_REPAIRED`

The tensor is invariant under cyclic permutation of its three inputs:

\[
\mathcal T(\alpha,\beta,\gamma)
=\mathcal T(\beta,\gamma,\alpha).
\]

For a declared pairing,

\[
\operatorname{tr}\mathcal T
=\langle\alpha,\beta\rangle
+\langle\beta,\gamma\rangle
+\langle\gamma,\alpha\rangle.
\]

**Proof.** Cyclic permutation reorders the same three summands.  Contraction of
each elementary tensor gives the trace formula.  ∎

**Refuted source subclaim.** The component expression
`T_AB+T_BC+T_CA=0` is not a tensor identity for arbitrary inputs.  It may be
added only as an extra seam constraint and is not used here.

---

## O05. Native prime seam lattice

### Definition O05-D

Using F00-G/H, for every native prime `p` define

\[
\boxed{\kappa(p)=\left(\operatorname{Log}_\Sigma p,
\frac{2\pi_\Sigma}{p}\right),
\qquad
\mathcal K_{\rm prime}=\{\kappa(p):p\text{ prime}\}.}
\]

### Theorem O05-T — `PROVED`

The map `kappa` is injective and the prime lattice is locally finite in its
classical coordinate chart.

**Proof.** Equality of second coordinates gives `1/p=1/q`, hence `p=q`.
For local finiteness, a bounded first coordinate bounds `log p`, hence bounds
`p`; only finitely many natural numbers, and therefore primes, occur below that
bound.  ∎

For a finite prime set `P`, its exact Fourier polynomial is

\[
\widehat\rho_P(u,v)=\sum_{p\in P}
e^{-iu\operatorname{Log}_\Sigma p}
e^{-iv,2\pi_\Sigma/p}.
\]

**Open boundary.** No identity with `zeta(1/2+iu)` follows from this definition.
An infinite Fourier distribution requires a test-function/regularization
contract.  The spacing claims in the source are not certified.

---

## O06. Finite-support cut character

### Definition O06-D

For `k=(k_j)` with finite support, define `sinc(0)=1` and

\[
\boxed{\chi_{\rm cut}(k)=
\prod_{j\in\operatorname{supp}k}
\frac{\sin(\pi k_j/4)}{\pi k_j/4}.}
\]

### Theorem O06-T — `PROVED_REPAIRED`

\[
\chi_{\rm cut}(0)=1,
\qquad
|\chi_{\rm cut}(k)|\le1,
\]

and `chi_cut(k)=0` whenever some nonzero component belongs to `4Z`.
On a finite torus of dimension `d`, normalized Haar integration gives

\[
\frac1{(2\pi)^d}\int_{\mathbb T^d}
\chi(k)\overline{\chi(k')}e^{i(k-k')\cdot\theta},d\theta
=|\chi(k)|^2\delta_{kk'}.
\]

**Proof.** These are the sinc bound, its integer zeros, and character
orthogonality.  ∎

**Repair.** The right side is not `delta_kk'` unless the nonzero weights are
normalized to unit modulus.  No unspecified infinite-dimensional Haar measure
is used.

---

## O07. Finite seam determinant

### Definition O07-D

For a finite `N`-dimensional carrier with eigenvalue multiset
`lambda_a=1+iota_Sigma nu_a`, define

\[
\boxed{\operatorname{sdet}_{\Sigma,N}(C;w)
=e^{-Nw^2}\prod_{a=1}^{N}(1+\iota_\Sigma\nu_a).}
\]

### Theorem O07-T — `PROVED_FINITE`

This equals `e^{-Nw^2} det(C)` in every proved splitting chart, is independent
of eigenvalue ordering, and vanishes exactly when one eigenvalue vanishes.

**Proof.** It is the finite determinant product, multiplied by a nonzero scalar.
∎

**Open boundary.** The source infinite product is not certified.  Repeating
`e^{-w^2}` once per mode does not regularize arbitrary eigenvalue growth.  A
Fredholm, zeta, or relative determinant requires its own operator domain,
summability theorem, and regularization independence.  The proposed
Dabas--Euler contour identity remains `OPEN`.

---

## O08. Lambda-weighted residue pair

Let `a=lambda-1`, and let `f` be meromorphic near isolated singularities.

### Definitions O08-D

The contour-compatible weighted residue is

\[
\boxed{R_\lambda(f;z_0)
=\operatorname{Res}_{z=z_0}\left(f(z)e^{\iota_\Sigma a z}\right).}
\]

The source-normalized local coefficient is

\[
\boxed{\widetilde R_\lambda(f;z_0)
=e^{-\iota_\Sigma a z_0}R_\lambda(f;z_0).}
\]

### Theorem O08-T — `PROVED_REPAIRED`

For a contour enclosing finitely many poles,

\[
\frac1{2\pi\iota_\Sigma}\oint_\gamma
f(z)e^{\iota_\Sigma a z}\,dz
=\sum_{z_k}R_\lambda(f;z_k)
=\sum_{z_k}e^{\iota_\Sigma a z_k}
\widetilde R_\lambda(f;z_k).
\]

**Proof.** Apply the ordinary residue theorem in the admitted complex chart to
the meromorphic product `f(z)e^{iota a z}` and substitute the second
definition.  ∎

For a simple pole of `f`, the normalized coefficient equals the ordinary
residue of `f`; for higher-order poles it mixes finitely many principal Laurent
coefficients.  This prevents the sign and normalization ambiguity in the
source example.

---

## O09. Logarithmic cut Fourier transform

### Definition O09-D

For a Schwartz function `F` on the radial line and `omega>0`, define

\[
\boxed{\mathcal F_{\rm cut}F(\omega)
=\int_{-\infty}^{\infty}
F(t)e^{-\iota_\Sigma t\operatorname{Log}_\Sigma\omega}\,dt.}
\]

### Theorem O09-T — `PROVED_WITH_DOMAIN`

This is the ordinary Fourier transform in the logarithmic coordinate
`x=Log_Sigma omega`.  Consequently,

\[
F(t)=\frac1{2\pi_\Sigma}\int_0^\infty
\mathcal F_{\rm cut}F(\omega)
e^{\iota_\Sigma t\operatorname{Log}_\Sigma\omega}
\frac{d\omega}{\omega},
\]

with the usual Schwartz/L2 interpretation.  If
`(T_aF)(t)=F(t-a)`, then

\[
\mathcal F_{\rm cut}(T_aF)(\omega)
=e^{-\iota_\Sigma a\operatorname{Log}_\Sigma\omega}
\mathcal F_{\rm cut}F(\omega).
\]

**Proof.** Substitute `x=Log_Sigma omega`, so `dx=domega/omega`, and apply
Fourier inversion and the translation law in the earned chart.  ∎

**Open boundary.** A distributional formula for zeta requires a correctly
typed Mellin distribution and convergence/continuation theorem; the variable-
mismatched source equality is not certified.

---

## O10. Seam winding index

### Definition O10-D

For a `C^1` nonvanishing loop `u:S^1 -> C_Sigma^*`, define

\[
\boxed{W_\Sigma(u)=\frac1{2\pi\iota_\Sigma}
\oint_{S^1}u^{-1}du.}
\]

### Theorem O10-T — `PROVED_WITH_NONVANISHING`

`W_Sigma(u)` is an integer in a classical complex chart, is invariant under
every homotopy through nonvanishing loops, and satisfies

\[
W_\Sigma(uv)=W_\Sigma(u)+W_\Sigma(v).
\]

**Proof.** Lift the phase locally around the circle; the total phase change is
an integer multiple of `2pi`.  Differentiating a nonvanishing homotopy gives an
exact periodic derivative, whose integral vanishes.  The product identity is
`(uv)^{-1}d(uv)=u^{-1}du+v^{-1}dv` in the commutative scalar chart.  ∎

For

\[
u_w(h,\theta)=
\tanh((h-h_0)/\sqrt2)e^{\iota_\Sigma w\theta},
\]

one has `W_Sigma=w` for `h != h_0`.  At `h=h_0` the loop vanishes and the
winding number is undefined; conservation cannot cross that singular slice
without an additional defect law.

---

## O11. Seam-tangent module (log tangent bundle bridge)

### Definition O11-D

For a smooth manifold `M` with embedded hypersurface `Sigma`, define

\[
\boxed{\mathcal V_\Sigma(M)
=\{X\in\Gamma(TM):X|_\Sigma\in\Gamma(T\Sigma)\}.}
\]

### Theorem O11-T — `PROVED_REPAIRED`

In an adapted chart `(x,y_1,...,y_{n-1})` with `Sigma={x=0}`, this module is
locally free with basis

\[
x\partial_x,\partial_{y_1},\ldots,\partial_{y_{n-1}}.
\]

Hence it is the section module of a rank-`n` vector bundle, the seam/log tangent
bundle.

**Proof.** Tangency says that the normal coefficient of `X` vanishes at `x=0`;
smooth divisibility gives that coefficient as `x a(x,y)`.  The displayed local
frame follows.  ∎

**Repair.** The source fibre `T_xSigma direct-sum R n` is just `T_xM` after a
chosen splitting and does not encode the tangency condition.  The proposed
connection correction remains `OPEN` until it is shown to transform as a
connection and preserve the seam-tangent module.

---

## O12. Eye asymptotic coefficient operator

### Definition O12-D

Let `A_h` and `A_0` act on a declared common Banach/Hilbert chart and suppose

\[
A_h=A_0+e^{-w^2h}E+R_h.
\]

Define the Eye coefficient, when the limit exists in the declared topology, by

\[
\boxed{\Delta_{\rm eye}
=\lim_{h\to\infty}e^{w^2h}(A_h-A_0).}
\]

### Theorem O12-T — `PROVED_CONDITIONAL_EXTRACTION`

If `e^{w^2h}||R_h|| -> 0` in operator norm, then

\[
\Delta_{\rm eye}=E.
\]

If each operator is self-adjoint and the convergence assumptions preserve the
common domain as stated, then the limit coefficient is self-adjoint whenever
`E` is self-adjoint.

**Proof.** Multiply the expansion by `e^{w^2h}` and take the declared norm
limit.  ∎

### Spectral/RH boundary — `OPEN`

No theorem in this package identifies `Spec(E)` with zeta zeros or proves

\[
\mathrm{RH}\Longleftrightarrow E\ge0.
\]

Such a statement needs a separately proved spectral adapter, reality/self-
adjointness of the relevant spectral encoding, equivalence in both directions,
and domain/resolvent control.  The Class F audit below cannot promote it.

---

## O13. Renormalized prime exponential form

### Refutation O13-R — `REFUTED_AS_STATED`

The raw series

\[
\sum_p e^{2\pi\iota_\Sigma\tau/p}
\]

diverges for every fixed `tau`, because its terms tend to `1`, not `0`.

### Definition O13-D

The second-order renormalized object is

\[
\boxed{F_{\rm prime}^{[2]}(\tau)
=\sum_p\left(
e^{2\pi\iota_\Sigma\tau/p}-1-
\frac{2\pi\iota_\Sigma\tau}{p}
\right).}
\]

### Theorem O13-T — `PROVED_REPAIRED`

The series converges absolutely and locally uniformly for `tau` in every
bounded subset of the complex chart; therefore it defines an entire function.

**Proof.** On `|tau|<=R`, Taylor's theorem gives a constant `C_R` such that
the summand has modulus at most `C_R/p^2`.  Since the primes are a subset of
the integers and `sum_{n>=2}1/n^2` converges, the Weierstrass M-test applies.
∎

**Open boundary.** No modular transformation law is claimed.  Modularity of a
completion remains a separate conjectural programme.

---

## O14. Seam prime-zeta deformation

### Definition O14-D

For `Re(s)>1`, define

\[
\boxed{\zeta_\Sigma(s)=
\sum_p p^{-s}e^{-2\pi\iota_\Sigma/p}.}
\]

### Theorem O14-T — `PROVED_ON_HALF_PLANE`

The series converges absolutely and locally uniformly on `Re(s)>1`.  In that
half-plane,

\[
\boxed{\zeta_\Sigma(s)=
\sum_{m=0}^{\infty}
\frac{(-2\pi\iota_\Sigma)^m}{m!}P(s+m),}
\]

where `P(s)=sum_p p^{-s}` is the prime zeta function.

**Proof.** Absolute convergence follows from
`|p^{-s}e^{-2pi iota/p}|=p^{-Re(s)}`.  Expand the exponential.  On compact
subsets of `Re(s)>1`, the resulting double series is absolutely dominated, so
the sums may be interchanged.  ∎

**Open boundary.** Analytic continuation, a functional equation, and the
proposed zero locations are not consequences of the definition and remain
`OPEN`.  No RH statement is promoted.

---

## O15. Cut Grassmannian repair

Let `V` have dimension `n`, and let `H` be a hyperplane.

### Collapse theorem O15-T1 — `PROVED`

For every `k`-plane `W`,

\[
\dim(W\cap H)\ge k-1.
\]

Therefore the source set

\[
\{W\in\operatorname{Gr}(k,V):\dim(W\cap H)\ge k-1\}
\]

equals the full Grassmannian and has dimension `k(n-k)`, not
`k(n-k)-1`.

**Proof.** The dimension inequality
`dim(W cap H) >= dim W + dim H - dim V` gives `k+(n-1)-n=k-1`.  ∎

### Definition O15-D2 — nontrivial cut divisor

Fix instead an `(n-k)`-dimensional subspace `F_{n-k}` and define

\[
\boxed{\operatorname{Gr}_\Sigma(n,k;F)
=\{W\in\operatorname{Gr}(k,V):
\dim(W\cap F_{n-k})\ge1\}.}
\]

### Theorem O15-T2 — `PROVED_CLASSICAL_BRIDGE`

This is the standard Schubert divisor.  It is a closed hyperplane section in
Plucker coordinates and, when nonempty and proper, has

\[
\dim\operatorname{Gr}_\Sigma(n,k;F)=k(n-k)-1.
\]

**Proof.** The projection `W -> V/F_{n-k}` is a map between `k`-dimensional
spaces.  The intersection is nonzero exactly when its determinant vanishes.
That determinant is one linear Plucker equation, giving a codimension-one
closed subvariety.  ∎

---

## Final status ledger

| ID | Object | Certified core | Unpromoted boundary |
|---|---|---|---|
| O01 | Seam Jacobian | normalized determinant and magnitude | unnormalized source formula |
| O02 | Winding metric | rank-one positive metric | indefiniteness/geodesic claim |
| O03 | Cut cohomology | abstract complex and Euler identity | relative de Rham bridge without chain map |
| O04 | Cyclic tensor | cyclic input invariance and trace | claimed zero component sum |
| O05 | Prime lattice | injection and local finiteness | zeta Fourier identity/spacing |
| O06 | Cut character | finite-support sinc character | unit orthogonality/infinite Haar form |
| O07 | Seam determinant | finite carrier | infinite product and Dabas--Euler identity |
| O08 | Lambda residue | weighted residue theorem | source normalization without weights |
| O09 | Cut Fourier | log-Fourier/Mellin chart | source zeta distribution identity |
| O10 | Soliton winding | nonvanishing-loop homotopy invariant | passage through kink zero |
| O11 | Seam tangent | log-tangent module | proposed connection correction |
| O12 | Eye operator | asymptotic coefficient lemma | zeta spectrum and RH equivalence |
| O13 | Prime exponential | second-order renormalized entire form | raw series and modularity |
| O14 | Seam zeta | half-plane series and prime-zeta expansion | continuation/FE/zero law |
| O15 | Cut Grassmannian | collapse theorem and repaired divisor | source codimension claim |

## Programme conclusion

The catalogue does generate a coherent family, but the common principle is not
the symbolic equation `Object * Seam = Eye`.  The certified common principle is

\[
\boxed{
\text{typed distinction}
\longrightarrow
\text{well-defined object}
\longrightarrow
\text{retained seam information}
\longrightarrow
\text{proved invariant or explicit open residue}.}
\]

That formulation is strong enough to generate new mathematics and strict
enough to prevent an evocative analogy from being mistaken for a theorem.
