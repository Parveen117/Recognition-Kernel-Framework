# Exact finite-akac accent conflict and full-carrier recovery

PG533 fixes four source words and their internal ownership:

| word | root/sense | inner present history | fixed akac placement |
| --- | --- | --- | --- |
| `pacataki` | pac 1011151, cooking | bhvādi śap + P3sg `tip` | `pacat|ak|i_ENDING` |
| `jalpataki` | jalp 1010464, articulate speech | bhvādi śap + P3sg `tip` | `jalpat|ak|i_ENDING` |
| `svapitaki` | svap 1020063, sleep | adādi śap-luk + 7.2.76 iṭ + P3sg `tip` | `svap-iṭ-t|ak|i_ENDING` |
| `śvasitaki` | śvas 1020064, breathe | adādi śap-luk + 7.2.76 iṭ + P3sg `tip` | `śvas-iṭ-t|ak|i_ENDING` |

Those words and operations receive no second credit.

## Competing accent paths

Akac has `c_IT`. Under 6.1.163, a cit affix ordinarily assigns udātta to the final vowel of the whole prakṛti-affix community. Because 5.3.71 inserts `ak` before the final vowel of the finite input, the candidate recipient in these four words is the original `tip` vowel `i_ENDING`, not the inserted `a` and not the rudādi iṭ.

The same `i_ENDING` remains part of an original l-sārvadhātuka ending. Kāśikā 6.1.186 prescribes anudātta for that l-sārvadhātuka after an anudātta-it root or an a-ending upadeśa and then states the priority result directly: `citsvaro'py anena lasārvadhātukānudāttatvena paratvād bādhyate`—the cit accent too is blocked by the later l-sārvadhātuka anudātta. Thus:

1. `pacataki` and `jalpataki` reach the a-ending śap condition preserved by PG533;
2. `svapitaki` and `śvasitaki` retain their anudātta-it root histories;
3. the original P3sg `tip` is the l-sārvadhātuka recipient in every record;
4. its final `i_ENDING` is selected as anudātta;
5. 6.1.163 cannot reassign udātta to that same ending vowel.

This is not deletion of all word accent. It is a typed conflict resolution for one vowel. Kāśikā 6.1.158 says that an accent prescription makes the remaining vowels anudātta except for the vowel whose accent survives, but the present packet does not infer a fully decorated surface beyond the pinned decision. In particular, 6.1.188 is inapplicable to the fixed svap/śvas inputs because it requires an ajādi aniṭ l-sārvadhātuka, while 7.2.76 supplies explicit iṭ here. Their complete non-ending accent placement stays Open.

## Full PG14 carrier and typed zero specialization

`B⁺=C⟨z_e,z_e*⟩`, `Mλ⁺=⊕h e_hB⁺`, with pairing `⟨x,y⟩=Σh x_h* y_h`. A grade retains root ID and sense, preverb, active voice, P3sg laṭ, śap or śap-luk history, rudādi iṭ where present, original `tip`, exact akac placement, `c_IT`, competing 6.1.163/6.1.186 paths, the selected ending-vowel feature and every Open/Excluded boundary.

`Q:FixedFiniteAkacRequest→OwnedPG533Word`; `C:OwnedPG533Word×AccentRules→CompetingFinalVowelPaths`; `R:CompetingFinalVowelPaths×RuleOrder→EndingAnudatta`; `P` retains the complete record. The typed square is

`π0,EndingAnudatta Pλ Rλ(Cλ(Qλ,id_K),id_ACCENT),id_ORDER) = P0 R0(C0(Q0,id_K),id_ACCENT),id_ORDER) π0,FixedFiniteAkacRequest`.

For every admitted edge, `T_e,λ(e_h a)=e_h′(1+z_e)a`, zero elsewhere. The unital dagger empty-word map satisfies `ε⁺((1+z_e)a)=ε⁺(a)`. State `π0`, operator `Π0,op` and scalar `ε⁺` remain distinct. Unit starts have coefficient one; every admitted zero path has its same-labelled lift. Finite sums, composition, adjoints, cuts, complements and pairing commute.

Typed specialization cannot merge `i_ENDING` with rudādi iṭ, `c_IT` with sounded `k`, śap with śap-luk, pac/jalp with svap/śvas, or the blocked final accent with an accentless word. The same label that owns the zero-stage ending owns its lifted anudātta decision. Grammatical lopa is not `ε⁺`; lambda is not time or a completion ratio.

The exact final-ending conflict closes locally. Other accent recipients and wider written gates remain Open.
