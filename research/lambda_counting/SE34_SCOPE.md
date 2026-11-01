# SE34 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. The observer reads the joint banks of the operation F, the
bank of a supplied cut inverse G_0 where a theorem uses one, and the
target state y. Each decoder consumes only those serialized readings
and returns the source. Replay and source records document the readings;
they are not independent mathematical certification conditions.

The [SE34 derivations](SE34_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY.md) are
pinned unchanged by the SE35 manifest. Their opening status line predates
this certificate; this scope and the chapter index record its issue.

| Assertion | Scope of the written proof |
| --- | --- |
| Dependency order | Theorem 1: on a finite sector, an acyclic dependency graph read from the bank gives a polynomial inverse; every valid order gives the same inverse; relabelling transports graph and equations |
| Positive-memory feedback | Theorem 2: if every cycle has positive unit weight, (SE34.7) reaches the unique retained fixed point within s(q+1) updates, and within 1+L_q; the inverse response is the finite geometric sum (SE34.9) |
| Cut-inverse lifting | Theorem 3: a supplied cut inverse G_0 lifts through every retained unit depth by (SE34.14); the nth iterate is exact through degree n |
| Residual decoding | Theorem 4: the next residual coefficient, transported by the cut response inverse, is the next source coefficient (SE34.21); the ordered inverse response (SE34.22) doubles the residual order (SE34.23) |
| Frame transport | (SE34.24): supplied coordinate changes transport the cut inverse and the lifted solution |

Four written derivations establish the general results. The executable
records 29 exact checks, including 11 negative controls, using unchanged
canonical rational-cut arithmetic, expression normalization, the SE33
joint-bank reader and the pinned SE35 bank construction. It is a
counting-specific application, not a second shared engine.

The saved observer certificates are:

- The labels 0, 2, 5 example: the dependency graph read from the bank,
  the recovery order 0, 5, 2 and the unit-valued source (SE34.6).
- The two-label feedback cycle (SE34.10): the weighted graph, the update
  bounds and the iteration trace to the series (SE34.11) through Lambda^3.
- The raising inverse of I-Lambda X at p_0 through unit depth five,
  with support growing to p_5 (SE34.17).
- The self-return x-Lambda x^2=1 through unit depth six, giving
  1, 1, 2, 5, 14, 42, 132 (SE34.19).
- The self-cycle -x+Lambda x^3 lifted from the supplied cut inverse -y,
  where the graph condition fails.
- Residual-layer decoding of the self-return, one coefficient per step.
- Order doubling on the feedback cycle through unit depth seven.
- Frame transport of the feedback cycle by two supplied linear changes.

A final check re-decodes every archived certificate from its saved JSON
and compares it with the stored decoded state.

Further positive checks cover two-sided inversion on rational and
unit-valued states; three valid orders on a four-label example;
relabelling; seeds independent of the result; the walk bound 2q+2 for
q=0..4; nilpotence of the response and both geometric inverse identities;
agreement of the lift with the feedback fixed point and with
G(F(z))=z; residual decoding on all three regular examples; the
worked doubling example with residual orders 1, 3 and its stated states;
and at most ceil(log_2(q+1)) corrections for q=0, 1, 3, 7.

Negative controls cover the increasing label order (refused, and
misdecoding when forced); rejection of the same bank by SE33's
fixed-order lowering condition; absence of a finite-support preimage
for I-X; one update before the walk bound; a zero-weight cycle (refused
and non-injective); an iterate one layer short; a wrong, branching or
unit-dependent cut inverse; the null cut Lambda x; the numerical unit
value Lambda=1 for (1-Lambda)x; residual updates without the cut
response inverse; and reversed operator order in (SE34.22).

The cut inverse is a supplied composition inverse. The decoder checks it
at the target cut and refuses an inconsistent one; it does not infer an
inverse from a Jacobian or choose a branch. Statements are on retained
unit quotients. No convergence after substituting a nonzero numerical
unit value, finite-support inversion on an infinite acyclic graph, noisy
data recovery or complexity bound is asserted.

Zero remains the stated typed cut. Coordinate nulls are separately typed
additive neutrals. No primitive metric, analytic derivative, RH result
or curvature development is asserted. Triangular inversion, formal
inverse lifting and order doubling carry no claim of novelty priority.
Formal proof-assistant verification and external review are not claimed.

Reproduction uses Python 3.12 and Node v22.22.0:

```bash
node proof_lab/lambda_unit_memory_lifting.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE34 source manifest. The whole-engine command result is
recorded in the source record.
