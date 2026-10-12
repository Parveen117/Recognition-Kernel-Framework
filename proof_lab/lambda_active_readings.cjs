'use strict';
// SE35 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const joint=require('./lambda_joint_readings.cjs');
const {F}=o,S=previous.presentation,{vector}=count,{coordinates,jointAction,jointBank,bankReader}=joint;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_ACTIVE_READINGS_RESULT.json');
const W=(n=0,d=0,c=1)=>S.word([...Array(d).fill('L'),...Array(n).fill('X')],c);
const Lam=W(0,1),nil=()=>S.zero();
const ix=w=>w.filter(t=>t==='X').length,ud=w=>w.filter(t=>t==='L').length;
const sum=xs=>vector(xs.reduce((a,b)=>a.plus(b),nil()));
const cut=(a,q)=>vector(previous.memory(vector(a),q));
const fact=n=>{let r=1n;for(let k=2;k<=n;k++)r*=BigInt(k);return r;};
const zeroF=()=>new F(0);
function cartesian(sets){return sets.reduce((rows,set)=>rows.flatMap(row=>set.map(x=>[...row,x])),[[]]);}
const coordOf=(v,n)=>new Map(coordinates(vector(v))).get(n)||nil();
// ---- states as coordinate vectors over Q[Lambda] ----
function svec(state,labels){
  const m=new Map(coordinates(vector(state)));
  for(const n of m.keys())if(!labels.includes(n))throw new RangeError('State outside the declared sector: '+n);
  return labels.map(n=>m.get(n)||nil());
}
const fromS=(vec,labels)=>sum(vec.map((s,i)=>vector(s).times(W(labels[i]))));
function qscalar(s){let r=zeroF();for(const [w,c]of vector(s).entries()){if(ud(w)||ix(w))throw new TypeError('Rational scalar required');r=r.add(c.rad);}return r;}
const pt=(labels,vals)=>sum(labels.map((n,i)=>W(n,0,String(vals[i]))));
const lin=(row,vec)=>vector(row.reduce((acc,w,j)=>w.zero()?acc:acc.plus(vector(vec[j]).scale(w)),nil()));
const matS=(M,vec)=>M.map(r=>lin(r,vec));
// ---- exact rational linear algebra on the canonical fractions ----
const transpose=m=>m.length?m[0].map((_,j)=>m.map(r=>r[j])):[];
function rrefQ(rows,ncols){
  const a=rows.map(r=>r.slice()),pivots=[];let p=0;
  for(let j=0;j<ncols&&p<a.length;j++){
    let k=-1;for(let i=p;i<a.length;i++)if(!a[i][j].zero()){k=i;break;}
    if(k<0)continue;[a[p],a[k]]=[a[k],a[p]];
    const d=a[p][j];a[p]=a[p].map(x=>x.div(d));
    for(let i=0;i<a.length;i++)if(i!==p&&!a[i][j].zero()){const f=a[i][j];a[i]=a[i].map((x,t)=>x.sub(f.mul(a[p][t])));}
    pivots.push(j);p++;
  }
  return {a:a.slice(0,p),pivots};
}
const rankQ=(rows,ncols)=>rows.length?rrefQ(rows,ncols).pivots.length:0;
function nullspaceQ(rows,ncols){
  const {a,pivots}=rrefQ(rows,ncols),free=[...Array(ncols).keys()].filter(j=>!pivots.includes(j));
  return free.map(f=>{const v=Array.from({length:ncols},zeroF);v[f]=new F(1);pivots.forEach((pj,i)=>{v[pj]=a[i][f].neg();});return v;});
}
function invQ(M){
  const n=M.length,aug=M.map((r,i)=>[...r,...Array.from({length:n},(_,j)=>new F(i===j?1:0))]);
  const {a,pivots}=rrefQ(aug,2*n);
  if(pivots.length<n||pivots.slice(0,n).some((p,i)=>p!==i))throw new RangeError('Singular matrix');
  return a.map(r=>r.slice(n));
}
const mulQ=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((z,x,k)=>z.add(x.mul(B[k][j])),zeroF())));
const mvQ=(A,v)=>A.map(r=>r.reduce((z,x,k)=>z.add(x.mul(v[k])),zeroF()));
const qvec=(state,labels)=>svec(state,labels).map(qscalar);
const qstate=(v,labels)=>sum(labels.map((n,i)=>W(n,0,String(v[i]))));
// A matrix S with L S z = z for every z in the image of L.
function sectionMatrix(L,n){
  const R=L.length,{pivots:J}=rrefQ(L,n),S0=Array.from({length:n},()=>Array.from({length:R},zeroF));
  if(!J.length)return S0;
  const LJ=L.map(r=>J.map(j=>r[j])),I=rrefQ(transpose(LJ),R).pivots,Minv=invQ(I.map(i=>LJ[i]));
  J.forEach((j,t)=>I.forEach((i,s)=>{S0[j][i]=Minv[t][s];}));
  return S0;
}
// ---- polynomial operations given by symmetric joint banks ----
// terms: coefficient (a scalar state), output label, exponents of input labels.
function buildOp({labels,outputs,constant=nil(),terms}){
  const L=[...labels].sort((a,b)=>a-b),tdeg=t=>Object.values(t.powers).reduce((a,b)=>a+b,0);
  const deg=Math.max(1,...terms.map(tdeg)),kernels=[];
  for(let r=1;r<=deg;r++){
    const own=terms.filter(t=>tdeg(t)===r);
    const read=tuple=>{
      const key=[...tuple].sort((a,b)=>a-b).join(',');let out=nil();
      for(const t of own){
        const ms=Object.entries(t.powers).flatMap(([lab,e])=>Array(e).fill(Number(lab))).sort((a,b)=>a-b).join(',');
        if(ms!==key)continue;
        const alpha=Object.values(t.powers).reduce((a,e)=>a*fact(e),1n);
        out=out.plus(vector(t.coeff).times(W(t.out)).scale(new F(alpha,fact(r))));
      }
      return vector(out);
    };
    kernels.push({arity:r,readings:jointBank(read,cartesian(Array(r).fill(L)))});
  }
  return {input_labels:L,output_labels:[...outputs].sort((a,b)=>a-b),degree:deg,constant:vector(constant).toJSON(),kernels};
}
const T=(out,coeff,powers)=>({out,coeff:vector(coeff),powers});
const readerCache=new WeakMap();
function kernelReader(op,r){
  const k=op.kernels.find(x=>x.arity===r);if(!k)throw new RangeError('Missing kernel of arity '+r);
  if(!readerCache.has(k))readerCache.set(k,bankReader(k.readings,r));
  return readerCache.get(k);
}
function requireSymmetric(op){
  for(const k of op.kernels){
    const read=kernelReader(op,k.arity);
    for(const row of k.readings){const sorted=[...row.inputs].sort((a,b)=>a-b);if(!read(row.inputs).equals(read(sorted)))throw new TypeError('Symmetric kernel components required');}
  }
}
function applyOp(op,x){
  let out=vector(S.fromJSON(op.constant));
  for(const k of op.kernels)out=vector(out.plus(jointAction(kernelReader(op,k.arity),Array(k.arity).fill(vector(x)))));
  return out;
}
// Linear contraction bank L_r of (SE35.4): rows (tuple,output), columns input labels.
function contraction(op,r){
  const L=op.input_labels,tuples=cartesian(Array(r-1).fill(L)),read=kernelReader(op,r),rows=[];
  for(const tup of tuples)for(const j of op.output_labels)rows.push(L.map(v=>qscalar(coordOf(read([v,...tup]),j))));
  return {rows,tuples};
}
const stackRows=(op,from,to)=>Array.from({length:to-from+1},(_,i)=>contraction(op,from+i).rows).flat();
const kernelBasis=op=>nullspaceQ(stackRows(op,1,op.degree),op.input_labels.length);
const inKernel=(op,v)=>mvQ(stackRows(op,1,op.degree),v).every(x=>x.zero());
// ---- active observation protocol ----
const probeGrid=(labels,D)=>cartesian(Array(labels.length).fill(Array.from({length:D},(_,i)=>i)));
const hState=(t,labels)=>sum(labels.map((n,i)=>W(n,0,t[i])));
const activeReading=(op,c,x,h)=>vector(applyOp(op,vector(x.plus(h))).minus(applyOp(op,vector(c.plus(h)))));
function activePacket(op,decoderOp,c,x,D){
  const labels=decoderOp.input_labels;
  return {target:'Recovery of the input modulo the translation-blind subspace from translated readings F(x+h)-F(c+h)',
    declared_degree:D,calibration:vector(c).toJSON(),decoder_operation:decoderOp,
    readings:probeGrid(labels,D).map(t=>({h:t,response:activeReading(op,c,x,hState(t,labels)).toJSON()}))};
}
function interpolate(table,n,D){
  const V=Array.from({length:D},(_,i)=>Array.from({length:D},(_,j)=>new F(i).pow(j))),Vinv=invQ(V),keys=probeGrid(Array(n).fill(0),D);
  let cur=table;
  for(let axis=0;axis<n;axis++){
    const next=new Map();
    for(const key of keys){
      let acc=nil();
      for(let i=0;i<D;i++){const k2=key.slice();k2[axis]=i;acc=acc.plus(cur.get(k2.join(',')).scale(Vinv[key[axis]][i]));}
      next.set(key.join(','),vector(acc));
    }
    cur=next;
  }
  return cur;
}
function responseTable(packet){
  const op=packet.decoder_operation,labels=op.input_labels,D=packet.declared_degree,table=new Map();
  if(!Number.isSafeInteger(D)||D<op.degree)throw new RangeError('Declared degree must cover the decoder operation');
  for(const row of packet.readings){const key=row.h.join(',');if(table.has(key))throw new TypeError('Duplicate active reading');table.set(key,vector(S.fromJSON(row.response)));}
  for(const t of probeGrid(labels,D))if(!table.has(t.join(',')))throw new RangeError('Unread active probe '+t.join(','));
  return table;
}
// Descending decoder of (SE35.9)-(SE35.12).
function decodeActive(packet){
  const op=packet.decoder_operation,labels=op.input_labels,n=labels.length,D=packet.declared_degree,d=op.degree;
  requireSymmetric(op);
  const c=vector(S.fromJSON(packet.calibration)),coef=interpolate(responseTable(packet),n,D);
  const mixed=tup=>{
    const alpha=Array(n).fill(0);tup.forEach(v=>{alpha[labels.indexOf(v)]++;});
    return vector(coef.get(alpha.join(',')).scale(new F(alpha.reduce((a,e)=>a*fact(e),1n))));
  };
  const banks=new Map();
  for(let r=d;r>=1;r--){
    let a=c;
    if(r<d){
      const vals=[];for(let k=r+1;k<=d;k++)vals.push(...banks.get(k).values);
      a=vector(c.plus(fromS(matS(sectionMatrix(stackRows(op,r+1,d),n),vals),labels)));
    }
    const {tuples}=contraction(op,r),values=[];
    for(const tup of tuples){
      let bracket=mixed(tup);
      for(let k=r+1;k<=d;k++){
        const rk=kernelReader(op,k),m=k-r+1,slots=tup.map(v=>W(v));
        const ta=jointAction(rk,[...Array(m).fill(a),...slots]),tc=jointAction(rk,[...Array(m).fill(c),...slots]);
        bracket=vector(bracket.minus(vector(ta.minus(tc)).scale(new F(fact(k),fact(k-r+1)))));
      }
      const state=vector(bracket.scale(new F(1n,fact(r))));
      for(const j of op.output_labels)values.push(coordOf(state,j));
    }
    banks.set(r,{tuples,values});
  }
  const all=[];for(let r=1;r<=d;r++)all.push(...banks.get(r).values);
  const x_hat=vector(c.plus(fromS(matS(sectionMatrix(stackRows(op,1,d),n),all),labels)));
  return {x_hat,kernel_dimension:n-rankQ(stackRows(op,1,d),n),banks:[...banks].map(([r,b])=>({order:r,values:b.values.map(v=>v.toJSON())}))};
}
// Four observer readings for the square response (SE35.22).
function squarePacket(op,c,x,probes){
  const f=a=>applyOp(op,a);
  return {target:'Displacement x-c from translated square readings',calibration:vector(c).toJSON(),
    probes:probes.map(hv=>{const h=W(0,0,String(hv)),m=W(0,0,String(new F(hv).neg()));
      return {h:String(hv),readings:{x_plus_h:f(vector(x.plus(h))).toJSON(),x_minus_h:f(vector(x.plus(m))).toJSON(),
        c_plus_h:f(vector(c.plus(h))).toJSON(),c_minus_h:f(vector(c.plus(m))).toJSON()}};})};
}
function decodeSquare(packet){
  if(!packet.probes.length)throw new RangeError('At least one probe reading required');
  const out=packet.probes.map(p=>{
    const h=new F(p.h);if(h.zero())throw new RangeError('Nonzero probe required');
    const g=k=>vector(S.fromJSON(p.readings[k]));
    return vector(vector(g('x_plus_h').minus(g('x_minus_h')).minus(g('c_plus_h')).plus(g('c_minus_h'))).scale(new F(1).div(h.mul(4))));
  });
  for(const v of out)if(!v.equals(out[0]))throw new TypeError('Probe readings disagree');
  return out[0];
}
// Completed observation Z=D_0(C_Lambda(.)) and its unit-memory inverse (SE35.19)-(SE35.21).
const completed=(op,decoderOp,c,D,x)=>decodeActive(activePacket(op,decoderOp,c,x,D)).x_hat;
function decodeLifted(packet){
  const q=packet.unit_memory_through,c=vector(S.fromJSON(packet.observation.calibration)),D=packet.observation.declared_degree;
  const dec=packet.observation.decoder_operation,z=decodeActive(packet.observation).x_hat;
  let x=cut(z,q);const trace=[x.toJSON()];
  for(let k=0;k<q;k++){
    const Zx=completed(packet.operation,dec,c,D,x);
    x=cut(vector(z.minus(vector(Zx.minus(x)))),q);trace.push(x.toJSON());
  }
  return {observed_completion:z.toJSON(),state:x.toJSON(),updates:trace};
}
// ---- target recovery and repair channels (SE35.15)-(SE35.16) ----
const kernelMatrix=(K,n)=>K.length?transpose(K):Array.from({length:n},()=>[]);
function targetRank(A,K,n){if(!K.length)return 0;return rankQ(A.map(r=>K.map(k=>r.reduce((z,x,j)=>z.add(x.mul(k[j])),zeroF()))),K.length);}
function repairChannels(A,K,n){
  if(!K.length)return [];
  const AK=A.map(r=>K.map(k=>r.reduce((z,x,j)=>z.add(x.mul(k[j])),zeroF()))),pivots=rrefQ(AK,K.length).pivots;
  if(!pivots.length)return [];
  const M=transpose(pivots.map(i=>K[i])),Mt=transpose(M);// n x b
  return mulQ(invQ(mulQ(Mt,M)),Mt);                      // b x n left inverse of the chosen kernel directions
}
function augment(op,B){
  const first=Math.max(...op.output_labels)+1,labels=B.map((_,t)=>first+t),copy=JSON.parse(JSON.stringify(op));
  copy.output_labels=[...op.output_labels,...labels];
  const k1=copy.kernels.find(k=>k.arity===1);
  for(const row of k1.readings){
    const v=op.input_labels.indexOf(row.inputs[0]);
    row.response=vector(S.fromJSON(row.response).plus(sum(B.map((b,t)=>W(labels[t],0,String(b[v])))))).toJSON();
  }
  return copy;
}
function transportOp(op,U,V){
  const L=op.input_labels,out=op.output_labels,Uinv=invQ(U),cols=a=>qstate(Uinv.map(r=>r[a]),L);
  const mapOut=y=>fromS(matS(V,svec(y,out)),out);
  const copy=JSON.parse(JSON.stringify(op));
  copy.constant=vector(mapOut(S.fromJSON(op.constant))).toJSON();
  for(const k of copy.kernels){
    const read=kernelReader(op,k.arity);
    for(const row of k.readings)row.response=mapOut(jointAction(read,row.inputs.map(v=>cols(L.indexOf(v))))).toJSON();
  }
  return copy;
}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE33_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const roundTrip=x=>JSON.parse(JSON.stringify(x));
  const eqState=(a,b)=>vector(a).equals(vector(b));
  // Declared operations.
  const one=W(0,0,1),opCubicLinear=buildOp({labels:[0,1],outputs:[0],terms:[T(0,one,{0:3}),T(0,one,{1:1})]});
  const opSquare=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:2})]});
  const opUOnly=buildOp({labels:[0,1],outputs:[0],terms:[T(0,one,{0:2})]});
  const opMatching=buildOp({labels:[0,1,2],outputs:[0,1,2],terms:[0,1,2].map(a=>T(a,one,{[a]:2}))});
  const opMixed=buildOp({labels:[0,1,2],outputs:[0,1],terms:[T(0,one,{0:2}),T(0,W(0,0,2),{0:1,2:1}),T(0,one,{2:2}),T(0,one,{1:3}),T(1,one,{0:1,1:1}),T(1,one,{1:1,2:1})]});
  const opSquareDeformed=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:2}),T(0,Lam,{0:3})]});
  const opSquareCut=buildOp({labels:[0],outputs:[0],terms:[T(0,one,{0:2})]});
  const opPairDeformed=buildOp({labels:[0,1],outputs:[0,1],terms:[T(0,one,{0:2}),T(0,Lam,{0:3}),T(1,one,{1:1})]});
  const opPairCut=buildOp({labels:[0,1],outputs:[0,1],terms:[T(0,one,{0:2}),T(1,one,{1:1})]});
  const opLayered=buildOp({labels:[0,1],outputs:[0],terms:[T(0,one,{0:2}),T(0,Lam,{1:1})]});
  const lab2=[0,1],lab3=[0,1,2];
  const xc3=pt(lab3,['2/3',-1,'1/2']),cc3=pt(lab3,['1/5',3,-2]),kdir=[new F(1),new F(0),new F(-1)];
  // ------------------------------------------------------------ Theorem 1
  check('symmetric_components_are_built_from_the_declared_polynomial_and_agree_with_it',()=>{
    for(const op of [opCubicLinear,opSquare,opUOnly,opMatching,opMixed])requireSymmetric(op);
    const [a,b,c]=['2/3',-1,'1/2'].map(x=>new F(x)),sq=x=>x.mul(x);
    const direct=[sq(a.add(c)).add(b.mul(b).mul(b)),a.add(c).mul(b)],got=applyOp(opMixed,xc3);
    assert(got.equals(pt([0,1],direct.map(String))));
    assert.equal(opMixed.degree,3);
  });
  check('unsymmetric_bank_is_rejected_as_a_symmetric_component',()=>{
    const two=roundTrip(opMixed),k=two.kernels.find(x=>x.arity===2),r01=k.readings.find(x=>x.inputs[0]===0&&x.inputs[1]===1);
    r01.response=vector(S.fromJSON(r01.response).plus(W(0,0,1))).toJSON();
    assert.throws(()=>requireSymmetric(two),/Symmetric/);
    assert.throws(()=>decodeActive(activePacket(opMixed,two,xc3,xc3,3)),/Symmetric/);
  },true);
  check('ordered_kernel_antisymmetric_part_is_invisible_to_the_symmetric_components',()=>{
    const ordered=([i,j])=>vector(W(0,0,i+j).plus(W(0,0,i-j))),sym=tuple=>vector(ordered(tuple).plus(ordered([tuple[1],tuple[0]])).scale('1/2'));
    const u=sum([W(1),W(2,0,3)]);
    const diag=read=>jointAction(read,[u,u]);
    assert(diag(ordered).equals(diag(sym)));
    assert(!ordered([1,2]).equals(sym([1,2])));
  },true);
  const Kmixed=kernelBasis(opMixed);
  check('blind_subspace_of_the_mixed_response_is_the_stated_line',()=>{
    assert.equal(Kmixed.length,1);
    const v=Kmixed[0],t=v[0];assert(!t.zero());
    kdir.forEach((x,i)=>assert(v[i].eq(x.mul(t))));
    assert(inKernel(opMixed,kdir));
    assert(!inKernel(opMixed,[new F(0),new F(1),new F(0)]));
    assert.equal(kernelBasis(opCubicLinear).length,0);assert.equal(kernelBasis(opSquare).length,0);
    assert.equal(kernelBasis(opUOnly).length,1);
  });
  check('translation_invariance_along_the_blind_line_and_not_off_it',()=>{
    const u=pt(lab3,['3/7',2,-1]),vdir=pt(lab3,[1,0,-1]);
    for(const t of ['-3','1/3',5])assert(applyOp(opMixed,vector(u.plus(vdir.scale(t)))).equals(applyOp(opMixed,u)));
    const off=pt(lab3,[0,1,0]);assert(!applyOp(opMixed,vector(u.plus(off))).equals(applyOp(opMixed,u)));
  });
  const mixedPacket=activePacket(opMixed,opMixed,cc3,xc3,3);
  check('complete_active_banks_have_exactly_the_cosets_of_the_blind_subspace_as_fibres',()=>{
    assert.equal(mixedPacket.readings.length,3**3);
    const bankOf=x=>JSON.stringify(activePacket(opMixed,opMixed,cc3,x,3).readings);
    const base=bankOf(xc3);
    for(const t of ['-2','1/2',4])assert.equal(bankOf(vector(xc3.plus(pt(lab3,[t,0,String(new F(t).neg())])))),base);
    for(const dv of [[0,1,0],[1,0,0],[0,0,1],['1/3','1/2',-1]])assert.notEqual(bankOf(vector(xc3.plus(pt(lab3,dv)))),base);
  });
  check('equal_translated_readings_iff_difference_lies_in_the_blind_subspace',()=>{
    const pairs=[[[2,1,3],[3,1,2]],[['1/2',0,'1/3'],['-1/2',0,'4/3']],[[1,1,1],[1,2,1]],[[0,0,0],[1,0,0]],[[2,2,2],[2,2,2]]];
    for(const [x,z] of pairs){
      const a=activePacket(opMixed,opMixed,cc3,pt(lab3,x),3),b=activePacket(opMixed,opMixed,cc3,pt(lab3,z),3);
      const diff=x.map((v,i)=>new F(v).sub(new F(z[i]))),same=JSON.stringify(a.readings)===JSON.stringify(b.readings);
      assert.equal(same,inKernel(opMixed,diff));
    }
  });
  check('raw_square_fibre_is_larger_than_the_active_fibre',()=>{
    const x=pt([0],['3/2']),y=pt([0],['-3/2']);
    assert(applyOp(opSquare,x).equals(applyOp(opSquare,y)));
    const c=pt([0],[1]);
    assert.notEqual(JSON.stringify(activePacket(opSquare,opSquare,c,x,2).readings),JSON.stringify(activePacket(opSquare,opSquare,c,y,2).readings));
  },true);
  check('calibration_change_adds_only_the_known_exact_term',()=>{
    const c2=pt(lab3,[-3,'1/4',2]);
    for(const t of [[0,0,0],[1,2,0],['1/2',-1,3]]){
      const h=pt(lab3,t),lhs=activeReading(opMixed,c2,xc3,h),rhs=vector(activeReading(opMixed,cc3,xc3,h).plus(applyOp(opMixed,vector(cc3.plus(h)))).minus(applyOp(opMixed,vector(c2.plus(h)))));
      assert(lhs.equals(rhs));
    }
    assert.equal(kernelBasis(opMixed).length,1);
  });
  check('finite_grid_interpolates_the_translated_response_polynomial_off_grid',()=>{
    const table=responseTable(mixedPacket),coef=interpolate(table,3,3),h=['3/2','-1','1/3'].map(x=>new F(x));
    let predicted=nil();
    for(const key of probeGrid(lab3,3)){
      let w=new F(1);key.forEach((e,i)=>{w=w.mul(h[i].pow(e));});
      predicted=predicted.plus(coef.get(key.join(',')).scale(w));
    }
    assert(vector(predicted).equals(activeReading(opMixed,cc3,xc3,pt(lab3,h.map(String)))));
    const over=activePacket(opMixed,opMixed,cc3,xc3,4);assert.equal(over.readings.length,4**3);
    assert(decodeActive(over).x_hat.equals(decodeActive(mixedPacket).x_hat));
  });
  check('understated_degree_bound_misreads_the_response',()=>{
    const under=activePacket(opMixed,opMixed,cc3,xc3,2);
    assert.throws(()=>decodeActive(under),/cover/);
    const cubicOnly=activePacket(opCubicLinear,opCubicLinear,pt(lab2,[0,0]),pt(lab2,[1,2]),2);
    const table=responseTable({...cubicOnly,decoder_operation:{...opCubicLinear,degree:2}}),coef=interpolate(table,2,2);
    const h=pt(lab2,[2,0]),direct=activeReading(opCubicLinear,pt(lab2,[0,0]),pt(lab2,[1,2]),h);
    let predicted=nil();for(const key of probeGrid(lab2,2)){let w=new F(1);key.forEach((e,i)=>{w=w.mul(new F([2,0][i]).pow(e));});predicted=predicted.plus(coef.get(key.join(',')).scale(w));}
    assert(!vector(predicted).equals(direct));
  },true);
  // ------------------------------------------------------------ Theorem 2
  const cubicC=pt(lab2,['1/3',-2]),cubicX=pt(lab2,['5/4','7/3']),cubicPacket=activePacket(opCubicLinear,opCubicLinear,cubicC,cubicX,3);
  check('descending_decoder_recovers_the_cubic_plus_linear_input_exactly',()=>{
    const r=decodeActive(roundTrip(cubicPacket));assert.equal(r.kernel_dimension,0);assert(r.x_hat.equals(cubicX));
    for(const c of [pt(lab2,[0,0]),pt(lab2,[-5,'3/2'])]){assert(decodeActive(activePacket(opCubicLinear,opCubicLinear,c,cubicX,3)).x_hat.equals(cubicX));}
    details.cubic_plus_linear_certificate={...cubicPacket,decoded:{state:decodeActive(cubicPacket).x_hat.toJSON(),blind_subspace_dimension:0}};
  });
  check('second_difference_reads_u_and_the_residual_reads_v',()=>{
    for(const [u,v] of [['5/4','7/3'],[0,1],[-2,'1/2']]){
      const f=(a,b)=>applyOp(opCubicLinear,pt(lab2,[a,b])),U=new F(u);
      const second=vector(f(U.add(1),v).minus(f(u,v).scale(2)).plus(f(U.sub(1),v)));
      assert(second.equals(W(0,0,String(U.mul(6)))));
      assert(vector(f(u,v).minus(W(0,0,String(U.pow(3))))).equals(W(0,0,String(new F(v)))));
    }
  });
  check('highest_order_contraction_alone_cannot_separate_the_linear_coordinate',()=>{
    const top=contraction(opCubicLinear,3).rows,nul=nullspaceQ(top,2);
    assert.equal(nul.length,1);assert(nul[0][0].zero()&&!nul[0][1].zero());
    assert.equal(rankQ(stackRows(opCubicLinear,1,3),2),2);
  },true);
  check('decoder_consumes_only_the_serialized_readings',()=>{
    const a=decodeActive(roundTrip(mixedPacket)),b=decodeActive(mixedPacket);assert(a.x_hat.equals(b.x_hat));
    const mutated=roundTrip(mixedPacket);mutated.readings[0].response=vector(S.fromJSON(mutated.readings[0].response).plus(W(0,0,1))).toJSON();
    assert(!decodeActive(mutated).x_hat.equals(a.x_hat));
  });
  check('omitted_or_duplicated_probe_rows_are_rejected',()=>{
    const bad=roundTrip(mixedPacket);bad.readings.pop();assert.throws(()=>decodeActive(bad),/Unread/);
    const dup=roundTrip(mixedPacket);dup.readings.push(dup.readings[0]);assert.throws(()=>decodeActive(dup),/Duplicate/);
  },true);
  check('mixed_response_is_recovered_modulo_the_blind_line',()=>{
    const r=decodeActive(mixedPacket),diff=qvec(vector(r.x_hat.minus(xc3)),lab3);
    assert(inKernel(opMixed,diff));assert.equal(r.kernel_dimension,1);
    assert(applyOp(opMixed,r.x_hat).equals(applyOp(opMixed,xc3)));
    const other=pt(lab3,[-3,'1/4',2]),r2=decodeActive(activePacket(opMixed,opMixed,other,xc3,3));
    assert(inKernel(opMixed,qvec(vector(r2.x_hat.minus(xc3)),lab3)));
    assert(inKernel(opMixed,qvec(vector(r2.x_hat.minus(r.x_hat)),lab3)));
    details.mixed_response_certificate={...mixedPacket,decoded:{state:r.x_hat.toJSON(),blind_subspace_dimension:r.kernel_dimension,banks:r.banks},
      blind_direction:Kmixed[0].map(String)};
  });
  check('marked_probe_reads_the_componentwise_square_in_two_whole_vector_readings',()=>{
    const x=pt(lab3,['3/2',-2,'1/7']),h=pt(lab3,[1,1,1]),neg=pt(lab3,[-1,-1,-1]);
    const diff=vector(applyOp(opMatching,vector(x.plus(h))).minus(applyOp(opMatching,vector(x.plus(neg)))));
    assert(diff.equals(vector(x.scale(4))));assert.equal(coordinates(diff).length,3);
    const c=pt(lab3,[0,'1/3',-1]),r=decodeActive(activePacket(opMatching,opMatching,c,x,2));
    assert.equal(r.kernel_dimension,0);assert(r.x_hat.equals(x));
  });
  check('square_formula_recovers_x_minus_c_including_the_vanishing_first_response',()=>{
    for(const cv of ['2/5',0,-3])for(const xv of [0,'3/2','-7/3']){
      const c=pt([0],[cv]),x=pt([0],[xv]),packet=squarePacket(opSquare,c,x,[1,'-1','3/2']);
      assert(decodeSquare(roundTrip(packet)).equals(vector(x.minus(c))));
    }
    assert(applyOp(opSquare,pt([0],[0])).equals(nil()));
    const c=pt([0],['2/5']),x=pt([0],['-7/3']),packet=squarePacket(opSquare,c,x,[1,'3/2']);
    details.square_moving_calibration_certificate={...packet,decoded:decodeSquare(packet).toJSON()};
  });
  check('zero_probe_reading_is_identically_zero_and_carries_no_input',()=>{
    const c=pt([0],['2/5']),zero=xv=>squarePacket(opSquare,c,pt([0],[xv]),[0]).probes[0].readings;
    for(const xv of ['3/2','-7/3']){
      const r=zero(xv);assert(vector(S.fromJSON(r.x_plus_h)).equals(vector(S.fromJSON(r.x_minus_h))));
      assert(vector(S.fromJSON(r.c_plus_h)).equals(vector(S.fromJSON(r.c_minus_h))));
    }
    assert.throws(()=>decodeSquare(squarePacket(opSquare,c,pt([0],['3/2']),[0])),/Nonzero probe/);
    const mixed=roundTrip(squarePacket(opSquare,c,pt([0],['3/2']),[1,2]));mixed.probes[1].readings.x_plus_h=mixed.probes[0].readings.x_plus_h;
    assert.throws(()=>decodeSquare(mixed),/disagree/);
  },true);
  // ------------------------------------------------------------ Theorem 3
  check('target_is_recoverable_exactly_when_the_blind_subspace_lies_in_its_kernel',()=>{
    const n=3,K=Kmixed,aPlusC=[[new F(1),new F(0),new F(1)]],aOnly=[[new F(1),new F(0),new F(0)]];
    assert.equal(targetRank(aPlusC,K,n),0);assert.equal(targetRank(aOnly,K,n),1);
    const r=decodeActive(mixedPacket),sum_=A=>mvQ(A,qvec(r.x_hat,lab3))[0],truth=A=>mvQ(A,qvec(xc3,lab3))[0];
    assert(sum_(aPlusC).eq(truth(aPlusC)));assert(!sum_(aOnly).eq(truth(aOnly)));
  });
  check('minimum_extra_linear_channels_equal_the_rank_of_the_target_on_the_blind_subspace',()=>{
    const I3=[0,1,2].map(i=>[0,1,2].map(j=>new F(i===j?1:0)));
    assert.equal(targetRank(I3,Kmixed,3),1);
    const B=repairChannels(I3,Kmixed,3);assert.equal(B.length,1);
    const augmented=augment(opMixed,B);
    assert.equal(kernelBasis(augmented).length,0);
    const repaired=activePacket(augmented,augmented,cc3,xc3,3),r=decodeActive(roundTrip(repaired));assert(r.x_hat.equals(xc3));
    details.repaired_mixed_certificate={...repaired,target:'Whole input from translated readings with the minimum supplementary linear channel',decoded:{state:r.x_hat.toJSON(),blind_subspace_dimension:r.kernel_dimension}};
    // two-input square: one channel, namely the v coordinate up to the chosen representative
    const I2=[[new F(1),new F(0)],[new F(0),new F(1)]],K2=kernelBasis(opUOnly);
    assert.equal(targetRank(I2,K2,2),1);
    const B2=repairChannels(I2,K2,2),aug2=augment(opUOnly,B2),c2=pt(lab2,[1,'1/2']),x2=pt(lab2,['3/2','-4/3']);
    assert.equal(kernelBasis(aug2).length,0);assert(decodeActive(activePacket(aug2,aug2,c2,x2,2)).x_hat.equals(x2));
    assert.equal(targetRank([[new F(1),new F(0)]],K2,2),0);
    details.repair_channel_mixed=B.map(r=>r.map(String));details.repair_channel_u_only=B2.map(r=>r.map(String));
  });
  check('a_channel_that_misses_the_blind_line_leaves_the_target_ambiguous',()=>{
    const zeroChannel=augment(opMixed,[[new F(0),new F(0),new F(0)]]);
    assert.equal(kernelBasis(zeroChannel).length,1);
    for(const B of [[1,0,0],[0,1,0],[0,0,1]].map(r=>r.map(x=>new F(x)))){
      const aug=augment(opMixed,[B]);
      const full=kernelBasis(aug).length===0;
      assert.equal(full,!B[0].add(B[2].neg()).zero());
    }
  },true);
  check('more_values_of_the_same_response_do_not_reveal_the_missing_coordinate',()=>{
    const c=pt(lab2,[1,2]),x=pt(lab2,[3,'1/4']),z=pt(lab2,[3,'-9/5']);
    for(const hv of [[0,0],[1,0],['1/3','5'],['-7/2','2/9']]){
      const h=pt(lab2,hv);assert(activeReading(opUOnly,c,x,h).equals(activeReading(opUOnly,c,z,h)));
    }
    assert.equal(JSON.stringify(activePacket(opUOnly,opUOnly,c,x,4).readings),JSON.stringify(activePacket(opUOnly,opUOnly,c,z,4).readings));
  },true);
  check('a_direction_blind_at_the_cut_can_appear_in_a_higher_unit_layer',()=>{
    const c=pt(lab2,[1,2]),x=pt(lab2,[3,'1/4']),z=pt(lab2,[3,'5/4']);
    const a=activeReading(opLayered,c,x,pt(lab2,[0,0])),b=activeReading(opLayered,c,z,pt(lab2,[0,0]));
    assert(cut(a,0).equals(cut(b,0)));assert(!cut(a,1).equals(cut(b,1)));
    assert.equal(kernelBasis(buildOp({labels:lab2,outputs:[0],terms:[T(0,one,{0:2})]})).length,1);
  });
  // ------------------------------------------------------------ Theorem 4
  const sqC=pt([0],['1/3']),sqX=pt([0],['3/4']);
  const lifted6=(q)=>({target:'Source recovered by the completed observer equation through the stated unit depth',operation:opSquareDeformed,
    unit_memory_through:q,observation:activePacket(opSquareDeformed,opSquareCut,sqC,sqX,3)});
  check('deformed_square_completed_observation_has_the_closed_form_with_identity_cut',()=>{
    const closed=(x,c)=>vector(x.plus(vector(x.times(x).minus(c.times(c))).times(Lam).scale('3/2')));
    for(const xv of ['3/4',0,'-2','5/3']){
      const x=pt([0],[xv]),z=completed(opSquareDeformed,opSquareCut,sqC,3,x);
      assert(z.equals(closed(x,sqC)));assert(cut(z,0).equals(x));
    }
    const probe=(x,c)=>{const f=a=>applyOp(opSquareDeformed,a),h=W(0,0,1),m=W(0,0,-1);
      return vector(c.plus(vector(f(vector(x.plus(h))).minus(f(vector(x.plus(m)))).minus(f(vector(c.plus(h)))).plus(f(vector(c.plus(m))))).scale('1/4')));};
    assert(probe(sqX,sqC).equals(closed(sqX,sqC)));
  });
  check('raw_square_cut_has_no_left_inverse_but_the_completed_cut_is_the_identity',()=>{
    const f=x=>applyOp(opSquareCut,x),p=pt([0],[1]),m=pt([0],[-1]);
    assert(f(p).equals(f(m)));assert(!p.equals(m));
    assert(applyOp(opSquareCut,pt([0],[0])).equals(nil()));
    const first=(x,h)=>vector(applyOp(opSquareCut,vector(x.plus(h))).minus(applyOp(opSquareCut,x)).minus(applyOp(opSquareCut,h)));
    assert(first(pt([0],[0]),pt([0],[1])).equals(nil()));
    for(const xv of [1,-1,'2/3'])assert(cut(completed(opSquareDeformed,opSquareCut,sqC,3,pt([0],[xv])),0).equals(pt([0],[xv])));
  },true);
  check('completed_observer_equation_recovers_the_source_one_unit_layer_per_update',()=>{
    const q=4,packet=lifted6(q),r=decodeLifted(roundTrip(packet)),want=sqX;
    assert(S.fromJSON(r.state).equals(cut(want,q)));
    r.updates.forEach((u,k)=>assert(cut(S.fromJSON(u),k).equals(cut(want,k))));
    for(let k=0;k<q;k++)assert(!cut(S.fromJSON(r.updates[k]),k+1).equals(cut(want,k+1)));
    const z=S.fromJSON(r.observed_completion),c=sqC;
    const zz=vector(z.times(z).minus(c.times(c))),series=vector(z.minus(vector(zz.times(Lam)).scale('3/2')).plus(vector(vector(z.times(zz)).times(Lam).times(Lam)).scale('9/2')));
    assert(cut(series,2).equals(cut(want,2)));
    details.deformed_square_certificate={...packet,decoded:r};
  });
  check('one_fewer_update_misses_a_unit_layer',()=>{
    const q=3,r=decodeLifted(lifted6(q)),early=S.fromJSON(r.updates[q-1]);
    assert(cut(early,q-1).equals(cut(sqX,q-1)));
    assert(!cut(early,q).equals(cut(sqX,q)));
    assert(cut(S.fromJSON(r.updates[q]),q).equals(cut(sqX,q)));
  },true);
  const pairX=vector(pt(lab2,['2/3',-1]).plus(W(0,1,'1/5'))),pairC=pt(lab2,['1/2',2]);
  check('supplementary_channel_repairs_the_two_input_cut_and_the_lifted_decode_recovers_both_coordinates',()=>{
    assert.equal(kernelBasis(opPairCut).length,0);
    const q=3,packet={target:'Source of the augmented response (u^2+Lambda u^3, v)',operation:opPairDeformed,unit_memory_through:q,observation:activePacket(opPairDeformed,opPairCut,pairC,pairX,3)};
    const r=decodeLifted(roundTrip(packet));
    assert(S.fromJSON(r.state).equals(cut(pairX,q)));
    r.updates.forEach((u,k)=>assert(cut(S.fromJSON(u),k).equals(cut(pairX,k))));
    details.augmented_pair_certificate={...packet,decoded:r};
  });
  check('inconsistent_bank_decodes_a_candidate_that_does_not_match_its_forward_readings',()=>{
    const aug=augment(opMixed,repairChannels([0,1,2].map(i=>[0,1,2].map(j=>new F(i===j?1:0))),Kmixed,3));
    const good=activePacket(aug,aug,cc3,xc3,3),corrupt=roundTrip(good);
    corrupt.readings[7].response=vector(S.fromJSON(corrupt.readings[7].response).plus(W(1,0,2))).toJSON();
    const cand=decodeActive(corrupt).x_hat,forward=activePacket(aug,aug,cc3,cand,3);
    assert.notEqual(JSON.stringify(forward.readings),JSON.stringify(corrupt.readings));
    assert.equal(JSON.stringify(activePacket(aug,aug,cc3,decodeActive(good).x_hat,3).readings),JSON.stringify(good.readings));
  },true);
  check('wrong_calibration_label_shifts_the_absolute_decode',()=>{
    const wrong=roundTrip(cubicPacket);wrong.calibration=pt(lab2,[1,-2]).toJSON();
    assert(decodeActive(cubicPacket).x_hat.equals(cubicX));
    assert(!decodeActive(wrong).x_hat.equals(cubicX));
  },true);
  // ------------------------------------------------------------ Section 7
  check('recovered_state_is_independent_of_the_calibration_for_a_null_blind_subspace',()=>{
    const x=pt([0],['5/6']);
    for(const cv of [0,'1/2','-3','7/4'])assert(decodeActive(activePacket(opSquare,opSquare,pt([0],[cv]),x,2)).x_hat.equals(x));
    assert.equal(kernelBasis(opSquare).length,0);
  });
  const Umat=[[1,2,0],[0,1,1],[1,0,1]].map(r=>r.map(x=>new F(x))),Vmat=[[1,1],[0,2]].map(r=>r.map(x=>new F(x)));
  const opT=transportOp(opMixed,Umat,Vmat);
  check('frame_transport_maps_the_blind_subspace_and_preserves_the_channel_count',()=>{
    const Kt=kernelBasis(opT),UK=Kmixed.map(k=>mvQ(Umat,k));
    assert.equal(Kt.length,Kmixed.length);
    assert.equal(rankQ([...Kt,...UK],3),Kt.length);
    const A=[[new F(1),new F(0),new F(0)]],Atilde=mulQ(A,invQ(Umat));
    assert.equal(targetRank(Atilde,Kt,3),targetRank(A,Kmixed,3));
    const I3=[0,1,2].map(i=>[0,1,2].map(j=>new F(i===j?1:0)));
    assert.equal(targetRank(mulQ(I3,invQ(Umat)),Kt,3),targetRank(I3,Kmixed,3));
    const cT=fromS(matS(Umat,svec(cc3,lab3)),lab3),xT=fromS(matS(Umat,svec(xc3,lab3)),lab3);
    const h=pt(lab3,['1/2',-1,2]),hT=fromS(matS(Umat,svec(h,lab3)),lab3);
    const mapped=fromS(matS(Vmat,svec(activeReading(opMixed,cc3,xc3,h),[0,1])),[0,1]);
    assert(activeReading(opT,cT,xT,hT).equals(mapped));
    details.transport={U:Umat.map(r=>r.map(String)),V:Vmat.map(r=>r.map(String)),blind_subspace_dimension:Kt.length};
  });
  check('untransported_probes_change_the_experiment',()=>{
    const cT=fromS(matS(Umat,svec(cc3,lab3)),lab3),xT=fromS(matS(Umat,svec(xc3,lab3)),lab3);
    const h=pt(lab3,['1/2',-1,2]),hWrong=h;
    const mapped=fromS(matS(Vmat,svec(activeReading(opMixed,cc3,xc3,h),[0,1])),[0,1]);
    assert(!activeReading(opT,cT,xT,hWrong).equals(mapped));
  },true);
  check('every_archived_observer_certificate_redecodes_from_its_saved_readings',()=>{
    const arc=roundTrip(details),same=(a,b)=>vector(S.fromJSON(a)).equals(vector(S.fromJSON(b)));
    for(const k of ['cubic_plus_linear_certificate','mixed_response_certificate','repaired_mixed_certificate']){
      const p=arc[k];assert(typeof p.target==='string'&&p.readings.length===p.declared_degree**p.decoder_operation.input_labels.length);
      assert(same(decodeActive(p).x_hat.toJSON(),p.decoded.state));
    }
    assert(same(decodeSquare(arc.square_moving_calibration_certificate).toJSON(),arc.square_moving_calibration_certificate.decoded));
    for(const k of ['deformed_square_certificate','augmented_pair_certificate']){
      const p=arc[k],{decoded,...packet}=p;assert(same(decodeLifted(packet).state,decoded.state));
    }
  });
  const dims={labels:3,declared_degree:3,probe_bank_size:27};
  return {schema:'rkf.lambda-active-readings.v1',date:'2026-10-12',status:'PASS_ACTIVE_READING_AND_SINGULAR_CUT_REPAIR',
    theorem_count:4,proposition_count:2,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting sectors over Q and Q[Lambda]',source:'Declared symmetric joint banks and supplied calibration',zero:'Typed cut operation; additive neutrals retain their separate types',
      primitive_metric:false,analytic_derivative_assumed:false,unknown_polynomial_degree_inferred_from_samples:false,passive_single_reading_sufficient:false,RH_development:false,curvature_developed:false},
    finite_ranges:{...dims,deformed_square_unit_depth:4,augmented_pair_unit_depth:3,two_input_probe_bank_size:9,transport_matrix_size:3},
    details,evidence:{general_results:'Four written derivations and two stated transport propositions',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false,SE34_certified:false},
    not_claimed:['recovery from a passive single reading','recovery of an unknown operation or degree from finite samples','recovery of an unknown infinite counting state from one finite bank',
      'arbitrary nonlinear invertibility','noisy-data stability','restricted-observer recovery','uniform minimality over nonlinear encodings or adaptive experiments','new RH or curvature result','novelty priority for finite differences or triangular lifting']};
}
module.exports={buildOp,applyOp,activePacket,decodeActive,squarePacket,decodeSquare,decodeLifted,kernelBasis,contraction,repairChannels,targetRank,transportOp,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE35_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}
