# Odd-Channel Exchange Law (theorum/51)

Transport of theorum/50's odd channel under the generalized Euler flow with
an anti-self-dagger generator D = B + iota A (B antisymmetric, A symmetric).
Exact: the even generator B moves each channel of the cut square inside
itself, the odd generator A exchanges the channels (R <- [A,T], T <- [R,A]);
total cut-square energy is the invariant, channel energies are exchanged;
the odd channel is created from a turn-free square by the odd generator.
Exact rational Cayley inverse over C_Sigma, no Hilbert verdict (source-guarded).

```bash
python proof_lab/odd_channel_exchange_law.py
python -m unittest proof_lab.test_odd_channel_exchange_law -v
```
Pin in `ODD_CHANNEL_EXCHANGE_LAW_EXPECTED.sha256`.
