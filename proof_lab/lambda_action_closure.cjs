'use strict';
// SE36 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const joint=require('./lambda_joint_readings.cjs');
const active=require('./lambda_active_readings.cjs');
const {F}=o,S=previous.presentation,{vector}=count,{coordinates}=joint;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_ACTION_CLOSURE_RESULT.json');
const W=(n=0,d=0,c=1)=>S.word([...Array(d).fill('L'),...Array(n).fill('X')],c);
const nil=()=>S.zero(),ud=w=>w.filter(t=>t==='L').length;
const sum=xs=>vector(xs.reduce((a,b)=>a.plus(b),nil()));
const roundTrip=x=>JSON.parse(JSON.stringify(x));
const Q=x=>x instanceof F?x:new F(x);
// ---- retained unit scalars: coefficient lists over Q, cut after unit degree q ----
const INF=Infinity;
function sNorm(a,q){let b=a.slice(0,Number.isFinite(q)?q+1:a.length);while(b.length&&b[b.length-1].zero())b.pop();return b;}
const sc=(...cs)=>sNorm(cs.map(Q),INF);
function sAdd(a,b,q){const n=Math.max(a.length,b.length),r=[];for(let i=0;i<n;i++)r.push((a[i]||new F(0)).add(b[i]||new F(0)));return sNorm(r,q);}
const sNeg=a=>a.map(x=>x.neg());
const sSub=(a,b,q)=>sAdd(a,sNeg(b),q);
function sMul(a,b,q){if(!a.length||!b.length)return [];const n=a.length+b.length-1,lim=Number.isFinite(q)?Math.min(n,q+1):n,r=Array.from({length:lim},()=>new F(0));
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length&&i+j<lim;j++)r[i+j]=r[i+j].add(a[i].mul(b[j]));return sNorm(r,q);}
const sEq=(a,b)=>!sSub(a,b,INF).length;
const sUnit=(d,c=1)=>sNorm([...Array(d).fill(new F(0)),Q(c)],INF);
// Inverse of a scalar with invertible cut coefficient, through depth q.
function sInv(a,q){if(!a.length||a[0].zero())throw new RangeError('Cut coefficient must be invertible');
  const r=[new F(1).div(a[0])];for(let k=1;k<=q;k++){let s=new F(0);for(let j=1;j<=k;j++)s=s.add((a[j]||new F(0)).mul(r[k-j]));r.push(s.neg().div(a[0]));}return sNorm(r,q);}
// ---- polynomial response functions on n counting coordinates ----
const keyOf=e=>e.join(','),expOf=k=>k===''?[]:k.split(',').map(Number);
function pNorm(m,q){const r=new Map();for(const [k,s]of m){const t=sNorm(s,q);if(t.length)r.set(k,t);}return r;}
const pConst=(n,s)=>pNorm(new Map([[keyOf(Array(n).fill(0)),s]]),INF);
const pVar=(n,i,s=sc(1))=>{const e=Array(n).fill(0);e[i]=1;return pNorm(new Map([[keyOf(e),s]]),INF);};
function pAdd(a,b,q){const r=new Map(a);for(const [k,s]of b)r.set(k,r.has(k)?sAdd(r.get(k),s,INF):s);return pNorm(r,q);}
const pScale=(a,s,q)=>pNorm(new Map([...a].map(([k,t])=>[k,sMul(t,s,q)])),q);
const pSub=(a,b,q)=>pAdd(a,pScale(b,sc(-1),INF),q);
function pMul(a,b,q){const r=new Map();for(const [k1,s1]of a)for(const [k2,s2]of b){const e1=expOf(k1),e2=expOf(k2),k=keyOf(e1.map((x,i)=>x+e2[i]));const t=sMul(s1,s2,q);if(t.length)r.set(k,r.has(k)?sAdd(r.get(k),t,q):t);}return pNorm(r,q);}
const pEq=(a,b)=>!pSub(a,b,INF).size;
const pDeg=a=>Math.max(-1,...[...a.keys()].map(k=>expOf(k).reduce((x,y)=>x+y,0)));
// Substitute polynomials for the variables of p; the result lives in the variables of subs.
const pVars=(polys,fallback)=>{for(const r of polys)for(const k of r.keys())return expOf(k).length;return fallback;};
function pCompose(p,subs,q){
  const n=pVars(subs,subs.length),powCache=subs.map(()=>[null]);
  const pw=(i,e)=>{const c=powCache[i];if(!c[1])c[1]=subs[i];while(c.length<=e)c.push(pMul(c[c.length-1],subs[i],q));return e===0?pConst(n,sc(1)):c[e];};
  let r=new Map();
  for(const [k,s]of p){const e=expOf(k);let t=pConst(n,s);e.forEach((x,i)=>{if(x)t=pMul(t,pw(i,x),q);});r=pAdd(r,t,q);}
  return r;
}
function pEval(p,pt,q){let r=[];for(const [k,s]of p){let t=s;expOf(k).forEach((x,i)=>{for(let j=0;j<x;j++)t=sMul(t,pt[i],q);});r=sAdd(r,t,q);}return r;}
const actOn=(g,pt,q)=>g.map(c=>pEval(c,pt,q));
const composeMaps=(f,g,q)=>f.map(c=>pCompose(c,g,q));// (f o g)
// ---- readings stored as counting states: channel label j, unit degree d ----
const toState=vals=>sum(vals.flatMap((s,j)=>s.map((c,d)=>W(j,d,c.toString()))));
function fromState(json,m){const v=vector(S.fromJSON(json)),m2=new Map(coordinates(v)),out=[];
  for(let j=0;j<m;j++){const s=[];for(const [w,c]of vector(m2.get(j)||nil()).entries()){const d=ud(w);while(s.length<=d)s.push(new F(0));s[d]=s[d].add(c.rad);}out.push(sNorm(s,INF));}
  for(const n of m2.keys())if(n>=m)throw new RangeError('Reading outside declared output channels');
  return out;}
// ---- exact Q-linear spans of response functions with provenance ----
function pVec(p){const v=new Map();for(const [k,s]of p)s.forEach((c,d)=>{if(!c.zero())v.set(k+'|'+d,c);});return v;}
class Span{
  constructor(){this.rows=[];this.size=0;}
  reduce(vec){const v=new Map(vec),combo=new Map();
    for(const r of this.rows){const c=v.get(r.pivot);if(!c||c.zero())continue;
      for(const [k,x]of r.vec){const y=(v.get(k)||new F(0)).sub(c.mul(x));if(y.zero())v.delete(k);else v.set(k,y);}
      for(const [i,x]of r.combo){const y=(combo.get(i)||new F(0)).add(c.mul(x));if(y.zero())combo.delete(i);else combo.set(i,y);}}
    return {rem:v,combo};}
  add(vec){const {rem,combo}=this.reduce(vec);if(!rem.size)return false;
    const idx=this.size++,piv=[...rem.keys()].sort()[0],d=rem.get(piv),c2=new Map([[idx,new F(1)]]);
    for(const [i,x]of combo)c2.set(i,x.neg());
    this.rows.push({pivot:piv,vec:new Map([...rem].map(([k,x])=>[k,x.div(d)])),combo:new Map([...c2].map(([i,x])=>[i,x.div(d)]))});return true;}
  coords(vec){const {rem,combo}=this.reduce(vec);if(rem.size)return null;const r=Array.from({length:this.size},()=>new F(0));for(const [i,x]of combo)r[i]=x;return r;}
}
// Closure (SE36.8)/(SE36.13): Q-span of supplied readings, their unit multiples, closed under pullbacks.
function closure({n,sensors,actions,q=0,maxStages=64}){
  const span=new Span(),basis=[];
  const offer=(f,wit)=>{if(span.add(pVec(f))){basis.push({f,witness:wit});return true;}return false;};
  for(let a=0;a<=(Number.isFinite(q)?q:0);a++){
    offer(pConst(n,sUnit(a)),{constant:true,unit_shift:a,word:[]});
    sensors.forEach((F_,j)=>offer(pScale(F_,sUnit(a),q),{channel:j,unit_shift:a,word:[]}));
  }
  const stages=[basis.length];let frontier=basis.slice(),increases=0;
  for(let s=0;s<maxStages&&frontier.length;s++){
    const next=[];
    for(const b of frontier)for(let i=0;i<actions.length;i++){
      if(b.witness.constant)continue;
      const f=pCompose(b.f,actions[i],q),wit={...b.witness,word:[i,...b.witness.word]};
      if(offer(f,wit))next.push(basis[basis.length-1]);
    }
    if(next.length)increases++;stages.push(basis.length);frontier=next;
  }
  if(frontier.length)throw new RangeError('No closure within the stage limit');
  const matrices=actions.map(g=>basis.map(b=>{const c=span.coords(pVec(pCompose(b.f,g,q)));if(!c)throw new Error('Closure failed');return c;}));
  return {span,basis,matrices,stages,increases};
}
const binom=(a,b)=>{let r=1n;for(let i=1n;i<=BigInt(b);i++)r=r*(BigInt(a)-BigInt(b)+i)/i;return Number(r);};
// Apply a word (actions in order) to a point.
const runWord=(actions,word,pt,q)=>word.reduce((x,i)=>actOn(actions[i],x,q),pt);
// ---- observer packets ----
// The observer records the sensor reading for each retained protocol and for supplied future protocols.
function closurePacket(target,{n,sensors,actions,q},cl,x,future){
  const m=sensors.length,read=w=>toState(sensors.map(F_=>pEval(F_,runWord(actions,w,x,q),q))).toJSON();
  return {target,unit_memory_through:Number.isFinite(q)?q:null,output_channels:m,
    protocols:cl.basis.map(b=>({witness:b.witness,reading:b.witness.constant?null:read(b.witness.word)})),
    action_matrices:cl.matrices.map(M=>M.map(r=>r.map(String))),
    sensor_coordinates:sensors.map(F_=>cl.span.coords(pVec(F_)).map(String)),
    future_protocols:future.map(w=>({word:w,reading:read(w)}))};
}
// Decode the completed response vector from the recorded protocols, then predict future readings.
function decodeClosure(packet){
  const q=packet.unit_memory_through===null?INF:packet.unit_memory_through,m=packet.output_channels;
  const Y=packet.protocols.map(p=>p.witness.constant?sUnit(p.witness.unit_shift):sMul(sUnit(p.witness.unit_shift),fromState(p.reading,m)[p.witness.channel],q));
  const M=packet.action_matrices.map(r=>r.map(row=>row.map(Q)));
  const apply=(Mi,y)=>Mi.map(row=>row.reduce((acc,c,k)=>c.zero()?acc:sAdd(acc,y[k].map(x=>x.mul(c)),q),[]));
  const predict=w=>{const y=w.reduce((acc,i)=>apply(M[i],acc),Y);return packet.sensor_coordinates.map(cs=>cs.map(Q).reduce((acc,c,k)=>c.zero()?acc:sAdd(acc,y[k].map(x=>x.mul(c)),q),[]));};
  return {Y,predictions:packet.future_protocols.map(p=>({word:p.word,predicted:toState(predict(p.word)).toJSON()}))};
}
// Restricted translated signature (SE36.1)-(SE36.2).
function signaturePacket(target,{n,sensors,d},probes,c,x){
  const k=probes.length,grid=k?Array.from({length:d**k},(_,i)=>Array.from({length:k},(_,a)=>Math.floor(i/d**a)%d)):[[]];
  const shift=(pt,t)=>pt.map((s,i)=>sAdd(s,[probes.reduce((acc,h,a)=>acc.add(Q(h[i]).mul(new F(t[a]))),new F(0))],INF));
  return {target,declared_degree:d,probes:probes.map(h=>h.map(String)),calibration_note:'Calibration readings are subtracted in each recorded difference',
    readings:grid.map(t=>({t,response:toState(sensors.map((F_,j)=>sSub(pEval(F_,shift(x,t),INF),pEval(F_,shift(c,t),INF),INF))).toJSON()}))};
}
function decodeSignature(packet,m){
  const d=packet.declared_degree,k=packet.probes.length,table=new Map();
  for(const r of packet.readings){const key=r.t.join(',');if(table.has(key))throw new TypeError('Duplicate restricted reading');table.set(key,fromState(r.response,m));}
  const grid=k?Array.from({length:d**k},(_,i)=>Array.from({length:k},(_,a)=>Math.floor(i/d**a)%d)):[[]];
  for(const t of grid)if(!table.has(t.join(',')))throw new RangeError('Unread restricted probe '+t.join(','));
  if(!k)return new Map([['',table.get('')]]);
  const V=Array.from({length:d},(_,i)=>Array.from({length:d},(_,j)=>new F(i).pow(j))),Vinv=invQ(V);
  let cur=table;
  for(let a=0;a<k;a++){const next=new Map();for(const t of grid){const out=Array.from({length:m},()=>[]);
    for(let i=0;i<d;i++){const t2=t.slice();t2[a]=i;const r=cur.get(t2.join(','));r.forEach((s,j)=>{out[j]=sAdd(out[j],s.map(x=>x.mul(Vinv[t[a]][i])),INF);});}
    next.set(t.join(','),out);}cur=next;}
  return cur;
}
function invQ(M){const n=M.length,a=M.map((r,i)=>[...r,...Array.from({length:n},(_,j)=>new F(i===j?1:0))]);
  for(let j=0;j<n;j++){let p=a.findIndex((r,i)=>i>=j&&!r[j].zero());if(p<0)throw new RangeError('Singular matrix');[a[j],a[p]]=[a[p],a[j]];
    const d=a[j][j];a[j]=a[j].map(x=>x.div(d));for(let i=0;i<n;i++)if(i!==j&&!a[i][j].zero()){const f=a[i][j];a[i]=a[i].map((x,t)=>x.sub(f.mul(a[j][t])));}}
  return a.map(r=>r.slice(n));}
const sigEq=(A,B)=>A.size===B.size&&[...A].every(([k,v])=>B.has(k)&&v.every((s,j)=>sEq(s,B.get(k)[j])));
// Translation subspace synthesized by reversible linear actions (SE36.14).
function synthesize(n,H0,group){
  for(const g of group)if(!g.inverse)throw new RangeError('Inverse action not available');
  const span=new Span(),basis=[];const offer=(h,w)=>{const v=new Map(h.map((x,i)=>[String(i),Q(x)]).filter(([,x])=>!x.zero()));if(span.add(v)){basis.push({h:h.map(Q),word:w});return true;}return false;};
  H0.forEach((h,i)=>offer(h,{probe:i,word:[]}));
  let frontier=basis.slice(),increases=0;
  while(frontier.length){const next=[];
    for(const b of frontier)group.forEach((g,gi)=>[[g.matrix,'A'],[g.inverse,'A^-1']].forEach(([M,tag])=>{
      const h=M.map(r=>r.reduce((acc,x,j)=>acc.add(Q(x).mul(b.h[j])),new F(0)));
      if(offer(h,{...b.word,word:[tag+gi,...b.word.word]}))next.push(basis[basis.length-1]);}));
    if(next.length)increases++;frontier=next;}
  return {basis,increases,dimension:basis.length};
}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE34_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const u=pVar(2,0),v=pVar(2,1),one2=pConst(2,sc(1));
  const P=(...cs)=>cs.map(c=>sc(c));
  const sq=(a)=>pMul(a,a,INF);
  const Fuv=pAdd(sq(u),sq(v),INF);
  const shiftU=[pAdd(u,one2,INF),v],swap=[v,u];
  // -------------------------------------------------- Theorem 1
  const c2=P('1/3',2),x2=P('5/4','-2/3');
  check('restricted_signature_reads_u_and_v_squared',()=>{
    const pkt=signaturePacket('Restricted signature of u^2+v^2 under horizontal translations',{n:2,sensors:[Fuv],d:2},[[1,0]],c2,x2);
    const J=decodeSignature(roundTrip(pkt),1),lin=J.get('1')[0],cst=J.get('0')[0];
    const uHat=sAdd(c2[0],lin.map(x=>x.div(new F(2))),INF);assert(sEq(uHat,x2[0]));
    const vSq=sSub(sAdd(cst,pEval(Fuv,c2,INF),INF),sMul(uHat,uHat,INF),INF);assert(sEq(vSq,sMul(x2[1],x2[1],INF)));
    details.restricted_signature_certificate={...pkt,decoded:{u:uHat.map(String),v_squared:vSq.map(String)}};
  });
  check('restricted_fibre_is_the_sign_pair_while_the_full_blind_subspace_is_null',()=>{
    const sig=x=>decodeSignature(signaturePacket('t',{n:2,sensors:[Fuv],d:2},[[1,0]],c2,x),1);
    assert(sigEq(sig(x2),sig([x2[0],sNeg(x2[1])])));
    for(const z of [P('5/4','2/3').map((s,i)=>i?s:x2[0]),P('5/4',1),P(1,'-2/3')])if(!sEq(z[1],sNeg(x2[1])))assert(!sigEq(sig(x2),sig(z)));
    const op=active.buildOp({labels:[0,1],outputs:[0],terms:[{out:0,coeff:vector(W()),powers:{0:2}},{out:0,coeff:vector(W()),powers:{1:2}}]});
    assert.equal(active.kernelBasis(op).length,0);
  });
  check('restricted_fibres_are_not_cosets_of_a_fixed_subspace',()=>{
    const sig=x=>decodeSignature(signaturePacket('t',{n:2,sensors:[Fuv],d:2},[[1,0]],c2,x),1);
    // The only line through (0,2v) is the v-axis, but translating along it changes the signature.
    assert(!sigEq(sig(P(1,1)),sig(P(1,2))));assert(sigEq(sig(P(1,1)),sig(P(1,-1))));assert(sigEq(sig(P(1,2)),sig(P(1,-2))));
  },true);
  const G=pAdd(pMul(sq(pVar(3,0)),pVar(3,1),INF),pVar(3,2),INF),H2=pMul(pVar(3,1),sq(pVar(3,2)),INF);
  check('finite_probe_grid_determines_every_restricted_reading',()=>{
    const probes=[[1,0,0],[0,1,1]],c=P(0,'1/2',-1),x=P(2,'-1/3','3/5');
    const pkt=signaturePacket('Restricted signature of (u^2v+w, vw^2) on a two-direction probe family',{n:3,sensors:[G,H2],d:3},probes,c,x);
    assert.equal(pkt.readings.length,9);const J=decodeSignature(roundTrip(pkt),2);
    for(const t of [['3/2',-1],['-2/7','5/3'],[4,4]]){
      const pred=[0,1].map(j=>[...J].reduce((acc,[k,vals])=>{const e=expOf(k);let w=new F(1);e.forEach((x,a)=>{w=w.mul(Q(t[a]).pow(x));});return sAdd(acc,vals[j].map(y=>y.mul(w)),INF);},[]));
      const sh=pt=>pt.map((s,i)=>sAdd(s,[probes.reduce((acc,h,a)=>acc.add(Q(h[i]).mul(Q(t[a]))),new F(0))],INF));
      const direct=[G,H2].map(F_=>sSub(pEval(F_,sh(x),INF),pEval(F_,sh(c),INF),INF));
      pred.forEach((p,j)=>assert(sEq(p,direct[j])));
    }
    const k0=signaturePacket('t',{n:3,sensors:[G,H2],d:3},[],c,x);assert.equal(k0.readings.length,1);
    const J0=decodeSignature(k0,2).get('');[G,H2].forEach((F_,j)=>assert(sEq(J0[j],sSub(pEval(F_,x,INF),pEval(F_,c,INF),INF))));
  });
  check('omitted_or_duplicated_restricted_probe_is_rejected',()=>{
    const pkt=signaturePacket('t',{n:2,sensors:[Fuv],d:2},[[1,0]],c2,x2),a=roundTrip(pkt);a.readings.pop();
    assert.throws(()=>decodeSignature(a,1),/Unread/);const b=roundTrip(pkt);b.readings.push(b.readings[0]);assert.throws(()=>decodeSignature(b,1),/Duplicate/);
  },true);
  // -------------------------------------------------- Theorem 2
  const cubic=pAdd(pMul(sq(u),u,INF),v,INF);
  const sysCubic={n:2,sensors:[cubic],actions:[shiftU],q:0};
  const clCubic=closure(sysCubic);
  check('affine_closure_of_the_cubic_response_is_spanned_by_four_protocols',()=>{
    assert.equal(clCubic.basis.length,4);assert.deepEqual(clCubic.basis.map(b=>b.witness.constant?'1':'F'+JSON.stringify(b.witness.word)),['1','F[]','F[0]','F[0,0]']);
    assert(clCubic.increases<=binom(2+3,3)-2);
    for(const f of [one2,u,sq(u),cubic])assert(clCubic.span.coords(pVec(f)));
    assert.equal(clCubic.span.coords(pVec(v)),null);
  });
  const xC=P('2/3','-5/4');
  const futureC=[[0,0,0],[0,0,0,0,0,0,0],Array(11).fill(0)];
  check('descended_matrices_predict_every_recorded_future_reading',()=>{
    const pkt=closurePacket('Every future reading of u^3+v under unit u-shifts',sysCubic,clCubic,xC,futureC),r=decodeClosure(roundTrip(pkt));
    r.predictions.forEach((p,i)=>assert(vector(S.fromJSON(p.predicted)).equals(vector(S.fromJSON(pkt.future_protocols[i].reading)))));
    const coordU=clCubic.span.coords(pVec(u)),uHat=coordU.reduce((acc,c,k)=>sAdd(acc,r.Y[k].map(x=>x.mul(c)),INF),[]);
    assert(sEq(uHat,xC[0]));
    const vHat=sSub(r.Y[1],sMul(sMul(uHat,uHat,INF),uHat,INF),INF);assert(sEq(vHat,xC[1]));
    details.cubic_shift_certificate={...pkt,decoded:{...r,Y:r.Y.map(s=>s.map(String)),u:uHat.map(String),v_by_polynomial_decoder:vHat.map(String)}};
  });
  check('equal_retained_readings_iff_equal_future_readings',()=>{
    const Yof=x=>clCubic.basis.map(b=>pEval(b.f,x,INF));
    const same=(x,z)=>Yof(x).every((s,i)=>sEq(s,Yof(z)[i]));
    const fut=(x,z)=>[0,1,2,3,5,8].every(N=>sEq(pEval(cubic,runWord([shiftU],Array(N).fill(0),x,INF),INF),pEval(cubic,runWord([shiftU],Array(N).fill(0),z,INF),INF)));
    for(const [x,z] of [[xC,xC],[xC,P('2/3',1)],[P(1,2),P(1,2)],[P(0,0),P(1,-1)]])assert.equal(same(x,z),fut(x,z));
  });
  check('passive_square_and_cube_recover_x_without_a_polynomial_decoder',()=>{
    const x=pVar(1,0),gens=[pMul(x,x,INF),pMul(pMul(x,x,INF),x,INF)],sp=new Span();
    const prods=[pConst(1,sc(1))];for(let k=0;k<6;k++)for(const p of prods.slice())for(const g of gens){const r=pMul(p,g,INF);if(pDeg(r)<=12)prods.push(r);}
    prods.forEach(p=>sp.add(pVec(p)));assert.equal(sp.coords(pVec(x)),null);
    for(const a of ['3/2','-2/7',0]){const A=Q(a),uu=A.mul(A),vv=uu.mul(A);assert((uu.zero()?new F(0):vv.div(uu)).eq(A));}
  },true);
  check('a_nonlinear_cut_action_has_no_finite_closure',()=>{
    const x=pVar(1,0);assert.throws(()=>closure({n:1,sensors:[x],actions:[[pMul(x,x,INF)]],q:0,maxStages:6}),/No closure/);
  },true);
  const sysSS={n:2,sensors:[Fuv],actions:[shiftU,swap],q:0},clSS=closure(sysSS);
  check('swap_and_shift_catalogue_closure_recovers_the_state',()=>{
    assert.equal(clSS.basis.length,4);for(const f of [u,v])assert(clSS.span.coords(pVec(f)));
    assert.deepEqual(clSS.basis.map(b=>b.witness.constant?'1':'F'+JSON.stringify(b.witness.word)),['1','F[]','F[0]','F[1,0]']);
  });
  check('shortest_separating_word_for_the_sign_pair_has_length_two',()=>{
    const x=P(3,'2/5'),z=P(3,'-2/5'),diff=b=>!sEq(pEval(b.f,x,INF),pEval(b.f,z,INF));
    const first=clSS.basis.find(diff);assert.deepEqual(first.witness.word,[1,0]);
    assert(!clSS.basis.filter(b=>b.witness.word.length<2).some(diff));
    details.separating_witness={pair:[x.map(s=>s.map(String)),z.map(s=>s.map(String))],word:first.witness.word,meaning:'apply the swap, then the unit shift, then read'};
  });
  check('shift_only_catalogue_cannot_separate_the_sign_pair',()=>{
    const cl=closure({n:2,sensors:[Fuv],actions:[shiftU],q:0}),x=P(3,'2/5'),z=P(3,'-2/5');
    assert(cl.basis.every(b=>sEq(pEval(b.f,x,INF),pEval(b.f,z,INF))));
  },true);
  // -------------------------------------------------- Theorem 3
  check('conjugated_translation_is_translation_by_the_transported_direction',()=>{
    const Am=[[1,2],[0,1]],Ainv=[[1,-2],[0,1]],lin=M=>[0,1].map(i=>pAdd(pScale(u,sc(M[i][0]),INF),pScale(v,sc(M[i][1]),INF),INF));
    const T=h=>[pAdd(u,pConst(2,sc(h[0])),INF),pAdd(v,pConst(2,sc(h[1])),INF)];
    for(const h of [[1,0],['1/2',-3]]){const word=composeMaps(lin(Am),composeMaps(T(h),lin(Ainv),INF),INF),Ah=[Q(h[0]).add(Q(h[1]).mul(2)),Q(h[1])];
      word.forEach((c,i)=>assert(pEq(c,T(Ah)[i])));}
    const JTJ=composeMaps(swap,composeMaps(shiftU,swap,INF),INF);assert(pEq(JTJ[0],u)&&pEq(JTJ[1],pAdd(v,one2,INF)));
  });
  check('synthesized_directions_span_the_sector_within_the_bound',()=>{
    const r=synthesize(2,[[1,0]],[{matrix:[[0,1],[1,0]],inverse:[[0,1],[1,0]]}]);assert.equal(r.dimension,2);assert(r.increases<=2-1);
    const r3=synthesize(3,[[1,0,0]],[{matrix:[[0,0,1],[1,0,0],[0,1,0]],inverse:[[0,1,0],[0,0,1],[1,0,0]]}]);assert.equal(r3.dimension,3);assert(r3.increases<=2);
    details.synthesized_translations=r3.basis.map(b=>({direction:b.h.map(String),word:b.word.word}));
  });
  check('three_catalogue_readings_decode_both_coordinates',()=>{
    const x=P('7/3','-4/5'),pkt={target:'(u,v) from F(x), F(Tx), F(TJx) for F=u^2+v^2',readings:[[],[0],[1,0]].map(w=>({word:w,reading:toState([pEval(Fuv,runWord(sysSS.actions,w,x,INF),INF)]).toJSON()}))};
    const dec=p=>{const [a,b,c]=p.readings.map(r=>fromState(r.reading,1)[0]),h=s=>sSub(sSub(s,a,INF),sc(1),INF).map(y=>y.div(new F(2)));return [h(b),h(c)];};
    const r=dec(roundTrip(pkt));assert(sEq(r[0],x[0])&&sEq(r[1],x[1]));
    const JT=runWord(sysSS.actions,[0,1],x,INF);assert(sEq(pEval(Fuv,JT,INF),sAdd(pEval(Fuv,x,INF),sAdd(sMul(sc(2),x[0],INF),sc(1),INF),INF)));
    details.swap_shift_certificate={...pkt,decoded:r.map(s=>s.map(String))};
  });
  check('an_unavailable_inverse_is_not_used_for_synthesis',()=>{
    assert.throws(()=>synthesize(2,[[1,0]],[{matrix:[[1,0],[1,1]],inverse:null}]),/not available/);
  },true);
  check('full_translation_sufficiency_is_not_necessary',()=>{
    const r=synthesize(2,[[1,0]],[]);assert.equal(r.dimension,1);
    const op=active.buildOp({labels:[0,1],outputs:[0],terms:[{out:0,coeff:vector(W()),powers:{0:3}},{out:0,coeff:vector(W()),powers:{1:1}}]});
    assert.equal(active.kernelBasis(op).length,0);
    assert(clCubic.span.coords(pVec(u)));assert.equal(clCubic.span.coords(pVec(v)),null);
    const x=P('-3/2',4),Yx=clCubic.basis.map(b=>pEval(b.f,x,INF)),uHat=clCubic.span.coords(pVec(u)).reduce((acc,c,k)=>sAdd(acc,Yx[k].map(y=>y.mul(c)),INF),[]);
    assert(sEq(uHat,x[0]));assert(sEq(sSub(Yx[1],sMul(sMul(uHat,uHat,INF),uHat,INF),INF),x[1]));
  });
  // -------------------------------------------------- Theorem 4
  const q2=2,X=pVar(1,0),g=[pAdd(X,pMul(pConst(1,sUnit(1)),pMul(X,X,INF),INF),INF)];
  const Ytuple=[X,pScale(pMul(X,X,INF),sUnit(1),q2),pScale(pMul(pMul(X,X,INF),X,INF),sUnit(2),q2)];
  check('unit_action_has_the_stated_exact_response_matrix',()=>{
    const M=[[1,1,0],[0,1,2],[0,0,1]];
    Ytuple.forEach((y,i)=>assert(pEq(pCompose(y,g,q2),Ytuple.reduce((acc,z,k)=>pAdd(acc,pScale(z,sc(M[i][k]),q2),q2),new Map()))));
  });
  const sysU={n:1,sensors:[X],actions:[g],q:q2},clU=closure(sysU);
  check('nonlinear_unit_closure_is_finite_within_the_degree_bound',()=>{
    const Nb=[0,1,2].reduce((a,r)=>a+binom(1+1+r,1+r),0);assert.equal(Nb,9);
    assert(clU.span.size<=Nb);assert(clU.increases<=Nb-clU.stages[0]);
    for(const b of clU.basis)for(const [k,s]of b.f)s.forEach((c,d)=>{if(!c.zero())assert(expOf(k)[0]<=1+d);});
    for(const y of Ytuple)assert(clU.span.coords(pVec(y)));
  });
  check('degree_versus_unit_bound_is_preserved_by_affine_cut_actions',()=>{
    const n=2,d=2,q=2,b=3,a=pVar(n,0),c=pVar(n,1),L=s=>pConst(n,sUnit(s));
    const gg=[pAdd(pAdd(pScale(a,sc(2),INF),pAdd(c,pConst(n,sc(1)),INF),INF),pMul(L(1),pMul(a,pMul(c,c,INF),INF),INF),q),
              pAdd(pSub(c,pConst(n,sc(3)),INF),pMul(L(2),pMul(a,pMul(a,a,INF),INF),INF),q)];
    for(let r=0;r<=q;r++)for(let i=0;i<=d+r*(b-1);i++)for(let j=0;i+j<=d+r*(b-1);j++){
      const e=[i,j],mono=pNorm(new Map([[keyOf(e),sUnit(r)]]),q),img=pCompose(mono,gg,q);
      for(const [k,s]of img)s.forEach((x,t)=>{if(!x.zero())assert(expOf(k).reduce((p,y)=>p+y,0)<=d+t*(b-1));});
    }
  });
  const xU=[sc('2/3',-1,'1/5')];
  check('three_protocol_readings_predict_every_iterate_at_the_cut',()=>{
    const fut=[3,4,7,12].map(N=>Array(N).fill(0)),pkt=closurePacket('Every future reading of F=x under g=x+Lambda x^2 through Lambda^2',sysU,clU,xU,fut),r=decodeClosure(roundTrip(pkt));
    r.predictions.forEach((p,i)=>assert(vector(S.fromJSON(p.predicted)).equals(vector(S.fromJSON(pkt.future_protocols[i].reading)))));
    const read=N=>pEval(X,runWord([g],Array(N).fill(0),xU,q2),q2);
    const [r0,r1,r2]=[0,1,2].map(read),Y=[r0,sSub(r1,r0,q2),sSub(sSub(r2,sMul(sc(2),r1,q2),q2),sMul(sc(-1),r0,q2),q2).map(y=>y.div(new F(2)))];
    Ytuple.forEach((y,i)=>assert(sEq(Y[i],pEval(y,xU,q2))));
    details.unit_action_certificate={...pkt,decoded:{...r,Y:r.Y.map(s=>s.map(String))},stated_protocol_coordinates:Y.map(s=>s.map(String))};
  });
  check('iterate_formula_holds_modulo_the_declared_cut',()=>{
    let gN=[X];const Lx2=pScale(pMul(X,X,INF),sUnit(1),q2),Lx3=pScale(pMul(pMul(X,X,INF),X,INF),sUnit(2),q2);
    for(let N=0;N<=12;N++){const want=pAdd(pAdd(X,pScale(Lx2,sc(N),q2),q2),pScale(Lx3,sc(N*(N-1)),q2),q2);assert(pEq(gN[0],want));gN=composeMaps(gN,g,q2);}
  });
  check('the_iterate_formula_is_not_an_identity_before_the_cut',()=>{
    const g2=composeMaps(composeMaps([X],g,INF),g,INF)[0],want=pAdd(pAdd(X,pScale(pMul(X,X,INF),sUnit(1,2),INF),INF),pScale(pMul(pMul(X,X,INF),X,INF),sUnit(2,2),INF),INF);
    assert(!pEq(g2,want));assert(pEq(pNorm(g2,q2),pNorm(want,q2)));
  },true);
  check('a_later_unit_reading_separates_the_sign_branch',()=>{
    const Fx2=pMul(X,X,INF),dec=p=>{const [a,b]=p.readings.map(r=>fromState(r.reading,1)[0]),a2=a[0]||new F(0),l=b[1]||new F(0);return a2.zero()?new F(0):l.div(a2.mul(new F(2)));};
    for(const a of ['3/2','-3/2',0,'-2/7']){
      const pkt={target:'Constant rational input a from F=x^2 and F(g a)',readings:[[],[0]].map(w=>({word:w,reading:toState([pEval(Fx2,runWord([g],w,[sc(a)],q2),q2)]).toJSON()}))};
      assert(dec(roundTrip(pkt)).eq(Q(a)));
      if(a==='-3/2')details.sign_branch_certificate={...pkt,decoded:dec(pkt).toString()};
    }
  });
  check('the_initial_sensor_alone_misses_the_sign',()=>{
    const Fx2=pMul(X,X,INF);assert(sEq(pEval(Fx2,[sc('3/2')],q2),pEval(Fx2,[sc('-3/2')],q2)));
  },true);
  // -------------------------------------------------- Section 6
  check('moving_and_held_calibration_updates_are_exact',()=>{
    for(const [cl,sys,x,c] of [[clSS,sysSS,P('7/3','-4/5'),P(1,'1/2')],[clU,sysU,xU,[sc(-1,'1/3')]]]){
      const q=sys.q===0?INF:sys.q,Y=pt=>cl.basis.map(b=>pEval(b.f,pt,q)),O=(a,b)=>Y(a).map((s,i)=>sSub(s,Y(b)[i],q));
      cl.matrices.forEach((M,i)=>{const gx=actOn(sys.actions[i],x,q),gc=actOn(sys.actions[i],c,q),apply=y=>M.map(row=>row.reduce((acc,m,k)=>m.zero()?acc:sAdd(acc,y[k].map(z=>z.mul(m)),q),[]));
        const moving=apply(O(x,c));O(gx,gc).forEach((s,k)=>assert(sEq(s,moving[k])));
        const held=apply(O(x,c)).map((s,k)=>sAdd(s,sSub(Y(gc)[k],Y(c)[k],q),q));O(gx,c).forEach((s,k)=>assert(sEq(s,held[k])));});
    }
  });
  check('dropping_the_held_calibration_correction_misreads',()=>{
    const x=P('7/3','-4/5'),c=P(1,'1/2'),Y=pt=>clSS.basis.map(b=>pEval(b.f,pt,INF)),M=clSS.matrices[0];
    const gx=actOn(shiftU,x,INF),O=Y(x).map((s,i)=>sSub(s,Y(c)[i],INF)),apply=M.map(row=>row.reduce((acc,m,k)=>m.zero()?acc:sAdd(acc,O[k].map(z=>z.mul(m)),INF),[]));
    assert(!Y(gx).map((s,i)=>sSub(s,Y(c)[i],INF)).every((s,k)=>sEq(s,apply[k])));
  },true);
  check('response_basis_change_transports_the_update',()=>{
    const Sm=[[1,1,0],[0,2,0],[1,0,1]].map(r=>r.map(Q)),Si=invQ(Sm);
    const Mt=[[1,1,0],[0,1,2],[0,0,1]].map(r=>r.map(Q)),mm=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((z,x,k)=>z.add(x.mul(B[k][j])),new F(0))));
    const Mnew=mm(mm(Sm,Mt),Si),Yn=pt=>Sm.map(r=>r.reduce((acc,c,k)=>c.zero()?acc:sAdd(acc,pEval(Ytuple[k],pt,q2).map(z=>z.mul(c)),q2),[]));
    const gx=actOn(g,xU,q2),lhs=Yn(gx),rhs=Mnew.map(r=>r.reduce((acc,c,k)=>c.zero()?acc:sAdd(acc,Yn(xU)[k].map(z=>z.mul(c)),q2),[]));
    lhs.forEach((s,i)=>assert(sEq(s,rhs[i])));
  });
  check('every_archived_certificate_redecodes_from_its_saved_readings',()=>{
    const arc=roundTrip(details);
    for(const k of ['cubic_shift_certificate','unit_action_certificate']){const r=decodeClosure(arc[k]);r.predictions.forEach((p,i)=>assert.deepEqual(p.predicted,arc[k].decoded.predictions[i].predicted));}
    const J=decodeSignature(arc.restricted_signature_certificate,1),uHat=sAdd(c2[0],J.get('1')[0].map(x=>x.div(new F(2))),INF);
    assert.deepEqual(uHat.map(String),arc.restricted_signature_certificate.decoded.u);
    const sw=arc.swap_shift_certificate,[a0,b0,c0]=sw.readings.map(r=>fromState(r.reading,1)[0]),h=t=>sSub(sSub(t,a0,INF),sc(1),INF).map(y=>y.div(new F(2)));
    assert.deepEqual([h(b0),h(c0)].map(t=>t.map(String)),sw.decoded);
    const sb=arc.sign_branch_certificate,[ra,rb]=sb.readings.map(r=>fromState(r.reading,1)[0]);assert.equal(rb[1].div(ra[0].mul(new F(2))).toString(),sb.decoded);
  });
  return {schema:'rkf.lambda-action-closure.v1',date:'2026-10-12',status:'PASS_RESTRICTED_PROBES_AND_ACTION_CLOSURE',
    theorem_count:4,proposition_count:2,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting sectors over Q and retained unit quotients Q[Lambda]/(Lambda^(q+1))',source:'Supplied sensors, supplied action catalogue and recorded protocol readings',
      zero:'Typed cut operation; additive neutrals retain their separate types',primitive_metric:false,unavailable_action_added:false,numerical_unit_value_assumed:false,RH_development:false,curvature_developed:false},
    finite_ranges:{restricted_probe_grid:'{0,1}^1 and {0,1,2}^2',affine_closure_dimensions:[4,4],unit_depth:q2,unit_closure_bound:9,future_words_through_length:12},
    details,evidence:{general_results:'Four written derivations, a separating-word corollary and the moving-observer identities',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['closure for actions with nonlinear cut','one finite observer for the full infinite unit tower','a minimum nonlinear observer','enumeration of arbitrary nonlinear fibres or a global experimental budget',
      'availability of an inverse that is not in the catalogue','noisy-data recovery','new RH or curvature result','novelty priority for pullbacks, invariant-span closure or conjugated translations']};
}
module.exports={sc,sAdd,sSub,sMul,sEq,sUnit,sNeg,sInv,INF,pConst,pVar,pAdd,pSub,pScale,pMul,pEq,pDeg,pCompose,pEval,pNorm,pVec,actOn,composeMaps,runWord,Span,closure,closurePacket,decodeClosure,toState,fromState,binom,invQ,keyOf,expOf,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE36_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}
