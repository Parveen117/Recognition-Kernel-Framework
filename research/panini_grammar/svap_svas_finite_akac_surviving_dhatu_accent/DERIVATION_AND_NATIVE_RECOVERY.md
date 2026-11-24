# Seṭ rudādi iṭ and the surviving dhātu accent

PG533 fixes two exact active laṭ P3sg inputs:

- svap 1020063, sleep: `svap-iṭ-t|ak|i_ENDING`;
- śvas 1020064, breathe: `śvas-iṭ-t|ak|i_ENDING`.

The iṭ is the 7.2.76 augment before the val-initial sārvadhātuka ending. It is
not akac's `c_IT`, the sounded `ak`, the root-final vowel or the original
ending vowel. PG661 already selects 6.1.186 anudātta for `i_ENDING` and records
that this later l-sārvadhātuka decision blocks 6.1.163 cit-final udātta.

Kāśikā 6.1.162 positively assigns udātta to a dhātu's final vowel. The remaining
possible svap/śvas competitor is 6.1.188, but its own wording requires an
ajādi **aniṭ** l-sārvadhātuka. It explicitly asks “why aniṭ?” and supplies
seṭ `svapitaḥ/śvasitaḥ` as the counterdomain; Nyāsa identifies their iṭ as
7.2.76. Therefore that optional initial route is not licensed for the fixed
`svapiti/śvasiti` histories carried into akac.

The iṭ's presence alone is not a rule assigning it udātta. Kāśikā 6.1.158
distinguishes an augment's possible accent from mere augment membership: an
augment accent can defeat a root accent when some accent prescription exists,
but 7.2.76 is the formation rule and supplies no such positive accent here.
After the PG661 final-ending conflict is resolved, 6.1.162 remains the positive
owner: the dhātu-final `a` is `UDATTA`, with the other vowels structurally
anudātta under the one-excepted procedure.

This is a bounded source-policy decision for the two exact PG533 records. It
does not claim that every iṭ is accentless, transfer 6.1.188 into seṭ contexts,
or fabricate accent marks for the whole words. `svapitaki/śvasitaki` receive
one accent construction/two records and no repeated word or morphology credit.

## Full PG14 carrier and typed zero specialization

Use `B⁺=C⟨z_e,z_e*⟩`, `Mλ⁺=⊕h e_hB⁺`, with pairing
`⟨x,y⟩B⁺=Σh x_h* y_h`. A grade retains root ID/sense, null preverb, active
voice, P3sg laṭ, śap-luk, 7.2.76 iṭ, original `tip`, akac placement and `c_IT`,
PG661 ending anudātta, the guarded 6.1.188 path, the selected 6.1.162 dhātu
recipient, and all Accepted/Open/Excluded boundaries.

Let `Q:SetRudadiAkacRequest→OwnedPG661EndingDecision` preserve the word and
ending result; `G:OwnedPG661EndingDecision×AccentGuards→BlockedOptionalInitial`
apply the aniṭ guard without deleting iṭ; `R:BlockedOptionalInitial×DhatuAccent→DhatuFinalUdatta`
select the surviving recipient; and `P` retain the complete record. Then

`π0,DhatuFinalUdatta Pλ Rλ(Gλ(Qλ,id_K),id_GUARD),id_DHATU) = P0 R0(G0(Q0,id_K),id_GUARD),id_DHATU) π0,SetRudadiAkacRequest`.

For admitted `e:h→h′`, `T_e,λ(e_h a)=e_h′(1+z_e)a`, zero elsewhere. The
unital dagger empty-word map satisfies `ε⁺((1+z_e)a)=ε⁺(a)`. State `π0`, typed
operator-entry `Π0,op` and scalar-pairing `ε⁺` specializations remain distinct.
Every unit-start admitted zero path has the same-labelled lift; finite sums,
composition, adjoints, cuts, complements and pairing commute with their
correctly typed maps.

Typed zero specialization cannot merge root-final `a` with iṭ-`i`, original
`i_ENDING`, akac-`a` or `c_IT`; cannot turn an aniṭ guard into deletion of the
seṭ augment; and cannot transfer the pac/jalp śap history into these rudādi
records. Grammatical lopa is not `ε⁺`; lambda is neither elapsed time nor a
completion ratio.

The two exact positive accent-owner records close locally. Other akac accent,
recitation and wider written gates remain Open.
