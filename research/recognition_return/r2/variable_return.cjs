'use strict';
/** Exact depth-dependent native aperture return. The coefficients and targets
 * are declared data; the returned tail enclosure is not a full infinite inverse.
 */
const o=require('../../../operator_foundation/core/native_operator.cjs');
const r1=require('../return_solver.cjs');
const {F}=o;
const zero=()=>new F(0),one=()=>new F(1);
function positive(x,name){x=F.of(x);if(x.n<=0n)throw new RangeError(name+' must be a positive exact radial scalar');return x;}
function nonnegative(x,name){x=F.of(x);if(x.n<0n)throw new RangeError(name+' must be nonnegative');return x;}
function natural(x,name){if(!Number.isSafeInteger(x)||x<1)throw new RangeError(name+' must be a positive safe integer');return x;}
function cells(xs){if(!Array.isArray(xs)||xs.length<1||xs.length>8192)throw new RangeError('Supply between 1 and 8192 positive paired cells');return xs.map((x,i)=>positive(x,'cell '+i));}
function step(a,x){a=positive(a,'paired coupling');x=nonnegative(x,'tail response');return a.div(one().add(a.mul(x)));}
function fromTail(xs,tail=0){xs=cells(xs);let x=nonnegative(tail,'tail response');for(let j=xs.length-1;j>=0;j--)x=step(xs[j],x);return x;}
function transfer(xs){xs=cells(xs);let A=one(),B=zero(),C=zero(),D=one();for(const a of xs){const r=one().div(a);[A,B,C,D]=[B,A.add(B.mul(r)),D,C.add(D.mul(r))];}return {A,B,C,D,count:xs.length};}
function endpoints(P){const x=P.B.div(P.D),y=P.A.div(P.C),lower=x.le(y)?x:y,upper=x.le(y)?y:x;const width=upper.sub(lower);if(!width.eq(one().div(P.C.mul(P.D))))throw new Error('Exact tail-width determinant identity failed');return {lower,upper,width,midpoint:lower.add(upper).div(2),error:width.div(2),zeroTail:x,infiniteTailEndpoint:y};}
function enclose(xs){xs=cells(xs);const P=transfer(xs),interval=endpoints(P),max=xs.reduce((a,b)=>a.le(b)?b:a),uniformBound=max.div(Math.ceil(xs.length/2));if(!interval.width.le(uniformBound))throw new Error('Uniform cutoff bound failed');return {protocol:'RKF_PAIRED_APERTURE_TAIL_R2',cells:xs.map(String),apertureHeight:2*xs.length,transfer:P,interval,uniform_width_bound:uniformBound,scope:'Encloses every finite nonnegative scalar tail at this prefix; does not infer infinite-profile convergence from finite data'};}
function pairResponse(leftProduct,rightProduct,{u=1,v=0}={}){
 const p=positive(leftProduct,'left edge product'),q=positive(rightProduct,'right edge product');u=F.of(u);v=F.of(v);
 const s=one().add(q.mul(v)),r=p.sub(q.mul(u)),delta=s.pow(2).sub(r.pow(2));if(delta.zero())throw new RangeError('Singular native paired Schur block');
 const outU=one().add(p.mul(r).div(delta)),outV=p.mul(s).div(delta);
 return {u:outU,v:outV,schur:{scalar:s,turn:r,determinant:delta},unitChannelPreserved:outU.eq(1)};
}
function pairWitness(p,q,tail={u:1,v:0}){
 const result=pairResponse(p,q,tail),P=r1.emk(),I=P.one(),R=P.word(['R']),K=P.word(['K']),L=r1.normal(K.times(R));
 const B0=R,C0=K.scale(p),B1=R,C1=K.scale(q),U=I.scale(F.of(tail.u??1)).plus(L.scale(F.of(tail.v??0)));
 const S=r1.normal(I.minus(C1.times(U).times(B1)).minus(B0.times(C0)));
 const declared=I.scale(result.schur.scalar).plus(L.scale(result.schur.turn));
 const inverse=I.scale(result.schur.scalar).minus(L.scale(result.schur.turn)).scale(one().div(result.schur.determinant));
 const actual=I.plus(C0.times(inverse).times(B0)),expected=I.scale(result.u).plus(L.scale(result.v));
 const claims={schur:S.minus(declared),leftInverse:inverse.times(S).minus(I),rightInverse:S.times(inverse).minus(I),response:actual.minus(expected)};
 const proofs={};for(const [name,expr] of Object.entries(claims)){const reduced=P.reduce(expr,{witness:true});if(reduced.normal.terms.size)throw new Error('Native pair identity failed: '+name);P.replay(reduced.certificate);proofs[name]=reduced.certificate;}
 return {presentation:P.spec(),presentation_sha256:P.hash(),result,proofs};
}
function pairedCellsFromBonds(bonds){if(!Array.isArray(bonds)||!bonds.length||bonds.length%2)throw new RangeError('An even nonzero edge count is required');const products=bonds.map((e,i)=>positive(e.opening,'opening '+i).mul(positive(e.closing,'closing '+i))),out=[];for(let j=0;j<products.length;j+=2){if(!products[j].eq(products[j+1]))throw new RangeError('Pair-balance fails at cell '+j/2);out.push(products[j]);}return out;}
function periodTwoResidual(a,b,x){a=positive(a,'period A');b=positive(b,'period B');x=nonnegative(x,'candidate return');return b.mul(x.pow(2)).add(x).sub(a);}
function synthesize(desired,b=2){const x=positive(desired,'desired scalar return'),B=positive(b,'free positive cell parameter'),A=x.add(B.mul(x.pow(2))),y=B.div(one().add(B.mul(x)));if(!step(A,y).eq(x)||!step(B,x).eq(y))throw new Error('Synthesized periodic return does not close');return {protocol:'RKF_NATIVE_RETURN_SYNTHESIS_R2',period:[A,B],desiredReturn:x,otherBoundaryReturn:y,normalizedCutDefect:x.pow(2).sub(1).div(4),exactNativeCut:x.eq(1),condition:'a = x + b*x^2; exact normalized idempotent when x=1, equivalently a=b+1',scope:'Designed positive depth-periodic family; no physical coupling law is inferred'};}
function synthesizePattern(targets){const xs=cells(targets),out=xs.map((x,j)=>{const next=xs[(j+1)%xs.length],gap=one().sub(x.mul(next));if(gap.n<=0n)throw new RangeError('Adjacent target product, including periodic wrap, must be below one');return x.div(gap);});out.forEach((a,j)=>{if(!step(a,xs[(j+1)%xs.length]).eq(xs[j]))throw new Error('Designed profile failed its native equation');});return {protocol:'RKF_NATIVE_PROFILE_SYNTHESIS_R2',targets:xs,period:out,cutPhases:xs.map((x,j)=>x.eq(1)?j:null).filter(x=>x!==null),scope:'Exact positive periodic response design under every adjacent product <1; no physical-source uniqueness claim'};}
function solvePeriodic({pattern=['3','2'],tolerance='1/1000000000000',maxCells=2048}={}){
 const pat=cells(pattern),tol=positive(tolerance,'tolerance');natural(maxCells,'maxCells');if(maxCells>8192)throw new RangeError('Declared allocation budget exceeded');
 let A=one(),B=zero(),C=zero(),D=one(),r,packet;const used=[];
 for(let k=0;k<maxCells;k++){const a=pat[k%pat.length];used.push(a);r=one().div(a);[A,B,C,D]=[B,A.add(B.mul(r)),D,C.add(D.mul(r))];packet=endpoints({A,B,C,D});if(packet.error.le(tol))break;}
 return {protocol:'RKF_PERIODIC_NATIVE_RETURN_R2',status:packet.error.le(tol)?'CERTIFIED_RECOGNITION_RESPONSE':'REFINEMENT_BUDGET_EXHAUSTED',input:{pattern:pat.map(String),tolerance:tol.toString(),maxCells},cellsUsed:used.length,apertureHeight:2*used.length,interval:packet,normalResponse:{identity:'1',RK:packet.midpoint.neg()},response_mass_error:packet.error,convergence_contract:'Positive periodic profile is bounded, so sum(1/a_j) diverges; tail-independent aperture limit is proved',global_inverse_claimed:false,physical_identification:false};
}
function persistentSquareWitness(count){natural(count,'count');if(count>2048)throw new RangeError('Witness allocation budget exceeded');const profile=Array.from({length:count},(_,j)=>new F(4).mul(new F(j+1).pow(2))),out=enclose(profile),lowerBound=new F(1,4);if(!lowerBound.le(out.interval.width))throw new Error('Persistent boundary width bound violated');return {...out,infinite_profile:'a_j=4(j+1)^2, j>=0',reciprocal_sum_upper_bound:new F(1,2),all_depths_width_lower_bound:lowerBound,verdict:'TWO_DISTINCT_APERTURE_SUBLIMITS',proof_contract:'Telescoping comparison bounds sum(1/a_j)<=1/2; normalized continuant denominators <=2 at all depths'};}
function prefixEnclosure(prefix,tailLower,tailUpper){prefix=cells(prefix);const lo=nonnegative(tailLower,'lower'),hi=nonnegative(tailUpper,'upper');if(!lo.le(hi))throw new RangeError('Ordered tail interval required');const a=fromTail(prefix,lo),b=fromTail(prefix,hi),lower=a.le(b)?a:b,upper=a.le(b)?b:a;return {lower,upper,width:upper.sub(lower),midpoint:lower.add(upper).div(2),error:upper.sub(lower).div(2)};}
function balancedDefectEnclosure(ratios,q,tailDepth){ratios=cells(ratios);q=positive(q,'background coupling');natural(tailDepth,'tailDepth');const background=r1.bracket(q,tailDepth),out=prefixEnclosure(ratios.map(r=>r.mul(q)),background.lower,background.upper);return {...out,ratios:ratios.map(String),backgroundCoupling:q,tailDepth,cut_error_bound:(out.lower.sub(1).abs().le(out.upper.sub(1).abs())?out.upper.sub(1).abs():out.lower.sub(1).abs()).div(2)};}
function recoverProducts(u,v,tailV=0){u=F.of(u);v=F.of(v);const x=nonnegative(tailV,'known unit-channel tail');if(v.zero())throw new RangeError('Nonzero return channel required');const w=u.sub(1).div(v),alpha=v.mul(one().sub(w.pow(2))),beta=alpha.sub(w),den=one().sub(beta.mul(x));if(den.zero())throw new RangeError('Degenerate source reconstruction');const p=positive(alpha.div(den),'recovered left product'),q=positive(beta.div(den),'recovered right product'),roundtrip=pairResponse(p,q,{u:1,v:x});if(!roundtrip.u.eq(u)||!roundtrip.v.eq(v))throw new Error('Recovered source products failed roundtrip');return {leftProduct:p,rightProduct:q,individual_directional_amplitudes_recovered:false};}
module.exports={step,fromTail,transfer,enclose,pairResponse,pairWitness,pairedCellsFromBonds,periodTwoResidual,synthesize,synthesizePattern,solvePeriodic,persistentSquareWitness,prefixEnclosure,balancedDefectEnclosure,recoverProducts};
if(require.main===module)console.log(JSON.stringify({finiteCouplingCut:synthesize(1,2),certifiedCutResponse:solvePeriodic(),persistentBoundaryMemory:persistentSquareWitness(20)},null,2));
