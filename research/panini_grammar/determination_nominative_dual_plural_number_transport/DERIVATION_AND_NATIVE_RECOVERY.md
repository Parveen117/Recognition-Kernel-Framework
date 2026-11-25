# PG816 · Derivation and native recovery

## Inherited stems; newly constructed number frames

PG431 already closes the six principal singular gender/case panels and explicitly leaves “dual/plural determination realization with explicitly admitted selected-member number/context frames” Open. This stage does not recreate its stem formation or singular outputs. It reuses the positively sourced mappings:

| source | affix | stem |
|---|---|---|
| `kim` | `ḍatarac` | `katara` |
| `kim` | `ḍatamac` | `katama` |
| `yad` | `ḍatarac` | `yatara` |
| `yad` | `ḍatamac` | `yatama` |
| `tad` | `ḍatarac` | `tatara` |
| `tad` | `ḍatamac` | `tatama` |

Kāśikā 5.3.92 defines `ḍatarac` as determination of one member from a pair; 5.3.93 defines `ḍatamac` as determination of one member from many in the qualified inquiry. The derived stems are sarvanāma by 1.1.27. Number under 1.4.21–22 and the sup endings of 4.1.2 belong to the selected referent, not automatically to the comparison set.

The new contract is therefore:

\[
N_D(q,C,m,|m|=2)=(q,C,m,\mathrm{dual}),\qquad
N_P(q,C,m,|m|>2)=(q,C,m,\mathrm{plural}),
\]

where `m` remains the one selected member under the inherited determination policy, but `m` may itself be a paired or plural group. Thus `katara` with dual number means “which dual/grouped member, of the two candidate members?”; it does **not** license selecting two separate candidates from the comparison pair. The same guard applies to plural. A flat multiple-selection reading is Excluded only from this grouped-member contract unless a positive source independently licenses it. Other textual gaps remain Open.

PG422's `K_STRICT` and reported `SK_BALA_REPORTED_BROAD` policies remain separate and Accepted with their existing source labels. PG816 adds no source-policy decision and does not upgrade the reported broader policy into an independently witnessed one.

## Owned nominative endings

All 36 literal rows are written in [NOMINAL_FORMS.tsv](NOMINAL_FORMS.tsv); no Sanskrit generator was run.

| gender/number | original ending | owned history | example |
|---|---|---|---|
| M dual | `au` | direct dual plus 6.1.88 | `katarau` |
| M plural | `jas` | whole-ending `śī`, 7.1.17 | `katare` |
| F dual | `au` | whole-ending `śī`, 7.1.18 | `katare` |
| F plural | `jas` | inherited `ṭāp` plus nominative plural | `katarāḥ` |
| N dual | `au` | whole-ending `śī`, 7.1.19 | `katare` |
| N plural | `jas` | short `śi`, `num`, 6.4.8 | `katarāṇi` |

The shared printed `-e` does not erase its distinct M-plural, F-dual and N-dual histories. The neuter plural keeps a more visible distinction: 7.1.20 supplies short `śi`, 7.1.72 supplies `num`, and 6.4.8 lengthens the preceding vowel. Stem `r` in the three `-tara` forms licenses retroflex `ṇ` under 8.4.1–2 (`katarāṇi`, `yatarāṇi`, `tatarāṇi`); the three `-tama` forms have no such owner and retain dental `n` (`katamāni`, `yatamāni`, `tatamāni`). The nasal is `num`, not a lexical stem nasal or the masculine plural `śas` nasal.

These are nominal derived-pronoun frames: roots are `null`, preverbs are empty and voice is `null`. Affix ownership stays `ḍatarac` versus `ḍatamac`; source question, comparison-set policy, selected grouped member, gender, original sup, ending substitution, nasal owner and ordered history all remain explicit.

## PG14 carrier and typed zero-specialization

Reuse PG14's full history carrier

\[
B=C_\Sigma\langle z_e,z_e^*:e\in E\rangle,\qquad
M_\lambda=\bigoplus_{h\in\mathcal H}e_hB,\qquad
M_0=\bigoplus_{h\in\mathcal H}e_hC_\Sigma.
\]

For this extension take the typed state

\[
X=(q,C,m,|m|,P,a,s,g,c,n,u,k,o,h,w),
\]

retaining source question `q`, comparison set `C`, selected member `m`, member cardinality, policy `P`, affix `a`, stem `s`, gender `g`, case `c`, number `n`, original sup `u`, marker/substitution/nasal owner `k`, source `o`, ordered history `h` and word `w`. Each admitted edge acts on the full carrier by

\[
T_{e,\lambda}(e_hb)=e_{h'}(1+z_e)b,
\qquad
\pi_{0,M}T_{e,\lambda}=T_{e,0}\pi_{0,M}.
\]

Let `N` be the guarded number-transport adapter and `E` the gender/number-owned nominative-ending adapter. Their typed zero components are identities on the respective zero fibres:

\[
N_0(X)=X,\qquad E_0(X)=X,
\]

and, on their admitted domains,

\[
\pi_{0,\mathrm{NumberFrame}}N_\lambda
=N_0\pi_{0,\mathrm{DeterminationFrame}},\qquad
\pi_{0,\mathrm{Word}}E_\lambda
=E_0\pi_{0,\mathrm{NumberFrame}}.
\]

Hence `π₀(Eλ Nλ(X)) = E₀ N₀(π₀X)`. Zero specialization removes selected residue coefficients but preserves the one-member determination, grouped-member cardinality, source policy, affix, original ending, nasal owner and ordered history. It therefore does not identify three distinct `-e` histories or the `-ṇi/-ni` branches. This is a written local lift/recovery proof, not grammar execution, universal confluence, source reconciliation or a physical-time claim.

## Closure boundary

Accepted: all 36 displayed forms under the guarded grouped-member reading and both already registered source-labelled semantic policies. Excluded from this contract: unlicensed flat selection of multiple comparison-set members. Open: non-nominative dual/plural cases, vocative, accent, compounds/names/subordination, the remaining derived-pronoun classes, independent Bhāṣya/Kaiyaṭa/commentary reconciliation, external source collation, C2–C5 and S1–S7. PG335's correction and PG340/346, PG349–352, PG355–360 and PG357–363 closures remain untouched. Claude retains Sanskrit generators, grammar execution, untouched suites and certificate replay.
