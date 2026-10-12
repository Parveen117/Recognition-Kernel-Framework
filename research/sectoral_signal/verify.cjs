'use strict';
// Finite controls over the existing exact rational cut field. No floating point.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const assert=require('node:assert/strict');
const o=require('../../operator_foundation/core/native_operator.cjs');
const {F,Cut,matrix:M,identity:I,zeros:Z,add,sub,scale,mul,dagger,
  equal,inverse,rank,energy,isZero,rowClosure}=o;
const checks=[],controls=[],details={};
function check(name,f){f();checks.push(name);}
function reject(name,f){f();checks.push(name);controls.push(name);}
function eq(a,b){assert(equal(a,b));}
function stack(a,b){return M(a.concat(b));}
function join(a,b){return M(a.map((r,i)=>r.concat(b[i])));}
function gram(a){return mul(dagger(a),a);}
function det2(a){return a[0][0].mul(a[1][1]).sub(a[0][1].mul(a[1][0]));}
function packet(m,u,v){
  const n=m[0].length,k=m.length,U=stack(I(n),m),N=join(scale(m,-1),I(k));
  const G=gram(U),H=mul(N,dagger(N)),z=stack(u,v),r=sub(v,mul(m,u));
  const estimate=mul(mul(inverse(G),dagger(U)),z);
  const compatible=mul(U,estimate),residue=mul(mul(dagger(N),inverse(H)),r);
  return {U,N,G,H,z,r,estimate,compatible,residue};
}
const C=M([[1,0]]),L=M([[0,1]]),A=M([[1,0],[1,1]]),G=gram(A);
check('native_cut_iota_and_dagger_preserved',()=>{
  const i=new Cut(0,1);assert(i.mul(i).eq(-1));assert(i.dagger().eq(i.neg()));
});
check('source_observer_blind_direction_is_real',()=>{
  const h=M([[0],[1]]);eq(mul(C,h),M([[0]]));eq(mul(L,h),M([[1]]));
});
check('singular_chart_family_has_constant_full_observer',()=>{
  for(const e of ['-3','-1','0','1/1000000','1/2','4']){
    const m=M([[1,1],[1,new F(1).add(e)]]);
    assert(det2(m).eq(e));eq(stack(C,mul(C,m)),A);
    eq(mul(inverse(A),A),I(2));
    if(e==='0')assert.throws(()=>inverse(m),/Singular/);
  }
  details.singular_chart={response_determinant:'epsilon',observer_determinant:'1',
    recovery:'p=t-s',uniform_gram_floor:'1/3',target_decoder_norm_squared:'2'};
});
check('uniform_stability_bound_at_and_across_zero',()=>{
  const shifted=sub(G,scale(I(2),'1/3'));
  assert(shifted[0][0].rad.n>0n&&shifted[1][1].rad.n>0n);
  assert(det2(shifted).eq('1/9'));
  for(let s=-4;s<=4;s++)for(let p=-4;p<=4;p++){
    const x=M([[new Cut(s,p)],[new Cut(p,-s)]]);
    assert(energy(x).div(3).le(energy(mul(A,x))));
  }
});
check('hidden_complex_signal_recovered_with_phase',()=>{
  for(let s=-3;s<=3;s++)for(let p=-3;p<=3;p++){
    const x=M([[new Cut(s,1)],[new Cut(p,-2)]]);
    eq(mul(inverse(A),mul(A,x)),x);
  }
  const x=M([[0],[new Cut(0,1)]]);
  eq(mul(inverse(A),mul(A,x)),x);
});
check('native_minimum_future_observer_agrees_with_two_channel_rank',()=>{
  const m=M([[1,1],[1,1]]),closure=rowClosure(C,[m]);
  assert.equal(closure.rank,2);assert.equal(closure.extra,1);
});
reject('zero_coupling_does_not_repair_blindness',()=>{
  const m=M([[2,0],[0,3]]),a=stack(C,mul(C,m));
  assert.equal(rank(a),1);eq(mul(a,M([[0],[1]])),Z(2,1));
});
reject('duplicate_readout_does_not_add_information',()=>{
  const duplicate=stack(C,scale(C,7));assert.equal(rank(duplicate),1);
});
reject('discarding_phase_confuses_distinct_signals',()=>{
  const x=M([[0],[new Cut(0,1)]]),y=scale(x,-1),ax=mul(A,x),ay=mul(A,y);
  assert(!equal(ax,ay));assert(energy(ax).eq(energy(ay)));
  for(let j=0;j<ax.length;j++)assert(ax[j][0].norm2().eq(ay[j][0].norm2()));
});
check('minimum_decoder_and_exact_noise_transfer',()=>{
  const O=mul(mul(L,inverse(G)),dagger(A));eq(O,M([[-1,1]]));
  eq(mul(O,A),L);eq(mul(O,dagger(O)),M([[2]]));
  const x=M([[2],[-3]]),e=M([['1/10'],['-1/5']]);
  eq(sub(mul(O,add(mul(A,x),e)),mul(L,x)),mul(O,e));
});
reject('exact_recovery_is_not_unit_contractivity',()=>{
  const O=M([[-1,1]]),e=M([[-1],[1]]);
  assert(energy(e).le(energy(mul(O,e))));
  assert(!energy(mul(O,e)).le(energy(e)));
});
check('full_graph_decomposition_including_rectangular_singular_and_complex',()=>{
  const matrices=[M([[1,1],[1,1]]),M([[0,0],[0,0]]),
    M([[[1,1],2],[0,[0,-1]]]),M([[1,2,3]]),M([[1],[new Cut(0,1)],[2]])];
  for(const m of matrices){
    const u=M(Array.from({length:m[0].length},(_,i)=>[new Cut(i-2,i+1)]));
    const v=M(Array.from({length:m.length},(_,i)=>[new Cut(i+3,1-i)]));
    const p=packet(m,u,v);
    eq(mul(p.N,p.U),Z(m.length,m[0].length));
    eq(add(p.compatible,p.residue),p.z);
    eq(mul(dagger(p.compatible),p.residue),M([[0]]));
    assert(energy(p.z).eq(energy(p.compatible).add(energy(p.residue))));
    const weighted=mul(mul(dagger(p.r),inverse(p.H)),p.r)[0][0];
    assert(weighted.turn.zero());assert(weighted.rad.eq(energy(p.residue)));
  }
  details.graph_models_checked=matrices.length;
});
check('compatible_packet_has_zero_transverse_residue',()=>{
  const m=M([[2,1],[1,3]]),x=M([[new Cut(2,1)],[-3]]),p=packet(m,x,mul(m,x));
  assert(isZero(p.r));eq(p.estimate,x);assert(isZero(p.residue));
});
reject('coherent_sensor_error_can_close_the_cycle',()=>{
  const m=M([[2,1],[1,3]]),x=M([[1],[2]]),h=M([[3],[-1]]);
  const p=packet(m,add(x,h),add(mul(m,x),mul(m,h)));
  assert(isZero(p.r));eq(p.estimate,add(x,h));assert(!equal(p.estimate,x));
});
reject('model_generated_output_is_not_independent_validation',()=>{
  const m=M([[1,1],[1,1]]),u=M([[15],[-20]]);
  assert(isZero(packet(m,u,mul(m,u)).r));
});
check('calibration_and_sensor_residue_keep_the_mixed_term',()=>{
  const m=M([[2,1],[0,3]]),E=M([[0,'1/5'],['-1/3',0]]),x=M([[2],[-1]]);
  const ex=M([['1/10'],['2/7']]),ey=M([['1/9'],['-2/11']]);
  const u=add(x,ex),v=add(mul(add(m,E),x),ey),r=sub(v,mul(m,u));
  eq(r,sub(add(mul(E,x),ey),mul(m,ex)));
  assert(!equal(r,add(mul(E,x),ey)));
});
check('output_VT_permutation_is_calibrated_not_new_rank',()=>{
  const m=M([[2,1],[1,3]]),j=M([[0,1],[1,0]]),d=M([[1,0]]);
  eq(mul(mul(d,j),mul(j,m)),mul(d,m));
  const u=M([[2],[-1]]),v=M([[4],[7]]),p=packet(m,u,v),q=packet(mul(j,m),u,mul(j,v));
  eq(p.estimate,q.estimate);assert(energy(p.residue).eq(energy(q.residue)));
});
check('nonorthogonal_coordinate_metric_must_be_transported',()=>{
  const t=M([[2,1],[0,1]]),h=gram(inverse(t)),x=M([[1],[2]]),tx=mul(t,x);
  const e=mul(mul(dagger(tx),h),tx)[0][0];assert(e.rad.eq(energy(x)));
  assert(!energy(tx).eq(energy(x)));
});
check('Legendre_inverse_sign_in_an_invertible_tangent_model',()=>{
  const m=M([[2,1],[1,3]]),f=scale(inverse(m),-1);
  eq(mul(f,m),scale(I(2),-1));eq(f,dagger(f));
});
check('noncommuting_block_cross_recovery_retains_order',()=>{
  const a=M([[1,1],[0,1]]),b=M([[1,0],[1,1]]),s=M([[2],[-1]]),p=M([[3],[4]]);
  const t=add(mul(a,s),mul(b,p));eq(mul(inverse(b),sub(t,mul(a,s))),p);
  assert(!equal(mul(inverse(b),a),mul(a,inverse(b))));
});
check('redundant_third_reading_has_a_testable_residue',()=>{
  for(const e of ['0','1/4','-2']){
    const a=M([[1,0],[1,1],[1,new F(1).add(e)]]);
    const n=M([[e,new F(1).add(e).neg(),1]]);
    eq(mul(n,a),Z(1,2));
    assert(!isZero(mul(n,M([[0],[0],[1]]))));
  }
});
check('source_residual_split_is_exact',()=>{
  const r=M([[1,2],[3,4]]),p=M([[1,0],[0,0]]),q=sub(I(2),p);
  eq(gram(r),add(gram(mul(p,r)),gram(mul(q,r))));
});
reject('nonorthogonal_sector_split_cannot_drop_cross_terms',()=>{
  const r=M([[1,2],[3,4]]),p=M([[1,1],[0,0]]),q=sub(I(2),p);
  eq(mul(p,p),p);assert(!equal(gram(r),add(gram(mul(p,r)),gram(mul(q,r)))));
});
reject('duplicating_residual_energy_changes_the_source',()=>{
  const r=M([[1,0]]),q=I(2),l=M([[0,1]]);
  const source=sub(add(q,gram(r)),gram(l));
  const wrong=sub(add(q,scale(gram(r),2)),gram(l));assert(!equal(source,wrong));
});
const root=__dirname;
const inputs=['THEOREM.md','README.md','verify.cjs',
  '../../operator_foundation/core/native_operator.cjs',
  '../../operator_foundation/theory/01_NATIVE_ALGEBRA.md',
  '../../theorum/stratified_recognition/04_physical_observer_minimum_sensor_repair.md',
  '../../theorum/thermodynamics/10_thermodynamic_cut_square_response_decomposition.md',
  '../../theorum/thermodynamics/09_scope_exclusions.md'];
const hashes=Object.fromEntries(inputs.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]));
const result={protocol:'RKF_SP_VT_SECTORAL_SIGNAL_SS1',status:'PASS_EXACT_FINITE_CONTROLS',
  check_count:checks.length,checks,negative_control_count:controls.length,negative_controls:controls,
  details,source_sha256:hashes,scope:{written_general_proofs:'THEOREM.md',
    full_engine_pass:false,external_review:false,formal_proof:false,
    physical_sensor_experiment:false,new_eta_certificate:false}};
const serialized=JSON.stringify(result,null,2)+'\n';
const hash=crypto.createHash('sha256').update(serialized).digest('hex');
const output=path.join(root,'RESULT.json'),pin=path.join(root,'EXPECTED.sha256');
if(process.argv.includes('--write')){
  if(fs.existsSync(output)||fs.existsSync(pin))throw Error('Refuse to overwrite existing evidence');
  fs.writeFileSync(output,serialized,{flag:'wx'});fs.writeFileSync(pin,hash+'\n',{flag:'wx'});
}else if(process.argv.includes('--check')){
  assert.equal(fs.readFileSync(output,'utf8'),serialized,'Source or evidence drift');
  assert.equal(fs.readFileSync(pin,'utf8').trim(),hash,'Evidence pin mismatch');
}
console.log(JSON.stringify({protocol:result.protocol,status:result.status,runtime:process.version,
  check_count:checks.length,negative_control_count:controls.length,details,sha256:hash},null,2));
