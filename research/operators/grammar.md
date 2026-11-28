# Language and rule order

How do letters, grammatical tags, word patterns and rule priorities change a derivation?

15 source rules · 3 specified models · 3 existing github fixtures

[Catalogue and counting convention](README.md) · [Native carrier and scope](framework-reading.md)

<a id="designation"></a>
## Saṃjñā designation

*Source rule.* Given a matched item, an applicable definition and a feature label, attach the label to its analysis while preserving the surface string. Saṃjñā names the act of assigning a technical designation.

**Example.** A rule marks token x as a stem. Its spelling stays x and a later rule requiring a stem becomes admissible.

The example uses an abstract label. Actual Sanskrit designations require an attested rule and scope.

[W003 · §§2–4](sources.md#s-w003) · [W004 · designation entries](sources.md#s-w004) · [Pāṇinian grammar specification · overview](../panini_grammar/GRAMMAR_SPEC.md)

<a id="substitution"></a>
## Ādeśa substitution

*Source rule.* Replace a specified item or substring by its declared substitute when its environment admits the rule. Preserve the location and the rule that fired.

**Example.** In the toy alphabet, a rule replaces x by y immediately before a. It maps xa to ya and leaves xb outside the rule’s domain.

The input, guard and replacement together identify a rule. Ādeśa is the relevant grammatical term for substitution.

[W003 · §§3–5](sources.md#s-w003) · [W099 · §§2–3](sources.md#s-w099)

<a id="insertion"></a>
## Āgama insertion and affix attachment

*Source rule.* Insert a specified token at a licensed boundary. In the string representation x|y becomes xuy for inserted u. Prefix and suffix positions give boundary specializations.

**Example.** Inserting t between a and i sends a|i to ati. Attaching a right suffix to ab appends it at the right boundary.

Augments and affixes have different grammatical provenance even when their string insertion machinery is shared.

[W003 · §§3–5](sources.md#s-w003) · [W096 · insertion helper](sources.md#s-w096) · [W101 · §5](sources.md#s-w101)

<a id="elision"></a>
## Lopa with retained history

*Source rule.* Erase marked material from the visible string while retaining its marker or past rule in the derivation record when a later operation can use it. Lopa is the grammatical name for this elision.

**Example.** The visible reading of a#Kb is ab if #K is a single marked token. A history that passed through #K can still be distinguished by a permitted future rule.

Repeat erasure after all designated marks disappear and the sound remains unchanged. Erasing an entire mathematical state would have a different effect.

[W097 · §§2,5–8](sources.md#s-w097) · [W099 · §§2,5](sources.md#s-w099) · [Canvas operators in the native cut algebra · B2](../../theorum/56_canvas_operators_nativized_theorem.md)

<a id="sandhi"></a>
## Sandhi boundary transduction

*Source rule.* Read the meeting of two sound strings and give the boundary its stipulated output. The joint may consume material from both sides.

**Example.** In the source toy rule, a joined to i gives e. Input and rule identity can be retained in a record even though the visible result has one symbol.

Sandhi names the sound change at the join. Only the stated toy domain is being used in this example.

[W095 · sandhi rules](sources.md#s-w095) · [W096 · sandhi rules](sources.md#s-w096) · [W100 · §4](sources.md#s-w100)

<a id="restriction"></a>
## Niyama domain restriction

*Source rule.* Restrict a rule r to inputs satisfying a specified predicate g. The new domain is dom(r) ∩ {x:g(x)} and the value there remains r(x).

**Example.** A stem operation restricted to bare forms accepts a bare noun and is disabled after a case ending has already been attached.

A disabled operation is different from a successful operation whose numerical result happens to be zero.

[W003 · §§3–5](sources.md#s-w003) · [W105 · §3](sources.md#s-w105)

<a id="exception"></a>
## Utsarga–Apavāda exception selection

*Source rule.* Given a default rule and a specific exception with declared precedence, use the exception on its admitted subdomain and the default on the rest of its own domain.

**Example.** A default writes A for every item in {x,y}. An exception for y writes B. The combined outputs are x→A and y→B.

This is selection by scope of the exception. Conflicts among other rules need their own declared precedence.

[W003 · §4 MR‑5](sources.md#s-w003) · [W001 · §3](sources.md#s-w001)

<a id="priority"></a>
## Vipratiṣedha priority resolution

*Source rule.* On a finite conflict set of applicable rules, apply the winner under the declared precedence, with an explicit tie rule if needed.

**Example.** If both r₁ and r₂ can rewrite x and the admitted ordering puts r₂ first, x takes r₂’s output. A disabled r₂ cannot override r₁.

A particular Sanskrit priority rule has a historical scope. The catalogue uses the finite conflict resolver.

[W001 · §3](sources.md#s-w001) · [W098 · §§4–6](sources.md#s-w098) · [Canvas operators in the native cut algebra · B2](../../theorum/56_canvas_operators_nativized_theorem.md)

<a id="optional"></a>
## Vibhāṣā optional branching

*Source rule.* For an admitted optional action r on x, return the set of licensed histories containing the unchanged case and the r-applied case.

**Example.** If r(x)=y, the two outcomes are a history ending at x and a history ending at y. Equal printed strings may still carry different histories.

This is a set-valued rule. It assigns no probability until supplied with weights.

[W003 · §4 MR‑6](sources.md#s-w003)

<a id="inheritance"></a>
## Anuvṛtti scoped inheritance

*Source rule.* Carry a specified head condition from its source rule into later rules within its declared scope. In the predicate model the inherited test is conjoined to each receiver’s local test.

**Example.** A block inherits the condition ‘vowel’. A receiver with local condition ‘final’ consequently requires both vowel and final.

The operator takes the source, recipients and stopping boundary as data. Finding historical boundaries is a separate source question.

[W001 · §3](sources.md#s-w001) · [W003 · §4](sources.md#s-w003)

<a id="visibility"></a>
## Asiddhatva visibility selection

*Specified model.* A rule evaluates its guard against a declared earlier or masked view of the derivation. The current record persists for other rules. The term names this scoped invisibility in the source’s model.

**Example.** After x is rewritten to y, a later rule declared blind to that rewrite can still test whether the earlier spelling was x.

A saved view models a specified dependency. It does not rewind all rules or imply one uniform policy for Sanskrit.

[W001 · §3 M₂](sources.md#s-w001) · [Pāṇinian grammar specification · overview](../panini_grammar/GRAMMAR_SPEC.md)

<a id="transfer"></a>
## Atideśa rule transfer

*Source rule.* Given a rule r and a specified correspondence h between its admissible source and target structures, transfer it by h r h⁻¹ on the image when h is a bijection.

**Example.** If h maps a→A and b→B, the rule a→b transfers to A→B.

The linguistic authority for a particular transfer and the domain of h are extra data. Similar spelling alone does not fix a correspondence.

[W001 · §3 M₆](sources.md#s-w001)

<a id="normal"></a>
## Rewrite normalization

*Source rule.* Given a terminating selected rewrite procedure, iterate to a terminal form. An order-independent normal form additionally requires confluence over the allowed choices.

**Example.** With aa→a, aaa reduces to a along either choice of adjacent pair. Reapplying the normalizer leaves a fixed.

A precedence policy defines one procedure even when unrestricted rule application has several endings.

[W097 · §5](sources.md#s-w097) · [W098 · §§4–6](sources.md#s-w098) · [W096 · fixed-point engine](sources.md#s-w096) · [Canvas operators in the native cut algebra · B2](../../theorum/56_canvas_operators_nativized_theorem.md)

<a id="phase-history"></a>
## Phase-weighted rewrite

*Source rule.* Along a licensed rewrite, update both the string and a complex weight. A transition of declared phase χ sends (s,w) to (r(s),χw). The full ordered rule record may be kept separately.

**Example.** Two phases i followed by −1 multiply an initial weight 1 to −i. The same product can arise from a different rule order.

The historical Python prototype derives its phase from a pattern-string hash. It demonstrates propagation and does not measure a phoneme frequency.

[W095 · lambda_phase and rewrite](sources.md#s-w095) · [W098 · §8](sources.md#s-w098)

<a id="tamil"></a>
## Tamil guarded inflection

*Existing GitHub fixture.* On a bare noun carrying lexeme, number and case state, take a declared plural or case transition and use its selected stem change. A case-bearing state is terminal in the repository’s two-noun fixture.

**Example.** மரம் (maram, tree) → மரங்கள் (maraṅkaḷ, trees) → மரங்களை (maraṅkaḷai, trees as object). The reverse order is disabled on its second step.

The bounded tree and house paradigms cover accusative and locative. The Drive programme also proposes longer derivational suffix sequences.

[T13 · §2](sources.md#s-t13) · [T09 · §6](sources.md#s-t09) · [Tamil and Hebrew recognition seams · Tamil order witness](../cross_linguistic_seams/README.md)

<a id="template"></a>
## Hebrew root–template realization

*Specified model.* Given an ordered root and a pattern with explicitly numbered slots, fill those slots and retain root and pattern in the analysis. Any vowels, stem changes and lexical exceptions must be supplied.

**Example.** Fill the written pattern [1, 2, ו, 3] with כ, ת, ב to obtain כתוב. The result still carries the three original root positions. Choosing a reading requires further lexical information.

The source combines root, template and pointing. A template independent of its vocalization is a modeling convention and cannot generate the whole language from these three letters alone.

[H07 · §§2–5](sources.md#s-h07) · [H06 · §4](sources.md#s-h06)

<a id="hebrew-spelling"></a>
## Hebrew pointing erasure

*Existing GitHub fixture.* For the attested pointed words in the branch fixture, remove the combining pointing marks while preserving the ordered base letters and, in the hidden data, the input analysis.

**Example.** כָּתַב (‘wrote’), כְּתָב (‘script’) and כַּתָּב (‘reporter’) all display as כתב under the unpointed observer.

This is an orthographic map. Lopa and this erasure have different input tags and different grammatical roles.

[H07 · §2](sources.md#s-h07) · [Tamil and Hebrew recognition seams · Hebrew recognition](../cross_linguistic_seams/README.md)

<a id="hebrew-context"></a>
## Hebrew context restriction and plural observation

*Existing GitHub fixture.* Start from the candidate lexical analyses for an unpointed token. Intersect them with the independently supplied slot and admissible neighboring-word cues, then observe their declared plural spellings.

**Example.** For the three selected readings of כתב, the pooled plural target has two unpointed outputs and three pointed outputs. When context leaves one reading, one plural output remains for that target.

This counts one bounded inference procedure. Its output-class counts give one versus two fixed-width bits for the two versus three target classes within this spelling. The branch measures residual memory after receiving context.

[H03 · §§2–5](sources.md#s-h03) · [H07 · §§2,5](sources.md#s-h07) · [Tamil and Hebrew recognition seams · Context and construct state](../cross_linguistic_seams/README.md)

<a id="uyirmei"></a>
## Uyirmei consonant–vowel formation

*Source rule.* Given a Tamil consonant and a vowel in the traditional 18-by-12 chart, use the spelling table to produce the corresponding written combination. Uyirmei is the Tamil term for this class of letters.

**Example.** க் (k) combined with இ (i) gives கி (ki). The chart has 216 consonant–vowel positions.

The table supplies a composition of written forms. The number 216 alone gives no group operation or theory of meaning.

[T13 · §3](sources.md#s-t13) · [T12 · §3](sources.md#s-t12) · [Basic Tamil, consonant and vowel combinations · Chapter 1.3](https://openbooks.lib.msu.edu/basictamil/chapter/chapter-1-2/)

<a id="gematria"></a>
## Gematria letter-value sum

*Source rule.* Choose a specified Hebrew letter-value convention. The readout of a word is the sum of the tabulated values of its letters. ‘Gematria’ names this established numerical reading.

**Example.** With א=1 and ב=2, אב has value 3 and בא also has value 3. The two different orders have become indistinguishable to this observer.

Other conventions must name their own tables. A numerical collision neither establishes shared meaning nor permits exact spelling reconstruction.

[H07 · §4](sources.md#s-h07) · [H05 · §2](sources.md#s-h05) · [Gematria and standard Hebrew letter values · standard letter values](https://www.chabad.org/library/article_cdo/aid/5541252/jewish/What-Is-Gematria.htm)

<a id="seed-code"></a>
## Bīja seed encoding

*Specified model.* Given a finite codebook c assigning each admitted source phrase a seed label, map a phrase to c(phrase). Bīja means seed in the source’s compression analogy.

**Example.** If two phrases map to seed S, the reader of S has two possible sources. A retained one-bit label can distinguish those two entries.

Exact decoding from the seed alone requires injectivity on the admitted phrase set. The source’s claimed expansion needs a codebook or side information.

[W017 · §3](sources.md#s-w017) · [W013 · §1](sources.md#s-w013) · [W016 · §4](sources.md#s-w016)
