# Phase, loops and feedback

Which readings record relative phase, completed turns and response to a reference?

7 source rules · 2 specified models

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="transport"></a>
## Ordered path transport and loop holonomy

*Source rule.* Attach a compatible transport Uₑ to every oriented edge. For a path e₁,…,eₙ return Uₑₙ⋯Uₑ₁. For a loop the product returns to the starting space and is its holonomy.

**Example.** Two scalar phase edges i and −1 give loop transport −i. With matrices, exchanging edge order can change the result.

An endpoint product can omit the path or the number of turns. Keep the source, path labels and a lift if the requested target distinguishes them.

[A24 · §§1–2,7](sources.md#s-a24) · [W098 · §8](sources.md#s-w098) · [Holonomy variation in a fixed connection · §§1–3](../../theorum/recognition_topology/02_abelian_holonomy_variation_transgression.md)

<a id="holonomy-variation"></a>
## Holonomy variation

*Source rule.* For a differentiable family of unitary loop readings U(s), take the tangent generator iU(s)⁻¹ dU(s)/ds. With U=e^(−iΦ), it reads dΦ/ds. This name identifies what changes and along which family.

**Example.** If U(s)=e^(−3is), the answer is 3 everywhere. The curve parameter has units only if the experiment supplies them.

For an abelian, fixed connection the geometric variation equals the line integral of curvature contracted with the loop’s deformation velocity. A varying connection contributes another term.

[A24 · §§2,4](sources.md#s-a24) · [A25 · §§2–4](sources.md#s-a25) · [Holonomy variation in a fixed connection · §§2,5](../../theorum/recognition_topology/02_abelian_holonomy_variation_transgression.md)

<a id="winding"></a>
## Lifted phase winding

*Source rule.* Given a continuous path of phases with a chosen real lift θ, read (θ(1)−θ(0))/(2π). This is an integer for a closed circle-valued path. Orient the path before reading the sign.

**Example.** A path 0→4π has winding 2. Its endpoint on the circle is the same as the endpoint of the constant path, whose winding is 0.

Samples of an endpoint cannot determine unobserved turns. Recovering winding from discrete sampling needs a branch or a bound on increments.

[A24 · §§1,5–7](sources.md#s-a24) · [A25 · §§3–5](sources.md#s-a25) · [Principal phase and lifted memory · §§1–4](../../theorum/recognition_topology/03_principal_holonomy_blindness_and_lifted_memory.md)

<a id="crossing"></a>
## Signed spectral crossing count

*Specified model.* For a continuous path of unitaries with tracked eigenphases and regular isolated crossings of a specified reference angle, add +1 or −1 using the chosen angular orientation. Fix endpoint and multiplicity conventions.

**Example.** For U(s)=e^(2πis) with 0≤s≤1, the phase crosses angle π once counterclockwise. The signed count is +1.

Equality with a different reported winding needs an identification of paths and conventions. A terminal eigenangle alone gives no crossing count.

[A24 · §§4–7](sources.md#s-a24) · [A40 · spectral flow](sources.md#s-a40)

<a id="phase-rotation"></a>
## Phase rotation

*Source rule.* Given complex amplitudes and a real phase φ, send ψ to e^(iφ)ψ. Position-dependent phase choices can change the frame of a field.

**Example.** With ψ=1 and φ=π/2, the output is i. Its squared magnitude is still 1.

A global phase and an independently measured relative phase carry different information. A gauge claim also needs transformation laws for the connection.

[C07 · §V](sources.md#s-c07) · [A18 · §§2–3](sources.md#s-a18)

<a id="coherence"></a>
## Phase-coherence readout

*Source rule.* For N≥1 supplied angles, return the magnitude of their average phasor, |∑e^(iθⱼ)|/N. It lies between 0 and 1.

**Example.** For two phases 0 and π, the readout is 0. For two phases π/2 and π/2, it is 1.

It measures alignment among supplied phases. It does not supply an absolute phase reference or define an awareness measurement.

[H06 · §9](sources.md#s-h06) · [C02 · §§II,V](sources.md#s-c02) · [W022 · §4](sources.md#s-w022)

<a id="phase-overlap"></a>
## Pairwise in-phase overlap

*Source rule.* Given two complex channel readings z and w, return Re(z conjugate(w)). For unit amplitudes this is the cosine of the relative phase.

**Example.** The pair (1,i) gives 0. The pair (1,−1) gives −1 even though both magnitudes are 1.

Signed overlap and the magnitude of a population average are different readouts. Conversion to energy or information transfer requires calibrated dynamics.

[C02 · §V](sources.md#s-c02)

<a id="phase-feedback"></a>
## Reference-linked phase correction

*Specified model.* Model the source’s proposed phase synchronization on a local unwrapped chart by e=θ−θ₀ and e′=(1−κ)e, with a fixed reference and 0<κ<1. The gain and the update law are explicit choices for this example.

**Example.** For a 10° offset and κ=1/2, successive offsets are 5° and 2.5°. With equal clock rates and no correction the original offset can persist.

The network note leaves its synchronization function open. This local example demonstrates the distinction between matching rates and correcting phase, without selecting a cosmic coupling.

[C03 · §§IV–V](sources.md#s-c03) · [C04 · §IV](sources.md#s-c04)

<a id="superposition"></a>
## Phase-weighted layer sum

*Source rule.* Given compatible complex layer amplitudes zⱼ and phase choices θⱼ, form ∑ⱼ e^(iθⱼ)zⱼ. Inputs must be transported to a common output space first.

**Example.** Two equal unit amplitudes add to 2 at equal phase and to 0 when their relative phase is π.

This is a specified aggregation of readings. A scale-to-scale interaction law and an external observable are separate inputs.

[C02 · §§II–III](sources.md#s-c02) · [C03 · §IX](sources.md#s-c03)
