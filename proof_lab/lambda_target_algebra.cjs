'use strict';
// SE37 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const ac=require('./lambda_action_closure.cjs');
const {F}=o,S=previous.presentation,{vector}=count;
const {sc,sAdd,sSub,sMul,sEq,sUnit,INF,pConst,pVar,pAdd,pSub,pScale,pMul,pEq,pCompose,pEval,pNorm,pVec,actOn,composeMaps,runWord,Span,closure,toState,fromState,binom,expOf}=ac;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_TARGET_ALGEBRA_RESULT.json');
const roundTrip=x=>JSON.parse(JSON.stringify(x));
const Q=x=>x instanceof F?x:new F(x);
const pPow=(p,e,q)=>{let r=pConst(p.size?expOf([...p.keys()][0]).length:1,sc(1));for(let i=0;i<e;i++)r=pMul(r,p,q);return r;};
// ---- polynomial descent on the observation image (SE37.5)-(SE37.6) ----
// A reduced observer: retained coordinates Z, updates Phi_i, decoder D, each given as polynomials.
function reducedPacket(target,{phi,decoder,q},z0,futureWords,measure){
  return {target,unit_memory_through:Number.isFinite(q)?q:null,retained_reading:toState(z0).toJSON(),
    updates:phi.map(P=>P.map(c=>[...c].map(([k,s])=>[k,s.map(String)]))),decoder:decoder.map(c=>[...c].map(([k,s])=>[k,s.map(String)])),
    future_protocols:futureWords.map(w=>({word:w,reading:toState(measure(w)).toJSON()}))};
}
const polyFrom=rows=>pNorm(new Map(rows.map(([k,s])=>[k,s.map(Q)])),INF);
function decodeReduced(packet,k){
  const q=packet.unit_memory_through===null?INF:packet.unit_memory_through;
  const phi=packet.updates.map(P=>P.map(polyFrom)),D=packet.decoder.map(polyFrom);
  let z0=fromState(packet.retained_reading,k);
  return packet.future_protocols.map(p=>{const z=p.word.reduce((acc,i)=>actOn(phi[i],acc,q),z0);return {word:p.word,predicted:toState(D.map(c=>pEval(c,z,q))).toJSON()};});
}
// ---- the unit-scaled family (SE37.19)-(SE37.21) ----
const unitAction=a=>{const x=pVar(1,0);return [a.reduce((acc,ar,i)=>pAdd(acc,pScale(pPow(x,i+2,INF),sUnit(i+1,ar),INF),INF),x)];};
// Update polynomials in (gamma, Delta).
function relativeUpdate(a){
  const g=pVar(2,0),d=pVar(2,1),L=k=>pConst(2,sUnit(k));
  let gp=g,dp=d;
  a.forEach((ar,i)=>{const r=i+1;if(Q(ar).zero())return;
    gp=pAdd(gp,pScale(pPow(g,r+1,INF),sc(ar),INF),INF);
    for(let k=1;k<=r+1;k++)dp=pAdd(dp,pScale(pMul(pMul(L(k-1),pPow(g,r+1-k,INF),INF),pPow(d,k,INF),INF),sc(Q(ar).mul(new F(binom(r+1,k)))),INF),INF);});
  return [gp,dp];
}
function relativePacket(target,catalogue,q,x,c,words){
  const acts=catalogue.map(unitAction),rd=w=>{const xs=runWord(acts,w,[x],q)[0],cs=runWord(acts,w,[c],q)[0];return toState([sSub(xs,cs,q)]).toJSON();};
  return {target,unit_memory_through:q,catalogue:catalogue.map(a=>a.map(String)),
    calibration_coordinate:toState([sMul(sUnit(1),c,q)]).toJSON(),relative_reading:rd([]),
    future_protocols:words.map(w=>({word:w,reading:rd(w)}))};
}
function decodeRelative(packet){
  const q=packet.unit_memory_through,upd=packet.catalogue.map(a=>relativeUpdate(a.map(Q)));
  const start=[fromState(packet.calibration_coordinate,1)[0],fromState(packet.relative_reading,1)[0]];
  if(start[0].length&&!start[0][0].zero())throw new RangeError('Calibration coordinate must lie in Lambda R');
  return packet.future_protocols.map(p=>{const s=p.word.reduce((acc,i)=>actOn(upd[i],acc,q),start);return {word:p.word,predicted:toState([s[1]]).toJSON(),calibration:toState([s[0]]).toJSON()};});
}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE36_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const stEq=(a,b)=>vector(S.fromJSON(a)).equals(vector(S.fromJSON(b)));
  const X=pVar(1,0),q2=2,L1=pConst(1,sUnit(1)),L2=pConst(1,sUnit(2));
  const g=[pAdd(X,pMul(L1,pMul(X,X,INF),INF),INF)];
  const Y=[X,pMul(L1,pMul(X,X,INF),q2),pMul(L2,pPow(X,3,INF),q2)];
  // -------------------------------------------------- Theorem 1
  check('three_linear_responses_reduce_to_one_nonlinear_coordinate',()=>{
    const z=pVar(1,0),Phi=[pAdd(z,pMul(L1,pMul(z,z,INF),INF),q2)],D=[z,pMul(L1,pMul(z,z,INF),q2),pMul(L2,pPow(z,3,INF),q2)];
    // C(Y(gx))=Phi(C(Y(x))) and Y=D(C(Y)) as identities in x through Lambda^2.
    assert(pEq(pCompose(Y[0],g,q2),pCompose(Phi[0],[Y[0]],q2)));
    Y.forEach((y,j)=>assert(pEq(y,pCompose(D[j],[Y[0]],q2))));
    const x=[sc('3/4','-2','1/3')],meas=w=>Y.map(y=>pEval(y,runWord([g],w,x,q2),q2));
    const words=[[],[0],[0,0],Array(5).fill(0),Array(12).fill(0)];
    const pkt=reducedPacket('All three bank entries after every repetition, from one retained nonlinear coordinate',{phi:[Phi],decoder:D,q:q2},[pEval(X,x,q2)],words,meas);
    const r=decodeReduced(roundTrip(pkt),1);r.forEach((p,i)=>assert(stEq(p.predicted,pkt.future_protocols[i].reading)));
    details.one_coordinate_reduction_certificate={...pkt,decoded:r};
  });
  check('deleting_an_entry_uses_its_explicit_reconstruction_identity',()=>{
    assert(pEq(Y[1],pMul(L1,pMul(Y[0],Y[0],INF),q2)));assert(pEq(Y[2],pMul(L2,pPow(Y[0],3,INF),q2)));
    const M=[[1,1,0],[0,1,2],[0,0,1]];
    const lin=Y.map((_,i)=>Y.reduce((acc,y,k)=>pAdd(acc,pScale(y,sc(M[i][k]),q2),q2),new Map()));
    lin.forEach((p,i)=>assert(pEq(p,pCompose(Y[i],g,q2))));
  });
  check('square_and_cube_admit_no_deletion_identity',()=>{
    const u=pMul(X,X,INF),v=pPow(X,3,INF);assert(pEq(pPow(v,2,INF),pPow(u,3,INF)));
    const inSpanOfPowers=(gen,f,K)=>{const sp=new Span();for(let k=0;k<=K;k++)sp.add(pVec(pPow(gen,k,INF)));return sp.coords(pVec(f))!==null;};
    assert(!inSpanOfPowers(u,v,8));assert(!inSpanOfPowers(v,u,8));
  },true);
  check('nilpotent_unit_relation_is_retained_rather_than_its_radical',()=>{
    const y=pMul(L1,X,1);assert.equal(pMul(y,y,1).size,0);assert(y.size>0);
    assert(sEq(pEval(y,[sc(3)],1),sUnit(1,3)));
  },true);
  // Two noncommuting affine actions on (u,v) with the full bank retained.
  const u=pVar(2,0),v=pVar(2,1),one2=pConst(2,sc(1));
  const shear=[pAdd(u,v,INF),v],swap=[v,u];
  check('descended_updates_compose_in_the_actual_word_order',()=>{
    const x=[sc('1/2'),sc(-3)],Z=x,Phi=[shear,swap];
    for(const w of [[0,1],[1,0],[0,0,1,0,1]]){
      const actual=runWord(Phi,w,x,INF),pred=w.reduce((acc,i)=>actOn(Phi[i],acc,INF),Z);
      actual.forEach((s,i)=>assert(sEq(s,pred[i])));
    }
    const a=runWord(Phi,[0,1],x,INF),b=runWord(Phi,[1,0],x,INF);assert(!sEq(a[0],b[0])||!sEq(a[1],b[1]));
  });
  // -------------------------------------------------- Theorem 2
  const targetClosure=(tau,actions,n,q=0)=>closure({n,sensors:[tau],actions,q});
  check('a_permutation_invariant_target_keeps_one_coordinate',()=>{
    const tau=pAdd(u,v,INF),cl=targetClosure(tau,[swap],2);
    assert.equal(cl.basis.length,2);assert(cl.span.coords(pVec(pCompose(tau,swap,INF))));
    const sp=new Span();for(let k=0;k<=6;k++)sp.add(pVec(pPow(tau,k,INF)));assert.equal(sp.coords(pVec(u)),null);
    const x=[sc(2),sc('-1/3')],meas=w=>[pEval(tau,runWord([swap],w,x,INF),INF)],z=pVar(1,0);
    const pkt=reducedPacket('Every future value of u+v under the swap, from z=u+v',{phi:[[z]],decoder:[z],q:INF},[pEval(tau,x,INF)],[[0],[0,0],[0,0,0]],meas);
    const r=decodeReduced(roundTrip(pkt),1);r.forEach((p,i)=>assert(stEq(p.predicted,pkt.future_protocols[i].reading)));
    details.invariant_target_certificate={...pkt,decoded:r,least_algebra_generators:['u+v']};
  });
  check('a_future_target_forces_retaining_the_second_coordinate',()=>{
    const cl=targetClosure(u,[shear],2);assert.equal(cl.basis.length,3);
    for(const f of [u,v,one2])assert(cl.span.coords(pVec(f)));
    assert.deepEqual(cl.basis.map(b=>b.witness.constant?'1':'tau'+JSON.stringify(b.witness.word)),['1','tau[]','tau[0]']);
  });
  check('keeping_only_the_present_target_loses_future_target_information',()=>{
    const x=[sc(1),sc(2)],z=[sc(1),sc(5)];assert(sEq(pEval(u,x,INF),pEval(u,z,INF)));
    assert(!sEq(pEval(u,actOn(shear,x,INF),INF),pEval(u,actOn(shear,z,INF),INF)));
  },true);
  check('target_closure_stabilizes_within_the_bank_degree_bound',()=>{
    for(const [tau,acts,m,D] of [[pAdd(u,v,INF),[swap],2,1],[u,[shear],2,1],[pMul(u,v,INF),[shear,swap],2,2]]){
      const cl=targetClosure(tau,acts,2),N=binom(m+D,D);assert(cl.span.size<=N);assert(cl.increases<=N-cl.stages[0]);}
    const cl=closure({n:1,sensors:[X],actions:[g],q:q2}),N=(q2+1)*binom(3+1,1);assert(cl.span.size<=N);assert(cl.increases<=N-cl.stages[0]);
  });
  // -------------------------------------------------- Theorem 3
  const zv=pVar(1,0),Phi=[pAdd(zv,pMul(L1,pMul(zv,zv,INF),INF),q2)];
  check('relative_and_calibration_updates_are_exact',()=>{
    for(const [x,c] of [[sc('3/4',-2,'1/3'),sc(-1,'1/2',4)],[sc(2,0,1),sc(0,3)]]){
      const b=pEval(X,[c],q2),dl=sSub(pEval(X,[x],q2),b,q2),gx=actOn(g,[x],q2)[0],gc=actOn(g,[c],q2)[0];
      const bp=pEval(Phi[0],[b],q2),dp=sSub(pEval(Phi[0],[sAdd(b,dl,q2)],q2),bp,q2);
      assert(sEq(bp,gc));assert(sEq(dp,sSub(gx,gc,q2)));
      assert(sEq(sSub(pEval(Phi[0],[sAdd(b,dl,q2)],q2),b,q2),sSub(gx,c,q2)));
    }
  });
  check('calibration_free_difference_law_holds_exactly_for_affine_updates',()=>{
    const bb=pVar(2,0),dd=pVar(2,1),inc=P=>pSub(pCompose(P,[pAdd(bb,dd,INF)],q2),pCompose(P,[bb],q2),q2);
    const dependsOnB=p=>[...p.keys()].some(k=>expOf(k)[0]>0);
    const affine=[pAdd(pScale(zv,sc(2),INF),pConst(1,sc(1)),INF),pAdd(pScale(zv,sUnit(1,3),INF),pConst(1,sUnit(2)),INF)];
    const nonlin=[Phi[0],pAdd(zv,pMul(L2,pMul(zv,zv,INF),INF),q2),pAdd(zv,pPow(zv,3,INF),INF)];
    for(const P of affine)assert(!dependsOnB(inc(P)));for(const P of nonlin)assert(dependsOnB(inc(P)));
  });
  check('the_relative_reading_alone_does_not_determine_its_next_value',()=>{
    const nxt=(x,c)=>sSub(actOn(g,[sc(x)],q2)[0],actOn(g,[sc(c)],q2)[0],q2);
    assert(sEq(sSub(sc(1),sc(0),q2),sSub(sc(2),sc(1),q2)));
    assert(sEq(nxt(1,0),sc(1,1)));assert(sEq(nxt(2,1),sc(1,3)));
  },true);
  check('the_one_step_calibration_signature_is_lambda_c',()=>{
    const d2=pVar(1,0),inc=c=>pSub(pCompose(Phi[0],[pAdd(pConst(1,c),d2,INF)],q2),pConst(1,pEval(Phi[0],[c],q2)),q2);
    const c=sc(1,2,5);assert(pEq(inc(c),inc(sc(1,2,-3))));assert(!pEq(inc(c),inc(sc(1,3,5))));assert(!pEq(inc(c),inc(sc(2,2,5))));
  });
  check('compressing_a_relative_reading_differs_from_the_relative_compression',()=>{
    const C=p=>pEval(pMul(zv,zv,INF),[p],q2),x=sc(2),c=sc(1);
    assert(!sEq(sSub(C(x),C(c),q2),C(sSub(x,c,q2))));
  },true);
  // -------------------------------------------------- Theorem 4
  const catalogue=[[1],['2/3','-5'],[0,0,'-1/2']];
  check('uniform_relative_update_is_an_identity_before_any_truncation',()=>{
    const x=pVar(2,0),c=pVar(2,1),gam=pMul(pConst(2,sUnit(1)),c,INF),del=pSub(x,c,INF);
    for(const a of catalogue){
      const [gp,dp]=relativeUpdate(a.map(Q)),gx=pCompose(unitAction(a)[0],[x],INF),gc=pCompose(unitAction(a)[0],[c],INF);
      assert(pEq(pCompose(gp,[gam,del],INF),pMul(pConst(2,sUnit(1)),gc,INF)));
      assert(pEq(pCompose(dp,[gam,del],INF),pSub(gx,gc,INF)));
      for(const [k] of dp)assert(expOf(k)[1]>=1||k==='');
    }
    const [gq,dq]=relativeUpdate([Q(1)]),gg=pVar(2,0),dd=pVar(2,1);
    assert(pEq(gq,pAdd(gg,pMul(gg,gg,INF),INF)));
    assert(pEq(dq,pAdd(pMul(pAdd(pConst(2,sc(1)),pScale(gg,sc(2),INF),INF),dd,INF),pMul(pConst(2,sUnit(1)),pMul(dd,dd,INF),INF),INF)));
    const [g2,d2]=relativeUpdate([Q('2/3'),Q(-5)]),a=Q('2/3'),b=Q(-5);
    assert(pEq(d2,[[pAdd(pConst(2,sc(1)),pAdd(pScale(gg,sc(a.mul(2)),INF),pScale(pMul(gg,gg,INF),sc(b.mul(3)),INF),INF),INF),1],[pAdd(pConst(2,sUnit(1,a)),pScale(gg,sUnit(1,b.mul(3)),INF),INF),2],[pConst(2,sUnit(2,b)),3]].reduce((acc,[co,e])=>pAdd(acc,pMul(co,pPow(dd,e,INF),INF),INF),new Map())));
    assert(pEq(g2,pAdd(gg,pAdd(pScale(pMul(gg,gg,INF),sc(a),INF),pScale(pPow(gg,3,INF),sc(b),INF),INF),INF)));
  });
  check('two_coordinate_observer_predicts_every_relative_reading',()=>{
    const q=4,x=sc('1/2',3,0,'-1/7',2),c=sc(-2,'1/3',5,1,-1);
    const words=[[0],[1,0],[2,1,0],[0,0,1,2,1],[1,1,1,0,2,0,1,2]];
    const pkt=relativePacket('Relative readings x-c after catalogue words, from (Delta, Lambda c)',catalogue,q,x,c,words);
    const r=decodeRelative(roundTrip(pkt));r.forEach((p,i)=>{assert(stEq(p.predicted,pkt.future_protocols[i].reading));
      const cs=runWord(catalogue.map(unitAction),p.word,[c],q)[0];assert(stEq(p.calibration,toState([sMul(sUnit(1),cs,q)]).toJSON()));});
    details.uniform_relative_observer_certificate={...pkt,decoded:r};
  });
  check('quadratic_action_repetition_formula_through_lambda_squared',()=>{
    const gg=pVar(2,0),dd=pVar(2,1),upd=relativeUpdate([Q(1)]);
    // gamma lies in Lambda R: work with gamma=Lambda*c from the start, cut at the declared depth.
    const sub=p=>pCompose(p,[pMul(pConst(2,sUnit(1)),gg,INF),dd],q2);
    let s=[sub(gg),dd];
    for(let N=0;N<=10;N++){
      const wantG=pAdd(gg,pScale(pMul(gg,gg,INF),sc(N),INF),q2);
      const lin=pAdd(pMul(pScale(gg,sc(2),INF),dd,INF),pMul(pConst(2,sUnit(1)),pMul(dd,dd,INF),INF),INF);
      const quad=pAdd(pAdd(pScale(pMul(pMul(gg,gg,INF),dd,INF),sc(3),INF),pScale(pMul(pConst(2,sUnit(1)),pMul(gg,pMul(dd,dd,INF),INF),INF),sc(3),INF),INF),pMul(pConst(2,sUnit(2)),pPow(dd,3,INF),INF),INF);
      const wantD=pAdd(pAdd(dd,pScale(lin,sc(N),INF),INF),pScale(quad,sc(N*(N-1)),INF),q2);
      assert(pEq(s[0],sub(wantG)));assert(pEq(s[1],sub(wantD)));
      s=upd.map(P=>pCompose(P,s,q2));
    }
  });
  check('the_last_calibration_coefficient_does_not_reach_any_relative_reading',()=>{
    // Equal recorded Delta and equal gamma: calibrations differing only in c_2 give identical futures.
    const q=2,x=sc(3,-1,2),c=sc(1,4,7),words=[[0],[0,1],[1,2,0,0],[2,2,1,0,1,0]];
    const pair=c2=>{const x2=sAdd(x,sSub(c2,c,q),q);return relativePacket('t',catalogue,q,x2,c2,words);};
    const a=pair(c),b=pair(sc(1,4,-9)),d=pair(sc(1,5,7));
    assert.deepEqual(a.relative_reading,b.relative_reading);assert.deepEqual(a.calibration_coordinate,b.calibration_coordinate);
    assert.deepEqual(a.future_protocols,b.future_protocols);
    assert.deepEqual(a.relative_reading,d.relative_reading);assert.notDeepEqual(a.future_protocols,d.future_protocols);
  });
  check('cubic_action_outside_the_family_needs_more_calibration',()=>{
    // At q=1, every polynomial in (Lambda, gamma) is affine in c0, while the Delta-coefficient 1+3 Lambda c0^2 is not.
    const coef=c0=>{const L=pConst(1,sUnit(1)),gx=[pAdd(X,pMul(L,pPow(X,3,INF),INF),INF)],d=pVar(1,0);
      const inc=pSub(pCompose(gx[0],[pAdd(pConst(1,sc(c0)),d,INF)],1),pConst(1,pEval(gx[0],[sc(c0)],1)),1);return inc.get('1')||[];};
    const sd=sAdd(sSub(coef(2),sMul(sc(2),coef(1),1),1),coef(0),1);assert(sEq(sd,sUnit(1,6)));
    for(let i=0;i<=3;i++)for(let j=0;j<=3;j++){const val=c0=>sMul(sUnit(i),(()=>{let t=sc(1);for(let k=0;k<j;k++)t=sMul(t,sUnit(1,c0),1);return t;})(),1);
      assert(sEq(sAdd(sSub(val(2),sMul(sc(2),val(1),1),1),val(0),1),[]));}
  },true);
  check('updates_commute_with_reduction_to_a_shallower_unit_depth',()=>{
    const x=sc('1/2',3,0,'-1/7',2),c=sc(-2,'1/3',5,1,-1),w=[0,2,1,1,0];
    const deep=decodeRelative(relativePacket('t',catalogue,4,x,c,[w]))[0],shallow=decodeRelative(relativePacket('t',catalogue,2,x,c,[w]))[0];
    const cutTo=(j,qq)=>{const s=fromState(j,1)[0];return s.slice(0,qq+1);};
    assert(sEq(cutTo(deep.predicted,2),fromState(shallow.predicted,1)[0]));
  });
  check('a_calibration_coordinate_with_a_cut_part_is_refused',()=>{
    const pkt=relativePacket('t',catalogue,2,sc(1),sc(1),[[0]]);pkt.calibration_coordinate=toState([sc(1,1)]).toJSON();
    assert.throws(()=>decodeRelative(pkt),/Lambda R/);
  },true);
  check('every_archived_certificate_redecodes_from_its_saved_readings',()=>{
    const arc=roundTrip(details);
    for(const k of ['one_coordinate_reduction_certificate','invariant_target_certificate'])decodeReduced(arc[k],1).forEach((p,i)=>assert(stEq(p.predicted,arc[k].decoded[i].predicted)));
    decodeRelative(arc.uniform_relative_observer_certificate).forEach((p,i)=>assert(stEq(p.predicted,arc.uniform_relative_observer_certificate.decoded[i].predicted)));
  });
  return {schema:'rkf.lambda-target-algebra.v1',date:'2026-10-12',status:'PASS_TARGET_ALGEBRA_AND_CALIBRATION_MEMORY',
    theorem_count:4,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting sectors over Q, Q[Lambda] and retained unit quotients',source:'Supplied available bank, target decoder, action catalogue and recorded protocol readings',
      zero:'Typed cut operation; additive neutrals retain their separate types',target_added_as_sensor:false,radical_replaces_unit_relations:false,primitive_metric:false,numerical_unit_value_assumed:false,RH_development:false,curvature_developed:false},
    finite_ranges:{reduction_unit_depth:q2,reduction_words_through_length:12,target_algebra_examples:4,relative_observer_unit_depth:4,relative_words_through_length:8,unit_scaled_catalogue_size:3},
    details,evidence:{general_results:'Four written derivation groups',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['a minimum coordinate count or acquisition cost','noisy-data conditioning','closure on (Delta, Lambda c) for arbitrary polynomial actions','finite information at infinite unit depth',
      'evaluation or convergence at a nonzero numerical unit','general nonlinear recovery','new RH, eta or curvature result','novelty priority for substitution, invariant-span closure or coefficient comparison']};
}
module.exports={relativeUpdate,unitAction,decodeReduced,decodeRelative,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE37_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}
