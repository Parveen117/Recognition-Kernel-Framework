# Śulba — Baudhāyana's Constructions as Measure-Residues (flat / memory-closed)

Owner's note (Vedic repo, *VRG_Sulba_Invariant_Geometry_v1*): a construction
r is **flat** when `Res = Rec(Measure(r(X))) − Rec(Measure(X)) = 0`, and
**memory-closed** when Res ≠ 0 but is stored exactly as Smṛti. Everything here
is rational arithmetic; √2 is never evaluated — the text's own cord is used.

## T1 Diagonal theorem (BŚS 1.48) — FLAT
d² − a² − b² = 0 on the triples the text names (1.49): 3-4-5, 12-5-13,
15-8-17, 7-24-25, 12-35-37, 15-36-39. Each is a rational point (a/d, b/d) of
the native circle — an instance of F00E Thm 5.4, Cos² + Sin² = 1.

## T2 The √2 cord (BŚS 2.12) — MEMORY-CLOSED
1 + 1/3 + 1/(3·4) − 1/(3·4·34) = **577/408**; Smṛti = (577/408)² − 2 =
**1/166464** exactly; 577² − 2·408² = 1 (Pell unit, verified by arithmetic and
native Euclid — no continued-fraction theory imported). Control: three terms
(17/12) leave Smṛti 1/144 — the text's last correction shrinks the residue
by a factor **1156**.

## T3 Area transfers
- square → rectangle (2.1–2.4): residue 0, FLAT.
- rectangle → square by gnomon (2.5): `big² − small² = p·q` exactly — the
  leftover small square is the diagonal Bindu in difference-of-squares form. FLAT.
- square → circle (2.9) → square (2.10, side = d·9785/11136): the round trip is
  an exact rational, side/a = 1 + **41/13630464**; the text's implied circle
  constant is **5992704/1940449** (≈ 3.0883, float for display only).
  MEMORY-CLOSED with the Smṛti recorded.

## T4 Classification
```text
diagonal 1.48 · square→rectangle · gnomon 2.5         FLAT
√2 cord 2.12 · square→circle→square 2.9/2.10          MEMORY-CLOSED (Smṛti exact)
```

## Certificate
```text
python proof_lab/sulba_measure_residue.py
python -m unittest proof_lab.test_sulba_measure_residue -v
```
`PASS_SULBA_MEASURE_RESIDUE_CANDIDATE`, SHA-256 `8f9db340d011dbc0f035570f9c7a33ef51a02aa367f77bf84f0fbb2ef0d0da37`.

## Claim boundary
```text
DIAGONAL BINDU = 0 ON THE TEXT'S TRIPLES; RATIONAL POINTS OF THE NATIVE CIRCLE   PROVED
√2 CORD 577/408, SMṚTI 1/166464, PELL UNIT; CORRECTION FACTOR 1156               PROVED
AREA TRANSFERS FLAT; CIRCLE ROUND TRIP MEMORY-CLOSED WITH EXACT SMṚTI           PROVED
GENERAL DIAGONAL THEOREM; OPTIMALITY OF THE CIRCLE RULE                          NOT CLAIMED
RH, YM                                                                           UNTOUCHED
```
