/-
  LEAN-RKF-4: theorum/62 T2 — vibration from silence is the Euler circular system.
  For the odd generator D = ω·R (R² = −I on the EMK 2×2 real carrier), the depth-4 exponential jet
      24 · Σ_{k≤4} t^k D^k / k!   =   (24 − 12 ω²t² + ω⁴t⁴)·I  +  (24 ωt − 4 ω³t³)·R
  i.e. Exp(tD) = Cos(ωt)·I + Sin(ωt)·D/ω exactly at jet depth 4 (F00E Thm 5.3), for ALL integers ω, t.
  Scaled by 24 = 4! so that every coefficient is an integer; core Lean 4, no Mathlib.
-/

structure M2 where
  a : Int
  b : Int
  c : Int
  d : Int
deriving DecidableEq, Repr

def M2.add (x y : M2) : M2 := ⟨x.a + y.a, x.b + y.b, x.c + y.c, x.d + y.d⟩
def M2.mul (x y : M2) : M2 := ⟨x.a*y.a + x.b*y.c, x.a*y.b + x.b*y.d, x.c*y.a + x.d*y.c, x.c*y.b + x.d*y.d⟩
def M2.smul (k : Int) (x : M2) : M2 := ⟨k*x.a, k*x.b, k*x.c, k*x.d⟩
def I2 : M2 := ⟨1, 0, 0, 1⟩
def R : M2 := ⟨0, -1, 1, 0⟩

theorem R_sq : R.mul R = M2.smul (-1) I2 := by decide

/-- 24·(I + tD + t²D²/2 + t³D³/6 + t⁴D⁴/24) with D = ωR, written with integer weights 24,24,12,4,1 -/
def expJet24 (ω t : Int) : M2 :=
  let D := M2.smul (ω*t) R
  (((M2.smul 24 I2).add (M2.smul 24 D)).add (M2.smul 12 (D.mul D))).add
    ((M2.smul 4 ((D.mul D).mul D)).add (((D.mul D).mul D).mul D))

def cos24 (ω t : Int) : Int := 24 - 12*(ω*t)*(ω*t) + (ω*t)*(ω*t)*(ω*t)*(ω*t)
def sin24 (ω t : Int) : Int := 24*(ω*t) - 4*(ω*t)*(ω*t)*(ω*t)

theorem circular_system (ω t : Int) :
    expJet24 ω t = (M2.smul (cos24 ω t) I2).add (M2.smul (sin24 ω t) R) := by
  simp only [expJet24, cos24, sin24, M2.add, M2.mul, M2.smul, I2, R]
  simp only [M2.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [Int.mul_zero, Int.zero_mul, Int.add_zero, Int.zero_add, Int.mul_one, Int.one_mul,
               Int.neg_mul, Int.mul_neg, Int.neg_neg, Int.sub_eq_add_neg, Int.neg_add, Int.mul_add,
               Int.add_mul, Int.mul_assoc, Int.mul_comm, Int.mul_left_comm, Int.add_comm, Int.add_left_comm, Int.add_assoc] <;>
    omega

/-- control: a nilpotent odd generator N (N² = 0) has jet I + tN only -- no oscillation -/
def N : M2 := ⟨0, 1, 0, 0⟩
theorem nilpotent_no_oscillation (t : Int) :
    let D := M2.smul t N
    (((M2.smul 24 I2).add (M2.smul 24 D)).add (M2.smul 12 (D.mul D))).add
      ((M2.smul 4 ((D.mul D).mul D)).add (((D.mul D).mul D).mul D))
      = (M2.smul 24 I2).add (M2.smul (24*t) N) := by
  intro D
  simp only [D, M2.add, M2.mul, M2.smul, I2, N]
  simp only [M2.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp only [Int.mul_zero, Int.zero_mul, Int.add_zero, Int.zero_add, Int.mul_one, Int.one_mul] <;> omega
