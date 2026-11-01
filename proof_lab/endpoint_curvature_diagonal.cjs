'use strict';
// SE29 application only: all exact cut/matrix arithmetic is canonical.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const {F,Cut,IOTA,matrix,identity,zeros,add,sub,scale,mul,dagger,equal,inverse,commutator}=o;
const root=path.resolve(__dirname,'..');
const resultPath=path.join(__dirname,'ENDPOINT_CURVATURE_DIAGONAL_RESULT.json');
const pinsPath=path.join(root,'papers/rkf_completed_weil_endpoint/development/SE29_SOURCE_PINS.json');
const parentPins=path.join(root,'papers/rkf_completed_weil_endpoint/development/SE28_SOURCE_PINS.json');
const f=F.of;
function scalar(gain){
  const g=f(gain);if(g.n<0n)throw new RangeError('Use the positive square root of the gain Gram');
  const t=g.pow(2),den=f(1).add(t),a=t.div(den),h=g.div(den),k=h.pow(2),delta=f(1).sub(t).div(den);
  const P=matrix([[a,h],[h,f(1).sub(a)]]),Gamma=matrix([[1,0],[0,-1]]);
  const curvature=scale(commutator(Gamma,P),new Cut(0,'-1/2'));
  return {gain:g,t,a,h,k,delta,P,Gamma,curvature};
}
function diagonal(values){const d=zeros(values.length);values.forEach((v,i)=>d[i][i]=Cut.of(v));return d;}
function rotate(a,u){return mul(mul(u,a),dagger(u));}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h] of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(parentPins),checks=[],controls=[];
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const gains=[0,'1/3','3/4',1,'4/3',2,7],models=gains.map(scalar);
  check('canonical_derived_iota',()=>assert(IOTA.mul(IOTA).eq(-1)));
  check('effect_projection_is_self_adjoint_and_idempotent',()=>{for(const r of models){assert(equal(dagger(r.P),r.P));assert(equal(mul(r.P,r.P),r.P));}});
  check('commutator_flux_matches_the_accepted_amplitude',()=>{for(const r of models){assert(equal(r.curvature,matrix([[0,new Cut(0,r.h.neg())],[new Cut(0,r.h),0]])));assert(r.curvature[1][0].norm2().eq(r.k));}});
  check('full_curvature_square_and_diagonal_identity',()=>{for(const r of models){assert(equal(mul(r.curvature,r.curvature),scale(identity(2),r.k)));assert(r.delta.pow(2).add(r.k.mul(4)).eq(1));}});
  check('retained_projector_diagonal_recovers_the_gain_Gram',()=>{for(const r of models){assert(sub(identity(2),scale(r.P,2))[0][0].eq(r.delta));assert(f(1).sub(r.delta).div(f(1).add(r.delta)).eq(r.t));}});
  check('reciprocal_gain_preserves_the_entire_curvature',()=>{for(const g of ['1/3','3/4',1,'4/3',2,7]){const a=scalar(g),b=scalar(f(1).div(g));assert(equal(a.curvature,b.curvature));assert(a.delta.eq(b.delta.neg()));assert(a.a.add(b.a).eq(1));}});
  const contractive=scalar('3/4'),expanding=scalar('4/3');
  check('same_signal_has_opposite_source_signs',()=>{assert(contractive.t.le(1));assert(!expanding.t.le(1));assert(contractive.k.eq('144/625'));assert(expanding.k.eq('144/625'));assert(contractive.delta.eq('7/25'));assert(expanding.delta.eq('-7/25'));},true);
  check('full_projector_retains_the_missing_information',()=>{assert(!equal(contractive.P,expanding.P));assert(!equal(sub(identity(2),scale(contractive.P,2)),sub(identity(2),scale(expanding.P,2))));});
  check('taking_only_the_positive_root_changes_the_expanding_source',()=>{const absolute=f('7/25');assert(absolute.pow(2).eq(f(1).sub(expanding.k.mul(4))));assert(!absolute.eq(expanding.delta));assert(f(1).sub(absolute).div(f(1).add(absolute)).eq(contractive.t));},true);
  check('unit_gain_has_zero_diagonal_and_nonzero_curvature',()=>{const r=scalar(1);assert(r.delta.zero());assert(r.h.eq('1/2'));assert(r.k.eq('1/4'));assert(!equal(r.curvature,zeros(2)));},true);
  check('zero_gain_is_allowed_and_is_not_unit_gain',()=>{const r=scalar(0);assert(equal(r.curvature,zeros(2)));assert(r.delta.eq(1));assert(!r.t.eq(1));},true);
  const U=matrix([['3/5','-4/5'],['4/5','3/5']]);
  const W=matrix([[2,1],[1,2]]),N=mul(W,W),T=rotate(diagonal(['9/16','16/9']),U);
  const source=mul(mul(W,sub(identity(2),T)),W);
  const R=rotate(diagonal(['4/5','3/5']),U); // (I+T)^(-1/2)
  const Q=mul(inverse(W),R),D=rotate(diagonal(['7/25','-7/25']),U);
  check('noncommuting_source_congruence_keeps_factor_order',()=>{assert(!equal(mul(N,T),mul(T,N)));assert(equal(mul(mul(dagger(Q),source),Q),D));});
  check('mixed_source_negative_witness_is_preserved',()=>{const h=mul(Q,mul(U,matrix([[0],[1]])));assert(mul(mul(dagger(h),source),h)[0][0].eq('-7/25'));});
  check('shift_transports_the_metric_instead_of_coordinate_identity',()=>{const eta=f('1079/2000');const actual=mul(mul(dagger(Q),add(source,scale(identity(2),eta))),Q);assert(equal(actual,add(D,scale(mul(dagger(Q),Q),eta))));assert(!equal(actual,add(D,scale(identity(2),eta))));},true);
  check('gauge_covariance_transports_the_reference_and_reading',()=>{const a=contractive,Pt=rotate(a.P,U),Gt=rotate(a.Gamma,U),Ft=scale(commutator(Gt,Pt),new Cut(0,'-1/2'));assert(equal(Ft,rotate(a.curvature,U)));const J=mul(U,matrix([[1],[0]]));assert(mul(mul(dagger(J),sub(identity(2),scale(Pt,2))),J)[0][0].eq(a.delta));});
  const samples=[];
  check('infinite_countermodel_coefficients_are_exactly_reciprocal',()=>{for(let n=1;n<=64;n++){const a=scalar(new F(n,n+1)),b=scalar(new F(n+1,n)),den=f(2*n*n+2*n+1);assert(equal(a.curvature,b.curvature));assert(a.h.eq(f(n*(n+1)).div(den)));assert(a.delta.eq(f(2*n+1).div(den)));assert(b.delta.eq(a.delta.neg()));assert(a.t.le(1)&&!b.t.le(1));if([1,2,4,16,64].includes(n))samples.push({n,contractive_gain_Gram:a.t,expanding_gain_Gram:b.t,shared_amplitude:a.h,positive_diagonal:a.delta});}});
  check('essential_threshold_deficit_identity_on_countermodel_modes',()=>{for(let n=1;n<=64;n++){const r=scalar(new F(n,n+1));assert(f('1/4').sub(r.k).eq(r.delta.pow(2).div(4)));assert(r.delta.le(new F(3,2*n)));}});
  check('finite_readings_cannot_rule_out_a_later_negative_sector',()=>{const M=16,a=Array(M+1).fill('9/16'),b=a.slice();b[M]='16/9';assert.deepEqual(a.slice(0,M),b.slice(0,M));assert(!f(b[M]).le(1));},true);
  check('negative_gain_root_is_rejected',()=>assert.throws(()=>scalar(-1),RangeError),true);
  const archive=JSON.parse(fs.readFileSync(path.join(__dirname,'ENDPOINT_CONNECTED_CUT_RESULT.json'),'utf8'));
  check('existing_global_certificate_is_preserved',()=>{assert.equal(archive.global_source.eta,'1079/2000');assert.equal(archive.global_source.shifted_native_floor,'1/492000');});
  return {
    schema:'rkf.endpoint-curvature-diagonal.v1',date:'2026-10-12',status:'PASS_CURVATURE_BLINDNESS_AND_DIAGONAL_CONTROLS',
    source:{inherited_global_eta:'1079/2000',inherited_native_floor:'1/492000',global_replay_rerun:false,eta_zero_certified:false,RH_proved:false},
    written_theorems:{count:4,actual_source_curvature_norm:'1/2',actual_source_curvature_Gram_norm:'1/4',actual_essential_curvature_norm:'1/2',
      attachment:'T=N^(-1/2)L_dagger L N^(-1/2); A=T(I+T)^(-1)',remaining_obligation:'Delta=(I-T)(I+T)^(-1) >= 0 on the entire actual carrier',
      warning:'Norm statements follow from the written SE5 Weyl-sequence proof, not from finite checks; other TVSP connections are not excluded'},
    reciprocal_pair:[contractive,expanding].map(r=>({gain_Gram:r.t,curvature_amplitude:r.h,curvature_Gram:r.k,source_diagonal:r.delta})),
    infinite_model_samples:samples,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,checks,controls,
    not_certified:['actual source diagonal nonnegativity','global eta zero or RH','new smaller eta','curvature flatness equivalent to RH','unique physical TVSP attachment','whole-engine PASS','proof-assistant or external review']
  };
}
module.exports={scalar,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.some(x=>!['--write','--check'].includes(x))||args.length>1)throw new Error('Choose --write or --check');
  const result=verify(),serialized=JSON.stringify(result,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,serialized,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),serialized,'Read-only replay differs from archive');console.log('Source pins checked:',pinCheck(pinsPath));}
  console.log(JSON.stringify({status:result.status,check_count:result.check_count,negative_control_count:result.negative_control_count,source:result.source},null,2));
}
