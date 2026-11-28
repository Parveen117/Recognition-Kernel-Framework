# Arithmetic and spectral transforms

Which rules act on numerals, prime factors, series coefficients and spectra?

13 source rules · 1 specified model

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="triple-add"></a>
## Lifted UGD addition

*Source rule.* In the draft’s lifted triple chart (a,s,k), with angle lift a, scale s and seam component k, add coordinates componentwise. The scalar reading π(a,s,k)=s preserves addition.

**Example.** (1,2,3) plus (4,5,6) gives (5,7,9), whose scalar reading is 2+5=7.

This is the addition in this historical chart. Angle addition descends modulo 2π. Multiplication needs additional care.

[A43 · §§1–4](sources.md#s-a43) · [A45 · §2](sources.md#s-a45)

<a id="triple-multiply"></a>
## Lifted UGD multiplication

*Source rule.* On lifted real triples, multiply (a,s,k) and (b,t,l) to obtain (at+bs, st, kt+ls). For the discrete seam chart use integer scales and charges. Projection to the middle coordinate preserves products.

**Example.** (1,2,3) times (4,5,6) gives (13,10,27). The unit is (0,1,0).

Arbitrary real scale times a phase specified only modulo 2π is ambiguous. Keep angle lifts, or impose conditions ensuring descent. This is a typed historical chart, distinct from the repository’s full native calculus.

[A43 · §§1–6](sources.md#s-a43)

<a id="positional"></a>
## Positional value and carry

*Specified model.* For finite digits cₙ in a declared integer base b≥2, read the word as ∑cₙbⁿ and normalize an overflowing digit by Euclidean carry. The UGD note also keeps phase digits and a seam ledger.

**Example.** In base 2 an intermediate digit 2 at the units position carries to the next position. The total value remains 2.

The scalar position and carry rule is exact on this domain. A full phase/seam numeral requires compatible bases, a chosen carry policy and convergence for an infinite word.

[A44 · §§1–4](sources.md#s-a44)

<a id="prime-factor"></a>
## Prime Euler-factor map

*Source rule.* Given a prime p and complex s with Re(s)>1, form (1−p^(−s))⁻¹. Multiplying over supplied primes gives the corresponding finite Euler product.

**Example.** For p=2 and s=2 the factor is 4/3. Including p=3 multiplies it by 9/8, giving 3/2.

This operation has explicit input and output. It does not by itself construct a self-adjoint operator whose spectrum gives all zeta zeros.

[A33 · prime encoding](sources.md#s-a33) · [A34 · prime encoding](sources.md#s-a34)

<a id="hecke"></a>
## Phase-weighted divisor–coset average

*Source rule.* For n≥1, a weight k, divisor weights χ(d) and a function on the upper half-plane, sum over ad=n the terms d^(k−1)χ(d) times the average of f((aτ+b)/d) over b modulo d. This preserves the source’s normalization.

**Example.** With n=2, k=1, χ=1 and f=1, each divisor pair contributes 1. The result is 2.

The note calls this a λ–Hecke operator. The displayed finite sum is well defined here. Comparison with a chosen Hecke normalization and twisted multiplicativity require separate proofs.

[W107 · §1](sources.md#s-w107)

<a id="mellin"></a>
## Mellin transform along the imaginary axis

*Source rule.* Given an axis profile g(t)=f(it) on t>0, return the integral of g(t)t^(s−1) over the positive half-line in its range of convergence.

**Example.** For g(t)=e^(−t) at s=1 the integral is 1.

A twist can be applied to the input before the transform. Continuation and functional equations require further structure.

[W107 · §2](sources.md#s-w107)

<a id="q-derivative"></a>
## Logarithmic q-derivative

*Source rule.* For a differentiable q-series set Df=q df/dq. The stated deformed form adds a prescribed directional term αA·∇f whenever those derivatives and the field A are defined.

**Example.** On q³ the undeformed result is 3q³. This operator commutes with the constant argument rotation f(q)↦f(e^(iφ)q).

Thus even the undeformed case does not support the note’s proposed universal nonzero commutator with a constant shift.

[W107 · §§3,5 and mini algebra](sources.md#s-w107)

<a id="coefficient"></a>
## Contour coefficient extraction

*Source rule.* Given f analytic inside and on a circle about 0, extract its Nth Taylor coefficient by integrating f(q)q^(−N−1)/(2πi) around that positively oriented circle.

**Example.** For f(q)=1+3q+2q², the extraction at N=2 gives 2.

Splitting the contour into weighted arcs changes the relation unless the arc contributions and their matching are supplied.

[W107 · §4](sources.md#s-w107)

<a id="q-shift"></a>
## q-series argument rotation

*Source rule.* Fix φ and substitute e^(iφ)q for q in f. The nth coefficient of the resulting q-series is multiplied by e^(inφ).

**Example.** With φ=π and f(q)=1+q+q² the result is 1−q+q².

This typed substitution on functions is distinct from multiplying a whole state by one common phase. Its action on coefficients is a diagonal multiplier.

[W107 · §5](sources.md#s-w107)

<a id="eta"></a>
## Eta-series synthesis

*Source rule.* Given coefficients hₘ and Im τ>0, form ∑ₘ hₘη((2m+1)τ), with finite support or an explicit convergence condition. The source proposes half-integer heat coefficients as input.

**Example.** For (h₀,h₁)=(1,2) and the others zero, the result is η(τ)+2η(3τ).

Existence of nonzero half-integer coefficients and a modular shadow identification depend on the specific heat problem.

[W107 · §6](sources.md#s-w107) · [A23 · §§3,8](sources.md#s-a23)

<a id="jump"></a>
## Twisted boundary mismatch

*Source rule.* Given two one-sided complex boundary values of a function and a declared seam phase χ, return f⁺−χf⁻. It vanishes when the two values glue under that phase.

**Example.** For f⁺=3, f⁻=2 and χ=−1, the mismatch is 5.

This reads a mismatch at the boundary. Solving for analytic functions with the prescribed jump is a separate inverse problem.

[W107 · §7](sources.md#s-w107) · [A41 · jump data](sources.md#s-a41)

<a id="theta"></a>
## Phase-weighted theta-series lift

*Source rule.* From coefficient functions fₙ(τ) form ∑ₙχ(n)q^(n²)y^(2n)fₙ(τ) with y=e^(πiz). Use finite support or specify convergence. The source also admits a shifted q.

**Example.** If only f₁=1 is nonzero and χ(1)=1, the output is qy².

A genuine Jacobi transformation law requires conditions on the coefficients, character and multiplier. The series formula alone does not prove it.

[W107 · §8](sources.md#s-w107)

<a id="heat-trace"></a>
## Heat-trace readout

*Source rule.* Given a nonnegative finite generator L with eigenvalues λⱼ, return Tr exp(−tL)=∑ⱼe^(−tλⱼ) for t>0. In infinite dimension the heat operator must be trace class for this reading.

**Example.** A generator with eigenvalues 0 and 2 gives 1+e^(−2t).

The trace omits eigenvectors. A boundary or a phase twist alone does not fix all small-time coefficients.

[A23 · §3](sources.md#s-a23) · [W082 · §4](sources.md#s-w082) · [W092 · §6](sources.md#s-w092)

<a id="zeta"></a>
## Spectral zeta readout

*Source rule.* For positive eigenvalues λⱼ with multiplicities, send L to ζ_L(s)=∑ⱼ λⱼ^(−s) where it converges. State how zero modes are excluded before taking the sum.

**Example.** Positive eigenvalues 1 and 2 give ζ_L(1)=3/2.

Regularized values outside a convergence domain require a separately justified continuation. This is a spectral observation of a supplied L.

[W092 · §6](sources.md#s-w092) · [W102 · §5](sources.md#s-w102)
