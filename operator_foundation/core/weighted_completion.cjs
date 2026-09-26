'use strict';
/** Finite certificates for the weighted native-completion theorems WC1-WC7.
 * Infinite objects are justified by the written completion proofs, not enumerated.
 * No positive pairing, coordinate adjoint, or physical clock is assumed.
 */
const {F, Cut} = require('./native_operator.cjs');
const {Presentation, daggerGate, star, digest} = require('./paninian_operator.cjs');
const min = (a, b) => a.le(b) ? a : b;
function nonnegative(x, name) {
  x = F.of(x);
  if (!new F(0).le(x)) throw new RangeError(name + ' must be nonnegative');
  return x;
}
function order(n) {
  if (!Number.isSafeInteger(n) || n < 0 || n > 512)
    throw new RangeError('Truncation order must be an integer from 0 to 512');
}
class WeightedCompletion {
  #s; #weights; #hash; #limits; #certificate;
  constructor(spec, weights, limits = {}) {
    this.#s = new Presentation(spec instanceof Presentation ? spec.spec() : spec);
    if (this.#s.objects.length !== 1)
      throw new TypeError('This completion implementation requires one declared object');
    if (!weights || typeof weights !== 'object' || Array.isArray(weights))
      throw new TypeError('Explicit positive rational generator weights required');
    const names = [...this.#s.order.keys()];
    if (Object.keys(weights).length !== names.length || names.some(g => !Object.hasOwn(weights, g)))
      throw new TypeError('Weights must cover exactly the declared generators');
    this.#weights = Object.fromEntries(names.map(g => {
      const x = F.of(weights[g]);
      if (x.zero() || !new F(0).le(x)) throw new RangeError('Strictly positive weights required');
      return [g, x];
    }));
    this.#limits = {maxSteps: 100000, maxTerms: 100000};
    for (const [key, value] of Object.entries(limits)) {
      if (!Object.hasOwn(this.#limits, key) || !Number.isSafeInteger(value) || value < 1 || value > 1000000)
        throw new RangeError('Invalid reduction budget');
      this.#limits[key] = value;
    }
    this.#hash = this.#s.hash();
    const audit = this.#s.audit(this.#limits);
    if (audit.status !== 'CONFLUENT_BY_CHECKED_DIAMONDS')
      throw new Error('A checked confluent presentation is required: ' + audit.status);
    const rules = this.#s.rules.map(r => ({
      rule: r.id, left_mass: this.wordWeight(r.lhs), right_mass: this.rawMass(r.rhs)
    }));
    if (rules.some(r => !r.right_mass.le(r.left_mass)))
      throw new Error('Weight contract fails; this does not reject the algebra itself');
    this.#certificate = {
      protocol: 'RKF_WEIGHTED_RULE_CONTRACT_V1', presentation_sha256: this.#hash,
      weights: this.#weights, rules, critical_pairs: audit.criticalPairs,
      norm_kind: 'real cut-gauge norm; bounded central cut-scalar action',
      basis_finiteness_required: false, primitive_hilbert_space: false
    };
  }
  get presentation() { return this.#s; }
  contract() { this.#unchanged(); return JSON.parse(JSON.stringify(this.#certificate)); }
  #unchanged() {
    if (this.#s.hash() !== this.#hash) throw new Error('Presentation changed after weight certification');
  }
  wordWeight(word) {
    this.#unchanged(); this.#s.wordType(word);
    return word.reduce((p, g) => p.mul(this.#weights[g]), new F(1));
  }
  rawMass(expr) {
    this.#unchanged();
    if (expr.system !== this.#s) throw new TypeError('Expression belongs to another presentation');
    return expr.entries().reduce((n, [w, c]) => n.add(c.gauge().mul(this.wordWeight(w))), new F(0));
  }
  normal(expr) { this.#unchanged(); return this.#s.reduce(expr, this.#limits).normal; }
  mass(expr) { return this.rawMass(this.normal(expr)); }
  mul(a, b) { return this.normal(a.times(b)); }
  add(a, b) { return this.normal(a.plus(b)); }
  sub(a, b) { return this.normal(a.minus(b)); }
  one() { this.#unchanged(); return this.#s.one(); }
  zero() { this.#unchanged(); return this.#s.zero(); }
  power(a, n) {
    order(n); let out = this.one();
    for (let k = 0; k < n; k++) out = this.mul(out, a);
    return out;
  }
  certifyDagger(images) {
    this.#unchanged();
    const gate = daggerGate(this.#s, images);
    if (gate.status !== 'DAGGER_DESCENDS') return {status: 'DAGGER_ALGEBRA_GATE_NOT_CLOSED', gate};
    const bounds = [...this.#s.order.keys()].map(g => ({
      generator: g, image_mass: this.mass(images[g]), allowed_mass: this.#weights[g]
    }));
    return {status: bounds.every(x => x.image_mass.le(x.allowed_mass)) ?
      'DAGGER_EXTENDS_ISOMETRICALLY' : 'DAGGER_WEIGHT_GATE_NOT_CLOSED', bounds};
  }
  inverseCertificate(a, x) {
    const left = this.sub(this.one(), this.mul(x, a));
    const right = this.sub(this.one(), this.mul(a, x));
    const qL = this.mass(left), qR = this.mass(right), mx = this.mass(x);
    const base = {left_residual: left.toJSON(), right_residual: right.toJSON(),
      left_mass: qL, right_mass: qR, approximate_inverse_mass: mx};
    if (!qL.le(1) || qL.eq(1) || !qR.le(1) || qR.eq(1))
      return {...base, status: 'TWO_SIDED_GATE_NOT_CLOSED', noninvertibility_proved: false};
    const kL = mx.div(new F(1).sub(qL)), kR = mx.div(new F(1).sub(qR));
    return {...base, status: 'TWO_SIDED_INVERSE_CERTIFIED',
      inverse_bound: min(kL, kR), error_bound: min(kL.mul(qL), kR.mul(qR))};
  }
  geometric(b, n) {
    order(n); const q = this.mass(b);
    let term = this.one(), approximation = term;
    for (let k = 1; k <= n; k++) { term = this.mul(term, b); approximation = this.add(approximation, term); }
    const residual = this.mul(term, b), a = this.sub(this.one(), b);
    const certificate = this.inverseCertificate(a, approximation);
    if (!this.normal(this.#s.fromJSON(certificate.left_residual)).equals(residual) ||
        !this.normal(this.#s.fromJSON(certificate.right_residual)).equals(residual))
      throw new Error('Exact geometric residual identity failed');
    const prior = q.le(1) && !q.eq(1) ? q.pow(n + 1).div(new F(1).sub(q)) : null;
    const bound = certificate.status === 'TWO_SIDED_INVERSE_CERTIFIED' ?
      (prior === null ? certificate.error_bound : min(prior, certificate.error_bound)) : prior;
    return {approximation, order: n, generator_mass: q, a_priori_tail: prior,
      certified_tail: bound, residual: residual.toJSON(), inverse_certificate: certificate};
  }
  exponential(a, n) {
    order(n); const r = this.mass(a);
    let term = this.one(), approximation = term;
    for (let k = 1; k <= n; k++) {
      term = this.mul(term, a).scale(new F(1, k));
      approximation = this.add(approximation, term);
    }
    const ratio = r.div(n + 2);
    if (!ratio.le(1) || ratio.eq(1))
      return {approximation, status: 'TAIL_GATE_NOT_CLOSED', divergence_proved: false};
    let first = new F(1);
    for (let k = 1; k <= n + 1; k++) first = first.mul(r).div(k);
    return {approximation, status: 'EXPONENTIAL_TAIL_CERTIFIED', order: n,
      tail: first.div(new F(1).sub(ratio)), next_term_bound: first, tail_ratio: ratio};
  }
  perturbation(a, x, delta) {
    const base = this.inverseCertificate(a, x);
    if (base.status !== 'TWO_SIDED_INVERSE_CERTIFIED') return {status: 'BASE_INVERSE_NOT_CERTIFIED', base};
    const epsilon = this.mass(delta), k = base.inverse_bound, rho = k.mul(epsilon);
    if (!rho.le(1) || rho.eq(1)) return {status: 'PERTURBATION_GATE_NOT_CLOSED', rho, singularity_proved: false};
    const margin = new F(1).sub(rho);
    return {status: 'PERTURBED_INVERSE_CERTIFIED', epsilon, rho,
      inverse_bound: k.div(margin), inverse_change_bound: k.pow(2).mul(epsilon).div(margin),
      first_order_remainder_bound: k.pow(3).mul(epsilon.pow(2)).div(margin),
      derivative: '-a_inverse * delta * a_inverse (factor order retained)'};
  }
  schurResponse({a, b, c, d, f, g, hiddenApprox, effectiveApprox}) {
    const hidden = this.inverseCertificate(d, hiddenApprox);
    if (hidden.status !== 'TWO_SIDED_INVERSE_CERTIFIED') return {status: 'HIDDEN_INVERSE_NOT_CERTIFIED', hidden};
    const bx = this.mul(b, hiddenApprox);
    const shat = this.sub(a, this.mul(bx, c));
    const fhat = this.sub(f, this.mul(bx, g));
    const effective = this.inverseCertificate(shat, effectiveApprox);
    if (effective.status !== 'TWO_SIDED_INVERSE_CERTIFIED') return {status: 'EFFECTIVE_INVERSE_NOT_CERTIFIED', hidden, effective};
    const eta = hidden.error_bound, mb = this.mass(b), mc = this.mass(c);
    const deltaS = mb.mul(eta).mul(mc), rho = effective.inverse_bound.mul(deltaS);
    if (!rho.le(1) || rho.eq(1)) return {status: 'MEMORY_TRANSFER_GATE_NOT_CLOSED', rho, hidden, effective};
    const k = effective.inverse_bound.div(new F(1).sub(rho));
    const u = this.mul(effectiveApprox, fhat), hiddenSource = this.sub(g, this.mul(c, u));
    const v = this.mul(hiddenApprox, hiddenSource);
    const residual = this.mass(this.sub(this.mul(shat, u), fhat));
    const memoryTerm = deltaS.mul(this.mass(u)), sourceTerm = mb.mul(eta).mul(this.mass(g));
    const uError = k.mul(residual.add(memoryTerm).add(sourceTerm));
    const vError = eta.mul(this.mass(hiddenSource)).add(hidden.inverse_bound.mul(mc).mul(uError));
    return {status: 'NATIVE_SCHUR_RESPONSE_CERTIFIED', visible: u, hidden: v,
      effective_operator: shat.toJSON(), effective_source: fhat.toJSON(),
      visible_error: uError, hidden_error: vError,
      budget: {solver_residual: residual, memory_operator_error: deltaS,
        memory_on_solution: memoryTerm, hidden_source_error: sourceTerm,
        effective_inverse_bound: k, transfer_ratio: rho},
      hidden_inverse: hidden, approximate_effective_inverse: effective};
  }
  nonlinearCertificate({source, linear = [], quadratic = [], radius}, approximation) {
    const r = nonnegative(radius, 'Radius');
    if (r.zero()) throw new RangeError('Use a strictly positive contraction radius');
    if (!Array.isArray(linear) || !Array.isArray(quadratic)) throw new TypeError('Explicit operator tuples required');
    for (const tuple of linear) if (!Array.isArray(tuple) || tuple.length !== 2) throw new TypeError('Linear tuple must be [left,right]');
    for (const tuple of quadratic) if (!Array.isArray(tuple) || tuple.length !== 3) throw new TypeError('Quadratic tuple must be [left,middle,right]');
    const beta = this.mass(source);
    const ell = linear.reduce((s, [a, b]) => s.add(this.mass(a).mul(this.mass(b))), new F(0));
    const q = quadratic.reduce((s, [a, b, c]) => s.add(this.mass(a).mul(this.mass(b)).mul(this.mass(c))), new F(0));
    const ballImage = beta.add(ell.mul(r)).add(q.mul(r.pow(2)));
    const kappa = ell.add(q.mul(r).mul(2));
    const gates = {radius: r, source_bound: beta, linear_bound: ell, quadratic_bound: q,
      ball_image_bound: ballImage, contraction_bound: kappa};
    if (!ballImage.le(r) || !kappa.le(1) || kappa.eq(1))
      return {...gates, status: 'NONLINEAR_BALL_GATE_NOT_CLOSED', nonexistence_proved: false};
    if (!this.mass(approximation).le(r)) return {...gates, status: 'APPROXIMATION_OUTSIDE_CERTIFIED_BALL'};
    let value = this.normal(source);
    for (const [a, b] of linear) value = this.add(value, this.mul(this.mul(a, approximation), b));
    for (const [a, b, c] of quadratic)
      value = this.add(value, this.mul(this.mul(this.mul(this.mul(a, approximation), b), approximation), c));
    const residual = this.mass(this.sub(value, approximation));
    return {...gates, status: 'UNIQUE_FIXED_POINT_IN_CERTIFIED_BALL', next_iterate: value,
      residual, error_bound: residual.div(new F(1).sub(kappa)), global_uniqueness_claimed: false};
  }
  coefficientError(word, massError) {
    if (this.#s.occurrences(word).length) throw new TypeError('Target coordinate must be an irreducible word');
    return nonnegative(massError, 'Mass error').div(this.wordWeight(word));
  }
}
module.exports = {WeightedCompletion};
