# SE19 verification scope and endpoint boundary

12 October 2026. Written development after review of published SE18.

## Results and hypotheses

| Result | Evidence | Boundary |
| --- | --- | --- |
| Exact source with unbudgeted pole | SE19.1--SE19.2; cancellation in SE17.11 | Same corrected odd source and graph norm |
| Best pole test below a fixed diagonal W | Theorem 1; weighted Cauchy--Schwarz and equality vector | Bounded W>=w>0; comparison criterion, not full-source necessity |
| Application at the existing anchor | Theorem 2, using SE17's existing Q floor and SE15's exact pole integral | Reuses eta=59/100; does not lower it |
| Actual residual analysis | Theorem 3; complete Gamma and prime squared differences | Bounded integrated observations, not unlicensed point samples |
| Finite full-Gram recovery | Theorem 4; inverse identity and native norm conversion | W floor and beta_n<=1 must be established for each proposed eta |
| Exact gain and blindness | Theorem 5; gain zero iff C A_n^(-1)v=0 | Fixed eta/weights; newly added event coordinates must be orthogonal to the old ones |
| Observation limit | Theorem 5; strong convergence and uniform inverse floor | Limit is the retained bounded-residual comparison; no eta-zero limit proved |
| Best next observation | Theorem 6; positive-energy quotient | Ideal maximizer not computed; finite candidate-space rule supplied |
| SE18 corrections | SE19.A1--SE19.A7 and direct source comparison | Unsupported floor and finite-aperture gluing withdrawn; qualitative core-density limit retained |

The two-dimensional examples are exact algebra controls for informative
and blind observations and for missed coupling. They are not instances
of the arithmetic source and do not establish an RH inequality.

## Verification record

- Read all three SE18 development files and its four navigation updates
  at parent commit `2d2809ae9fcc5c6463ff499dfaa52d63f34533e9`.
- Matched all 1,194 parent Git blobs before edits.
- Checked the factor 4 in the half-line pole, the z-integral Jacobian,
  the Gamma factor 1/2, and the complete prime residual coefficient
  directly against SE15--SE17.
- Checked the inverse identities by multiplication and the optimization
  by its equality direction; included explicit coercivity and density.
- Checked the exact C_16 rational sum and the polynomial subtraction
  directly. No sample-grid extremum is used as a continuum proof.
- New numerical pole/Gram evaluation, finer eta search, aperture replay,
  new test suite and certificate generation: deferred under the user's
  theory-first instruction. Formal proof assistant and external review:
  not performed.
- Documentation checks: all changed-file links, the sixteen SE19 tags
  and seven audit tags passed; the existing eight mathematics-navigation
  tests passed under Python 3.12.14. These are documentation checks,
  not a new arithmetic-source test suite.
- The 1,190 untouched parent blobs, including every earlier development
  file, archive and source pin, matched after edits. Only four existing
  navigation files are modified; four SE19 documents are added.
- Shared engine gate: not rerun in this written stage. The engine is
  unchanged, and routine numerical/engine replay is deferred under the
  user's theory-first instruction. No current engine PASS is claimed;
  SE17's separately reported gate failure is not overwritten or repaired
  by changing its pins.

## Current frontier

```text
global executed anchor eta=59/100, native floor 1/7380       UNCHANGED (SE17)
implied nonnegative shift 10883/18450                       UNCHANGED (SE17)
positive local aperture 21/25                              UNCHANGED (SE14)
new smaller-eta W floor and complete recovered pole Gram    NOT EVALUATED
SE18 claimed eta_pw>=0.58938 / anchor tightness              WITHDRAWN
SE18 finite-aperture max-only global conclusion             WITHDRAWN
cofinal eta-zero sign; eta=1/2; critical global recovery     OPEN
historical five-label attachment; K0; RH                    OPEN
```

No progress percentage, new exact spectral edge, universal weight
optimizer or unconditional convergence to eta zero is claimed.
The new inverse proof requires a positive seed; it cannot be continued
to a singular seed by notation alone. See the
[theorem](SE19_RETAINED_RESIDUAL_POLE_RECOVERY.md),
[audit](SE19_SE18_AUDIT.md), and [sources](SE19_SOURCE_RECORD.md).
