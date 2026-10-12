'use strict';
// SE32 counting-module application. The unchanged canonical compiler performs
// every expression product and normal form. No second shared engine is added.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const m=require('../operator_foundation/core/paninian_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const {Count}=require('./endpoint_lambda_counting.cjs');
const {F,Cut}=o,S=previous.presentation;
const root=path.resolve(__dirname,'..');
const home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_READING_CALCULUS_RESULT.json');
const nf=e=>S.reduce(e).normal;
const W=(i=0,j=0,d=0,v=1)=>S.word([...Array(d).fill('L'),...Array(i).fill('X'),...Array(j).fill('D')],v);
const I=W(),X=W(1),D=W(0,1),Lambda=W(0,0,1),neutral=()=>S.zero();
const countIndex=w=>w.filter(t=>t==='X').length;
const unitIndex=w=>w.filter(t=>t==='L').length;
const fact=n=>{let v=1n;for(let j=1;j<=n;j++)v*=BigInt(j);return v;};
const falling=(n,k)=>k>n?0n:fact(n)/fact(n-k);
function vector(e){const v=nf(e);if(v.entries().some(([w,c])=>w.includes('D')||!c.turn.zero()))throw new TypeError('Finite rational counting response required');return v;}
function scalar(e){const v=vector(e);if(v.entries().some(([w])=>countIndex(w)))throw new TypeError('Central unit polynomial required');return v;}
const maxCount=v=>Math.max(-1,...vector(v).entries().map(([w])=>countIndex(w)));
const maxUnit=v=>Math.max(0,...vector(v).entries().map(([w])=>unitIndex(w)));
// In the module P, a normal X^i D^j acts on p_0; j>0 annihilates p_0.
function polynomialAction(operator,state){const e=nf(operator.times(vector(state)));return vector(new m.Expr(S,'*','*',e.entries().filter(([w])=>!w.includes('D'))));}
function readAction(read,state){let out=neutral();for(const [w,c]of vector(state).entries())out=out.plus(W(0,0,unitIndex(w),c).times(vector(read(countIndex(w)))));return vector(out);}
function memo(read){const cache=new Map();return n=>{if(!Number.isSafeInteger(n)||n<0)throw new RangeError('Nonnegative counting index required');if(!cache.has(n))cache.set(n,vector(read(n)));return cache.get(n);};}
const prefix=n=>Array.from({length:n+1},(_,k)=>k);
const bank=(read,indices)=>indices.map(n=>({probe:n,response:vector(read(n)).toJSON()}));
function bankMap(rows){const out=new Map();for(const row of rows){if(!Number.isSafeInteger(row.probe)||row.probe<0||out.has(row.probe))throw new TypeError('Distinct labelled response rows required');out.set(row.probe,vector(S.fromJSON(row.response)));}return out;}
function requireRow(rows,n){if(!rows.has(n))throw new RangeError('Unread counting response '+n);return rows.get(n);}
function decodePrefix(rows){
  const table=bankMap(rows),coefficients=[];let partial=neutral();
  for(let k=0;k<rows.length;k++){
    let residual=requireRow(table,k);
    for(let j=0;j<k;j++)residual=nf(residual.minus(coefficients[j].times(W(k-j)).scale(falling(k,j))));
    const a=vector(residual.scale(new F(1n,fact(k))));coefficients.push(a);
    partial=nf(partial.plus(a.times(W(0,k))));
  }
  return {input_prefix_through:rows.length-1,normal_partial:partial,coefficients};
}
function supportOfBank(rows){const support=new Set();for(const v of bankMap(rows).values())for(const [w]of v.entries())support.add(countIndex(w));return [...support].sort((a,b)=>a-b);}
function composeFromReadings(leftRows,rightRows){const left=bankMap(leftRows),right=bankMap(rightRows);return [...right].sort((a,b)=>a[0]-b[0]).map(([probe,state])=>({probe,response:readAction(k=>requireRow(left,k),state).toJSON()}));}
function adaptivePacket(leftRead,rightRead,through){
  const right=bank(rightRead,prefix(through)),needed=supportOfBank(right),left=bank(leftRead,needed);
  return {rule:'Certification is the recorded observer reading decoded for its declared target',
    target:'Ordered product action on the specified finite input prefix',input_prefix_through:through,
    right_readings:right,required_left_indices:needed,left_readings:left,
    decoded_product:composeFromReadings(left,right),verdict:'COMPLETE_PRODUCT_READING_ON_DECLARED_INPUT_PREFIX'};
}
function inverseFromReadings(rows){
  const table=bankMap(rows),decoded=new Map();
  for(let n=0;n<rows.length;n++){
    const lower=requireRow(table,n);
    if(maxCount(lower)>=n)throw new RangeError('Reading is not strictly lowering on the declared prefix');
    const response=vector(W(n).plus(readAction(k=>requireRow(decoded,k),lower)));
    decoded.set(n,response);
  }
  return [...decoded].map(([probe,response])=>({probe,response:response.toJSON()}));
}
function inversePacket(lowerRead,through){const readings=bank(lowerRead,prefix(through));return {
  rule:'Certification is the recorded observer reading decoded for its declared target',
  target:'Two-sided inverse action of I-L on the supplied lowering prefix',input_prefix_through:through,
  lowering_readings:readings,decoded_inverse:inverseFromReadings(readings),
  verdict:'COMPLETE_INVERSE_READING_ON_DECLARED_INPUT_PREFIX'};
}
function profileRead(phi){return memo(n=>scalar(phi(n)).times(W(n)));}
function profileExpansion(phi,through){const coeff=[];let out=neutral();for(let n=0;n<=through;n++){let rem=scalar(phi(n));for(let k=0;k<n;k++)rem=nf(rem.minus(coeff[k].scale(falling(n,k))));const a=scalar(rem.scale(new F(1n,fact(n))));coeff.push(a);out=nf(out.plus(a.times(W(n,n))));}return out;}
function primeCount(n){if(n<2)return false;const count=new Count(n);for(let k=2;k*k<=n;k++)if(new Count(k).divides(count))return false;return true;}
function pinCheck(file){const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);return Object.keys(pins).length;}
function verify(){
  const inheritedPins=pinCheck(path.join(root,'papers/rkf_completed_weil_endpoint/development/SE31_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const doubling=memo(n=>W(2*n+1));
  const growingUnits=memo(n=>W(n,0,n));
  const irregular=memo(n=>W(n%3,0,n%4,new F(n+1,n+2)).plus(W(2*n+1,0,1,-1)));
  const L=nf(D.plus(Lambda.times(X).times(D).times(D)));
  const lower=memo(n=>polynomialAction(L,W(n)));
  const lowerFormula=n=>n?vector(W(n-1,0,0,n).plus(W(n-1,0,1,n*(n-1)))):neutral();
  check('native_counting_module_action_respects_the_existing_relation',()=>{for(let n=0;n<=9;n++)assert(polynomialAction(D.times(X).minus(X.times(D)),W(n)).equals(W(n)));});
  check('response_packets_exclude_operator_tokens_and_out_of_carrier_scalars',()=>{assert.throws(()=>vector(D),TypeError);assert.throws(()=>vector(W(1,0,0,new Cut(1,1))),TypeError);},true);
  check('arbitrary_finite_columns_decode_without_a_global_order_bound',()=>{for(const read of [doubling,growingUnits,irregular])for(let r=0;r<=7;r++){const decoded=decodePrefix(bank(read,prefix(r)));for(let n=0;n<=r;n++)assert(polynomialAction(decoded.normal_partial,W(n)).equals(read(n)));}});
  check('successive_decoders_preserve_every_earlier_normal_coefficient',()=>{for(const read of [doubling,irregular]){const full=decodePrefix(bank(read,prefix(8)));for(let r=0;r<8;r++){const small=decodePrefix(bank(read,prefix(r)));small.coefficients.forEach((a,j)=>assert(a.equals(full.coefficients[j])));}}});
  check('finite_readings_do_not_identify_the_full_unknown_operator',()=>{for(let r=0;r<=6;r++){const hidden=W(0,r+1);for(let n=0;n<=r;n++)assert.equal(polynomialAction(hidden,W(n)).terms.size,0);assert(polynomialAction(hidden,W(r+1)).equals(I.scale(fact(r+1))));}},true);
  check('reading_partial_matches_a_finite_mixed_input_exactly',()=>{const state=vector(W(2,0,3,'2/7').plus(W(5,0,0,-3)).plus(W(0,0,2)));for(const read of [doubling,irregular]){const partial=decodePrefix(bank(read,prefix(5))).normal_partial;assert(polynomialAction(partial,state).equals(readAction(read,state)));}});
  const product=adaptivePacket(lower,doubling,3);
  check('composition_aperture_is_obtained_from_the_recorded_response_support',()=>{assert.deepEqual(product.required_left_indices,[1,3,5,7]);const decoded=composeFromReadings(JSON.parse(JSON.stringify(product.left_readings)),JSON.parse(JSON.stringify(product.right_readings)));assert.deepEqual(decoded,product.decoded_product);for(const row of decoded)assert(S.fromJSON(row.response).equals(readAction(lower,doubling(row.probe))));details.adaptive_observer_certificate=product;});
  check('every_requested_basis_column_can_change_the_target_product',()=>{for(const omitted of product.required_left_indices){const changed=memo(n=>lower(n).plus(n===omitted?I:neutral()));const other=adaptivePacket(changed,doubling,3);assert.notDeepEqual(other.decoded_product,product.decoded_product);}},true);
  check('a_same_size_prefix_can_lose_the_next_composition_response',()=>{for(let r=0;r<=5;r++){const hidden=W(0,r+1);assert.equal(polynomialAction(hidden,W(r)).terms.size,0);assert(polynomialAction(hidden.times(X),W(r)).equals(I.scale(fact(r+1))));}},true);
  check('missing_required_readings_are_reported_as_unread',()=>{assert.throws(()=>composeFromReadings(product.left_readings.slice(0,-1),product.right_readings),/Unread counting response/);},true);
  check('an_empty_right_response_needs_no_left_readings',()=>{let requested=0;const p=adaptivePacket(()=>{requested++;return I;},()=>neutral(),4);assert.equal(requested,0);assert.deepEqual(p.required_left_indices,[]);assert(p.decoded_product.every(row=>S.fromJSON(row.response).terms.size===0));});
  check('ordered_composition_is_associative_on_finite_counting_states',()=>{const state=vector(W(2,0,2).plus(W(0,0,0,'3/7')));const AB=memo(n=>readAction(irregular,doubling(n))),BC=memo(n=>readAction(doubling,lower(n)));assert(readAction(AB,readAction(lower,state)).equals(readAction(irregular,readAction(BC,state))));});
  check('unit_cuts_commute_with_adaptive_composition',()=>{for(let q=0;q<=4;q++){const left=memo(n=>previous.memory(irregular(n),q)),right=memo(n=>previous.memory(doubling(n),q));for(let n=0;n<=5;n++)assert(previous.memory(readAction(irregular,doubling(n)),q).equals(previous.memory(readAction(left,right(n)),q)));}});
  check('unit_cut_commutes_with_successive_response_decoding',()=>{for(let q=0;q<=4;q++){const rows=bank(irregular,prefix(6)),cutRows=rows.map(row=>({probe:row.probe,response:previous.memory(S.fromJSON(row.response),q).toJSON()}));const full=decodePrefix(rows),cut=decodePrefix(cutRows);assert(previous.memory(full.normal_partial,q).equals(cut.normal_partial));}});
  check('a_fixed_unit_depth_does_not_recover_every_later_response',()=>{for(let q=0;q<=5;q++){assert.equal(previous.memory(growingUnits(q+1),q).terms.size,0);assert(previous.memory(growingUnits(q+1),q+1).equals(growingUnits(q+1)));assert.equal(maxUnit(growingUnits(q+1)),q+1);}},true);
  check('complete_finite_response_banks_have_readable_finite_unit_depth',()=>{for(let r=0;r<=7;r++){const rows=prefix(r).map(growingUnits),depth=Math.max(0,...rows.map(maxUnit));assert.equal(depth,r);for(const v of rows)assert(previous.memory(v,depth).equals(v));}});
  const profiles=[n=>I.scale(n),n=>I.scale(new F(1,n+1)),n=>I.scale(n%2),n=>Lambda.scale(n+1).plus(I.scale(n*n+1)),n=>I.scale(primeCount(n)?1:0)];
  check('arbitrary_count_profiles_decode_from_their_counting_values',()=>{for(const phi of profiles){const op=profileExpansion(phi,12),read=profileRead(phi);for(let n=0;n<=12;n++)assert(polynomialAction(op,W(n)).equals(read(n)));}});
  check('count_profile_products_are_pointwise_products',()=>{for(const a of profiles)for(const b of profiles)for(let n=0;n<=6;n++){const A=profileRead(a),B=profileRead(b);assert(readAction(A,B(n)).equals(nf(a(n).times(b(n)).times(W(n)))));}});
  check('residue_sector_projections_partition_and_route_counts',()=>{for(const modulus of [2,3,5]){const sectors=prefix(modulus-1).map(r=>profileRead(n=>I.scale(n%modulus===r?1:0)));for(let n=0;n<=12;n++){let sum=neutral();for(let r=0;r<modulus;r++){const P=sectors[r];sum=sum.plus(P(n));assert(readAction(P,P(n)).equals(P(n)));assert(readAction(P,W(n+1)).equals(polynomialAction(X,sectors[(r-1+modulus)%modulus](n))));assert(readAction(P,polynomialAction(D,W(n))).equals(polynomialAction(D,sectors[(r+1)%modulus](n))));for(let s=0;s<modulus;s++)if(s!==r)assert.equal(readAction(P,sectors[s](n)).terms.size,0);}assert(sum.equals(W(n)));}}});
  check('prime_selection_uses_the_existing_positive_count_divisibility',()=>{const read=profileRead(n=>I.scale(primeCount(n)?1:0));const selected=[];for(let n=0;n<=30;n++){assert(readAction(read,read(n)).equals(read(n)));if(read(n).terms.size)selected.push(n);}assert.deepEqual(selected,[2,3,5,7,11,13,17,19,23,29]);details.prime_count_selection={through:30,selected,distribution_claim:false};});
  check('inverse_of_N_plus_I_is_read_count_by_count',()=>{const phi=n=>I.scale(n+1),psi=n=>I.scale(new F(1,n+1));for(let n=0;n<=12;n++){assert(readAction(profileRead(phi),profileRead(psi)(n)).equals(W(n)));assert(readAction(profileRead(psi),profileRead(phi)(n)).equals(W(n)));}});
  check('nonunit_count_profile_does_not_acquire_a_rational_polynomial_inverse',()=>{const sample=profileRead(()=>Lambda)(2);assert(previous.memory(sample,0).terms.size===0);assert(!previous.memory(W(2),0).equals(neutral()));},true);
  check('generated_lowering_rule_is_read_directly_from_D_and_X',()=>{for(let n=0;n<=10;n++){assert(lower(n).equals(lowerFormula(n)));assert(maxCount(lower(n))<n);}});
  const inverseReading=inversePacket(lower,7),inverseTable=bankMap(inverseReading.decoded_inverse),G=n=>requireRow(inverseTable,n);
  check('inverse_decoder_uses_only_the_archived_lowering_response_bank',()=>{const detached=JSON.parse(JSON.stringify(inverseReading.lowering_readings));assert.deepEqual(inverseFromReadings(detached),inverseReading.decoded_inverse);details.inverse_observer_certificate=inverseReading;});
  check('inverse_readings_obey_both_inverse_identities_on_the_declared_prefix',()=>{for(let n=0;n<=7;n++){assert(vector(G(n).minus(readAction(lower,G(n)))).equals(W(n)));assert(readAction(G,vector(W(n).minus(lower(n)))).equals(W(n)));}});
  check('recursive_inverse_matches_independent_finite_geometric_action',()=>{for(let n=0;n<=7;n++){let term=W(n),sum=neutral();for(let k=0;k<=n;k++){sum=sum.plus(term);term=readAction(lower,term);}assert.equal(term.terms.size,0);assert(vector(sum).equals(G(n)));}});
  check('inverse_reading_matches_the_counted_product_formula',()=>{for(let n=0;n<=7;n++){let sum=neutral(),weight=I;for(let k=0;k<=n;k++){sum=sum.plus(weight.times(W(n-k)).scale(falling(n,k)));weight=nf(weight.times(I.plus(Lambda.scale(n-k-1))));}assert(vector(sum).equals(G(n)));}});
  check('inverse_survives_the_operator_cut_with_its_declared_unit_layers',()=>{for(let q=0;q<=3;q++){const rows=inverseReading.lowering_readings.map(row=>({probe:row.probe,response:previous.memory(S.fromJSON(row.response),q).toJSON()}));const decoded=inverseFromReadings(rows);decoded.forEach((row,n)=>assert(previous.memory(S.fromJSON(row.response),q).equals(previous.memory(G(n),q))));}});
  check('inverse_readings_extend_without_changing_an_earlier_response',()=>{for(let r=0;r<=6;r++){const rows=inverseFromReadings(bank(lower,prefix(r)));assert.deepEqual(rows,inverseReading.decoded_inverse.slice(0,r+1));}});
  check('infinite_order_inverse_has_a_visible_high_input_constant_response',()=>{for(let n=1;n<=7;n++){const cut=previous.memory(G(n),0),constant=cut.entries().filter(([w])=>countIndex(w)===0);assert.equal(constant.length,1);assert(constant[0][1].eq(fact(n)));const partial=decodePrefix(inverseReading.decoded_inverse.slice(0,n)).normal_partial;assert(!polynomialAction(partial,W(n)).equals(G(n)));}},true);
  check('raising_is_not_silently_admitted_as_a_lowering_inverse',()=>{assert.throws(()=>inverseFromReadings(bank(n=>W(n+1),prefix(4))),/not strictly lowering/);let finite=neutral();for(let k=0;k<=5;k++)finite=finite.plus(W(k));assert(polynomialAction(I.minus(X),finite).equals(I.minus(W(6))));},true);
  return {schema:'rkf.lambda-reading-calculus.v1',date:'2026-10-12',status:'PASS_COUNTING_OBSERVER_READING_CALCULUS',
    theorem_count:5,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting states over Q[Lambda]',operator_completion:'All column-finite R-linear counting actions',convergence:'Eventual exact agreement on every finite input prefix',primitive_metric:false,analytic_convergence_assumed:false,curvature_developed:false,RH_development:false,full_infinite_black_box_certified_by_finite_data:false},
    finite_ranges:{arbitrary_column_recovery_prefix_through:8,count_profiles_through:12,sector_moduli:[2,3,5],prime_selection_through:30,lowering_formula_through:10,inverse_prefix_through:7,unit_cut_orders_through:5},details,
    evidence:{general_results:'Five written proofs derived from counting actions',executable:'Exact observer reading/decoding examples on unchanged canonical engines',formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['bounded operators on an unspecified normed space','uniform noisy-data stability','infinite state series on this carrier','global identification from a finite unknown response bank','new prime-distribution law','new RH or curvature result']};
}
module.exports={vector,polynomialAction,readAction,decodePrefix,supportOfBank,composeFromReadings,adaptivePacket,inverseFromReadings,profileExpansion,verify};
if(require.main===module){const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');const r=verify(),data=JSON.stringify(r,null,2)+'\n';if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE32_SOURCE_PINS.json')));}console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));}
