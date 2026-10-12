# SE35 scope and verification

12 October 2026. Owner: Monty.

The certificate is the saved observer reading decoded for its stated
target. The observer applies labelled translations h to the same
unknown input, measures F(x+h)-F(c+h) against its calibration c, and
records those measurements. Each decoder reads only the archived
measurements, the declared symmetric kernel banks and the calibration.
Replay and source records document those readings; they are not
independent mathematical certification conditions or permission gates.

| Assertion | Scope of the written proof |
| --- | --- |
| Translation-blind subspace | Theorem 1: K_F is the common kernel of the contraction banks of a polynomial response with symmetric kernels on a finite counting sector |
| Fibres of all translated readings | Equal translated readings exactly when the difference lies in K_F; the probe grid {0,...,d-1}^n determines the response polynomial in h |
| Descending decoder | Theorem 2: recovered order banks (SE35.9)-(SE35.11) and the section give x-hat with x-x-hat in K_F |
| Target recovery | Theorem 3: A(x-c) is readable exactly when K_F lies in ker A; rank(A restricted to K_F) extra linear channels are necessary and attained |
| Singular-cut repair | Theorem 4: a completed observation with identity cut admits the unit-memory update (SE35.21) |
| Calibration and frame | Section 7: the moving-calibration identity (SE35.26) and transport K_F -> U K_F with transported probes (SE35.27) |

Four written derivations establish the general results. The executable
records 36 exact checks, including 14 negative controls, using
unchanged canonical rational-cut arithmetic, expression normalization
and the SE33 joint-bank reader. It is a counting-specific application,
not a second shared engine.

The saved observer certificates are:

- The cubic-plus-linear response F(u,v)=u^3+v: nine translated
  readings on the grid {0,1,2}^2, decoded exactly to the input.
- A three-label, two-output mixed response of degree three with a
  one-dimensional blind line: 27 translated readings, the recovered
  order banks, and the decoded representative of the blind coset.
- The same response with the minimum supplementary linear channel
  (one channel): 27 readings decoded to the whole input.
- The square response with a moving calibration: four readings
  Q(x+h), Q(x-h), Q(c+h), Q(c-h) at two probes, decoded to x-c.
- The deformed square F=u^2+Lambda u^3: the completed observation and
  its unit-memory update trace through depth four.
- The augmented pair (u^2+Lambda u^3, v) with a Lambda-layer input,
  recovered through depth three.

A final check re-decodes every archived certificate from its saved JSON
and compares it with the stored decoded state.

Further positive checks cover symmetric bank construction against direct
evaluation; the blind line and invariance along it; calibration movement;
off-grid interpolation and grid oversampling; the second difference 6u
and residual v; the marked probe reading the componentwise square in two
whole-vector readings; target recoverability for A=u+w versus A=u;
minimum repair channels for the mixed and u^2 examples; a cut-blind
direction visible at the first unit layer; the deformed-square closed
form (SE35.24) and series (SE35.25) through Lambda^2; calibration
independence when K_F is null; and frame transport of the blind
subspace, target rank and readings.

Negative controls cover a non-symmetric bank, the invisible
antisymmetric ordered part, the raw square fibre {x,-x}, an
understated degree bound, the highest-order bank alone missing v,
omitted or duplicated probe rows, the zero probe, a channel missing the
blind line, further u-only readings not revealing v, the singular raw
square cut, one update too few, an inconsistent bank whose candidate
fails its forward readings, a wrong calibration label and untransported
probes. The displayed finite ranges do not stand in for the written
proofs.

Theorem 4's lifting is replayed directly by the update (SE35.21) on the
saved completed observation. The general SE34 lifting theorem it cites
remains a written derivation; no SE34 certificate is issued here. The
lifted decoder evaluates the declared kernel banks at its own candidates;
the unknown source enters only through the observer's readings.

The statements require the declared ability to read F(x+h). Degree
bounds are declared construction properties, never inferred from
samples. No recovery from a passive single reading, unknown operation
or degree, unknown infinite counting state, arbitrary nonlinear
invertibility, noisy-data stability, restricted-observer recovery or
uniform minimality over nonlinear encodings is asserted.

Zero remains the stated typed cut. Coordinate nulls are separately
typed additive neutrals. No primitive metric, analytic derivative,
RH result or curvature development is asserted. Finite differences,
polarization, linear quotient decoding and formal inverse lifting
carry no claim of novelty priority. Formal proof-assistant
verification and external review are not claimed.

Reproduction uses Python 3.12 and Node v22.22.0:

```bash
node proof_lab/lambda_active_readings.cjs --check
node proof_lab/lambda_joint_readings.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

Read-only application replay reproduces the JSON archive byte for byte
and checks the SE35 source manifest. The whole-engine command result
is recorded in the source record.
