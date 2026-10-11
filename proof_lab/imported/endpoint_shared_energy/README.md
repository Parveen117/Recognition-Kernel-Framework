# Pinned T21 profile for the SE1 shared-energy replay

`T21_PROFILE.b64` is the concatenation, with one terminal newline, of the
seven `NW3_6_T21_PROFILE.partXX.b64` files in
`Parveen117/RH-Framework`, branch `agent/native-w3-kernel-faithfulness`,
commit `c2a05268279f701f265cbb29f1bb0995ac0924e7`,
directory `gpt_lab/native_w3_kernel/`.

It decodes to an XZ stream containing the original 19,344-byte binary
profile. No profile entry has been changed. The upstream manifest is
copied as `UPSTREAM_PROFILE_PINS.json`; it records MP PR 278, the exact
source and export commits, Actions artifact provenance, and the hashes
of the original seven parts.

| Item | SHA-256 |
| --- | --- |
| XZ stream | `63b5f8ed67fe8bba606e1486b98279c8ff2976dd7f8831f2de00294c7ccac95b` |
| Binary profile | `0cf54e6f8e2d30e4d03f70f5826d47972c3a8c698d730d358dca8b5b7e3fcc02` |

The big-endian binary format is: 8-byte magic `NW3T21P1`; 20-byte MP
source commit; 20-byte export commit; 32-byte original artifact ZIP hash;
32-byte internal profile hash; two unsigned 32-bit counts (2,400 cells,
78,734 events); binary64 near-zero slope; binary64 far floor; 2,401
binary64 source floors.

The mesh width is exactly `1/200`. Cell zero uses the quadratic seam
floor with coefficient half the stored near-zero slope. Cells 1 through
2399 use their left-endpoint stored floors on the whole interval.
The terminal floor at 12 is retained for integrity; the replay uses the
weaker supplied far floor beyond 12. The upstream floor on [12,13] is
also greater than that far floor.

These entries are treated as exact representations of supplied outward
outputs, not exact identities for analytic constants. The local replay
checks byte integrity and performs exact rational accumulation. It does
not regenerate the upstream Arb inequalities, reconstruct event phases,
or establish attachment of this profile to the debt-paid source.

See the [SE1 proof and boundary](../../../papers/rkf_completed_weil_endpoint/development/SE1_SHARED_ENERGY_BUDGET.md)
and [replay](../../endpoint_shared_energy_budget.py).
