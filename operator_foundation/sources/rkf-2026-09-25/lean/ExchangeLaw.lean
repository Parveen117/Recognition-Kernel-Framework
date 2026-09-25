/-
  LEAN-RKF-2: theorum/51 EXCHANGE LAW on the 2×2 C_Σ carrier, core Lean 4 (no Mathlib).
  Scalars are C_Σ pairs (rad, turn) over Int with ι² = −1.  D = B + ιA with B antisymmetric
  and A symmetric (anti-self-dagger), S = R + ιT with R symmetric, T antisymmetric.
  Claim (T51 T2):  D†S + SD = ([R,B] + [A,T]) + ι([T,B] + [R,A]), entrywise, for ALL integer entries.
-/

structure CS where
  r : Int
  t : Int
deriving DecidableEq, Repr

def CS.add (x y : CS) : CS := ⟨x.r + y.r, x.t + y.t⟩
def CS.sub (x y : CS) : CS := ⟨x.r - y.r, x.t - y.t⟩
def CS.mul (x y : CS) : CS := ⟨x.r * y.r - x.t * y.t, x.r * y.t + x.t * y.r⟩
def CS.conj (x : CS) : CS := ⟨x.r, -x.t⟩

/-- 2×2 matrix as four scalars (row-major) -/
structure M2 where
  a : CS
  b : CS
  c : CS
  d : CS
deriving DecidableEq, Repr

def M2.add (x y : M2) : M2 := ⟨x.a.add y.a, x.b.add y.b, x.c.add y.c, x.d.add y.d⟩
def M2.sub (x y : M2) : M2 := ⟨x.a.sub y.a, x.b.sub y.b, x.c.sub y.c, x.d.sub y.d⟩
def M2.mul (x y : M2) : M2 :=
  ⟨(x.a.mul y.a).add (x.b.mul y.c), (x.a.mul y.b).add (x.b.mul y.d),
   (x.c.mul y.a).add (x.d.mul y.c), (x.c.mul y.b).add (x.d.mul y.d)⟩
/-- native dagger: transpose + conj -/
def M2.dag (x : M2) : M2 := ⟨x.a.conj, x.c.conj, x.b.conj, x.d.conj⟩
def comm (x y : M2) : M2 := (x.mul y).sub (y.mul x)
def iota (x : M2) : M2 := x.mul ⟨⟨0,1⟩,⟨0,0⟩,⟨0,0⟩,⟨0,1⟩⟩

def real (p q s u : Int) : M2 := ⟨⟨p,0⟩,⟨q,0⟩,⟨s,0⟩,⟨u,0⟩⟩

/-- B antisymmetric real, A symmetric real, R symmetric real, T antisymmetric real -/
def B (b : Int) : M2 := real 0 b (-b) 0
def A (a1 a2 a3 : Int) : M2 := real a1 a2 a2 a3
def R (r1 r2 r3 : Int) : M2 := real r1 r2 r2 r3
def T (t : Int) : M2 := real 0 t (-t) 0

theorem anti_self_dagger (b a1 a2 a3 : Int) :
    ((B b).add (iota (A a1 a2 a3))).dag = (M2.sub ⟨⟨0,0⟩,⟨0,0⟩,⟨0,0⟩,⟨0,0⟩⟩ ((B b).add (iota (A a1 a2 a3)))) := by
  simp [M2.add, M2.sub, M2.dag, iota, M2.mul, CS.add, CS.sub, CS.mul, CS.conj, B, A, real]

theorem exchange_law (b a1 a2 a3 r1 r2 r3 t : Int) :
    let D := (B b).add (iota (A a1 a2 a3))
    let S := (R r1 r2 r3).add (iota (T t))
    (D.dag.mul S).add (S.mul D)
      = ((comm (R r1 r2 r3) (B b)).add (comm (A a1 a2 a3) (T t))).add
          (iota ((comm (T t) (B b)).add (comm (R r1 r2 r3) (A a1 a2 a3)))) := by
  intro D S
  simp only [D, S, M2.add, M2.sub, M2.dag, M2.mul, comm, iota, CS.add, CS.sub, CS.mul, CS.conj, B, A, R, T, real]
  simp only [M2.mk.injEq, CS.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩ <;>
    simp only [Int.mul_zero, Int.zero_mul, Int.add_zero, Int.zero_add, Int.sub_zero, Int.zero_sub,
               Int.mul_one, Int.one_mul, Int.neg_mul, Int.mul_neg, Int.neg_neg, Int.sub_eq_add_neg,
               Int.neg_add, Int.mul_add, Int.add_mul] <;>
    first
      | omega
      | (simp only [Int.mul_comm, Int.mul_left_comm, Int.mul_assoc, Int.add_comm, Int.add_left_comm, Int.add_assoc]; try omega)

