# Seams and field response

How does an applied source or local change propagate through a field and across a join?

14 source rules · 4 specified models

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="difference"></a>
## Square-root-window difference

*Source rule.* For a function f and x>0 in a dimensionless chart, with both sample points in the domain, return (f(x+√x)−f(x−√x))/(2√x). This is a central slope with a position-dependent observation width.

**Example.** For f(t)=t³ and x=4, sample at 2 and 6. The slope is (216−8)/4=52. The point derivative at 4 is 48.

This formula does not automatically inherit the ordinary derivative’s product and chain rules. A dimensional coordinate requires a reference scale before taking the stated window.

[A16 · §3](sources.md#s-a16) · [A14 · §2](sources.md#s-a14) · [A12 · §7](sources.md#s-a12)

<a id="gradient"></a>
## Nonlocal difference gradient

*Source rule.* A specified interaction kernel or edge incidence D sends a field u to differences across pairs. On an oriented edge i→j, use (Du)ᵢⱼ=uⱼ−uᵢ. A continuum version requires a kernel and a declared integration space.

**Example.** For two sites with values 3 and 8, the oriented edge difference is 5. Reversing the edge gives −5.

A kernel’s mean and range alone do not ensure detection of every nonconstant field or recovery of a continuum gradient.

[A42 · §§1–2](sources.md#s-a42) · [A40 · kernel limit](sources.md#s-a40)

<a id="laplace"></a>
## Weighted difference Laplacian

*Source rule.* Given the difference map D, a pairing defining D* and positive edge mobility M, build L=D*MD. It maps a field to its net imbalance. The energy pairing is ⟨u,Lu⟩=⟨Du,MDu⟩.

**Example.** For one unit-weight edge, L(3,8)=(−5,5). A constant pair produces (0,0).

This self-adjoint form and a drift-augmented generator have distinct hypotheses. Constants can remain in the kernel.

[A42 · §§1–5](sources.md#s-a42) · [A23 · §§0–2](sources.md#s-a23)

<a id="drift"></a>
## Diffusion with directional drift

*Source rule.* For smooth u in a fixed Euclidean chart, use div(G∇u)+α div(A∇u)−β∇ψ·∇u, with G symmetric positive and A skew. Boundary data and a measure determine the operator realization.

**Example.** With G=I, A=0, β=1 and ψ(x)=x in one dimension, u(x)=x² maps to 2−2x.

A constant skew matrix contributes zero through div(A∇u) for a smooth scalar u in this chart. Spectral-gap and heat-coefficient statements require further hypotheses.

[A23 · §§0–2,6,8](sources.md#s-a23)

<a id="trace"></a>
## Interface value and flux jump

*Source rule.* Take the two one-sided traces at an oriented interface. The value trace returns the boundary value on each side. A signed difference of consistently oriented flux traces reads the interface source.

**Example.** Using the right-minus-left convention, flux readings 2 on the left and 5 on the right give jump 3. Reversing orientation changes its sign.

This is one interface observation with selectable output. A nonlocal continuum trace must first be defined in the chosen field space.

[A42 · §§3–4](sources.md#s-a42)

<a id="green"></a>
## Seam Green operator

*Specified model.* Given boundary data, a specified difference operator L and compatible forcing f, return the solution u of Lu=f on the pinned space or chosen complement of the kernel. Homogeneous boundary data give a linear solution map. For pure flux data, compatibility and a gauge choice enter separately.

**Example.** Two sites have unit contact and site 1 is held at zero. Supplying 2 at site 2 gives u₂=2. With contact strength g>0 the same input gives 2/g.

This calculation fixes the finite map. A continuum inverse needs a valid seam trace, source compatibility and a lower energy bound on the chosen space. The source’s listed moment assumptions alone do not supply that bound.

[A42 · §§1–7](sources.md#s-a42) · [Native seam resolvent · resolvent comparison](../../theorum/52_native_seam_resolvent_theorem.md)

<a id="jacobian"></a>
## Phase–entropy differential

*Specified model.* For a specified differentiable chart map F on the phase and entropy coordinates, push an increment h forward by J_F h. The source proposes a local two-channel matrix. Its entries must come from a declared map or coframe.

**Example.** For the linear map F(x,s)=(x+2s,s), an increment (0,1) becomes (2,1). Its determinant is 1.

A determinant is local signed volume scaling. A statement about irreversible heating needs a separate entropy law and calibrated observables.

[A11 · §§2–5](sources.md#s-a11) · [A13 · §§3–6](sources.md#s-a13)

<a id="tangent"></a>
## Constraint-tangent update

*Source rule.* At a smooth constraint set with supplied metric and tangent projector Πᵤ, take a candidate update v and use Πᵤv. The structural proposal uses the sum of an algebraic and a seam contribution as v.

**Example.** On the unit circle at (1,0), projecting (2,3) onto the tangent gives (0,3). A finite step requires a retraction or integration on the manifold.

The projection is determined once the constraints, pairing and v are fixed. It alone does not prove every proposed entropy or charge law.

[A46 · §§1–4,8](sources.md#s-a46)

<a id="flux"></a>
## Mobility-weighted flux

*Source rule.* In a supplied mobility M and chemical or energy potential μ, return J=−M Dμ. Paired with a divergence it gives a transport law. Flux is already defined on edges before forming a Laplacian.

**Example.** Across one edge with μ rising from 3 to 5 and mobility 2, the signed flux is −4 in the chosen orientation.

The minus sign specifies transport down the potential gradient. Material values and units must be supplied for physical use.

[A46 · §§4–5](sources.md#s-a46) · [A23 · §1](sources.md#s-a23)

<a id="gradient-flow"></a>
## Potential gradient flow

*Source rule.* On a specified metric state space with differentiable potential V, evolve by dx/dt=−grad V(x). The metric selects which vector represents a given change of V.

**Example.** For V(x)=x²/2 on the real line, starting at x=2 gives x(t)=2e^(−t). The potential decreases.

The language or awareness interpretations require independently defined coordinates and a potential. The calculation is for the declared mathematical model.

[T05 · §7](sources.md#s-t05) · [W072 · §4](sources.md#s-w072) · [W076 · §7](sources.md#s-w076)

<a id="heat"></a>
## Heat propagation and selective release

*Source rule.* For a fixed positive semidefinite matrix L, apply H(t)=exp(−tL) for t≥0. Śānti is a source name for damping disturbances. Bond release is the specialization that damps a chosen subspace while preserving its complement.

**Example.** For L=diag(1,0), (2,3) evolves to (2e^(−t),3). The second coordinate survives however long the first is damped.

Positive generators justify contraction in this finite pairing. A claimed bond-energy decline for a different metric or noncommuting observable needs its own proof.

[W049 · §§2–5](sources.md#s-w049) · [W054 · §§2–5](sources.md#s-w054) · [W082 · §§1–2](sources.md#s-w082) · [W093 · heat evolution](sources.md#s-w093)

<a id="product-heat"></a>
## Heat propagation on independent factors

*Source rule.* For independent factors and finite generators L₁,L₂, evolve under the sum L₁⊗I+I⊗L₂. The result factors as exp(−tL₁)⊗exp(−tL₂) because the two summands commute.

**Example.** Two factor eigenmodes with rates 1 and 2 have joint decay e^(−3t).

A coupling between the factors can break the product formula. This entry uses the separable model actually written in the heat-kernel note.

[W082 · §§1–4](sources.md#s-w082) · [W083 · §§3–6](sources.md#s-w083)

<a id="unitary"></a>
## Hamiltonian phase evolution

*Source rule.* For a fixed Hermitian generator H and a specified parameter t, send x to exp(−itH)x in a representation with ℏ=1. Norm is preserved.

**Example.** For H=diag(0,1) and t=π, the second coordinate changes sign and the first stays fixed.

The parameter here belongs to the chosen model. A physical clock, Hamiltonian or semantic interpretation requires its own calibration.

[W046 · §2](sources.md#s-w046) · [H06 · §5](sources.md#s-h06) · [C06 · §II](sources.md#s-c06)

<a id="covariant"></a>
## Connection-corrected derivative

*Source rule.* Given a field ψ and a specified connection component Aᵢ on the same bundle, Dᵢψ=∂ᵢψ+Aᵢψ. The second term tells how frames are compared across locations.

**Example.** For the constant field ψ=1 and constant scalar connection A₁=2i, D₁ψ=2i in that frame.

Frame changes must transform the connection consistently. The abstract connection in a source does not determine a material gauge field.

[A10 · §2](sources.md#s-a10) · [A24 · §1](sources.md#s-a24) · [C07 · §V](sources.md#s-c07)

<a id="curvature"></a>
## Connection curvature

*Source rule.* For a supplied matrix connection, form Fᵢⱼ=∂ᵢAⱼ−∂ⱼAᵢ+[Aᵢ,Aⱼ]. It returns an endomorphism-valued two-form measuring infinitesimal transport around a loop.

**Example.** With an abelian connection Aₓ=0 and Aᵧ=ix on a plane, Fₓᵧ=i. Its integrated value changes with enclosed area.

This is the curvature of this declared connection. It does not identify native cut curvature with a Riemannian spacetime tensor.

[C07 · §V](sources.md#s-c07) · [A24 · §§1–3](sources.md#s-a24) · [Holonomy variation in a fixed connection · §§1–3](../../theorum/recognition_topology/02_abelian_holonomy_variation_transgression.md)

<a id="regularize"></a>
## Regularized support projection

*Specified model.* Given a positive semidefinite finite B, form (B+εI)⁻¹B for ε>0. As ε decreases to zero this approaches the orthogonal projector onto the range of B. Its complement is the sharp release map.

**Example.** For B=diag(2,0) and ε=1, the regularized diagonal is (2/3,0). Its limiting diagonal is (1,0).

This derivation uses the identity metric. With a general weight the pairing, adjoint and limiting range must be specified again.

[W054 · §3](sources.md#s-w054)

<a id="hodge"></a>
## Hodge Laplacian on forms

*Specified model.* On a specified graded complex with differential d, d²=0 and a pairing defining d*, send a form to (dd*+d*d) applied to it. At the bottom degree it reduces to d*d.

**Example.** For two vertices joined by one oriented edge with unit weight, the bottom-degree operator maps the vertex values (0,1) to (−1,1).

A proposed twist that mixes degrees must declare a compatible graded or parity space. This entry covers the defined untwisted complex.

[A23 · §5](sources.md#s-a23) · [A32 · geometric operator](sources.md#s-a32)

<a id="geodesic"></a>
## Geodesic transport of position and direction

*Source rule.* For a given smooth metric, initial position and velocity, evolve by the geodesic equation using its metric connection, on the interval where the solution exists.

**Example.** In a flat plane a unit horizontal velocity starting from (2,3) gives position (2+t,3) at parameter t.

The path is locally stationary for length or energy under the usual hypotheses. A shortest linguistic change additionally requires fitted coordinates and a justified metric.

[T05 · §4](sources.md#s-t05) · [W076 · §3](sources.md#s-w076)
