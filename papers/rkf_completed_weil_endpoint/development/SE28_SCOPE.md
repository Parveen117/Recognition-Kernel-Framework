# SE28 scope and verification

12 October 2026. Owner: Monty.

| Statement | Status and scope |
| --- | --- |
| Circle/sheet numbers | Written reversible representation for real-valued readings in the admitted chart; integer turns retained |
| Whole cut line | Both opposite rays have retained side labels; cut and unit changes preserve the decoded reading |
| Zero-unit fibre | Normalized data extend to zero in the resolved packet; raw zero alone loses them |
| TVSP flat coordinate | r=(I_th-1)/(I_th+1) is derived from the existing corrected tetrad ratio |
| Native phase adapter | Declared Cayley phase is unitary and equals one exactly at scalar flat closure |
| Infinite zeta specialization | Z_r(s)=sum chi_r^Omega(n)/n^s, with Z_0=zeta on Re(s)>1, using supplied arithmetic primes and log(p) |
| Prime-power signal | The logarithmic derivative has coefficient chi_r^k log(p) at p^k; the flat member recovers von Mangoldt weights |
| Full RH source transport | Written unitary theorem retains Gamma, every prime event, the pole, all residuals and the native graph norm |
| Best global source bound | Inherited SE27 eta=1079/2000, native floor 1/492000; no smaller anchor here |
| Fixed-state zero-unit limit | Weak zero, no strong zero limit; information escapes every fixed finite set of sheets |
| Full-curvature flatness equivalent to RH | Not established |
| Derivation of arithmetic primes or canonical log(p) from TVSP | Not established |
| Universal physical measurement unit | Not established |
| Analytic continuation of every twisted family member | Not established |
| Eta zero, K0 attachment and RH | Open |

There are seven written theorems. Their general algebraic, unitary,
convergence and limit arguments are separate from finite controls.
The exact native application has 28 checks including eight negative
controls. The Python application has 11 checks including three negative
controls. It verifies all nine mixed entries of the actual SE27 event Gram
at three circle calibrations using exact head-plus-infinite-tail identities;
the actual Gamma-blind pole pairing remains 45607/433125. Eighteen
prime-power translations have outward-enclosed logarithmic carries.
Finite Euler coefficient controls run through integer 256 and 54 primes;
the infinite identity follows from the written absolute-convergence proof.

The controls reject phase-only aliasing, deleting the cut-line side,
division by a zero unit, automatic flatness of a collapsed tetrad,
discarded sheet tails, independent periodicity on each sheet, ambiguous
cut crossings, treating a twisted arithmetic family as a rechart, and
inferring source sign from reference flatness. They do not claim to
verify arbitrary physical constitutive laws.

Reproduction uses Python 3.12.14 and Node v24.19.0:

```bash
python -m proof_lab.endpoint_circular_calibration_certificate --check
python -m unittest proof_lab.test_mathematics_index -v
node operator_foundation/verify_all.cjs --check
```

The fresh read-only replay reproduced the complete archived JSON exactly,
passed all 39 scoped checks and verified 78 source pins. All eight mathematics
navigation tests passed. Every one of the 15 imported runtime Python modules
is pinned. The 72 inherited pinned blobs were checked against the published
SE27 parent and match it exactly. Final publication also checks every expected
blob and preserves all parent blobs outside the four navigation updates.

SE27's global numerical archive and source pins are reused unchanged;
its expensive full interval replay is not rerun because calibration is
proved to transport the same source. No new numerical global certificate
is claimed by the finite circle tests.

The required unchanged engine gate was executed and reproduced its inherited
first-suite mismatch: expected
`f8ae27c1c6e776cf4a9e0a50ebc984b3574466bc2466628609fcf53de27fd6e6`,
actual
`35a9efc5ef96e6a3b88546011b99c0f9a386441db81c3a47da8109445428d79e`.
No engine pin was changed, and later suites did not execute after that
failure. Scoped direct canonical arithmetic and path controls pass;
whole-engine PASS is not claimed. No proof-assistant or external review
is asserted. Standard covering, unitary rechart, Cayley and Euler-product
identities are not claimed as new mathematics in isolation.
