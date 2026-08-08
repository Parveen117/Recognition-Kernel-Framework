# RT-03 - Principal-Holonomy Blindness and Lifted Branch-Memory Theorem

## 1. Lift and projection

Let the lifted abelian holonomy phase be
\[
\Phi\in\mathbb R.
\]

The principal \(U(1)\) holonomy is
\[
\boxed{
q(\Phi)=e^{-i\Phi}.
}
\]

## 2. Theorem - exact blindness kernel

For \(\Phi,\Phi'\in\mathbb R\),
\[
q(\Phi)=q(\Phi')
\]
if and only if
\[
\boxed{
\Phi'-\Phi\in2\pi\mathbb Z.
}
\]

Therefore
\[
\boxed{
\ker q=2\pi\mathbb Z.
}
\]

### Proof

\[
e^{-i\Phi}=e^{-i\Phi'}
\]
is equivalent to
\[
e^{-i(\Phi'-\Phi)}=1.
\]

The real solutions are exactly
\[
\Phi'-\Phi=2\pi n,
\qquad
n\in\mathbb Z.
\]
QED.

## 3. Corollary - integer winding is invisible to terminal principal holonomy

If a lifted loop phase satisfies
\[
\Phi=2\pi\nu,
\qquad
\nu\in\mathbb Z,
\]
then
\[
\boxed{
q(\Phi)=1
}
\]
for every integer \(\nu\).

Thus the terminal group element alone cannot distinguish
\[
\nu=0,\pm1,\pm2,\ldots.
\]

A statement of the form
\[
H(C)=e^{2\pi i\nu}
\]
therefore describes a projection that **forgets** integer winding; it is not an
injective encoding of the winding sector.

## 4. Branch repair

Choose a principal phase
\[
\theta\in(-\pi,\pi]
\]
for \(q(\Phi)\).

Then every lift is
\[
\boxed{
\Phi=\theta+2\pi k,
\qquad
k\in\mathbb Z.
}
\]

The pair
\[
(\theta,k)
\]
recovers the lifted scalar phase exactly.

Hence, in the scalar \(U(1)\) case, a branch integer is sufficient to repair
the blindness of principal phase to the real lift.

This does not claim that one integer repairs a general nonabelian or
multi-eigenchannel target. Those settings require the full projectors/branch
labels or a separately proved faithful observer.

## 5. Recognition-faithfulness form

If the target \(\Pi\) distinguishes lifts differing by \(2\pi n\), while the
observer records only \(q(\Phi)\), then
\[
\ker q\not\subseteq\ker\Pi.
\]

The observer is therefore target-blind in exactly the sense of the framework's
minimal-observer and path-blindness theorems.

The lawful repair is not to deny the collision. It is to retain sufficient
lift/path/branch memory.

## 6. Relation to existing lambda geometry

The existing lambda-geometry archive already contains stronger concrete
witnesses:

- terminal principal holonomy equal to the identity;
- nonzero lifted curvature flux;
- integer branch memory retained by the recognition ledger.

RT-03 extracts the domain-independent quotient theorem behind those examples.

## 7. Claim status

```text
PRINCIPAL U(1) HOLONOMY KERNEL 2pi Z       PROVED
INTEGER WINDING INVISIBLE AT TERMINAL U(1) PROVED
SCALAR BRANCH-INTEGER REPAIR               PROVED
TARGET-BLINDNESS INTERPRETATION            PROVED GIVEN DECLARED TARGET
GENERAL NONABELIAN MINIMAL REPAIR COUNT    NOT CLAIMED HERE
```
