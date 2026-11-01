# SP–VT measurement and signal packet

This applies the user's SP/VT arrow-overlap observation to an explicit
complementary measurement model. The main concrete result is stable
two-channel recovery through a singular output-response chart. The complete
signal also has an exact compatible/incompatible decomposition; coherent
sensor error can remain invisible to its consistency residual.

Read [the theorem and scope](THEOREM.md). Run from the repository root:

```sh
node research/sectoral_signal/verify.cjs --check
```

The verifier imports the existing canonical cut-scalar engine without
modifying it. [RESULT.json](RESULT.json) and [EXPECTED.sha256](EXPECTED.sha256)
bind the declared finite controls and source files. `--write` initializes
new evidence only and refuses to replace existing result/pin files.
Neither a finite PASS nor this inverse-chart repair proves RH or a physical
mass gap. The application source and detector calibration remain explicit
inputs. See [validation status](VALIDATION.md) for actual repository gates.
