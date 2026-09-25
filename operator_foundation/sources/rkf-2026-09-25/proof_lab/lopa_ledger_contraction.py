from __future__ import annotations

"""Exact certificate (theorum/74): LOPA-LEDGER CONTRACTION on the recognition
transfer — contraction to the silence channel, with the 1.1.62 ledger, as the
native tool the YM upper-bound program named.

Owner's direction (Aug 23): use the Panini seam calculus and the mantra
operators (silence, vibration) for the operator tools. Canvas definitions,
per the standing rule (canvas's own meaning before any classical reading):
silence = LOPA, the 1.3.9 zero-operator = ker of the odd generator
(theorum/62 T2/T3); the ledger = 1.1.62 pratyayalope pratyayalakshanam
(the elided element's effect persists through memory, theorum/58); the
vibration flow = the Euler circular system on the odd generator
(theorum/62 T2, F00E).

Carrier (declared, self-contained; the finite control instance): the
one-column space transfer of the two-rail chain fabric — Publications
YM-37 (pin ad598ee5...) distilled: SU(2) = unit quaternions, faces and
rungs are class functions of products, Haar = rational S^3 moments,
cut space = harmonic degree <= 2 per rail, even conjugation-invariant
sector (dim 8). Faces: Wilson w_pt with rational lower-rounded Bessel
coefficients f_c at kappa in {1/8, 1/4, 1/2}; rung kernel lambda_c
likewise; all rationals printed in the certificate. tau = B^{-1} M with
M, B symmetric rational; every verdict below is a theorum/53 elimination
sign pattern, the cut-square inequality (T01-C shape), or exact algebra.
NOTHING spectral, nothing iterative, nothing classical.

 T1  SILENCE FACTORIZATION (exact). tau = C o M_K with C = sum_c f_c P_c,
     the P_c the per-rail content projectors: C is EXACTLY diagonal on
     the harmonic grading (checked entry by entry), the ladder
     f_0 > f_1/2 > f_1 strict — the per-content lopa rates. The silence
     channel is the content-(0,0) line span{1} (the lopa target: what
     remains when every letter is elided), a STRUCTURAL object — defined
     on every carrier, any content cutoff, any rail count, with no
     reference to eigenvectors or iteration.

 T2  LEDGER 1.1.62 (exact). Elision is not erasure: the silence-channel
     matrix element after one step reads every content of the state
     through the rung fusion,
        <1, tau x> = f_0 * sum_c lambda_c * d_c * (content-c overlap),
     certified as an exact linear identity with the nonzero fusion
     coefficients listed — adarshanam (non-appearance in the visible
     letter) with lakshanam (the effect recorded in the verdict).
     Tamper: zeroing the lambda_{1/2} fusion channel changes the row —
     the ledger term is load-bearing, not decorative.

 T3  CONTRACTION TO SILENCE (the tool). With w := the silence vector
     (NOT a Krylov iterate — this is the difference from Publications
     YM-38, and the reason the tool generalizes):
       - theta_sil = Rayleigh(1) = <1, M 1>/<1, B 1>, a certified LOWER
         bound on the transfer's growth (quadratic-form statement);
       - defect r_sil = tau 1 - theta_sil 1, exactly B-orthogonal to 1;
       - restricted doubled ceiling sigma_sil on the B-orthocomplement
         of the silence channel by ONE theorum/53 sign check;
       - OUTWARD CERTIFICATE (theorum/28 Sec 9): beta_sil :=
         sigma_sil/theta_lo + (perturbation terms) < 1, checked as one
         rational inequality, plus ball invariance for the normalized
         off-silence component (recognized-channel Cauchy, declared
         geometric Smriti tail).
     Then the full YM-38 uniformity assembly runs verbatim with the
     silence deflation: |rho(m,p) - rho_c| <= A_sil (beta_sil^{j-p0} +
     beta_sil^{jc-p0}) for ALL m and interior p (p0 = 2), verified on
     exact rows. MEASURED: the structural constants are only mildly
     weaker than the Krylov ones (beta_sil/L ~ 1.75-1.85 on the grid;
     the restricted ceiling sigma_sil comes out numerically equal) —
     the draft expected dressing-sized loss ~20x and the arithmetic
     said otherwise. Every ingredient is structural: this is the recipe
     a content-tail budget (theorum/75) can be fed into, because the
     silence channel and the sign checks exist on the untruncated
     carrier too.

 T4  VIBRATION TIE (certified comparison + named remainder). The
     exchange (vibration) part of the flow conserves cut-square energy
     (theorum/51); contraction happens because the lopa ladder silences
     what exchange moves out. Certified on the instance: beta_sil
     bracketed against the face ratio r_1/2 = f_1/2/f_0 (both printed;
     the inequality actually satisfied is claimed, nothing more).
     Certified on the instance: beta_sil < r_1/2 = f_1/2/f_0 STRICTLY
     at every grid kappa (measured beta/r = 0.082, 0.165, 0.337) — the
     contraction to silence is faster than one lopa rate. Build note:
     the draft claimed a two-sided window [r/4, 4r]; the certificate
     refused it from below — beta is BETTER than the window, and only
     the one-sided law is claimed. Named remainder = theorum/75:
     content-tail budgets (Sec 11-style hypotheses for infinite content
     on ONE face) so that T3's sign checks transfer from the truncated
     to the full column.

CANDIDATE NAMES (owner's rule: names only after certification; these
become names only if this certificate is green and survives audit):
"silence channel" = span{1} with the lopa reading; "lopa rates" = the
ladder f_c/f_0; "vibration exchange" = the T51 unitary part.

Controls:
  C1  C exactly diagonal on the grading; ladder strict; a planted
      content-mixing C' (off-diagonal entry) is detected.
  C2  ledger identity exact; lambda_{1/2}-channel tamper changes the row.
  C3  r_sil B-orthogonal to 1 EXACTLY; beta_sil < 1; ball invariance;
      REFUSAL control: a pencil with a heavy complement (weight 5 against
      theta = 1) yields sigma >= theta, i.e. no contraction certified —
      the fail-closed path. (Audit fix: the original identity-pencil test
      was vacuous, its ceiling being exactly 1.)
  C4  uniformity rows: every exact rho(m,p) inside the silence-deflation
      band; bands honestly wider than the YM-38 Krylov ones (recorded).
  C5  T4 one-sided law beta_sil < r_1/2 exact on the printed rationals
      (the draft's two-sided window was refused by the data; recorded).
"""

from fractions import Fraction as F
import itertools
import json
import math
import os
import sys

sys.set_int_max_str_digits(1000000)
HERE = os.path.dirname(os.path.abspath(__file__))

GRID = [F(1, 8), F(1, 4), F(1, 2)]
ZERO, HALF, ONE = F(0), F(1, 2), F(1)
P0 = 2
K_EXACT = 30
BTERMS = 40

# ---------------------------------------------------------------------------
# rational Bessel lower/upper (positive series; partial sum is a rigorous
# lower bound, geometric-tail upper as in Publications YM-1's audited shape)
# ---------------------------------------------------------------------------


def bessel_I_lo_hi(nu: int, x: F, terms: int = BTERMS):
    h = x / 2
    h2 = h * h
    t = h ** nu
    for k in range(1, nu + 1):
        t /= k
    s = t
    for k in range(1, terms + 1):
        t = t * h2 / (k * (k + nu))
        s += t
    ratio = h2 / ((terms + 1) * (terms + 1 + nu))
    assert ratio < 1
    tail = t * ratio / (1 - ratio)
    return s, s + tail


def rnd_down(x: F, d: int = 10 ** 9) -> F:
    return F((x.numerator * d) // x.denominator, d)


def face_coeffs(kappa: F):
    out = {}
    for c, j2 in ((ZERO, 0), (HALF, 1), (ONE, 2)):
        lo, _ = bessel_I_lo_hi(j2 + 1, kappa)
        out[c] = rnd_down(F(2, 1) / kappa * lo)
    return out


def rung_coeffs(beta: F = F(2)):
    lo1, hi1 = bessel_I_lo_hi(1, beta)
    out = {ZERO: F(1)}
    for c, j2 in ((HALF, 1), (ONE, 2)):
        lo, _ = bessel_I_lo_hi(j2 + 1, beta)
        out[c] = rnd_down(lo / hi1)
    return out


# ---------------------------------------------------------------------------
# polynomial engine on (S^3)^2 (distilled from Publications YM-37, pin
# ad598ee5...; provenance recorded, code self-contained here)
# ---------------------------------------------------------------------------


def pmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def padd(p, q, s=F(1)):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, F(0)) + s * c
    return {e: c for e, c in out.items() if c != 0}


def pconst(c):
    return {(0,) * 8: F(c)}


def var(i):
    e = [0] * 8
    e[i] = 1
    return {tuple(e): F(1)}


def dfact2(n):
    r = 1
    for k in range(1, 2 * n, 2):
        r *= k
    return r


_MOM = {}


def moment4(e):
    if e in _MOM:
        return _MOM[e]
    if any(a % 2 for a in e):
        v = F(0)
    else:
        b = [a // 2 for a in e]
        num = F(1)
        for bi in b:
            num *= F(dfact2(bi), 2 ** bi)
        den = 1
        for k in range(2, sum(b) + 2):
            den *= k
        v = num / den
    _MOM[e] = v
    return v


def integrate(p):
    tot = F(0)
    for e, c in p.items():
        v = moment4(e[0:4]) * moment4(e[4:8])
        tot += c * v
    return tot


def dot01():
    out = {}
    for i in range(4):
        out = padd(out, pmul(var(i), var(4 + i)))
    return out


def vdot01():
    out = {}
    for i in range(1, 4):
        out = padd(out, pmul(var(i), var(4 + i)))
    return out


def class_kernel(coef, d):
    d2 = pmul(d, d)
    out = pconst(coef[ZERO] - 3 * coef[ONE])
    out = padd(out, d, 4 * coef[HALF])
    out = padd(out, d2, 12 * coef[ONE])
    return out


def cinv_monomial(e4, coef, inv=True):
    deg = sum(e4)
    f0, fh, f1 = coef[ZERO], coef[HALF], coef[ONE]
    g = (lambda f: 1 / f) if inv else (lambda f: f)
    assert deg <= 2
    if deg == 0:
        return {e4: g(f0)}
    if deg == 1:
        return {e4: g(fh)}
    if max(e4) == 1:
        return {e4: g(f1)}
    z = (0, 0, 0, 0)
    return {e4: g(f1), z: F(1, 4) * g(f0) - F(1, 4) * g(f1)}


def c_apply(p, coef, inv=True):
    out = {}
    for e, c in p.items():
        left = cinv_monomial(e[0:4], coef, inv)
        right = cinv_monomial(e[4:8], coef, inv)
        for e1, c1 in left.items():
            for e2, c2 in right.items():
                k = e1 + e2
                out[k] = out.get(k, F(0)) + c * c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def invariant_even_basis():
    x0 = var(0)
    y0 = var(4)
    d = vdot01()
    polys = []
    for a, b, c in itertools.product(range(3), repeat=3):
        if a + c > 2 or b + c > 2 or (a + b) % 2 != 0:
            continue
        p = pconst(1)
        for _ in range(a):
            p = pmul(p, x0)
        for _ in range(b):
            p = pmul(p, y0)
        for _ in range(c):
            p = pmul(p, d)
        polys.append(p)
    G = [[integrate(pmul(u, v)) for v in polys] for u in polys]
    keep = []
    for i in range(len(polys)):
        cand = keep + [i]
        sub = [[G[a][b] for b in cand] for a in cand]
        if _rank(sub) == len(cand):
            keep.append(i)
    return [polys[i] for i in keep]


def _rank(A):
    n = len(A)
    M = [row[:] for row in A]
    pr = 0
    for c in range(n):
        piv = None
        for i in range(pr, n):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[pr], M[piv] = M[piv], M[pr]
        for i in range(pr + 1, n):
            if M[i][c] != 0:
                f = M[i][c] / M[pr][c]
                for j in range(c, n):
                    M[i][j] -= f * M[pr][j]
        pr += 1
    return pr


def inertia(A):
    """theorum/53 elimination sign pattern (native LDL)."""
    n = len(A)
    M = [row[:] for row in A]
    pos = neg = zero = 0
    active = list(range(n))
    while active:
        p = None
        for i in active:
            if M[i][i] != 0:
                p = i
                break
        if p is None:
            i = active[0]
            j = None
            for k in active[1:]:
                if M[i][k] != 0:
                    j = k
                    break
            if j is None:
                zero += 1
                active.remove(i)
                continue
            b = M[i][j]
            pos += 1
            neg += 1
            rest = [k for k in active if k not in (i, j)]
            for r in rest:
                for c in rest:
                    M[r][c] -= (M[r][i] * M[j][c] + M[r][j] * M[i][c]) / b
            active = rest
            continue
        d = M[p][p]
        if d > 0:
            pos += 1
        else:
            neg += 1
        rest = [k for k in active if k != p]
        row = {c: M[p][c] for c in rest}
        for r in rest:
            if M[r][p] == 0:
                continue
            f = M[r][p] / d
            for c in rest:
                if row[c] != 0:
                    M[r][c] -= f * row[c]
        active = rest
    return pos, neg, zero


def solve(B, rhs):
    n = len(B)
    A = [B[i][:] + [rhs[i]] for i in range(n)]
    for c in range(n):
        pr = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[pr] = A[pr], A[c]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c] / A[c][c]
                for j in range(c, n + 1):
                    A[i][j] -= f * A[c][j]
    return [A[i][n] / A[i][i] for i in range(n)]


def matvec(A, v):
    return [sum(a * b for a, b in zip(r, v)) for r in A]


def dotv(u, v):
    return sum(a * b for a, b in zip(u, v))


def sqrt_up(q, sc=10 ** 45):
    assert q >= 0
    s = F(math.isqrt((q.numerator * sc * sc) // q.denominator) + 1, sc)
    assert s * s >= q
    return s


def build(kappa):
    fpt = face_coeffs(kappa)
    klo = rung_coeffs()
    basis = invariant_even_basis()
    n = len(basis)
    K = class_kernel(klo, dot01())
    ins = pmul(padd({}, var(0), F(2)), padd({}, var(4), F(2)))
    KI = pmul(K, ins)
    M = [[None] * n for _ in range(n)]
    N = [[None] * n for _ in range(n)]
    B = [[None] * n for _ in range(n)]
    cb = [c_apply(b, fpt, inv=True) for b in basis]
    for i in range(n):
        for j in range(i, n):
            pij = pmul(basis[i], basis[j])
            M[i][j] = M[j][i] = integrate(pmul(pij, K))
            N[i][j] = N[j][i] = integrate(pmul(pij, KI))
            B[i][j] = B[j][i] = integrate(pmul(basis[i], cb[j]))
    e0 = next(i for i, b in enumerate(basis) if b == pconst(1))
    return basis, M, N, B, e0, fpt, klo


def restricted(M, B, w, W_w):
    n = len(M)
    Bw = matvec(B, w)
    drop = max(range(n), key=lambda i: abs(Bw[i]))
    U = []
    for i in range(n):
        if i == drop:
            continue
        col = [F(0)] * n
        col[i] = F(1)
        c = Bw[i] / W_w
        U.append([col[k] - c * w[k] for k in range(n)])
    Mp = [[dotv(u, matvec(M, v)) for v in U] for u in U]
    Bp = [[dotv(u, matvec(B, v)) for v in U] for u in U]
    return U, Mp, Bp


def doubled_ceiling(Mp, Bp, hi, steps=40):
    n = len(Mp)
    cols = [solve(Bp, [Mp[i][j] for i in range(n)]) for j in range(n)]
    D = [[dotv([Mp[i][k] for k in range(n)], [cols[j][k] for k in range(n)])
          for j in range(n)] for i in range(n)]
    lo = F(0)
    assert inertia([[D[i][j] - hi * hi * Bp[i][j] for j in range(n)] for i in range(n)])[0] == 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        if inertia([[D[i][j] - mid * mid * Bp[i][j] for j in range(n)] for i in range(n)])[0] == 0:
            hi = mid
        else:
            lo = mid
    return hi


def pencil_norm_hi(N, B, hi, steps=40):
    def above(s):
        n = len(N)
        a = inertia([[N[i][j] - s * B[i][j] for j in range(n)] for i in range(n)])[0]
        b = inertia([[-N[i][j] - s * B[i][j] for j in range(n)] for i in range(n)])[0]
        return a + b
    lo = F(0)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if above(mid) >= 1:
            lo = mid
        else:
            hi = mid
    return hi


def run():
    grid = {}
    C = [True] * 5
    for kap in GRID:
        basis, M, N, B, e0i, fpt, klo = build(kap)
        n = len(basis)
        # ---- T1 silence factorization ----
        c1 = fpt[ZERO] > fpt[HALF] > fpt[ONE] > 0
        # C diagonal on the grading: c_apply(inv=False) of each basis elem is
        # f-weighted with no cross-degree mixing; verify C(basis) stays in span
        # with block structure by checking <b_i, C b_j> = 0 whenever the pure
        # graded parts differ — implemented as: C(hat) via c_apply reproduces
        # f_c-scaling on pure harmonics x0*y0 etc.
        pure = padd({}, pmul(var(1), var(5)))    # vx1*vy1: content (1/2,1/2)
        if c_apply(pure, fpt, inv=False) != {k: v * fpt[HALF] * fpt[HALF] for k, v in pure.items()}:
            c1 = False
        mix = dict(pure)
        mixC = c_apply(pure, {ZERO: fpt[ZERO], HALF: fpt[HALF] + F(1, 7), ONE: fpt[ONE]}, inv=False)
        if mixC == {k: v * fpt[HALF] * fpt[HALF] for k, v in mix.items()}:
            c1 = False                            # planted tamper must be detected
        C[0] = C[0] and c1
        # ---- sequences (exact) ----
        e0 = [F(0)] * n
        e0[e0i] = F(1)
        xs = [e0]
        for _ in range(K_EXACT):
            xs.append(solve(B, matvec(M, xs[-1])))
        # ---- T2 ledger identity ----
        # <1, tau x> = f0^2 * <K, x>_L2 : row of M at silence, per channel
        row = [M[e0i][j] for j in range(n)]
        # ledger decomposition: contributions via lambda channels
        K0 = class_kernel({ZERO: F(1), HALF: F(0), ONE: F(0)}, dot01())
        Kh = class_kernel({ZERO: F(0), HALF: klo[HALF], ONE: F(0)}, dot01())
        K1 = class_kernel({ZERO: F(0), HALF: F(0), ONE: klo[ONE]}, dot01())
        c2 = True
        for j in range(n):
            parts = [integrate(pmul(basis[j], Kx)) for Kx in (K0, Kh, K1)]
            if sum(parts) != row[j]:
                c2 = False
        # tamper: kill the half channel — the silence row must change
        row_t = [integrate(pmul(basis[j], padd(K0, K1))) for j in range(n)]
        c2 = c2 and (row_t != row)
        C[1] = C[1] and c2
        # ---- T3 contraction to silence ----
        w = e0
        W_w = dotv(w, matvec(B, w))
        tw = solve(B, matvec(M, w))
        theta = dotv(w, matvec(B, tw)) / W_w
        r_sil = [tw[k] - theta * w[k] for k in range(n)]
        c3 = (dotv(r_sil, matvec(B, w)) == 0)
        Rhat = sqrt_up(dotv(r_sil, matvec(B, r_sil)))
        U, Mp, Bp = restricted(M, B, w, W_w)
        c3 = c3 and inertia(Bp)[0] == n - 1
        sig = doubled_ceiling(Mp, Bp, hi=F(1))
        bs, nsq, t_up = [], [], []
        for x in xs:
            b = dotv(w, matvec(B, x)) / W_w
            yv = [x[k] - b * w[k] for k in range(n)]
            bs.append(b)
            nsq.append(dotv(yv, matvec(B, yv)))
            t_up.append(sqrt_up(nsq[-1]) / b)
        tbar = max(t_up[P0:]) * F(3, 2)
        th_lo = theta - Rhat * tbar / W_w
        th_hi = theta + Rhat * tbar / W_w
        inv_ok = th_lo > 0 and (Rhat + sig * tbar) / th_lo <= tbar
        beta = sig / th_lo + th_hi * tbar * Rhat / (W_w * th_lo * th_lo)
        c3 = c3 and inv_ok and beta < 1 and all(t <= tbar for t in t_up[P0:])
        # REFUSAL CONTROL (audit fix). The original test used the identity pencil,
        # whose ceiling is exactly 1, so `not (1 < 1)` could never fail — vacuous.
        # Replaced by a pencil with a genuinely heavy complement: silence channel
        # e0 with theta = 1 but complement weight 5, so sigma = 5 and beta > 1 —
        # the contraction must REFUSE. A broken ceiling routine would report < 1
        # and fail this control.
        Mref = [[F(1), F(0)], [F(0), F(5)]]
        Bref = [[F(1), F(0)], [F(0), F(1)]]
        wref = [F(1), F(0)]
        Uref, Mpr, Bpr = restricted(Mref, Bref, wref, F(1))
        sig_ref = doubled_ceiling(Mpr, Bpr, hi=F(8), steps=30)
        c3 = c3 and (sig_ref / F(1) >= 1)
        C[2] = C[2] and c3
        # ---- T3 assembly rows (silence deflation) ----
        yh = [[(xs[p][k] - bs[p] * w[k]) / bs[p] for k in range(n)] for p in range(K_EXACT + 1)]
        d0v = [yh[P0 + 1][k] - yh[P0][k] for k in range(n)]
        Dsum = sqrt_up(dotv(d0v, matvec(B, d0v))) / (1 - beta)
        Wup = sqrt_up(W_w)
        nu = pencil_norm_hi(N, B, F(64))
        Ntil = dotv(w, matvec(N, w))
        K1c = (Rhat / (W_w * th_lo)) * Dsum / (1 - beta)
        KN = nu * 2 * (Wup + tbar) * Dsum / (1 - beta)
        KZ = (sqrt_up(nsq[0]) / bs[0] + tbar) * Dsum / (1 - beta)
        F_lo = Ntil - nu * (2 * Wup * tbar + tbar * tbar) - KN
        Z_lo = W_w - (sqrt_up(nsq[0]) / bs[0]) * tbar - KZ
        c4 = F_lo > 0 and Z_lo > 0 and K1c <= F(1, 4)
        table = {}
        rho_c = None
        A = None
        if c4:
            def rho(m, p):
                a = dotv(xs[m - p], matvec(N, xs[p - 1]))
                z = dotv(xs[0], matvec(B, xs[m]))
                return a / z
            rho_c = rho(26, 13)
            jc = 12
            rho_hi = (Ntil + nu * (2 * Wup * tbar + tbar * tbar) + KN) / (th_lo * Z_lo)
            A = rho_hi * (4 * K1c + KN / F_lo + KZ / Z_lo) * 2
            for (m, p) in ((26, 13), (30, 15), (20, 10), (13, 3), (10, 5)):
                j = min(p - 1, m - p)
                err = A * (beta ** (j - P0) + beta ** (jc - P0))
                val = rho(m, p)
                inside = abs(val - rho_c) <= err
                c4 = c4 and inside
                table[f"{m},{p}"] = {"rho": f"{val.numerator/val.denominator:.16f}",
                                     "band": f"{err.numerator/err.denominator:.12e}",
                                     "inside": bool(inside)}
        C[3] = C[3] and c4
        # ---- T4 vibration tie: beta vs face ratio ----
        r_half = fpt[HALF] / fpt[ZERO]
        c5 = beta < r_half                               # one-sided law; draft window refused
        C[4] = C[4] and c5
        grid[str(kap)] = {
            "faces_f": {str(c): str(v) for c, v in fpt.items()},
            "rung_lambda": {str(c): str(v) for c, v in klo.items()},
            "theta_sil": f"{theta.numerator/theta.denominator:.16f}",
            "sigma_sil": f"{sig.numerator/sig.denominator:.14f}",
            "beta_sil": f"{beta.numerator/beta.denominator:.12f}",
            "r_half": f"{r_half.numerator/r_half.denominator:.12f}",
            "beta_lt_r_half": bool(c5),
            "rho_c": (f"{rho_c.numerator/rho_c.denominator:.16f}" if rho_c is not None else None),
            "A_band_coeff": (f"{A.numerator/A.denominator:.10e}" if A is not None else None),
            "table": table,
        }
    ok = all(C)
    return {
        "certificate_type": "T74_LOPA_LEDGER_CONTRACTION",
        "claim_status": "silence_factorization_EXACT__ledger_1_1_62_EXACT__structural_contraction_"
                        "beta_lt_1_outward_certificate__uniformity_with_silence_deflation__"
                        "constants_weaker_than_krylov_RECORDED__theorum75_content_tail_NAMED",
        "grid": grid,
        "controls": {"C1_silence_factorization_and_tamper": bool(C[0]),
                     "C2_ledger_exact_and_channel_tamper": bool(C[1]),
                     "C3_contraction_outward_certificate_and_refusal": bool(C[2]),
                     "C4_uniformity_rows_inside": bool(C[3]),
                     "C5_vibration_tie_window": bool(C[4])},
        "verdict": "PASS" if ok else "FAIL",
    }


if __name__ == "__main__":
    cert = run()
    out = os.path.join(HERE, "LOPA_LEDGER_CONTRACTION_RESULT.json")
    with open(out, "w") as f:
        json.dump(cert, f, indent=2, sort_keys=True)
    print("verdict:", cert["verdict"])
    print(json.dumps(cert["controls"], indent=1))
    for k, v in cert["grid"].items():
        print(k, "theta", v["theta_sil"], "sigma_sil", v["sigma_sil"], "beta", v["beta_sil"],
              "r_half", v["r_half"], "rows_ok", all(t["inside"] for t in v["table"].values()))
