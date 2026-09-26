'use strict';
/** Native graded-aperture response. Uses the canonical cut arithmetic/compiler.
 * No square-root evaluation, Hilbert norm, or fitted matrix is a solver input.
 */
const {F,Cut}=require('../../operator_foundation/core/native_operator.cjs');
const {Presentation}=require('../../operator_foundation/core/paninian_operator.cjs');
function nonnegative(x,name){x=F.of(x);if(!new F(0).le(x))throw new RangeError(name+' must be a nonnegative exact radial scalar');return x;}
function index(n,name){if(!Number.isSafeInteger(n)||n<0)throw new RangeError(name+' must be a nonnegative safe integer');return n;}
function emk(){return new Presentation({tokens:['R','K'],rules:[
 {id:'RR',lhs:['R','R'],rhs:[[[],-1]],source:'RKF T48/T55: R squared'},
 {id:'KK',lhs:['K','K'],rhs:[[[],1]],source:'RKF T48/T55: K squared'},
 {id:'KR',lhs:['K','R'],rhs:[[['R','K'],-1]],source:'RKF T48/T55: anticommutation'}]});}
const normal=e=>e.system.reduce(e).normal;
function product(...xs){return xs.reduce((a,b)=>normal(a.times(b)));}
function mass(e){return normal(e).entries().reduce((s,[,c])=>s.add(c.gauge()),new F(0));}
function identityProof(p,expr){const r=p.reduce(expr,{witness:true});if(r.normal.terms.size)throw new Error('Required native identity does not close');p.replay(r.certificate);return r.certificate;}
function certifyRelations(p,B,C){
 if(p.objects.length!==1||B.system!==p||C.system!==p)throw new TypeError('One declared coefficient object is required');
 if(p.audit().status!=='CONFLUENT_BY_CHECKED_DIAMONDS')throw new Error('Uncertified coefficient presentation');
 const X=product(C,B),proof=identityProof(p,B.times(C).plus(C.times(B)));
 return {X,anticommutator:proof};
}
function catalan(n){index(n,'Catalan index');let c=1n;for(let k=0;k<n;k++)c=c*BigInt(4*k+2)/BigInt(k+2);return new F(c);}
function firstReturnCoefficients(p,B,C,order){
 index(order,'Coefficient order');if(order>120)throw new RangeError('Declared coefficient budget exceeded');
 const a=[p.one()];for(let n=1;n<=order;n++){let s=p.zero();for(let j=0;j<n;j++)s=s.plus(product(C,a[j],B,a[n-1-j]));a.push(normal(s));}return a;
}
function anticommutingCoefficient(p,X,n){index(n,'Coefficient index');if(n===0)return p.one();if(n%2===0)return p.zero();let a=p.one();for(let k=0;k<n;k++)a=product(a,X);return a.scale(catalan((n-1)/2).mul((n-1)%4===0?1:-1));}
function gradedContract(b,c){
 b=nonnegative(b,'opening amplitude');c=nonnegative(c,'return amplitude');const p=emk(),R=p.word(['R']),K=p.word(['K']),L=normal(K.times(R));
 const B=R.scale(b),C=K.scale(c),q=b.mul(c),checked=certifyRelations(p,B,C);
 const witnesses={...checked,cutSquare:identityProof(p,L.times(L).minus(p.one())),
  feedback:identityProof(p,C.times(L).times(B).plus(p.one().scale(q)))};
 return {p,R,K,L,B,C,q,b,c,witnesses};
}
function iterate(q,x){q=nonnegative(q,'coupling');x=nonnegative(x,'boundary response');return q.div(new F(1).add(q.mul(x)));}
function bracket(q,k){
 q=nonnegative(q,'coupling');index(k,'refinement depth');if(k>10000)throw new RangeError('Refinement budget exceeded');
 let a=new F(0);for(let j=0;j<k;j++)a=iterate(q,a);const b=iterate(q,a);
 const lo=a.le(b)?a:b,hi=a.le(b)?b:a;
 return {depth:k,aperture_heights:[2*k,2*k+2],left:a,right:b,lower:lo,upper:hi,width:hi.sub(lo),estimate:lo.add(hi).div(2),error:hi.sub(lo).div(2)};
}
function continueFrom(q,seed,k){q=nonnegative(q,'coupling');seed=nonnegative(seed,'boundary response');index(k,'refinement depth');let d=seed;for(let j=0;j<k;j++)d=iterate(q,d);return d;}
function solve({opening='2',closing='3/5',tolerance='1/1000000000000',maxRefinements=1000}={}){
 const model=gradedContract(opening,closing),tol=nonnegative(tolerance,'tolerance');if(tol.zero())throw new RangeError('Positive tolerance required');index(maxRefinements,'refinement budget');
 let a=new F(0),b=iterate(model.q,a),k=0;
 while(b.sub(a).abs().div(2).le(tol)===false&&k<maxRefinements){a=b;b=iterate(model.q,b);k++;}
 const packet=bracket(model.q,k),enclosed=packet.error.le(tol),response=normal(model.p.one().plus(model.L.scale(packet.estimate)));
 return {protocol:'RKF_GRADED_APERTURE_RESPONSE_R1',status:enclosed?'CERTIFIED_RECOGNITION_RESPONSE':'REFINEMENT_BUDGET_EXHAUSTED',
  input:{opening:model.b.toString(),closing:model.c.toString(),tolerance:tol.toString(),maxRefinements},
  q:model.q.toString(),presentation:model.p.spec(),presentation_sha256:model.p.hash(),native_witnesses:model.witnesses,
  bracket:packet,response:response.toJSON(),response_mass_error_bound:packet.error,
  domain:{coefficient_algebra:'EMK: R^2=-1, K^2=1, KR=-RK',memory:'half-line stack, TS=1, ST is not 1',
   aperture_sequence:'heights 0,2,4,...; finite inverses, then recognized boundary block',
   boundary_class:'finite nonnegative radial seeds under d -> q/(1+q d)',q_range:'all finite nonnegative radial q',
   primitive_hilbert_space:false,global_inverse_or_state_convergence_claimed:false,physical_identification:false},
  series_comparison:{whole_neumann_sufficient_gate: model.b.add(model.c).le(1)&&!model.b.add(model.c).eq(1),
   generic_unsigned_catalan_sufficient_gate:model.q.mul(4).le(1)&&!model.q.mul(4).eq(1),
   paired_return_strict_radius_gate:model.q.mul(model.q).mul(4).le(1)&&!model.q.mul(model.q).mul(4).eq(1)}};
}
function emergentCutBound(q,k){
 q=nonnegative(q,'coupling');index(k,'refinement depth');
 if(q.zero()||k===0)throw new RangeError('Positive coupling and refinement depth required');
 return {toLimitingResponse:new F(2).mul(q).div(k),toStrongCouplingAperture:q.div(k).add(new F(1).div(q.mul(4))),normalization:'P_k=(I+d_k KR)/2'};
}
function checkRationalRoot(q,d){q=nonnegative(q,'coupling');d=nonnegative(d,'candidate response');return d.le(1)&&d.eq(q.mul(new F(1).sub(d.mul(d))));}
function pairedTail(p,X,terms){index(terms,'retained Catalan terms');const u=mass(X),ratio=u.mul(u).mul(4);if(!ratio.le(1)||ratio.eq(1))return {status:'OUTSIDE_STRICT_RETURN_SERIES_GATE',ratio};
 const tail=catalan(terms).mul(u.pow(2*terms+1)).div(new F(1).sub(ratio));return {status:'CERTIFIED_ABSOLUTE_TAIL',ratio,bound:tail};}
module.exports={emk,normal,product,mass,catalan,certifyRelations,firstReturnCoefficients,anticommutingCoefficient,gradedContract,iterate,bracket,continueFrom,solve,checkRationalRoot,pairedTail,emergentCutBound};
if(require.main===module){console.log(JSON.stringify(solve(),null,2));}
