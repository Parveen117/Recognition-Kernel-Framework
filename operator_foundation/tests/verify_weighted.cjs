'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path'), crypto = require('node:crypto');
const o = require('../core/native_operator.cjs');
const p = require('../core/paninian_operator.cjs');
const wb = require('../core/workbench.cjs');
const {WeightedCompletion} = require('../core/weighted_completion.cjs');
const {F, Cut, matrix: M, identity: I, zeros: Z, mul, add, sub, scale, inverse, equal} = o;
const checks = [], details = {}; let exactProducts = 0;
function check(name, fn) { fn(); checks.push(name); }
const clone = x => JSON.parse(JSON.stringify(x));
const emk = {tokens:['R','K'],rules:[
  {id:'RR',lhs:['R','R'],rhs:[[[],-1]],source:'native EMK R^2=-I'},
  {id:'KK',lhs:['K','K'],rhs:[[[],1]],source:'native EMK K^2=I'},
  {id:'KR',lhs:['K','R'],rhs:[[['R','K'],-1]],source:'native EMK KR=-RK'}]};
const plane = {tokens:['X','Y'],rules:[
  {id:'YX',lhs:['Y','X'],rhs:[[['X','Y'],'1/2']],source:'declared infinite algebra, no physical identification'}]};
const E = new WeightedCompletion(emk,{R:1,K:1}), es = E.presentation;
const R = es.word(['R']), K = es.word(['K']), one = E.one();
const C = new WeightedCompletion(plane,{X:1,Y:1}), s = C.presentation;
const X=s.word(['X']),Y=s.word(['Y']),b=X.plus(Y).scale('1/4');
check('unit_has_mass_one_not_matrix_dimension',()=>assert(E.mass(one).eq(1)));
check('EMK_four_diamonds_and_three_weight_rules',()=>{assert.equal(E.contract().critical_pairs,4);assert.equal(E.contract().rules.length,3);});
check('infinite_normal_language_is_retained',()=>assert.equal(wb.finiteBasis(s).status,'INFINITE_IRREDUCIBLE_LANGUAGE'));
check('no_primitive_pairing_in_completion_contract',()=>assert.equal(C.contract().primitive_hilbert_space,false));
check('weights_missing_generator_rejected',()=>assert.throws(()=>new WeightedCompletion(plane,{X:1}),/Weights/));
check('weights_extra_generator_rejected',()=>assert.throws(()=>new WeightedCompletion(plane,{X:1,Y:1,Z:1}),/Weights/));
check('nonpositive_weights_rejected',()=>assert.throws(()=>new WeightedCompletion(plane,{X:0,Y:1}),/positive/));
check('floating_weight_rejected',()=>assert.throws(()=>new WeightedCompletion(plane,{X:0.5,Y:1}),TypeError));
check('relation_mass_violation_refused',()=>assert.throws(()=>new WeightedCompletion(emk,{R:'1/2',K:1}),/Weight contract/));
check('nonconfluent_input_refused_before_completion',()=>assert.throws(()=>new WeightedCompletion({tokens:['X'],rules:[
  {id:'x0',lhs:['X'],rhs:[],source:'bad fork'},{id:'x1',lhs:['X'],rhs:[[[],1]],source:'bad fork'}]},{X:1}),/confluent/));
check('uncertified_differential_weight_not_false_algebra_rejection',()=>{
  const spec={tokens:['X','D'],rules:[{id:'DX',lhs:['D','X'],rhs:[[['X','D'],1],[[],1]],source:'Weyl test presentation'}]};
  assert.equal(new p.Presentation(spec).audit().status,'CONFLUENT_BY_CHECKED_DIAMONDS');
  assert.throws(()=>new WeightedCompletion(spec,{X:1,D:1}),/does not reject the algebra/);
});
check('post_certificate_rule_mutation_rejected',()=>{
  const a=new WeightedCompletion({tokens:['X'],rules:[]},{X:1}), x=a.presentation.word(['X']);
  a.presentation.addRule({id:'x',lhs:['X'],rhs:[],source:'late alteration'});
  assert.throws(()=>a.mass(x),/changed after/);
});
check('cross_presentation_expression_rejected',()=>assert.throws(()=>E.mass(X),/another presentation|Presentation/));
check('unknown_weight_option_refused',()=>assert.throws(()=>new WeightedCompletion(plane,{X:1,Y:1},{skipProof:true}),/budget/));
check('exact_qplane_products_256_cases',()=>{
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)for(let l=0;l<4;l++){
    const u=s.word(Array(i).fill('X').concat(Array(j).fill('Y')));
    const v=s.word(Array(k).fill('X').concat(Array(l).fill('Y')));
    const expected=s.word(Array(i+k).fill('X').concat(Array(j+l).fill('Y')),new F(1,2).pow(j*k));
    const actual=C.mul(u,v);assert(actual.equals(expected));assert(C.mass(actual).le(C.mass(u).mul(C.mass(v))));exactProducts++;
  }
});
check('unequal_generator_weights_track_normal_coordinates',()=>{
  const w=new WeightedCompletion(plane,{X:2,Y:3}), q=w.presentation;
  assert(w.mass(q.word(['Y','X'])).eq(3));assert(w.wordWeight(['X','X','Y']).eq(12));
});
check('normal_mass_uses_reduced_not_raw_expression',()=>{const z=R.times(R).plus(one);assert(E.rawMass(z).eq(2));assert(E.mass(z).zero());});
const dg={X:Y,Y:X};
check('native_dagger_extends_after_its_own_gate',()=>assert.equal(C.certifyDagger(dg).status,'DAGGER_EXTENDS_ISOMETRICALLY'));
check('dagger_mass_invariance_on_noncommutative_expression',()=>{
  const z=X.times(Y).scale(new Cut(2,1)).plus(X.scale('-2/3'));
  assert(C.mass(p.star(z,dg)).eq(C.mass(z)));
});
check('dagger_without_compatible_weights_not_promoted',()=>{
  const w=new WeightedCompletion(plane,{X:1,Y:2}), t=w.presentation;
  assert.equal(w.certifyDagger({X:t.word(['Y']),Y:t.word(['X'])}).status,'DAGGER_WEIGHT_GATE_NOT_CLOSED');
});
const reference=C.geometric(b,12).approximation;
for(let n=0;n<=8;n++)check('infinite_geometric_tail_'+n,()=>{
  const z=C.geometric(b,n);assert.equal(z.inverse_certificate.status,'TWO_SIDED_INVERSE_CERTIFIED');
  assert(z.a_priori_tail.eq(new F(1,2).pow(n))); // (1/2)^(n+1)/(1-1/2)
  assert(C.mass(reference.minus(z.approximation)).le(z.certified_tail));
  assert(C.normal(s.fromJSON(z.residual)).equals(C.power(b,n+1)));
});
const g8=C.geometric(b,8);
check('qplane_45_term_infinite_inverse_demonstration',()=>{
  assert.equal(g8.approximation.terms.size,45);assert(g8.a_priori_tail.eq('1/256'));
  assert(g8.certified_tail.le(g8.a_priori_tail));
  details.infinite_example={relation:'YX=(1/2)XY',normal_basis:'X^i Y^j, i,j>=0',order:8,
    retained_monomials:45,prior_tail:g8.a_priori_tail,residual_tail:g8.certified_tail,
    computed_residual_mass:g8.inverse_certificate.left_mass};
});
check('one_sided_inverse_is_not_two_sided',()=>{
  const A=new WeightedCompletion({tokens:['S','T'],rules:[{id:'TS',lhs:['T','S'],rhs:[[[],1]],source:'one-sided inverse control'}]},{S:1,T:1});
  const t=A.presentation, z=A.inverseCertificate(t.word(['S']),t.word(['T']));
  assert(z.left_mass.zero());assert(z.right_mass.eq(2));assert.equal(z.status,'TWO_SIDED_GATE_NOT_CLOSED');
});
check('power_sharpening_accepts_mass_greater_than_one',()=>{
  const A=new WeightedCompletion({tokens:['N'],rules:[{id:'N2',lhs:['N','N'],rhs:[],source:'native jet relation'}]},{N:1});
  const z=A.geometric(A.presentation.word(['N'],5),1);
  assert(z.generator_mass.eq(5));assert(z.certified_tail.zero());assert.equal(z.a_priori_tail,null);
});
check('inverse_gate_failure_does_not_assert_singularity',()=>{
  const z=E.inverseCertificate(one.scale(2),one);assert.equal(z.noninvertibility_proved,false);
});
check('exponential_tail_dominates_later_partial_sum',()=>{
  const z=C.exponential(b,4), later=C.exponential(b,10);
  assert.equal(z.status,'EXPONENTIAL_TAIL_CERTIFIED');assert(C.mass(later.approximation.minus(z.approximation)).le(z.tail));
});
check('exponential_weak_tail_gate_is_not_divergence',()=>{
  const z=C.exponential(X.scale(3),0);assert.equal(z.status,'TAIL_GATE_NOT_CLOSED');assert.equal(z.divergence_proved,false);
  assert.equal(C.exponential(X.scale(3),4).status,'EXPONENTIAL_TAIL_CERTIFIED');
});
const rm=M([[0,-1],[1,0]]),km=M([[0,1],[1,0]]),mat={R:rm,K:km};
const evaluate=e=>p.matrixValue(e,mat,2);
function fromMatrix(a){
  const two=new Cut(2), v=[a[0][0].add(a[1][1]).div(two),a[1][0].sub(a[0][1]).div(two),
    a[0][1].add(a[1][0]).div(two),a[1][1].sub(a[0][0]).div(two)];
  return [one,R,K,R.times(K)].reduce((s,x,i)=>s.plus(x.scale(v[i])),E.zero());
}
const invert=e=>fromMatrix(inverse(evaluate(e)));
const a=one.scale(2).plus(R), ai=one.scale(2).minus(R).scale('1/5'), h=K.scale('1/10');
check('noncentral_inverse_perturbation_bound',()=>{
  const z=E.perturbation(a,ai,h), actual=invert(a.plus(h));
  assert.equal(z.status,'PERTURBED_INVERSE_CERTIFIED');assert(E.mass(actual.minus(ai)).le(z.inverse_change_bound));
  const rem=actual.minus(ai).plus(E.mul(E.mul(ai,h),ai));assert(E.mass(rem).le(z.first_order_remainder_bound));
});
check('inverse_derivative_factor_order_matters',()=>assert(!E.mul(E.mul(ai,h),ai).equals(E.mul(E.mul(ai,ai),h))));
check('perturbation_boundary_refused_not_called_singular',()=>{
  const z=E.perturbation(one,one,R);assert.equal(z.status,'PERTURBATION_GATE_NOT_CLOSED');assert.equal(z.singularity_proved,false);
});
function fullSolve(a,b,c,d,f,g){
  const A=evaluate(a), B=evaluate(b), C=evaluate(c), D=evaluate(d), F=evaluate(f), G=evaluate(g);
  const block=M(A.map((row,i)=>row.concat(B[i])).concat(C.map((row,i)=>row.concat(D[i]))));
  const sol=mul(inverse(block),M(F.concat(G)));
  return {u:fromMatrix(sol.slice(0,2)),v:fromMatrix(sol.slice(2))};
}
const block={a:one.scale(2),b:R.scale('1/4'),c:K.scale('1/4'),d:one.minus(R.scale('1/2')),
  f:one,g:K.scale('1/3'),hiddenApprox:one.plus(R.scale('1/2')),effectiveApprox:one.scale('1/2')};
for(const g of [E.zero(),K.scale('1/3'),R.scale('1/5').plus(one.scale('1/7'))])check('Schur_full_system_error_'+checks.length,()=>{
  const z=E.schurResponse({...block,g}), actual=fullSolve(block.a,block.b,block.c,block.d,block.f,g);
  assert.equal(z.status,'NATIVE_SCHUR_RESPONSE_CERTIFIED');assert(E.mass(actual.u.minus(z.visible)).le(z.visible_error));
  assert(E.mass(actual.v.minus(z.hidden)).le(z.hidden_error));
  if(g===block.g)details.schur_example={visible_error:z.visible_error,hidden_error:z.hidden_error,budget:z.budget};
});
check('Schur_summary_has_three_separate_error_sources',()=>{
 const z=E.schurResponse(block),actual=fullSolve(block.a,block.b,block.c,block.d,block.f,block.g);
 assert(!z.budget.hidden_source_error.zero());
 details.schur_example={visible:z.visible.toJSON(),actual_visible:actual.u.toJSON(),
   measured_mass_error:E.mass(actual.u.minus(z.visible)),proved_visible_error:z.visible_error,
   proved_hidden_error:z.hidden_error,budget:z.budget};
});
check('exact_hidden_source_dressing_is_load_bearing',()=>{
  const dx=invert(block.d), shat=E.sub(block.a,E.mul(E.mul(block.b,dx),block.c)), sx=invert(shat);
  const z=E.schurResponse({...block,hiddenApprox:dx,effectiveApprox:sx}),truth=fullSolve(block.a,block.b,block.c,block.d,block.f,block.g);
  assert(z.visible_error.zero());assert(E.normal(z.visible).equals(E.normal(truth.u)));
  assert(!E.mul(sx,block.f).equals(E.normal(truth.u)));
});
function eliminate(B,f,k){
  const keep=B.map((_,i)=>i).filter(i=>i!==k),di=invert(B[k][k]);
  return {B:keep.map(i=>keep.map(j=>E.sub(B[i][j],E.mul(E.mul(B[i][k],di),B[k][j])))),
    f:keep.map(i=>E.sub(f[i],E.mul(E.mul(B[i][k],di),f[k])))};
}
check('nested_elimination_order_with_noncommuting_blocks',()=>{
  const B=[[one.scale(3),R.scale('1/3'),K.scale('1/4')],
    [K.scale('1/5'),one.scale(2),R.scale('1/6')],
    [R.scale('1/7'),K.scale('1/8'),one.scale(4)]],f=[one,R,K];
  const q=eliminate(B,f,2),p1=eliminate(q.B,q.f,1),t=eliminate(B,f,1),p2=eliminate(t.B,t.f,1);
  assert(p1.B[0][0].equals(p2.B[0][0]));assert(p1.f[0].equals(p2.f[0]));
});
check('Schur_missing_hidden_inverse_fails_closed',()=>assert.equal(E.schurResponse({...block,d:E.zero()}).status,'HIDDEN_INVERSE_NOT_CERTIFIED'));
check('coordinate_error_bound_uses_declared_weight',()=>{
  const w=new WeightedCompletion(plane,{X:2,Y:3});assert(w.coefficientError(['X','Y'],'1/10').eq('1/60'));
});
check('reducible_word_is_not_a_basis_coordinate',()=>assert.throws(()=>C.coefficientError(['Y','X'],1),/irreducible/));
check('negative_error_bound_refused',()=>assert.throws(()=>C.coefficientError(['X'],-1),/nonnegative/));
const zstar=one.plus(R).scale('1/16'),linear=[[K.scale('1/8'),K]],quadratic=[[one,R.scale('1/16'),one]];
const source=E.sub(E.sub(zstar,E.mul(E.mul(linear[0][0],zstar),linear[0][1])),
  E.mul(E.mul(E.mul(E.mul(quadratic[0][0],zstar),quadratic[0][1]),zstar),quadratic[0][2]));
const nonlinear={source,linear,quadratic,radius:'1/4'};let z=E.zero();
for(let i=0;i<7;i++)check('nonlinear_residual_certificate_iteration_'+i,()=>{
  const c=E.nonlinearCertificate(nonlinear,z);assert.equal(c.status,'UNIQUE_FIXED_POINT_IN_CERTIFIED_BALL');
  assert(E.mass(zstar.minus(z)).le(c.error_bound));assert(c.contraction_bound.eq('5/32'));
  if(i===3)details.nonlinear_example={manufactured_exact_fixture:true,contraction:c.contraction_bound,
    ball_radius:c.radius,iteration:i,residual:c.residual,error_bound:c.error_bound,
    actual_error:E.mass(zstar.minus(z)),global_uniqueness:c.global_uniqueness_claimed};
  z=c.next_iterate;
});
check('nonlinear_exact_solution_has_zero_residual',()=>assert(E.nonlinearCertificate(nonlinear,zstar).residual.zero()));
check('nonlinear_failed_ball_does_not_prove_nonexistence',()=>{
  const c=E.nonlinearCertificate({...nonlinear,source:one.scale(2)},E.zero());assert.equal(c.nonexistence_proved,false);
});
check('nonlinear_outside_approximation_refused',()=>assert.equal(E.nonlinearCertificate(nonlinear,one).status,'APPROXIMATION_OUTSIDE_CERTIFIED_BALL'));
check('nonlinear_invalid_tuple_refused',()=>assert.throws(()=>E.nonlinearCertificate({...nonlinear,linear:[[R]]},E.zero()),/Linear tuple/));
const root=path.resolve(__dirname,'..'),sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const files=['core/weighted_completion.cjs','theory/WEIGHTED_OPERATOR_COMPLETION.md','tests/verify_weighted.cjs'];
const report={protocol:'RKF_WEIGHTED_COMPLETION_V0_5',status:'PASS_EXACT_FINITE_CERTIFICATES',check_count:checks.length,
  exact_qplane_products:exactProducts,checks,details,source_sha256:Object.fromEntries(files.map(f=>[f,sha(fs.readFileSync(path.join(root,f)))])),
  scope:{infinite_theorems:'WC1-WC7 written proofs under explicit hypotheses',infinite_series_enumerated:false,
    primitive_hilbert_space:false,physical_source_identification:false,independent_proof_assistant:false}};
const text=JSON.stringify(report,null,2)+'\n',hash=sha(text);
if(process.argv.includes('--write')){fs.writeFileSync(path.join(root,'audit/WEIGHTED_COMPLETION_CERTIFICATE.json'),text);fs.writeFileSync(path.join(root,'audit/WEIGHTED_EXPECTED.sha256'),hash+'\n');}
if(process.argv.includes('--check')){assert.equal(fs.readFileSync(path.join(root,'audit/WEIGHTED_COMPLETION_CERTIFICATE.json'),'utf8'),text);assert.equal(fs.readFileSync(path.join(root,'audit/WEIGHTED_EXPECTED.sha256'),'utf8').trim(),hash);}
if(process.argv.includes('--json'))console.log(JSON.stringify(report));else console.log('PASS_WEIGHTED_COMPLETION',checks.length,hash);
