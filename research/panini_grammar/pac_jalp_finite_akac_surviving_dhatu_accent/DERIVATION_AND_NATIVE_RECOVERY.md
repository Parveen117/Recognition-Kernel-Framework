# Surviving dhātu accent and full-carrier recovery

PG533 owns the two words and their histories:

- pac 1011151, cooking, active laṭ P3sg, śap, fixed `pacat|ak|i_ENDING`;
- jalp 1010464, articulate speech, active laṭ P3sg, śap, fixed `jalpat|ak|i_ENDING`.

PG661 then settles the competing suffix-side paths: the original `tip` vowel is anudātta under 6.1.186, which explicitly blocks 6.1.163 cit-final udātta. No word, morphology or final-ending accent credit is repeated here.

Kāśikā 6.1.162 positively assigns udātta to the final vowel of a dhātu and gives `pacati` as an exact example. The rule is general to the dhātu recipient, so the same typed operation applies to jalp without changing its root sense or source word. Kāśikā 6.1.158 explains the one-excepted word-accent procedure: the vowel for which the surviving accent is prescribed is excepted while the remainder is anudātta. Because PG661 has already removed the cit-final competitor and retained the ending as anudātta, the dhātu-final vowel is the positive owner in these two records.

The output is stored structurally as `DHATU_FINAL_UDATTA`; no accent-marked whole word is invented. This construction is not extended to *svapitaki/śvasitaki*: their preserved rudādi iṭ creates a separate augment/accent interaction that the present pinned decision does not settle.

## Full PG14 carrier and typed zero specialization

`B⁺=C⟨z_e,z_e*⟩`, `Mλ⁺=⊕h e_hB⁺`, with pairing `⟨x,y⟩=Σh x_h* y_h`. A grade retains root ID and sense, null preverb, active voice, P3sg laṭ, śap, original `tip`, akac placement, `c_IT`, PG661's selected ending anudātta, the 6.1.162 dhātu recipient, and Open/Excluded scope.

`Q:PacJalpAkacRequest→OwnedPG661EndingDecision`; `C:OwnedPG661EndingDecision×DhatuAccent→PositiveAccentCandidate`; `R:PositiveAccentCandidate×OneExceptedRule→DhatuFinalUdatta`; `P` retains the complete record. The typed square is

`π0,DhatuFinalUdatta Pλ Rλ(Cλ(Qλ,id_K),id_DHATU),id_61158) = P0 R0(C0(Q0,id_K),id_DHATU),id_61158) π0,PacJalpAkacRequest`.

For every admitted edge, `T_e,λ(e_h a)=e_h′(1+z_e)a`, zero elsewhere. The unital dagger empty-word map satisfies `ε⁺((1+z_e)a)=ε⁺(a)`. State `π0`, operator `Π0,op` and scalar `ε⁺` remain distinct. Unit starts have coefficient one; every admitted zero path has its same-labelled lift. Finite sums, composition, adjoints, cuts, complements and pairing commute.

Typed specialization cannot merge dhātu-final `a` with śap-`a`, original `i_ENDING`, akac-`a` or `c_IT`; nor can it transfer the pac/jalp decision to a rudādi-iṭ word. The same-labelled zero-stage dhātu recipient has the same-labelled lifted accent owner. Grammatical lopa is not `ε⁺`; lambda is not time or a completion ratio.

The two exact positive accent-owner records close locally; the other two PG661 non-ending accents and wider written gates remain Open.
