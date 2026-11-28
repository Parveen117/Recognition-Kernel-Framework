# Metre, rhythm and sound

Which operations count, organize or transform an actual sequence of pulses or pitches?

5 source rules · 4 specified models

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="duration"></a>
## Chandas duration reading

*Source rule.* For a supplied stream of laghu and guru symbols, sum their declared weights 1 and 2. In this prosodic model the total counts mātrās.

**Example.** Laghu–guru–laghu has 1+2+1=4 units and three syllables.

A syllable count and a mātrā count answer different questions. A named traditional metre needs its own documented criterion.

[W023 · §1](sources.md#s-w023) · [W022 · §1](sources.md#s-w022)

<a id="metre"></a>
## Chandas pattern admission

*Source rule.* Given a pattern and segmented input, return whether each segment satisfies its prescribed length and weight conditions. On the free vector space of candidate sequences, keeping admitted basis vectors and sending the others to zero defines a projector.

**Example.** With a two-segment target of 3 and 2 mātrās, [laghu,guru] | [guru] passes. [guru] | [laghu,guru] fails although the total is the same.

Supply the counting convention and segment boundaries. The examples are constructed metre patterns.

[W023 · §2](sources.md#s-w023) · [W022 · §1](sources.md#s-w022)

<a id="metre-generation"></a>
## Vṛtta pattern generation

*Source rule.* Given a finite prosodic alphabet, length bound and metre constraints, enumerate all admissible sequences. Generation returns a set of words, whereas the admission test returns one decision.

**Example.** Three mātrās in one segment over L=1 and G=2 give LLL, LG and GL.

This counts forms admitted by the stated constraint. Lexical, metrical and recitation restrictions can reduce the set further.

[W022 · §1](sources.md#s-w022) · [W019 · §2](sources.md#s-w019)

<a id="cycle"></a>
## Tāla cycle advance

*Source rule.* For a cycle of L>0 beat positions, advance a phase k by n beats using (k+n) modulo L. Tāla is justified by the periodic rhythmic carrier.

**Example.** In an eight-position cycle numbered 0 to 7, advancing from position 6 by three beats lands at 1.

The readout gives a position. Tracking completed cycles requires a retained turn count, just as in phase winding.

[W019 · §1](sources.md#s-w019) · [W023 · §6](sources.md#s-w023) · [W044 · §2](sources.md#s-w044)

<a id="subdivide"></a>
## Beat subdivision

*Specified model.* Given a specified ordered grouping of pulses, map the subdivisions to their parent beat or flatten a hierarchy in the stated order. Multiplicative subdivision and concatenating unequal groups require separate input conventions.

**Example.** Four beats divided into three equal pulses each give twelve pulse positions. In zero-based indexing, pulse 7 belongs to parent beat 2.

This realizes the recursive rhythm in the notes. Total length alone does not determine the grouping or stress pattern.

[W019 · §§1–2](sources.md#s-w019) · [W015 · §4](sources.md#s-w015)

<a id="microtone"></a>
## Śruti pitch displacement

*Specified model.* Given a reference frequency and a calibrated pitch interval, multiply by the specified frequency ratio. In a cents chart, an offset c gives f′=2^(c/1200)f. Śruti locates the source idea in fine interval adjustment.

**Example.** A 1200-cent shift sends 220 Hz to 440 Hz. Reversing the interval returns to 220 Hz.

The unit example fixes a coordinate convention. The historical tuning of a particular śruti requires its own evidence.

[W022 · §3](sources.md#s-w022) · [W023 · §5](sources.md#s-w023)

<a id="ornament"></a>
## Gamaka pitch modulation

*Specified model.* Take a base pitch contour and a prescribed ornament contour. In a pitch-coordinate chart add them pointwise. Glides and oscillations are distinct choices of contour within this family.

**Example.** On a 200 Hz constant tone, an example frequency modulation of 5 sin(2πt) Hz produces 205 Hz at t=1/4 s and 195 Hz at t=3/4 s.

Gamaka names melodic ornamentation. The sinusoid illustrates one model and does not define the practice across rāgas.

[W021 · §1](sources.md#s-w021) · [W020 · §2](sources.md#s-w020)

<a id="harmonics"></a>
## Harmonic synthesis

*Source rule.* Given a fundamental frequency and specified amplitudes and phases, sum the harmonic components. A finite drone model is ∑ₙ aₙ cos(2πnf₀t+φₙ).

**Example.** At 100 Hz, the first and third harmonics contribute tones at 100 and 300 Hz. If both have amplitude 1 and phase 0 their sum at t=0 is 2.

The drone, Tanpura and Nāda labels describe uses of the synthesis. Instrument response data are needed for an acoustic prediction.

[W021 · §§2,4](sources.md#s-w021) · [W020 · §3](sources.md#s-w020)

<a id="sympathetic"></a>
## Coupled-mode acoustic response

*Specified model.* Given an excitation vector x of string or mode amplitudes and a calibrated response matrix C, return Cx. Off-diagonal coefficients represent drive into another mode.

**Example.** If C has rows (1,0) and (1/2,1), driving only the first mode at unit amplitude gives outputs (1,1/2).

The source describes sympathetic vibration. Nonzero coefficients, losses and their frequency dependence belong to the instrument model.

[W021 · §2](sources.md#s-w021) · [W020 · §3](sources.md#s-w020)
