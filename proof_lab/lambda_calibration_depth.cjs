'use strict';
// SE38 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const ac=require('./lambda_action_closure.cjs');
const {F}=o,S=previous.presentation,{vector}=count;
const {sc,sAdd,sSub,sMul,sEq,sUnit,sNorm,INF,pConst,pVar,pAdd,pSub,pScale,pMul,pEq,pCompose,pEval,pNorm,pVec,Span,toState,fromState,binom,keyOf,expOf}=ac;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_CALIBRATION_DEPTH_RESULT.json');
const roundTrip=x=>JSON.parse(JSON.stringify(x));
const Q=x=>x instanceof F?x:new F(x);
const sNormQ=(a,q)=>{let b=a.slice(0,Number.isFinite(q)?q+1:a.length);while(b.length&&b[b.length-1].zero())b.pop();return b;};
const pPow=(p,e,n,q=INF)=>{let r=pConst(n,sc(1));for(let i=0;i<e;i++)r=pMul(r,p,q);return r;};
const cutP=(p,q)=>pNorm(p,q);
const deg=a=>a.reduce((x,y)=>x+y,0);
// ---- Theorem 1: the monomial calibration algebra A_D ----
function multiIndices(n,maxDeg,minDeg=1){const out=[];const rec=(i,left,acc)=>{if(i===n){const d=deg(acc);if(d>=minDeg)out.push(acc.slice());return;}for(let e=0;e<=left;e++){acc.push(e);rec(i+1,left-e,acc);acc.pop();}};rec(0,maxDeg,[]);return out.sort((a,b)=>deg(a)-deg(b)||keyOf(b).localeCompare(keyOf(a)));}
const generators=(n,D)=>multiIndices(n,D).map(keyOf);
function inAD(p,D){for(const [k,s]of p){const a=deg(expOf(k));for(let r=0;r<s.length;r++)if(!s[r].zero()&&a>D*r)return false;}return true;}
// Express a polynomial in c as a polynomial in U_alpha=Lambda c^alpha (SE38.6), without division by Lambda.
function expressInU(p,n,D){
  const terms=[];
  for(const [k,s]of p){const al=expOf(k),factors=[];al.forEach((e,i)=>{for(let j=0;j<e;j++)factors.push(i);});
    s.forEach((cf,r)=>{if(cf.zero())return;const l=Math.ceil(factors.length/D);if(l>r&&factors.length)throw new RangeError('Monomial outside A_D');
      const groups=[];for(let g=0;g<l;g++){const e=Array(n).fill(0);factors.slice(g*D,(g+1)*D).forEach(i=>{e[i]++;});groups.push(keyOf(e));}
      terms.push({coefficient:cf.toString(),unit_power:r-l,factors:groups});});}
  return terms;
}
function evalU(terms,U,q){let r=[];for(const t of terms){let v=sUnit(t.unit_power,t.coefficient);for(const f of t.factors){if(!U.has(f))throw new RangeError('Unread calibration coordinate '+f);v=sMul(v,U.get(f),q);}r=sAdd(r,v,q);}return sNormQ(r,q);}
function rebuild(terms,n){let p=new Map();for(const t of terms){let m=pConst(n,sUnit(t.unit_power,t.coefficient));for(const f of t.factors)m=pMul(m,pScale(pNorm(new Map([[f,sc(1)]]),INF),sUnit(1),INF),INF);p=pAdd(p,m,INF);}return p;}
// ---- Theorem 2: relative coefficients and calibration closure ----
const lift2=(p,n)=>pCompose(p,Array.from({length:n},(_,i)=>pVar(2*n,i)),INF);
function relativeCoefficients(g,n){
  const subs=Array.from({length:n},(_,i)=>pAdd(pVar(2*n,i),pVar(2*n,n+i),INF));
  return g.map(comp=>{const inc=pSub(pCompose(comp,subs,INF),lift2(comp,n),INF),by=new Map();
    for(const [k,s]of inc){const e=expOf(k),b=keyOf(e.slice(n)),a=keyOf(e.slice(0,n));if(!by.has(b))by.set(b,new Map());by.get(b).set(a,s);}
    return [...by].map(([b,m])=>({beta:b,coefficient:pNorm(m,INF)}));});
}
function nonlinearTerms(g){const out=[];g.forEach(comp=>{for(const [k,s]of comp){const a=deg(expOf(k));s.forEach((c,r)=>{if(c.zero())return;if(a>=2&&r===0)throw new RangeError('Nonlinear cut: outside the affine-cut class');if(a>=2)out.push({a,r});});}});return out;}
const criterion=(cat,D)=>cat.every(g=>nonlinearTerms(g).every(({a,r})=>a-1<=D*r));
const Dstar=cat=>Math.max(0,...cat.flatMap(g=>nonlinearTerms(g).map(({a,r})=>Math.ceil((a-1)/r))));
// The closed observer formulas (SE38.10), derived from the supplied catalogue.
function observerFormulas(cat,n,D){
  const gens=generators(n,D);
  return cat.map(g=>({
    calibration:gens.map(k=>{const al=expOf(k);let m=pConst(n,sUnit(1));al.forEach((e,i)=>{m=pMul(m,pPow(g[i],e,n),INF);});return {generator:k,expression:expressInU(m,n,D)};}),
    relative:relativeCoefficients(g,n).map(comp=>comp.map(({beta,coefficient})=>{if(!inAD(coefficient,D))throw new RangeError('Relative coefficient outside A_D');return {beta,expression:expressInU(coefficient,n,D)};}))}));
}
function bankPacket(target,cat,n,D,q,x,c,words){
  const gens=generators(n,D),run=(w,pt)=>w.reduce((p,i)=>cat[i].map(comp=>pEval(comp,p,q)),pt);
  const Uof=pt=>Object.fromEntries(gens.map(k=>{let v=sUnit(1);expOf(k).forEach((e,i)=>{for(let j=0;j<e;j++)v=sMul(v,pt[i],q);});return [k,toState([v]).toJSON()];}));
  const rel=w=>toState(run(w,x).map((s,i)=>sSub(s,run(w,c)[i],q))).toJSON();
  return {target,sector_size:n,degree_bound:D,unit_memory_through:q,formulas:observerFormulas(cat,n,D),
    calibration_bank:Uof(c),relative_reading:rel([]),future_protocols:words.map(w=>({word:w,relative_reading:rel(w),calibration_bank:Uof(run(w,c))}))};
}
function decodeBank(packet){
  const n=packet.sector_size,q=packet.unit_memory_through;
  const U0=new Map(Object.entries(packet.calibration_bank).map(([k,j])=>[k,fromState(j,1)[0]])),d0=fromState(packet.relative_reading,n);
  const step=([U,d],i)=>{const f=packet.formulas[i];
    const d2=f.relative.map(comp=>comp.reduce((acc,{beta,expression})=>{let v=evalU(expression,U,q);expOf(beta).forEach((e,j)=>{for(let t=0;t<e;t++)v=sMul(v,d[j],q);});return sAdd(acc,v,q);},[]));
    const U2=new Map(f.calibration.map(({generator,expression})=>[generator,evalU(expression,U,q)]));return [U2,d2];};
  return packet.future_protocols.map(p=>{const [U,d]=p.word.reduce(step,[U0,d0]);return {word:p.word,relative_reading:toState(d).toJSON(),calibration_bank:Object.fromEntries([...U].map(([k,v])=>[k,toState([v]).toJSON()]))};});
}
// ---- Theorem 5: labelled coefficient shift and the shallow calibration record ----
function shiftDown(s,k,q){for(let r=0;r<Math.min(k,s.length);r++)if(!s[r].zero())throw new RangeError('Calibration record must lie in Lambda^k R_q');return sNormQ(s.slice(k),q-k);}
// Scalar actions g(x)=A x+b+Lambda^w H(x) with A,b in R and H a polynomial over R.
function applyAction(act,x,q){const X=pVar(1,0),g=pAdd(pAdd(pScale(X,act.A,INF),pConst(1,act.b),INF),pScale(act.H,sUnit(act.w),INF),INF);return pEval(g,[x],q);}
function depthPacket(target,cat,q,s,x,c,words){
  const w=Math.min(...cat.map(a=>a.w)),k=w+s,run=(word,pt)=>word.reduce((p,i)=>applyAction(cat[i],p,q),pt);
  const ser=a=>({A:a.A.map(String),b:a.b.map(String),w:a.w,H:[...a.H].map(([kk,v])=>[kk,v.map(String)])});
  return {target,unit_memory_through:q,relative_order:s,common_unit_order:w,catalogue:cat.map(ser),
    calibration_record:k<=q?toState([sMul(sUnit(k),c,q)]).toJSON():null,relative_reading:toState([sSub(x,c,q)]).toJSON(),
    future_protocols:words.map(word=>({word,relative_reading:toState([sSub(run(word,x),run(word,c),q)]).toJSON()}))};
}
const parseAct=a=>({A:a.A.map(Q),b:a.b.map(Q),w:a.w,H:pNorm(new Map(a.H.map(([k,v])=>[k,v.map(Q)])),INF)});
function decodeDepth(packet,liftJunk=null){
  const q=packet.unit_memory_through,s=packet.relative_order,cat=packet.catalogue.map(parseAct),w=Math.min(...cat.map(a=>a.w)),k=w+s;
  if(cat.some(a=>a.w<w))throw new RangeError('Common unit order required');
  let d=fromState(packet.relative_reading,1)[0];if(d.slice(0,s).some(x=>!x.zero()))throw new RangeError('Relative reading below its declared unit order');
  let gamma=packet.calibration_record?fromState(packet.calibration_record,1)[0]:null;
  return packet.future_protocols.map(p=>{let G=gamma,D=d;
    for(const i of p.word){const a=cat[i],X=pVar(1,0),Hp=pScale(a.H,sUnit(a.w),INF);
      if(q<k){D=sNormQ(sMul(a.A,D,q),q);continue;}
      const h=shiftDown(G,k,q),ht=liftJunk?sAdd(h,sUnit(q-k+1,liftJunk),q):h;
      G=sMul(sUnit(k),applyAction(a,ht,q),q);
      D=sAdd(sMul(a.A,D,q),sSub(pEval(Hp,[sAdd(ht,D,q)],q),pEval(Hp,[ht],q),q),q);}
    return {word:p.word,relative_reading:toState([D]).toJSON()};});
}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE37_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const stEq=(a,b)=>vector(S.fromJSON(a)).equals(vector(S.fromJSON(b)));
  const L=(n,r,cf=1)=>pConst(n,sUnit(r,cf)),X=pVar(1,0);
  // -------------------------------------------------- Theorem 1
  check('membership_criterion_and_partition_expression_agree',()=>{
    for(const [n,D] of [[1,2],[2,1],[2,2],[2,3]]){
      assert.equal(generators(n,D).length,binom(n+D,D)-1);
      for(const al of multiIndices(n,3*D,0))for(let r=0;r<=4;r++){
        const m=pNorm(new Map([[keyOf(al),sUnit(r,'3/7')]]),INF),inside=deg(al)<=D*r||deg(al)===0;
        assert.equal(inAD(m,D),inside);
        if(inside)assert(pEq(rebuild(expressInU(m,n,D),n),m));else assert.throws(()=>expressInU(m,n,D),/outside A_D/);
      }
    }
  });
  check('calibration_coordinates_satisfy_their_unit_relation',()=>{
    const a=pScale(X,sUnit(1),INF),b=pScale(pMul(X,X,INF),sUnit(1),INF);
    assert(pEq(pMul(a,a,INF),pScale(b,sUnit(1),INF)));
    const lhs=pMul(L(1,4),pPow(X,6,1),INF);
    assert(pEq(rebuild(expressInU(lhs,1,2),1),lhs));assert(pEq(rebuild(expressInU(lhs,1,3),1),lhs));
  });
  check('a_cut_level_calibration_is_not_in_the_memory_algebra',()=>{
    assert(!inAD(X,4));assert(!inAD(pMul(L(1,1),pPow(X,3,1),INF),2));
    assert.throws(()=>expressInU(X,1,3),/outside A_D/);
  },true);
  // -------------------------------------------------- Theorem 2
  const u=pVar(2,0),v=pVar(2,1);
  const cat2=[[pAdd(u,pMul(L(2,1),pMul(v,v,INF),INF),INF),pAdd(v,pMul(L(2,2),pPow(u,3,2),INF),INF)],
              [v,pAdd(pAdd(pScale(u,sUnit(0,2),INF),pConst(2,sc(1)),INF),pMul(L(2,1),pMul(pMul(u,u,INF),v,INF),INF),INF)],
              [pAdd(pScale(u,sc(1,'1/2'),INF),pConst(2,sc(0,-3)),INF),v]];
  check('degree_unit_rule_holds_at_the_least_monomial_degree',()=>{
    assert.equal(Dstar(cat2),2);assert(criterion(cat2,2));assert(!criterion(cat2,1));
    assert.doesNotThrow(()=>observerFormulas(cat2,2,2));assert.throws(()=>observerFormulas(cat2,2,1),/outside A_D/);
    assert.equal(Dstar([[X]]),0);
  });
  check('necessity_reads_the_offending_relative_coefficient',()=>{
    const cubic=[[pAdd(X,pMul(L(1,1),pPow(X,3,1),INF),INF)]];
    const co=relativeCoefficients(cubic[0],1)[0].find(t=>t.beta==='1').coefficient;
    assert(!inAD(co,1));assert(inAD(co,2));assert.equal(Dstar(cubic),2);
  },true);
  check('substitution_preserves_the_memory_algebra',()=>{
    for(const g of cat2)for(const k of generators(2,2)){let m=pConst(2,sUnit(1));expOf(k).forEach((e,i)=>{m=pMul(m,pPow(g[i],e,2),INF);});assert(inAD(m,2));}
  });
  check('nonlinear_cut_action_is_refused',()=>{
    assert.throws(()=>Dstar([[pMul(X,X,INF)]]),/Nonlinear cut/);
  },true);
  const xB=[sc('1/2',3,0,-1),sc(-2,'1/3',1)],cB=[sc(1,-1,'2/5'),sc('3/2',0,-4,1)];
  check('closed_bank_observer_predicts_every_relative_reading_and_calibration',()=>{
    const words=[[0],[1,0],[2,1,0],[0,0,1,2],[1,2,1,0,0,2]];
    const pkt=bankPacket('Relative readings and calibration bank after catalogue words, at depth three',cat2,2,2,3,xB,cB,words);
    const r=decodeBank(roundTrip(pkt));
    r.forEach((p,i)=>{assert(stEq(p.relative_reading,pkt.future_protocols[i].relative_reading));
      for(const k of generators(2,2))assert(stEq(p.calibration_bank[k],pkt.future_protocols[i].calibration_bank[k]));});
    details.closed_bank_certificate={...pkt,decoded:r};
  });
  check('the_same_formulas_serve_every_retained_depth',()=>{
    const words=[[2,0,1]],deep=decodeBank(bankPacket('t',cat2,2,2,4,xB,cB,words))[0],sh=decodeBank(bankPacket('t',cat2,2,2,2,xB,cB,words))[0];
    const a=fromState(deep.relative_reading,2).map(s=>sNormQ(s,2)),b=fromState(sh.relative_reading,2);a.forEach((s,i)=>assert(sEq(s,b[i])));
    assert.deepEqual(bankPacket('t',cat2,2,2,4,xB,cB,words).formulas,bankPacket('t',cat2,2,2,2,xB,cB,words).formulas);
  });
  check('affine_frame_change_preserves_the_memory_algebra',()=>{
    const Sm=[[2,1],[1,1]],Si=[[1,-1],[-1,2]],t=['1/2',-3],ti=[Q(t[0]).neg().mul(Q(1)).add(Q(t[1]).mul(Q(1))),Q(t[0]).add(Q(t[1]).mul(Q(-2)))];
    const fwd=[0,1].map(i=>pAdd(pAdd(pScale(u,sc(Sm[i][0]),INF),pScale(v,sc(Sm[i][1]),INF),INF),pConst(2,sc(t[i])),INF));
    const back=[0,1].map(i=>pAdd(pAdd(pScale(u,sc(Si[i][0]),INF),pScale(v,sc(Si[i][1]),INF),INF),pConst(2,sc(ti[i])),INF));
    [0,1].forEach(i=>assert(pEq(pCompose(back[i],fwd,INF),[u,v][i])));
    for(const map of [fwd,back])for(const k of generators(2,2)){let m=pConst(2,sUnit(1));expOf(k).forEach((e,i)=>{m=pMul(m,pPow(map[i],e,2),INF);});assert(inAD(m,2));}
  });
  // -------------------------------------------------- Theorem 3
  const monomialAction=(h,w,d)=>[pAdd(X,pMul(L(1,w,h),pPow(X,d+1,1),INF),INF)];
  check('monomial_action_has_the_closed_least_bank_formulas',()=>{
    for(const [h,w,d] of [[1,1,2],['-3/2',2,2],['2/5',1,3]]){
      const g=monomialAction(h,w,d)[0],U=j=>pMul(L(1,w),pPow(X,j,1),INF),ud=U(d);
      for(let j=1;j<=d;j++)assert(pEq(pCompose(U(j),[g],INF),pMul(U(j),pPow(pAdd(pConst(1,sc(1)),pScale(ud,sc(h),INF),INF),j,1),INF)));
      const co=relativeCoefficients([g],1)[0];
      for(let kk=1;kk<=d+1;kk++){const t=co.find(z=>z.beta===String(kk)).coefficient;
        const want=kk<=d?pAdd(kk===1?pConst(1,sc(1)):new Map(),pScale(U(d+1-kk),sc(Q(h).mul(new F(binom(d+1,kk)))),INF),INF):pConst(1,sUnit(w,h));assert(pEq(t,want));}
    }
  });
  check('the_least_bank_needs_d_generators_at_the_first_memory_layer',()=>{
    for(const [w,d] of [[1,2],[2,2],[1,3],[3,4]]){
      const sp=new Span();for(let j=1;j<=d;j++)sp.add(pVec(cutP(pMul(L(1,w),pPow(X,j,1),INF),w)));assert.equal(sp.size,d);
      const t1=pMul(L(1,w),X,INF),t2=pMul(L(1,w),pPow(X,d,1),INF);assert.equal(cutP(pMul(t1,t2,INF),w).size,0);
    }
  });
  check('a_larger_algebra_coordinate_is_not_in_the_least_bank',()=>{
    const w=2,d=2,inB=p=>[...p].every(([k,s])=>s.every((c,r)=>c.zero()||Number(k)===0||r>=w*Math.ceil(Number(k)/d)));
    assert(inB(pMul(L(1,2),X,INF)));assert(inB(pMul(L(1,4),pPow(X,3,1),INF)));assert(!inB(pMul(L(1,1),X,INF)));
  },true);
  const aS=pVar(2,0),bS=pVar(2,1);
  check('cubic_obstruction_is_repaired_and_preserves_its_relation',()=>{
    const one=pConst(2,sc(1));
    const a2=pMul(aS,pAdd(one,bS,INF),INF),b2=pMul(bS,pMul(pAdd(one,bS,INF),pAdd(one,bS,INF),INF),INF);
    const rel=p=>pSub(pMul(p[0],p[0],INF),pScale(p[1],sUnit(1),INF),INF);
    assert(pEq(rel([a2,b2]),pMul(rel([aS,bS]),pMul(pAdd(one,bS,INF),pAdd(one,bS,INF),INF),INF)));
    const g3=monomialAction(1,1,2)[0],a=pMul(L(1,1),X,INF),b=pMul(L(1,1),pMul(X,X,INF),INF);
    assert(pEq(pCompose(a,[g3],INF),pCompose(a2,[a,b],INF)));assert(pEq(pCompose(b,[g3],INF),pCompose(b2,[a,b],INF)));
  });
  check('ordered_quadratic_and_cubic_words_are_read_by_one_bank',()=>{
    const g2=pAdd(X,pMul(L(1,1),pMul(X,X,INF),INF),INF),g3=monomialAction(1,1,2)[0];
    assert(pEq(cutP(pSub(pCompose(g3,[g2],INF),pCompose(g2,[g3],INF),INF),2),pMul(L(1,2),pPow(X,4,1),INF)));
    const cat=[[g2],[g3]],x=[sc(2,-1,'1/3',5)],c=[sc('1/2',0,2,-1)];
    const pkt=bankPacket('Relative readings of the ordered words g3 g2 and g2 g3, depth three',cat,1,2,3,x,c,[[0,1],[1,0]]);
    const r=decodeBank(roundTrip(pkt)),d=p=>fromState(p.relative_reading,1)[0];
    r.forEach((p,i)=>assert(stEq(p.relative_reading,pkt.future_protocols[i].relative_reading)));
    const A=sMul(sUnit(1),c[0],2),B=sMul(sUnit(1),sMul(c[0],c[0],2),2),Dl=sSub(x[0],c[0],2),m=(...xs)=>xs.reduce((p,y)=>sMul(p,y,2),sc(1));
    const want=[m(sc(4),A,B,Dl),m(sc(6),sUnit(1),B,Dl,Dl),m(sc(4),sUnit(1),A,Dl,Dl,Dl),m(sUnit(2),Dl,Dl,Dl,Dl)].reduce((p,y)=>sAdd(p,y,2),[]);
    assert(sEq(sNormQ(sSub(d(r[0]),d(r[1]),3),2),want));
    details.ordered_word_certificate={...pkt,decoded:r};
  });
  // -------------------------------------------------- Theorem 4
  check('retained_memory_algebra_has_the_stated_dimension',()=>{
    for(const [n,D,q] of [[1,2,3],[2,1,3],[2,2,2],[1,3,2]]){
      const gens=generators(n,D).map(k=>pScale(pNorm(new Map([[k,sc(1)]]),INF),sUnit(1),INF)),sp=new Span();
      const rec=(start,l,prod)=>{for(let kk=0;kk+l<=q;kk++)sp.add(pVec(cutP(pScale(prod,sUnit(kk),INF),q)));if(l===q)return;for(let i=start;i<gens.length;i++)rec(i,l+1,cutP(pMul(prod,gens[i],INF),q));};
      rec(0,0,pConst(n,sc(1)));
      const formula=Array.from({length:q+1},(_,r)=>binom(n+D*r,D*r)).reduce((a,b)=>a+b,0);
      assert.equal(sp.size,formula);
    }
  });
  check('the_cut_quotient_is_not_the_lambda_multiple_quotient',()=>{
    const Ua=pMul(L(1,1),pMul(X,X,INF),INF);assert.equal(cutP(Ua,0).size,0);assert(!inAD(pMul(X,X,INF),2));
    // Lambda^2 U_alpha=Lambda^3 c^2 lies in A_D and dies at the depth-two cut, yet is not Lambda^3 times an element of A_D.
    const LqU=pScale(Ua,sUnit(2),INF);assert(inAD(LqU,2));assert.equal(cutP(LqU,2).size,0);assert(!inAD(pMul(X,X,INF),2));
  },true);
  // -------------------------------------------------- Theorem 5
  const act=(A,b,w,H)=>({A:sc(...A),b:sc(...b),w,H});
  const catD=[act([1],[0],1,pPow(X,3,1)),act([1,1],['1/2'],1,pAdd(pMul(X,X,INF),pScale(pPow(X,3,1),sUnit(1,-2),INF),INF)),act([2],[0,3],1,pAdd(pScale(X,sc(-1),INF),pPow(X,4,1),INF))];
  check('labelled_shift_refuses_a_record_with_low_unit_coefficients',()=>{
    assert(sEq(shiftDown(sc(0,0,3,4,5),2,4),sc(3,4,5)));assert.throws(()=>shiftDown(sc(0,1,3),2,4),/Lambda\^k/);
  },true);
  check('shallow_calibration_update_equals_the_actual_update_for_every_lift',()=>{
    for(const [q,s] of [[3,0],[5,1],[4,2]]){
      const c=sc(2,-1,'1/3',4,0,7),Dl=sUnit(s,'3/2'),x=sAdd(c,sAdd(Dl,sUnit(s+1,-2),q),q),words=[[0],[1,0],[2,1,0,0],[1,2,2,0,1]];
      const pkt=depthPacket('t',catD,q,s,x,c,words);
      for(const junk of [null,'5','-7/2']){const r=decodeDepth(roundTrip(pkt),junk);r.forEach((p,i)=>assert(stEq(p.relative_reading,pkt.future_protocols[i].relative_reading)));}
      pkt.future_protocols.forEach(p=>{const d=fromState(p.relative_reading,1)[0];assert(d.slice(0,s).every(y=>y.zero()));});
    }
  });
  check('labelled_calibration_record_certificate_at_depth_five',()=>{
    const q=5,s=1,c=sc(2,-1,'1/3',4,0,7),x=sAdd(c,sc(0,'3/2',-2,0,1),q),words=[[0],[1,0],[2,1,0,0],[1,2,2,0,1],[0,0,0,1,1,2,2]];
    const pkt=depthPacket('Relative readings after catalogue words, from Lambda^2 c and Delta at depth five',catD,q,s,x,c,words),r=decodeDepth(roundTrip(pkt));
    r.forEach((p,i)=>assert(stEq(p.relative_reading,pkt.future_protocols[i].relative_reading)));
    assert.equal(fromState(pkt.calibration_record,1)[0].length,q+1);
    details.calibration_depth_certificate={...pkt,decoded:r};
  });
  check('omitted_calibration_coefficients_cannot_affect_relative_readings',()=>{
    const q=3,s=1,Dl=sc(0,2,-1,'1/2'),words=[[0],[0,1],[2,0,1,1],[1,1,2,0,0]];
    const run=(c)=>depthPacket('t',catD,q,s,sAdd(c,Dl,q),c,words).future_protocols;
    assert.deepEqual(run(sc(1,-2,5,9)),run(sc(1,-2,-4,0)));assert.notDeepEqual(run(sc(1,-2,5,9)),run(sc(1,3,5,9)));
  });
  check('below_the_combined_order_no_calibration_is_needed',()=>{
    const q=2,s=2,Dl=sUnit(2,3),words=[[0,1],[2,2,0]];
    const a=depthPacket('t',catD,q,s,sAdd(sc(5,1),Dl,q),sc(5,1),words),b=depthPacket('t',catD,q,s,sAdd(sc(-1,9,2),Dl,q),sc(-1,9,2),words);
    assert.equal(a.calibration_record,null);assert.deepEqual(a.future_protocols,b.future_protocols);
    decodeDepth(a).forEach((p,i)=>assert(stEq(p.relative_reading,a.future_protocols[i].relative_reading)));
  });
  check('the_calibration_depth_bound_is_sharp',()=>{
    for(const [q,w,s] of [[3,1,1],[4,2,1],[5,1,0],[6,3,2]]){
      const g=[act([1],[0],w,pMul(X,X,INF))],Dl=sUnit(s),c0=sc(0),c1=sUnit(q-w-s);
      const nxt=c=>sSub(applyAction(g[0],sAdd(c,Dl,q),q),applyAction(g[0],c,q),q);
      assert(sEq(sSub(nxt(c1),nxt(c0),q),sUnit(q,2)));
      assert(sEq(sNormQ(c0,q-w-s-1),sNormQ(c1,q-w-s-1)));
    }
  },true);
  check('a_relative_reading_below_its_declared_order_is_refused',()=>{
    const pkt=depthPacket('t',catD,3,1,sc(1,1),sc(1),[[0]]);pkt.relative_reading=toState([sc(1,1)]).toJSON();
    assert.throws(()=>decodeDepth(pkt),/declared unit order/);
  },true);
  check('every_archived_certificate_redecodes_from_its_saved_readings',()=>{
    const arc=roundTrip(details);
    for(const k of ['closed_bank_certificate','ordered_word_certificate'])decodeBank(arc[k]).forEach((p,i)=>assert(stEq(p.relative_reading,arc[k].decoded[i].relative_reading)));
    decodeDepth(arc.calibration_depth_certificate).forEach((p,i)=>assert(stEq(p.relative_reading,arc.calibration_depth_certificate.decoded[i].relative_reading)));
  });
  return {schema:'rkf.lambda-calibration-depth.v1',date:'2026-10-13',status:'PASS_UNIT_WEIGHTED_CALIBRATION_AND_CUT_DEPTH',
    theorem_count:5,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting sectors over Q[Lambda] and retained unit quotients',source:'Supplied affine-cut catalogue, recorded relative readings and recorded calibration readings',
      zero:'Typed cut operation; additive neutrals retain their separate types',inverse_of_lambda_on_R_q:false,radical_replaces_unit_relations:false,primitive_metric:false,numerical_unit_value_assumed:false,RH_development:false,curvature_developed:false},
    finite_ranges:{monomial_bank_cases:'(n,D) in (1,2),(2,1),(2,2),(2,3)',closed_bank_depth:3,dimension_cases:4,least_bank_cases:4,calibration_depths:[3,4,5],sharpness_cases:4},
    details,evidence:{general_results:'Five written derivation groups',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['a minimum among all observers or decoder types','finite generation of the least all-depth calibration subalgebra for every catalogue','finite information at infinite depth',
      'recovery of an absolute target from a relative reading and a shortened calibration','noisy measurement, conditioning or acquisition cost','convergence at a nonzero numerical unit','new RH, Yang-Mills or curvature result','novelty priority for binomial expansion, monomial independence or coefficient shifts']};
}
module.exports={inAD,expressInU,observerFormulas,decodeBank,decodeDepth,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE38_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}
