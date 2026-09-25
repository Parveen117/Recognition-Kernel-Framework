/-
  LEAN-RKF-3: theorum/60 confluence verdict on the gam+śap+tip word carrier.
  Objects: reachable states (canonical order), rules as total maps (extension by identity).
  A state is a normal form iff every rule fixes it.  Kernel-checked by `decide`:
  with memory carried the root reaches exactly ONE normal form (gacchati);
  with memory erased at lopa the root reaches several (not confluent) — the flip at A4 of the
  Vedic confluence note, now outside the Python lineage.
-/
namespace Mem
def n : Nat := 16
def t0 : List (Fin 16) := [2, 3, 2, 3, 6, 7, 6, 7, 10, 11, 10, 11, 14, 15, 14, 15]
def t1 : List (Fin 16) := [1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]
def t2 : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7, 12, 13, 14, 15]
def t3 : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def t4 : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def t5 : List (Fin 16) := [0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11, 12, 13, 14, 15]
def t6 : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3]
def rules : List (Fin 16 → Fin 16) := [(fun w => t0.getD w.val 0), (fun w => t1.getD w.val 0), (fun w => t2.getD w.val 0), (fun w => t3.getD w.val 0), (fun w => t4.getD w.val 0), (fun w => t5.getD w.val 0), (fun w => t6.getD w.val 0)]
def isNF (w : Fin 16) : Bool := rules.all (fun r => decide (r w = w))
def stepAll (s : List (Fin 16)) : List (Fin 16) := (s ++ (s.bind (fun w => rules.map (fun r => r w)))).eraseDups
def iter : Nat → List (Fin 16) → List (Fin 16)
  | 0, s => s
  | k+1, s => iter k (stepAll s)
def reach : List (Fin 16) := iter 16 [8]
def reachableNFs : List (Fin 16) := reach.filter isNF
theorem reachable_normal_forms : reachableNFs = [3] := by decide
theorem all_states_reached : reach.length = 16 := by decide
end Mem

namespace NoMem
def n : Nat := 20
def t0 : List (Fin 20) := [3, 4, 2, 3, 4, 8, 9, 7, 8, 9, 13, 14, 12, 13, 14, 18, 19, 17, 18, 19]
def t1 : List (Fin 20) := [1, 1, 2, 2, 4, 6, 6, 7, 7, 9, 11, 11, 12, 12, 14, 16, 16, 17, 17, 19]
def t2 : List (Fin 20) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 12, 13, 14, 15, 16, 17, 18, 19]
def t3 : List (Fin 20) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
def t4 : List (Fin 20) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
def t5 : List (Fin 20) := [0, 1, 2, 3, 4, 15, 16, 17, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
def t6 : List (Fin 20) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4]
def rules : List (Fin 20 → Fin 20) := [(fun w => t0.getD w.val 0), (fun w => t1.getD w.val 0), (fun w => t2.getD w.val 0), (fun w => t3.getD w.val 0), (fun w => t4.getD w.val 0), (fun w => t5.getD w.val 0), (fun w => t6.getD w.val 0)]
def isNF (w : Fin 20) : Bool := rules.all (fun r => decide (r w = w))
def stepAll (s : List (Fin 20)) : List (Fin 20) := (s ++ (s.bind (fun w => rules.map (fun r => r w)))).eraseDups
def iter : Nat → List (Fin 20) → List (Fin 20)
  | 0, s => s
  | k+1, s => iter k (stepAll s)
def reach : List (Fin 20) := iter 20 [10]
def reachableNFs : List (Fin 20) := reach.filter isNF
theorem reachable_normal_forms : reachableNFs = [12, 14, 4, 2] := by decide
theorem all_states_reached : reach.length = 20 := by decide
end NoMem

theorem confluent_with_memory : Mem.reachableNFs.length = 1 := by decide
theorem not_confluent_without_memory : NoMem.reachableNFs.length ≥ 2 := by decide
