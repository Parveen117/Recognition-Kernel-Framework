from __future__ import annotations

"""LADDER AUDIT 50-59 (adversarial, from scratch where cheap).

Owner request Aug 23 2026: before growing the operator-algebra ladder, attack
it.  For each theorum 50..59 this capsule does one or more of:
  (R) re-derive a load-bearing claim with an INDEPENDENT implementation
      (own mass, own LDL, own exchange-law formula, own jets);
  (P) plant a negative that the theorem's own machinery MUST reject;
  (S) scope probe -- find where a check is weaker than its headline and
      record the honest boundary;
  (I) renaming test (TAUT-1, R1): run the same computation on random data
      of the same shape -- if it reproduces, the claim is an identity, not
      carrier content.

Findings are recorded as data (severity CERT_DEFECT / HEADLINE_DOWNGRADE /
SCOPE_NOTE / OK).  Fixes applied to the ladder in this commit are listed in
FIXES_APPLIED.  The audit PASSES iff every planted negative is rejected and
every re-derivation agrees; findings do not fail the audit -- they are its
product.
"""

import argparse
import hashlib
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Any

from proof_lab import canvas_operators_nativized as t56
from proof_lab import generalized_euler_emk_dock as t55
from proof_lab import infinite_face_recognition_completion as t54
from proof_lab import loop_residue_first_visible_jet_binding as t57
from proof_lab import native_cut_square_factorization as t53
from proof_lab import native_seam_gap_odd_covariance as t50
from proof_lab import native_seam_resolvent as t52
from proof_lab import odd_channel_exchange_law as t51
from proof_lab import paninian_seam_calculus as t58
from proof_lab import prime_letter_operators as t59
from proof_lab.native_seam_gap_odd_covariance import F0, F1, cut_square, dagger, eye, is_zero, m_add, m_scale, m_sub, mat, sc, star, zeros

Finding = dict[str, Any]


def finding(theorem: str, kind: str, severity: str, text: str, data: Any = None) -> Finding:
    return {"theorem": theorem, "kind": kind, "severity": severity, "text": text, "data": data}


# ---------------------------------------------------------------- independent primitives
def my_mass(M) -> Fraction:
    return sum(abs(x[0]) + abs(x[1]) for row in M for x in row)


def my_comm(X, Y):
    return m_sub(star(X, Y), star(Y, X))


def rnd_sc(rng, lo=-3, hi=3):
    return sc(Fraction(rng.randint(lo, hi)), Fraction(rng.randint(lo, hi)))


def rnd_mat(rng, n):
    return mat([[rnd_sc(rng) for _ in range(n)] for _ in range(n)])


def anti_self_dagger(rng, n):
    X = rnd_mat(rng, n)
    return m_sub(X, dagger(X))


# ---------------------------------------------------------------- 50
def audit_50(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    faces = t50.instance_faces()
    rho = Fraction(1, 2)
    # (R) sheet-mass multiplicativity with MY mass on every memory word, m = 1..4
    ok = True
    for m in range(1, 5):
        fcs = faces[:m]
        pd = t50.product_data(fcs)
        for word in itertools.product((1, -1), repeat=m):
            if all(s == 1 for s in word):
                continue
            Pi = t50.sheet_projector(fcs, word)
            block = star(star(Pi, pd["L"]), Pi)
            expect = F1
            for fc, s in zip(fcs, word):
                expect *= fc["f0"] if s == 1 else my_mass(fc["B"])
            ok &= my_mass(block) == expect
    checks["50_R_sheet_mass_multiplicative_own_mass_m_le_4"] = ok
    # (P) planted face violating H2 (weight > rho f0) must be flagged by face_hypotheses
    bad = t50.flow_face(Fraction(2), Fraction(3), faces[0]["generator"], Fraction(1, 2))
    checks["50_P_overweight_face_rejected_by_H2"] = not t50.face_hypotheses(bad, rho)["H2_mass_contraction"]
    # (S) A4 "every quadratic form is turn-free" -- probe an OFF-diagonal pairing x^dag S y, x != y
    S = cut_square(rnd_mat(rng, 3))
    x, y = mat([[rnd_sc(rng)] for _ in range(3)]), mat([[rnd_sc(rng)] for _ in range(3)])
    off = star(star(dagger(x), S), y)[0][0]
    diag = star(star(dagger(x), S), x)[0][0]
    checks["50_S_diagonal_turn_free_offdiagonal_not"] = diag[1] == 0 and off[1] != 0
    fs.append(finding("50", "S", "SCOPE_NOTE", "A4 is a DIAGONAL statement (x^dag S x turn-free); off-diagonal pairings x^dag S y carry turn -- the odd channel is visible to polarization, invisible to squares (LEAN-4 shape). Headline 'invisible to every quadratic form' should read 'to every self-pairing'.", {"off_turn": str(off[1])}))
    return fs, checks


# ---------------------------------------------------------------- 51
def audit_51(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (R) exchange law from scratch: D = B + iota A (B real antisym, A real sym); dS = D^dag S + S D
    ok = True
    for _ in range(12):
        n = 3
        D = anti_self_dagger(rng, n)
        S = cut_square(rnd_mat(rng, n))
        dS = m_add(star(dagger(D), S), star(S, D))
        # own prediction: split into rad/turn by hand
        Brad = tuple(tuple(x[0] for x in row) for row in D)
        Aturn = tuple(tuple(x[1] for x in row) for row in D)
        Rs = tuple(tuple(x[0] for x in row) for row in S)
        Ts = tuple(tuple(x[1] for x in row) for row in S)
        def rmul(X, Y):
            return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)) for i in range(n))
        def radd(X, Y, sgn=1):
            return tuple(tuple(X[i][j] + sgn * Y[i][j] for j in range(n)) for i in range(n))
        def T(X):
            return tuple(tuple(X[j][i] for j in range(n)) for i in range(n))
        # D^dag = B^T - iota A^T = -B - iota A (B antisym, A sym)  ->  D^dag S = (-B - iA)(R + iT)
        rad_pred = radd(radd(rmul(T(Brad), Rs), rmul(T(Aturn), Ts), -1), radd(rmul(Rs, Brad), rmul(Ts, Aturn), -1))
        turn_pred = radd(radd(rmul(T(Brad), Ts), rmul(T(Aturn), Rs), -1), radd(rmul(Ts, Brad), rmul(Rs, Aturn)))
        # careful sign: D^dag = T(B) + iota*(-T(A))... compute exactly instead of trusting hand algebra:
        Ddag = dagger(D)
        Bd = tuple(tuple(x[0] for x in row) for row in Ddag)
        Ad = tuple(tuple(x[1] for x in row) for row in Ddag)
        rad_pred = radd(radd(rmul(Bd, Rs), rmul(Ad, Ts), -1), radd(rmul(Rs, Brad), rmul(Ts, Aturn), -1))
        turn_pred = radd(radd(rmul(Bd, Ts), rmul(Ad, Rs)), radd(rmul(Rs, Aturn), rmul(Ts, Brad)))
        ok &= tuple(tuple(x[0] for x in row) for row in dS) == rad_pred and tuple(tuple(x[1] for x in row) for row in dS) == turn_pred
    checks["51_R_exchange_law_rederived_by_hand_12_of_12"] = ok
    # (P) tampered Cayley (different h on numerator/denominator) must break unitarity & energy invariance
    D = anti_self_dagger(rng, 3)
    n = 3
    bad = star(t51.inverse(m_sub(eye(n), m_scale(sc(Fraction(1, 4)), D))), m_add(eye(n), m_scale(sc(Fraction(1, 3)), D)))
    S = cut_square(rnd_mat(rng, 3))
    checks["51_P_tampered_cayley_not_unitary_energy_not_invariant"] = star(dagger(bad), bad) != eye(n) and t50.energy(t51.transport(S, bad)) != t50.energy(S)
    return fs, checks


# ---------------------------------------------------------------- 52
def audit_52(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (S) q < 1 is SUFFICIENT for the mass-Neumann inverse, not necessary: exhibit q >= 1 with exact inverse
    L = mat([[sc(2), sc(0)], [sc(0), sc(2)]])
    lam = sc(3)
    q = t52.q_ratio(L, lam)
    inv_exists = True
    try:
        t51.inverse(t52.lam_I_minus(L, lam))
    except AssertionError:
        inv_exists = False
    checks["52_S_q_lt_1_sufficient_not_necessary_witness"] = inv_exists and q >= 1  # q = 4/3 yet (lambda I - L) = I invertible
    found = None
    for a in range(1, 6):
        Lx = mat([[sc(a), sc(a)], [sc(0), sc(a)]])
        lamx = sc(a + 1)
        qx = t52.q_ratio(Lx, lamx)
        try:
            t51.inverse(t52.lam_I_minus(Lx, lamx))
            if qx >= 1:
                found = {"a": a, "q": str(qx)}
                break
        except AssertionError:
            pass
    checks["52_S_found_invertible_instance_outside_gap_region"] = found is not None
    fs.append(finding("52", "S", "SCOPE_NOTE", "The native gap region G_rho = {N(lambda) <= rho f0 D(lambda)} / mass-Neumann condition q<1 is a SUFFICIENT certificate for the resolvent; invertible instances exist with q >= 1. Headline 'gap as native region' is a region of certified resolvability, not the resolvent set.", found))
    # (P) budget must be violated when q is halved artificially (their own control) -- re-run independently
    L = mat([[sc(0, Fraction(1, 2)), sc(Fraction(1, 3))], [sc(0), sc(Fraction(1, 4), Fraction(1, 4))]])
    lam = sc(4)  # q < 1 here
    q = t52.q_ratio(L, lam)
    assert q < 1
    exact = t51.inverse(t52.lam_I_minus(L, lam))
    viol = any(my_mass(m_sub(exact, t52.partial_resolvent(L, lam, N))) > t52.tail_budget(L, lam, N, q / 2) for N in range(0, 8))
    holds = all(my_mass(m_sub(exact, t52.partial_resolvent(L, lam, N))) <= t52.tail_budget(L, lam, N) for N in range(0, 8))
    checks["52_P_tail_budget_holds_own_mass_and_halved_q_violated"] = holds and viol
    # (P) FOUND: tail_budget returned a NEGATIVE budget silently for q >= 1 (1/(1-q) < 0) -- no fail-closed guard
    refused = False
    try:
        t52.tail_budget(mat([[sc(2), sc(0)], [sc(0), sc(2)]]), sc(3), 1)
    except AssertionError:
        refused = True
    checks["52_P_tail_budget_outside_region_now_refused"] = refused
    fs.append(finding("52", "P", "CERT_DEFECT", "tail_budget(L, lambda, N) silently returned a NEGATIVE budget for q >= 1 (e.g. L = 2I, lambda = 3: q = 4/3, budget = -4). Not fail-closed. FIXED in this commit: assert q < 1 (re-pinned).", {"q": "4/3", "old_budget": "-4"}))
    return fs, checks


# ---------------------------------------------------------------- 53
def audit_53(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (R) factorization reconstructs with an independent check; (P) singular L (rank-deficient cut square)
    ok = True
    for _ in range(8):
        S = cut_square(rnd_mat(rng, 3))
        fac = t53.ldl_native(S)
        ok &= t53.reconstruct(fac) == S and all(w >= 0 for w in fac["weights"]) and fac["witness"] is None
    checks["53_R_reconstruction_and_nonnegativity_8_of_8"] = ok
    L = mat([[sc(1), sc(2), sc(3)], [sc(2), sc(4), sc(6)], [sc(0, 1), sc(0, 2), sc(0, 3)]])  # rank 1
    S = cut_square(L)
    try:
        fac = t53.ldl_native(S)
        status = "factorized" if t53.reconstruct(fac) == S else "wrong"
    except AssertionError as e:
        status = f"refused: {e}"
    checks["53_P_rank_deficient_cut_square_handled_or_refused_honestly"] = status in ("factorized",) or status.startswith("refused")
    fs.append(finding("53", "P", "SCOPE_NOTE" if status.startswith("refused") else "OK", f"rank-1 cut square: {status}. If refused, the no-pivoting LDL requires a pivoting order for rank-deficient squares -- boundary to state in 53.", {"status": status}))
    # (P) planted non-square self-dagger with a hidden negative direction -> witness must be returned
    T = mat([[sc(1), sc(2), sc(0)], [sc(2), sc(1), sc(0)], [sc(0), sc(0), sc(1)]])  # eigen -1 along (1,-1,0)
    fac = t53.ldl_native(T)
    w = fac["witness"]
    checks["53_P_hidden_negative_direction_found"] = w is not None and t53.quad(T, w)[0] < 0
    return fs, checks


# ---------------------------------------------------------------- 54
def audit_54(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (P) the finite-product bound 1/(1 - sum) is meaningless when sum >= 1: confirm their t3 refuses / never claims there
    res = t54.t3_t4_cauchy_tails_and_margin(Fraction(1, 2), Fraction(1, 2), 8)  # sum mu = 1/2 * sum (1/2)^i < 1
    checks["54_R_declared_instance_sum_lt_1"] = all(res["checks"].values())
    blew = False
    try:
        res2 = t54.t3_t4_cauchy_tails_and_margin(Fraction(2), Fraction(1, 2), 6)  # sum = 2 > 1
        blew = not all(res2["checks"].values())
    except (AssertionError, ZeroDivisionError):
        blew = True
    checks["54_P_sum_ge_1_instance_not_certified"] = blew
    fs.append(finding("54", "CERT_DEFECT", "CERT_DEFECT", "t5_separation had 'sum_mu_diverges': True hard-coded. FIXED in this commit: partial sums of the constant-mu family are computed and shown to exceed every bound N up to 50 (re-pinned).", None))
    return fs, checks


# ---------------------------------------------------------------- 55
def audit_55(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (R) two gradings from scratch over the 8 elements {I,K,R,RK} x {1, iota}
    I2, K, R, RK = t55.I2, t55.K, t55.R, t55.RK
    elems = {"I": I2, "K": K, "R": R, "RK": RK}
    table = {}
    for name, X in elems.items():
        for pre, c in (("", sc(1)), ("i", sc(0, 1))):
            Y = m_scale(c, X)
            dag_odd = dagger(Y) == m_scale(-1, Y)  # anti-self-dagger = flow generator
            k_even = star(star(K, Y), K) == Y
            table[pre + name] = {"anti_self_dagger": dag_odd, "K_even": k_even}
    gens = sorted(k for k, v in table.items() if v["anti_self_dagger"])
    checks["55_R_flow_generators_are_R_iI_iK_iRK"] = gens == ["R", "iI", "iK", "iRK"]
    checks["55_R_gradings_differ"] = table["R"]["K_even"] is False and table["iK"]["K_even"] is True
    # (P) the EMK bracket sign: [R,K] = 2RK -- planted [K,R] must give -2RK
    checks["55_P_bracket_orientation"] = my_comm(K, R) == m_scale(-2, RK) and my_comm(R, K) == m_scale(2, RK)
    return fs, checks


# ---------------------------------------------------------------- 56
def audit_56(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    strings = ["".join(p) for n in range(1, 4) for p in itertools.product("aiu", repeat=n)]
    # compute what the hard-coded True claimed: fixed composition yan∘guna iterated gives one NF per string
    def nf_prec(w):
        for _ in range(10):
            w2 = t56.yan(t56.guna(w))
            if w2 == w:
                return w
            w = w2
        return None
    unique = all(nf_prec(w) is not None for w in strings)
    in_free = all(nf_prec(w) in t56.normal_forms(w, [t56.guna, t56.yan]) for w in strings)
    checks["56_R_precedence_unique_nf_now_COMPUTED"] = unique and in_free
    fs.append(finding("56", "CERT_DEFECT", "CERT_DEFECT", "B2 'precedence_restores_unique_normal_form': True was hard-coded. FIXED in this commit: computed as iterated yan∘guna fixed point, checked to lie in the free normal-form set (re-pinned).", {"unique": unique, "in_free": in_free}))
    return fs, checks


# ---------------------------------------------------------------- 57
def audit_57(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (I) renaming test: a2 = [D1,D2] and a3 = 1/2[D1+D2,[D1,D2]] on ARBITRARY (non anti-self-dagger) matrices
    ok = True
    for _ in range(8):
        n = rng.choice([2, 3])
        D1, D2 = rnd_mat(rng, n), rnd_mat(rng, n)
        try:
            g = t57.residue_jet(D1, D2)
        except AssertionError:
            continue
        ok &= g[2] == my_comm(D1, D2) and g[3] == t57.a3_closed_form(D1, D2)
    checks["57_I_jet_identities_hold_for_arbitrary_matrices"] = ok
    fs.append(finding("57", "I", "HEADLINE_DOWNGRADE", "T1/T2 jet identities (a2 = bracket, a3 = 1/2[D1+D2,[D1,D2]]) reproduce on arbitrary matrices: they are identities of the Cayley map, NOT odd-sector/carrier content (TAUT-1 R1). Carrier content in 57 is only the TYPING (Gamma as a 46 seam observable, false-residue = visible before order 2) and the EMK evaluation 2 iota alpha beta RK. Headline 'exact order-3 loop identity' stands as a lemma about Cayley, not about the flow.", None))
    # (P) the order-2 quotient must FAIL if the denominator is h^2 with wrong normalization (b2 = 2)
    D1, D2 = t57.emk_pair(Fraction(2), Fraction(3))
    g = t57.residue_jet(D1, D2)
    from proof_lab.first_visible_jet_seam_quotient import classify_finite_jets
    q = classify_finite_jets([g[k][1][0][1] for k in range(5)], [0, 0, 2, 0, 0])
    checks["57_P_denominator_normalization_load_bearing"] = q.quotient == my_comm(D1, D2)[1][0][1] / 2
    return fs, checks


# ---------------------------------------------------------------- 58
def audit_58(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (I) 'ambiguity set = union of commutator supports' -- is it a law?  Toy counterexample:
    #     r1: a->b, r2: a->c, r3: b->d, r4: c->d.  [r1,r2] nonzero on 'a' but unique NF 'd'.
    def r1(w): return ("b",) if w == ("a",) else None
    def r2(w): return ("c",) if w == ("a",) else None
    def r3(w): return ("d",) if w == ("b",) else None
    def r4(w): return ("d",) if w == ("c",) else None
    rules = [r1, r2, r3, r4]
    nf = t58.free_normal_forms(("a",), rules)
    supp = t58.apply_rule(r1, t58.apply_rule(r2, ("a",))) != t58.apply_rule(r2, t58.apply_rule(r1, ("a",)))
    checks["58_I_toy_nonzero_commutator_but_confluent"] = nf == {("d",)} and supp
    fs.append(finding("58", "I", "HEADLINE_DOWNGRADE", "T2(i) 'free ambiguity set EQUALS union of commutator supports' is a property of the five-sutra instance, not a law: a toy system has nonzero [r1,r2] yet a unique normal form (divergences rejoin). The lawful general statement is containment: ambiguity ⊆ ∪ supp[ρi,ρj] over reachable states (priority needed ONLY where a residue is nonzero, not EXACTLY where). Theorem text amended.", None))
    # (P) tie attack: two rules with the SAME sutra key both applicable -> priority_normal_form must refuse
    tie_rules = t58.SANDHI + [("6.1.101", lambda j: ("Z",) if j == ("i", "i") else None)]
    refused = False
    try:
        t58.priority_normal_form(("i", "i"), tie_rules)
    except AssertionError:
        refused = True
    checks["58_P_equal_priority_tie_refused"] = refused
    fs.append(finding("58", "CERT_DEFECT", "CERT_DEFECT", "determinacy checks used isinstance(..., tuple) (vacuous: the function always returns a tuple or raises) and a dead placeholder line. FIXED in this commit: priority_normal_form now refuses ties (AssertionError), and the determinacy check verifies (a) no tie at any step, (b) termination, (c) result lies in the free normal-form set (re-pinned).", None))
    return fs, checks


# ---------------------------------------------------------------- 59
def audit_59(rng) -> tuple[list[Finding], dict[str, bool]]:
    fs, checks = [], {}
    # (I) T4(d) invisibility and T4(c) Cayley residue hold for ANY scalar, prime or not
    ok = True
    for _ in range(6):
        S = cut_square(rnd_mat(rng, 3))
        x = Fraction(rng.randint(1, 9), rng.randint(1, 5))
        U = t51.cayley_unitary(m_scale(sc(0, x), eye(3)), Fraction(1, 2))
        ok &= t51.transport(S, U) == S
    checks["59_I_central_invisibility_is_scalar_identity"] = ok
    fs.append(finding("59", "I", "HEADLINE_DOWNGRADE", "T4(c),(d) reproduce for arbitrary scalars: prime letters sit in the CENTRAL scalar sector, which is trivially odd (iota*scalar) -- NOT the off-diagonal odd channel of theorum/50 where Aghora lives. Prime-specific content in 59 is T1-T3 only (ledger, dagger law, Lambda support). 'Aghora placement' should read 'central-turn placement; zero exchange by centrality'. Theorem text amended.", None))
    # (R) dagger law re-derived on integers: n * q^{-1} has ledger e_p - e_q  <=>  p/q in Q
    f = t59.load_f00h()
    ok2 = all(t59.l_add(dict(f.factor_integer(p)), t59.l_neg(dict(f.factor_integer(q)))) == ({p: 1, q: -1} if p != q else {}) for p in (2, 3, 5, 7) for q in (2, 3, 5, 7))
    checks["59_R_dagger_law_on_F00H_factorizations"] = ok2
    return fs, checks


FIXES_APPLIED = [
    "theorum/52 proof_lab: tail_budget silently negative for q >= 1 -> fail-closed assert q < 1 (re-pinned)",
    "theorum/54 proof_lab: 'sum_mu_diverges' hard-coded True -> computed partial sums exceed N for N<=50 (re-pinned)",
    "theorum/56 proof_lab: B2 'precedence_restores_unique_normal_form' hard-coded True -> computed (re-pinned)",
    "theorum/58 proof_lab: vacuous isinstance determinacy checks -> tie-refusing priority + terminating + membership (re-pinned); T2(i) headline downgraded to containment",
    "theorum/57 md: a2/a3 identities labelled as Cayley-map lemmas (renaming test), carrier content restated",
    "theorum/59 md: 'Aghora placement' restated as central-turn placement",
    "theorum/50 md: A4 restated as self-pairing statement; theorum/52 md: gap region = certified-resolvability region",
]


def build_certificate() -> dict[str, Any]:
    rng = random.Random(5059)
    findings: list[Finding] = []
    checks: dict[str, bool] = {}
    for fn in (audit_50, audit_51, audit_52, audit_53, audit_54, audit_55, audit_56, audit_57, audit_58, audit_59):
        fs, cs = fn(rng)
        findings += fs
        checks.update(cs)
    status = "PASS_LADDER_AUDIT_50_59" if all(checks.values()) else "FAIL_LADDER_AUDIT_50_59"
    return {
        "schema": "rkf.ladder_audit_50_59.v1",
        "status": status,
        "summary": {
            "cert_defects": sum(f["severity"] == "CERT_DEFECT" for f in findings),
            "headline_downgrades": sum(f["severity"] == "HEADLINE_DOWNGRADE" for f in findings),
            "scope_notes": sum(f["severity"] == "SCOPE_NOTE" for f in findings),
        },
        "fixes_applied": FIXES_APPLIED,
        "not_done": ["external GPT verifier pass (owner's tool)", "Lean kernel for any 50-59 statement (I2 channel)", "attacks on theorums 54 T1-T4 kron identities beyond the declared instance"],
        "checks": checks,
        "findings": findings,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    payload = build_certificate()
    if args.output:
        args.output.write_bytes(canonical_bytes(payload))
    print(payload["status"], payload["summary"])
    for k, v in payload["checks"].items():
        print(k, v)
    for f in payload["findings"]:
        print(f"[{f['severity']}] {f['theorem']}: {f['text'][:140]}")
    return 0 if payload["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
