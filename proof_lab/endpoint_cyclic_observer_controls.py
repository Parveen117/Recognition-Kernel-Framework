"""SE40 exact state-action and supplied-response controls; not an RH certificate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

from proof_lab.endpoint_rh_bridge_controls import derivative, evaluate, multiply


RESULT = Path(__file__).with_name("ENDPOINT_CYCLIC_OBSERVER_CONTROLS.json")


def state_polynomials(b, count):
    states = [[F(1)]]
    for n in range(1, count):
        p = [F(0)] * (n + 1)
        for j in range(n - 1, -1, -1):
            higher = p[j + 2] if j + 2 <= n else F(0)
            p[j + 1] = (states[-1][j] + (j+2)*(j+1)*higher) / (2*b*(j+1))
        states.append(p)
    return states


def complex_multiply(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def sine_integral(p, b, frequency):
    # Integral of p(x) exp(-b*x) sin(frequency*x), using exact Laplace moments.
    inv = (b/(b*b+frequency*frequency), frequency/(b*b+frequency*frequency))
    power = (F(1), F(0))
    total = F(0)
    for k, c in enumerate(p):
        power = complex_multiply(power, inv)
        total += c * factorial(k) * power[1]
    return total


def translate_polynomial(p, tau, degree):
    return [sum((p[j]*comb(j,k)*tau**(j-k) for j in range(k,len(p))), F(0))
            for k in range(degree+1)]


def response_moments(p, tau, count):
    # Taylor coefficients of 2*t*H'(t)/H(t), computed by series division.
    numerator = multiply([F(0), F(2)], derivative(p))
    h = translate_polynomial(p, tau, count)
    num = translate_polynomial(numerator, tau, count)
    quotient = []
    for n in range(count+1):
        quotient.append((num[n]-sum(h[j]*quotient[n-j] for j in range(1,n+1))) / h[0])
    return [(-1)**k*quotient[k+1] for k in range(count)]


def atom_moments(atoms, tau, count):
    return [sum((2*m*v/(tau+v)**(k+2) for v,m in atoms), F(0)) for k in range(count)]


def hankel(mu, size):
    return [[2*mu[i+j] for j in range(size)] for i in range(size)]


def determinant(matrix):
    a = [row[:] for row in matrix]
    det = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        value = a[j][j]
        det *= value
        for i in range(j+1,len(a)):
            q = a[i][j]/value
            for k in range(j+1,len(a)):
                a[i][k] -= q*a[j][k]
    return det


def encoded(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [encoded(v) for v in value]
    if isinstance(value, dict):
        return {k: encoded(v) for k,v in value.items()}
    return value


def replay():
    checks = []

    def require(name, condition):
        if not condition:
            raise ArithmeticError(name)
        checks.append(name)

    b, tau, d = F(5,2), F(25,4), F(4)
    polys = state_polynomials(b, 8)
    require("first two actual state polynomials have the derived normalization",
            polys[1] == [0,F(1,5)] and polys[2] == [0,F(1,125),F(1,50)])
    ode_ok = True
    for n in range(1,8):
        dp, ddp = derivative(polys[n]), derivative(derivative(polys[n]))
        result = [2*b*dp[j]-(ddp[j] if j<len(ddp) else 0) for j in range(len(dp))]
        ode_ok &= result == polys[n-1] and polys[n][0] == 0
    require("all seven Green-action recurrences and odd boundaries match", ode_ok)
    frequencies = [F(1,3),F(1),F(3),F(7)]
    require("independent Laplace integrals match 32 actual Fourier state readings",
            all(sine_integral(p,b,w) == w/(tau+w*w)**(n+1)
                for n,p in enumerate(polys) for w in frequencies))
    unreflected = [1/(4*b*b),1/(2*b)]
    require("dropping the reflected odd boundary creates a detectable constant mode",
            evaluate(unreflected,F(0)) == F(1,25)
            and sine_integral(unreflected,b,F(1)) != 1/(tau+1)**2)

    atoms = [(F(1),1),(F(2),2),(F(5),1)]
    polynomial = [F(1)]
    for v,m in atoms:
        for _ in range(m):
            polynomial = multiply(polynomial,[v,F(1)])
    mu = response_moments(polynomial,tau,15)
    require("15 complete rational-response jets equal independent atom moments",
            mu == atom_moments(atoms,tau,15))
    detached = [F(x) for x in json.loads(json.dumps(encoded(mu[:7])))]
    bank = hankel(detached,4)
    independent = [[sum(4*m*v/(tau+v)**(i+j+2) for v,m in atoms)
                    for j in range(4)] for i in range(4)]
    require("seven detached coefficients decode all 16 mixed readings", bank == independent)
    require("three positive sectors have positive leading minors and a genuine fourth null pivot",
            all(determinant([r[:n] for r in bank[:n]]) > 0 for n in (1,2,3))
            and determinant(bank) == 0)
    nu = [d**k*x for k,x in enumerate(detached)]
    normalized = hankel(nu,4)
    require("normalized readings are a diagonal congruence",
            normalized == [[d**i*bank[i][j]*d**j for j in range(4)] for i in range(4)])

    pair_mu = response_moments([F(2),F(2),F(1)],tau,3)
    pair_bank = hankel(pair_mu,2)
    require("positive diagonal jets do not exclude a negative mixed source direction",
            pair_bank[0][0]>0 and pair_bank[1][1]>0 and determinant(pair_bank)<0)

    offsets, n = [F(1),F(-1,2)], 5
    exact = sum(4*m*v/((tau+offsets[0]+v)*(tau+offsets[1]+v)) for v,m in atoms)
    approximation = sum(2*(-offsets[0])**i*(-offsets[1])**j*mu[i+j]
                        for i in range(n) for j in range(n))
    model_d = tau+min(v for v,_ in atoms)
    q,r = [abs(x)/model_d for x in offsets]
    bound = 2*mu[0]*(q**n+r**n)/((1-q)*(1-r))
    require("independent exact mixed response lies inside its analytic tail bound",
            abs(exact-approximation) <= bound and exact != approximation)

    transport = []
    delta, length = F(1), 7
    shifted = atom_moments(atoms,tau+delta,4)
    for k in range(4):
        approx = sum((-delta)**l*comb(k+l+1,l)*mu[k+l] for l in range(length))
        q = abs(delta)/model_d
        theta = q*F(k+length+2,length+1)
        tail = mu[0]*model_d**(-k)*comb(k+length+1,length)*q**length/(1-theta)
        transport.append({"order":k,"exact":shifted[k],"decoded":approx,"tail":tail})
    require("moving-calibration coefficient readings satisfy their negative-binomial tails",
            all(abs(row['exact']-row['decoded'])<=row['tail'] for row in transport))
    wrong = sum((-delta)**l*comb(l,l)*mu[l] for l in range(length))
    require("omitting the extra binomial factor is detected by the stated tail",
            abs(shifted[0]-wrong)>transport[0]['tail'])

    route = [F(25,4),F(9),F(49,4)]
    ratios = [abs(t-s)/(s-F(9,4)) for s,t in zip(route,route[1:])]
    require("overlapping calibrations repair an inadmissible single geometric step",
            (route[-1]-route[0])/d>1 and all(q<1 for q in ratios))
    sigma = route[-1]
    require("exact transport remains valid outside one local series disk",
            all(1/(sigma+w*w) == (1/(tau+w*w))/(1+(sigma-tau)/(tau+w*w))
                for w in frequencies))

    coeff = [F(1),F(-2),F(3)]
    errors = [(-1)**k*F(1,1000) for k in range(5)]
    actual_error = abs(sum(2*coeff[i]*coeff[j]*errors[i+j] for i in range(3) for j in range(3)))
    error_budget = sum(2*abs(coeff[i])*abs(coeff[j])*abs(errors[i+j]) for i in range(3) for j in range(3))
    require("measurement-error budget includes and attains all mixed terms", actual_error == error_budget)

    signed_moments = [F(1,2)**k-F(1,3)**k for k in range(3)]
    signed_bank = [[signed_moments[i+j] for j in range(2)] for i in range(2)]
    require("contractive source-symmetric action does not certify source positivity",
            signed_bank == [[0,F(1,6)],[F(1,6),F(5,36)]] and determinant(signed_bank)==F(-1,36))
    return encoded({
        "stage":"SE40",
        "scope":"Actual state-action identities and supplied rational response controls; no actual xi Hankel positivity or RH certificate.",
        "actual_action":{"tau":tau,"norm_upper":1/d,"polynomial_states":polys,"fourier_frequencies":frequencies},
        "detached_moment_bank":{"model_coefficients":polynomial,"moments":detached,"decoded_gram":bank,"normalized_gram":normalized},
        "negative_pair":{"moments":pair_mu,"gram":pair_bank,"determinant":determinant(pair_bank)},
        "mixed_recovery":{"offsets":offsets,"retained_count":n,"exact":exact,"decoded":approximation,"tail":bound},
        "calibration_transport":transport,
        "overlap_route":{"calibrations":route,"local_ratios":ratios},
        "measurement_error":{"actual":actual_error,"budget":error_budget},
        "contractive_negative_model":{"moments":signed_moments,"gram":signed_bank,"determinant":determinant(signed_bank)},
        "actual_analytic_kernel_bounds":{"scope":"|delta|,|epsilon|<=1 at tau=25/4; analytic bound, not eta", "N16":F(1376,27)*F(1,4)**16,"N32":F(1376,27)*F(1,4)**32},
        "checks":checks,"check_count":len(checks),
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write",action="store_true")
    mode.add_argument("--check",action="store_true")
    args = parser.parse_args()
    result = replay()
    if args.write:
        RESULT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    elif json.loads(RESULT.read_text(encoding="utf-8")) != result:
        raise SystemExit("Saved SE40 readings differ from exact replay")
    print(f"SE40: {result['check_count']} exact controls passed; no RH certificate")


if __name__ == "__main__":
    main()
