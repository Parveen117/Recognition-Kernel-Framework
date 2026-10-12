'use strict';
// SE34 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const joint=require('./lambda_joint_readings.cjs');
const active=require('./lambda_active_readings.cjs');
const {F}=o,S=previous.presentation,{vector}=count,{coordinates,jointAction,bankReader}=joint,{buildOp,applyOp,transportOp}=active;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_UNIT_MEMORY_LIFTING_RESULT.json');
const W=(n=0,d=0,c=1)=>S.word([...Array(d).fill('L'),...Array(n).fill('X')],c);
const Lam=W(0,1),one=W(),nil=()=>S.zero();
const ix=w=>w.filter(t=>t==='X').length,ud=w=>w.filter(t=>t==='L').length;
const sum=xs=>vector(xs.reduce((a,b)=>a.plus(b),nil()));
const cut=(a,q)=>vector(previous.memory(vector(a),q));
const layerOf=(a,r)=>vector(previous.layer(vector(a),r));
const T=(out,coeff,powers)=>({out,coeff:vector(coeff),powers});
const coordOf=(v,n)=>vector(new Map(coordinates(vector(v))).get(n)||nil());
const roundTrip=x=>JSON.parse(JSON.stringify(x));
const st=j=>vector(S.fromJSON(j));
// Lowest unit degree present in a state; Infinity for the additive neutral.
function unitOrder(v){let m=Infinity;for(const [w,c]of vector(v).entries())if(!c.rad.zero())m=Math.min(m,ud(w));return m;}
// Numerical substitution of the marked unit by one; used only as a boundary control.
const atUnitOne=v=>sum([...vector(v).entries()].map(([w,c])=>W(ix(w),0,c.rad.toString())));
// ---- operations read from serialized joint banks ----
const readerCache=new WeakMap();
function readers(op){
  if(!readerCache.has(op))readerCache.set(op,op.kernels.map(k=>({arity:k.arity,read:bankReader(k.readings,k.arity)})));
  return readerCache.get(op);
}
const evalOp=(op,x)=>applyOp(op,vector(x));
// Exact linear response delta op_x(h)=sum_r r T_r(x,...,x,h).
function response(op,x,h){
  let out=nil();
  for(const {arity,read}of readers(op))out=out.plus(vector(jointAction(read,[...Array(arity-1).fill(vector(x)),vector(h)])).scale(arity));
  return vector(out);
}
function mapBank(op,f){
  const c=roundTrip(op);c.constant=f(st(op.constant)).toJSON();
  for(const k of c.kernels)for(const row of k.readings)row.response=f(st(row.response)).toJSON();
  return c;
}
const cutOp=(op,q)=>mapBank(op,v=>cut(v,q));
function requireRational(op){
  const all=[st(op.constant),...op.kernels.flatMap(k=>k.readings.map(r=>st(r.response)))];
  for(const v of all)for(const [w]of v.entries())if(ud(w))throw new TypeError('Cut inverse must have unit-degree-zero readings');
}
// H=x-F for a closed sector, read from the bank of F.
function complement(op){
  if(JSON.stringify(op.input_labels)!==JSON.stringify(op.output_labels))throw new RangeError('Closed counting sector required');
  const c=mapBank(op,v=>vector(v.scale(-1)));
  const k1=c.kernels.find(k=>k.arity===1);
  for(const row of k1.readings)row.response=vector(st(row.response).plus(W(row.inputs[0]))).toJSON();
  return c;
}
// Weighted dependency graph j->i: least unit degree among monomials of H_i containing x_j.
function dependencyGraph(H){
  const edges=new Map();
  for(const k of H.kernels)for(const row of k.readings){
    const v=st(row.response);
    for(const [i,coef]of coordinates(v)){
      const w=unitOrder(coef);if(w===Infinity)continue;
      for(const j of new Set(row.inputs)){const key=j+'>'+i;edges.set(key,Math.min(edges.has(key)?edges.get(key):Infinity,w));}
    }
  }
  return [...edges].map(([k,w])=>{const [j,i]=k.split('>').map(Number);return {from:j,to:i,weight:w};}).sort((a,b)=>a.from-b.from||a.to-b.to);
}
function topoOrder(labels,edges){
  const indeg=new Map(labels.map(l=>[l,0]));for(const e of edges)indeg.set(e.to,indeg.get(e.to)+1);
  const order=[],ready=labels.filter(l=>!indeg.get(l));
  while(ready.length){ready.sort((a,b)=>a-b);const v=ready.shift();order.push(v);for(const e of edges)if(e.from===v){indeg.set(e.to,indeg.get(e.to)-1);if(!indeg.get(e.to))ready.push(e.to);}}
  if(order.length<labels.length)throw new RangeError('Dependency cycle at the cut');
  return order;
}
// Solve x_i=y_i+H_i(parents) in a supplied order; the order is not checked here.
function solveInOrder(H,y,order){
  let x=nil();
  for(const i of order){const xi=vector(coordOf(y,i).plus(coordOf(evalOp(H,x),i)));x=vector(x.plus(xi.times(W(i))));}
  return vector(x);
}
// ---- Theorem 1 ----
function decodeDependency(packet,order=null){
  const H=complement(packet.operation),edges=dependencyGraph(H),labels=H.input_labels;
  const chosen=order||topoOrder(labels,edges),pos=new Map(chosen.map((v,k)=>[v,k]));
  if(chosen.length!==labels.length||labels.some(l=>!pos.has(l)))throw new RangeError('Order must list every label once');
  for(const e of edges)if(pos.get(e.from)>=pos.get(e.to))throw new RangeError('Order violates dependency '+e.from+'->'+e.to);
  return {order:chosen,edges,state:solveInOrder(H,st(packet.target_state),chosen)};
}
// ---- Theorem 2 ----
function longestWalk(labels,edges,q){
  const memo=new Map();
  const go=(v,budget)=>{const key=v+':'+budget;if(memo.has(key))return memo.get(key);
    let best=0;for(const e of edges)if(e.from===v&&e.weight<=budget)best=Math.max(best,1+go(e.to,budget-e.weight));
    memo.set(key,best);return best;};
  return Math.max(0,...labels.map(v=>go(v,q)));
}
function decodeFeedback(packet){
  const H=complement(packet.operation),edges=dependencyGraph(H),labels=H.input_labels,q=packet.unit_memory_through;
  topoOrder(labels,edges.filter(e=>e.weight===0));
  const N=labels.length*(q+1),sharp=1+longestWalk(labels,edges,q),y=st(packet.target_state);
  let x=cut(st(packet.seed),q);const trace=[x.toJSON()];
  for(let n=0;n<N;n++){x=cut(vector(y.plus(evalOp(H,x))),q);trace.push(x.toJSON());}
  return {edges,update_bound:N,sharp_bound:sharp,state:x,trace};
}
// Finite geometric inverse response (SE34.9) applied to a direction.
function inverseResponse(H,x,q,N,w){
  let term=cut(w,q),total=term;
  for(let j=1;j<N;j++){term=cut(response(H,x,term),q);total=vector(total.plus(term));}
  return total;
}
// ---- Theorem 3 ----
function liftCheck(packet){
  const Fop=packet.operation,G0=packet.cut_inverse;requireRational(G0);
  const F0=cutOp(Fop,0),y0=cut(st(packet.target_state),0);
  if(!evalOp(F0,evalOp(G0,y0)).equals(y0))throw new RangeError('Supplied cut inverse does not invert the cut at the target');
  return {Fop,G0,F0};
}
function decodeLift(packet){
  const {Fop,G0,F0}=liftCheck(packet),q=packet.unit_memory_through,y=st(packet.target_state);
  let x=cut(evalOp(G0,y),q);const trace=[x.toJSON()];
  for(let n=0;n<q;n++){
    const lamB=vector(evalOp(Fop,x).minus(evalOp(F0,x)));
    x=cut(evalOp(G0,cut(vector(y.minus(lamB)),q)),q);trace.push(x.toJSON());
  }
  return {state:x,trace};
}
// ---- Theorem 4 ----
function decodeResidualLayers(packet){
  const {Fop,G0}=liftCheck(packet),q=packet.unit_memory_through,y=st(packet.target_state),y0=cut(y,0);
  const A0inv=w=>cut(response(G0,y0,w),0);
  let x=cut(evalOp(G0,y0),0);const trace=[x.toJSON()];
  for(let r=1;r<=q;r++){
    const e=layerOf(vector(y.minus(evalOp(Fop,x))),r);
    x=vector(x.plus(A0inv(e).times(W(0,r))));trace.push(x.toJSON());
  }
  return {state:x,trace};
}
function correction(Fop,F0,G0,x,y,q,wrongOrder=false){
  const x0=cut(x,0),y0=cut(y,0),A0inv=w=>response(G0,y0,cut(w,q)),A0=h=>response(F0,x0,h);
  const E=h=>vector(response(Fop,x,h).minus(A0(h))),C=h=>cut(A0inv(E(h)),q);
  const series=w=>{let term=cut(w,q),total=term;for(let j=1;j<=q;j++){term=cut(vector(C(term).scale(-1)),q);total=vector(total.plus(term));}return total;};
  const w=cut(vector(y.minus(evalOp(Fop,x))),q);
  return wrongOrder?cut(A0inv(series(w)),q):series(cut(A0inv(w),q));
}
function decodeDoubling(packet,wrongOrder=false){
  const {Fop,G0,F0}=liftCheck(packet),q=packet.unit_memory_through,y=st(packet.target_state);
  let x=cut(evalOp(G0,cut(y,0)),q);
  const residualOrder=()=>unitOrder(cut(vector(y.minus(evalOp(Fop,x))),q));
  const trace=[{state:x.toJSON(),residual_order:residualOrder()}];
  for(let k=0;k<=q&&residualOrder()<=q;k++){
    x=cut(vector(x.plus(correction(Fop,F0,G0,x,y,q,wrongOrder))),q);
    trace.push({state:x.toJSON(),residual_order:residualOrder()});
  }
  return {state:x,trace,corrections:trace.length-1};
}
const enc=r=>Number.isFinite(r)?r:'none through retained depth';
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE35_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const pt=(labels,vals)=>sum(labels.map((n,i)=>W(n,0,String(vals[i]))));
  const L1=c=>vector(one.plus(W(0,1,c)));
  // -------------------------------------------------- Theorem 1
  const lab=[0,2,5];
  const opDep=buildOp({labels:lab,outputs:lab,terms:[T(0,one,{0:1}),T(2,one,{2:1}),T(5,one,{5:1}),T(5,vector(L1(1).scale(-1)),{0:2}),T(2,W(0,0,-1),{5:1,0:1})]});
  const yDep=vector(pt(lab,['2/3','-1/2',3]).plus(W(5,1,'1/4')));
  const depPacket={target:'Source of F=x-H with H_5=(1+Lambda)x_0^2 and H_2=x_5x_0 on labels 0,2,5',operation:opDep,target_state:yDep.toJSON()};
  check('dependency_graph_is_read_from_the_saved_bank',()=>{
    const e=dependencyGraph(complement(roundTrip(opDep))).map(x=>[x.from,x.to,x.weight]);
    assert.deepEqual(e,[[0,2,0],[0,5,0],[5,2,0]]);
  });
  check('dependency_order_solves_the_relabelled_example_exactly',()=>{
    const r=decodeDependency(roundTrip(depPacket));assert.deepEqual(r.order,[0,5,2]);
    const y0=coordOf(yDep,0),y2=coordOf(yDep,2),y5=coordOf(yDep,5);
    const x5=vector(y5.plus(L1(1).times(y0).times(y0))),x2=vector(y2.plus(x5.times(y0)));
    assert(r.state.equals(sum([y0.times(W(0)),x2.times(W(2)),x5.times(W(5))])));
    assert(evalOp(opDep,r.state).equals(yDep));
    details.dependency_order_certificate={...depPacket,decoded:{order:r.order,edges:r.edges,state:r.state.toJSON()}};
  });
  check('inverse_is_two_sided_on_rational_and_unit_valued_states',()=>{
    for(const z of [pt(lab,[1,2,3]),pt(lab,['-1/3',0,'5/2']),vector(pt(lab,[2,-1,0]).plus(W(0,1,3)).plus(W(2,2,'-1/2')))]){
      const r=decodeDependency({...depPacket,target_state:evalOp(opDep,z).toJSON()});assert(r.state.equals(vector(z)));
    }
  });
  check('every_valid_order_gives_the_same_inverse',()=>{
    const extra=buildOp({labels:[0,1,2,3],outputs:[0,1,2,3],terms:[0,1,2,3].map(i=>T(i,one,{[i]:1})).concat([T(2,W(0,0,-1),{0:2}),T(3,W(0,0,-1),{1:1}),T(1,W(0,0,-2),{0:1})])});
    const y=pt([0,1,2,3],[1,'1/2',-2,'3/7']),pkt={target:'Source on four labels',operation:extra,target_state:y.toJSON()};
    const orders=[[0,1,2,3],[0,1,3,2],[0,2,1,3]],sols=orders.map(o=>decodeDependency(pkt,o).state);
    for(const s of sols){assert(s.equals(sols[0]));assert(evalOp(extra,s).equals(y));}
  });
  check('relabelling_transports_equations_and_graph_together',()=>{
    const map={0:7,2:1,5:3},rl=[1,3,7];
    const opR=buildOp({labels:rl,outputs:rl,terms:[T(7,one,{7:1}),T(1,one,{1:1}),T(3,one,{3:1}),T(3,vector(L1(1).scale(-1)),{7:2}),T(1,W(0,0,-1),{3:1,7:1})]});
    const yR=sum(coordinates(yDep).map(([n,c])=>vector(c).times(W(map[n])))),r=decodeDependency({...depPacket,operation:opR,target_state:yR.toJSON()});
    const x=decodeDependency(depPacket).state,xR=sum(coordinates(x).map(([n,c])=>vector(c).times(W(map[n]))));
    assert(r.state.equals(xR));assert.deepEqual(r.order,[7,3,1]);
  });
  check('increasing_label_order_is_refused_and_would_misdecode',()=>{
    assert.throws(()=>decodeDependency(depPacket,[0,2,5]),/violates dependency 5->2/);
    const bad=solveInOrder(complement(opDep),yDep,[0,2,5]);assert(!evalOp(opDep,bad).equals(yDep));
  },true);
  check('fixed_counting_order_condition_rejects_the_same_bank',()=>{
    const read=t=>{const k=[...t].sort((a,b)=>a-b).join(',');
      if(k==='0,0')return vector(L1(1).times(W(5)));if(k==='0,5')return vector(W(2,0,'1/2'));return vector(nil());};
    assert.throws(()=>joint.inversePacket([{arity:2,read}],5,yDep),/lowering/);
  },true);
  check('acyclic_infinite_raising_has_no_finite_support_preimage',()=>{
    for(let n=0;n<=6;n++){const x=sum(Array.from({length:n+1},(_,r)=>W(r)));
      const img=vector(x.minus(sum(Array.from({length:n+1},(_,r)=>W(r+1)))));
      assert(img.equals(vector(W(0).minus(W(n+1)))));assert(!img.equals(vector(W(0))));}
  },true);
  // -------------------------------------------------- Theorem 2
  const lab2=[0,2];
  const opCycle=buildOp({labels:lab2,outputs:lab2,terms:[T(0,one,{0:1}),T(0,W(0,0,-1),{2:2}),T(2,one,{2:1}),T(2,W(0,1,-1),{0:1})]});
  const a=new F('1/2'),b=new F('-1/3'),cc=a.add(b.mul(b));
  const yCycle=pt(lab2,[a,b]);
  const closed=(()=>{const c=cc,B=b,t=(...xs)=>xs.reduce((u,v)=>u.mul(v),new F(1));
    const x0=[c,t(2,B,c),t(4,B,B,c).add(t(c,c)),t(8,B,B,B,c).add(t(6,B,c,c))],x2=[B,c,t(2,B,c),t(4,B,B,c).add(t(c,c))];
    return sum([...x0.map((v,r)=>W(0,r,v.toString())),...x2.map((v,r)=>W(2,r,v.toString()))]);})();
  const cyclePacket=(seed,q=3)=>({target:'Source of the two-label feedback cycle (x_0-x_2^2, x_2-Lambda x_0)',operation:opCycle,target_state:yCycle.toJSON(),unit_memory_through:q,seed:vector(seed).toJSON()});
  check('weighted_graph_has_a_cycle_whose_cut_graph_is_acyclic',()=>{
    const e=dependencyGraph(complement(opCycle)).map(x=>[x.from,x.to,x.weight]);
    assert.deepEqual(e,[[0,2,1],[2,0,0]]);
    assert.throws(()=>topoOrder(lab2,dependencyGraph(complement(opCycle))),/cycle/);
    assert.deepEqual(topoOrder(lab2,dependencyGraph(complement(opCycle)).filter(x=>x.weight===0)),[2,0]);
  });
  check('feedback_iteration_reaches_the_stated_series_from_every_seed',()=>{
    for(const seed of [nil(),pt(lab2,[3,'-7/2']),vector(pt(lab2,[-1,1]).plus(W(0,2,5)).plus(W(2,3,-4)))]){
      const r=decodeFeedback(roundTrip(cyclePacket(seed)));
      assert.equal(r.update_bound,8);assert(r.state.equals(closed));
      assert(cut(evalOp(opCycle,r.state),3).equals(yCycle));
    }
    const r=decodeFeedback(cyclePacket(nil()));
    details.feedback_cycle_certificate={...cyclePacket(nil()),decoded:{edges:r.edges,update_bound:r.update_bound,sharp_bound:r.sharp_bound,state:r.state.toJSON(),trace:r.trace}};
  });
  check('sharper_walk_bound_is_attained_and_sufficient',()=>{
    for(const q of [0,1,2,3,4]){
      const r=decodeFeedback(cyclePacket(nil(),q));assert.equal(r.sharp_bound,2*q+2);
      const at=st(r.trace[r.sharp_bound]);assert(at.equals(r.state));
      if(q>0)assert(!st(r.trace[r.sharp_bound-2]).equals(r.state));
    }
  });
  check('one_update_before_the_walk_bound_misses_the_last_layer',()=>{
    const r=decodeFeedback(cyclePacket(nil(),3));
    assert(!st(r.trace[r.sharp_bound-1]).equals(r.state));
  },true);
  check('inverse_response_is_the_finite_geometric_sum',()=>{
    const q=3,H=complement(opCycle),x=decodeFeedback(cyclePacket(nil(),q)).state,N=8;
    for(const w of [W(0),W(2),pt(lab2,['2/5',-3]),vector(W(0,1,2).plus(W(2)))]){
      let p=cut(w,q);for(let j=0;j<N;j++)p=cut(response(H,x,p),q);assert(p.equals(nil()));
      const s=inverseResponse(H,x,q,N,w),IminusJ=v=>cut(vector(vector(v).minus(response(H,x,v))),q);
      assert(IminusJ(s).equals(cut(w,q)));assert(inverseResponse(H,x,q,N,IminusJ(w)).equals(cut(w,q)));
      assert(cut(response(opCycle,x,s),q).equals(cut(w,q)));
    }
  });
  check('zero_weight_cycle_is_refused_and_is_not_injective',()=>{
    const op=buildOp({labels:lab2,outputs:lab2,terms:[T(0,one,{0:1}),T(0,W(0,0,-1),{2:1}),T(2,one,{2:1}),T(2,W(0,0,-1),{0:1})]});
    assert.throws(()=>decodeFeedback({...cyclePacket(nil()),operation:op}),/cycle/);
    assert(evalOp(op,pt(lab2,[1,1])).equals(evalOp(op,pt(lab2,[0,0]))));
  },true);
  // -------------------------------------------------- Theorem 3
  const q5=5,labX=[0,1,2,3,4,5];
  const opRaise=buildOp({labels:labX,outputs:[...labX,6],terms:labX.flatMap(n=>[T(n,one,{[n]:1}),T(n+1,W(0,1,-1),{[n]:1})])});
  const idX=buildOp({labels:labX,outputs:labX,terms:labX.map(n=>T(n,one,{[n]:1}))});
  check('raising_lift_retains_new_count_support',()=>{
    const pkt={target:'Retained inverse of I-Lambda X at p_0',operation:opRaise,cut_inverse:idX,target_state:vector(W(0)).toJSON(),unit_memory_through:q5};
    const r=decodeLift(roundTrip(pkt)),want=sum(Array.from({length:q5+1},(_,k)=>W(k,k)));
    assert(r.state.equals(want));
    assert(evalOp(opRaise,r.state).equals(vector(W(0).minus(W(q5+1,q5+1)))));
    r.trace.forEach((u,k)=>assert(cut(st(u),k).equals(cut(want,k))));
    details.raising_lift_certificate={...pkt,decoded:{state:r.state.toJSON(),trace:r.trace}};
  });
  const opRet=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:1}),T(0,W(0,1,-1),{0:2})]}),id0=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:1})]});
  const retPacket=(y,q)=>({target:'Retained source of x-Lambda x^2',operation:opRet,cut_inverse:id0,target_state:vector(y).toJSON(),unit_memory_through:q});
  const catalan=[1,1,2,5,14,42,132];
  check('self_return_lift_counts_the_return_coefficients',()=>{
    const r=decodeLift(roundTrip(retPacket(W(0),6)));
    assert(r.state.equals(sum(catalan.map((c,k)=>W(0,k,c)))));
    const y=new F('2/3'),r2=decodeLift(retPacket(W(0,0,'2/3'),6));
    assert(r2.state.equals(sum(catalan.map((c,k)=>W(0,k,new F(c).mul(y.pow(k+1)).toString())))));
    details.self_return_certificate={...retPacket(W(0),6),decoded:{state:r.state.toJSON(),trace:r.trace}};
  });
  check('nth_iterate_agrees_through_degree_n_and_not_beyond',()=>{
    const r=decodeLift(retPacket(W(0),6));
    for(let n=0;n<6;n++){assert(cut(st(r.trace[n]),n).equals(cut(r.state,n)));assert(!cut(st(r.trace[n]),n+1).equals(cut(r.state,n+1)));}
  },true);
  const opSelf=buildOp({labels:[0],outputs:[0],terms:[T(0,W(0,0,-1),{0:1}),T(0,Lam,{0:3})]}),neg0=buildOp({labels:[0],outputs:[0],terms:[T(0,W(0,0,-1),{0:1})]});
  check('an_available_cut_inverse_lifts_where_the_graph_condition_fails',()=>{
    const y=pt([0],['3/2']),q=4,pkt={target:'Retained source of -x+Lambda x^3',operation:opSelf,cut_inverse:neg0,target_state:y.toJSON(),unit_memory_through:q};
    assert.throws(()=>decodeFeedback({...pkt,seed:nil().toJSON()}),/cycle/);
    const r=decodeLift(roundTrip(pkt));assert(cut(evalOp(opSelf,r.state),q).equals(y));
    const r2=decodeLift({...pkt,target_state:evalOp(opSelf,r.state).toJSON()});assert(r2.state.equals(r.state));
    details.self_cycle_lift_certificate={...pkt,decoded:{state:r.state.toJSON(),trace:r.trace}};
  });
  const G0cycle=buildOp({labels:lab2,outputs:lab2,terms:[T(0,one,{0:1}),T(0,one,{2:2}),T(2,one,{2:1})]});
  check('cut_inverse_lift_agrees_with_the_feedback_fixed_point',()=>{
    const pkt={target:'Source of the two-label feedback cycle',operation:opCycle,cut_inverse:G0cycle,target_state:yCycle.toJSON(),unit_memory_through:3};
    assert(decodeLift(pkt).state.equals(closed));
    for(const z of [pt(lab2,[2,-1]),vector(pt(lab2,['1/3',0]).plus(W(2,1,2)))]){
      const r=decodeLift({...pkt,target_state:evalOp(opCycle,z).toJSON()});assert(r.state.equals(cut(z,3)));
    }
  });
  check('wrong_or_missing_cut_inverse_is_refused',()=>{
    const pkt={target:'x',operation:opSelf,cut_inverse:id0,target_state:pt([0],['3/2']).toJSON(),unit_memory_through:2};
    assert.throws(()=>decodeLift(pkt),/does not invert/);
    const sq=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:2}),T(0,Lam,{0:3})]});
    assert(evalOp(cutOp(sq,0),pt([0],[2])).equals(evalOp(cutOp(sq,0),pt([0],[-2]))));
    assert.throws(()=>decodeLift({...pkt,operation:sq,target_state:pt([0],[4]).toJSON()}),/does not invert/);
    const unitG=buildOp({labels:[0],outputs:[0],terms:[T(0,L1(1),{0:1})]});
    assert.throws(()=>decodeLift({...pkt,operation:opRet,cut_inverse:unitG}),/unit-degree-zero/);
  },true);
  check('null_cut_leaves_the_highest_retained_layer_unread',()=>{
    const op=buildOp({labels:[0],outputs:[0],terms:[T(0,Lam,{0:1})]}),q=3;
    for(const x of [pt([0],[0]),pt([0],[5]),vector(W(0,2,7))])assert(unitOrder(evalOp(op,x))>=1);
    const z=vector(W(0,0,2).plus(W(0,1,-1))),z2=vector(z.plus(W(0,q,9)));
    assert(cut(evalOp(op,z),q).equals(cut(evalOp(op,z2),q)));assert(!cut(z,q).equals(cut(z2,q)));
  },true);
  check('formal_inverse_is_not_a_numerical_unit_inverse',()=>{
    const op=buildOp({labels:[0],outputs:[0],terms:[T(0,vector(one.minus(Lam)),{0:1})]});
    const r=decodeLift({target:'Retained source of (1-Lambda)x',operation:op,cut_inverse:id0,target_state:vector(W(0)).toJSON(),unit_memory_through:4});
    assert(r.state.equals(sum([0,1,2,3,4].map(k=>W(0,k)))));
    assert(atUnitOne(evalOp(op,pt([0],[1]))).equals(nil()));assert(atUnitOne(evalOp(op,pt([0],[7]))).equals(nil()));
  },true);
  // -------------------------------------------------- Theorem 4
  check('each_residual_coefficient_supplies_the_next_source_coefficient',()=>{
    const pkt=retPacket(W(0),6),r=decodeResidualLayers(roundTrip(pkt));
    assert(r.state.equals(decodeLift(pkt).state));
    r.trace.forEach((u,k)=>{assert(st(u).equals(cut(r.state,k)));});
    const cy={target:'Source of the two-label feedback cycle',operation:opCycle,cut_inverse:G0cycle,target_state:yCycle.toJSON(),unit_memory_through:3};
    assert(decodeResidualLayers(cy).state.equals(closed));
    const sp={target:'Retained source of -x+Lambda x^3',operation:opSelf,cut_inverse:neg0,target_state:pt([0],['3/2']).toJSON(),unit_memory_through:4};
    assert(decodeResidualLayers(sp).state.equals(decodeLift(sp).state));
    details.residual_layer_certificate={...pkt,decoded:{state:r.state.toJSON(),trace:r.trace}};
  });
  check('residual_without_the_cut_response_inverse_misdecodes',()=>{
    const sp={target:'x',operation:opSelf,cut_inverse:neg0,target_state:pt([0],['3/2']).toJSON(),unit_memory_through:3};
    const y=st(sp.target_state);let x=cut(evalOp(neg0,y),0);
    for(let r=1;r<=3;r++)x=vector(x.plus(layerOf(vector(y.minus(evalOp(opSelf,x))),r).times(W(0,r))));
    assert(!x.equals(decodeLift(sp).state));
  },true);
  check('order_doubling_matches_the_worked_return_example',()=>{
    const r=decodeDoubling(roundTrip(retPacket(W(0),3)));
    assert.deepEqual(r.trace.map(t=>enc(t.residual_order)),[1,3,'none through retained depth']);
    assert(st(r.trace[1].state).equals(sum([[0,1],[1,1],[2,2],[3,4]].map(([k,c])=>W(0,k,c)))));
    assert(r.state.equals(sum([[0,1],[1,1],[2,2],[3,5]].map(([k,c])=>W(0,k,c)))));
    assert.equal(r.corrections,2);
  });
  check('order_doubling_uses_at_most_ceil_log2_corrections',()=>{
    for(const q of [0,1,3,7]){
      const r=decodeDoubling(retPacket(W(0),q));assert(r.state.equals(cut(sum(catalan.concat([429]).map((c,k)=>W(0,k,c))),q)));
      assert(r.corrections<=Math.ceil(Math.log2(q+1)));
      for(let k=1;k<r.trace.length;k++)assert(r.trace[k].residual_order>=Math.min(q+1,2*r.trace[k-1].residual_order));
    }
    const cy={target:'Source of the two-label feedback cycle',operation:opCycle,cut_inverse:G0cycle,target_state:yCycle.toJSON(),unit_memory_through:7};
    const r=decodeDoubling(roundTrip(cy));assert(cut(evalOp(opCycle,r.state),7).equals(yCycle));
    assert(r.state.equals(decodeLift(cy).state));assert(r.corrections<=3);
    details.order_doubling_certificate={...cy,decoded:{state:r.state.toJSON(),trace:r.trace.map(t=>({state:t.state,residual_order:enc(t.residual_order)})),corrections:r.corrections}};
  });
  check('reversed_operator_order_in_the_inverse_response_loses_the_doubling',()=>{
    const cy={target:'x',operation:opCycle,cut_inverse:G0cycle,target_state:yCycle.toJSON(),unit_memory_through:7};
    const y=yCycle,{Fop,G0,F0}=liftCheck(cy);let x=cut(evalOp(G0,cut(y,0)),7);
    x=cut(vector(x.plus(correction(Fop,F0,G0,x,y,7))),7);
    const good=cut(vector(x.plus(correction(Fop,F0,G0,x,y,7))),7),bad=cut(vector(x.plus(correction(Fop,F0,G0,x,y,7,true))),7);
    const ord=s=>unitOrder(cut(vector(y.minus(evalOp(Fop,s))),7));
    assert(ord(good)>=Math.min(8,2*ord(x)));assert(ord(bad)<Math.min(8,2*ord(x)));
  },true);
  // -------------------------------------------------- Frame transport
  check('frame_transport_moves_the_lifted_solution_and_changes_the_graph',()=>{
    const U=[[1,1],[0,1]].map(r=>r.map(x=>new F(x))),V=[[2,0],[1,1]].map(r=>r.map(x=>new F(x)));
    const lin=(M,v)=>sum(lab2.map((n,i)=>vector(M[i].reduce((acc,m,j)=>m.zero()?acc:acc.plus(coordOf(v,lab2[j]).scale(m)),nil())).times(W(n))));
    const Ft=transportOp(opCycle,U,V),Gt=transportOp(G0cycle,V,U),yt=lin(V,yCycle);
    const pkt={target:'Source in transported frames',operation:Ft,cut_inverse:Gt,target_state:yt.toJSON(),unit_memory_through:3};
    const r=decodeLift(roundTrip(pkt));assert(r.state.equals(cut(lin(U,closed),3)));
    const e0=dependencyGraph(complement(opCycle)).map(x=>[x.from,x.to,x.weight]),e1=dependencyGraph(complement(Ft)).map(x=>[x.from,x.to,x.weight]);
    assert.notDeepEqual(e0,e1);
    details.transport_certificate={...pkt,U:U.map(r=>r.map(String)),V:V.map(r=>r.map(String)),decoded:r.state.toJSON(),transported_edges:e1};
  });
  check('every_archived_certificate_redecodes_from_its_saved_readings',()=>{
    const arc=roundTrip(details),same=(a,b)=>st(a).equals(st(b));
    assert(same(decodeDependency(arc.dependency_order_certificate).state.toJSON(),arc.dependency_order_certificate.decoded.state));
    assert(same(decodeFeedback(arc.feedback_cycle_certificate).state.toJSON(),arc.feedback_cycle_certificate.decoded.state));
    for(const k of ['raising_lift_certificate','self_return_certificate','self_cycle_lift_certificate'])assert(same(decodeLift(arc[k]).state.toJSON(),arc[k].decoded.state));
    assert(same(decodeResidualLayers(arc.residual_layer_certificate).state.toJSON(),arc.residual_layer_certificate.decoded.state));
    assert(same(decodeDoubling(arc.order_doubling_certificate).state.toJSON(),arc.order_doubling_certificate.decoded.state));
    assert(same(decodeLift(arc.transport_certificate).state.toJSON(),arc.transport_certificate.decoded));
  });
  return {schema:'rkf.lambda-unit-memory-lifting.v1',date:'2026-10-12',status:'PASS_DEPENDENCY_FEEDBACK_AND_UNIT_MEMORY_LIFTING',
    theorem_count:4,proposition_count:1,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting sectors over Q[Lambda] and their retained unit quotients',source:'Saved joint banks of the operation, a supplied cut-inverse bank where stated, and the target state',
      zero:'Typed cut operation; additive neutrals retain their separate types',primitive_metric:false,analytic_derivative_assumed:false,numerical_unit_value_assumed:false,RH_development:false,curvature_developed:false},
    finite_ranges:{dependency_labels:3,feedback_unit_depths:'0..4',raising_unit_depth:q5,self_return_unit_depth:6,doubling_unit_depths:[0,1,3,7],transport_matrix_size:2},
    details,evidence:{general_results:'Four written derivations and the frame-transport identity',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['convergence after substituting a nonzero numerical unit value','inversion on an infinite acyclic graph within finite support','a manufactured inverse for a singular or multi-branch cut',
      'recovery from unmodelled noise','a complexity bound independent of support, degree or coefficient size','new RH or curvature result','novelty priority for triangular inversion, formal inverse lifting or order doubling']};
}
module.exports={complement,dependencyGraph,decodeDependency,decodeFeedback,decodeLift,decodeResidualLayers,decodeDoubling,response,cutOp,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE34_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}
