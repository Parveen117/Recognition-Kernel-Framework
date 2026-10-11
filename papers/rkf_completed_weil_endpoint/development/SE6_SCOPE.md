# SE6 written audit and verification scope

11 October 2026. Owner: Monty Dabas.

## Mathematical audit

| Result | Justification | Limit |
| --- | --- | --- |
| Paired prime/boundary operator | Odd autocorrelation Laplace identity and native translation norm | Signed integral; not termwise positivity |
| Matched cutoff | Complete prime tail plus exact pole integral tail | Absolute error still needs a reserve at zero |
| Aperture support | Correlations vanish beyond twice the radius | Includes every active prime power |
| Unpaired-truncation obstruction | Fixed bump pair, bounded finite prime response and exponentially growing boundary | Applies to the truncated model only |
| Moment mass bound | Taylor remainder, Cauchy--Schwarz and exact Fourier measure | Required moments cannot be omitted |
| Full small-aperture contraction | Positive Gamma lower sums, parity, no active prime shifts and exact boundary cost | Radius 1/16 in the admitted logarithmic chart |
| Prime-active complement | Thirty vanishing moments, fifteen automatic by parity, prime 2 retained | Only the kernel of the fifteen remaining moment readings |
| Native reserve transport | Full graph norm and all-prime mismatch upper bound | No L2/native identity substituted |
| Schur reduction | Explicit independent moment functionals and pivot >=8/1453 | F_15 still needs evaluation and sign |

The prime/pole signs, translation factor, boundary norm, factorial
exponents, Fourier-measure constants, native reserve directions and
Schur mixed blocks were checked in the written derivation.

## Exact arithmetic

The standard-library program
[endpoint_paired_aperture_budget.py](../../../proof_lab/endpoint_paired_aperture_budget.py)
replays 25 named rational comparisons, including two 128-term positive
Gamma lower sums and the aperture reserves. It includes controls against
discarding a Schur mixed block and against using the high-moment budget
with only the automatic zeroth odd moment.

The [recorded result](../../../proof_lab/ENDPOINT_PAIRED_APERTURE_RESULT.json)
separates these comparisons from analytic inputs and from the unevaluated
finite matrix. No floating-point eigenvalue, numerical quadrature,
sampled digamma value or full-aperture numerical PASS is used.

## Repository verification

Under Python 3.12.14, the 25 exact comparisons and recorded-result
read-back passed. All eight mathematics-navigation checks passed.
Thirteen parent-source pins and two arithmetic-artifact pins matched
their Git blob and SHA-256 digests. All 120 local links across the
changed notes and navigation surfaces resolved. Twenty equation tags
are unique; math delimiters, environments, whitespace, Python syntax
and git diff --check passed.

The 1,092 parent files outside the four navigation edits match the
published SE5 tree byte for byte. The operator engine remains unchanged.
Its required check, attempted on Node v24.19.0, failed the existing first
runtime-sensitive pin:
actual 35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e,
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6.
The report includes process.version, and the engine documents Node
22.16.0. This check is not PASS; no pins were changed to bypass it.

Commands: python proof_lab/endpoint_paired_aperture_budget.py --check;
python -m unittest proof_lab.test_mathematics_index -v; and
node operator_foundation/verify_all.cjs --check. These local runs do not
represent a complete scientific regression or a remote CI result.

## Completion boundary

The two displayed aperture restrictions have proved source floors and
contractive exact observers. The larger restriction is a moment-blind
complement, not the whole prime-active aperture.

The full sign there reduces to F_15 but is not yet certified. Larger
apertures, all their finite Schur blocks, the historical five-source
endpoint and the global RH sign remain open. General finite-codimension
existence is not a uniform limit theorem. No proof-assistant result,
external review or remote CI success is claimed.

See the [proof](SE6_PAIRED_APERTURE_AND_MOMENT_SCHUR.md) and
[source record](SE6_SOURCE_RECORD.md).
