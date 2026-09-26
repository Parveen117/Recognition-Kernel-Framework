# Clock-Free Cut-Memory Stage 1

## Branch

```text
agent/cut-memory-spectral-isomorphism
```

## Pull the branch in an existing clone

```bash
git fetch origin
git switch agent/cut-memory-spectral-isomorphism
git pull --ff-only origin agent/cut-memory-spectral-isomorphism
```

If the branch does not yet exist locally:

```bash
git fetch origin
git switch -c agent/cut-memory-spectral-isomorphism --track origin/agent/cut-memory-spectral-isomorphism
```

## Stage-1 dry execution

The generalized implementation has been written but no pass is claimed yet.
Run:

```bash
python -m proof_lab.clock_free_cut_memory_general_example \
  --output proof_lab/CLOCK_FREE_CUT_MEMORY_STAGE1_ACTUAL.json
```

Expected status if the implementation is coherent:

```text
PASS_CLOCK_FREE_CUT_MEMORY_GENERAL_EXAMPLE_STAGE1
```

The formal test suite belongs to Stage 2 and is intentionally not claimed in
Stage 1.
