# Certificate Index

## Campaign

| Field | Value |
|---|---|
| Campaign | Native foundation proof-transport campaign |
| Source commit | `c588ded973a395b5fce37c82f670616160979a2e` |
| Implemented packages | `2` |
| Status | `PASS_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN` |
| Canonical summary SHA-256 | `8728ab0319afe5fb6e6329deaee479cfa93f50bb4422ee863aaaf4f911dd9582` |
| RH status | `OPEN` |

Archived summary:

```text
certificates/foundation/campaign_result.json
```

## Package F00_F00E_EULER_V0_1

| Field | Value |
|---|---|
| Certificate class | Foundational computational audit |
| Scope | cut scalar and native Euler derivation |
| Status | `PASS_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT` |
| Package canonical result SHA-256 | `edc07e6bed39874251c0b75bb0e806a393a9b61343351fb40d70034fa66a2af5` |
| Archived result file SHA-256 | `c8db07cc20bb532ddf483bb56483ab43e3d717b765e7f9525fd8dafc2f380a41` |

Files:

```text
certificates/foundation/F00_F00E_EULER_V0_1/README.md
certificates/foundation/F00_F00E_EULER_V0_1/spec.json
certificates/foundation/F00_F00E_EULER_V0_1/verify.py
certificates/foundation/F00_F00E_EULER_V0_1/result.json
```

Authoritative mathematical and executable sources:

```text
src/rh_framework/native_summability.py
theorems/foundation/F00E_NATIVE_EULER_FROM_IOTA_COMPLEX.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Package F00GHI_LOG_ARITHMETIC_ZETA_V0_1

| Field | Value |
|---|---|
| Certificate class | exact and rational-interval foundational audit |
| Scope | native logarithm, arithmetic, prime factorization, and half-plane zeta |
| Status | `PASS_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT` |
| Package canonical result SHA-256 | `672865d994b1111a876b160a80858f78d3133f400351f0792715a8d8bee142bd` |
| Archived result file SHA-256 | `b5eff18191bc1834d57b8783a0f35c7214123d544d0ba6431d241e4227e150b6` |

Files:

```text
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/README.md
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/spec.json
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py
certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result.json
```

Authoritative theorem sources:

```text
theorems/foundation/F00G_NATIVE_LOGARITHM_AND_POWERS.md
theorems/foundation/F00H_NATIVE_NATURAL_ARITHMETIC_AND_PRIME_FACTORIZATION.md
theorems/foundation/F00I_NATIVE_DIRICHLET_ZETA_EULER_PRODUCT.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Theorem 45 directed arithmetic-analytic closure packet

| Field | Value |
|---|---|
| Certificate class | Exact finite arithmetic / enclosure algebra audit |
| Scope | finite-decimal exact rationalization, zero-radius exact embedding, outward threshold composition, refinement identity, certified-ball overlap |
| Status | `PASS_DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_CANDIDATE` |
| Canonical result SHA-256 | `294f5da69567086e869953ee0374fced3b4ea5f745138673b8025fb6d615ca5a` |
| Branch proof-lab CI | `PASS` |

Files:

```text
theorum/45_directed_arithmetic_analytic_closure_theorem.md
proof_lab/directed_arithmetic_analytic_closure.py
proof_lab/test_directed_arithmetic_analytic_closure.py
proof_lab/DIRECTED_ARITHMETIC_ANALYTIC_CLOSURE_EXPECTED.sha256
```

This packet is intentionally exact and finite. It proves the arithmetic/enclosure identities used by Theorem 45. Correctness of an arbitrary external interval/ball implementation remains a separate dependency and raw nearest-rounded floating point without an outward enclosure remains non-proof-bearing.

Theorem lineage:

```text
theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md
theorum/44_madhava_smriti_bilateral_jet_flow_closure_theorem.md
theorum/45_directed_arithmetic_analytic_closure_theorem.md
theorum/28_recognition_complete_finite_to_infinite_cut_theorem.md
certificates/foundation/NUMERICAL_PROOF_PROTOCOL.md
```

## Theorem 46 first-visible-jet seam quotient packet

| Field | Value |
|---|---|
| Certificate class | Exact finite-jet indeterminate-limit classification audit |
| Scope | raw division-by-zero rejection, first-visible-order classification, equal-order seam quotient, regular reparameterization invariance, denominator separation, exact quotient enclosure |
| Status | `PASS_FIRST_VISIBLE_JET_SEAM_QUOTIENT_CANDIDATE` |
| Canonical result SHA-256 | `9d4ad6ef6ff7a798d2e169b09dda170e166d13ec5b233801c9c8cf7e20a2d1ad` |
| Branch proof-lab CI | `PASS` on Python 3.11 and 3.12 |

Files:

```text
theorum/46_first_visible_jet_seam_quotient_theorem.md
proof_lab/first_visible_jet_seam_quotient.py
proof_lab/test_first_visible_jet_seam_quotient.py
proof_lab/FIRST_VISIBLE_JET_SEAM_QUOTIENT_EXPECTED.sha256
```

The packet verifies the exact finite algebra used by Theorem 46. It deliberately rejects raw algebraic `1/0` and `0/0`; it treats all-zero finite denominator jets as unresolved; and it verifies the explicit denominator-separation quotient radius with exact rational arithmetic. Flat-function or genuinely different-seam cases remain outside this finite-jet certificate.

Theorem lineage:

```text
theorum/42_cut_graded_lambda_jacobian_tower_theorem.md
theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md
theorum/44_madhava_smriti_bilateral_jet_flow_closure_theorem.md
theorum/45_directed_arithmetic_analytic_closure_theorem.md
theorum/46_first_visible_jet_seam_quotient_theorem.md
```

## Theorem 47 source-bound proof-carrying numerical validation packet

| Field | Value |
|---|---|
| Certificate class | Exact source-bound interval-DAG and theorem-tail validation audit |
| Scope | source-bound exact leaves, interval DAG enclosure, zero-denominator gate, forged-radius rejection, geometric tail, rational exponential upper bound, Theorem-43 tail adapter, certainty-aware strict boundary, implementation-manifest integrity |
| Status | `PASS_SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_CANDIDATE` |
| Canonical result SHA-256 | `318511a662326234894bd264a9c428902262560aa7df066d5b3982d17254bbd8` |
| Proof arithmetic | exact `fractions.Fraction`; no binary float needed in the proof packet |
| Branch proof-lab CI | `PASS` on Python 3.11 and 3.12 |

Files:

```text
theorum/47_source_bound_proof_carrying_numerical_validation_theorem.md
proof_lab/source_bound_numerical_validation.py
proof_lab/test_source_bound_numerical_validation.py
proof_lab/SOURCE_BOUND_PROOF_CARRYING_NUMERICAL_VALIDATION_EXPECTED.sha256
```

The packet proves the local-to-global enclosure induction for an admitted exact rational proof DAG. It rejects a node interval narrower than the verifier-computed enclosure, rejects interval division when the denominator enclosure contains zero, holds unsupported source classes or an open source-completeness obligation at `OPEN`, and computes theorem-tail examples by exact rational arithmetic. A participant-supplied radius or tail is therefore not proof-bearing merely because it is syntactically valid.

Theorem lineage:

```text
theorum/34_native_common_chart_decoder_transfer.md
theorum/38_native_compatibility_form_range_source_domination.md
theorum/39_native_source_kernel_no_blindness_strict_odd.md
theorum/43_bilateral_jet_flow_recognition_capstone_theorem.md
theorum/44_madhava_smriti_bilateral_jet_flow_closure_theorem.md
theorum/45_directed_arithmetic_analytic_closure_theorem.md
theorum/46_first_visible_jet_seam_quotient_theorem.md
theorum/47_source_bound_proof_carrying_numerical_validation_theorem.md
```

External backend authenticity, arbitrary real-world source truth, universal source completeness, and endpoint resource-exhaustion controls remain separate obligations.

## Planned but not certified

The following package names describe intended future audits. Their absence or design status must not be counted as a PASS:

```text
F06_08_OPERATOR_FOUNDATION_V0_1
F09_10_FOURIER_GAMMA_XI_V0_1
F11_EXPLICIT_WEIL_V0_1
F12_15_WEIL_OPERATOR_REDUCTION_V0_1
F16_ACTIVE_BAND_OUTWARD_V0_1
ENDPOINT_K0_OUTWARD_V0_1
```

## Verification rule

A package is considered reproducibly verified only when:

```text
its source pins match;
its verifier exits with code 0;
its result JSON reports a PASS status;
all mandatory obligations are present;
all negative controls behave as specified;
the result is reproducible from a clean checkout.
```

## Theorem 48 EMK algebra cut-graded curvature packet

| Field | Value |
|---|---|
| Certificate class | Exact rational 2×2 EMK instantiation of Theorem 42's cut-graded curvature |
| Scope | primitive relations, `J_E := K` involution, induced even/odd grading, representative curvature, general closed-form commutator, and three negative controls |
| Status | `PASS_EMK_ALGEBRA_CUT_GRADED_CURVATURE_CANDIDATE` |
| Canonical result SHA-256 | `8f5da0b72389d88380c9af6c26e2edf4c4f63554bf1fd5485b0ccdee95c58a0f` |
| Boundary | physical T–V–S–P identification and response two-form adapter remain open; no RH or Yang–Mills gate is affected |

```text
theorum/48_emk_algebra_cut_graded_curvature_theorem.md
proof_lab/README_EMK_ALGEBRA_CUT_GRADED_CURVATURE.md
proof_lab/emk_algebra_cut_graded_curvature.py
proof_lab/test_emk_algebra_cut_graded_curvature.py
proof_lab/EMK_ALGEBRA_CUT_GRADED_CURVATURE_EXPECTED.sha256
```

## Theorem 49 local-to-uniform seam gap packet

| Field | Value |
|---|---|
| Certificate class | Exact product-carrier seam-gap certificate |
| Scope | global recognition cut vs tensor cut, (H1) seam compatibility = evenness, (H2) exact cut-square contraction, uniform-in-m memory contraction on the full product (m=1..5, dims up to 72), sheet law with attainment, theorum/28 §9 outward certificate delivered m-uniformly, memory-only coupling, three controls |
| Status | `PASS_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE` |
| Canonical result SHA-256 | `d75992cd8fea4ed9b4b1d10a0dd5defe22651ba749b1c3b888be1ebd91a4ccb8` |
| Proof arithmetic | exact `fractions.Fraction`; no float, no NumPy, no exponential evaluated |
| Branch proof-lab CI | `PASS` — GitHub Actions run `32630967128` at tip `51afbcd75b79e806c67f1ce96a6e2aed06825b17` |

Files:

```text
theorum/49_local_to_uniform_seam_gap_theorem.md
proof_lab/local_to_uniform_seam_gap.py
proof_lab/test_local_to_uniform_seam_gap.py
proof_lab/LOCAL_TO_UNIFORM_SEAM_GAP_EXPECTED.sha256
```

Infinite-face limit (theorum/28 §11 hypotheses 1–5) and m-uniformity of an interacting coupling norm remain separate obligations.

## Theorem 56 canvas operators nativized packet (originally filed as 50)

| Field | Value |
|---|---|
| Certificate class | Exact reduction of owner operator canvases to the cut algebra |
| Scope | Bindu–Lopa chart-dependent commutator + seam-alphabet termination; Pāṇinian rewrite (lopa, precedence, non-confluence, anubandha blindness); Operator-Universe tower = theorum/41 grading; Aghora refusal (G=0) + odd-signed repair; OM factorization + m-torus gap (Theorem 49); projector sectors |
| Status | `PASS_CANVAS_OPERATORS_NATIVIZED_CANDIDATE` |
| Canonical result SHA-256 | `df4c77161f37e874b4fd22d0a8af3d3e1e65a263d4e9afbd4dea14f9bdf9ea68` |
| Proof arithmetic | exact `fractions.Fraction`; no float, no root of unity, no exponential evaluated |

Files: `theorum/56_canvas_operators_nativized_theorem.md`, `proof_lab/canvas_operators_nativized.py`, `proof_lab/test_canvas_operators_nativized.py`, `proof_lab/CANVAS_OPERATORS_NATIVIZED_EXPECTED.sha256`.

## Theorem 50 native seam gap / odd-sector covariance packet

| Field | Value |
|---|---|
| Certificate class | Primitive-carrier (C_Σ) product seam-gap and cut-square odd-channel certificate |
| Scope | T01 laws re-verified on carrier; flow-generated faces; exactly multiplicative sheet mass ≤ ρ^k f0^m and energy contraction ρ² f0^(2m) uniform in m (m=1..4, dim 108); odd-sector covariance law A1–A6; three controls; source-level no-Hilbert guard |
| Status | `PASS_NATIVE_SEAM_GAP_ODD_COVARIANCE_CANDIDATE` |
| Canonical result SHA-256 | `d46a26c91eabd8733a25161564bca1b6dc66bc1b3f9f02ab7fd992dc78ea8826` |
| Proof arithmetic | exact `fractions.Fraction` pairs (rad, turn); no float, no NumPy, no inner product, no PSD |

Files:

```text
theorum/50_native_seam_gap_odd_sector_covariance_theorem.md
proof_lab/native_seam_gap_odd_covariance.py
proof_lab/test_native_seam_gap_odd_covariance.py
proof_lab/NATIVE_SEAM_GAP_ODD_COVARIANCE_EXPECTED.sha256
```

Theorem 49 is retained as a derived-layer (Hilbert) cross-check and superseded by this packet. Dynamical law of the odd channel under the flow and the infinite-face limit remain open.

## Theorem 51 odd-channel exchange law packet

| Field | Value |
|---|---|
| Certificate class | Primitive-carrier flow-transport certificate for the cut square |
| Scope | anti-self-dagger Cayley step native-unitary (exact C_Σ inverse); exchange law D†S+SD = ([R,B]+[A,T]) + ι([T,B]+[R,A]); first-order residual identity; creation/no-creation; energy invariant with channel exchange; product Leibniz transport; step non-factorization; controls |
| Status | `PASS_ODD_CHANNEL_EXCHANGE_LAW_CANDIDATE` |
| Canonical result SHA-256 | `80be9fb9020268066f58908e9f497c0e845eadfbf940f29c3e7414ae0750e7f3` |
| Proof arithmetic | exact `fractions.Fraction` pairs (rad, turn); no float, no inner product |

Files:

```text
theorum/51_odd_channel_exchange_law_theorem.md
proof_lab/odd_channel_exchange_law.py
proof_lab/test_odd_channel_exchange_law.py
proof_lab/ODD_CHANNEL_EXCHANGE_LAW_EXPECTED.sha256
```

## Theorem 52 native seam resolvent packet

| Field | Value |
|---|---|
| Certificate class | Primitive-carrier resolvent / spectral-region certificate |
| Scope | mass-Neumann resolvent with declared geometric Smriti tails (N=0..6, planted control); det factorization and native gap region G_ρ with f0 outside; exact triangular locus; power-sharpened region; product locus uniform in m, resolvent non-local |
| Status | `PASS_NATIVE_SEAM_RESOLVENT_CANDIDATE` |
| Canonical result SHA-256 | `c813f2a4797ebdf426ebe84309d87fe6ad177e23e85828c2050fda23d9242afe` |
| Proof arithmetic | exact K_Σ (Fraction pairs); no float, no inner product, no eigenvalue approximation |

Files:

```text
theorum/52_native_seam_resolvent_theorem.md
proof_lab/native_seam_resolvent.py
proof_lab/test_native_seam_resolvent.py
proof_lab/NATIVE_SEAM_RESOLVENT_EXPECTED.sha256
```

## Theorem 53 native cut-square factorization packet

| Field | Value |
|---|---|
| Certificate class | Primitive-carrier factorization certificate for cut squares |
| Scope | exact C†Dg C over K_Σ, turn-free nonnegative weights, odd channel in factor phases; native Parseval; negative witness; seam-face weight bounds; product tensoring; det S flow-invariant |
| Status | `PASS_NATIVE_CUT_SQUARE_FACTORIZATION_CANDIDATE` |
| Canonical result SHA-256 | `2079f98d0aa2565ec99c8b33ee3fd21c024a919aad65d5e2e2b8193f20ddc725` |
| Proof arithmetic | exact K_Σ; no sqrt, no float, no inner product, no eigenvalue |

Files:

```text
theorum/53_native_cut_square_factorization_theorem.md
proof_lab/native_cut_square_factorization.py
proof_lab/test_native_cut_square_factorization.py
proof_lab/NATIVE_CUT_SQUARE_FACTORIZATION_EXPECTED.sha256
```

## Theorem 54 infinite-face recognition completion packet

| Field | Value |
|---|---|
| Certificate class | theorum/28 §11 hypothesis delivery on the product carrier |
| Scope | word-mass/kron consistency; sheet stationarity; exact memory increments and declared geometric Smriti tail; floor 1 and outward margin from n₀; separation sup μ<1 vs Σμ<∞ with divergent control; §11 ledger (hyp. 4 not built) |
| Status | `PASS_INFINITE_FACE_RECOGNITION_COMPLETION_CANDIDATE` |
| Canonical result SHA-256 | `f3354b0a69fb7003aa4e7431de3d173d29310fab6a9fde0cc8e7f2289fb93057` |
| Proof arithmetic | exact Fraction; no float, no exponential |

Files:

```text
theorum/54_infinite_face_recognition_completion_theorem.md
proof_lab/infinite_face_recognition_completion.py
proof_lab/test_infinite_face_recognition_completion.py
proof_lab/INFINITE_FACE_RECOGNITION_COMPLETION_EXPECTED.sha256
```

## Theorem 55 Generalized Euler / EMK dock packet

| Field | Value |
|---|---|
| Certificate class | Dock certificate binding theorum/51, 53 to EMK/GE transport |
| Scope | EMK flow generators and two gradings; GE connection obeys the exchange law; [R,K]=2RK as leading loop residue (dyadic window); Δ∥+Δ⊥ invariant with channel exchange; GE false-residue verdict |
| Status | `PASS_GENERALIZED_EULER_EMK_DOCK_CANDIDATE` |
| Canonical result SHA-256 | `bcddc7a3a622deae64a469489e39eeaf9ed72f093d3f2e71beb1323a045d4a7c` |
| Proof arithmetic | exact K_Σ; rational rotations, no trigonometry, no float |

Files:

```text
theorum/55_generalized_euler_emk_dock_theorem.md
proof_lab/generalized_euler_emk_dock.py
proof_lab/test_generalized_euler_emk_dock.py
proof_lab/GENERALIZED_EULER_EMK_DOCK_EXPECTED.sha256
```

## Theorem 57 Loop-residue / first-visible-jet binding packet

| Field | Value |
|---|---|
| Certificate class | Binding certificate: theorum/55's Γ_μ loop residue resolved by theorum/46's seam quotient |
| Scope | Γ = loop − I as a 46 seam observable on the step seam h; Γ ⊙_S h² = [D₁,D₂] = 2ιαβRK through 46's classifier; exact order-3 identity a₃ = ½[D₁+D₂,[D₁,D₂]]; reparameterization invariance; false residue = visible before order 2 |
| Status | `PASS_LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_CANDIDATE` |
| Canonical result SHA-256 | `712c272d3e1a1d1dadc869045130226f42da11f1ca20b6c98584305234e502a6` |
| Proof arithmetic | exact C_Σ jets in C_Σ[h]/h⁵ (terminating geometric inverse); no float |

Files:

```text
theorum/57_loop_residue_first_visible_jet_binding_theorem.md
proof_lab/loop_residue_first_visible_jet_binding.py
proof_lab/test_loop_residue_first_visible_jet_binding.py
proof_lab/LOOP_RESIDUE_FIRST_VISIBLE_JET_BINDING_EXPECTED.sha256
```

## Theorem 58 Pāṇinian seam calculus packet

| Field | Value |
|---|---|
| Certificate class | Canonical-sūtra upgrade of theorum/56 B2 on a recognized/memory two-channel carrier |
| Scope | vowel-strength semilattice (1.1.1/1.1.2/1.1.3); priority 1.4.2 = commutator support (computed, free ambiguity set = union of supports); gacchati / nayati derivations with 1.1.62 memory channel load-bearing; R–A–S determinacy disproved free / proved under priority |
| Status | `PASS_PANINIAN_SEAM_CALCULUS_CANDIDATE` |
| Canonical result SHA-256 | `7966cc7271302338487eb41b88a6f3e2da61e35c7d9ed72afc350cfb3c0387ad` |
| Proof arithmetic | exact finite combinatorics; no float; no hard-coded verdicts |

Files:

```text
theorum/58_paninian_seam_calculus_theorem.md
proof_lab/paninian_seam_calculus.py
proof_lab/test_paninian_seam_calculus.py
proof_lab/PANINIAN_SEAM_CALCULUS_EXPECTED.sha256
```

## Theorem 59 Prime letter operators packet

| Field | Value |
|---|---|
| Certificate class | Prime Operator canvas relocated to the primitive carrier (odd sector), binding F00H/F00E/T55/T57 and the Vedic Letter–Root seed algebra |
| Scope | canvas A4 corrected (a_p a_q† = a_{p/q}, a_pq† disproved); irreducible ⟺ ledger mass 1; generator support = Λ support; letter generator ιxI is ODD; zero loop residue; Exp phase accumulation exact in jets; Cayley chart residue ⊙ t³ = ιxy(x+y)/4; letter unitary invisible to every cut square |
| Status | `PASS_PRIME_LETTER_OPERATORS_CANDIDATE` |
| Canonical result SHA-256 | `e583a360ab78b9907165fc5363c095d777241dde18b1a57a772407eabe3b70a3` |
| Proof arithmetic | exact integer ledgers (F00H verify.py pinned by SHA in certificate) + exact C_Σ jets; no float |

Files:

```text
theorum/59_prime_letter_operators_theorem.md
proof_lab/prime_letter_operators.py
proof_lab/test_prime_letter_operators.py
proof_lab/PRIME_LETTER_OPERATORS_EXPECTED.sha256
```

## Theorem 60 Seam-compensated confluence verdict packet

| Field | Value |
|---|---|
| Certificate class | Decidable confluence-mod-ledger verdict on finite reachable carriers (Vedic confluence note, no Newman import) |
| Scope | critical-pair classification PRIORITY_RESOLVED / LEDGER_ABSORBED / OPEN; word carrier: memory ⇒ zero critical pairs, erased ⇒ OPEN (1.3.9, 7.3.77); sandhi carrier under/without 1.4.2; containment ≠ equality; termination checked |
| Status | `PASS_SEAM_COMPENSATED_CONFLUENCE_VERDICT_CANDIDATE` |
| Canonical result SHA-256 | `c3fb318c965a07820c4b58981c415b69a28e5c0c03f20c8f5f6200d42d2bd14c` |
| Proof arithmetic | exact finite enumeration; no float |

Files:

```text
theorum/60_seam_compensated_confluence_verdict_theorem.md
proof_lab/seam_compensated_confluence_verdict.py
proof_lab/test_seam_compensated_confluence_verdict.py
proof_lab/SEAM_COMPENSATED_CONFLUENCE_VERDICT_EXPECTED.sha256
```

## Theorem 61 Rewrite rules as cut-module operators packet

| Field | Value |
|---|---|
| Certificate class | 0/1 realization of rewrite rules on the C_Σ free module; theorum/60 residue = matrix commutator; 57 binding |
| Scope | faithful realization; commutator support = order-dependence set, M_Σ = 2·count; conflict/enabling split (memory ⇒ no conflicts); Γ ⊙ h² = [D_lopa, D_chaḥ]; priority NF operator is a projector onto normal forms |
| Status | `PASS_REWRITE_RULES_AS_CUT_MODULE_OPERATORS_CANDIDATE` |
| Canonical result SHA-256 | `9a94b881415c5db9a9b1f47980bff829550d198bbd670336bcf353941280241f` |
| Proof arithmetic | exact sparse C_Σ matrices (cross-checked against dense star); no float |

```text
theorum/61_rewrite_rules_as_cut_module_operators_theorem.md
proof_lab/rewrite_rules_as_cut_module_operators.py
proof_lab/test_rewrite_rules_as_cut_module_operators.py
proof_lab/REWRITE_RULES_AS_CUT_MODULE_OPERATORS_EXPECTED.sha256
```

## Theorem 62 Silence–vibration / sūtra-flow / awareness-category packet

| Field | Value |
|---|---|
| Certificate class | Second canvas batch nativized: two canvas laws disproved, circular-system identity proved, terminal-object ⟺ confluence |
| Status | `PASS_SILENCE_VIBRATION_SUTRA_FLOW_CANDIDATE` |
| Canonical result SHA-256 | `44f88cfa73330bfe0d377d94522f806cbde47bd5b38ac47689cb16add7064426` |

```text
theorum/62_silence_vibration_sutra_flow_theorem.md
proof_lab/silence_vibration_sutra_flow.py
proof_lab/test_silence_vibration_sutra_flow.py
proof_lab/SILENCE_VIBRATION_SUTRA_FLOW_EXPECTED.sha256
```

## Theorem 63 Sup-vibhakti / resolver ladder packet

| Field | Value |
|---|---|
| Certificate class | Nominal sector (rāma paradigm, 21 forms) from canonical sūtras with soundness oracle; resolver ladder 8.2.1 > apavāda > nitya > para executable |
| Status | `PASS_SUP_VIBHAKTI_RESOLVER_LADDER_CANDIDATE` |
| Canonical result SHA-256 | `49671feae1f92cd65fac0fe37fb109f128f4dc38e5cfb3dd69e13a3bdabc6d31` |

```text
theorum/63_sup_vibhakti_resolver_ladder_theorem.md
proof_lab/sup_vibhakti_resolver_ladder.py
proof_lab/test_sup_vibhakti_resolver_ladder.py
proof_lab/SUP_VIBHAKTI_RESOLVER_LADDER_EXPECTED.sha256
```

## Theorem 64 Tiṅ laṭ parasmaipada packet

| Field | Value |
|---|---|
| Certificate class | Verbal sector: laṭ parasmaipada of bhū and gam (18 forms) from canonical sūtras; real earlier-apavāda 6.1.97 ⊊ 6.1.101; grammar-wide apavāda domains |
| Status | `PASS_TING_LAT_PARASMAIPADA_CANDIDATE` |
| Canonical result SHA-256 | `073705dabbd629242140637068f55ef4f7cfb256674f09a9e7251ba6b071feb9` |

```text
theorum/64_ting_lat_parasmaipada_theorem.md
proof_lab/ting_lat_parasmaipada.py
proof_lab/test_ting_lat_parasmaipada.py
proof_lab/TING_LAT_PARASMAIPADA_EXPECTED.sha256
```

## Theorem 65 Stem classes / Gāyatrī coverage packet

| Field | Value |
|---|---|
| Certificate class | ṛ-stem, s-stem, neuter sarvanāma sectors from canonical sūtras; Gāyatrī line 1 pada coverage 5/6 (dhīmahi refused) |
| Status | `PASS_STEM_CLASSES_GAYATRI_COVERAGE_CANDIDATE` |
| Canonical result SHA-256 | `6f6f988e2a6b6b19ef5c5d57654f1021093ace5d5964f763594e4cea9fff6414` |

```text
theorum/65_stem_classes_gayatri_coverage_theorem.md
proof_lab/stem_classes_gayatri_coverage.py
proof_lab/test_stem_classes_gayatri_coverage.py
proof_lab/STEM_CLASSES_GAYATRI_COVERAGE_EXPECTED.sha256
```

## Theorem 66 laṭ ātmanepada packet

| Field | Value |
|---|---|
| Certificate class | Ātmanepada sector (edh, labh, 18 forms) from canonical sūtras; declared-bādhaka rung finding; antaraṅga gap recorded; dhīmahi refused with reason |
| Status | `PASS_LAT_ATMANEPADA_CANDIDATE` |
| Canonical result SHA-256 | `2ab0cf226c593e1533f38b4c466db17fa8246d913d9826f42c81a465a4e9aa23` |

```text
theorum/66_lat_atmanepada_theorem.md
proof_lab/lat_atmanepada.py
proof_lab/test_lat_atmanepada.py
proof_lab/LAT_ATMANEPADA_EXPECTED.sha256
```

## Theorem 67 Pada → line external sandhi packet

| Field | Value |
|---|---|
| Certificate class | Gāyatrī lines from padas by external sandhi (8.2.66, 6.1.113/114, 6.1.87, 8.3.15, 8.3.23); provenance 5 derived / 5 given; confluence per line |
| Status | `PASS_PADA_TO_LINE_EXTERNAL_SANDHI_CANDIDATE` |
| Canonical result SHA-256 | `75d6abbbabf1498ef49d23067398a47c3ff3a5a64104b6184988137693b923a9` |

```text
theorum/67_pada_to_line_external_sandhi_theorem.md
proof_lab/pada_to_line_external_sandhi.py
proof_lab/test_pada_to_line_external_sandhi.py
proof_lab/PADA_TO_LINE_EXTERNAL_SANDHI_EXPECTED.sha256
```

## Theorem 68 Kāraka → vibhakti carrier packet

| Field | Value |
|---|---|
| Certificate class | 1.4 kāraka saṃjñā + 2.3 vibhakti-artha under the abhihita ledger (3.4.69 / 2.3.1); Gāyatrī vibhaktis reproduced; voice-switch and 2.3.1 controls |
| Status | `PASS_KARAKA_VIBHAKTI_CARRIER_CANDIDATE` |
| Canonical result SHA-256 | `d6f1a3fabb69b71c4888290a9b6f62c720522498fd7657795e6976e00d573fd3` |

```text
theorum/68_karaka_vibhakti_carrier_theorem.md
proof_lab/karaka_vibhakti_carrier.py
proof_lab/test_karaka_vibhakti_carrier.py
proof_lab/KARAKA_VIBHAKTI_CARRIER_EXPECTED.sha256
```

## Theorem 69 Mīmāṃsā obligation closure packet

| Field | Value |
|---|---|
| Certificate class | Owner's Mīmāṃsā kernel executable: vidhi/niṣedha closure K_M on a situation carrier; resolver scope > authority > vikalpa; Gāyatrī classified as mantra by its lakāra |
| Status | `PASS_MIMAMSA_OBLIGATION_CLOSURE_CANDIDATE` |
| Canonical result SHA-256 | `294e7e927c1f3b2989ff8f23e801fa98341bd0986b584caa471a084b8f87a127` |

```text
theorum/69_mimamsa_obligation_closure_theorem.md
proof_lab/mimamsa_obligation_closure.py
proof_lab/test_mimamsa_obligation_closure.py
proof_lab/MIMAMSA_OBLIGATION_CLOSURE_EXPECTED.sha256
```

## Theorem 70 Aṅgatva pramāṇa ladder packet

| Field | Value |
|---|---|
| Certificate class | MS 3.3.14 six pramāṇas as a delay-ordered resolver; Bhāṣya instances; monotonicity; Gāyatrī aṅgatva derived from evidence |
| Status | `PASS_ANGATVA_PRAMANA_LADDER_CANDIDATE` |
| Canonical result SHA-256 | `8a31fe5abc6966d64ebd2463882ddcf96ec6a3f0012cd37cc850ef4e77651dbe` |

```text
theorum/70_angatva_pramana_ladder_theorem.md
proof_lab/angatva_pramana_ladder.py
proof_lab/test_angatva_pramana_ladder.py
proof_lab/ANGATVA_PRAMANA_LADDER_EXPECTED.sha256
```

## Theorem 71 Piṅgala chandas pratyaya packet

| Field | Value |
|---|---|
| Certificate class | Piṅgala's six pratyayas exact; meru closure (Rec-anchored S_M); mātrā-meru Virahāṅka; Gāyatrī metre from the theorum/67 text (7-8-8 written, 8-8-8 restored) |
| Status | `PASS_PINGALA_CHANDAS_PRATYAYA_CANDIDATE` |
| Canonical result SHA-256 | `316a794e34981420da9e1151440e5e66ec31323a764a81862be10ce9cd718568` |

```text
theorum/71_pingala_chandas_pratyaya_theorem.md
proof_lab/pingala_chandas_pratyaya.py
proof_lab/test_pingala_chandas_pratyaya.py
proof_lab/PINGALA_CHANDAS_PRATYAYA_EXPECTED.sha256
```

## Theorem 72 Śulba measure residue packet

| Field | Value |
|---|---|
| Certificate class | Baudhāyana constructions on an exact rational carrier; flat vs memory-closed per the owner's note; √2 cord Smṛti 1/166464; circle round-trip Smṛti |
| Status | `PASS_SULBA_MEASURE_RESIDUE_CANDIDATE` |
| Canonical result SHA-256 | `8f9db340d011dbc0f035570f9c7a33ef51a02aa367f77bf84f0fbb2ef0d0da37` |

```text
theorum/72_sulba_measure_residue_theorem.md
proof_lab/sulba_measure_residue.py
proof_lab/test_sulba_measure_residue.py
proof_lab/SULBA_MEASURE_RESIDUE_EXPECTED.sha256
```

## Theorem 73 Vedāṅga Jyotiṣa yuga ledger packet

| Field | Value |
|---|---|
| Certificate class | VJ 5-year yuga as exact cyclic ledger: intercalation Smṛti = −5-year residue exactly; tithi/kṣaya; phases zero at 1830 only; daylight zigzag; calendar as prastāra word |
| Status | `PASS_VEDANGA_JYOTISA_YUGA_LEDGER_CANDIDATE` |
| Canonical result SHA-256 | `569b61ea6a8ab4852bd422faf68228c55ff5fed817f21e670a972e630b964295` |

```text
theorum/73_vedanga_jyotisa_yuga_ledger_theorem.md
proof_lab/vedanga_jyotisa_yuga_ledger.py
proof_lab/test_vedanga_jyotisa_yuga_ledger.py
proof_lab/VEDANGA_JYOTISA_YUGA_LEDGER_EXPECTED.sha256
```

## Lean kernel witnesses (second lineage)

| Witness | Statement | Kernel |
|---|---|---|
| LEAN-RKF-1 | theorum/61 commutator support + no conflicts on the gam word carrier (16 states) | `decide`, no axioms |
| LEAN-RKF-3 | theorum/60 confluence verdict on the gam carrier (1 NF with memory, 4 without) | `decide`, no axioms |
| LEAN-RKF-4 | theorum/62 circular system 24·Exp-jet₄(tωR) = Cos₂₄·I + Sin₂₄·R, all integers ω, t | accepted (propext) |
| LEAN-RKF-5 | theorum/71 Piṅgala pratyayas (naṣṭa/uddiṣṭa inverse n≤8, meru, Virahāṅka) + theorum/73 yuga closure (intercalation identity, least closure 1830) | `decide`, no axioms |
| LEAN-RKF-2 | theorum/51 exchange law D†S + SD = ([R,B]+[A,T]) + ι([T,B]+[R,A]), all integer entries, 2×2 | accepted (propext, Quot.sound) |

```text
lean/CommutatorSupport.lean
lean/ExchangeLaw.lean
lean/ConfluenceVerdict.lean
lean/CircularSystem.lean
lean/ChandasJyotisa.lean
lean/README.md
proof_lab/test_lean_tables.py
```

## Ladder audit 50–59

| Field | Value |
|---|---|
| Class | Adversarial audit capsule (re-derivations, planted negatives, scope probes, renaming tests) |
| Status | `PASS_LADDER_AUDIT_50_59` — 4 cert defects fixed (52, 54, 56, 58; re-pinned), 3 headline downgrades (57, 58, 59), 2 scope notes (50, 52) |

```text
theorum/AUDIT_LADDER_50_59.md
proof_lab/ladder_audit_50_59.py
proof_lab/LADDER_AUDIT_50_59_REPORT.json
proof_lab/test_ladder_audit_50_59.py
```

## Theorem 74 Lopa-ledger contraction packet

| Field | Value |
|---|---|
| Certificate class | Exact finite one-column, two-rail silence/lopa contraction witness |
| Scope | silence factorization, strict lopa ladder, 1.1.62 ledger decomposition, exact orthogonality, outward `beta_sil < 1`, declared-grid uniformity, and one-sided vibration law |
| Status | `PROVED` for the declared finite instance; candidate names retained pending owner audit |
| Archived result file SHA-256 | `37add42918b9bdc4f9775bc084978511719e79dee3c01fc89f5e6ec1ee6d4c6e` |
| Boundary | infinite-content transfer is delegated to Theorem 75; chain-gap operator upper bound `E4D-C` remains open |

```text
theorum/74_lopa_ledger_contraction_theorem.md
proof_lab/lopa_ledger_contraction.py
proof_lab/test_lopa_ledger_contraction.py
proof_lab/LOPA_LEDGER_CONTRACTION_RESULT.json
```

## Theorem 75 selective-release content-tail packet

| Field | Value |
|---|---|
| Certificate class | Native-carrier content-tail release and outward full-column certificate |
| Scope | all-content ladder inequality, exact low-block stationarity, integer seam-count retention at the instantiated release levels, contraction transfer, and `u + e < 1` on the declared grid |
| Status | `PROVED` on the declared carrier; levels above 2 enter through the stated geometric tail and recorded Gram-uniformity declaration |
| Archived result file SHA-256 | `c018bc25beba74937d1645808d2979601cbe431f38af708343694de3b9a56065` |
| Audit note | the classical-Laplacian dependency was removed by native character-ladder regrading; the Laplacian remains only an independent cross-check |
| Boundary | chain-gap operator upper bound `E4D-C` remains open |

```text
theorum/75_selective_release_content_tail_theorem.md
theorum/AUDIT_74_75.md
proof_lab/selective_release.py
proof_lab/test_selective_release.py
proof_lab/SELECTIVE_RELEASE_RESULT.json
```

## Theorem 76 seam-flow meter packet

| Field | Value |
|---|---|
| Certificate class | Exact rational native-sector and determinant-channel crossing witness |
| Scope | integer sectors, 14 simple flips bracketed to width `2^-40`, count/determinant parity agreement, exact ladder identity, and stability for 24 declared rational perturbations |
| Status | `PROVED` for the declared finite instance and perturbation family |
| Archived result file SHA-256 | `3e49afb85da0b9d908bc80a3dbd042cfe7e214f1915bc4032bf1d34232402070` |
| Boundary | no universal protection radius; no claimed identification with the YM-23 weak-coupling threshold; cited spectral-flow law is not rederived |

```text
theorum/76_seam_flow_meter_theorem.md
proof_lab/seam_flow_meter.py
proof_lab/test_seam_flow_meter.py
proof_lab/SEAM_FLOW_METER_RESULT.json
```

## Theorem 77 typed semantic Paninian normal-form packet

| Field | Value |
|---|---|
| Certificate class | Deterministic finite typed semantic-normalization witness |
| Scope | source-pinned ordered alias rewrite, type/precedence guard, explicit Bindu selection, ledger-before-Lopa, identity/entailment separation, typed polarity/time contradictions, and fail-closed ambiguity |
| Status | `PASS_TYPED_SEMANTIC_PANINIAN_NORMAL_FORM_STAGE1` / `PROVED_FOR_EXPLICIT_FINITE_PRESENTATION` |
| Canonical generated payload SHA-256 | `b1962e95e4a3284e51f0b1ded453fb829d63c78787e76a93526ff4cba37b487f` |
| Numbering note | branch-local Theorem 45 was renamed to canonical Theorem 77 during consolidation; theorem content is unchanged |
| Boundary | unrestricted natural-language parsing, Nyāya support/defeat, Mīmāṃsā context/priority, Yukti transport, full observer injectivity, and truth certification remain open |

```text
theorum/77_semantic_paninian_typed_claim_normal_form.md
proof_lab/README_SEMANTIC_PANINIAN_NORMAL_FORM.md
proof_lab/semantic_paninian_types.py
proof_lab/semantic_paninian_normalizer.py
proof_lab/semantic_paninian_normal_form.py
proof_lab/test_semantic_paninian_normal_form.py
proof_lab/imported/SEMANTIC_PANINIAN_SOURCE_PINS.json
proof_lab/SEMANTIC_PANINIAN_NORMAL_FORM_EXPECTED.sha256
```


## Theorem 78 Śaiva sources nativized packet

| Field | Value |
|---|---|
| Certificate class | Quoted primary Śaiva/Pāṇinian sources turned into exact finite theorems: Māheśvara-sūtra interval code (1.1.71), necessity of the repeated *ha*, Spanda turn group on the EMK odd generator, Pratyabhijñā recognition defect on the MR-03 cocycle lift |
| Status | `PASS_SHAIVA_SOURCES_NATIVIZED_CANDIDATE` |
| Canonical result SHA-256 | `3d1ce14b679eb5c02e33473fb808ec4a192502b79d912b927a52240c94c58950` |
| Boundary | marker-count minimality of the fourteen sūtras not re-derived; breath, deity, ontology and the five acts cited only; recognition across different decompositions without a memory gauge is an open obligation |

```text
theorum/78_shaiva_sources_maheshvara_spanda_pratyabhijna_theorem.md
proof_lab/shaiva_sources_nativized.py
proof_lab/test_shaiva_sources_nativized.py
proof_lab/SHAIVA_SOURCES_NATIVIZED_EXPECTED.sha256
```


## Theorem 79 Śaiva sources II: varga grid and crystal theorem packet

| Field | Value |
|---|---|
| Certificate class | Varga/manner 5×5 grid of the Māheśvara code (udit columns never intervals, manner rows pratyāhāras), exact count 2304 of set-preserving within-sūtra orders with forced leaders, and the crystal theorem (recognition-blind ⟺ symmetric ⟺ coboundary) on the MR-03 memory lift |
| Status | `PASS_SHAIVA_SOURCES_VARGA_CRYSTAL_CANDIDATE` |
| Canonical result SHA-256 | `4440bf2f0e4f941ba8c7a1e83d7ed63a558c756efddd360a69fe5ef3ce3b37ca` |
| Boundary | presiding mothers of the vargas and the breath reading of Vijñāna-bhairava 26 cited only; the Aghora ladder (TA 10.45) and śiva/śivatara (TS 4.5.8) refused |

```text
theorum/79_shaiva_sources_varga_grid_crystal_theorem.md
proof_lab/shaiva_sources_varga_crystal.py
proof_lab/test_shaiva_sources_varga_crystal.py
proof_lab/SHAIVA_SOURCES_VARGA_CRYSTAL_EXPECTED.sha256
```


## Theorem 80 Pāṇinian instruction-format packet

| Field | Value |
|---|---|
| Certificate class | Case-structured sūtra records compiled by the quoted paribhāṣās (1.1.49, 1.1.66–67, 6.1.84, 1.1.69–70, 1.1.52/55, 1.1.46, 1.3.10, 1.1.50–51, 1.4.2) and certified against theorum/58's hand-coded rules: equal wherever 58 fires, 24 extra long-ī/ū junctions by 1.1.69; antaratama reproduces every table; compiled sandhi confluent under 1.4.2; word rules equal 58 on all 40 reachable states |
| Status | `PASS_PANINIAN_INSTRUCTION_FORMAT_CANDIDATE` |
| Canonical result SHA-256 | `8ac53de2a233fbe94d7d6f3f9e3806ade7bd2f68c759faba81882119ae87bccb` |
| Boundary | not a general Aṣṭādhyāyī interpreter: only the listed paribhāṣās and the rules realized in theorum/58; adhikāra spans declared, not parsed; ṝ ḹ and pluta outside the declared carrier |

```text
theorum/80_paninian_instruction_format_theorem.md
proof_lab/paninian_instruction_format.py
proof_lab/test_paninian_instruction_format.py
proof_lab/PANINIAN_INSTRUCTION_FORMAT_EXPECTED.sha256
```

## Theorem 81 Pāṇinian saṁjñā sound-layer packet and the Aṣṭādhyāyī ledger

| Field | Value |
|---|---|
| Certificate class | Saṁjñā sūtras of pāda 1.1 realized on the sound carrier: savarṇa derived from the sthāna/prayatna table by 1.1.9 with 1.1.10 (exactly the vowel length pairs and the five vargas; 1.1.10 load-bearing), ṭi / upadhā / tadanta selectors (1.1.64, 1.1.65, 1.1.72), saṁyoga 1.1.7, anunāsika 1.1.8, pragṛhya 1.1.11 with 6.1.125 blocking every compiled sandhi rule of theorum/80 on dual ī/ū/e junctions and nothing else |
| Status | `PASS_PANINIAN_SAMJNA_SOUND_LAYER_CANDIDATE` |
| Canonical result SHA-256 | `98c8a45c5eee2a022a5a7fe72286d44d5a5cb4eac7b22522e1fca6e30c961c48` |
| Ledger | `proof_lab/astadhyayi/ASTADHYAYI_LEDGER.json` is the single claim boundary of the all-sūtra programme: 156 of 3959 sūtras listed (10 compiled, 34 meta, 72 hand-coded, 38 cited, 2 misnumbered citations in theorum/58); `proof_lab/test_astadhyayi_ledger.py` checks the committed ledger equals its rebuild |
| Boundary | e/ai, o/au separated by the recorded proportion attribute, not by the table; pluta, anusvāra, nasalized vowels not on the carrier; the dvivacana flag is supplied, not derived from morphology |

```text
theorum/81_paninian_samjna_sound_layer_theorem.md
proof_lab/paninian_samjna_sound_layer.py
proof_lab/test_paninian_samjna_sound_layer.py
proof_lab/PANINIAN_SAMJNA_SOUND_LAYER_EXPECTED.sha256
proof_lab/astadhyayi_ledger.py
proof_lab/test_astadhyayi_ledger.py
proof_lab/astadhyayi/ASTADHYAYI_LEDGER.json
proof_lab/astadhyayi/ASTADHYAYI_LEDGER.md
```

## Theorem 82 Pāṇinian it-saṁjñā compiled packet

| Field | Value |
|---|---|
| Certificate class | 1.3.2–1.3.9 as one interpreter on IAST teaching forms (with 1.3.4, 'ataddhite', 'pratyayasya' and the jñāpaka overrides 7.1.3 / 7.3.50 / 7.1.2 each load-bearing on named forms), equal to the traditional it-sets on 116 forms; theorum/58's and theorum/63's hand-coded it_lopa shown to be instances; 1.1.46 / 1.1.47 augment placement and 1.4.13 aṅga read off the its, with theorum/80's 7.3.84 trigger equal to 'aṅga ends in ik' on all 40 reachable states |
| Status | `PASS_PANINIAN_IT_SAMJNA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `094d38e1fcb4b3cd97bba95ca066472af05719f4f4045f9c0a45b643db8665cf` |
| Boundary | jñāpaka exceptions declared from the cited sūtras, not derived; 6.1.64 / 6.1.65 cited; ir-it, accent its and the whole Dhātupāṭha not on the carrier |

```text
theorum/82_paninian_it_samjna_compiled_theorem.md
proof_lab/paninian_it_samjna_compiled.py
proof_lab/test_paninian_it_samjna_compiled.py
proof_lab/PANINIAN_IT_SAMJNA_COMPILED_EXPECTED.sha256
```

## Theorem 83 Pāṇinīya Śikṣā sources packet

| Field | Value |
|---|---|
| Certificate class | The Pāṇinīya Śikṣā quoted (verses 3–5, 11, 13, 17, 18, 21, 38–40): varṇa counts reproduced on the carrier; theorum/81's sthāna table derived from 13/17/18 (ka-varga at jihvāmūla, 1.1.9 classes identical); theorum/79's manner rows derived from 39–40; verse 21's openness grades separate e/ai, o/au from the text; 1.1.10 load-bearing under the karaṇa reading, redundant under the sparśa reading |
| Status | `PASS_PANINIYA_SIKSHA_SOURCES_CANDIDATE` |
| Canonical result SHA-256 | `473bcf775c05db5253310b94e9fd818d6e22eb20a4f9ed6d2342a836e80b2de5` |
| Boundary | yamas, anusvāra, visarga, ayogavāhas, pluta counted not carried; accent and mātrā cited; the intended prayatna reading not decided |

```text
theorum/83_paniniya_siksha_sources_theorem.md
proof_lab/paniniya_siksha_sources.py
proof_lab/test_paniniya_siksha_sources.py
proof_lab/PANINIYA_SIKSHA_SOURCES_EXPECTED.sha256
```

## Theorem 84 Vedāṅga sources quoted packet

| Field | Value |
|---|---|
| Certificate class | Chandaḥśāstra 8.20–8.35, Baudhāyana Śulbasūtra i.48 / i.61–62, Ṛgveda Vedāṅga Jyotiṣa 1, 4, 22, 32 quoted; the pinned packets of theorum/71, 72, 73 imported and shown to compute the texts' numbers (prastāra … meru equal n ≤ 10/12; √2 cord 577/408; 124 parvans = 2 × 62; RVJ 22 daylight = theorum/73's zigzag on every day) |
| Status | `PASS_VEDANGA_SOURCES_QUOTED_CANDIDATE` |
| Canonical result SHA-256 | `a13d6fe56945ec2faffa37a33ce38d12e17db349c8ceeee027b44f050f679fb1` |
| Boundary | theorum/71's adhvayoga is the literal 8.32 value + 1 (discrepancy recorded, pin untouched); the Yajus-recension integers 1830 / 67 / 1835 / 1860 are not quoted; pins of 71–73 unchanged |

```text
theorum/84_vedanga_sources_quoted_theorem.md
proof_lab/vedanga_sources_quoted.py
proof_lab/test_vedanga_sources_quoted.py
proof_lab/VEDANGA_SOURCES_QUOTED_EXPECTED.sha256
```

## Theorem 85 Nirukta nāmāny-ākhyātajāni packet

| Field | Value |
|---|---|
| Certificate class | Nirukta 1.12 (Śākaṭāyana) made a computation: from gamḷ~, bhū, ḍukṛñ, theorum/82's its + kta with 6.4.37 / 7.2.10 give gata, bhūta, kṛta; theorum/63's pinned ladder derives all 66 sup forms; theorum/64's pinned laṭ gives the 18 ākhyāta forms from the same roots; nāma / ākhyāta partition the computed padas |
| Status | `PASS_NIRUKTA_NAMA_AKHYATAJANI_CANDIDATE` |
| Canonical result SHA-256 | `950cad0deabd1f8185eadb5f85cb7b407a24f6fdf2e544466693cc1542a2b73b` |
| Boundary | three roots and one kṛt affix (Gārgya's "na sarvāṇi" not decided); 6.4.37 list and aniṭ status declared from the Dhātupāṭha; Nirukta 1.1 standard text, 1.12 verified; upasarga / nipāta cited |

```text
theorum/85_nirukta_nama_akhyatajani_theorem.md
proof_lab/nirukta_nama_akhyatajani.py
proof_lab/test_nirukta_nama_akhyatajani.py
proof_lab/NIRUKTA_NAMA_AKHYATAJANI_EXPECTED.sha256
```

## Theorem 86 Nirukta Dhātupāṭha-nāma packet

| Field | Value |
|---|---|
| Certificate class | Eleven kta-prātipadikas read from the PG5 / PG6 pinned Dhātupāṭha entries (Devanagari teaching forms through theorum/82's its, 6.1.64, 6.4.37, 7.2.10); theorum/63's pinned ladder derives all 242 sup forms; the PG stages' laṭ 3sg forms are disjoint from them; six entries refused by the rule they need |
| Status | `PASS_NIRUKTA_DHATUPATHA_NAMA_CANDIDATE` |
| Canonical result SHA-256 | `fdd0f424280bf180ba92c1b00a1f90423c9c36a232230c154acd8d38b71464d2` |
| Boundary | aniṭ status declared; PG laṭ forms read as pinned data, not re-derived; Gārgya's objection undecided |

```text
theorum/86_nirukta_dhatupatha_nama_theorem.md
proof_lab/nirukta_dhatupatha_nama.py
proof_lab/test_nirukta_dhatupatha_nama.py
proof_lab/NIRUKTA_DHATUPATHA_NAMA_EXPECTED.sha256
```

## Theorem 87 Tripādī niṣṭhā compiled packet

| Field | Value |
|---|---|
| Certificate class | 8.2.30, 8.2.40, 8.2.42, 8.2.44, 8.4.53 applied in sūtra order under 8.2.1 to the pinned teaching forms pac, labh, tud, lū + kta → pakta, labdha, tunna, lūna; reverse order leaves labhdha (8.2.1 load-bearing); theorum/63's ladder derives all 88 sup forms |
| Status | `PASS_TRIPADI_NISHTHA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `8f25f7b7384d1e75c3f669f211e82ff798c747c4a001684e9858d17959654228` |
| Boundary | one five-rule, four-input instance of 8.2.1; lvādi beyond lū and 8.2.30 at pada end not claimed; aniṭ declared |

```text
theorum/87_tripadi_nishtha_compiled_theorem.md
proof_lab/tripadi_nishtha_compiled.py
proof_lab/test_tripadi_nishtha_compiled.py
proof_lab/TRIPADI_NISHTHA_COMPILED_EXPECTED.sha256
```

## Theorem 88 Āp-stem sup packet

| Field | Value |
|---|---|
| Certificate class | ṭāp (4.1.4) feminines declined through 7.1.18, 7.3.116, 7.3.113, 7.1.54, 7.3.105, 7.3.106, 6.1.68, 6.1.69, the sandhi sūtras and 8.2.66 / 8.3.15 on theorum/82's it-layer: latā's 22 forms equal the classical paradigm; each stage breaks exactly its own cells; the fifteen kta feminines of theorum/86–87 give 330 forms |
| Status | `PASS_AP_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `0a0e12bffaafc240ce4d8d9edce5aa33776a8f2f440bfc356e03d64859b2c8cb` |
| Boundary | stage order declared as a pipeline; ṅīp, nadī, consonant stems, pronouns not claimed |

```text
theorum/88_ap_stem_sup_compiled_theorem.md
proof_lab/ap_stem_sup_compiled.py
proof_lab/test_ap_stem_sup_compiled.py
proof_lab/AP_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 89 Nadī-stem sup packet

| Field | Value |
|---|---|
| Certificate class | nadī's 22 forms through 7.3.112, 7.3.116, 7.1.54, 7.3.107, 6.1.68, 6.1.69, 6.1.77, 6.1.102 / 6.1.105, 6.1.107, 6.1.88, 6.1.101, 8.3.59, 8.2.66, 8.3.15 (each stage breaks exactly its cells; 7.3.112 redundant on 7s); kartṛ, śrotṛ, hotṛ, cetṛ, sotṛ from the pinned roots by tṛc with theorum/80's guṇa and 1.1.51, + ṅīp → five nadī feminines, 110 forms |
| Status | `PASS_NGI_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `b13ad1d61f7330ba83b7ebd4fe8e9e7215578b189898be111c3ed8843dac591d` |
| Boundary | aniṭ before tṛc declared; stage order a declared pipeline; ṅīṣ / ṅīn, ū-stems, strī not claimed |

```text
theorum/89_ngi_stem_sup_compiled_theorem.md
proof_lab/ngi_stem_sup_compiled.py
proof_lab/test_ngi_stem_sup_compiled.py
proof_lab/NGI_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 90 Ṛ-stem sup packet

| Field | Value |
|---|---|
| Certificate class | kartṛ's 22 forms through 7.1.94 / 1.1.53, 6.4.8, 6.4.11, 7.3.110 / 1.1.51, 6.1.111 / 8.2.24, 6.1.102 / 6.1.103, 6.1.77, 7.1.54 / 6.4.3 / 8.4.1, 8.3.59, 8.2.7, 6.1.68, 8.2.66, 8.3.15; the sarvanāmasthāna saṁjñā and each stage break exactly their cells; śrotṛ, hotṛ, cetṛ, sotṛ (theorum/89) give 88 more forms |
| Status | `PASS_R_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `81f511f69ff7fbb714257449fa620d440b31fdc85345e44eb7b9f958ef447dcd` |
| Boundary | kinship ṛ-stems, 6.4.11's other members, neuters not claimed; 8.4.1 on ṛ-varṇa is the vārttika; stage order a declared pipeline |

```text
theorum/90_r_stem_sup_compiled_theorem.md
proof_lab/r_stem_sup_compiled.py
proof_lab/test_r_stem_sup_compiled.py
proof_lab/R_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 91 Ghi-stem sup packet

| Field | Value |
|---|---|
| Certificate class | hari and guru (one engine; guṇa by theorum/80's antaratama) 22 forms each through 1.4.7, 7.3.111, 7.3.119, 7.3.120, 7.3.108, 7.3.109, 6.1.110, 6.1.102 / 103, 6.1.107 / 77 / 78 / 88, 7.1.54 / 6.4.3, 8.4.1 / 8.4.2 / 8.4.37, 6.1.69, 8.3.59, pause rules; the ghi saṁjñā breaks exactly {3s, 4s, 5s, 6s, 7s}; agni and vāyu 44 forms with ṇatva decided on the carrier |
| Status | `PASS_GHI_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `8c344c02789c9c78512cf0e00d12469ec32ee675795f717712c384258ed8712a` |
| Boundary | sakhi / pati, feminine and neuter i / u stems, ī / ū stems not claimed; stems declared prātipadikas; stage order a declared pipeline |

```text
theorum/91_ghi_stem_sup_compiled_theorem.md
proof_lab/ghi_stem_sup_compiled.py
proof_lab/test_ghi_stem_sup_compiled.py
proof_lab/GHI_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 92 Consonant-stem sup packet

| Field | Value |
|---|---|
| Certificate class | rājan, ātman, marut (66 forms) through 1.4.17 pada / 1.4.18 bha, 6.4.8, 6.1.68, 8.2.7 / 8.2.8, 6.4.134 / 6.4.136 / 6.4.137, 8.4.40, 8.2.39 / 8.4.55 / 8.4.56, pause rules; pada and bha break exactly their cells; 6.4.137 control (*ātmnaḥ); pada not load-bearing on marutsu (recorded) |
| Status | `PASS_HAL_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `e1f6ab512415adf1632311d5d915e3cd85ed2b20a9229011be4cfa67d677330c` |
| Boundary | other consonant stems, neuters, option mechanics of 6.4.136 not claimed; stems declared prātipadikas; stage order a declared pipeline |

```text
theorum/92_hal_stem_sup_compiled_theorem.md
proof_lab/hal_stem_sup_compiled.py
proof_lab/test_hal_stem_sup_compiled.py
proof_lab/HAL_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 93 The Neuter Sup Paradigms Compiled packet

| Field | Value |
|---|---|
| Certificate class | phala and vāri (44 forms) through 7.1.23 / 7.1.24, 7.1.19, 7.1.20 with 1.1.42, 7.1.72, 7.1.73, 6.4.8, 6.1.87 and theorum/63's a-stem sūtras; each neuter substitute and num rule breaks exactly its cells; nuṭ read before 7.1.73 |
| Status | `PASS_NAPUMSAKA_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `3857e2b0476872a7b4407f3c97750bc5eb550fc53c57cdae6ebdadb52cb42006` |
| Boundary | madhu, consonant neuters, neuter sarvanāma not claimed; the second sambuddhi option he vāri listed from the Siddhānta-kaumudī; stage order a declared pipeline |

```text
theorum/93_napumsaka_sup_compiled_theorem.md
proof_lab/napumsaka_sup_compiled.py
proof_lab/test_napumsaka_sup_compiled.py
proof_lab/NAPUMSAKA_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 94 The Sarvanāma Sup Paradigms Compiled packet

| Field | Value |
|---|---|
| Certificate class | sarva (22 forms) and tad (21) through 1.1.27, 7.1.17, 7.1.14, 7.1.15, 7.1.52, 7.3.103, 8.3.59, 7.2.102, 7.2.106 with 6.1.97 and theorum/63's a-stem sūtras; the sarvanāma saṁjñā breaks exactly {1p, 4s, 5s, 6p, 7s}; 7.2.102 every cell of tad, 7.2.106 exactly 1s; sambuddhi of tad refused |
| Status | `PASS_SARVANAMA_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `1a04614384396443b1eaf0c4bf07da61a822b8cbab3b80315bfd53e96f924152` |
| Boundary | feminine / neuter pronouns, etad / yad / idam / asmad, the 1.1.34 option cells not claimed; sarva declared from the gaṇa; stage order a declared pipeline |

```text
theorum/94_sarvanama_sup_compiled_theorem.md
proof_lab/sarvanama_sup_compiled.py
proof_lab/test_sarvanama_sup_compiled.py
proof_lab/SARVANAMA_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 95 Laṅ Parasmaipada Compiled on Theorem 58's Stems packet

| Field | Value |
|---|---|
| Certificate class | laṅ parasmaipada of bhū, gam, nī (27 forms) on theorum/58's derived present stems with 6.4.71 (aṭ placed by theorum/82's marker reading), 3.4.100, 3.4.101, 3.4.99, 7.1.3, 8.2.23, 7.3.101, 8.2.66 / 8.3.15; each stage breaks exactly its cells |
| Status | `PASS_LAN_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `7b473c21e9ebc878a4d573de20642158079a9a4ddb0756b5b21a31dc372fd427` |
| Boundary | ātmanepada, 6.4.72 āṭ, accent, other roots and lakāras not claimed; stage order a declared pipeline |

```text
theorum/95_lan_parasmaipada_compiled_theorem.md
proof_lab/lan_parasmaipada_compiled.py
proof_lab/test_lan_parasmaipada_compiled.py
proof_lab/LAN_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 96 Loṭ and Vidhi-Liṅ Parasmaipada Compiled packet

| Field | Value |
|---|---|
| Certificate class | loṭ (3.4.85–92, 6.4.105) and vidhi-liṅ (3.4.103 yāsuṭ, 3.4.108, 7.2.79, 7.2.80, 6.1.66, 6.1.97) parasmaipada of bhū, gam, nī on theorum/58's stems: 54 forms; each stage breaks exactly its cells; 7.3.101 blocked by yāsuṭ (bhaveva); 3.4.92 surface-load-bearing on 1s only |
| Status | `PASS_LOT_LIN_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `0fd095433be173b03093358c1ca55fd4af77d661d71aa9128cafc330fe25672a` |
| Boundary | ātmanepada loṭ / liṅ, āśīr-liṅ, other roots not claimed; stage orders declared pipelines |

```text
theorum/96_lot_lin_parasmaipada_compiled_theorem.md
proof_lab/lot_lin_parasmaipada_compiled.py
proof_lab/test_lot_lin_parasmaipada_compiled.py
proof_lab/LOT_LIN_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 97 Lṛṭ and Luṭ Parasmaipada Compiled packet

| Field | Value |
|---|---|
| Certificate class | lṛṭ (sya, iṭ by 7.2.35 / 7.2.58, 7.3.84 guṇa, 6.1.78, 8.3.59) of bhū, gam, nī and luṭ (tās, 2.4.85 ḍā / rau / ras, 6.4.143, 7.4.50, 7.4.51) of bhū, nī: 45 forms; each stage breaks exactly its cells; 7.2.58 load-bearing on gam only; gam's luṭ refused |
| Status | `PASS_LRT_LUT_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `0d245b9d5254260fb1074afd6344c73b3a7ff532c256bc12ad227d8858182875` |
| Boundary | seṭ / aniṭ declared; lṛṅ, luṅ, liṭ, ātmanepada, other roots not claimed; stage orders declared pipelines |

```text
theorum/97_lrt_lut_parasmaipada_compiled_theorem.md
proof_lab/lrt_lut_parasmaipada_compiled.py
proof_lab/test_lrt_lut_parasmaipada_compiled.py
proof_lab/LRT_LUT_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 98 The Feminine Sarvanāma (Āp) Sup Paradigms Compiled packet

| Field | Value |
|---|---|
| Certificate class | sarvā (22) and sā (21) on the āp engine with 7.3.114 syāṭ + shortening and 7.1.52; sarvanāma breaks exactly {4s, 5s, 6s, 7s, 6p}; 7.3.113 superseded; the masculine 7.1.17 / 7.1.15 shown not to reach the feminine (*sarve, *sarvāsmin); 7.2.102 every cell of sā, 7.2.106 exactly 1s |
| Status | `PASS_SARVANAMA_AP_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `dc7a91476353ced6c2f85ef1c50ca5eccf55f5469ebcf685f20a381209b68ed9` |
| Boundary | neuter pronouns, idam / etad / yad, 1.1.34 options, 7.3.115 not claimed; stage order a declared pipeline |

```text
theorum/98_sarvanama_ap_sup_compiled_theorem.md
proof_lab/sarvanama_ap_sup_compiled.py
proof_lab/test_sarvanama_ap_sup_compiled.py
proof_lab/SARVANAMA_AP_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 99 Laṅ, Loṭ and Vidhi-Liṅ Ātmanepada Compiled packet

| Field | Value |
|---|---|
| Certificate class | laṅ (6.4.71 / 6.4.72 + 6.1.90, 7.2.81 chain), loṭ (3.4.90–93) and vidhi-liṅ (3.4.102 sīyuṭ, 3.4.105–107, 7.2.79, 6.1.66, 6.1.87) ātmanepada of labh and edh on theorum/66's stems: 54 forms; each stage breaks exactly its cells; 6.4.72 on edh only; 7.3.101 blocked by sīyuṭ; three surface-neutral stages recorded |
| Status | `PASS_ATMANEPADA_LAN_LOT_LIN_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `494ca1c894b7a576a97d7b8dfbf79f837726ea9d49a2ed56f5609d4e014489ea` |
| Boundary | other roots, luṅ / liṭ / lṛṭ ātmanepada, 3.4.95–96, accent not claimed; stage orders declared pipelines |

```text
theorum/99_atmanepada_lan_lot_lin_compiled_theorem.md
proof_lab/atmanepada_lan_lot_lin_compiled.py
proof_lab/test_atmanepada_lan_lot_lin_compiled.py
proof_lab/ATMANEPADA_LAN_LOT_LIN_COMPILED_EXPECTED.sha256
```

## Theorem 100 The Kṛt Affixes ktvā, tumun, tavya from the Pinned Roots packet

| Field | Value |
|---|---|
| Certificate class | ktvā, tumun, tavya of bhū, gam, kṛ, śru, nī, hu (18 forms): iṭ by 7.2.35 against 7.2.11, guṇa by 7.3.84 against 1.1.5, gam's nasal by 6.4.37 against 8.3.24 / 8.4.58; each rule breaks exactly the forms stated; gantā realized |
| Status | `PASS_KRT_KTVA_TUMUN_TAVYA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `2f0229cf938ac80b60dc5e7b11904ede4275b8cb58eb8f3c52ab10cd6465ced9` |
| Boundary | bhū's seṭ status declared; lyap, anīyar, ṇvul, 7.2.56 option, other roots not claimed |

```text
theorum/100_krt_ktva_tumun_tavya_compiled_theorem.md
proof_lab/krt_ktva_tumun_tavya_compiled.py
proof_lab/test_krt_ktva_tumun_tavya_compiled.py
proof_lab/KRT_KTVA_TUMUN_TAVYA_COMPILED_EXPECTED.sha256
```

## Theorem 101 Luṅ Parasmaipada Compiled packet

| Field | Value |
|---|---|
| Certificate class | luṅ parasmaipada of bhū (2.4.77 sic-luk, 6.4.88 vuk), gam (3.1.55 aṅ by the ḷ-it) and nī (sic: 7.2.1, 7.3.96, 8.3.59, 8.4.41, 3.4.109): 27 forms; each stage breaks exactly its cells on exactly its root |
| Status | `PASS_LUN_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `2e5af3d79ef6d321f922d0cb3b140cefd2df8e6646e76dc2054d23b628895bc0` |
| Boundary | other aorist shapes, ātmanepada, 6.4.72, the gaṇas beyond the ḷdit test, other roots not claimed; stage order a declared pipeline |

```text
theorum/101_lun_parasmaipada_compiled_theorem.md
proof_lab/lun_parasmaipada_compiled.py
proof_lab/test_lun_parasmaipada_compiled.py
proof_lab/LUN_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 102 Liṭ Parasmaipada Compiled with Reduplication packet

| Field | Value |
|---|---|
| Certificate class | liṭ of bhū, gam, kṛ, nī in the option-free cells (20 forms): abhyāsa by 6.1.1 / 6.1.4 / 6.1.8, 7.4.59 / 60 / 62 / 66 / 73, 8.4.54; 1.2.5 kit; 7.2.115 / 7.2.116 vṛddhi before ṇal; 6.4.98; 6.4.88; 7.2.13 / 7.2.35; each stage breaks exactly the forms stated |
| Status | `PASS_LIT_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `740371db21bfa78c1b0d53919a0a08e94a065f10e3c2a0003c8d4229188c80ba` |
| Boundary | option cells, ātmanepada, ām-liṭ, cluster / vowel-initial roots, accent not claimed; stage order a declared pipeline |

```text
theorum/102_lit_parasmaipada_compiled_theorem.md
proof_lab/lit_parasmaipada_compiled.py
proof_lab/test_lit_parasmaipada_compiled.py
proof_lab/LIT_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 103 Taddhita Affixes aṇ, iñ, yañ, ṭhak Compiled packet

| Field | Value |
|---|---|
| Certificate class | aupagava, kaurava, dāśarathi, dākṣi, gārgya, śaiva, bauddha, paurāṇika from the quoted sense sūtras with 7.2.117 / 7.2.118 (first-vowel vṛddhi by theorum/80's antaratama), 6.4.146, 6.4.148, 7.3.50, 6.1.78; each rule breaks exactly the derivations stated |
| Status | `PASS_TADDHITA_AN_IN_YAN_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `b155be373ef472d8b22663dea569cb8e1b23b856db4bf9831a479cd6df170d60` |
| Boundary | affix choice declared from the sense sūtra / gaṇa; feminines, 1.1.73, exceptions, declension not claimed |

```text
theorum/103_taddhita_an_in_yan_compiled_theorem.md
proof_lab/taddhita_an_in_yan_compiled.py
proof_lab/test_taddhita_an_in_yan_compiled.py
proof_lab/TADDHITA_AN_IN_YAN_COMPILED_EXPECTED.sha256
```

## Theorem 104 Samāsa Compiled packet

| Field | Value |
|---|---|
| Certificate class | rājapuruṣa, kṛṣṇaśrita, yūpadāru, vṛkabhaya, akṣaśauṇḍa, devālaya, nīlotpala, rājarṣi, mahārāja, pītāmbara, citragu, rāmalakṣmaṇa from their sup-ending members by 2.4.71, 1.2.43 / 2.2.30, 2.2.34, 6.3.46, 5.4.91, 6.4.144, 8.2.7, 1.2.48, 6.1.101, 6.1.87, 1.1.51; rājapuruṣa declined 21 cells on theorum/63 with 8.4.1's ṣ-trigger; each rule breaks exactly the compounds stated |
| Status | `PASS_SAMASA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `d23a43e951dd5217e30315dabe4cc4ff3d95d24f6ea6a35e51675bb0933eeec4` |
| Boundary | kind of compound and karmadhāraya / bahuvrīhi order declared; other samāsānta affixes, accent, dvigu, avyayībhāva, ekaśeṣa not claimed |

```text
theorum/104_samasa_compiled_theorem.md
proof_lab/samasa_compiled.py
proof_lab/test_samasa_compiled.py
proof_lab/SAMASA_COMPILED_EXPECTED.sha256
```

## Theorem 105 ṇic Causatives Compiled packet

| Field | Value |
|---|---|
| Certificate class | bhāvayati, kārayati, nāyayati, hārayati, pācayati, gamayati, sthāpayati, dāpayati, pāyayati, vedayati, bodhayati, karṣayati in laṭ 3s / 3p / 1s by 3.1.26 with 7.2.115, 7.2.116, 6.4.92, 7.3.36, 7.3.37, 7.3.86, 1.1.51, 7.3.84, 6.1.78, 7.1.3, 6.1.97, 7.3.101; each rule breaks exactly the forms stated |
| Status | `PASS_NIC_CAUSATIVE_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `c194911675d12b32db4c70365d36cdfc522253b94ac3f3a398d236726c307c03` |
| Boundary | mit status and the puk / yuk root lists declared; ātmanepada, other lakāras, 6.4.51 not claimed |

```text
theorum/105_nic_causative_compiled_theorem.md
proof_lab/nic_causative_compiled.py
proof_lab/test_nic_causative_compiled.py
proof_lab/NIC_CAUSATIVE_COMPILED_EXPECTED.sha256
```

## Theorem 106 san Desideratives Compiled packet

| Field | Value |
|---|---|
| Certificate class | pipaṭhiṣati, bubhūṣati, cikīrṣati, jigamiṣati, pipāsati, ninīṣati, pipakṣati, jijñāsate, ditsati by 3.1.7 with 6.1.9 on theorum/102's abhyāsa carrier and 7.4.79, 7.2.35 / 7.2.10 / 7.2.58, 1.2.9, 6.4.16, 7.1.100, 8.2.77, 8.3.59, 8.2.30, 7.4.54 / 7.4.49 / 7.4.58, 1.3.57 with 3.4.79; each rule breaks exactly the forms stated |
| Status | `PASS_SAN_DESIDERATIVE_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `1164e8716903032b4254280ceed473ff26099e6648fa43b217b6d49e1de84924` |
| Boundary | anudātta and ghu status declared; other persons / lakāras, sannanta kṛt, 7.4.55–57 roots not claimed |

```text
theorum/106_san_desiderative_compiled_theorem.md
proof_lab/san_desiderative_compiled.py
proof_lab/test_san_desiderative_compiled.py
proof_lab/SAN_DESIDERATIVE_COMPILED_EXPECTED.sha256
```

## Theorem 107 Kṛt ghañ / lyuṭ / ṇvul / śatṛ Compiled packet

| Field | Value |
|---|---|
| Certificate class | bhāva, kāra, nāya, pāka, tyāga, yoga (ghañ), bhavana, nayana, karaṇa, gamana, pacana (lyuṭ), kāraka, pācaka, nāyaka, bhāvaka, yojaka (ṇvul), bhavat, gacchat, nayat (śatṛ on theorum/58's present stem) with 7.1.1, 7.2.115, 7.2.116, 7.3.52, 7.3.84, 7.3.86, 1.1.51, 6.1.78, 8.4.2, 6.1.97; each rule breaks exactly the words stated |
| Status | `PASS_KRT_GHAN_LYUT_NVUL_SATR_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `38288cf4d74d7d0abf729d13454cdc5b615ce666c1214df692fdd12f75216e0a` |
| Boundary | affix per word declared; declension of the kṛt words, feminine of śatṛ, ghañ exceptions, accent not claimed |

```text
theorum/107_krt_ghan_lyut_nvul_satr_compiled_theorem.md
proof_lab/krt_ghan_lyut_nvul_satr_compiled.py
proof_lab/test_krt_ghan_lyut_nvul_satr_compiled.py
proof_lab/KRT_GHAN_LYUT_NVUL_SATR_COMPILED_EXPECTED.sha256
```

## Theorem 108 yaṅ Intensives Compiled packet

| Field | Value |
|---|---|
| Certificate class | bobhūyate, pāpacyate, cekrīyate, dedīpyate, nenīyate, jaṅgamyate by 3.1.22 / 1.3.12 with 7.4.27, 6.1.9 on theorum/102's abhyāsa carrier, 7.4.82, 7.4.83 with its apavāda 7.4.85 (+ 8.3.24, 8.4.58), 1.1.5, 3.4.79; each rule breaks exactly the forms stated; 7.4.59 recorded vacuous |
| Status | `PASS_YAN_INTENSIVE_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `f1fbe2ff7939e7746529fc134269de3bdd6524026bf7a5b4057587900cfb83f2` |
| Boundary | yaṅ-luk, other persons / lakāras, the 7.4.84–92 augments not claimed |

```text
theorum/108_yan_intensive_compiled_theorem.md
proof_lab/yan_intensive_compiled.py
proof_lab/test_yan_intensive_compiled.py
proof_lab/YAN_INTENSIVE_COMPILED_EXPECTED.sha256
```

## Theorem 109 Ugit at-Stems Declined packet

| Field | Value |
|---|---|
| Certificate class | bhavat, bhagavat, dhīmat declined (22 cells each) on theorum/92's consonant-stem carrier with 7.1.70 num (ugit read from the anunāsika markers by theorum/82, placed by 1.1.47), 6.4.14, 8.2.23, 8.2.9; each new rule breaks exactly its cells; marut control takes no num |
| Status | `PASS_UGIT_AT_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `6588e97cfbc637bdd36e4b89c10be219917ecdef217d0311cbd63b0f92189fd9` |
| Boundary | feminine, neuter, mahat, vasu- / īyasu-stems not claimed; theorum/92's rules are the carrier |

```text
theorum/109_ugit_at_stem_sup_compiled_theorem.md
proof_lab/ugit_at_stem_sup_compiled.py
proof_lab/test_ugit_at_stem_sup_compiled.py
proof_lab/UGIT_AT_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 110 The Passive Compiled packet

| Field | Value |
|---|---|
| Certificate class | bhūyate, nīyate, gamyate, pacyate, labhyate, hanyate, dīyate, sthīyate, ucyate, supyate, ijyate and their 3p by 3.1.67 / 3.4.69 / 1.3.13 with 1.1.5, 6.4.66, 6.1.15 + 6.1.108 (1.1.45), 7.1.3, 6.1.97, 3.4.79; each rule breaks exactly the forms stated |
| Status | `PASS_PASSIVE_YAK_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `742d0a1cf7ca58dd30ef7f0117232a91525c275c34d13616abb3c87a623cb687` |
| Boundary | list membership of 6.1.15 / 6.4.66 declared; kṛ, derived-root passives, other persons / lakāras not claimed |

```text
theorum/110_passive_yak_compiled_theorem.md
proof_lab/passive_yak_compiled.py
proof_lab/test_passive_yak_compiled.py
proof_lab/PASSIVE_YAK_COMPILED_EXPECTED.sha256
```

## Theorem 111 The Feminine Affixes Compiled packet

| Field | Value |
|---|---|
| Certificate class | bālā, devā, ajā, kārikā, pācikā, nāyikā (ṭāp 4.1.4, 7.3.44), bhavantī, dhīmatī, bhagavatī (ṅīp 4.1.6, 7.1.81), aupagavī, dākṣī (4.1.15), gārgī (4.1.16, 6.4.150), gaurī (ṅīṣ 4.1.41), with 6.4.148; the forming affix's markers read by theorum/82; each rule breaks exactly the stems stated; bālā, kārikā on theorum/88 and bhavantī, gārgī on theorum/89 |
| Status | `PASS_STRI_PRATYAYA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `57435747f98233302542a21415e4baabf436c9d4a094674ad40a17778f8b1326` |
| Boundary | gaurādi membership and optional affixes declared; 4.1.5, 4.1.20–75, ṅīn, ūṅ not claimed |

```text
theorum/111_stri_pratyaya_compiled_theorem.md
proof_lab/stri_pratyaya_compiled.py
proof_lab/test_stri_pratyaya_compiled.py
proof_lab/STRI_PRATYAYA_COMPILED_EXPECTED.sha256
```

## Theorem 112 Ātmanepada lṛṭ and luṭ Compiled packet

| Field | Value |
|---|---|
| Certificate class | labh (aniṭ) and edh (seṭ) in lṛṭ / luṭ ātmanepada, 6 cells each: 3.1.33 sya / tās, 7.2.35 / 7.2.10, 8.4.55 (lapsyate), 8.2.40 + 8.4.53 (labdhā), 8.3.59, 3.4.79 / 3.4.80, 7.2.81 chain (lapsyete), 2.4.85 + 6.4.143 + 7.4.51, 7.4.50 (labdhāse), 7.4.52 (labdhāhe); each rule breaks exactly the forms stated |
| Status | `PASS_ATMANEPADA_LRT_LUT_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `01b054d21b3318af879b201cdd1c0776fe4a4c52cf2f9e30654e4de3b776f367` |
| Boundary | see the capsule's claim boundary |

```text
theorum/112_atmanepada_lrt_lut_compiled_theorem.md
proof_lab/atmanepada_lrt_lut_compiled.py
proof_lab/test_atmanepada_lrt_lut_compiled.py
proof_lab/ATMANEPADA_LRT_LUT_COMPILED_EXPECTED.sha256
```

## Theorem 113 The Pronominal Adverbs Compiled packet

| Field | Value |
|---|---|
| Certificate class | tataḥ, tatra, tadā, yataḥ, yatra, yadā, kutaḥ, kutra, kadā, iha, ataḥ, atra, sarvataḥ, sarvatra, sarvadā by tasil / tral / dā / haḥ (5.3.7, 5.3.10, 5.3.15, 5.3.11) with 2.4.71, 7.2.102 + 6.1.97, 7.2.103, 7.2.104, 5.3.3, 5.3.5, 8.2.66 / 8.3.15; each rule breaks exactly the forms stated |
| Status | `PASS_PRONOMINAL_TADDHITA_ADVERBS_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `ca3e9059981c53bf1c444a1f33e61913847fa71a0ab0f9341a606e3c5d8033b2` |
| Boundary | see the capsule's claim boundary |

```text
theorum/113_pronominal_taddhita_adverbs_compiled_theorem.md
proof_lab/pronominal_taddhita_adverbs_compiled.py
proof_lab/test_pronominal_taddhita_adverbs_compiled.py
proof_lab/PRONOMINAL_TADDHITA_ADVERBS_COMPILED_EXPECTED.sha256
```

## Theorem 114 Avyayībhāva and Dvigu Compiled packet

| Field | Value |
|---|---|
| Certificate class | upakumbham, pratidinam (2.4.83 am), adhihari, yathāśakti (2.4.82 luk), trilokī, pañcamūlī (4.1.21 + 6.4.148), pañcagavam (5.4.92 + 6.1.78 + 2.4.17 + 7.1.24), tripadam — the two compound kinds theorum/104 left out; each rule breaks exactly the forms stated |
| Status | `PASS_AVYAYIBHAVA_DVIGU_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `58653d425c4c29a2f3c1a1b5f60a6df82de242dbdf74b6704a91d676e6082f57` |
| Boundary | see the capsule's claim boundary |

```text
theorum/114_avyayibhava_dvigu_compiled_theorem.md
proof_lab/avyayibhava_dvigu_compiled.py
proof_lab/test_avyayibhava_dvigu_compiled.py
proof_lab/AVYAYIBHAVA_DVIGU_COMPILED_EXPECTED.sha256
```

## Theorem 115 Āśīrliṅ Parasmaipada Compiled packet

| Field | Value |
|---|---|
| Certificate class | bhūyāt, gamyāt, nīyāt, pacyāt, deyāt, stheyāt and their 3d / 3p (18 forms): 3.4.103 yāsuṭ, 3.4.104 kit (1.1.5), 7.2.79, 6.4.67 er liṅi, 3.4.100 / 3.4.101 / 3.4.108; each rule breaks exactly the forms stated |
| Status | `PASS_ASIRLIN_PARASMAIPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `523b3d25575aa3495182cdc17dbcc4ef7a5e4f62bc09990353262ef905495f7d` |
| Boundary | see the capsule's claim boundary |

```text
theorum/115_asirlin_parasmaipada_compiled_theorem.md
proof_lab/asirlin_parasmaipada_compiled.py
proof_lab/test_asirlin_parasmaipada_compiled.py
proof_lab/ASIRLIN_PARASMAIPADA_COMPILED_EXPECTED.sha256
```

## Theorem 116 Ātmanepada luṅ Compiled packet

| Field | Value |
|---|---|
| Certificate class | alabdha, alapsātām, alapsata, alapsi, alabdhāḥ, alapsmahi; aidhiṣṭa, aidhiṣātām, aidhiṣata, aidhiṣi, aidhiṣṭhāḥ, aidhiṣmahi: 3.1.44 sic, 6.4.71 / 6.4.72 + 6.1.90, 7.2.35 / 7.2.10, 8.2.26 jhalo jhali, 8.2.40 + 8.4.53, 8.4.55, 8.3.59 + 8.4.41, 7.1.5; each rule breaks exactly the forms stated |
| Status | `PASS_ATMANEPADA_LUN_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `d2912a3970719023cdf9c7594fcb083122af1e0d21bb9adbbd7a13e9d47f1f33` |
| Boundary | see the capsule's claim boundary |

```text
theorum/116_atmanepada_lun_compiled_theorem.md
proof_lab/atmanepada_lun_compiled.py
proof_lab/test_atmanepada_lun_compiled.py
proof_lab/ATMANEPADA_LUN_COMPILED_EXPECTED.sha256
```

## Theorem 117 Āśīrliṅ Ātmanepada Compiled packet

| Field | Value |
|---|---|
| Certificate class | lapsīṣṭa, lapsīyāstām, lapsīran, lapsīya; edhiṣīṣṭa, edhiṣīyāstām, edhiṣīran, edhiṣīya: 3.4.102 sīyuṭ, 3.4.107 suṭ, 3.4.105 ran, 3.4.106 iṭo 't, 6.1.66, 7.2.35 / 7.2.10, 8.4.55, 8.3.59 + 8.4.41; each rule breaks exactly the forms stated |
| Status | `PASS_ASIRLIN_ATMANEPADA_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `2e721a69e0515126fd4ff1d861bf5ac4fd82076892c5f9c1003a022b89ba8c15` |
| Boundary | see the capsule's claim boundary |

```text
theorum/117_asirlin_atmanepada_compiled_theorem.md
proof_lab/asirlin_atmanepada_compiled.py
proof_lab/test_asirlin_atmanepada_compiled.py
proof_lab/ASIRLIN_ATMANEPADA_COMPILED_EXPECTED.sha256
```

## Theorem 123 In-Stems Declined packet

| Field | Value |
|---|---|
| Certificate class | daṇḍin (22 cells), yaśasvin / grāhin / uṣṇabhojin, the neuter daṇḍi, by 6.4.13 (daṇḍī), 6.4.12 (daṇḍīni), 6.1.68, 8.2.7 on the pada, 8.2.8, 7.1.23 / 7.1.20, 8.3.59, 8.4.2 (grāhiṇau); prathiman on theorum/92's an-carrier — the engine theorum/120 and 121 named as their next target; each rule breaks exactly the cells stated |
| Status | `PASS_IN_STEM_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `9f753001c51e9c51949615be4d707b736f0c27f453999379ef2d758201f0733e` |
| Boundary | see the capsule's claim boundary |

```text
theorum/123_in_stem_sup_compiled_theorem.md
proof_lab/in_stem_sup_compiled.py
proof_lab/test_in_stem_sup_compiled.py
proof_lab/IN_STEM_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 124 yuṣmad and asmad Declined packet

| Field | Value |
|---|---|
| Certificate class | the two personal pronouns, 21 cells each: the maparyanta substitutes 7.2.91–97, the ā / y / lopa of the final 7.2.86–90 (anādeśe), the ending substitutes 7.1.27–33, 6.1.107 / 6.1.101 / 6.1.97; twenty-two ablations; each rule breaks exactly the cells stated |
| Status | `PASS_YUSMAD_ASMAD_SUP_COMPILED_CANDIDATE` |
| Canonical result SHA-256 | `9a32fce53c02e30c7eebe43ee3da6131a8e98975f950255d1c58c6fefb817d15` |
| Boundary | see the capsule's claim boundary |

```text
theorum/124_yusmad_asmad_sup_compiled_theorem.md
proof_lab/yusmad_asmad_sup_compiled.py
proof_lab/test_yusmad_asmad_sup_compiled.py
proof_lab/YUSMAD_ASMAD_SUP_COMPILED_EXPECTED.sha256
```

## Theorem 125 The Sup Rule-Table Engine packet

| Field | Value |
|---|---|
| Certificate class | one rule table (64 quoted sūtra rows) and one phase-ordered driver reproduce the 330 cells of fifteen certified paradigms (theorum/63, 88, 89, 90, 91, 92, 93, 94, 98, 109, 123) exactly; every row load-bearing on the suite; new classes cost rows, not engines |
| Status | `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `90dd54de973176a173a5a7644dcaae9aa65c797f9e3a7a15b481cec9935dd5dc` |
| Boundary | declared class flags and gender are inputs; option cells compared on the first alternative; Theorem 63's ladder remains the account of conflict |

```text
theorum/125_sup_rule_table_engine_theorem.md
proof_lab/sup_rule_table_engine.py
proof_lab/test_sup_rule_table_engine.py
proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 127 Rule-Table Engine III packet

| Field | Value |
|---|---|
| Certificate class | Rule-Table Engine III |
| Status | `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `90dd54de973176a173a5a7644dcaae9aa65c797f9e3a7a15b481cec9935dd5dc` |
| Boundary | numerals dvi, tri, catur, pañcan, ṣaṣ, aṣṭan in three genders; 84 cells from 13 rows |

```text
theorum/127_sup_rule_table_engine_numerals_theorem.md
proof_lab/sup_rule_table_engine.py
proof_lab/test_sup_rule_table_engine.py
proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 128 Rule-Table Engine IV packet

| Field | Value |
|---|---|
| Certificate class | Rule-Table Engine IV |
| Status | `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `90dd54de973176a173a5a7644dcaae9aa65c797f9e3a7a15b481cec9935dd5dc` |
| Boundary | pronouns tad, etad, yad, tyad, kim, idam in three genders; 315 cells from 14 rows |

```text
theorum/128_sup_rule_table_engine_pronouns_theorem.md
proof_lab/sup_rule_table_engine.py
proof_lab/test_sup_rule_table_engine.py
proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 129 Tiṅ Rule-Table Engine packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | bhvādi present system: bhū, gam, nī, edh, labh × laṭ, laṅ, loṭ, liṅ; 180 cells from 40 rows |

```text
theorum/129_ting_rule_table_engine_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 130 Tiṅ Rule-Table Engine II packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine II |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | lṛṭ, luṭ, āśīrliṅ, luṅ of bhū, gam, nī, edh, labh on the certified cells; 125 cells from 23 rows; 63 rows on 305 cells |

```text
theorum/130_ting_rule_table_engine_ardhadhatuka_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 131 Tiṅ Rule-Table Engine III packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine III |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | liṭ of bhū, gam, kṛ, nī on the 20 certified cells from 12 rows; the abhyāsa as a segment; 75 rows on 325 cells |

```text
theorum/131_ting_rule_table_engine_lit_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 132 Tiṅ Rule-Table Engine IV packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine IV |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | the vikaraṇa classes (śyan, śa, śnu, u, śnā, ṇic) on 79 quoted laṭ cells of seventeen roots; 96 rows on 404 cells |

```text
theorum/132_ting_rule_table_engine_vikarana_classes_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 133 Tiṅ Rule-Table Engine V packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine V |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | adādi, juhotyādi, rudhādi (luk, ślu, śnam) on 101 quoted laṭ cells of fourteen roots; 109 rows on 505 cells |

```text
theorum/133_ting_rule_table_engine_luk_slu_snam_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 134 Tiṅ Rule-Table Engine VI packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine VI |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | 86 svādi / tanādi / kryādi entries on 91 quoted cells from eight new rows; 115 rows on 596 cells |

```text
theorum/134_ting_rule_table_engine_nasal_breadth_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 135 Tiṅ Rule-Table Engine VII packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine VII |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | 38 adādi / juhotyādi entries on 136 quoted cells from ten new rows; 125 rows on 732 cells |

```text
theorum/135_ting_rule_table_engine_adadi_juhotyadi_breadth_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 136 Tiṅ Rule-Table Engine VIII packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine VIII |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | 32 adādi consonant-root entries on 176 quoted cells from nineteen new rows; 144 rows on 908 cells |

```text
theorum/136_ting_rule_table_engine_adadi_consonant_roots_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 137 Independent-Oracle Audit packet

| Field | Value |
|---|---|
| Certificate class | Independent-Oracle Audit |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | both engines against vidyut-prakriya: 1,728 / 1,744 comparable cells agree, no engine form wrong, three attributions corrected (7.2.76, 8.4.40, 3.4.107) |

```text
theorum/137_independent_oracle_audit_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 138 Generalisation Test packet

| Field | Value |
|---|---|
| Certificate class | Generalisation Test |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | 7,052 unseen cells against vidyut: laṭ of classes 1–10 and lṛṭ / āśīrliṅ of the bhvādi 1,373 / 1,373 after five row corrections; laṅ / loṭ / liṅ of classes 2–10 measured as the open lane |

```text
theorum/138_generalisation_test_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 139 Tiṅ Rule-Table Engine IX packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine IX |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | laṅ / loṭ / vidhiliṅ of classes 2–10 from the strong-ending predicate and nine rows: 5,064 / 5,373 generator cells, 6,706 / 7,052 unseen cells overall; 154 rows |

```text
theorum/139_ting_rule_table_engine_open_lane_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 140 Tiṅ Rule-Table Engine X packet

| Field | Value |
|---|---|
| Certificate class | Tiṅ Rule-Table Engine X |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | the open lane, second pass: 5,223 / 5,373 generator cells, 6,865 / 7,052 unseen cells overall; 157 rows |

```text
theorum/140_ting_rule_table_engine_open_lane_ii_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 141 Sup Generalisation Test packet

| Field | Value |
|---|---|
| Certificate class | Sup Generalisation Test |
| Status | `PASS_SUP_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `90dd54de973176a173a5a7644dcaae9aa65c797f9e3a7a15b481cec9935dd5dc` |
| Boundary | 48 new stems of every declared class against vidyut: 1,068 / 1,078 cells; two rows exposed (kṣ in ṇatva, 7.1.25) |

```text
theorum/141_sup_generalisation_test_theorem.md
proof_lab/sup_rule_table_engine.py
proof_lab/test_sup_rule_table_engine.py
proof_lab/SUP_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 142 Pāṇini Kernel packet

| Field | Value |
|---|---|
| Certificate class | Pāṇini Kernel |
| Status | `PASS_PANINI_KERNEL_CANDIDATE` |
| Canonical result SHA-256 | `691ca9459edbfe2341c4773a258eb6847a4cbda89933c49aa335357bb39128d5` |
| Boundary | the two engines, the ledger and the evidence as one object: 230 sūtras as rows after theorum/143 (225 at first pin 41854a6b…, in the history), 18 shared (junction / tripādī only), every row a ledger entry and every engine ledger entry a row; coverage counted |

```text
theorum/142_panini_kernel_theorem.md
proof_lab/panini_kernel.py
proof_lab/test_panini_kernel.py
proof_lab/PANINI_KERNEL_EXPECTED.sha256
```

## Theorem 143 tiṅ rule-table engine XI — the open lane closed: 5,373 / 5,373 packet

| Field | Value |
|---|---|
| Certificate class | tiṅ rule-table engine XI — the open lane closed: 5,373 / 5,373 |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | laṅ / loṭ / vidhiliṅ of classes 2–10 on the independent generator's cells, 5,373 / 5,373 (from 5,223), with nine new rows and the apṛkta attribution corrected to 6.1.68 — PROVED on the suite (908 / 908), DECLARED on the lane; the 8.2.74 ru branch, 8.4.56's jaś branch, 8.4.65, 7.1.35's tāt, 7.3.95's īṭ recorded as options, not claimed |

```text
theorum/143_ting_rule_table_engine_open_lane_closed_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 144 tiṅ rule-table engine XII — the Dhātupāṭha pinned and the ārdhadhātuka lane: lṛṭ, luṭ, āśīrliṅ of every declared root, 1,845 / 1,854 each packet

| Field | Value |
|---|---|
| Certificate class | tiṅ rule-table engine XII — the Dhātupāṭha pinned and the ārdhadhātuka lane: lṛṭ, luṭ, āśīrliṅ of every declared root, 1,845 / 1,854 each |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | the Dhātupāṭha (ashtadhyayi.com's list, 2,259 records, pinned) as the ground of 7.2.10; lṛṭ / luṭ / āśīrliṅ of all 194 declared (root, pada) on the generator's cells, 1,845 / 1,854 each (daridrā's nine: a vārttika, not claimed) — PROVED on the suite (908 / 908), DECLARED on the lane; liṭ 514 / 1,849, luṅ 1,042 / 1,854, lṛṅ 0 / 1,854 reported as the next baseline |

```text
theorum/144_ting_rule_table_engine_ardhadhatuka_lane_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 145 tiṅ rule-table engine XIII — liṭ at breadth (1,799 / 1,849) and lṛṅ (1,845 / 1,854) packet

| Field | Value |
|---|---|
| Certificate class | tiṅ rule-table engine XIII — liṭ at breadth (1,799 / 1,849) and lṛṅ (1,845 / 1,854) |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | liṭ of all 194 declared (root, pada) on the generator's cells, 1,799 / 1,849, from 25 new rows (3.4.81, the periphrastic 3.1.35–40, the vowel-initial abhyāsa, 6.1.17, 6.4.120–123, 7.4.11, 7.1.34, 6.4.64 …); lṛṅ 1,845 / 1,854 as the ṅit sya-lakāra — PROVED on the suite (908 / 908), DECLARED on the lane; the 50 liṭ cells left named (jakṣ, stubh, stṛ, ūrṇu, i-thal); luṅ 1,077 / 1,854 the next baseline |

```text
theorum/145_ting_rule_table_engine_lit_breadth_lrn_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 146 tiṅ rule-table engine XIV — luṅ at breadth, 1,854 / 1,854: the kartari tiṅanta closed on the lane packet

| Field | Value |
|---|---|
| Certificate class | tiṅ rule-table engine XIV — luṅ at breadth, 1,854 / 1,854: the kartari tiṅanta closed on the lane |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | luṅ of all 194 declared (root, pada) on the generator's cells, 1,854 / 1,854, from the cli substitutes as rows (sic, aṅ, ksa, caṅ, the luk of 2.4.77) with the vṛddhi, iṭ and kit rules of the sic (7.2.1–7.2.5, 7.2.72–73, 1.2.11–12, 1.2.17, 8.2.25–28) — PROVED on the suite (908 / 908), DECLARED on the lane; with it every lakāra of the kartari tiṅanta stands on the lane: 5,373 / 5,373 present, 1,845 / 1,854 ×4, 1,799 / 1,849 liṭ, 1,854 / 1,854 luṅ |

```text
theorum/146_ting_rule_table_engine_lun_breadth_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Theorem 147 tiṅ rule-table engine XV — the karmaṇi: the passive present system of every declared root, 6,912 / 6,948 packet

| Field | Value |
|---|---|
| Certificate class | tiṅ rule-table engine XV — the karmaṇi: the passive present system of every declared root, 6,912 / 6,948 |
| Status | `PASS_TING_RULE_TABLE_ENGINE_CANDIDATE` |
| Canonical result SHA-256 | `5d304194769dbc0d3f87b196a7d3589b3afd18e184a69f1037118daef1800ed9` |
| Boundary | the karmaṇi prayoga on the same table: laṭ / laṅ / loṭ / vidhiliṅ of all 193 declared roots in the passive, 6,912 / 6,948 on the generator's cells (daridrā's 36 a vārttika's), from 3.1.67 yak as a kit vikaraṇa row, 1.3.13, the kit-y rows of āśīrliṅ generalised through one predicate, 7.4.22, 6.4.44 — PROVED on the suite (908 / 908), DECLARED on the lane |

```text
theorum/147_ting_rule_table_engine_karmani_theorem.md
proof_lab/ting_rule_table_engine.py
proof_lab/test_ting_rule_table_engine.py
proof_lab/TING_RULE_TABLE_ENGINE_EXPECTED.sha256
```

## Consolidated parallel-lineage index

| Lineage | Canonical surface | Recorded status |
|---|---|---|
| Morphic Recognition | `theorum/morphic_recognition/` (MR-01–MR-07) | general proofs plus separate source-pinned finite contracts; executable calibration is not universal formal proof |
| Recognition Topology | `theorum/recognition_topology/` (RT-01–RT-04) | bounded topological theorems and explicit non-claims |
| Singularity Calculus | `theorum/singularity_calculus/` (SC-01–SC-18) | `RNKE_VERIFIED_SINGULARITY_THEORY_V5_WITH_EXCLUSIONS` |
| Stratified Recognition | `theorum/stratified_recognition/` (SR-01–SR-04) | `RNKE_VERIFIED_STRATIFIED_RECOGNITION_LINEAR_CORE` |
| Morphic Algebra | `theorum/morphic_algebra/` | `RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`; full manuscript certification false |
| Morphic Calculus | `theorum/morphic_calculus/` | `RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`; full manuscript certification false |
| Morphic Operator Geometry | `theorum/morphic_geometry/` | `RNKE_VERIFIED_WITH_OPEN_OBLIGATIONS`; audited corrections and rejected overclaims retained |

## MR-04–MR-07 memory certificate

- Scope and proof route: [Memory development](theorum/morphic_recognition/MEMORY_DEVELOPMENT.md).
- Actual run evidence: [Verification record](theorum/morphic_recognition/MEMORY_VERIFICATION.md).
- Finite evidence: [Certificate](theorum/morphic_recognition/MEMORY_CERTIFICATE.json).
- Immutable-input specification: [Source manifest](theorum/morphic_recognition/MEMORY_SOURCE_MANIFEST.json).
- Internal review: [Development review](theorum/morphic_recognition/DEVELOPMENT_REVIEW.md).
- Reproduce: `python3.12 -m proof_lab.morphic_recognition.certify_memory --check-archive`.

Formal proof-assistant and external peer-review status remain `NOT CLAIMED`.

## Earlier consolidation regression record

On the 2026-09-12 pre-publish consolidated tree, Python 3.12 compilation and complete unittest discovery reported `Ran 344 tests` and `OK`. This is an operational regression result, not an independent proof of every manuscript statement. See `theorum/BRANCH_CONSOLIDATION_AUDIT.md` for graph ancestry, merge provenance, and the hosted-CI boundary.

## 1 November 2026 integrated research evidence

The [integration audit](research-history/PENDING_WORK_2026_11_01.md) records fresh
local checks separately from the imported historical certificates.

| Packet | Evidence and scope |
|---|---|
| R3 structure report | [Finite certificate](research/structure_report/RESULT.json), [mutation controls](research/structure_report/MUTATIONS.json) |
| R4 declared-pairing repair | [Finite certificate](research/structure_report/r4/RESULT.json), [mutation controls](research/structure_report/r4/MUTATIONS.json) |
| SS1 complementary signals | [Finite evidence](research/sectoral_signal/RESULT.json) |
| Source-energy SE1–SE49 | [Paper certificate table](papers/rkf_completed_weil_endpoint/CERTIFICATE_TABLE.md), [current SE49 scope](papers/rkf_completed_weil_endpoint/development/SE49_SCOPE.md) |
| Lambda-counting continuation | [Stage index](research/lambda_counting/INDEX.md) |

SE49's archived V_24 result remains a finite complete-source subspace statement.
All-order positivity, global eta zero, K0 and RH remain open. The later-stage
numerical campaigns were imported with their source bytes and history intact;
this integration does not claim a fresh execution of every campaign.
