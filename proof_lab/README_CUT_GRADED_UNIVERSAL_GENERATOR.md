# Cut-Graded Universal Generator Candidate

This stage applies the Recognition-Kernel cut calculus to the uploaded
universal-generator manuscript without promoting its unsupported identities.

## Added

```text
theorum/41_cut_graded_universal_generator_theorem.md
proof_lab/cut_graded_universal_generator.py
proof_lab/test_cut_graded_universal_generator.py
proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_EXPECTED.sha256
proof_lab/README_CUT_GRADED_UNIVERSAL_GENERATOR.md
```

## Jupyter run

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch agent/cut-graded-universal-generator
!git pull --ff-only origin agent/cut-graded-universal-generator

!python -m unittest -v proof_lab.test_cut_graded_universal_generator

!python -m proof_lab.cut_graded_universal_generator \
    --output proof_lab/CUT_GRADED_UNIVERSAL_GENERATOR_ACTUAL.json
```

Expected:

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

## Hash check

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

## Important boundary

A passing exact certificate validates the finite rational theorem packet and
its negative controls. It does not yet identify the uploaded coordinate vector
field with a closed physical universal generator. The central manuscript
theorem is updated only after the user run and hash are reported.
