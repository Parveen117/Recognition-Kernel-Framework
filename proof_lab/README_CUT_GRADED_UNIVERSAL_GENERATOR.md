# Certified Cut-Graded Universal Generator

This stage applies the Recognition-Kernel cut calculus to the uploaded
universal-generator manuscript and replaces its unsupported identities by a
certified cut-graded theorem.

## Status

```text
user-local exact theorem suite      PASS
RKF proof-lab CI                    PASS
Recognition Kernel Review          PASS
central theorem                    CERTIFIED ON BRANCH
```

The user has reported the complete prescribed Jupyter run as passing. The local
console log and generated `CUT_GRADED_UNIVERSAL_GENERATOR_ACTUAL.json` are not
committed by this status update.

## Files

```text
theorum/41_cut_graded_universal_generator_theorem.md
proof_lab/cut_graded_universal_generator.py
proof_lab/test_cut_graded_universal_generator.py
proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_EXPECTED.sha256
proof_lab/README_CUT_GRADED_UNIVERSAL_GENERATOR.md
```

## Certified chain

```text
primitive involutive cut J
-> unique G_even + G_odd decomposition
-> bilateral exponential reconstruction
-> exponential cut-square identity
-> cut-loop memory coefficient
-> seam curvature [G_even,G_odd]
-> periodic / antiperiodic closure spectrum
-> clock-free Eye
-> target-faithful component observer.
```

## Reproduction command

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-graded-universal-generator
!git pull --ff-only origin agent/cut-graded-universal-generator

!python -m unittest -v proof_lab.test_cut_graded_universal_generator

!python -m proof_lab.cut_graded_universal_generator \
    --output proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_ACTUAL.json
```

Expected theorem packet:

```text
Ran 10 tests
OK

PASS_CUT_GRADED_UNIVERSAL_GENERATOR_CANDIDATE
CUT_DECOMPOSITION True
CUT_LOOP_MEMORY_CURVATURE True
BILATERAL_EXPONENTIAL_CUT_SQUARE True
CLOSURE_SPECTRUM True
CLOCK_FREE_EYE True
COMPONENT_OBSERVER True
CERTIFICATE_SHA256 34afc44543cd83cacd96cbced32b77f5fdd765c28fbaf81105d0d2063cf5f36e
```

## Hash verification

```python
from hashlib import sha256
from pathlib import Path

expected = Path(
    "proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_EXPECTED.sha256"
).read_text(encoding="ascii").strip()

actual = sha256(
    Path(
        "proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_ACTUAL.json"
    ).read_bytes()
).hexdigest()

print("HASH_STABLE", expected == actual)
print("EXPECTED", expected)
print("ACTUAL  ", actual)
```

Expected:

```text
HASH_STABLE True
```

## Claim boundary

A passing exact certificate validates the bounded finite rational theorem packet
and its negative controls. It does not identify the uploaded coordinate vector
field with a closed physical universal generator. The unbounded-domain theorem
still requires a declared carrier, invariant domain, closed generator and
lawful functional calculus.
