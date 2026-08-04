# Theorum 05: Transfer Boundary and Next Gate

## What has been moved here

The following MP-certified theorem packets now have clean Recognition Kernel Framework capsules:

```text
positive-eta UGD/amplitude-lift path equality;
seam-integer and common five-matrix reduction;
single-sector terminal reduction after source/even sign reduction;
exact M3 positivity and positive odd accepted block;
zero-cut T03 endpoint completion.
```

This folder is now the readable theorem surface. The MP repository should be treated as proof-lab history and implementation residue after these theorem capsules are transferred.

## What should not be reopened

```text
M3 positivity                       CLOSED
G3/M3 accepted odd block             CLOSED
positive-eta path equality           CLOSED
rank-at-most-five seam matrix        CLOSED AS REDUCTION
threshold holonomy/seam charge       CLOSED AS EQUIVALENCE
zero-cut T03 source-Gram endpoint    TRANSFERRED AS CERTIFIED SOURCE THEOREM
```

Reopening any of these would be mathematical archaeology for sport, which is apparently a hobby now, but not a proof strategy.

## Important chronological correction

Earlier PRs still state the full parity requirement:

```text
W3 >= 0 iff W3_even >= 0 and W3_odd >= 0.
```

That is true at the raw parity-split level.

Later seam-integer and T03 reductions change the terminal object. After the common pure-source sign, favorable even boundary and single-sector reduction, the even sector remains represented upstream but is not an independent terminal gate. The odd/five-label seam packet becomes terminal.

Correct wording:

```text
The even sector is retained by the bilateral carrier.
It becomes non-terminal only after the native seam-integer/source-sign/favorable-even reduction.
```

## Remaining work after transfer

There are two different continuation modes.

### Framework mode

Use the capsules as already proved theorem inputs. Continue from:

```text
T03 endpoint closure
-> formalize final theorem dependency graph
-> publication-quality normalization interface
-> reproducibility pointers.
```

### Proof-lab cleanup mode

After removing/moving theorem capsules from MP, inspect what remains in MP for:

```text
untransferred implementation scripts;
untransferred numerical packets;
duplicate manuscript surfaces;
old branches still carrying superseded claims;
source files needed only for reproducibility.
```

## Deletion discipline for MP

Theorems should be removed from MP only where they are duplicated as readable doctrine or manuscript theorem summaries. Executable provenance modules and raw validation packets should not be destroyed unless their contents are also copied, hashed or archived.

Safe deletion class:

```text
human-readable theorem capsules;
status summaries duplicated by this folder;
old manuscript theorem surfaces superseded by these capsules.
```

Unsafe deletion class:

```text
raw verifier scripts;
state capsules;
large numerical packets;
source audit scripts;
artifacts needed to regenerate the theorem evidence.
```

## Local rule going forward

Whenever a result is certified in MP and becomes part of the Recognition Kernel Framework, create one file here:

```text
theorum/NN_short_name.md
```

with:

```text
source PR;
objects;
statement;
proof skeleton;
numerical certificate if any;
claim boundary;
use in the framework.
```

Then MP can be cleaned by comparing against this folder instead of trusting a moving ledger. Ledgers are useful until they start impersonating reality.
