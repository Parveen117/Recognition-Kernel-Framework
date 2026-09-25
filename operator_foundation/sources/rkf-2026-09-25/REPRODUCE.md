# Reproduce the Certificate Campaign

## Requirements

```text
Python 3.11 or later
Git
standard-library execution for the implemented packages
```

No ordinary floating-point proof margin is used in the F00/F00-E package. The F00-G/H/I package uses exact integer and rational arithmetic with explicit rational interval and tail obligations.

## Clean-clone run

```bash
git clone https://github.com/Parveen117/Recognition-Kernel-Framework.git
cd Recognition-Kernel-Framework
python certificates/foundation/run_campaign.py \
  --output certificates/foundation/campaign_result_reproduced.json
```

Expected terminal status:

```text
PASS_IMPLEMENTED_FOUNDATION_CERTIFICATE_CAMPAIGN
F00GHI_LOG_ARITHMETIC_ZETA_V0_1 PASS_F00GHI_LOG_ARITHMETIC_ZETA_AUDIT 0
F00_F00E_EULER_V0_1 PASS_F00_F00E_RIGOROUS_COMPUTATIONAL_AUDIT 0
```

Expected process exit code:

```text
0
```

## Jupyter run

```python
from pathlib import Path
import json
import os
import subprocess
import sys

repo = Path.cwd()
env = os.environ.copy()
env["PYTHONINTMAXSTRDIGITS"] = "0"

run = subprocess.run(
    [
        sys.executable,
        "certificates/foundation/run_campaign.py",
        "--output",
        "certificates/foundation/campaign_result_reproduced.json",
    ],
    cwd=repo,
    text=True,
    capture_output=True,
    env=env,
)

print(run.stdout)
print(run.stderr)
print("RETURN CODE:", run.returncode)
assert run.returncode == 0
```

## Compare statuses

```python
archived = json.loads(
    (repo / "certificates/foundation/campaign_result.json")
    .read_text(encoding="utf-8")
)

reproduced = json.loads(
    (repo / "certificates/foundation/campaign_result_reproduced.json")
    .read_text(encoding="utf-8")
)

print("ARCHIVED:", archived["status"])
print("REPRODUCED:", reproduced["status"])

assert archived["status"] == reproduced["status"]

archived_packages = {
    item["package"]: item["reported_status"]
    for item in archived["packages"]
}
reproduced_packages = {
    item["package"]: item["reported_status"]
    for item in reproduced["packages"]
}

assert archived_packages == reproduced_packages
print("PACKAGE STATUSES MATCH")
```

## Hash note

A campaign summary includes captured stdout and result-file hashes. The archived canonical summary SHA is:

```text
8728ab0319afe5fb6e6329deaee479cfa93f50bb4422ee863aaaf4f911dd9582
```

A clean reproduction should produce the same mathematical statuses and package results. If a platform-dependent field causes a different campaign-summary hash, report the exact differing field rather than silently replacing the archived artifact.

## Direct package runs

```bash
python certificates/foundation/F00_F00E_EULER_V0_1/verify.py \
  --output certificates/foundation/F00_F00E_EULER_V0_1/result_reproduced.json

python certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/verify.py \
  --output certificates/foundation/F00GHI_LOG_ARITHMETIC_ZETA_V0_1/result_reproduced.json
```

## Failure handling

Do not weaken an obligation merely to recover a PASS.

On failure:

```text
record the failing obligation;
confirm source pins;
separate infrastructure defects from mathematical defects;
repair the theorem or verifier as appropriate;
version the package if certified source or obligation semantics change;
rerun from a clean checkout.
```
