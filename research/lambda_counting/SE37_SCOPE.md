# SE37 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. The observer records the retained readings, relative readings
and calibration coordinate that the declared protocol supplies. Each
decoder reads only that record and the supplied updates and decoder
polynomials, then predicts later readings, which are compared with the
recorded ones. Replay and source records document the readings; they
are not independent certification conditions.

| Assertion | Scope of the written proof |
| --- | --- |
| Polynomial descent | Theorem 1: retained coordinates with decoder D and updates Phi_i satisfying (SE37.5) on the observation image give (SE37.6) after every word, in its actual order; an entry is deleted only with its reconstruction identity |
| Least target algebra | Theorem 2: closure of the target under the catalogue stabilizes within (SE37.12) and generates the least action-preserved algebra containing it |
| Calibration dependence | Theorem 3: the joint update (SE37.16); a calibration-free difference law exactly for affine updates (SE37.17); the one-step calibration signature (SE37.18) |
| Unit-scaled family | Theorem 4: the two-coordinate observer (Delta, Lambda c) has the exact polynomial update (SE37.21) for (SE37.19), before any truncation |

Four written derivation groups establish the general results. The
executable records 22 exact checks, including 7 negative controls. It
uses canonical exact fractions arranged by retained unit degree and the
pinned SE36 polynomial response layer unchanged; readings are archived
as counting states. It is a counting-specific application, not a second
shared engine.

The saved observer certificates are:

- The SE36 bank (x, Lambda x^2, Lambda^2 x^3) at q=2 reduced to one
  coordinate z=x with update z+Lambda z^2: from one recorded reading it
  predicts all three bank entries after 0, 1, 2, 5 and 12 repetitions.
- The swap-invariant target u+v kept by one coordinate with update z'=z,
  predicting every later target reading.
- The uniform relative observer at q=4 for a three-action catalogue
  (x+Lambda x^2; x+(2/3)Lambda x^2-5Lambda^2 x^3; x-(1/2)Lambda^3 x^4):
  from Delta and Lambda c it predicts the relative readings and the
  calibration coordinate after five words up to length eight.

A final check re-decodes every archived certificate from its saved JSON.

Further positive checks cover the reconstruction identities replacing
the linear update; word order for noncommuting actions; the closure
(1, u, v) forced by the future target u under (u,v)->(u+v,v); stage
bounds for three examples over Q and one over R_2; the exact moving and
held calibration updates; affine updates having calibration-free
increments while three nonlinear updates do not; the calibration
signature Lambda c at q=2; (SE37.21), (SE37.23) and (SE37.25) as
identities in Q[Lambda][x,c]; the repetition formula (SE37.24) for
N=0..10; discarding the last calibration coefficient c_2 at q=2 when
Delta and Lambda c are equal; and reduction from q=4 to q=2.

Negative controls cover x^2 and x^3 with v^2=u^3 but neither a
polynomial in the other; the nilpotent relation (Lambda x)^2=0 at q=1
with Lambda x nonzero; future target information lost by keeping only
u; Delta=1 from (1,0) and (2,1) with next readings 1+Lambda and
1+3Lambda; compressing a relative reading versus relative compression;
the action x+Lambda x^3 needing more calibration than (Lambda, Lambda c);
and refusal of a calibration coordinate with a nonzero cut part.

Leastness is inclusion of polynomial observation algebras, not a minimum
coordinate count, acquisition cost or noise-conditioning result. The
target is never added as a sensor; relation ideals keep their nilpotent
unit relations. Uniformity concerns the number and formula of the two
formal coordinates; their retained coefficients grow with depth. No
finite information at infinite depth, evaluation at a nonzero numerical
unit, closure for arbitrary polynomial actions or general nonlinear
recovery is asserted.

Zero remains the stated typed cut; coordinate nulls are separately typed
additive neutrals. No primitive metric, RH, eta or curvature result is
asserted. Polynomial substitution, invariant-span closure and coefficient
comparison carry no claim of novelty priority. Formal proof-assistant
verification and external review are not claimed.

Reproduction uses Python 3.12 and Node v22.22.0:

```bash
node proof_lab/lambda_target_algebra.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE37 source manifest. The whole-engine command result is
recorded in the source record.
