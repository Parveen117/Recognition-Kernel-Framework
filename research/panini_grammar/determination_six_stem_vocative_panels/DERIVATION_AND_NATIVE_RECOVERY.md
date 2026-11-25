# PG880 · Derivation and native recovery

## Positive address and number evidence

Kāśikā 2.3.47 defines address as turning the addressee toward the speaker and
assigns the first case where bare stem meaning would not itself supply it. Its
three examples are explicit in number: `he devadatta`, `he devadattau`, `he
devadattāḥ`. Rule 2.3.49 names only the address first singular `sambuddhi`.
Therefore singular takes the special sambuddhi operations, while dual and
plural retain their ordinary first-case gender/number ending histories under a
vocative case-role key.

PG431 already fixes the six derived-pronoun stems, their source questions and
their affix owners. PG816 separately closes their M/F/N nominative dual and
plural endings under the guarded grouped-member reading. PG880 makes two
positive scope decisions:

1. the gender-neutral address rule of 2.3.47 admits these six already sourced
   stems in all three genders and all three numbers;
2. only the singular is `sambuddhi`: M singular uses the ordinary short-`a`
   route, F singular the `ṭāp` route, and N singular keeps PG818's `adḍ` route.

The source fields were already frozen in PG40, the compound-case source record,
PG431, PG816 and PG818. They are reused by exact file/commit pin, so PG880 claims
zero new source observations.

## Singular ownership

For masculine `katara/katama` and their `yad/tad` counterparts, address supplies
first singular `su`. Rule 6.1.69 deletes the consonant of the sambuddhi ending
after the short-vowel stem: `katara + su → katara`. Rule 7.1.25 does not replace
this masculine ending; its `adḍ` route inherits the neuter domain of 7.1.23–24.

For the feminine, PG431's `ṭāp` gives long `ā`. Rule 7.3.106 directly replaces
final `ā` of the feminine affix by `e` before sambuddhi, and 6.1.69 removes the
ending consonant: `katarā + su → katare`. This is not the M-plural `śī` history,
even when the printed word is also `katare`.

The N singular is not re-credited. PG818 already derives `katarat/katarad` and
the other five pairs from whole-ending `adḍ`, deleted `ḍ_IT`, stem-final ṭi-lopa
and the pause option. The six rows in the new table are explicit controls with
position and reading credit zero.

## Dual and plural ownership

Because 2.3.47 supplies first case to address and 2.3.49 restricts sambuddhi to
singular, every dual/plural vocative reuses the corresponding PG816 ending
history but owns a new vocative case key:

| gender/number | retained owner | example |
|---|---|---|
| M dual | direct `au`, 6.1.88 | `he katarau` |
| M plural | `jas → śī`, 7.1.17 | `he katare` |
| F dual | `au → śī`, 7.1.18 | `he katare` |
| F plural | inherited `ṭāp + jas` | `he katarāḥ` |
| N dual | `au → śī`, 7.1.19 | `he katare` |
| N plural | `jas → śi + num`, 7.1.20, 7.1.72, 6.4.8 | `he katarāṇi` |

Equal printed `-e` does not merge M plural, F dual or N dual. The N plural keeps
PG816's internal-nasal distinction: `-tara` permits `ṇ` under 8.4.1–2, while
`-tama` retains dental `n`. Roots are `null`, preverbs are empty and voice is
`null`; source question, comparison policy, affix, gender, number, vocative role,
original sup, operation owner and word remain explicit.

## Credit and duplicate boundary

The literal table contains 54 selected vocative keys. Six N singular keys are
PG818 controls. The other 48 are new: six stems × two M/F singulars, plus six
stems × three genders × two non-singular numbers. Every new key has one reading.
No nominative key is re-credited: identical spelling across case roles is not
identity of the case request. Flat selection of multiple comparison-set members
remains excluded only from PG816's grouped-member contract; it is not a claim
that a missing text or different construction is ungrammatical.

## PG14 carrier and typed zero-specialization

Reuse PG14's full operator/history carrier

\[
B=C_\Sigma\langle z_e,z_e^*:e\in E\rangle,\qquad
M_\lambda=\bigoplus_{h\in\mathcal H}e_hB,\qquad
M_0=\bigoplus_{h\in\mathcal H}e_hC_\Sigma.
\]

Use the typed state

\[
X=(q,C,m,|m|,P,a,s,g,n,\mathrm{addr},c,u,k,o,h,w),
\]

retaining source question, comparison set, selected grouped member/cardinality,
policy, affix, stem, gender/number, address relation, vocative case, original
sup, ending operation owner, source, ordered history and word. For each admitted
event,

\[
T_{e,\lambda}(e_hb)=e_{h'}(1+z_e)b,
\qquad \pi_{0,M}T_{e,\lambda}=T_{e,0}\pi_{0,M}.
\]

Let `A` be the typed 2.3.47 address-to-first-case adapter, `S` the singular
sambuddhi selector, and `E` the gender/number-owned ending adapter. On their
respective zero fibres their typed components preserve all labels:

\[
A_0(X)=X,\qquad S_0(X)=X,\qquad E_0(X)=X.
\]

On the admitted domains,

\[
\pi_{0,\mathrm{FirstCase}}A_\lambda=A_0\pi_{0,\mathrm{AddressRequest}},
\]

\[
\pi_{0,\mathrm{EndingFrame}}S_\lambda=S_0\pi_{0,\mathrm{FirstCase}},
\qquad
\pi_{0,\mathrm{Word}}E_\lambda=E_0\pi_{0,\mathrm{EndingFrame}}.
\]

Hence

\[
\pi_{0,\mathrm{Word}}E_\lambda S_\lambda A_\lambda
=E_0S_0A_0\pi_{0,\mathrm{AddressRequest}}.
\]

For dual/plural, `S` is the typed identity and retains PG816's ending history;
for singular it selects the M short-`a`, F `ṭāp`, or N `adḍ` channel. Typed zero
specialization therefore does not collapse the three `katare` histories or
erase the N-singular marker/payload distinction. This is a written local
lift/recovery proof, not Sanskrit execution, universal vocative morphology or
a physical-time claim.

## Closure boundary

Accepted: the 48 new rows in `VOCATIVE_FORMS.tsv` and the six PG818 controls.
Locally closed after PG818+PG880: the selected six stems' M/F/N vocatives in all
three numbers. Still Open: accent, compounds/names/subordination, other
derived-pronoun members, independent Bhāṣya/Kaiyaṭa and external source
collation, wider C2–C5 and S1–S7. PG335's correction and PG340/346, PG349–352,
PG355–360 and PG357–363 closures remain untouched. Claude retains Sanskrit
generators, grammar execution, untouched suites and certificate replay.
