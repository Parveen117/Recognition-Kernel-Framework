/-
  LEAN-RKF-1: theorum/61 commutator-support theorem on the gam+śap+tip word carrier
  (16 reachable states, 7 canonical sūtras, memory carried).  The tables are the
  certified realization exported from proof_lab/rewrite_rules_as_cut_module_operators;
  the theorems below are checked by the Lean 4 kernel (`decide`), core Lean only,
  no Mathlib.  Independence: the kernel does not run the Python.
-/
def n : Nat := 16
def r_1_3_9_tab : List (Fin 16) := [2, 3, 2, 3, 6, 7, 6, 7, 10, 11, 10, 11, 14, 15, 14, 15]
def r_1_3_9 (w : Fin 16) : Fin 16 := r_1_3_9_tab.getD w.val 0
def appl_r_1_3_9_tab : List Bool := [true, true, false, false, true, true, false, false, true, true, false, false, true, true, false, false]
def appl_r_1_3_9 (w : Fin 16) : Bool := appl_r_1_3_9_tab.getD w.val false
def r_3_4_113_tab : List (Fin 16) := [1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]
def r_3_4_113 (w : Fin 16) : Fin 16 := r_3_4_113_tab.getD w.val 0
def appl_r_3_4_113_tab : List Bool := [true, false, true, false, true, false, true, false, true, false, true, false, true, false, true, false]
def appl_r_3_4_113 (w : Fin 16) : Bool := appl_r_3_4_113_tab.getD w.val false
def r_7_3_77_tab : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7, 12, 13, 14, 15]
def r_7_3_77 (w : Fin 16) : Fin 16 := r_7_3_77_tab.getD w.val 0
def appl_r_7_3_77_tab : List Bool := [false, false, false, false, false, false, false, false, true, true, true, true, false, false, false, false]
def appl_r_7_3_77 (w : Fin 16) : Bool := appl_r_7_3_77_tab.getD w.val false
def r_7_3_84_tab : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def r_7_3_84 (w : Fin 16) : Fin 16 := r_7_3_84_tab.getD w.val 0
def appl_r_7_3_84_tab : List Bool := [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
def appl_r_7_3_84 (w : Fin 16) : Bool := appl_r_7_3_84_tab.getD w.val false
def r_6_1_78_tab : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def r_6_1_78 (w : Fin 16) : Fin 16 := r_6_1_78_tab.getD w.val 0
def appl_r_6_1_78_tab : List Bool := [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
def appl_r_6_1_78 (w : Fin 16) : Bool := appl_r_6_1_78_tab.getD w.val false
def r_6_1_73_tab : List (Fin 16) := [0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11, 12, 13, 14, 15]
def r_6_1_73 (w : Fin 16) : Fin 16 := r_6_1_73_tab.getD w.val 0
def appl_r_6_1_73_tab : List Bool := [false, false, false, false, true, true, true, true, false, false, false, false, false, false, false, false]
def appl_r_6_1_73 (w : Fin 16) : Bool := appl_r_6_1_73_tab.getD w.val false
def r_8_4_40_tab : List (Fin 16) := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3]
def r_8_4_40 (w : Fin 16) : Fin 16 := r_8_4_40_tab.getD w.val 0
def appl_r_8_4_40_tab : List Bool := [false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, true]
def appl_r_8_4_40 (w : Fin 16) : Bool := appl_r_8_4_40_tab.getD w.val false

/-- column support of the commutator [R_a, R_b] : states where a∘b ≠ b∘a -/
def supp (a b : Fin 16 → Fin 16) : List (Fin 16) :=
  ((List.range 16).map (fun i => (Fin.ofNat i : Fin 16))).filter (fun w => decide (a (b w) ≠ b (a w)))
/-- conflict states: both applicable and order-dependent -/
def conflicts (a b : Fin 16 → Fin 16) (pa pb : Fin 16 → Bool) : List (Fin 16) :=
  (supp a b).filter (fun w => pa w && pb w)
theorem supp_r_1_3_9_r_3_4_113 : supp r_1_3_9 r_3_4_113 = [] := by decide
theorem supp_r_1_3_9_r_7_3_77 : supp r_1_3_9 r_7_3_77 = [] := by decide
theorem supp_r_1_3_9_r_7_3_84 : supp r_1_3_9 r_7_3_84 = [] := by decide
theorem supp_r_1_3_9_r_6_1_78 : supp r_1_3_9 r_6_1_78 = [] := by decide
theorem supp_r_1_3_9_r_6_1_73 : supp r_1_3_9 r_6_1_73 = [] := by decide
theorem supp_r_1_3_9_r_8_4_40 : supp r_1_3_9 r_8_4_40 = [] := by decide
theorem supp_r_3_4_113_r_7_3_77 : supp r_3_4_113 r_7_3_77 = [] := by decide
theorem supp_r_3_4_113_r_7_3_84 : supp r_3_4_113 r_7_3_84 = [] := by decide
theorem supp_r_3_4_113_r_6_1_78 : supp r_3_4_113 r_6_1_78 = [] := by decide
theorem supp_r_3_4_113_r_6_1_73 : supp r_3_4_113 r_6_1_73 = [] := by decide
theorem supp_r_3_4_113_r_8_4_40 : supp r_3_4_113 r_8_4_40 = [] := by decide
theorem supp_r_7_3_77_r_7_3_84 : supp r_7_3_77 r_7_3_84 = [] := by decide
theorem supp_r_7_3_77_r_6_1_78 : supp r_7_3_77 r_6_1_78 = [] := by decide
theorem supp_r_7_3_77_r_6_1_73 : supp r_7_3_77 r_6_1_73 = [8, 9, 10, 11] := by decide
theorem supp_r_7_3_77_r_8_4_40 : supp r_7_3_77 r_8_4_40 = [] := by decide
theorem supp_r_7_3_84_r_6_1_78 : supp r_7_3_84 r_6_1_78 = [] := by decide
theorem supp_r_7_3_84_r_6_1_73 : supp r_7_3_84 r_6_1_73 = [] := by decide
theorem supp_r_7_3_84_r_8_4_40 : supp r_7_3_84 r_8_4_40 = [] := by decide
theorem supp_r_6_1_78_r_6_1_73 : supp r_6_1_78 r_6_1_73 = [] := by decide
theorem supp_r_6_1_78_r_8_4_40 : supp r_6_1_78 r_8_4_40 = [] := by decide
theorem supp_r_6_1_73_r_8_4_40 : supp r_6_1_73 r_8_4_40 = [4, 5, 6, 7] := by decide

/-- T61 T3: with memory carried there are NO conflicts on any pair -/
theorem noconf_r_1_3_9_r_3_4_113 : conflicts r_1_3_9 r_3_4_113 appl_r_1_3_9 appl_r_3_4_113 = [] := by decide
theorem noconf_r_1_3_9_r_7_3_77 : conflicts r_1_3_9 r_7_3_77 appl_r_1_3_9 appl_r_7_3_77 = [] := by decide
theorem noconf_r_1_3_9_r_7_3_84 : conflicts r_1_3_9 r_7_3_84 appl_r_1_3_9 appl_r_7_3_84 = [] := by decide
theorem noconf_r_1_3_9_r_6_1_78 : conflicts r_1_3_9 r_6_1_78 appl_r_1_3_9 appl_r_6_1_78 = [] := by decide
theorem noconf_r_1_3_9_r_6_1_73 : conflicts r_1_3_9 r_6_1_73 appl_r_1_3_9 appl_r_6_1_73 = [] := by decide
theorem noconf_r_1_3_9_r_8_4_40 : conflicts r_1_3_9 r_8_4_40 appl_r_1_3_9 appl_r_8_4_40 = [] := by decide
theorem noconf_r_3_4_113_r_7_3_77 : conflicts r_3_4_113 r_7_3_77 appl_r_3_4_113 appl_r_7_3_77 = [] := by decide
theorem noconf_r_3_4_113_r_7_3_84 : conflicts r_3_4_113 r_7_3_84 appl_r_3_4_113 appl_r_7_3_84 = [] := by decide
theorem noconf_r_3_4_113_r_6_1_78 : conflicts r_3_4_113 r_6_1_78 appl_r_3_4_113 appl_r_6_1_78 = [] := by decide
theorem noconf_r_3_4_113_r_6_1_73 : conflicts r_3_4_113 r_6_1_73 appl_r_3_4_113 appl_r_6_1_73 = [] := by decide
theorem noconf_r_3_4_113_r_8_4_40 : conflicts r_3_4_113 r_8_4_40 appl_r_3_4_113 appl_r_8_4_40 = [] := by decide
theorem noconf_r_7_3_77_r_7_3_84 : conflicts r_7_3_77 r_7_3_84 appl_r_7_3_77 appl_r_7_3_84 = [] := by decide
theorem noconf_r_7_3_77_r_6_1_78 : conflicts r_7_3_77 r_6_1_78 appl_r_7_3_77 appl_r_6_1_78 = [] := by decide
theorem noconf_r_7_3_77_r_6_1_73 : conflicts r_7_3_77 r_6_1_73 appl_r_7_3_77 appl_r_6_1_73 = [] := by decide
theorem noconf_r_7_3_77_r_8_4_40 : conflicts r_7_3_77 r_8_4_40 appl_r_7_3_77 appl_r_8_4_40 = [] := by decide
theorem noconf_r_7_3_84_r_6_1_78 : conflicts r_7_3_84 r_6_1_78 appl_r_7_3_84 appl_r_6_1_78 = [] := by decide
theorem noconf_r_7_3_84_r_6_1_73 : conflicts r_7_3_84 r_6_1_73 appl_r_7_3_84 appl_r_6_1_73 = [] := by decide
theorem noconf_r_7_3_84_r_8_4_40 : conflicts r_7_3_84 r_8_4_40 appl_r_7_3_84 appl_r_8_4_40 = [] := by decide
theorem noconf_r_6_1_78_r_6_1_73 : conflicts r_6_1_78 r_6_1_73 appl_r_6_1_78 appl_r_6_1_73 = [] := by decide
theorem noconf_r_6_1_78_r_8_4_40 : conflicts r_6_1_78 r_8_4_40 appl_r_6_1_78 appl_r_8_4_40 = [] := by decide
theorem noconf_r_6_1_73_r_8_4_40 : conflicts r_6_1_73 r_8_4_40 appl_r_6_1_73 appl_r_8_4_40 = [] := by decide

/-- the two nonzero commutators are exactly the enabling pairs chaḥ→tuk and tuk→ścutva -/
theorem enabling_chain : supp r_7_3_77 r_6_1_73 = [8, 9, 10, 11] ∧ supp r_6_1_73 r_8_4_40 = [4, 5, 6, 7] := by decide

