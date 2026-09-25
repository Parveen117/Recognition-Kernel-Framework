# Recognition Topology

This folder isolates the topological theorem layer that links winding, holonomy,
curvature transgression, branch memory, and Recognition seam events.

The primitive point is not that curvature automatically creates a topological
transition. The proved statement is sharper:

```text
continuous nonvanishing phase homotopy
        => winding sector is constant;

change of winding sector
        => the admitted nonvanishing/gapped carrier is exited somewhere.
```

That exit is the Recognition-topology seam event.

The folder deliberately separates four objects that are easy to conflate:

1. **winding / degree** - an integer homotopy invariant of a nonvanishing phase map;
2. **principal holonomy** - a group element that only remembers lifted phase modulo
   one full turn;
3. **lifted holonomy phase / branch memory** - the real lift or integer branch data
   needed when the target cares about winding history;
4. **curvature transgression** - the infinitesimal law governing how holonomy phase
   changes under a smooth loop deformation.

## Theorem chain

1. `01_winding_sector_stability_and_seam_event.md`
   proves homotopy invariance of winding and the necessity of a seam event for an
   integer sector change.

2. `02_abelian_holonomy_variation_transgression.md`
   proves, for a fixed abelian connection,
   \[
   \frac{d}{dt}\oint_{C_t}\omega
   =
   \oint_{C_t}\iota_{V_t}\Omega,
   \qquad \Omega=d\omega,
   \]
   and therefore identifies the holonomy-rate generator with curvature
   transgression under the declared sign convention.

3. `03_principal_holonomy_blindness_and_lifted_memory.md`
   proves that principal \(U(1)\) holonomy forgets integer branch memory:
   lifted phases differing by \(2\pi n\) have the same terminal holonomy.

4. `04_unitary_phase_crossing_and_sector_index.md`
   gives the safe finite-rank/scalar crossing statement: for a closed unitary phase
   path, the signed eigenphase crossing number equals its winding degree. It does
   **not** identify winding with spectral flow of the rate generator
   \(iU^{-1}\dot U\) without extra operator-family hypotheses.

## Existing framework dependencies

This layer does not replace the existing lambda-geometry results. It sharpens
their topological boundary:

- `thermodynamics/lambda_geometry/10_lambda_holonomy_and_branch_memory.md`
  already proves branch-memory classification and a finite declared
  winding/crossing result.
- `thermodynamics/lambda_geometry/15_curvature_flux_no_collapse.md`
  already proves that lifted curvature flux can survive even when principal
  holonomy is the identity.
- `thermodynamics/lambda_geometry/16_primitive_flux_spectrum_and_obstruction.md`
  already gives integer lifted-flux witnesses collapsed by principal holonomy.

The present folder extracts the domain-independent topological core.

## Claim boundary

```text
WINDING HOMOTOPY INVARIANCE                         PROVED
SECTOR CHANGE REQUIRES EXIT FROM NONVANISHING CLASS PROVED
ABELIAN HOLONOMY VARIATION / CURVATURE TRANSGRESSION PROVED
PRINCIPAL HOLONOMY BLINDNESS TO INTEGER LIFTS       PROVED
SCALAR UNITARY PHASE CROSSING = WINDING             PROVED

CURVATURE MAGNITUDE THRESHOLD => TOPOLOGICAL JUMP   NOT A THEOREM
MODEL-SPECIFIC ENTROPY/SKEW CONNECTION               NOT PROMOTED HERE
GENERIC NONABELIAN TRANSgression BY PLAIN LINE INTEGRAL NOT CLAIMED
SPECTRAL FLOW OF i U^{-1} UDOT = WINDING GENERICALLY NOT CLAIMED
PHYSICAL IDENTIFICATION OF A RECOGNITION SEAM       REQUIRES DOMAIN ADAPTER
```

The source notes that motivated this audit are retained only by source hashes in
`SOURCE_PROVENANCE.md`; personal naming from those notes is not used in this
repository surface.
