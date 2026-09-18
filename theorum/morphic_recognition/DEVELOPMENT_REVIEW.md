# MR-04–MR-07 Internal Development Review

Review date: 2026-09-18.

**Outcome: no remaining blocking finding in the inspected, declared finite
scope.** This is an internal AI review of statements, proofs, implementations,
and certificate coverage. It is not external independent review, a proof-assistant
verification, or an assessment establishing novelty or priority.

The review did not rerun tests or generate a certificate. Final execution
results, source pins, and archive reproduction belong to
[MEMORY_VERIFICATION.md](MEMORY_VERIFICATION.md),
[MEMORY_SOURCE_MANIFEST.json](MEMORY_SOURCE_MANIFEST.json), and
[MEMORY_CERTIFICATE.json](MEMORY_CERTIFICATE.json). A successful internal review
does not substitute for those separate checks.

## Reviewed mathematical scope

| Capsule | Quantified result inspected | Essential restriction |
|---|---|---|
| [MR-04](04_future_complete_linear_recognition.md) | Finite row-space closure, invariant future-blind Cut, unique quotient dynamics, minimum linear Smriti, bounded-length distinguishing continuation | Total linear actions; whole declared finite-dimensional carrier; linear observation channels |
| [MR-05](05_seam_memory_gluing.md) | Simultaneous typed backward closure, compatible quotient edges, nodewise minimum memory, one-seam rank deficit | Finite typed graph; total linear edges; node and edge identity retained; no state-dependent guards |
| [MR-06](06_guarded_lopa_future_equivalence.md) | Coarsest guarded behavioral quotient, minimum number of retained states, lawful Lopa, shortest distinguishing word | Finite deterministic partial rules; both admissibility and outputs are part of the target |
| [MR-07](07_holonomy_area_scaling.md) | Explicit repeated-loop error bound, fixed-area limit, fixed-edge collapse to identity | Finite matrices; submultiplicative norm; uniform declared cubic remainder bound |

MR-04's stationary row-space identity justifies every finite future word; a
word sample is not used to prove the universal assertion. Each strict round
increases dimension, giving the stated horizon and the separate final equality
check. Its minimum counts linear channels, not arbitrary encodings or states
on one selected orbit. The baseline observation is included before saturation,
so the minimally repaired observation has an invariant kernel and supports
updates. Redundant stored coordinates only give uniqueness on their image.

MR-05's simultaneous recurrence pulls back terminal observations in the correct
chronological order. Its global dimension sum bounds strict rounds even with
cycles. The one-seam formula fixes the target observation; the capsule correctly
refuses to turn it into a one-pass network algorithm. Graph gluing here means
compatible induced transitions, not a smooth manifold quotient, path independence,
or commuting cycles.

MR-06 preserves the language of enabled continuations as well as final outputs.
Including every prefix also preserves intermediate observations. Its minimum is
a behavioral class count, distinct from MR-04/05's channel rank. The proof and
implementation separate an information-sufficient retained record from one whose
extra labels themselves admit deterministic updates. The pair search queues
disabled-side terminals rather than returning them prematurely; this preserves
the shortest-witness assertion when another pair at the same depth has a shorter
output distinction.

MR-07's noncommutative telescoping identity and exponential-series bound yield
the stated norm estimates. The scale is `n h^2`: `h=sqrt(tau/n)` retains area,
whereas `h=T/n` gives the identity limit. The exact shear polynomial, its
determinant-one identity, and the `22/27` wrong-scaling separation are consistent
with the proofs. Nonzero commutator alone does not imply a nonidentity exponential
at every chosen area; the capsule explicitly retains this limitation.

## Findings and resolutions

| Finding | Resolution inspected | Status |
|---|---|---|
| Early MR-04/MR-05 executable check IDs described different obligations from the theorem capsules; some named negative controls were absent | `verify_memory_contract()` now emits the capsule's ten MR-04 and ten MR-05 checks, including action-order, parallel-edge, and guarded-input refusal controls. The package verifier independently compares manifest IDs with IDs declared in the theorem files before accepting emitted results | Resolved |
| A directly fabricated `MemoryClosure` with empty maps could pass vacuously for a nonempty edgeless graph | `MemoryClosure.verify()` now checks exact node/edge coverage, dimensions, record counts and indices, initial ranks, history endpoints, and per-node growth before algebraic identities. A regression case supplies the previously vacuous object | Resolved |
| Total-edge linear closure must not silently accept a state-dependent guard | `TypedGraph` explicitly refuses an edge carrying a guard. Guarded partial rules are handled separately by MR-06. Graph inputs are copied and exposed through immutable mappings | Resolved |
| Present-output preservation could be mistaken for future faithfulness | Shear and delayed-shift witnesses retain the enabling distinction; the proofs use saturated future rows or complete finite behavioral equivalence | Resolved in stated scope |
| Historical Morphic Calculus uses incorrect fixed-edge holonomy accumulation scaling | MR-07 is an explicit normative erratum; the historical source remains preserved and the incorrect inference is superseded | Resolved for the named scaling passage |
| Neighboring Euler-step BCH and symmetric-step formulas omit separate Euler truncation terms | MR-07 explicitly excludes those formulas from its proof and certification. Their correction remains outside this package | Open, explicitly excluded; not a blocker for MR-07 |

## Implementation and certificate review

The rational implementation retains original future-response rows and their
actual typed paths, rather than attaching arbitrary words to row-reduced linear
combinations. Output factorization, edge intertwining, and row provenance jointly
give a checkable certificate of the constructed future response space. Rank on
the baseline observation's kernel supplies an additional check of the memory
count. The implementation covers rational data; the ordinary proofs separately
state their field hypotheses.

The guarded implementation compares partition refinement with a separate pair
search on its declared finite calibration collection and replays returned
witnesses. This supports the implementation contract without converting that
collection into a proof over every finite grammar. Observations must have the
declared equality semantics; unrestricted natural-language meanings are not
inferred.

The source verifier requires the complete expected source set, checks file
hashes, matches manifest obligations against theorem-declared obligations, and
rejects missing, duplicate, empty, or failed emitted checks. Archive checking
compares the regenerated packet with the archived packet. The hash is content
binding, not mathematical authority or a signature proving trusted authorship;
the reviewed source manifest remains part of the trust input.

## Boundaries retained after review

No result here identifies differential rank loss with exact information loss,
memory dimension with curvature, or a quotient set with a smooth space. Smooth
and singular gluing, nonlinear or infinite-dimensional minimum memory, noisy
measurement guarantees, a physical TVSP adapter, and whole-manuscript
certification remain outside the package. RH and Yang–Mills endpoint gates are
unchanged. The finite constructions have established mathematical antecedents;
this review does not make a broad novelty assertion.
