'use strict';
// SE33 counting-specific application; canonical exact arithmetic and word
// normalization stay in operator_foundation. No shared-engine fork.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const previous=require('./endpoint_counting_operator_recovery.cjs');
const count=require('./lambda_reading_calculus.cjs');
const {F}=o,S=previous.presentation,{vector,readAction,polynomialAction}=count;
const root=path.resolve(__dirname,'..'),home=path.join(root,'research/lambda_counting');
const resultPath=path.join(__dirname,'LAMBDA_JOINT_READINGS_RESULT.json');
const W=(n=0,d=0,c=1)=>S.word([...Array(d).fill('L'),...Array(n).fill('X')],c);
const I=W(),Lambda=W(0,1),nil=()=>S.zero(),nf=e=>S.reduce(e).normal;
const ix=w=>w.filter(x=>x==='X').length,ud=w=>w.filter(x=>x==='L').length;
const sum=xs=>vector(xs.reduce((a,b)=>a.plus(b),nil()));
const prod=xs=>vector(xs.reduce((a,b)=>a.times(b),I));
const prefix=n=>Array.from({length:n+1},(_,i)=>i);
const fact=n=>{let out=1n;for(let k=2;k<=n;k++)out*=BigInt(k);return out;};
const maxCount=v=>Math.max(-1,...vector(v).entries().map(([w])=>ix(w)));
function coordinates(v){
  const out=new Map();
  for(const [w,c]of vector(v).entries()){
    const n=ix(w);out.set(n,vector((out.get(n)||nil()).plus(W(0,ud(w),c))));
  }
  return [...out].sort((a,b)=>a[0]-b[0]);
}
const coordinate=(v,n)=>new Map(coordinates(v)).get(n)||nil();
function cartesian(sets){return sets.reduce((rows,set)=>rows.flatMap(row=>set.map(x=>[...row,x])),[[]]);}
function jointAction(read,states){
  if(!Array.isArray(states)||!states.length)throw new TypeError('Positive joint arity required');
  return sum(cartesian(states.map(coordinates)).map(tuple=>prod(tuple.map(x=>x[1])).times(vector(read(tuple.map(x=>x[0]))))));
}
function jointBank(read,tuples){return tuples.map(inputs=>({inputs:[...inputs],response:vector(read(inputs)).toJSON()}));}
function bankReader(rows,arity){
  if(!Number.isSafeInteger(arity)||arity<1)throw new TypeError('Positive integer arity required');
  const table=new Map();
  for(const row of rows){
    if(!Array.isArray(row.inputs)||row.inputs.length!==arity||row.inputs.some(n=>!Number.isSafeInteger(n)||n<0))throw new TypeError('Labelled joint input tuple required');
    const key=JSON.stringify(row.inputs);
    if(table.has(key))throw new TypeError('Duplicate joint reading');
    table.set(key,vector(S.fromJSON(row.response)));
  }
  return tuple=>{
    if(tuple.length!==arity)throw new TypeError('Joint arity mismatch');
    const key=JSON.stringify(tuple);if(!table.has(key))throw new RangeError('Unread joint response '+key);
    return table.get(key);
  };
}
const grid=(arity,m)=>cartesian(Array.from({length:arity},()=>prefix(m)));
function decodeAdaptive(packet){
  const read=bankReader(packet.outer_readings,packet.arity);
  return packet.inner_responses.map(row=>({inputs:row.inputs,response:jointAction(read,row.states.map(s=>S.fromJSON(s))).toJSON()}));
}
function adaptivePacket(outer,innerMaps,inputTuples){
  const inner_responses=inputTuples.map(inputs=>({inputs,states:inputs.map((n,k)=>vector(innerMaps[k](n)).toJSON())}));
  const needed=new Map();
  for(const row of inner_responses)for(const tuple of cartesian(row.states.map(s=>coordinates(S.fromJSON(s)).map(x=>x[0]))))needed.set(JSON.stringify(tuple),tuple);
  const required_outer_tuples=[...needed.values()].sort((a,b)=>{for(let k=0;k<a.length;k++)if(a[k]!==b[k])return a[k]-b[k];return 0;});
  const packet={target:'Joint composite action on the stated input tuples',arity:innerMaps.length,inner_responses,required_outer_tuples,outer_readings:jointBank(outer,required_outer_tuples)};
  packet.decoded=decodeAdaptive(packet);return packet;
}
function decodeOrder(packet){
  const read=k=>vector(S.fromJSON(packet[k]));
  return vector(read('q_sum').minus(read('q_u')).minus(read('q_v')).plus(read('ordered_difference')).scale('1/2'));
}
function polarize(diagonal,states){
  const k=states.length;if(!k||k>20)throw new RangeError('Finite application arity 1 through 20 required');
  const terms=[];
  for(let mask=0;mask<2**k;mask++){
    const chosen=states.filter((_,i)=>mask&(2**i));
    terms.push(diagonal(sum(chosen)).scale((k-chosen.length)%2?-1:1));
  }
  return sum(terms).scale(new F(1n,fact(k)));
}
// All [t^j] responses are decoded from distinct rational-node readings.
// Degree is supplied by the constructed polynomial operation, not inferred.
function coefficientReadings(evaluate,degree){
  if(!Number.isSafeInteger(degree)||degree<0)throw new RangeError('Declared finite degree required');
  const nodes=prefix(degree),readings=nodes.map(t=>({parameter:String(t),response:vector(evaluate(new F(t))).toJSON()}));
  return {degree,readings};
}
function decodeCoefficients(packet){
  const {degree,readings}=packet;
  if(!Number.isSafeInteger(degree)||degree<0||readings.length!==degree+1)throw new TypeError('Degree plus one readings required');
  const nodes=readings.map(r=>new F(r.parameter)),seen=new Set(nodes.map(x=>x.toString()));
  if(seen.size!==nodes.length)throw new TypeError('Distinct rational nodes required');
  const inv=o.inverse(nodes.map(t=>prefix(degree).map(j=>t.pow(j))));
  const values=readings.map(r=>vector(S.fromJSON(r.response)));
  return inv.map(row=>sum(row.map((weight,i)=>values[i].scale(weight))));
}
function responses(evaluate,degree){return decodeCoefficients(coefficientReadings(evaluate,degree));}
function decodeInverse(packet){
  const m=packet.input_prefix_through;
  if(!Number.isSafeInteger(m)||m<0)throw new RangeError('Declared finite counting sector required');
  const y=vector(S.fromJSON(packet.target_state));
  if(maxCount(y)>m)throw new RangeError('Target outside declared sector');
  const kernels=packet.kernels.map(bank=>{
    const read=bankReader(bank.readings,bank.arity);
    for(const tuple of grid(bank.arity,m)){
      const v=read(tuple);
      if(maxCount(v)>=Math.min(...tuple))throw new RangeError('Joint reading violates all-input lowering');
    }
    return {arity:bank.arity,read};
  });
  let state=nil();const trace=[];
  for(let k=m;k>=0;k--){
    const correction=coordinate(sum(kernels.map(x=>jointAction(x.read,Array(x.arity).fill(state)))),k);
    const next=vector(coordinate(y,k).plus(correction));
    state=vector(state.plus(next.times(W(k))));
    trace.push({coordinate:k,recovered_coefficient:next.toJSON()});
  }
  return {state:state.toJSON(),trace};
}
function inversePacket(kernels,m,y){
  const packet={target:'Inverse of v minus the supplied diagonal kernels, on the stated finite counting sector',input_prefix_through:m,
    target_state:vector(y).toJSON(),kernels:kernels.map(x=>({arity:x.arity,readings:jointBank(x.read,grid(x.arity,m))}))};
  packet.decoded=decodeInverse(packet);return packet;
}
function pinCheck(file){
  const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;
  for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);
  return Object.keys(pins).length;
}
function verify(){
  const inheritedPins=pinCheck(path.join(home,'SE32_SOURCE_PINS.json'));
  const checks=[],controls=[],details={};
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const mu=tuple=>W(tuple.reduce((a,b)=>a+b,0));
  const matching=([i,j])=>i===j?W(i):nil();
  const ordered=([i,j])=>vector(W(i+j).plus(Lambda.scale(i-j)));
  const transposed=([i,j])=>ordered([j,i]);
  const K=([i,j])=>i===j&&i>0?vector(W(i-1).plus(W(i-1,1,i))):nil();
  const cross=([i,j])=>i>0&&j>0?vector(W(Math.min(i,j)-1,0,i+j).plus(W(Math.min(i,j)-1,1))):nil();
  const cubic=tuple=>Math.min(...tuple)>0?W(Math.min(...tuple)-1,0,tuple.reduce((a,b)=>a+b,1)):nil();
  const u=vector(W(1).plus(W(0,1,'2/3'))),v=vector(W(2).minus(W(1,1))),h=vector(W(1).plus(W(0)));
  const bilinear=(read,a,b)=>jointAction(read,[a,b]);
  const Q=a=>bilinear(ordered,a,a),H=a=>bilinear(K,a,a),Fmap=a=>vector(a.minus(H(a)));
  const dH=(a,b)=>vector(bilinear(K,a,b).plus(bilinear(K,b,a)));
  const dF=(a,b)=>vector(b.minus(dH(a,b)));
  check('joint_basis_readings_extend_R_multilinearly',()=>{
    const a=I.plus(Lambda),b=I.scale('2/3').minus(Lambda);
    for(const read of [mu,matching,ordered,K]){
      assert(bilinear(read,vector(u.times(a).plus(v.times(b))),h).equals(vector(bilinear(read,u,h).times(a).plus(bilinear(read,v,h).times(b)))));
      assert(bilinear(read,h,vector(u.times(a).plus(v.times(b)))).equals(vector(bilinear(read,h,u).times(a).plus(bilinear(read,h,v).times(b)))));
    }
  });
  check('formula_product_and_matching_have_distinct_joint_readings',()=>{assert(bilinear(mu,W(1),W(2)).equals(W(3)));assert.equal(bilinear(matching,W(1),W(2)).terms.size,0);assert(bilinear(matching,W(2),W(2)).equals(W(2)));});
  check('joint_bank_rejects_duplicate_mislabelled_or_unread_rows',()=>{
    const row=jointBank(ordered,[[1,2]]);
    assert.throws(()=>bankReader([...row,...row],2),/Duplicate/);
    assert.throws(()=>bankReader(row,3),/Labelled/);
    assert.throws(()=>bankReader(row,2)([2,1]),/Unread/);
    assert.throws(()=>jointAction(ordered,[]),/arity/);
  },true);
  const adaptive=adaptivePacket(ordered,[n=>W(2*n+1),n=>W(n).plus(W(n+1))],grid(2,1));
  check('adaptive_joint_decoder_consumes_only_serialized_inner_and_outer_readings',()=>{
    assert.deepEqual(decodeAdaptive(JSON.parse(JSON.stringify(adaptive))),adaptive.decoded);
    for(const row of adaptive.decoded)assert(S.fromJSON(row.response).equals(bilinear(ordered,W(2*row.inputs[0]+1),W(row.inputs[1]).plus(W(row.inputs[1]+1)))));
    assert.deepEqual(adaptive.required_outer_tuples,[[1,0],[1,1],[1,2],[3,0],[3,1],[3,2]]);
    details.adaptive_joint_certificate=adaptive;
  });
  check('omitted_joint_response_is_not_replaced_by_a_silent_null',()=>{
    const bad=JSON.parse(JSON.stringify(adaptive));bad.outer_readings.pop();assert.throws(()=>decodeAdaptive(bad),/Unread/);
  },true);
  check('a_null_inner_slot_needs_no_outer_readings',()=>{
    let calls=0;const p=adaptivePacket(()=>{calls++;return I;},[()=>nil(),n=>W(n)],grid(2,1));
    assert.equal(calls,0);assert(p.decoded.every(row=>S.fromJSON(row.response).terms.size===0));
  });
  check('iterated_joint_tree_agrees_with_finite_count_product',()=>{
    assert(bilinear(mu,bilinear(mu,u,v),h).equals(bilinear(mu,u,bilinear(mu,v,h))));
    assert(jointAction(mu,[u,v,h]).equals(prod([u,v,h])));
  });
  check('diagonal_readings_hide_the_antisymmetric_input_order_part',()=>{
    for(const state of [u,v,h,vector(u.plus(v)),W(3,2)])assert(Q(state).equals(bilinear(mu,state,state)));
    assert(!ordered([1,2]).equals(transposed([1,2])));
    assert(Q(vector(u.plus(v))).equals(bilinear(transposed,vector(u.plus(v)),vector(u.plus(v)))));
  },true);
  const orderPacket={target:'Ordered bilinear response on the labelled pair (p_1,p_2)',inputs:[W(1).toJSON(),W(2).toJSON()],
    q_u:Q(W(1)).toJSON(),q_v:Q(W(2)).toJSON(),q_sum:Q(W(1).plus(W(2))).toJSON(),
    ordered_difference:ordered([1,2]).minus(ordered([2,1])).toJSON()};
  orderPacket.decoded=decodeOrder(orderPacket).toJSON();
  check('ordered_difference_repairs_the_diagonal_bank',()=>{
    assert(decodeOrder(JSON.parse(JSON.stringify(orderPacket))).equals(ordered([1,2])));
    const recovered=vector(Q(u.plus(v)).minus(Q(u)).minus(Q(v)).plus(bilinear(ordered,u,v).minus(bilinear(ordered,v,u))).scale('1/2'));
    assert(recovered.equals(bilinear(ordered,u,v)));details.diagonal_order_certificate=orderPacket;
  });
  check('finite_polarization_recovers_symmetric_arity_two_through_four',()=>{
    for(let k=2;k<=4;k++){const states=[u,v,h,W(1,1)].slice(0,k);assert(polarize(a=>jointAction(mu,Array(k).fill(a)),states).equals(jointAction(mu,states)));}
  });
  check('unsymmetric_polarization_recovers_only_the_permutation_average',()=>{
    const recovered=polarize(Q,[u,v]),sym=vector(bilinear(ordered,u,v).plus(bilinear(ordered,v,u)).scale('1/2'));
    assert(recovered.equals(sym));assert(!recovered.equals(bilinear(ordered,u,v)));
  },true);
  check('nonlinear_response_coefficients_come_from_saved_rational_node_readings',()=>{
    const packet=coefficientReadings(t=>Fmap(vector(v.plus(h.scale(t)))),2);
    const coeff=decodeCoefficients(JSON.parse(JSON.stringify(packet)));
    assert(coeff[0].equals(Fmap(v)));assert(coeff[1].equals(dF(v,h)));assert(coeff[2].equals(H(h).scale(-1)));
    details.polynomial_response_certificate={...packet,decoded_coefficients:coeff.map(x=>x.toJSON()),target:'All coefficients of the constructed degree-at-most-two response F(v+t h)'};
  });
  check('finite_taylor_response_reconstructs_the_shifted_operation',()=>{
    const coeff=responses(t=>Fmap(vector(v.plus(h.scale(t)))),2);
    assert(sum(coeff).equals(Fmap(vector(v.plus(h)))));
    const second=responses(t=>dF(vector(v.plus(h.scale(t))),h),1)[1];
    assert(second.equals(coeff[2].scale(2)));
  });
  const Gmap=a=>vector(a.plus(bilinear(mu,a,a))),dG=(a,b)=>vector(b.plus(bilinear(mu,a,b)).plus(bilinear(mu,b,a)));
  check('finite_chain_rule_matches_independent_degree_four_response_readings',()=>{
    const coeff=responses(t=>Gmap(Fmap(vector(v.plus(h.scale(t))))),4);
    assert(coeff[1].equals(dG(Fmap(v),dF(v,h))));assert(sum(coeff).equals(Gmap(Fmap(v.plus(h)))));
  });
  check('ordered_bilinear_product_rule_preserves_both_input_slots',()=>{
    const shift=W(2),B=a=>bilinear(ordered,Fmap(a),vector(a.plus(shift)));
    const read=responses(t=>B(vector(v.plus(h.scale(t)))),3)[1];
    const wanted=vector(bilinear(ordered,dF(v,h),v.plus(shift)).plus(bilinear(ordered,Fmap(v),h)));
    assert(read.equals(wanted));assert(!read.equals(bilinear(ordered,dF(v,h),v.plus(shift)).scale(2)));
  },true);
  check('response_samples_do_not_infer_an_unknown_global_degree_bound',()=>{
    const nodes=[0,1,2];for(const t of nodes)assert.equal(new F(t).mul(t-1).mul(t-2).zero(),true);
    assert(!new F(3).mul(2).mul(1).zero());
    const packet=coefficientReadings(t=>W(0,0,t),1);packet.readings[1].parameter='0';assert.throws(()=>decodeCoefficients(packet),/Distinct/);
  },true);
  check('joint_composition_and_order_recovery_commute_with_unit_cuts',()=>{
    for(let q=0;q<=3;q++){
      const cut=a=>previous.memory(vector(a),q),read=tuple=>cut(ordered(tuple));
      assert(cut(bilinear(ordered,u,v)).equals(cut(bilinear(read,cut(u),cut(v)))));
      const p=JSON.parse(JSON.stringify(orderPacket));for(const key of ['q_u','q_v','q_sum','ordered_difference'])p[key]=cut(S.fromJSON(p[key])).toJSON();
      assert(cut(decodeOrder(p)).equals(cut(decodeOrder(orderPacket))));
    }
  });
  check('polynomial_response_decoding_commutes_with_retained_unit_layers',()=>{
    const original=coefficientReadings(t=>Gmap(Fmap(vector(v.plus(h.scale(t))))),4),full=decodeCoefficients(original);
    for(let q=0;q<=3;q++){
      const p=JSON.parse(JSON.stringify(original));p.readings.forEach(r=>{r.response=previous.memory(S.fromJSON(r.response),q).toJSON();});
      decodeCoefficients(p).forEach((a,j)=>assert(a.equals(previous.memory(full[j],q))));
    }
  });
  check('unit_memory_and_input_order_are_independent_observation_labels',()=>{
    assert(previous.memory(ordered([1,2]),0).equals(previous.memory(ordered([2,1]),0)));
    assert(!previous.memory(ordered([1,2]),1).equals(previous.memory(ordered([2,1]),1)));
    const rationalOrder=([i,j])=>W(i+j).plus(W(0,0,i-j));
    assert(!previous.memory(rationalOrder([1,2]),0).equals(previous.memory(rationalOrder([2,1]),0)));
  },true);
  check('nonlinear_kernel_is_generated_by_existing_profile_matching_and_lowering',()=>{
    const D=S.word(['D']),phi=n=>vector(W(n).plus(W(n,1,n)));
    const shift=a=>readAction(n=>W(n,0,new F(1,n+1)),polynomialAction(D,a));
    for(let i=0;i<=5;i++)for(let j=0;j<=5;j++)assert(shift(readAction(phi,matching([i,j]))).equals(K([i,j])));
  });
  const inverseReading=inversePacket([{arity:2,read:K}],3,W(3));
  const inverse=y=>S.fromJSON(decodeInverse({...inverseReading,target_state:vector(y).toJSON()}).state);
  const solved=inverse(W(3));
  check('nonlinear_inverse_is_decoded_from_archived_joint_readings_only',()=>{
    assert.deepEqual(decodeInverse(JSON.parse(JSON.stringify(inverseReading))),inverseReading.decoded);
    details.nonlinear_inverse_certificate=inverseReading;
  });
  check('inverse_at_p3_matches_the_independent_coordinate_product_formula',()=>{
    const a=I.plus(Lambda),b=I.plus(Lambda.scale(2)),c=I.plus(Lambda.scale(3));
    const wanted=sum([W(3),c.times(W(2)),prod([b,c,c]).times(W(1)),prod([a,b,b,c,c,c,c])]);
    assert(solved.equals(wanted));assert(Fmap(solved).equals(W(3)));
  });
  check('both_nonlinear_inverse_identities_hold_on_mixed_finite_inputs',()=>{
    const inputs=[nil(),W(3),v,vector(W(2).plus(W(1,1,'2/3')).minus(W(0,2)))];
    for(const a of inputs){assert(Fmap(inverse(a)).equals(a));assert(inverse(Fmap(a)).equals(a));}
  });
  check('inverse_decoder_handles_cross_terms_and_mixed_kernel_arities',()=>{
    const target=vector(W(2).plus(W(1,1)));
    const kernels=[{arity:2,read:cross},{arity:3,read:cubic}];
    const Hmix=a=>sum(kernels.map(k=>jointAction(k.read,Array(k.arity).fill(a))));
    const p=inversePacket(kernels,2,target),answer=S.fromJSON(p.decoded.state);
    assert(vector(answer.minus(Hmix(answer))).equals(target));
    const source=vector(W(2,0,'1/2').plus(W(0)));
    const p2={...p,target_state:vector(source.minus(Hmix(source))).toJSON()};
    assert(S.fromJSON(decodeInverse(p2).state).equals(source));
  });
  check('finite_sector_inverse_extensions_preserve_earlier_solutions',()=>{
    for(let m=0;m<=3;m++){const y=W(m),small=inversePacket([{arity:2,read:K}],m,y);assert(S.fromJSON(small.decoded.state).equals(inverse(y)));}
  });
  check('nonlinear_inverse_commutes_with_unit_cuts',()=>{
    for(let q=0;q<=3;q++){
      const p=JSON.parse(JSON.stringify(inverseReading));
      p.target_state=previous.memory(S.fromJSON(p.target_state),q).toJSON();
      p.kernels.forEach(k=>k.readings.forEach(r=>{r.response=previous.memory(S.fromJSON(r.response),q).toJSON();}));
      assert(previous.memory(S.fromJSON(decodeInverse(p).state),q).equals(previous.memory(solved,q)));
    }
  });
  check('inverse_linear_response_matches_the_exact_lowering_geometric_sum',()=>{
    const y=W(3),direction=vector(W(3).plus(W(1))),state=inverse(y);
    const fromReadings=responses(t=>inverse(vector(y.plus(direction.scale(t)))),8)[1];
    let term=direction,total=nil();
    for(let j=0;j<=3;j++){total=total.plus(term);term=dH(state,term);}
    assert.equal(term.terms.size,0);assert(vector(total).equals(fromReadings));
    assert(dF(state,fromReadings).equals(direction));
    details.inverse_linear_response={base:y.toJSON(),direction:direction.toJSON(),decoded:fromReadings.toJSON(),response_degree_bound:8,finite_geometric_last_power:3};
  });
  check('inverse_degree_doubles_with_count_height_in_the_generated_family',()=>{
    for(let m=0;m<=3;m++){
      const p=inversePacket([{arity:2,read:K}],m,W(m)),degree=2**m;
      const at=t=>S.fromJSON(decodeInverse({...p,target_state:W(m,0,t).toJSON()}).state);
      const coeff=responses(at,degree);
      assert(coordinate(coeff[degree],0).terms.size>0);
      for(let j=0;j<degree;j++)assert.equal(coordinate(coeff[j],0).terms.size,0);
    }
  });
  check('output_degree_lowering_alone_does_not_imply_nonlinear_invertibility',()=>{
    const bad=([i,j])=>i+j===1?W(0,0,'1/2'):nil();
    const target=W(0).plus(W(1));
    assert.throws(()=>inversePacket([{arity:2,read:bad}],1,target),/all-input lowering/);
    for(const coefficient of [-2,0,1,3]){
      const state=W(0,0,coefficient).plus(W(1)),out=vector(state.minus(bilinear(bad,state,state)));
      assert(out.equals(W(1)));assert(!out.equals(target));
    }
  },true);
  check('inverse_decoder_reports_missing_joint_data_and_out_of_sector_targets',()=>{
    const p=JSON.parse(JSON.stringify(inverseReading));p.kernels[0].readings.pop();assert.throws(()=>decodeInverse(p),/Unread/);
    assert.throws(()=>decodeInverse({...inverseReading,target_state:W(4).toJSON()}),/outside/);
  },true);
  return {schema:'rkf.lambda-joint-readings.v1',date:'2026-10-12',status:'PASS_JOINT_READING_AND_NONLINEAR_COUNTING',
    theorem_count:5,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    certificate_rule:'The recorded observer reading decoded for its stated target',
    construction:{carrier:'Finite counting states over Q[Lambda]',source:'Existing counting action and generated joint kernels',zero:'Typed cut operation; additive neutrals retain their separate types',
      primitive_metric:false,analytic_derivative_assumed:false,unknown_polynomial_degree_inferred_from_samples:false,RH_development:false,curvature_developed:false},
    finite_ranges:{polarization_arities:[2,3,4],joint_composition_input_grid_through:1,joint_composition_requested_tuples:6,
      generated_kernel_indices_through:5,quadratic_inverse_sector_through:3,mixed_quadratic_cubic_inverse_sector_through:2,unit_cut_orders:[0,1,2,3],inverse_response_degree_through:8},
    details,evidence:{general_results:'Five written proofs from finite counting expansions',executable:'Exact recorded-reading decoding and counterexamples using unchanged canonical engines',
      formal_proof_assistant:false,external_review:false,whole_engine_pass:false},
    not_claimed:['identification of an arbitrary unknown nonlinear operation from finite samples','arbitrary nonlinear invertibility','uniform noisy-data stability',
      'global bounded polynomial degree of the inverse','physical quadrant identification','new RH or curvature result','novelty priority for elementary polarization or triangular inversion']};
}
module.exports={coordinates,jointAction,jointBank,bankReader,decodeAdaptive,adaptivePacket,decodeOrder,polarize,coefficientReadings,decodeCoefficients,decodeInverse,inversePacket,verify};
if(require.main===module){
  const args=process.argv.slice(2);if(args.length>1||args.some(a=>!['--write','--check'].includes(a)))throw new Error('Choose --write or --check');
  const r=verify(),data=JSON.stringify(r,null,2)+'\n';
  if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});
  if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(path.join(home,'SE33_SOURCE_PINS.json')));}
  console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,finite_ranges:r.finite_ranges,certificate_rule:r.certificate_rule},null,2));
}

