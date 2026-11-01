'use strict';
// SE31 application of the unchanged canonical symbolic/coefficient engines.
// All normal forms and formal-series products are delegated to that engine.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const l=require('../operator_foundation/core/native_laurent.cjs');
const m=require('../operator_foundation/core/paninian_operator.cjs');
const c=require('./endpoint_lambda_counting.cjs');
const {F,Cut}=o;
const root=path.resolve(__dirname,'..');
const dev=path.join(root,'papers/rkf_completed_weil_endpoint/development');
const resultPath=path.join(__dirname,'ENDPOINT_COUNTING_OPERATOR_RECOVERY_RESULT.json');
const S=new m.Presentation({tokens:['L','X','D'],rules:[
  {id:'XL',lhs:['X','L'],rhs:[[['L','X'],1]],source:'SE30 constant unit: Lambda commutes with X'},
  {id:'DL',lhs:['D','L'],rhs:[[['L','D'],1]],source:'SE30 constant unit: Lambda commutes with D'},
  {id:'DX',lhs:['D','X'],rhs:[[['X','D'],1],[[],1]],source:'SE30 Theorem 4: [D,X]=I on the counting basis'}
]});
const nf=e=>S.reduce(e).normal;
const W=(i,j,d=0,v=1)=>S.word([...Array(d).fill('L'),...Array(i).fill('X'),...Array(j).fill('D')],v);
const D=W(0,1),X=W(1,0),I=S.one();
const mono=(v,k)=>l.monomial([[Cut.of(v)]],k);
const empty=()=>l.series([],1); // additive-neutral polynomial, not the named cut
const scale=(p,v)=>l.times(p,mono(v,0));
const sub=(a,b)=>l.plus(a,scale(b,-1));
const eq=l.equalSeries;
const degree=p=>Math.max(-1,...p.terms.keys());
const factorial=n=>{let v=1n;for(let k=1;k<=n;k++)v*=BigInt(k);return v;};
const descending=(n,k)=>k>n?0n:factorial(n)/factorial(n-k);
const choose=(n,k)=>k>n?0n:descending(n,k)/factorial(k);
function indices(w){return {i:w.filter(t=>t==='X').length,j:w.filter(t=>t==='D').length,d:w.filter(t=>t==='L').length};}
function actWord(w,p,h){let out=p;for(const t of [...w].reverse())out=t==='D'?c.delta(out,h):t==='X'?c.raise(out,h):scale(out,h);return out;}
function action(e,p,h){let out=empty();for(const [w,v]of e.entries())out=l.plus(out,scale(actWord(w,p,h),v));return out;}
function coefficients(e,h,r){const out=Array.from({length:r+1},empty);for(const [w,v]of nf(e).entries()){const {i,j,d}=indices(w);assert(j<=r);out[j]=l.plus(out[j],mono(v.mul(F.of(h).pow(d)),i));}return out;}
function recover(responses,h){
  if(!responses.length)throw new RangeError('A nonempty complete response prefix is required');
  const a=[];
  responses.forEach((response,k)=>{let rem=c.untransform(response,h);for(let j=0;j<k;j++)rem=sub(rem,scale(l.times(a[j],mono(1,k-j)),descending(k,j)));a.push(scale(rem,new F(1n,factorial(k))));});
  return a;
}
function recoverCountingChart(responses,h){const a=[];responses.forEach((response,k)=>{let rem=response;for(let j=0;j<k;j++)rem=sub(rem,scale(c.bullet(a[j],c.falling(k-j,h),h),descending(k,j)));a.push(scale(rem,new F(1n,factorial(k))));});return a;}
function fromCoefficients(a){let out=S.zero();a.forEach((p,j)=>{for(const [i,v]of p.terms)out=out.plus(W(i,j,0,v[0][0]));});return out;}
function memory(e,q){if(!Number.isSafeInteger(q)||q<0)throw new RangeError('A nonnegative memory depth is required');return new m.Expr(S,'*','*',nf(e).entries().filter(([w])=>indices(w).d<=q));}
function layer(e,d){return new m.Expr(S,'*','*',nf(e).entries().filter(([w])=>indices(w).d===d).map(([w,v])=>[w.filter(t=>t!=='L'),v]));}
function recoverMemory(e,r,q){
  let out=S.zero();
  for(let d=0;d<=q;d++){
    // Responses expressed in U^{-1} coordinates. Zero here is the already
    // computed degree-zero coefficient adapter, never a Count unit erasure.
    const bank=Array.from({length:r+1},(_,k)=>action(layer(e,d),mono(1,k),0));
    const a=recover(bank,0);
    a.forEach((p,j)=>{for(const [i,v]of p.terms)out=out.plus(W(i,j,d,v[0][0]));});
  }
  return nf(out);
}
function decodeReadingPacket(packet){
  let out=S.zero();
  assert.equal(packet.readings.length,packet.retained_unit_degree+1);
  packet.readings.forEach((reading,d)=>{
    assert.equal(reading.unit_degree,d);assert.equal(reading.probes.length,packet.probe_order+1);
    const bank=reading.probes.map((probe,k)=>{assert.equal(probe.probe,k);return l.series(probe.polynomial.map(v=>[v.x_power,[[Cut.of(v.coefficient)]]]),1);});
    recover(bank,0).forEach((p,j)=>{for(const [i,v]of p.terms)out=out.plus(W(i,j,d,v[0][0]));});
  });
  return nf(out);
}
function readingPacket(e,r,q){
  const packet={rule:'Certification is the declared observer reading interpreted by its exact decoder',
    target:'The complete normal-ordered operator in the stated polynomial class',
    declared_class:{D_order_at_most:r,normal_coefficient_Lambda_degree_at_most:q},
    probe_order:r,retained_unit_degree:q,response_coordinates:'U^-1(A p_k), coefficient by coefficient in Lambda',
    readings:Array.from({length:q+1},(_,d)=>({unit_degree:d,probes:Array.from({length:r+1},(_,k)=>({probe:k,
      polynomial:[...action(layer(e,d),mono(1,k),0).terms].map(([power,v])=>({x_power:power,coefficient:v[0][0].toJSON()}))}))})),
    example_scope:'The supplied SE31 polynomial family; not the actual RH source'};
  const decoded=decodeReadingPacket(packet);
  return {...packet,decoded_operator:decoded.toJSON(),verdict:'COMPLETE_OPERATOR_READING_IN_DECLARED_CLASS'};
}
function evaluate(p,x){let out=Cut.of(0);for(const [k,v]of p.terms)out=out.add(v[0][0].mul(F.of(x).pow(k)));return out;}
function expLower(p,a,h){let out=empty(),term=p;for(let k=0;k<=degree(p);k++){out=l.plus(out,scale(term,F.of(a).pow(k).div(factorial(k))));term=c.delta(term,h);}return out;}
function translate(p,a){let out=empty(),term=p;for(let k=0;k<=degree(p);k++){out=l.plus(out,scale(term,F.of(a).pow(k).div(factorial(k))));term=l.derivative(term);}return out;}
function newtonTranslate(p,a,h){let out=empty(),term=p;for(let k=0;k<=degree(p);k++){out=l.plus(out,scale(term,evaluate(c.falling(k,h),a).div(factorial(k))));term=c.delta(term,h);}return out;}
function logGenerator(p,h){let out=empty(),term=p;for(let k=1;k<=degree(p);k++){term=c.delta(term,h);out=l.plus(out,scale(term,F.of(h).pow(k-1).mul(k%2?1:-1).div(k)));}return out;}
function window(N){const d=o.zeros(N+1),x=o.zeros(N+1);for(let k=1;k<=N;k++)d[k-1][k]=Cut.of(k);for(let k=0;k<N;k++)x[k+1][k]=Cut.of(1);return {D:d,X:x,L:o.identity(N+1)};}
function height(w){let running=0,high=0;for(const t of [...w].reverse()){running+=t==='X'?1:t==='D'?-1:0;high=Math.max(high,running);}return high;}
function* words(n,p=[]){yield p;if(n)for(const t of ['D','X'])yield* words(n-1,p.concat(t));}
function pinCheck(file){const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);return Object.keys(pins).length;}
function verify(){
  const inheritedPins=pinCheck(path.join(dev,'SE30_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const steps=['1/3',1,2,'-2/5'];
  check('canonical_normal_order_presentation_closes_all_critical_pairs',()=>{const a=S.audit();assert.equal(a.status,'CONFLUENT_BY_CHECKED_DIAMONDS');for(const z of a.resolutions){S.replay(z.left);S.replay(z.right);}details.normal_order={audit:a.status,critical_pairs:a.criticalPairs,presentation:S.spec()};});
  check('ordered_power_formula_matches_independent_canonical_rewrite',()=>{for(let j=0;j<=6;j++)for(let k=0;k<=6;k++){let expected=S.zero();for(let v=0;v<=Math.min(j,k);v++)expected=expected.plus(W(k-v,j-v,0,choose(j,v)*descending(k,v)));const proof=S.reduce(S.word([...Array(j).fill('D'),...Array(k).fill('X')]),{witness:true});assert(proof.normal.equals(expected));assert(S.replay(proof.certificate));}});
  check('word_action_and_normal_action_agree_on_SE30_polynomials',()=>{for(const w of words(5))for(const h of steps){const e=S.word(['L',...w]),p=l.plus(mono('3/7',6),mono(-2,2));assert(eq(action(e,p,h),action(nf(e),p,h)));}});
  check('incremental_probe_recovery_matches_all_declared_coefficients',()=>{
    for(let r=0;r<=5;r++)for(const h of steps){let A=S.zero();for(let j=0;j<=r;j++)A=A.plus(W(j%3,j,j%3,new F(j+1,j+2))).plus(W(0,j,0,-1));
      const bank=Array.from({length:r+1},(_,k)=>action(A,c.falling(k,h),h)),a=recover(bank,h),known=coefficients(A,h,r);
      a.forEach((p,j)=>assert(eq(p,known[j])));
      const native=recoverCountingChart(bank,h);native.forEach((p,j)=>assert(eq(p,c.transform(a[j],h))));
      for(let k=0;k<=r;k++){const partial=fromCoefficients(a.slice(0,k+1));for(let n=0;n<=k;n++)assert(eq(action(partial,c.falling(n,h),h),bank[n]));}
      for(const n of [r+1,r+3])assert(eq(action(fromCoefficients(a),c.falling(n,h),h),action(A,c.falling(n,h),h)));
    }
  });
  check('missing_last_probe_leaves_a_nontrivial_operator_invisible',()=>{for(let r=1;r<=6;r++)for(const h of steps){for(let k=0;k<r;k++)assert.equal(action(W(0,r),c.falling(k,h),h).terms.size,0);assert(eq(action(W(0,r),c.falling(r,h),h),mono(factorial(r),0)));}},true);
  check('unknown_order_cannot_be_certified_by_a_finite_prefix',()=>{const prefix=4,A=W(2,prefix+1);for(let k=0;k<=prefix;k++)assert.equal(action(A,c.falling(k,1),1).terms.size,0);assert.notEqual(action(A,c.falling(prefix+1,1),1).terms.size,0);},true);
  check('ordinary_product_in_native_recovery_would_give_wrong_coefficient',()=>{const a=c.falling(1,1),p=c.falling(1,1);assert(!eq(c.bullet(a,p,1),l.times(a,p)));},true);
  const A=nf(W(2,2,0,'2/3').plus(W(1,0,1)).plus(W(0,3,2,-2)).plus(W(3,1,3,'4/7'))),B=nf(X.plus(D).plus(W(0,0,2)));
  check('retained_unit_layers_reconstruct_the_bounded_degree_family',()=>{assert(recoverMemory(A,3,3).equals(A));for(let q=0;q<=3;q++)assert(recoverMemory(A,3,q).equals(memory(A,q)));details.recovered_family=A.toJSON();details.observer_certificate=readingPacket(A,3,3);assert.equal(details.observer_certificate.verdict,'COMPLETE_OPERATOR_READING_IN_DECLARED_CLASS');assert(S.fromJSON(details.observer_certificate.decoded_operator).equals(A));});
  check('memory_cut_preserves_ordered_products_in_its_quotient',()=>{for(let q=0;q<=4;q++){assert(memory(A.times(B),q).equals(memory(memory(A,q).times(memory(B,q)),q)));assert(memory(A.plus(B),q).equals(memory(A,q).plus(memory(B,q))));}});
  check('single_cut_loses_the_first_unretained_operator_layer',()=>{const v=D.plus(W(1,0,1));assert(memory(v,0).equals(D));assert(!memory(v,1).equals(D));details.single_cut_example={family:v.toJSON(),cut:memory(v,0).toJSON(),repair:memory(v,1).toJSON()};},true);
  check('every_fixed_memory_depth_has_an_explicit_blind_next_layer',()=>{for(let q=0;q<=5;q++){const unseen=W(0,0,q+1);assert.equal(memory(unseen,q).terms.size,0);assert.notEqual(memory(unseen,q+1).terms.size,0);}},true);
  check('negative_memory_depth_is_not_an_admitted_cut',()=>assert.throws(()=>memory(A,-1),RangeError),true);
  check('cut_is_faithful_for_lambda_independent_normal_coefficients',()=>{const base=nf(X.times(D).plus(D.times(X)).plus(I));assert(memory(base,0).equals(base));const banks=Array.from({length:2},(_,k)=>action(base,mono(1,k),0));assert(fromCoefficients(recover(banks,0)).equals(base));});
  check('bivariate_ordered_exponential_coefficients_keep_the_central_factor',()=>{for(let i=0;i<=6;i++)for(let j=0;j<=6;j++){const left=nf(W(0,i).times(W(j,0))).scale(new F(1n,factorial(i)*factorial(j)));let right=S.zero();for(let v=0;v<=Math.min(i,j);v++)right=right.plus(W(j-v,i-v,0,new F(1n,factorial(v)*factorial(i-v)*factorial(j-v))));assert(left.equals(right));}});
  const flowOrder=8;
  check('formal_ordered_loop_equals_exp_of_its_central_coefficient',()=>{const a=F.of('2/3'),b=F.of('5/7');let loop=m.formalExp(D.scale(a),flowOrder);for(const factor of [m.formalExp(X.scale(b),flowOrder),m.formalExp(D.scale(a.neg()),flowOrder),m.formalExp(X.scale(b.neg()),flowOrder)])loop=m.seriesMultiply(loop,factor,flowOrder);loop.forEach((v,k)=>assert(v.equals(k%2?S.zero():I.scale(a.mul(b).pow(k/2).div(factorial(k/2))))));details.loop={formal_modulus:'t^9',parameters:['2/3','5/7'],identity:'exp((10/21)*t^2) I',first_retained_coefficients:loop.slice(0,5).map(e=>e.toJSON())};});
  check('dropping_the_central_factor_changes_the_ordered_product',()=>{assert(!nf(D.times(X)).equals(nf(X.times(D))));assert(nf(D.times(X).minus(X.times(D))).equals(I));},true);
  check('formal_exponentials_descend_through_each_memory_cut',()=>{const E=m.formalExp(X.plus(W(0,1,1)),6);for(let q=0;q<=2;q++){const Fq=m.formalExp(memory(X.plus(W(0,1,1)),q),6);E.forEach((e,k)=>assert(memory(e,q).equals(memory(Fq[k],q))));}});
  check('raising_exponential_on_unit_is_the_existing_counting_exponential',()=>{const E=m.formalExp(X,8);for(const h of steps)E.forEach((v,k)=>assert(eq(action(v,mono(1,0),h),scale(c.falling(k,h),new F(1n,factorial(k))))));});
  const polys=[mono(1,0),mono(1,2),l.plus(mono('2/7',9),l.plus(mono(-3,5),mono(4,1)))];
  check('counting_lowering_flow_has_additive_composition',()=>{for(const h of steps)for(const p of polys)assert(eq(expLower(expLower(p,'2/3',h),'3/5',h),expLower(p,F.of('2/3').add('3/5'),h)));});
  check('Newton_translation_matches_independent_finite_Taylor_translation',()=>{for(const h of steps)for(const a of ['2/3',-2,0])for(const p of polys)assert(eq(newtonTranslate(p,a,h),translate(p,a)));});
  check('regular_logarithmic_generator_is_the_original_polynomial_derivative',()=>{for(const h of [...steps,0])for(const p of polys)assert(eq(logGenerator(p,h),l.derivative(p)));});
  check('counting_flow_and_raw_translation_differ_before_the_cut',()=>{const p=mono(1,2),a=F.of('2/3'),h=F.of('3/5');assert(eq(sub(expLower(p,a,h),translate(p,a)),mono(a.mul(h),0)));assert(!eq(expLower(p,a,h),translate(p,a)));assert(eq(expLower(p,a,0),translate(p,a)));details.flow_difference={probe:'x^2',counting_minus_translation:'a Lambda',first_unit_layer:'a'};},true);
  check('all_finite_windows_retain_the_top_boundary_commutator_defect',()=>{for(let N=0;N<=8;N++){const v=window(N),expected=o.identity(N+1);expected[N][N]=Cut.of(-N);assert(o.equal(o.commutator(v.D,v.X),expected));assert(l.trace(o.commutator(v.D,v.X)).zero());}});
  check('finite_window_is_rejected_as_a_full_operator_algebra_representation',()=>{for(let N=0;N<=5;N++)assert.equal(m.representationGate(S,window(N),N+1).status,'RELATION_VIOLATION');},true);
  let guardedWordChecks=0;
  check('word_height_guard_preserves_every_intermediate_state',()=>{for(const w of words(5))for(let input=0;input<=3;input++){const N=input+height(w),v=window(N),M=m.matrixValue(S.word(w),v,N+1),full=action(S.word(w),mono(1,input),0);assert(degree(full)<=N);for(let j=0;j<=N;j++)assert(M[j][input].eq(l.coefficient(full,j)[0][0]));guardedWordChecks++;}});
  check('unguarded_DX_loses_a_nonzero_boundary_response',()=>{const N=4,v=window(N),M=m.matrixValue(D.times(X),v,N+1);assert(M.every(row=>row[N].zero()));assert(eq(action(D.times(X),mono(1,N),0),mono(N+1,N)));},true);
  const inherited=JSON.parse(fs.readFileSync(path.join(__dirname,'ENDPOINT_CONNECTED_CUT_RESULT.json'),'utf8'));
  check('historical_RH_source_and_global_eta_are_unchanged',()=>{assert.equal(inherited.global_source.eta,'1079/2000');assert.equal(inherited.global_source.shifted_native_floor,'1/492000');});
  return {schema:'rkf.counting-operator-recovery.v1',date:'2026-10-12',status:'PASS_COUNTING_OPERATOR_RECOVERY_AND_ORDERED_FLOW',
    theorem_count:5,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    contract:{carrier:'Q[Lambda,x] with the SE30 counting basis',zero:'Named typed cut; additive neutral elements and compressed-window loss are separate types',response:'Whole polynomial A p_k',probe_order:'Declared r; probes p_0 through p_r',memory_depth:'Declared normal-coefficient Lambda degree d; retain through d',curvature_developed:false},
    finite_ranges:{steps,normal_power_degrees_through:6,recovery_order_through:5,unit_memory_example_degree:3,bivariate_exp_orders_through:[6,6],formal_flow_order:flowOrder,polynomial_translation_degree_through:9,window_N_through:8,guarded_word_length_through:5,guarded_word_checks:guardedWordChecks},details,
    RH:{eta:'1079/2000',native_floor:'1/492000',global_replay_rerun:false,eta_zero_certified:false,RH_proved:false},
    evidence:{universal_arguments:'Five written theorems',finite_computation:'Exact application of unchanged canonical engines',formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['r+1 scalar measurements suffice','unknown order recovered from finite data','a finite jet recovers arbitrary infinite memory','a bounded realization of the polynomial Weyl pair','T55 EMK relations equal Weyl relations','analytic convergence without a domain contract','uniform noisy-data stability','new eta or RH positivity']};
}
module.exports={presentation:S,action,recover,recoverCountingChart,memory,layer,recoverMemory,decodeReadingPacket,expLower,newtonTranslate,logGenerator,height,verify};
if(require.main===module){const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');const r=verify(),data=JSON.stringify(r,null,2)+'\n';if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(dev,'SE31_SOURCE_PINS.json')));}console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,RH:r.RH},null,2));}
