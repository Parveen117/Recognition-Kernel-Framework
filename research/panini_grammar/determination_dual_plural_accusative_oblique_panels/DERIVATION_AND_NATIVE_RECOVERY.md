# PG817 · Derivation and native recovery

## Scope and credit boundary

PG431 closes the singular M/F/N seven-case panels for `katara/katama`, `yatara/yatama` and `tatara/tatama`. PG816 closes their nominative dual/plural positions and supplies the guarded grouped-member number contract. A repository-wide exact-form and determination-register audit found no credited accusative–locative dual/plural keys for these six principal stems. Forms under `chinnakatar-` and `chinnakatam-` belong to different comparative/superlative derivations and are not duplicates.

This stage literally writes 36 stem×gender×number rows in [CASE_PANELS.tsv](CASE_PANELS.tsv). Each row contains six independently keyed cases, so the ledger owns `36 × 6 = 216` positions and readings. No generator or grammar execution produced them.

Roots are `null`, preverbs are empty and voice is `null`. The inherited source-question and affix mappings remain:

| source | affix | stems |
|---|---|---|
| `kim/yad/tad` | `ḍatarac` | `katara/yatara/tatara` |
| `kim/yad/tad` | `ḍatamac` | `katama/yatama/tatama` |

Both `K_STRICT` and `SK_BALA_REPORTED_BROAD` retain their existing source labels. No new source priority is asserted.

## Case-role transport

For inherited determination frame `D=(q,C,m,|m|,P,a,s,g,n)`, PG817 adds a case-role request `r` and original sup `u_r`:

\[
R_r(D)=(q,C,m,|m|,P,a,s,g,n,r,u_r).
\]

The selected member `m` remains one grouped member under PG816; case marks that member's relation in the clause. Accusative, instrumental, dative, ablative, genitive and locative are therefore six distinct keys even when several print the same word. In the dual, `bhyām` owns instrumental/dative/ablative and `os` owns genitive/locative. Their equal surfaces do not merge case roles. In the plural, dative and ablative share `bhyas` but retain distinct addresses.

## Ending owners

The frozen sarva register supplies the reviewed a-final sarvanāma consumers. PG817 applies them to the already sourced determination stems without claiming a new general declension theorem.

| domain | accusative | instrumental | dative | ablative | genitive | locative |
|---|---|---|---|---|---|---|
| M dual | `auṭ → -au` | `bhyām → -ābhyām` | same surface, DAT key | same surface, ABL key | `os → -ayoḥ` | same surface, LOC key |
| F dual | `auṭ → śī → -e` | `-ābhyām` | DAT key | ABL key | `-ayoḥ` | LOC key |
| N dual | `auṭ → śī → -e` | `-ābhyām` | DAT key | ABL key | `-ayoḥ` | LOC key |
| M plural | `śas → -ān` | `bhis → ais → -aiḥ` | `bhyas → -ebhyaḥ` | same surface, ABL key | `ām+suṭ → -eṣām` | `su → -eṣu` |
| F plural | `śas → -āḥ` | `-ābhiḥ` | `-ābhyaḥ` | same surface, ABL key | `ām+suṭ → -āsām` | `-āsu` |
| N plural | `śas → śi+num → -āṇi/-āni` | `-aiḥ` | `-ebhyaḥ` | ABL key | `-eṣām` | `-eṣu` |

Masculine accusative-plural word-final `n` remains dental because 8.4.37 blocks retroflexion at word end even after `r`. Neuter accusative plural instead has internal `num`: `-tara` stems license `ṇ` under 8.4.1–2, while `-tama` stems retain dental `n`. Masculine/neuter genitive and locative plural obtain `ṣ` from their actual e-plus-ending environment; feminine long `ā` keeps dental `s`. These owners are not interchangeable.

## PG14 carrier and typed zero-specialization

Reuse PG14's full carrier

\[
B=C_\Sigma\langle z_e,z_e^*:e\in E\rangle,\qquad
M_\lambda=\bigoplus_{h\in\mathcal H}e_hB,\qquad
M_0=\bigoplus_{h\in\mathcal H}e_hC_\Sigma.
\]

Extend PG816's state to

\[
X=(q,C,m,|m|,P,a,s,g,n,r,u,k,o,h,w),
\]

retaining source question, comparison set, selected grouped member/cardinality, policy, affix, stem, gender/number, case role, original sup, ending/marker/nasal owner, source, ordered history and word. Each actual event satisfies

\[
T_{e,\lambda}(e_hb)=e_{h'}(1+z_e)b,
\qquad \pi_{0,M}T_{e,\lambda}=T_{e,0}\pi_{0,M}.
\]

Let `R` be the typed case-role transport and `E` the typed ending adapter. On admitted zero fibres,

\[
R_0(X)=X,\qquad E_0(X)=X,
\]

and

\[
\pi_{0,\mathrm{CaseFrame}}R_\lambda=R_0\pi_{0,\mathrm{DeterminationFrame}},\qquad
\pi_{0,\mathrm{Word}}E_\lambda=E_0\pi_{0,\mathrm{CaseFrame}}.
\]

Thus `π₀(Eλ Rλ(X)) = E₀ R₀(π₀X)`. Typed zero specialization does not identify INS/DAT/ABL `-ābhyām`, GEN/LOC `-ayoḥ`, DAT/ABL `-ebhyaḥ`, or the distinct nasal/sibilant histories. It preserves root-null nominal ownership, source policy, affix, grouped-member cardinality, case role, original ending and ordered history.

## Closure boundary

Accepted: all 216 literal case keys under PG816's number guard and both inherited source-labelled policies. Excluded only from these contracts: flat multiple-selection readings without positive evidence and case-role mergers based solely on equal surfaces. Open: vocative, accent, compounds/names/subordination, remaining derived-pronoun members, independent Bhāṣya/Kaiyaṭa/commentary reconciliation, external source collation, C2–C5 and S1–S7. No textual gap is converted into an exclusion. PG335's correction and PG340/346, PG349–352, PG355–360 and PG357–363 closures remain untouched. Claude retains Sanskrit generators, grammar execution, untouched suites and certificate replay.
