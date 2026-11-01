# SE46 proof scope and observer readings

13 October 2026 (Asia/Kolkata). Author: Monty.

## Written proof scope

[SE46](SE46_ORDERED_CELL_RECONSTRUCTION.md) proves six theorem groups:

1. Tree-normalized loop recovery, simultaneous moving-frame covariance,
   completeness up to vertex frames and independent chord targets in the
   unrestricted finite graph protocol.
2. Exact rectangular reconstruction from ordered, transported cell
   returns; equivalence to the full chord bank and discrete graph
   flatness. Equal individual cell conjugacy classes can still give
   different boundary traces.
3. Attachment to an actual constant-coefficient counting connection,
   the signed mixed-curvature coefficient and source-consistent
   subdivision of its boundary.
4. Formal logarithmic reconstruction through the first ordered
   commutator layer, with an explicit order-only word whose first
   detectable unit layer is twice the generator order.
5. Reconstruction in a supplied invertible memory lift and preservation
   under its forgetful projection, with a central-memory collision
   invisible to every projected edge reading.
6. General product-error telescoping, its unitary specialization,
   the connector-error contribution and a sound nonidentity decision.

The hypotheses travel with each theorem. A finite response graph, a
formal unit-memory carrier, a declared memory lift and an admitted normed
representation are different contracts. None is selected automatically
by Lambda or by the TVSP label. An arbitrary numerical matrix logarithm,
a physical metric and a continuum curvature field are not premises.

## Exact finite observer evidence

[ordered_cell_reconstruction.py](../../proof_lab/ordered_cell_reconstruction.py)
and [ORDERED_CELL_RECONSTRUCTION_RESULT.json](../../proof_lab/ORDERED_CELL_RECONSTRUCTION_RESULT.json)
record **35 exact controls, including 13 negative controls**:

- A 2 by 2 grid from the native count connection with C=E12, D=E21,
  steps a=1/3, b=1/2, and all twelve complete edge-reading packets.
  The decoded cells recover the four independent chords and the direct
  boundary. Missing channels/edges, inconsistent frames, missing
  connectors and wrong row order are detected.
- The same twelve edge readings in nine independently changed vertex
  frames. The aligned cells and boundary undergo the same root
  conjugation. A second spanning tree preserves the boundary with its
  own word, while an unrevised comb scan fails.
- Two complete 2 by 1 grids with face banks (A,B) and (A,A), for the
  stated conjugate unipotents. Every individual cell conjugacy class
  agrees, but the boundary traces are exactly 3 and 2.
- A 4 by 4 half-step grid with forty complete edge packets. Its sixteen
  aligned cells recover the original four-cell boundary. A planted
  refinement without consistent edge products changes the source.
- Formal unit series through degree 8, with generator order m=2. The
  exact logarithm retains the commutator correction. A closed word is
  invisible at depths below 4 and detected at depth 4; the actual
  forward count return has coefficient -4ab[E12,E21]. These particular
  depth claims are not universal bounds for all operator words.
- Two lifted 2 by 1 grids with full five-channel readings. Projected
  edge maps and projected identity boundaries coincide; the retained
  central integer is respectively 1 and 0.
- Rational three-channel unitary responses with return-reading error
  at most 1/40 and connector error at most 1/50. Exact positive-semidefinite
  inequalities establish a 13/200 aligned-factor bound and a 13/100
  two-factor bound. The measured residual exceeds that bound, certifying
  nonidentity. A separate nonunitary example checks product weights;
  a sub-budget nonidentity turn rejects the false converse.

All finite arithmetic is rational under Python 3.12. The probe decoder
uses serialized accepted and complementary readings. The read-only
check also independently decodes the saved grid banks and repeats their
cell-to-boundary identities. This is exact supplied observer evidence,
not physical detector validation or proof-assistant verification.

```bash
python3.12 -m proof_lab.ordered_cell_reconstruction --write
python3.12 -m proof_lab.ordered_cell_reconstruction --check
python3.12 -m proof_lab.tvsp_variable_jya --check
python3.12 -m proof_lab.ordered_return_feedback --check
python3.12 -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

## Execution record

- SE46 passes all 35 controls, including 13 negative controls. The 20
  local source pins and saved-archive replay match. All 15 inherited
  pinned source blobs also match the published parent commit.
- The unchanged SE45 and SE41 replays pass their 36 and 26 controls.
- All 8 mathematics-navigation tests pass.
- The required full-engine check was run and fails at
  `tests/verify.cjs --check` with the same inherited mismatch already
  recorded in SE41--SE45:

```text
expected f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6
actual   35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e
```

The shared engine, older sources and historical certificate pins were
not edited. A full-engine PASS is not claimed; source authentication,
general written proof, finite replay, formal verification and external
review are separate status layers.

## Unchanged boundaries

All identity cell returns imply identity on this supplied discrete graph,
not continuum flatness or absence of unrecorded turns inside an edge.
An identity boundary does not imply every cell is identity. A complete
matrix observation does not reconstruct memory discarded before the
matrix was acquired. Formal unit depth does not supply numerical
convergence or an unknown winding lift.

The independent chord count concerns an unrestricted matrix-valued edge
protocol, not every compression or sensor design. Observation-error
bounds are explicit assumptions and verified finite inputs, not inferred
from closure. This reconstruction does not prove global feedback
convergence for arbitrary nonunitary returns or unknown changing sources.

Zero remains the typed Cut; Lambda is not eta. The actual RH source is
unchanged: global eta 1079/2000 with floor 1/492000, eta zero on V_16,
and the universal source inequality still unproved. No Yang--Mills
mass-gap or universal physical TVSP geometry claim follows.
