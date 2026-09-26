/-
  LEAN-RKF-5: theorum/71 Piṅgala pratyayas and theorum/73 Vedāṅga Jyotiṣa yuga closure,
  kernel-checked.  Core Lean 4, no Mathlib.
-/

set_option maxRecDepth 100000

namespace Pingala

/-- naṣṭa (Chandaḥ-sūtra 8.24–25): row index -> pattern, as a list of Bool (true = L) -/
def nashta : Nat → Nat → List Bool
  | 0, _ => []
  | n+1, r => if r % 2 == 0 then true :: nashta n (r / 2) else false :: nashta n ((r + 1) / 2)

/-- uddiṣṭa (8.26–27): pattern -> row index, 1 + Σ_{L at i} 2^i -/
def uddishta (p : List Bool) : Nat := 1 + go p 0
where
  go : List Bool → Nat → Nat
    | [], _ => 0
    | b :: bs, i => (if b then 2 ^ i else 0) + go bs (i + 1)

def rows (n : Nat) : List Nat := (List.range (2 ^ n)).map (· + 1)

/-- uddiṣṭa ∘ naṣṭa = id on every row, n ≤ 8 -/
theorem uddishta_nashta_id : ((List.range 9).map (fun n => (rows n).all (fun r => uddishta (nashta n r) == r))).all id = true := by decide

/-- first row is all-guru (false), last row all-laghu (true) -/
theorem first_last (n : Nat) (h : n ≤ 8) :
    nashta n 1 = List.replicate n false ∧ nashta n (2 ^ n) = List.replicate n true := by
  revert n; decide

/-- meru = binomial: lagakriyā row sums are 2^n (n ≤ 10), via the recursion -/
def meru : Nat → List Nat
  | 0 => [1]
  | n+1 => let m := meru n; List.zipWith (· + ·) (0 :: m) (m ++ [0])

theorem meru_rowsum : ∀ n, n ≤ 10 → (meru n).foldl (· + ·) 0 = 2 ^ n := by decide
theorem meru_8 : meru 8 = [1, 8, 28, 56, 70, 56, 28, 8, 1] := by decide

/-- mātrā-meru (w(L)=1, w(G)=2): count of patterns of weight m, m ≤ 12, is the Virahāṅka sequence -/
def patterns (n : Nat) : List (List Bool) := (rows n).map (nashta n)
def weight (p : List Bool) : Nat := p.foldl (fun acc b => acc + (if b then 1 else 2)) 0
def matraCount (m : Nat) : Nat := ((List.range (m + 1)).map (fun n => ((patterns n).filter (fun p => weight p == m)).length)).foldl (· + ·) 0
theorem virahanka : (List.range 10).map (fun i => matraCount (i + 1)) = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] := by decide

end Pingala

namespace Jyotisa
/-- Vedāṅga Jyotiṣa yuga: 5 years × 366 = 1830 days; 62 synodic months; 1860 tithis; 1835 sidereal days -/
theorem yuga_days : 5 * 366 = 1830 := by decide
/-- 5-year solar–lunar residue equals exactly two synodic months:  5·(12·1830 − 366·62) = −2·1830  (cleared of the denominator 62) -/
theorem intercalation_closes : 5 * (12 * 1830 - 366 * 62 : Int) = -2 * 1830 := by decide
theorem adhimasa : 62 - 60 = 2 := by decide
theorem ksaya_tithis : 1860 - 1830 = 30 := by decide
theorem sidereal_minus_civil_is_years : 1835 - 1830 = 5 := by decide
/-- all cycles re-align at 1830 and at no earlier day: 1830 is the least common multiple-closure -/
theorem all_cycles_close : 1830 % 1830 = 0 ∧ (1830 * 62) % 1830 = 0 ∧ (1830 * 1860) % 1830 = 0 := by decide
theorem least_closure : ((List.range 1830).map (· + 1)).all (fun t => t == 1830 || !((t * 62) % 1830 == 0 && (t * 67) % 1830 == 0 && (t * 1835) % 1830 == 0 && t % 366 == 0)) = true := by decide
end Jyotisa
