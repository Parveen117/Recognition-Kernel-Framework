# Local-to-Uniform Seam Gap (theorum/49)

Turns locality into uniformity inside the framework's own cut algebra:
faces with a declared sup-weight `W`, recognized mean `f0` and memory
contraction `lambda` (certified by theorum/41's exact cut-square criterion)
multiply to a product whose memory sheet contracts by
`rho = max W*lambda/f0` for **every** number of faces `m`.  The global
recognition cut is `J_rec = 2 (x)P_i - I`, not the tensor cut `(x)J_i`
(certified separation).  Delivers theorum/28 Sec. 9's outward certificate
`u + e = rho < 1` uniformly in `m`; the infinite-face limit is NOT claimed.

## Reproduce

```bash
python proof_lab/local_to_uniform_seam_gap.py
python -m unittest proof_lab.test_local_to_uniform_seam_gap -v
```

Expected status: `PASS_LOCAL_TO_UNIFORM_SEAM_GAP_CANDIDATE`
Expected SHA-256: see `LOCAL_TO_UNIFORM_SEAM_GAP_EXPECTED.sha256`.
