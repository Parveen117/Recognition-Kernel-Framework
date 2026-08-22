# Lean kernel witnesses (channel I2 — second lineage)

Core Lean 4 (v4.12.0), **no Mathlib**. These files are checked by the Lean
kernel, which does not execute any Python: they are the first statements of
the 50–73 ladder verified outside the repo's own certification lineage.

| File | Theorem | Statement | Kernel status |
|---|---|---|---|
| `CommutatorSupport.lean` | LEAN-RKF-1 (theorum/61 T2/T3) | on the gam+śap+tip word carrier (16 states, 7 sūtras, memory carried): column support of every rule commutator equals the listed set; every conflict set is empty; the only nonzero commutators are the enabling pairs chaḥ→tuk, tuk→ścutva | accepted by `decide`; depends on no axioms |
| `ExchangeLaw.lean` | LEAN-RKF-2 (theorum/51 T2) | for **all** integer entries: D = B + ιA (B antisym, A sym) is anti-self-dagger, and D†S + SD = ([R,B] + [A,T]) + ι([T,B] + [R,A]) on the 2×2 C_Σ carrier | accepted; axioms: propext, Quot.sound (Lean's standard) |

Controls (not committed, reproduced in the build log): a planted wrong
support list and a planted wrong-sign exchange law are both rejected by the
kernel.

Reproduce:
```text
curl -sL -o lean.tar.zst https://github.com/leanprover/lean4/releases/download/v4.12.0/lean-4.12.0-linux.tar.zst
tar --zstd -xf lean.tar.zst && export PATH=$PWD/lean-4.12.0-linux/bin:$PATH
lean lean/CommutatorSupport.lean && lean lean/ExchangeLaw.lean
```
The tables in `CommutatorSupport.lean` are exported from
`proof_lab/rewrite_rules_as_cut_module_operators.py`; the Lean file re-derives
the supports from the tables — what is trusted from Python is only the
*realization table*, and `test_lean_tables.py` pins that export.

Not yet in Lean: everything else in 50–73. Each row added here moves a
statement from PROVED (finite certificate, one lineage) to KERNEL-CHECKED.
