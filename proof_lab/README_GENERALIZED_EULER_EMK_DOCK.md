# Generalized Euler / EMK Dock (theorum/55)

Binds theorum/51's exchange law to the EMK/DE RK transport: R = even flow
generator (commutator inside channels), iota K = odd flow generator
(channel exchange), [R,K] = 2RK = leading loop residue of composing the two
flows, and EMK-1's Delta_par + Delta_perp = theorum/53's flow invariant with
the two channels exchanging. GE false-residue prevention as a verdict.

```bash
python proof_lab/generalized_euler_emk_dock.py
python -m unittest proof_lab.test_generalized_euler_emk_dock -v
```
Pin in `GENERALIZED_EULER_EMK_DOCK_EXPECTED.sha256`.
