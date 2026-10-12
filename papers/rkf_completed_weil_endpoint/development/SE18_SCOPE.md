# SE18 scope and verification record

12 October 2026. Owner: Monty. Written stage under the 10 October
verification preference: written proofs and only the direct checks
needed for the changed claims; no replay, certificate, test suite or
regenerated archive.

| Result | Evidence | Scope |
| --- | --- | --- |
| Floor functional eta_pw | SE18.2; affine slope 1+z^6-L_Gamma>0 | Fixed comparison weights; certifiable eta set is [eta_pw,1) |
| SE17 anchor tight | SE18.3; archive cells at x in [0.008,0.012], [0.495,0.500], [0.580,0.583] | eta_pw(SE17 weights)>=0.58938; no fourth anchor without new weights |
| Exterior floor | SE18.4; L_Gamma(0)=0, V_alpha(0)=0 | Every constant-pole comparison needs eta>=b_c=1/10 |
| Pole budget law | SE18.5--SE18.7; weighted Cauchy--Schwarz, equality case | tau certifies the pole iff 4 int v^2/tau<=1; convex set; q_0 row saturates it |
| Row band | SE18.8--SE18.9; exact polynomial (z-1)(3z^5+3z^4+3z^3-5z^2-5z+3) | tau_0 exceeds b_c(1-z^6) only on z in (0.48277,0.86415), by at most 0.00765 |
| Cut-point floor | SE18.10--SE18.11; certified masses p_{5/2}, p_{11/2} | SE17 weights force eta>=0.5784 at x=0; inside SE14's radius 0.84 |
| Translate charging | SE18.12 | For every weight, max{V_q(0),V_q(log 2)}>=0.245 |
| Exterior decay | SE18.13--SE18.16; Lambda(n)<=log n and integral tests only | Phi_ext(e^{-A/2})=O(A e^{-A/2}); support-exterior f certified from SE17.11 alone |
| Hybrid criterion | Theorem 6; SE13.I17 and SE15 section 6 consumed | eta-zero convergence iff eta_loc(A_j) -> 0 on apertures A_j -> infinity |

## Direct checks

All numbers in section 7 of the theorem note were computed from the
SE17 archive proof_lab/ENDPOINT_WEIGHT_FAMILY_RESULT.json at commit
2e556a1a (exact rationals for L_Gamma and its polynomial; the archive's
90-digit outward prime masses; exact fractions for <v,q_0> and the pole
budget; bisection to 2^-60 for the band roots; the regenerated 604-entry
Lambda catalogue through 4096 for the prime-row ratio on [1/20,1/2]).
The regenerated catalogue was used only to illustrate the looseness of
(SE18.13); no certified number depends on it.

## Not run

```text
proof_lab replays (SE15--SE17)        not rerun; archives byte-preserved
Python test suites                    not rerun
node operator_foundation/verify_all   not run (known Node pin mismatch unchanged)
Lean                                  not applicable
```

Reported as such. No source pin, archive, proof or certificate was
modified. The branch adds one theorem note, this scope record, one
source record and four navigation edits.

## Boundary

Nothing below 59/100 is certified. The local radius remains 21/25.
Eta=1/2, the cofinal eta-zero sign, global critical contractivity, the
historical five-label endpoint, K0 and RH remain open. The pole row
tau_0 is not substituted into any certified stage here; its band cost
exceeds SE17's spatial floor and belongs to an executable stage with a
shaped admissible density or a larger anchor on the band.

See the [theorems](SE18_FLOORS_OF_THE_POINTWISE_ROUTE_AND_HYBRID_MECHANISM.md)
and [sources](SE18_SOURCE_RECORD.md).
