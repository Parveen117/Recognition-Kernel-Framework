# PG881 · Derivation and native recovery

## Reviewed inputs and positive address licence

PG434 closes the selected ordinary M/F/N singular cases of lexical `itara`,
`anya` and `anyatara`; PG819 closes their dual/plural non-vocative panels.
PG433 similarly closes `ekatara/ekatama` singulars and PG820 their dual/plural
non-vocatives. All five packets explicitly leave vocative Open. No new lexical
sense or stem is inferred here.

PG880 positively reads Kāśikā 2.3.47: address receives first-case endings, and
the rule prints singular, dual and plural examples. Rule 2.3.49 restricts the
special `sambuddhi` designation to singular. PG881 reuses that reviewed address
adapter by exact commit/file pin. Dual/plural therefore preserve PG819/820's
gender-number ending histories under new vocative keys; singular selects its
actual M, F or N channel.

## Masculine and feminine singular

Each masculine short-`a` stem receives address `su`; 6.1.69 deletes the ending
consonant, yielding `itara`, `anya`, `anyatara`, `ekatara`, `ekatama`. Each
feminine is the already owned `ṭāp` stem. Rule 7.3.106 replaces final `ā` by
`e` before sambuddhi and 6.1.69 removes the ending consonant, yielding `itare`,
`anye`, `anyatare`, `ekatare`, `ekatame`. These F-singular histories remain
distinct from M-plural and F/N-dual `-e`.

## The neuter singular fork

Kāśikā 7.1.25 names `itara`, `anya`, `anyatara` and the `ḍatara/ḍatama`
families in its five-member `adḍ` domain. Ordinary neuter singular address of
the lexical three and `ekatama` therefore uses whole-ending `adḍ`; deleted
`ḍ_IT` licenses 6.4.143 stem-final ṭi-lopa, and 8.4.56 preserves the paired
pause readings:

| stem | selected readings |
|---|---|
| `itara` | `itarat / itarad` |
| `anya` | `anyat / anyad` |
| `anyatara` | `anyatarat / anyatarad` |
| `ekatama` | `ekatamat / ekatamad` |

Rule 7.1.26 is not a spelling heuristic: it positively blocks `adḍ` for
`ekatara` in both chandas and ordinary language. Neuter `ekatara` instead
takes the 7.1.24 `am` replacement. Kāśikā 6.1.69 explicitly explains that in
a neuter sambuddhi the consonant of this `am` is deleted even though it is not
an apṛkta affix. Hence `ekatara + am → ekatara`, with no ending-ḍit and no
second ṭi-lopa. The shared surface with M singular does not merge gender or
ending history. The itara-chandas `itaram` control from PG434 is a separate
register-specific direct-case path; it is not exported to ordinary vocative.

## Dual and plural

Under 2.3.47 the dual/plural address uses the same first-case sup histories
already written at PG819/820. Case role is new; ending derivation is not
re-credited:

| gender/number | owner | representative outputs |
|---|---|---|
| M dual | direct `au`, 6.1.88 | `itarau`, `anyau`, `ekatarau` |
| M plural | `jas → śī`, 7.1.17 | `itare`, `anye`, `ekatare` |
| F dual | `au → śī`, 7.1.18 | `itare`, `anye`, `ekatare` |
| F plural | `ṭāp + jas` | `itarāḥ`, `anyāḥ`, `ekatarāḥ` |
| N dual | `au → śī`, 7.1.19 | `itare`, `anye`, `ekatare` |
| N plural | `jas → śi + num` | `itarāṇi`, `anyāni`, `ekatarāṇi` |

The `r`-bearing N plurals retain internal `ṇ`; `anya` and `-tama` retain dental
`n`. Roots are `null`, preverbs empty and voice `null`. Lexeme/affix, sense,
register, gender, number, address role, original sup, marker/exception and word
are separate owned coordinates.

## Credit boundary

The literal table contains five stems × three genders × three numbers = 45 new
case keys. Four N-singular rows have two pause readings, so the reading total is
49. No PG433/434 direct case or PG819/820 nominative key is re-credited.
Identical words across nominative/vocative or gender histories are not identical
requests. Unresolved senses and source histories stay Open rather than becoming
exclusions.

## PG14 carrier and typed zero-specialization

Reuse PG14's full carrier

\[
B=C_\Sigma\langle z_e,z_e^*:e\in E\rangle,\qquad
M_\lambda=\bigoplus_{h\in\mathcal H}e_hB,\qquad
M_0=\bigoplus_{h\in\mathcal H}e_hC_\Sigma.
\]

Use the typed state

\[
X=(\ell,s,r,P,a,g,n,\mathrm{addr},c,u,k,o,h,w),
\]

retaining lexeme, sense, register, source policy, affix/lexical-stem status,
gender/number, address relation, vocative case, original sup, ending/exception
owner, source, ordered history and word. Each admitted event satisfies

\[
T_{e,\lambda}(e_hb)=e_{h'}(1+z_e)b,
\qquad \pi_{0,M}T_{e,\lambda}=T_{e,0}\pi_{0,M}.
\]

Let `A` admit address and first case, `S` choose singular sambuddhi versus the
dual/plural identity channel, `G` select the actual gender-number ending, and
`W` realize the pause word. Their zero components preserve typed labels, and

\[
\pi_{0,\mathrm{Word}}W_\lambda G_\lambda S_\lambda A_\lambda
=W_0G_0S_0A_0\pi_{0,\mathrm{AddressRequest}}.
\]

On N singular, `G` has distinct `adḍ` and `ekatara`-blocked summands. Typed
zero specialization preserves ordinary versus chandas register, ending m
versus d payload, deleted `ḍ_IT`, ṭi-lopa owner, gender and case. It therefore
cannot turn the positive `ekatara` exception into an `-tara` spelling rule or
merge equal `-e` outputs. This is a local written lift/recovery proof, not
Sanskrit execution, universal vocative morphology or a physical-time claim.

## Closure boundary

Accepted: all 45 literal rows and 49 readings in `VOCATIVE_FORMS.tsv`.
Locally closed: selected M/F/N vocatives of the five stems across all numbers.
Still Open: other senses, compounds/names/subordination, accent, independent
Maitrāyaṇī/Kaiyaṭa/print collation, remaining derived-pronoun classes, C2–C5
and S1–S7. PG335's correction and PG340/346, PG349–352, PG355–360 and
PG357–363 closures remain untouched. Claude retains Sanskrit generators,
grammar execution, untouched suites and certificate replay.
