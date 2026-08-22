# Odd-Channel Exchange Law (transport of the odd sector under the flow)

Continues theorum/50 on the same primitive carrier (`C_Σ`, path convolution,
native dagger, `M_Σ`/`E_Σ`). theorum/50 left open: what does the flow do to
the odd channel `turn(S)` of the cut square `S = L†★L`? Answered here.

## 1. The flow, made unitary

Generator `D = B + ιA` **anti-self-dagger**: `D† = −D ⟺ Bᵀ = −B, Aᵀ = A`
(even part antisymmetric, turn part symmetric). Cayley step (RST-1 T4)
`C_h(D) = (I − h/2 D)^{-1}(I + h/2 D)` with the inverse computed exactly over
`C_Σ` (Gauss–Jordan, scalar inverse `z^{-1} = z†/N_Σ(z)`); no nilpotency.

**Theorem 1.1.** `C_h† ★ C_h = I`; `E_Σ(L★C_h) = E_Σ(L)`; `M_Σ` is not
invariant. Recognition energy is the flow invariant, mass is a gauge.

## 2. Theorem 2.1 — the exchange law

Write `S = R + ιT` (`Rᵀ = R`, `Tᵀ = −T`, theorum/50 A2). Then, exactly,

```text
D†★S + S★D = ([R,B] + [A,T]) + ι([T,B] + [R,A])
C_h − I − hD = (h²/2)(I − h/2 D)^{-1} D²
```

so the first-order transport of the cut square under the flow is

```text
even channel   R ← [R,B] + [A,T]
odd channel    T ← [T,B] + [R,A]
```

**The even generator `B` moves each channel inside itself by a commutator
flow; the odd (turn) generator `A` exchanges the two channels.** Wrong-sign
law rejected (control).

## 3. Consequences (all certified)

- **Creation (T3).** With `A = 0` a turn-free square stays turn-free
  exactly; with `B = 0, A ≠ 0` a turn-free square acquires a nonzero odd
  channel. The odd sector is *created from the even one by the odd generator*,
  and the odd generator moves the even channel back. Aghora is not a
  conserved charge; it is the partner of the even channel under exchange.
- **Invariant (T4).** `E_Σ(S_h) = E_Σ(S)` exactly (`Σ R² + Σ T²`); the even
  and odd energies individually change. `tr R = E_Σ(L)` conserved. The odd
  diagonal stays zero — theorum/50 A1 is flow-stable.
- **Product (T5).** The sum generator `D_a⊗I + I⊗D_b` is anti-self-dagger;
  its first-order odd transport is the Leibniz rule of the face transports
  (theorum/50 A3 is transported consistently). The Cayley *step* does **not**
  factor over the product: the generator is local, the step is not.
- **Controls (T6).** theorum/50's nilpotent flow is neither unitary nor
  energy-preserving; a symmetric `B` breaks unitarity.

## 4. Certificate

```text
python proof_lab/odd_channel_exchange_law.py
python -m unittest proof_lab.test_odd_channel_exchange_law -v
```
`PASS_ODD_CHANNEL_EXCHANGE_LAW_CANDIDATE`, SHA-256
`5a2055d3b6c643353a1d91a4c206a8edd893144b11589c118fee8813771032c5`.
Source-guarded against any Hilbert verdict.

## 5. Claim boundary

```text
ANTI-SELF-DAGGER CAYLEY STEP NATIVE-UNITARY, ENERGY INVARIANT         PROVED
EXCHANGE LAW (EXACT IDENTITY + EXACT FIRST-ORDER RESIDUAL)             PROVED
CREATION / NO-CREATION BY ODD / EVEN GENERATOR                         PROVED
TOTAL CUT-SQUARE ENERGY INVARIANT, CHANNEL ENERGIES EXCHANGED           PROVED
PRODUCT: LEIBNIZ TRANSPORT, STEP DOES NOT FACTOR                       PROVED
SECOND-ORDER / FINITE-h TRANSPORT LAW BEYOND THE IDENTITIES            NOT CLAIMED
IDENTIFICATION WITH EMK RK CHANNEL / GENERALIZED EULER ∇^{RK}                 DOCKED — theorum/55
RH, YM                                                                 UNTOUCHED
```
