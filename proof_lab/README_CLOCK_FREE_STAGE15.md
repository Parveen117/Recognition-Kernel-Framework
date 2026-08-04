# Clock-Free Cut-Memory Stage 1.5

Stage 1.5 tests the buried Recognition-Seam and morphic-calculus results before any RH specialization.

## Exact packet

```text
proof_lab/clock_free_cut_memory_stage15_examples.py
```

It contains five exact rational calibrations:

```text
E  recovered middle identity;
F  shadow-Cauchy versus recognition-Cauchy;
G  Madhava--Smriti finite recursion and exact tail;
H  morphic object stabilization across distinct paths;
I  recognition-complete five-memory limit.
```

No RH data, external clock, floating eigensolver, fitted correction, or post-hoc rank threshold is used.

## Run from Jupyter

```python
%cd "<LOCAL_PATH>/Recognition-Kernel-Framework"

!git fetch origin
!git switch main
!git pull --ff-only origin main

!python -m unittest -v proof_lab.test_clock_free_cut_memory_stage15

!python -m proof_lab.write_stage15_certificate \
    --output proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE15_ACTUAL.json
```

Expected terminal results:

```text
Ran 7 tests
OK
PASS_CLOCK_FREE_CUT_MEMORY_STAGE15
```

The dedicated writer uses canonical UTF-8 bytes with LF newlines, so Windows and Linux produce the same certificate file.

## Byte-level deterministic comparison

```python
from pathlib import Path

expected = Path("proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE15_EXPECTED.json").read_bytes()
actual = Path("proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE15_ACTUAL.json").read_bytes()
print("BYTE_STABLE", expected == actual)
```

Expected:

```text
BYTE_STABLE True
```

## Semantic diagnostic

When investigating an old certificate generated before the canonical writer was added:

```python
import json
from pathlib import Path

expected_obj = json.loads(
    Path("proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE15_EXPECTED.json").read_text(encoding="utf-8")
)
actual_obj = json.loads(
    Path("proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE15_ACTUAL.json").read_text(encoding="utf-8")
)
print("SEMANTIC_EQUAL", expected_obj == actual_obj)
```

A semantic pass with a byte failure indicates serialization or newline mismatch, not a theorem failure.

## Claim boundary

A pass certifies the generalized exact examples only. It does not certify a completed-Weil event lift, RH target faithfulness, completed-Weil positivity, or RH. The next stage begins only after the seven tests and byte-stable certificate comparison pass.
