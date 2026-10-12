'use strict';
// SE27 finite chart controls, using the unchanged canonical cut arithmetic.
const assert=require('node:assert/strict');
const o=require('../operator_foundation/core/native_operator.cjs');
const {F,Cut,matrix:M,identity:I,zeros:Z,add,sub,scale,mul,dagger,equal,energy}=o;
const checks=[],controls=[];
function check(name,f){f();checks.push({name,status:'PASS'});}
function reject(name,f){f();checks.push({name,status:'PASS'});controls.push(name);}
function eq(a,b){assert(equal(a,b));}
function sum(a){return a.reduce((x,y)=>add(x,y),Z(3,3));}
const basis=[M([[1],[0],[0]]),M([[0],[1],[0]]),M([[0],[0],[1]])];
const planes=basis.map(e=>sub(I(3),mul(e,dagger(e))));
const frame=M([[1,0],[0,1],[0,0]]);
function rotation(axis,r,derivative=false){
  r=F.of(r);
  if(!new F(0).le(r)||!r.le(1))throw new RangeError('Cut-path parameter outside [0,1]');
  const t=r.pow(2).mul(3).sub(r.pow(3).mul(2));
  const dt=r.mul(new F(1).sub(r)).mul(6),den=new F(1).add(t.pow(2));
  const c=derivative?t.mul(-4).mul(dt).div(den.pow(2)):new F(1).sub(t.pow(2)).div(den);
  const s=derivative?new F(1).sub(t.pow(2)).mul(2).mul(dt).div(den.pow(2)):t.mul(2).div(den);
  const one=derivative?0:1;
  if(axis==='x')return M([[one,0,0],[0,c,s.neg()],[0,s,c]]);
  if(axis==='y')return M([[c,0,s],[0,one,0],[s.neg(),0,c]]);
  if(axis==='z')return M([[c,s.neg(),0],[s,c,0],[0,0,one]]);
  throw new TypeError('Unknown typed rotation axis');
}
const Ry=rotation('y',1),Rz=rotation('z',1),Rx=rotation('x',1);
function path(segment,r,derivative=false){
  if(segment===0)return rotation('y',r,derivative);
  if(segment===1)return mul(rotation('z',r,derivative),Ry);
  if(segment===2)return mul(mul(rotation('x',r,derivative),Rz),Ry);
  throw new RangeError('Unknown path segment');
}
const samples=[0,'1/4','1/2','3/4',1];
const y=M([[new Cut(1,2)],[new Cut(-3,1)],[new Cut(2,-1)]]);
const a=M([[new Cut(2,-1)],[new Cut(1,1)],[new Cut(-1,2)]]);
check('derived_iota_and_dagger',()=>{const i=new Cut(0,1);assert(i.mul(i).eq(-1));assert(i.dagger().eq(i.neg()));});
check('three_cut_path_unitary_exact_rational_controls',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const u=path(j,r);eq(mul(dagger(u),u),I(3));}
});
check('each_cut_is_self_adjoint_idempotent',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const u=path(j,r);for(const p of planes){const q=mul(mul(u,p),dagger(u));eq(mul(q,q),q);eq(dagger(q),q);}}
});
check('overlap_charged_once_by_half_sum',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const u=path(j,r);eq(scale(sum(planes.map(p=>mul(mul(u,p),dagger(u)))),'1/2'),I(3));}
});
check('all_complex_reading_energy_retained',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const u=path(j,r);let e=new F(0);for(const p of planes)e=e.add(energy(mul(mul(mul(u,p),dagger(u)),y)));assert(e.div(2).eq(energy(y)));}
});
check('complete_target_recovery_and_paid_norm',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const u=path(j,r);let pairing=Z(1,1),cost=new F(0);for(const p of planes){const q=mul(mul(u,p),dagger(u)),b=mul(q,a);pairing=add(pairing,mul(dagger(b),mul(q,y)));cost=cost.add(energy(b));}eq(scale(pairing,'1/2'),mul(dagger(a),y));assert(cost.div(2).eq(energy(a)));}
});
check('matching_at_both_cut_junctions',()=>{eq(path(0,1),path(1,0));eq(path(1,1),path(2,0));});
check('zero_endpoint_velocity_gives_C1_joining',()=>{for(let j=0;j<3;j++)for(const r of [0,1])eq(path(j,r,true),Z(3,3));});
check('actual_tangent_plane_transport_is_horizontal',()=>{
  for(let j=0;j<3;j++)for(const r of samples){const f=mul(path(j,r),frame),df=mul(path(j,r,true),frame);eq(mul(dagger(f),df),Z(2,2));}
});
const H=mul(mul(Rx,Rz),Ry),H2=M([[0,-1],[1,0]]);
check('curved_loop_normals_and_base_cut_close',()=>{
  eq(mul(Ry,basis[2]),basis[0]);eq(mul(mul(Rz,Ry),basis[2]),basis[1]);eq(mul(H,basis[2]),basis[2]);eq(mul(mul(H,planes[2]),dagger(H)),planes[2]);
});
check('closed_cut_has_nontrivial_quarter_turn_holonomy',()=>{eq(H,M([[0,-1,0],[1,0,0],[0,0,1]]));eq(mul(H,frame),mul(frame,H2));assert(!equal(H2,I(2)));});
check('whole_cut_collection_returns_with_lawful_relabelling',()=>{eq(mul(mul(H,planes[0]),dagger(H)),planes[1]);eq(mul(mul(H,planes[1]),dagger(H)),planes[0]);});
check('loop_readings_and_decoder_transport_together',()=>{
  const start=mul(dagger(frame),y),end=mul(dagger(mul(H,frame)),y),c=M([[1],[new Cut(0,1)]]);
  eq(end,mul(dagger(H2),start));eq(mul(dagger(mul(dagger(H2),c)),end),mul(dagger(c),start));
});
reject('unweighted_gluing_double_counts_source',()=>{eq(sum(planes),scale(I(3),2));assert(!equal(sum(planes),I(3)));});
reject('one_third_weights_lose_the_target',()=>{assert(!equal(scale(sum(planes),'1/3'),I(3)));});
reject('one_cut_is_not_the_complete_reference',()=>{for(let j=0;j<3;j++)eq(mul(planes[j],basis[j]),Z(3,1));});
reject('closed_cut_does_not_erase_memory',()=>{assert(!equal(mul(dagger(H2),M([[1],[0]])),M([[1],[0]])));});
reject('fixed_decoder_after_loop_reads_wrong_target',()=>{
  const c=M([[1],[0]]),z=M([[1],[0]]);assert(!equal(mul(dagger(c),mul(dagger(H2),z)),mul(dagger(c),z)));
});
reject('path_domain_is_enforced',()=>{assert.throws(()=>rotation('x','5/4'),RangeError);assert.throws(()=>path(3,0),RangeError);});
console.log(JSON.stringify({schema:'rkf.connected-cut-geometry.v1',status:'PASS_EXACT_CUT_CONTROLS',check_count:checks.length,negative_control_count:controls.length,
  holonomy:[['0','-1'],['1','0']],overlap_identity:'(P1+P2+P3)/2=I_3',path_segments:3,
  continuum_evidence:'Written rational path and projector identities; finite samples are controls, not the continuum proof',checks,controls},null,2));
