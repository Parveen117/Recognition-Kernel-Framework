'use strict';
/**
 * Structure report R3: cut split -> observer completion -> returning-memory mark -> cut-square factorization.
 *
 * Consumes operator_foundation/core/native_operator.cjs unchanged. Exact cut scalars (rad, turn) only.
 * Sources: 01_NATIVE_ALGEBRA N01 (cut grading), N03 (minimum future-complete observation),
 * N06 (compression defect = returning memory); theorum/53 (native cut-square factorization);
 * theorum/76 (seam count n_+(M - mu B) reading). Proofs of the new statements R3-A..R3-D are in THEOREM.md.
 *
 * No primitive Hilbert space: the only positivity used is the native norm N(z)=rad^2+turn^2 (F00-E) and
 * square-sourced forms a^dagger a. The dagger is the native path reversal, never a coordinate transpose.
 */
const o=require('../../operator_foundation/core/native_operator.cjs');
const {F,Cut,ZERO,ONE,matrix,zeros,identity,add,sub,scale,mul,dagger,equal,mass,energy,isZero,rref,rank,inverse,rowClosure,descendedAction}=o;

function square(a){a=matrix(a);if(a.length!==a[0].length)throw new RangeError('Square matrix required');return a;}
function isSelfDagger(a){return equal(a,dagger(a));}
function transposeOnly(a){a=matrix(a);return a[0].map((_,j)=>a.map(r=>r[j]));}
function trace(a){a=square(a);return a.reduce((s,r,i)=>s.add(r[i]),ZERO);}
function turnFree(x){return x.turn.zero();}

/** Independent determinant route (row elimination), used only as a cross-check of the weight product. */
function determinant(a){a=square(a).map(r=>r.slice());let d=ONE;const n=a.length;for(let j=0;j<n;j++){let k=j;while(k<n&&a[k][j].zero())k++;if(k===n)return ZERO;if(k!==j){[a[k],a[j]]=[a[j],a[k]];d=d.neg();}const p=a[j][j];d=d.mul(p);for(let i=j+1;i<n;i++){const q=a[i][j].div(p);if(q.zero())continue;for(let t=j;t<n;t++)a[i][t]=a[i][t].sub(q.mul(a[j][t]));}}return d;}

/** Admitted cut: J = J^dagger = J^-1 (N01). */
function admittedCut(J){J=square(J);if(!isSelfDagger(J))throw new RangeError('Cut must be self-dagger');if(!equal(mul(J,J),identity(J.length)))throw new RangeError('Cut must square to the identity');return J;}
function cutSplit(s,J){s=square(s);const c=mul(mul(J,s),J);return {even:scale(add(s,c),'1/2'),odd:scale(sub(s,c),'1/2')};}

/** Self-dagger retained projector P = D^dagger (D D^dagger)^-1 D onto the completed observer's recovered sector. */
function retainedProjector(D){D=matrix(D);if(rref(D).rank!==D.length)throw new RangeError('Completed observer must have independent rows');const Dd=dagger(D),G=mul(D,Dd);const P=mul(mul(Dd,inverse(G)),D);return {P,gram:G};}
function compress(P,a){return mul(mul(P,a),P);}

/** All words of length <= L over the catalogue (as matrices), with their letter strings. */
function words(gens,L){const n=gens[0].m.length;let layer=[{word:[],m:identity(n)}];const out=[...layer];for(let l=1;l<=L;l++){layer=layer.flatMap(w=>gens.map(g=>({word:w.word.concat(g.name),m:mul(w.m,g.m)})));out.push(...layer);}return out;}

/**
 * theorum/53 shape: exact congruence S = C^dagger Dg C with turn-free weights, no square root, no eigenvalue.
 * Elimination with native scalar inverses; symmetric pivot search keeps the congruence exact when a diagonal
 * pivot vanishes (u = e_i + c e_j with c = S_ij^dagger makes 2 N(S_ij) > 0 appear on the diagonal).
 * Returns weights, rank, inertia (n_plus, n_zero, n_minus), the transform T (so that T S T^dagger = diag),
 * and a negative witness vector when a negative weight appears (T3 shape).
 */
function congruenceDiagonalize(S){S=square(S);if(!isSelfDagger(S))throw new RangeError('Self-dagger form required');const n=S.length;let A=S.map(r=>r.slice()),T=identity(n);
  const applyRowOp=(ops)=>{ // ops: function mutating a row-operation matrix E (n x n) ; A <- E A E^dagger ; T <- E T
    const E=identity(n);ops(E);A=mul(mul(E,A),dagger(E));T=mul(E,T);};
  for(let k=0;k<n;k++){
    if(A[k][k].zero()){
      let j=-1;for(let t=k+1;t<n;t++)if(!A[t][t].zero()){j=t;break;}
      if(j>=0){applyRowOp(E=>{E[k][k]=ZERO;E[j][j]=ZERO;E[k][j]=ONE;E[j][k]=ONE;});}
      else{let t=-1;for(let u=k+1;u<n;u++)if(!A[k][u].zero()){t=u;break;}
        if(t<0){continue;} // zero row and zero pivot: weight 0
        const c=A[k][t];applyRowOp(E=>{E[k][t]=c;});} // new pivot = A_kt c^dagger + c A_tk = 2 N(A_kt) > 0
    }
    const p=A[k][k];if(!turnFree(p))throw new Error('Pivot of a self-dagger form must be turn-free');
    for(let i=k+1;i<n;i++){if(A[i][k].zero())continue;const q=A[i][k].div(p).neg();applyRowOp(E=>{E[i][k]=q;});}
  }
  const weights=A.map((r,i)=>r[i]);
  if(!A.every((r,i)=>r.every((x,j)=>i===j||x.zero())))throw new Error('Congruence did not diagonalize');
  const sgn=w=>w.rad.n>0n?1:w.rad.n<0n?-1:0;
  const inertia={n_plus:weights.filter(w=>sgn(w)>0).length,n_zero:weights.filter(w=>sgn(w)===0).length,n_minus:weights.filter(w=>sgn(w)<0).length};
  let witness=null;const neg=weights.findIndex(w=>sgn(w)<0);
  if(neg>=0){ // v = T^dagger e_neg gives v^dagger S v = weight_neg < 0
    const v=dagger(T).map(r=>[r[neg]]);const value=mul(mul(dagger(v),S),v)[0][0];if(!value.eq(weights[neg]))throw new Error('Negative witness must reproduce its weight');witness={vector:v.map(r=>r[0]),value:value};}
  const product=weights.reduce((a,w)=>a.mul(w),ONE);
  return {weights,rank:n-inertia.n_zero,inertia,transform:T,witness,weight_product:product};
}

/** theorum/53 factorization of a cut square S (all weights must be turn-free and nonnegative). */
function cutSquareFactorization(S){const f=congruenceDiagonalize(S);if(f.inertia.n_minus>0)return {status:'NOT_A_CUT_SQUARE',...f};
  // Native Parseval (T53 T2): tr rad(S) = sum_k d_k E(c_k) with S = C^dagger Dg C, C = (T^-1)^dagger rows ... we verify tr rad(S) = sum weights * E(c_k) using C = dagger(inverse(T)).
  // T S T^dagger = Dg, so S = T^-1 Dg (T^-1)^dagger = C^dagger Dg C with C = (T^-1)^dagger; rows c_k of C give S = sum_k d_k c_k^dagger c_k.
  const c=dagger(inverse(f.transform));const rebuilt=c.reduce((acc,row,k)=>add(acc,scale(mul(dagger([row]),[row]),f.weights[k])),zeros(S.length));
  if(!equal(rebuilt,S))throw new Error('Weighted squares must rebuild the form exactly');
  const parsevalLeft=trace(S).rad,parsevalRight=c.reduce((acc,row,k)=>acc.add(f.weights[k].rad.mul(energy([row]))),new F(0));
  if(!parsevalLeft.eq(parsevalRight))throw new Error('Native Parseval failed');
  return {status:'CUT_SQUARE',weights:f.weights,rank:f.rank,inertia:f.inertia,factors:c,parseval:parsevalLeft,weight_product:f.weight_product};}

/**
 * The structure report. Input: catalogue {name: matrix}, observer rows, optional target rows, optional cut J,
 * optional threshold list for the seam-count reading, optional word length for the multiplicativity census.
 */
function structureReport(job){
  const names=Object.keys(job.catalogue||{});if(!names.length)throw new RangeError('A nonempty action catalogue is required');
  const gens=names.map(name=>({name,m:square(job.catalogue[name])}));const n=gens[0].m.length;gens.forEach(g=>{if(g.m.length!==n)throw new RangeError('Catalogue carrier mismatch');});
  const C=matrix(job.observer);if(C[0].length!==n)throw new RangeError('Observer must act on the carrier');
  const L=job.target===undefined?[]:matrix(job.target);if(L.length&&L[0].length!==n)throw new RangeError('Target must act on the carrier');
  const wordLength=job.word_length===undefined?3:job.word_length;const thresholds=(job.thresholds||[]).map(F.of);
  const report={protocol:'RKF_STRUCTURE_REPORT_R3',carrier:{dimension:n,field:'cut-complex (rad,turn)',generators:names}};

  // Stage 1: cut grading (N01). Declared data; absent cut means no grading stage.
  let J=null;if(job.cut!==undefined){J=admittedCut(job.cut);report.cut={admitted:true,generators:{}};
    for(const g of gens){const sp=cutSplit(g.m,J);if(!equal(mul(mul(J,sp.even),J),sp.even)||!equal(mul(mul(J,sp.odd),J),scale(sp.odd,-1))||!equal(add(sp.even,sp.odd),g.m))throw new Error('Cut grading identities failed');
      g.even=sp.even;g.odd=sp.odd;report.cut.generators[g.name]={even_mass:mass(sp.even),odd_mass:mass(sp.odd),purely_even:isZero(sp.odd),purely_odd:isZero(sp.even)};}}

  // Stage 2: observer completion (N03): forward, then with the reversed catalogue.
  const seed=C.concat(L),forward=rowClosure(seed,gens.map(g=>g.m)),withDagger=rowClosure(seed,gens.map(g=>g.m),{includeDagger:true});
  const D=forward.rank?forward.observer:null;if(!D)throw new RangeError('Observer of rank zero sees nothing; nothing to report');
  const descended=gens.map(g=>descendedAction(g.m,D));if(descended.some(a=>a===null))throw new Error('Forward action did not descend (N03 violated)');
  report.observer={initial_rank:rank(C),seed_rank:rank(seed),forward_rank:forward.rank,forward_extra:forward.rank-rank(C),forward_ladder:forward.ranks,dagger_rank:withDagger.rank,dagger_extra:withDagger.rank-forward.rank,completed_observer:D};

  // Stage 3: the mark (N06 on the completed observer).
  const {P,gram}=retainedProjector(D),Q=sub(identity(n),P);
  if(!equal(mul(P,P),P)||!isSelfDagger(P))throw new Error('Retained projector must be a self-dagger idempotent');
  const forwardLeakZero=gens.every(g=>isZero(mul(mul(P,g.m),Q)));if(!forwardLeakZero)throw new Error('R3-A failed: completed observer must satisfy P s Q = 0');
  if(rank(P)!==forward.rank||!isZero(mul(D,Q)))throw new Error('ker P must equal ker D');
  const W=words(gens,wordLength);let multiplicative=0;for(const a of W)for(const b of W){if(!equal(compress(P,mul(a.m,b.m)),mul(compress(P,a.m),compress(P,b.m))))throw new Error('R3-A failed on forward words '+a.word.join('')+'|'+b.word.join(''));multiplicative++;}
  const marks={};let K=zeros(n);let anyLeak=false;
  for(const g of gens){const leak=mul(mul(Q,g.m),P);const sq=mul(dagger(leak),leak);
    const defect=sub(compress(P,mul(dagger(g.m),g.m)),mul(compress(P,dagger(g.m)),compress(P,g.m)));
    if(!equal(defect,sq))throw new Error('N06 identity failed for '+g.name);
    const entry={leak_mass:mass(leak),leak_energy:energy(leak),defect_trace_rad:trace(sq).rad,zero:isZero(leak)};
    if(!entry.defect_trace_rad.eq(entry.leak_energy))throw new Error('Native Parseval failed on the mark');
    if(J){const le=mul(mul(Q,g.even),P),lo=mul(mul(Q,g.odd),P);if(!equal(add(le,lo),leak))throw new Error('Leak must split along the cut');entry.even_leak_mass=mass(le);entry.odd_leak_mass=mass(lo);}
    if(!entry.zero)anyLeak=true;marks[g.name]=entry;K=add(K,sq);}
  report.returning_memory={generators:marks,any:anyLeak,form_supported_on_retained_sector:isZero(mul(K,Q))&&isZero(mul(Q,K))};
  // R3-B cross route: leak vanishes for every generator iff the dagger completion adds nothing.
  const commutes=gens.every(g=>equal(mul(P,g.m),mul(g.m,P))&&equal(mul(P,dagger(g.m)),mul(dagger(g.m),P)));
  report.returning_memory.cross_route={leak_free:!anyLeak,projector_commutes_with_catalogue:commutes,dagger_extra_zero:report.observer.dagger_extra===0};
  if(!((!anyLeak)===commutes&&commutes===(report.observer.dagger_extra===0)))throw new Error('R3-B routes disagree');
  if(J){const face=equal(P,scale(add(identity(n),J),'1/2'));report.returning_memory.cut_aligned_observer=face;if(face){for(const g of gens)if(!isZero(mul(mul(Q,g.even),P)))throw new Error('R3-D failed: even generator leaked from a cut face');}}

  // Stage 4: cut-square factorization of the returning-memory form (theorum/53) and seam-count reading (theorum/76 shape).
  const fac=cutSquareFactorization(K);if(fac.status!=='CUT_SQUARE')throw new Error('Returning-memory form must be a cut square');
  const detRoute=determinant(K);if(!detRoute.eq(fac.weight_product))throw new Error('Weight product must equal the determinant channel');
  report.returning_memory_form={rank:fac.rank,weights:fac.weights,inertia:fac.inertia,parseval_trace:fac.parseval,sum_of_leak_energies:gens.reduce((a,g)=>a.add(marks[g.name].leak_energy),new F(0)),weight_product_equals_determinant:true};
  if(!report.returning_memory_form.parseval_trace.eq(report.returning_memory_form.sum_of_leak_energies))throw new Error('Trace of the form must equal the total returning energy');
  if(thresholds.length){let prev=null;report.seam_count_reading=thresholds.map(mu=>{const r=congruenceDiagonalize(sub(K,scale(P,new Cut(mu))));if(prev!==null&&r.inertia.n_plus>prev)throw new Error('Seam count must be non-increasing in the threshold');prev=r.inertia.n_plus;return {threshold:mu,n_plus:r.inertia.n_plus,n_zero:r.inertia.n_zero,n_minus:r.inertia.n_minus};});}

  // Verdict (trichotomy of THEOREM.md).
  report.verdict=!anyLeak?(report.observer.forward_extra===0?'VISIBLE_LOCAL':'HIDDEN_LOCAL'):'GLOBAL_RETURNING_MEMORY';
  report.census={forward_word_pairs_multiplicative:multiplicative,word_length:wordLength};
  report.scope={finite_declared_carrier:true,encoding_is_supplied_data:true,primitive_hilbert_space:false,dagger_is_native_reversal_not_transpose:true,infinite_limit_invoked:false};
  return report;
}

module.exports={structureReport,congruenceDiagonalize,cutSquareFactorization,retainedProjector,cutSplit,admittedCut,compress,words,determinant,transposeOnly,trace};
