# SE29 scope and verification

12 October 2026. Owner: Monty.

| Assertion | Evidence and scope |
| --- | --- |
| Exact source attachment | Theorem 1; actual SE5 source, bounded invertible normalization, retained native metric |
| Reciprocal curvature blindness | Theorem 2; complete curvature identical at T and T^(-1), diagonal reversed |
| Infinite countermodels | Written diagonal constructions with stable mismatch, essential threshold and compact excess; no RH arithmetic |
| Actual essential curvature | Theorem 3; SE5's actual weakly escaping sequence proves norms 1/2 for F and 1/4 for its accepted Gram |
| Recovery of the missing diagonal | Theorems 1 and 4; full projector reading or curvature plus the strict negative-sector projection |
| Positive sign of the recovered actual diagonal | Unproved |
| Curvature flatness equivalent to RH | Not established; this particular source attachment has unavoidable nonzero curvature |
| New smaller eta or global eta zero | None |
| Best inherited global bound | SE27: S_b+(1079/2000)I_X >= (1/492000)I_X |
| Unique physical TVSP connection | Not claimed |
| RH, historical K0 attachment, formal verification, external review | Not proved or certified by this stage |

The four written theorems contain the infinite-dimensional arguments.
The application uses the unchanged canonical exact cut and matrix engine
for 20 checks, including seven negative controls. These cover reciprocal
aliasing, loss of the diagonal sign through a positive square root,
nonzero curvature at unit gain, a zero-gain degeneracy, the shifted native
metric, a later unobserved negative sector and rejection of a negative
square-root branch. Sixty-four sampled modes check the exact formulas of
the infinite countermodels; their limits and compactness are proved in
the note, not inferred from those samples.

A noncommuting N,T example checks the order in the source congruence and
retains a negative witness. Gauge controls transport both the reference
and the readout. No actual RH negative vector is produced. The verifier
checks SE28's inherited source pins and reads SE27's preserved global
archive; the 63496-cell global computation is not rerun.

Reproduction uses Python 3.12.14 and Node v24.19.0:

```bash
node proof_lab/endpoint_curvature_diagonal.cjs --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The source pins bind the exact application, result, written proofs and
consumed repository inputs. The finite result is separate from the four
universal written arguments. All prior theorem and numerical certificate
files remain unchanged; only the four navigation surfaces are updated.
No canonical engine source or pin is changed.

The read-only replay reproduced the archived JSON byte for byte, passed
all 20 scoped checks and verified 87 source pins. The eight mathematics
navigation tests passed. Publication checks also compare every inherited
pinned blob to the parent tree and preserve every non-navigation parent
blob. The new packet contains six files and four navigation updates.

The unchanged whole-engine gate was run and failed at its inherited first
suite, `tests/verify.cjs --check`, with expected hash
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`
and actual hash
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`.
The later suites did not execute. No pin was changed to suppress that
failure; scoped direct arithmetic checks pass, while a whole-engine PASS
is not claimed.
