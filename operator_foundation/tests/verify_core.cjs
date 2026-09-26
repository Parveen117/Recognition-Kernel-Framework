'use strict';
/** Independent exact finite regressions; not a proof assistant or an experiment. */
const assert=require('node:assert/strict');
const fs=require('node:fs');const path=require('node:path');const crypto=require('node:crypto');
const o=require('../core/native_operator.cjs');
const {F,Cut,IOTA,matrix:M,identity:Id,zeros:Z,add,sub,scale,mul,dagger,equal,mass,energy,isZero,power,kron,rank,inverse,cayley,commutator,rowClosure,operatorAlgebra,descendedAction,idealReadoutClosureFullMatrix,resolvent,neumann}=o;
const checks=[];const details={};
function check(name,fn){fn();checks.push(name);}
function eq(a,b){assert(equal(a,b));}
function scalar(a,b){assert(Cut.of(a).eq(b));}
function det2(a){return a[0][0].mul(a[1][1]).sub(a[0][1].mul(a[1][0]));}
const R=M([[0,-1],[1,0]]),K=M([[0,1],[1,0]]),P=M([[1,0],[0,0]]),Q=sub(Id(2),P);
check('iota_squared_minus_one',()=>scalar(IOTA.mul(IOTA),-1));
check('dagger_reverses_iota',()=>scalar(IOTA.dagger(),IOTA.neg()));
check('fraction_normalization',()=>assert(new F('-6/-8').eq('3/4')));
check('reject_float_input',()=>assert.throws(()=>new F(0.1),TypeError));
check('reject_zero_denominator',()=>assert.throws(()=>new F(1,0),RangeError));
check('reject_zero_scalar_inverse',()=>assert.throws(()=>new Cut().inv(),RangeError));
check('reject_ragged_matrix',()=>assert.throws(()=>M([[1,0],[1]]),TypeError));
check('reject_invalid_carrier',()=>assert.throws(()=>mul(M([[1,0]]),M([[1]])),RangeError));
let scalarProducts=0;
check('exhaustive_scalar_dagger_norm_gauge_625_products',()=>{
  for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
    const x=new Cut(a,b),y=new Cut(c,d),p=x.mul(y);
    scalar(p,new Cut(a*c-b*d,a*d+b*c));scalar(p.dagger(),y.dagger().mul(x.dagger()));
    assert(p.norm2().eq(x.norm2().mul(y.norm2())));assert(p.gauge().le(x.gauge().mul(y.gauge())));
    if(!x.zero())scalar(x.mul(x.inv()),1);scalarProducts++;
  }
});
check('mixed_phase_mass_is_not_multiplicative',()=>{
  const a=new Cut(1,1);assert(a.mul(a).gauge().eq(2));assert(a.gauge().mul(a.gauge()).eq(4));
});
check('T50_admissible_mixed_face_counterexample',()=>{
  const d=M([[0,[1,1]],[0,0]]),b=scale(add(Id(2),d),'1/8');eq(power(d,2),Z(2));
  assert(mass(b).eq('1/2'));assert(mass(kron(b,b)).eq('7/32'));assert(mass(kron(b,b)).le(mass(b).pow(2)));
  details.tensor_mass={one_face:mass(b),two_faces:mass(kron(b,b)),product_bound:mass(b).pow(2)};
});
let seed=20260926;
function ri(){seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return (seed>>>0)%5-2;}
function sample(){return Array.from({length:2},()=>Array.from({length:2},()=>new Cut(new F(ri(),3),new F(ri(),5))));}
for(let j=0;j<40;j++){
  const a=sample(),b=sample(),c=sample(),v=M([[new Cut(ri(),ri())],[new Cut(ri(),ri())]]);
  check(`native_composition_and_mass_${j}`,()=>{
    eq(mul(mul(a,b),c),mul(a,mul(b,c)));eq(dagger(mul(a,b)),mul(dagger(b),dagger(a)));
    assert(mass(mul(a,b)).le(mass(a).mul(mass(b))));assert(mass(kron(a,b)).le(mass(a).mul(mass(b))));
    assert(energy(mul(a,v)).le(mass(a).pow(2).mul(energy(v))));
    eq(sub(mul(mul(P,mul(a,b)),P),mul(mul(mul(P,a),P),mul(b,P))),mul(mul(mul(mul(P,a),Q),b),P));
  });
}
check('EMK_R_square',()=>eq(power(R,2),scale(Id(2),-1)));
check('EMK_K_square',()=>eq(power(K,2),Id(2)));
check('EMK_mixed_commutator',()=>eq(commutator(R,K),scale(mul(R,K),2)));
check('EMK_generated_full_cut_matrix_algebra',()=>{
  const a=operatorAlgebra([R,K]);assert.equal(a.dimension,4);details.EMK_algebra_dimension=a.dimension;details.EMK_algebra_rank_steps=a.ranks;
});
check('diagonal_family_not_full_matrix_algebra',()=>assert.equal(operatorAlgebra([M([[1,0],[0,-1]])]).dimension,2));
check('full_algebra_adapter_rejects_diagonal_family',()=>assert.throws(()=>idealReadoutClosureFullMatrix([[1,0,0,0]],[M([[1,0],[0,-1]])]),RangeError));
check('single_state_readout_needs_one_complex_channel_repair',()=>{
  const a=rowClosure([[1,0]],[R,K],{includeDagger:true});assert.equal(a.rank,2);assert.equal(a.extra,1);
  eq(descendedAction(R,a.observer),R);details.module_repair={initial_complex_channels:1,completed_complex_channels:a.rank,extra_complex_channels:a.extra};
});
check('unrepaired_state_readout_does_not_descend',()=>assert.equal(descendedAction(K,[[1,0]]),null));
check('zero_readout_stays_zero',()=>assert.equal(rowClosure([[0,0]],[R,K]).rank,0));
check('no_generators_gives_no_extra_channels',()=>assert.equal(rowClosure([[1,0]],[]).extra,0));
check('redundant_seed_rows_do_not_count_as_extra_information',()=>assert.equal(rowClosure([[1,0],[2,0]],[K]).extra,1));
check('forward_invariance_differs_from_dagger_closure',()=>{
  const g=M([[0,1],[0,0]]);assert.equal(rowClosure([[0,1]],[g]).rank,1);assert.equal(rowClosure([[0,1]],[g],{includeDagger:true}).rank,2);
});
check('proper_lossy_module_with_disconnected_memory',()=>{
  const g=M([[0,1,0],[1,0,0],[0,0,2]]),a=rowClosure([[1,0,0]],[g],{includeDagger:true});
  assert.equal(a.rank,2);assert.equal(a.extra,1);eq(descendedAction(g,a.observer),K);
});
for(let i=0;i<4;i++)check(`nonzero_full_algebra_readout_needs_all_four_coordinates_${i}`,()=>{
  const c=[Array.from({length:4},(_,j)=>Number(i===j))];const a=idealReadoutClosureFullMatrix(c,[R,K]);assert.equal(a.rank,4);assert.equal(a.extra,3);
  if(i===0)details.algebra_quotient_repair={initial_complex_functionals:1,completed_complex_functionals:4,extra_complex_functionals:3};
});
check('zero_algebra_readout_has_zero_quotient',()=>assert.equal(idealReadoutClosureFullMatrix([[0,0,0,0]],[R,K]).rank,0));
check('compression_not_multiplicative',()=>{eq(mul(mul(P,power(K,2)),P),P);eq(power(mul(mul(P,K),P),2),Z(2));});
check('cut_square_multiplicativity_defect_is_returning_memory',()=>{
  const a=new Cut(3,2),b=M([[1,a],[0,2]]);eq(sub(mul(mul(P,mul(dagger(b),b)),P),mul(mul(mul(P,dagger(b)),P),mul(b,P))),mul(dagger(mul(mul(Q,b),P)),mul(mul(Q,b),P)));
});
check('native_mass_is_not_C_star_norm',()=>{
  const p=Id(2);assert(mass(mul(dagger(p),p)).eq(2));assert(mass(p).pow(2).eq(4));
  details.C_star_counterexample={projection_mass:mass(p),square_mass:mass(mul(dagger(p),p)),mass_squared:mass(p).pow(2)};
});
for(const t of ['1/2','1/3','-2/5'])check(`Cayley_native_dagger_unitarity_${t}`,()=>{
  const g=add(scale(R,'2/3'),scale(K,new Cut(0,'1/4'))),u=cayley(g,t);eq(dagger(g),scale(g,-1));eq(mul(dagger(u),u),Id(2));eq(cayley(g,new F(t).neg()),inverse(u));
});
check('bare_K_is_not_skew_dagger_generator',()=>assert(!equal(dagger(K),scale(K,-1))));
check('matrix_inverse_independent_two_by_two_formula',()=>{
  const a=M([[[2,1],1],[1,[3,-1]]]),d=det2(a);const direct=scale(M([[a[1][1],a[0][1].neg()],[a[1][0].neg(),a[0][0]]]),d.inv());eq(inverse(a),direct);
});
check('singular_inverse_rejected',()=>assert.throws(()=>inverse(M([[1,1],[1,1]])),RangeError));
check('resolvent_identity_at_two_cut_scalars',()=>{
  const a=M([[['1/5','1/7'],'1/9'],[0,'1/8']]),l=new Cut(2,1),m=new Cut(3,-1),rl=resolvent(a,l),rm=resolvent(a,m);
  eq(sub(rl,rm),scale(mul(rl,rm),m.sub(l)));
});
const bounded=M([[['1/8','1/16'],'1/10'],[0,'1/12']]);
for(let n=0;n<=10;n++)check(`native_Neumann_tail_order_${n}`,()=>{
  const z=new Cut(2,1),b=neumann(bounded,z,n),error=mass(sub(resolvent(bounded,z),b.approximation));assert(error.le(b.tail));
  if(n===10)details.neumann={q:b.q,order:n,actual_mass_error:error,declared_tail:b.tail};
});
check('Neumann_failure_is_not_noninvertibility',()=>{
  const a=scale(Id(2),2);eq(resolvent(a,3),Id(2));assert.throws(()=>neumann(a,3,4),RangeError);
});
check('local_resolvent_expansion_inside_shifted_chart',()=>{
  const a=M([[2,1],[0,2]]),r0=resolvent(a,4),h=new Cut('1/10','1/20');const rl=resolvent(a,new Cut(4).add(h));
  eq(sub(rl,r0),scale(mul(rl,r0),h.neg()));
});
check('nilpotent_native_exponential_addition_for_one_generator',()=>{
  const n=M([[0,1,0],[0,0,[1,1]],[0,0,0]]);eq(power(n,3),Z(3));
  function e(t){return add(add(Id(3),scale(n,t)),scale(power(n,2),F.of(t).pow(2).div(2)));}
  eq(mul(e('1/3'),e('2/5')),e(new F('1/3').add('2/5')));
});
check('noncommuting_exponential_addition_is_not_automatic',()=>{
  const a=M([[0,1],[0,0]]),b=M([[0,0],[1,0]]);assert(!equal(mul(add(Id(2),a),add(Id(2),b)),mul(add(Id(2),b),add(Id(2),a))));
});
const u=M([['3/5','-4/5'],['4/5','3/5']]),xs=[new Cut(2)],ys=[new Cut('1/3')];
for(let n=0;n<10;n++){
  const full=mul(u,M([[xs[n]],[ys[n]]]));
  let memory=u[0][0].mul(xs[n]).add(u[0][1].mul(new Cut('3/5').rad.pow(n)).mul(ys[0]));
  for(let j=0;j<n;j++)memory=memory.add(u[0][1].mul(new F('3/5').pow(n-1-j)).mul(u[1][0]).mul(xs[j]));
  check(`exact_discrete_memory_step_${n+1}`,()=>scalar(memory,full[0][0]));xs.push(full[0][0]);ys.push(full[1][0]);
}
check('memory_return_changes_two_step_prediction',()=>{
  const x=M([[1],[0]]);scalar(mul(power(K,2),x)[0][0],1);scalar(power(M([[K[0][0]]]),2)[0][0],0);
  details.memory_return={full_two_step:'1',memory_reset_two_step:'0'};
});
check('Schur_source_response_equals_full_resolvent_corner',()=>{
  const z=new Cut(2),effective=z.sub(new Cut(1).div(z)).inv();scalar(resolvent(K,z)[0][0],effective);scalar(effective,'2/3');
  details.Schur_response={with_memory:'2/3',naive_corner:'1/2'};
});
for(let n=1;n<=12;n++)check(`finite_faithfulness_not_uniform_decoder_bound_${n}`,()=>{
  const c=Z(n);for(let j=0;j<n;j++)c[j][j]=new Cut(new F(1,j+1));assert.equal(rank(c),n);
  const e=Z(n,1);e[n-1][0]=new Cut(1);assert(mass(e).div(mass(mul(c,e))).eq(n));
});
function plane(y){const j=M([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]),g=mul(dagger(y),y),a=scale(mul(mul(dagger(y),j),y),-1);return det2(a).div(det2(g));}
const yp=M([[1,0],[0,1],[0,1],[0,0]]);
check('QG_chi_fixture',()=>scalar(plane(yp),'1/2'));
check('QG_chi_is_blind_to_common_source_amplitude',()=>{for(const s of [2,3,-1])scalar(plane(scale(yp,s)),plane(yp));});
check('QG_chi_changes_under_complex_compatible_lossy_cut',()=>scalar(plane(mul(M([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]),yp)),1));
check('same_local_two_jet_does_not_select_global_warp',()=>{
  function k(w,w1,w2){return F.of(w1).pow(2).div(F.of(w).pow(2).mul(4)).sub(F.of(w2).div(F.of(w).mul(2)));}
  assert(k(1,0,'1/4').eq('-1/8'));
  const first=k('9/8','1/4','1/4'),second=k('19/16','1/2',1);assert(!first.eq(second));
  details.QG_scope={chi:'1/2',source_amplitude_selected:false,global_warp_selected:false};
});
const report={protocol:'NATIVE_OPERATOR_FOUNDATION_V0_1',status:'PASS_EXACT_FINITE_CHECKS',arithmetic:'BigInt rational cut pairs; no floating-point field arithmetic',scalar_products:scalarProducts,check_count:checks.length,checks,details,scope:{general_proofs:'theory/01_NATIVE_ALGEBRA.md and theory/02_COMPLETION_AND_MEMORY.md',infinite_limits_executed:false,python_regression_suite_rerun:false,physical_gravity_identified:false,universal_problem_solver_claimed:false}};
function sorted(x){if(x===null||typeof x!=='object')return x;if(x instanceof F||x instanceof Cut)return x.toJSON();if(Array.isArray(x))return x.map(sorted);return Object.fromEntries(Object.keys(x).sort().map(k=>[k,sorted(x[k])]));}
const root=path.resolve(__dirname,'..');
const pins=['core/native_operator.cjs','tests/verify.cjs','theory/01_NATIVE_ALGEBRA.md','theory/02_COMPLETION_AND_MEMORY.md'];
report.source_sha256=Object.fromEntries(pins.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')]));
const bytes=JSON.stringify(sorted(report),null,2)+'\n',digest=crypto.createHash('sha256').update(bytes).digest('hex');
const out=path.join(root,'audit/FINITE_CERTIFICATE.json'),pin=path.join(root,'audit/EXPECTED.sha256');
if(process.argv.includes('--write')){fs.writeFileSync(out,bytes);fs.writeFileSync(pin,digest+'\n');console.log('WROTE_EXACT_FINITE_EVIDENCE',checks.length,digest);}
else if(process.argv.includes('--check')){assert.equal(fs.readFileSync(out,'utf8'),bytes,'Evidence/source drift');assert.equal(fs.readFileSync(pin,'utf8').trim(),digest,'Pin mismatch');console.log('PASS_EXACT_FINITE_CHECKS',checks.length,digest);}
else console.log('PASS_EXACT_FINITE_CHECKS_UNPINNED',checks.length,digest);
