# Dabas-Euler / EMK Dock (theorum/55)

Binds theorum/51's exchange law to the EMK/DE RK transport: R = even flow
generator (commutator inside channels), iota K = odd flow generator
(channel exchange), [R,K] = 2RK = leading loop residue of composing the two
flows, and EMK-1's Delta_par + Delta_perp = theorum/53's flow invariant with
the two channels exchanging. DE false-residue prevention as a verdict.

```bash
python proof_lab/dabas_euler_emk_dock.py
python -m unittest proof_lab.test_dabas_euler_emk_dock -v
```
Pin in `DABAS_EULER_EMK_DOCK_EXPECTED.sha256`.
