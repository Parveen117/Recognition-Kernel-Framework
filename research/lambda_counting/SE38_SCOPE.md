# SE38 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. The observer records its relative reading Delta=x-c and its
calibration record: the bank U_alpha=Lambda c^alpha, or the labelled
packet Lambda^(w+s) c. Each decoder reads only those records and the
formulas derived from the supplied catalogue, then predicts the readings
after catalogue words, which are compared with the recorded ones.
Replay and source records document the readings; they are not
independent certification conditions.

| Assertion | Scope of the written proof |
| --- | --- |
| Monomial calibration algebra | Theorem 1: membership in A_D is exactly (SE38.5); (SE38.6) gives the expression without division by Lambda |
| Degree/unit-order rule | Theorem 2: (SE38.9) is necessary and sufficient for relative coefficients in A_D; substitution preserves A_D; the closed observer (SE38.10) works at every depth; D_* of (SE38.13) |
| Least bank for a monomial action | Theorem 3: B_(w,d) with the closed formulas (SE38.15) is least and needs d generators |
| Actual cut of the memory algebra | Theorem 4: the induced filtration quotient (SE38.20) with dimension (SE38.21), distinct from A_D/Lambda^(q+1)A_D |
| Calibration depth | Theorem 5: the lift-independent update (SE38.25) from Lambda^(w+s)c needs c only through depth q-w-s, and this bound is sharp (SE38.27) |

Five written derivation groups establish the general results. The
executable records 25 exact checks, including 8 negative controls. It
uses canonical exact fractions arranged by retained unit degree and the
pinned SE36 polynomial response layer unchanged; readings are archived
as counting states. It is a counting-specific application, not a second
shared engine.

The saved observer certificates are:

- A two-coordinate catalogue of three affine-cut actions with D_*=2:
  from the five calibration readings Lambda c^alpha and Delta at depth
  three, the closed observer predicts the relative reading and the whole
  calibration bank after five words up to length six.
- The ordered quadratic and cubic actions with the bank (Lambda c,
  Lambda c^2): the readings after g3 g2 and g2 g3, whose difference is
  (SE38.18) at Lambda^2.
- A three-action scalar catalogue with common order w=1 and relative
  order s=1 at depth five: from Lambda^2 c and Delta the observer
  predicts the relative readings after five words up to length seven.

A final check re-decodes every archived certificate from its saved JSON.

Further positive checks cover the membership criterion and its
expression for (n,D)=(1,2),(2,1),(2,2),(2,3) on every monomial through
degree 3D and unit degree four; the relation a^2=Lambda b; D_*=2 for the
catalogue, failing at D=1; preservation of A_D by substitution and by an
affine frame change and its inverse; identical formulas at depths four
and two with commuting reductions; (SE38.15) for three monomial actions;
d independent first-layer memories with vanishing products for four
(w,d) pairs; the repaired cubic update (SE38.16) and preservation of
a^2=Lambda b; the dimension (SE38.21) for four (n,D,q) cases computed
from products of generators; lift independence for three lifts at three
(q,s) pairs; omitted c_2 and c_3 at q=3, s=1; and no calibration below
the combined order.

Negative controls cover a cut-level calibration outside A_D; the cubic
relative coefficient outside A_1; refusal of a nonlinear cut action;
Lambda c outside the least bank for w=d=2; the cut quotient differing
from the Lambda-multiple quotient; a labelled record with low unit
coefficients; sharpness of the depth bound for four (q,w,s) cases; and a
relative reading below its declared order.

The coefficient shift is the inverse of the labelled embedding
R_(q-k) -> Lambda^k R_q, not an inverse of Lambda on R_q, and recovers
no unavailable coefficient. Leastness concerns the declared monomial
family and same-carrier polynomial generators, not the minimum number
of measurements or a minimum over all observers. An absolute target can
need more calibration than its relative transport. No noisy-data,
conditioning, acquisition-cost or numerical-unit claim is made.

Zero remains the stated typed cut; coordinate nulls are separately typed
additive neutrals. No primitive metric, RH, Yang--Mills or curvature
result is asserted. Binomial expansion, monomial independence and
coefficient shifts carry no claim of novelty priority. Formal
proof-assistant verification and external review are not claimed.

Reproduction uses Python 3.12 and Node v22.22.0:

```bash
node proof_lab/lambda_calibration_depth.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE38 source manifest. The whole-engine command result is
recorded in the source record.
