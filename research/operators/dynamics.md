# State changes and equations of motion

What action is taken on a state, or what residual tests a proposed motion?

9 source rules · 2 specified models

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="event-state"></a>
## Guarded state-machine step

*Specified model.* Supply a state, labelled transitions and an external guard value. Execute a transition only if its source and guard match. The output carries both target and event history.

**Example.** For a three-stage model enter→prepare→finish, with the second edge enabled only at score ≥2, score 1 leaves the finish edge disabled.

The staged ritual is the source’s example. Its proposed internal qualities would need a measured definition before being used as experimental inputs.

[W016 · §3](sources.md#s-w016) · [W098 · §§2–4](sources.md#s-w098)

<a id="ladder"></a>
## Mode raising and lowering

*Specified model.* On a finite ladder with basis e₀,…,eₘ, send eⱼ to eⱼ₊₁ where j<m and send the top state to the zero vector. With the standard pairing the adjoint lowers the mode and kills the bottom state.

**Example.** On three modes, raising e₁ gives e₂ and lowering e₂ gives e₁. A raise applied to the top mode e₂ gives zero.

This is a truncated shift realization of the ladder idea. Bosonic coefficients, boundary rules and commutators change with the choice of carrier.

[W081 · §§3–5](sources.md#s-w081) · [W064 · §§2–3](sources.md#s-w064) · [T07 · field quantization](sources.md#s-t07)

<a id="normalization"></a>
## State normalization

*Source rule.* For a nonzero vector v in a supplied normed representation, return v/‖v‖. The operation is nonlinear and requires a nonzero input.

**Example.** The vector (3,4) is mapped to (3/5,4/5). Both this input and (6,8) give the same output.

Positive rescaling becomes invisible under normalization. If amplitude magnitude is a target, retain the original norm as another reading.

[W084 · §4](sources.md#s-w084) · [W083 · §§2–3](sources.md#s-w083)

<a id="sym-product"></a>
## Symmetrized operator product

*Source rule.* Given two endomorphisms A and B, form AB+BA. For Hermitian matrices this sum is Hermitian. The source uses the sum of the two orderings as a candidate generator.

**Example.** For A=diag(1,−1) and B the two-coordinate swap, AB+BA=0 even though AB and BA are nonzero.

An algebraic expression for a generator supplies no physical units, calibrated energy or equation of motion on its own.

[W064 · §4](sources.md#s-w064) · [W057 · §1](sources.md#s-w057)

<a id="mixing"></a>
## Hadamard basis transformation

*Source rule.* On a two-component amplitude, use H(x,y)=((x+y)/√2,(x−y)/√2). This is the standard finite gate named in the Hebrew notes.

**Example.** A single input (1,0) gives equal amplitudes in the two channels. A second application recovers (1,0).

Associating a word or conjunction with the gate is a modelling proposal. The gate action itself is fully specified in this representation.

[H06 · §7](sources.md#s-h06)

<a id="control"></a>
## Controlled bit flip

*Source rule.* On two bits (c,b), send the pair to (c,b⊕c). The first bit controls whether the second flips. The same basis permutation defines a controlled gate on amplitudes.

**Example.** (1,0) becomes (1,1) while (0,0) stays (0,0). The map is its own inverse.

The source assigns CNOT a linguistic analogy. A Hebrew grammatical condition supplies a quantum gate only after an actual encoded construction.

[H06 · §7](sources.md#s-h06)

<a id="logic"></a>
## Joint Boolean admission

*Source rule.* For two supplied truth values S and E, return 1 exactly when both are 1 and return 0 otherwise. This is the explicit Boolean test of the source’s two-component symmetry model.

**Example.** The pairs (1,1) and (1,0) yield 1 and 0 respectively.

Its output is a predicate. Turning the predicate into an operator on a vector space needs a defined basis and diagonal indicator.

[A03 · §4](sources.md#s-a03) · [H03 · §8](sources.md#s-h03)

<a id="dilation"></a>
## Dilation of a test function

*Source rule.* For ε>0 and a function on a scale-invariant domain, set (Dεf)(x)=f(x/ε). If unitary normalization is required, specify the dimension and measure and supply the normalization factor.

**Example.** For f(x)=x² and ε=2 the output at x=4 is 4. This convention compresses the argument to 2.

Limits in a pointwise, weak or distributional topology may differ. The formula does not equate a zero operator with an infinite operator.

[W102 · §§2–4](sources.md#s-w102)

<a id="parity-step"></a>
## Parity-dependent integer iteration

*Source rule.* On positive integers, send an even n to n/2 and an odd n to 3n+1. The familiar Collatz example is included in the dynamics note as a standalone update.

**Example.** Three iterations from 6 give 6→3→10→5.

The finite rule defines every next step. A universal assertion that all inputs reach 1 is a different statement.

[A36 · Collatz section](sources.md#s-a36) · [A37 · discrete dynamics](sources.md#s-a37)

<a id="momentum"></a>
## Fluid momentum residual

*Source rule.* For sufficiently smooth velocity u and pressure p with prescribed viscosity ν, return ∂ₜu+(u·∇)u+∇p−νΔu in the source’s unforced unit-density chart.

**Example.** A constant velocity and constant pressure give zero residual. A nonconstant supplied field can be checked by the same operator.

A residual test is distinct from existence or smoothness of all solutions. Incompressibility and boundary data are additional conditions.

[A36 · Navier–Stokes section](sources.md#s-a36)

<a id="variation"></a>
## Euler–Lagrange residual

*Source rule.* For a one-coordinate action with differentiable L(q,v,t), form d/dt(∂L/∂v)−∂L/∂q on a sufficiently smooth trial path. Field versions use the corresponding variational derivative.

**Example.** With L=(v²−q²)/2, the residual is q″+q. The trial q(t)=cos t gives zero.

The source proposes an action for several fields. This card records the variational operation, with its elementary example in a specified ordinary coordinate.

[W057 · §§2–4](sources.md#s-w057)
