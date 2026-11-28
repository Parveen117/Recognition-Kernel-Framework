# Observation and memory

What can a chosen measurement or a retained history distinguish?

12 source rules · 1 specified model · 1 existing github fixture

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="identity"></a>
## Identity action

*Source rule.* On any declared state space, I sends every state to itself. The Witness note calls this the witness action.

**Example.** For (3,4), the output is (3,4). Applying it twice has the same effect as applying it once.

A state fixed by one operation does not make that operation the identity on every state.

[W085 · §3](sources.md#s-w085) · [W058 · §§1–2](sources.md#s-w058)

<a id="cut"></a>
## Subspace projection and complement

*Source rule.* Given a specified subspace and inner product, P sends a vector to its orthogonal component in that subspace. The complementary output is (I−P)x. Bindu is justified as the name of the one-mode specialization with a supplied unit vector b and P=bb*.

**Example.** Project (3,4) onto the first axis. The retained part is (3,0) and the complementary part is (0,4).

A reset that sends every input to the same nonzero state has a different action. Mode selection, sharp bond release and finite band selection are instances of projection.

[W045 · §3](sources.md#s-w045) · [W054 · §§3–5](sources.md#s-w054) · [W069 · §7](sources.md#s-w069) · [W086 · §3](sources.md#s-w086) · [W091 · §§1–2](sources.md#s-w091)

<a id="order"></a>
## Commutator probe

*Source rule.* Given endomorphisms A and X of the same space, measure [A,X]=AX−XA. A family of probes sends X to the list ([Aⱼ,X])ⱼ. Spanda is the source’s cultural name for the particular model i[A,H₀].

**Example.** Let P retain the first of two coordinates and let X swap them. On (1,0), PX gives (0,0) and XP gives (0,1). The difference is (0,−1).

Every X+cI has the same commutator readings as X. Additional blind directions depend on the chosen probes. If A and H₀ commute, the stated Spanda expression is zero.

[W106 · §§2–4](sources.md#s-w106) · [W041 · §1](sources.md#s-w041) · [W058 · §§2–4](sources.md#s-w058)

<a id="sandwich"></a>
## Two-sided operator probe

*Source rule.* Supply admissible input and output filters B and A. The probe of an unknown operation X is AXB, defined wherever the composition exists. With one-dimensional filters this reads an individual input-to-output channel.

**Example.** For X exchanging ports 1 and 2, the channel from 1 to 2 has coefficient 1 and the return channel from 1 to 1 has coefficient 0.

An unspecified X is determined only up to equality on the admitted probes. Specifying one product does not define it on all inputs.

[W106 · §§2–4](sources.md#s-w106) · [W105 · §1](sources.md#s-w105)

<a id="shadow"></a>
## Diagonal spectral readout

*Source rule.* Fix an ordered orthonormal probe basis eⱼ. Send X to the list of return amplitudes ⟨eⱼ,Xeⱼ⟩. The notes call this a spectral shadow.

**Example.** The two-port swap and the zero matrix both give (0,0). The cross-port probe distinguishes them.

These entries depend on the probe basis. The example exhibits two operators with different spectra and identical diagonal data.

[W103 · §§1–3](sources.md#s-w103) · [W104 · §§1–3](sources.md#s-w104)

<a id="synthesis"></a>
## Diagonal operator synthesis

*Source rule.* Given a fixed orthonormal basis and a bounded list dⱼ, build the operator ∑ⱼ dⱼ eⱼeⱼ*. Finitely many modes suffice for the examples.

**Example.** The list (2,−1) acts on (3,4) by returning (6,−4). Unit-modulus weights give phase selection and 0/1 weights give a projection.

Synthesizing from the diagonal readout recovers the diagonal part. Recovering X from its diagonal alone requires a restriction such as a known diagonal family.

[W103 · §§3–6](sources.md#s-w103) · [W086 · §3](sources.md#s-w086) · [W107 · §9](sources.md#s-w107)

<a id="overlap"></a>
## Observer amplitude

*Source rule.* A fixed normalized observer v sends a state x to the linear amplitude v*x in a chosen complex representation. A signed or complex value can retain phase information.

**Example.** With v=(1,1)/√2 and x=(1,−1)/√2 the reading is zero even though x is a unit vector.

A different observer can see the same state. The chosen pairing and observer belong to the input data.

[W058 · §3](sources.md#s-w058) · [W021 · §4](sources.md#s-w021) · [H06 · §§2–6](sources.md#s-h06)

<a id="outcome"></a>
## Outcome probability readout

*Source rule.* For a normalized complex vector x and a complete family of orthogonal projectors Pⱼ, return (‖Pⱼx‖²)ⱼ. For a selected outcome of positive probability the normalized state is Pⱼx/‖Pⱼx‖.

**Example.** For x=(1,i)/√2 and the coordinate projectors, the probabilities are (1/2,1/2). The vectors (1,i)/√2 and (1,−i)/√2 give the same pair.

This is a rule in a supplied quantum representation. The Hebrew analogy supplies no empirical language amplitudes or evidence of physical collapse.

[H06 · §§5–7](sources.md#s-h06) · [W064 · §6](sources.md#s-w064)

<a id="expectation"></a>
## Expectation projection onto scalars

*Source rule.* Given a density matrix ρ with trace 1, map an observable X to Tr(ρX)I. The output is a scalar multiple of the identity on the entire space.

**Example.** For ρ=I/2 and X=diag(2,6), the output is 4I. Applying the map again returns 4I.

The scalar records a mean. The two individual readings cannot be recovered from that mean alone.

[W102 · §§1,3,7](sources.md#s-w102)

<a id="parity"></a>
## Even and odd cut decomposition

*Specified model.* For an idempotent cut P put J=2P−I. An endomorphism X splits into (X+JXJ)/2 and (X−JXJ)/2, provided 2 is invertible. The latter also equals [P,[P,X]].

**Example.** With P retaining the first coordinate, diagonal entries of a 2×2 matrix belong to the even part and off-diagonal entries to the odd part.

The double commutator in the Operator Universe notes gains this precise interpretation in the repository’s B3 result.

[W058 · §§3–4](sources.md#s-w058) · [W059 · axioms](sources.md#s-w059) · [Canvas operators in the native cut algebra · B3](../../theorum/56_canvas_operators_nativized_theorem.md)

<a id="conjugation"></a>
## Change of frame by conjugation

*Source rule.* Given an invertible change of frame U, transport an endomorphism X to UXU⁻¹. A unitary frame change also preserves inner products. The Aghora sign reversal is an extra condition on the pair.

**Example.** Conjugating diag(1,−1) by the two-coordinate swap gives diag(−1,1).

If a unitary involution sends a positive semidefinite operator to its negative, that operator is zero. A nonzero sign-reversing example needs a signed operator.

[W086 · §7](sources.md#s-w086) · [W051 · §§4–9](sources.md#s-w051) · [Canvas operators in the native cut algebra · B4](../../theorum/56_canvas_operators_nativized_theorem.md)

<a id="toggle"></a>
## Two-state involution

*Source rule.* On two distinct declared labels, exchange the labels. Extend linearly on their span if using vectors. Applying this operation twice gives the identity.

**Example.** Starting at the left port, two exchanges return to the left port. This also supplies the swap used in the diagonal-readout example.

The empty/full language in the source names two labels for this model. It does not identify the framework’s cut-zero with an ordinary scalar or empty set.

[W028 · §3](sources.md#s-w028) · [H06 · §7](sources.md#s-h06)

<a id="memory"></a>
## Smṛti future-response quotient

*Existing GitHub fixture.* Group retained histories when the available observations agree on every admitted future test, including whether each test is enabled. The quotient sends a history to its future-response class. Smṛti names the retained memory in the framework.

**Example.** Two histories display the same word. If the same allowed next probe produces different outputs, they require two records. If every licensed continuation has the same definedness and reading, those two histories can share a record.

The branch constructs this operation for finite grammar fixtures. The Drive notes supply the hidden-marker and memory motivation. Changing the target can change the quotient.

[W097 · §§5–7](sources.md#s-w097) · [W036 · §§1–2](sources.md#s-w036) · [Tamil and Hebrew recognition seams · Hebrew recognition](../cross_linguistic_seams/README.md) · [Guarded Lopa and future equivalence · guarded responses](../../theorum/morphic_recognition/06_guarded_lopa_future_equivalence.md)

<a id="successive-exclusion"></a>
## Neti neti successive exclusion

*Source rule.* Given a finite ordered list of orthogonal projectors P₁,…,Pₙ, remove their selected components successively using (I−Pₙ)⋯(I−P₁). The source borrows the repeated negation ‘neti neti’ for this construction.

**Example.** On three coordinates, excluding the first and then the second maps (2,3,4) to (0,0,4). These coordinate projectors commute.

For commuting projectors the product projects onto the common surviving space. Noncommuting exclusions can depend on order. A single pass need not be a projector.

[W047 · §4](sources.md#s-w047) · [W052 · §§2–4](sources.md#s-w052) · [Canvas operators in the native cut algebra · B6](../../theorum/56_canvas_operators_nativized_theorem.md)
