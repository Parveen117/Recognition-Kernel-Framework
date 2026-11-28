# Probability and information

How do frequencies, evidence, weighting and resolution change a statistical reading?

5 source rules · 6 specified models

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="entropy"></a>
## Entropy readout

*Source rule.* For a normalized finite probability distribution p, return −∑ pᵢ log pᵢ with 0 log 0=0. The base of the logarithm specifies the unit.

**Example.** With base 2, (1/2,1/2) has entropy 1 bit and (1,0) has entropy 0 bits.

This measures uncertainty of a declared distribution. Mean entropy is a different quantity from the minimum fixed-width memory needed to distinguish every possible output.

[T05 · §5](sources.md#s-t05) · [W072 · §§1–3](sources.md#s-w072)

<a id="divergence"></a>
## Relative entropy

*Source rule.* For two distributions on the same alphabet, return D(p‖q)=∑pᵢ log(pᵢ/qᵢ). Take +∞ if an event has positive p and zero q.

**Example.** Comparing (1,0) with (1/2,1/2) gives log 2 in natural units. Reversing the arguments gives +∞.

A model of semantic difference must first specify how words determine distributions. This directional quantity is not a symmetric distance.

[T05 · §5](sources.md#s-t05)

<a id="fisher"></a>
## Fisher information

*Source rule.* Given a differentiable positive distribution p(x given θ), take the expected product of the log-probability derivatives. The result gᵢⱼ=E[∂ᵢlog p · ∂ⱼlog p] measures local parameter sensitivity.

**Example.** For a Bernoulli coin with success probability θ, g=1/[θ(1−θ)], which is 4 at θ=1/2.

The metric may have blind parameter directions. Estimating a Tamil semantic metric requires an actual distribution and fitted parameters.

[T05 · §§2–4](sources.md#s-t05) · [A46 · §8](sources.md#s-a46)

<a id="gibbs"></a>
## Normalized exponential weighting

*Source rule.* Given a finite set of energies Eᵢ, form probabilities pᵢ=e^(−Eᵢ)/∑ⱼe^(−Eⱼ). An inverse temperature may be included if energies have physical units.

**Example.** For energies 0 and log 3 the probabilities are 3/4 and 1/4.

The output is defined once the energy function is given. Different choices can give different word or state probabilities.

[T05 · §2](sources.md#s-t05)

<a id="distribution"></a>
## Distribution of a summary

*Specified model.* Given a probability law p and an explicit summary T, form its pushforward by adding the probabilities of all inputs with the same summary. Repeating this over sampled windows implements the statistical-layer proposal.

**Example.** For a fair die, summarizing by parity gives (1/2,1/2). To form a distribution of window summaries one must also specify how windows are sampled.

The summary and sampling law determine what survives compression. Iteration alone supplies no convergence theorem.

[A27 · §§1–4](sources.md#s-a27) · [A29 · §§1–5](sources.md#s-a29)

<a id="forecast"></a>
## Probability transition and forecast

*Specified model.* Supply a finite transition kernel K with nonnegative rows summing to 1. A row distribution p advances to pK. A state x starts from its point mass. This is a precise version of the Future Arrow proposal.

**Example.** With K rows (3/4,1/4) and (1/2,1/2), starting at the first state gives (3/4,1/4) after one step.

The historical entropy and prime-anchor proposal does not determine K. Forecast calibration and prediction skill are separate questions.

[A26 · §§2–5](sources.md#s-a26) · [W098 · §7](sources.md#s-w098)

<a id="symmetry-pooling"></a>
## Reflection pooling of a distribution

*Specified model.* On a finite state set with a declared involutive reflection R, take S(p)=(p+R_*p)/2. This is an idempotent map onto reflection-invariant distributions.

**Example.** If R exchanges left and right, (3/4,1/4) becomes (1/2,1/2). A second pooling gives the same answer.

The choice of symmetry is a hypothesis. It can hide a real asymmetry and entails no forecast improvement by itself.

[A26 · §9](sources.md#s-a26)

<a id="convex-dual"></a>
## Convex conjugation

*Specified model.* Given an explicit proper convex potential H on a real vector space, form H*(y)=supₓ(⟨y,x⟩−H(x)). This specifies the Legendre-type transform proposed for a dual forecast potential.

**Example.** For H(x)=x²/2 on the real line, H*(y)=y²/2.

A dual potential needs its own map into forecast probabilities. The transform alone supplies no bound on forecasting error.

[A26 · §9](sources.md#s-a26)

<a id="memory-trace"></a>
## Additive memory imprint

*Source rule.* On an affine memory carrier, an event with retained trace v and weight ε sends the current record m to m+εv. Saṃskāra is the source’s name for storing an impression in this model.

**Example.** From m=(1,0), adding a trace v=(0,2) with ε=1/2 gives (1,1). Repeating the event gives (1,2).

This stores a trace of supplied events. It differs from quotienting histories by what later probes can distinguish.

[W036 · §1](sources.md#s-w036) · [W029 · §1](sources.md#s-w029)

<a id="conditional-law"></a>
## Class-conditioned update

*Specified model.* Given a discrete probability law p, event E and p(E)>0, restrict p to E and divide by p(E). The operation makes explicit how a selection can update a distribution when prior weights exist.

**Example.** Start with probabilities (1/2,1/3,1/6). Keeping the last two states gives (2/3,1/3) within that event.

The Hebrew branch intersects candidate sets without supplied probabilities. This is a possible weighted reading of a selection, not an inference of lexical frequencies.

[W064 · §6](sources.md#s-w064) · [H06 · §6](sources.md#s-h06) · [A26 · §§2–3](sources.md#s-a26)

<a id="coarse"></a>
## Idempotent coarse-graining

*Specified model.* Choose a finite partition and positive reference weights. Replace a scalar reading on each cell by its weighted cell average. The map acts on readings and is idempotent.

**Example.** With equally weighted cells {1,2} and {3}, readings (2,6,9) become (4,4,9). Reapplying the same filter gives the same triple.

The Defog draft asks for an idempotent change of resolution. This chosen partition supplies an explicit averaging rule.

[A28 · §4](sources.md#s-a28) · [A29 · §4](sources.md#s-a29)
