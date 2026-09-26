'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../core/native_operator.cjs'),p=require('../core/native_laurent.cjs'),g=require('../core/native_paths.cjs'),gate=require('../core/dependency_gate.cjs');
const {Cut,F,ONE,ZERO,IOTA,matrix:M,identity:I,zeros:Z,scale,add,sub,mul,dagger,equal,isZero,rank,inverse,power,rowClosure,mass}=o;
const checks=[],details={};function check(n,f){f();checks.push(n);}function eq(a,b){assert(equal(a,b));}function cs(a,b){assert(Cut.of(a).eq(b));}
function diagonal(exponents){const n=exponents.length;return p.series(exponents.map((k,i)=>{const m=Z(n);m[i][i]=ONE;return[k,m];}),n);}
function negDiagonal(exponents){return diagonal(exponents.map(k=>-k));}
function nilUnit(s,k=1){return p.plus(p.constant(I(s.length)),p.monomial(s,k));}
function packetSummary(q){return {dimension:q.dimension,depth:q.depth,determinant_order:q.determinantOrder,full:q.fullLocalModule,unseen:q.unseenJetDimensions,chain_lengths:q.chainLengths,rank_sequence:q.rankSequence};}
check('native_iota_quarter_turn',()=>cs(IOTA.mul(IOTA),-1));
check('native_zero_inverse_refused',()=>assert.throws(()=>ZERO.inv(),RangeError));
check('reject_fractional_Laurent_exponent',()=>assert.throws(()=>p.monomial([[1]],0.5),RangeError));
check('reject_ragged_coefficient',()=>assert.throws(()=>p.series([[0,[[1,0],[1]]]],2),TypeError));
check('reject_nonsquare_coefficient',()=>assert.throws(()=>p.constant([[1,0]]),RangeError));
check('reject_mixed_carriers',()=>assert.throws(()=>p.plus(p.constant([[1]]),p.constant(I(2))),RangeError));
check('reject_negative_pencil_power',()=>assert.throws(()=>p.localPacket(p.monomial([[1]],-1)),RangeError));
check('reject_identically_singular_pencil',()=>assert.throws(()=>p.localPacket(p.constant([[1,0],[0,0]])),RangeError));
check('reject_invalid_depth',()=>assert.throws(()=>p.localPacket(p.monomial([[1]],2),{depth:0}),RangeError));
check('reject_unverified_inverse',()=>assert.throws(()=>p.logarithmicResidues(p.monomial([[1]],2),p.monomial([[1]],-1)),RangeError));
check('coefficient_addition_cancels_exactly',()=>assert.equal(p.series([[1,[[1]]],[1,[[-1]]]],1).terms.size,0));
for(let m=1;m<=9;m++){
 const a=p.monomial([[1]],m),b=p.monomial([[1]],-m),r=p.logarithmicResidues(a,b),q=p.localPacket(a);
 check(`native_scalar_order_${m}_residue`,()=>{cs(r.right[0][0],m);cs(r.rightDefect[0][0],m*(m-1));assert.equal(r.rightIsIdempotent,m===1);});
 check(`native_scalar_order_${m}_jet_carrier`,()=>{assert.equal(q.dimension,m);assert.equal(q.fullLocalModule,true);assert.deepEqual(q.chainLengths,[m]);assert.equal(q.nilpotenceIndex,m);eq(power(q.action,m),Z(m));});
 check(`native_scalar_order_${m}_true_jet_identity`,()=>{const id=I(q.dimension);eq(mul(id,id),id);eq(dagger(id),id);});
 if(m>1)check(`native_scalar_order_${m}_truncated_memory`,()=>{const t=p.localPacket(a,{depth:m-1});assert.equal(t.fullLocalModule,false);assert.equal(t.unseenJetDimensions,1);});
 check(`native_scalar_order_${m}_zero_and_first_residue_distinct`,()=>{cs(p.coefficient(b,-m)[0][0],1);if(m>1)cs(p.coefficient(b,-1)[0][0],0);});
 if(m===2)details.scalar_order_two={logarithmic_residue:r.right,idempotence_defect:r.rightDefect,local_module:packetSummary(q),continuation:q.action,idempotent_on_jet_carrier:I(2)};
}
for(const s of [[0],[0,0],[0,1],[1,1],[1,2],[2,3],[0,2,3],[1,1,2]]){
 const a=diagonal(s),b=negDiagonal(s),r=p.logarithmicResidues(a,b),q=p.localPacket(a),delta=s.reduce((a,b)=>a+b,0);
 check(`diagonal_partial_orders_${s.join('_')}`,()=>{cs(r.trace,delta);assert.equal(q.dimension,delta);assert.deepEqual(q.chainLengths,s.filter(x=>x>0).sort((a,b)=>b-a));assert.equal(q.nilpotenceIndex,Math.max(...s));});
}
for(const s of [[0,1],[0,2],[1,1],[1,2],[2,3]])for(const alpha of [1,new Cut('1/2','2/3')])for(const beta of [new Cut(0,1),-2]){
 const S=M([[0,alpha],[0,0]]),T=M([[0,0],[beta,0]]),U=M([[1,1],[0,2]]),V=M([[2,0],[1,1]]);
 const e=p.times(p.constant(U),nilUnit(S,2)),ei=p.times(nilUnit(scale(S,-1),2),p.constant(inverse(U)));
 const f=p.times(nilUnit(T),p.constant(V)),fi=p.times(p.constant(inverse(V)),nilUnit(scale(T,-1)));
 const a=p.times(p.times(e,diagonal(s)),f),b=p.times(p.times(fi,negDiagonal(s)),ei),r=p.logarithmicResidues(a,b),q=p.localPacket(a),q0=p.localPacket(diagonal(s));
 const name=`unit_transformed_${s.join('_')}_${checks.length}`;
 check(name+'_inverse_trace_and_chain',()=>{p.verifyInverse(a,b);cs(r.trace,s[0]+s[1]);assert.equal(q.dimension,s[0]+s[1]);assert.deepEqual(q.chainLengths,s.filter(x=>x>0).sort((a,b)=>b-a));assert.equal(q.nilpotenceIndex,p.poleOrder(b));});
 check(name+'_basis_covariance',()=>{const el=p.toeplitz(e,q.depth),B=mul(mul(q.observer,el),p.rightInverse(q0.observer));eq(mul(B,q0.observer),mul(q.observer,el));assert.equal(rank(B),q.dimension);eq(mul(q.action,B),mul(B,q0.action));});
 check(name+'_full_marker_reconstruction',()=>{for(let j=1;j<=r.poleOrder;j++){const R=p.coefficient(b,-j);eq(p.recoverCompleteMarkers(p.markerValues(R,p.matrixUnitMarkers(2)),2),R);}});
}
for(const c of [0,1,2,new Cut('2/3','-1/4')]){
 const C=Cut.of(c),a=p.series([[0,[[0,C],[0,0]]],[1,I(2)]],2),b=p.series([[-1,I(2)],[-2,[[0,C.neg()],[0,0]]]],2),r=p.logarithmicResidues(a,b),q=p.localPacket(a);
 check(`triangular_chain_${JSON.stringify(C)}`,()=>{eq(p.coefficient(b,-1),I(2));assert.equal(q.dimension,2);assert.deepEqual(q.chainLengths,C.zero()?[1,1]:[2]);eq(r.right,I(2));});
 check(`triangular_marker_${JSON.stringify(C)}`,()=>{cs(p.markerValues(p.coefficient(b,-2),[I(2)])[0],0);cs(p.markerValues(p.coefficient(b,-2),[M([[0,0],[1,0]])])[0],C.neg());});
}
check('higher_chain_counterexample_not_discarded',()=>{details.same_determinant_and_simple_residue={determinant:'t^2',simple_residue:I(2),c_0_chains:[1,1],c_1_chains:[2],one_extra_marker:'Tr(E21 R_-2)=-c'};});
check('jet_future_observer_one_extra_cut_channel',()=>{const q=p.localPacket(p.monomial([[1]],2)),r=rowClosure([[0,1]],[q.action]);assert.equal(r.rank,2);assert.equal(r.extra,1);details.minimum_jet_repair={initial_channels:1,extra_channels:1,final_channels:2};});
check('jet_target_faithfulness_uses_algebraic_dual_not_pairing',()=>{const q=p.localPacket(diagonal([0,2]));assert.equal(q.dimension,2);assert(isZero(mul(q.observer,q.relation)));});
check('finite_depth_equality_is_certificate_not_guess',()=>{const a=diagonal([1,3]),q=p.localPacket(a,{depth:3});assert.equal(q.dimension,4);assert.equal(q.fullLocalModule,true);const low=p.localPacket(a,{depth:2});assert.equal(low.dimension,3);assert.equal(low.fullLocalModule,false);});
check('nonzero_jet_does_not_require_native_positive_state',()=>{const q=p.localPacket(p.monomial([[1]],2));assert.equal(q.nilpotenceIndex,2);assert(!equal(q.action,dagger(q.action)));});
const x=g.arrow('b','a',1),y=g.arrow('b','a',0),pa=g.arrow('a','a'),pb=g.arrow('b','b'),unit=g.unit(['a','b']),w=x.sub(y);
check('typed_seam_bridge_source_identity',()=>assert(x.dagger().mul(x).eq(pa)));
check('typed_seam_bridge_target_identity',()=>assert(x.mul(x.dagger()).eq(pb)));
check('different_native_identities_not_scalar_collapse',()=>assert(!pa.eq(pb)));
check('endpoint_color_does_not_erase_native_sheet',()=>{assert(!w.eq(new g.Paths()));assert(isZero(w.endpointShadow(['a','b'])));cs(w.dagger().mul(w).identityCoefficientSum(),2);});
check('native_aperture_enlargement_not_sheet_erasure',()=>{const small=unit.sub(pa).mul(x).mul(pa),wide=unit.sub(unit).mul(x).mul(unit);assert(small.eq(x));assert(wide.eq(new g.Paths()));assert(!x.eq(y));});
check('incorrect_sheet_type_rejected',()=>assert.throws(()=>g.arrow('a','b',0.5),TypeError));
check('endpoint_chart_rejects_missing_object',()=>assert.throws(()=>x.endpointShadow(['a']),RangeError));
check('duplicate_object_aperture_rejected',()=>assert.throws(()=>g.unit(['a','a']),TypeError));
for(let i=-3;i<=3;i++)for(let j=-2;j<=2;j++){
 const a=g.arrow('b','a',i,new Cut('1/2',j)),b=g.arrow('a','b',j,new Cut(i,'1/3')),c=g.arrow('b','a',1,new Cut(1,-1));
 check(`residue_groupoid_${i}_${j}`,()=>{assert(a.mul(b).mul(c).eq(a.mul(b.mul(c))));assert(a.mul(b).dagger().eq(b.dagger().mul(a.dagger())));assert(a.mul(b).mass().le(a.mass().mul(b.mass())));assert(a.dagger().mul(a).identityCoefficientSum().rad.eq(a.coefficientEnergy()));eq(a.mul(b).endpointShadow(['a','b']),mul(a.endpointShadow(['a','b']),b.endpointShadow(['a','b'])));});
}
check('noncomposable_paths_have_no_invented_product',()=>assert.equal(x.mul(y).terms.size,0));
check('integer_memory_does_not_wrap_as_phase',()=>{const a=g.arrow('a','a',2),b=a.mul(a);cs(b.coeff('a','a',4),1);cs(b.coeff('a','a',0),0);});
check('Laurent_depth_and_sheet_label_are_distinct',()=>{const q=p.localPacket(p.monomial([[1]],2));assert.equal(q.dimension,2);assert(!g.arrow('a','a',2).eq(g.arrow('a','a',0)));details.seam_record={same_endpoint:true,distinct_sheet:true,blind_shadow:isZero(w.endpointShadow(['a','b'])),native_difference_energy:w.coefficientEnergy(),jet_depth_is_not_sheet_modulus:true};});
const nodes={NR7:{role:'NATIVE_SCALAR',requires:[]},NR1:{role:'NATIVE_PATH',requires:['NR7']},FORMAL:{role:'DECLARED_FORMAL_EXTENSION',requires:['NR7']},JET:{role:'NATIVE_ALGEBRA_DERIVATION',requires:['FORMAL','NR1']}};
check('native_dependency_route_closes',()=>assert.deepEqual(gate.nativeDependencies('JET',nodes),['NR7','FORMAL','NR1','JET']));
for(const role of ['HILBERT_PRIMITIVE','EXTERNAL_ANALYTIC_IMPORT','PHYSICAL_ADAPTER','REPRESENTATION_SHADOW'])check('dependency_gate_rejects_'+role,()=>assert.throws(()=>gate.nativeDependencies('JET',{...nodes,NR7:{role,requires:[]}}),/Non-native premise/));
check('dependency_gate_rejects_unbound_source',()=>assert.throws(()=>gate.nativeDependencies('UNKNOWN',nodes),/Unbound/));
check('dependency_gate_rejects_cycle',()=>assert.throws(()=>gate.nativeDependencies('JET',{...nodes,NR7:{role:'NATIVE_SCALAR',requires:['JET']}}),/Cyclic/));
const root=path.resolve(__dirname,'..'),binding=['README.md','core/native_operator.cjs','core/native_laurent.cjs','core/native_paths.cjs','core/dependency_gate.cjs','tests/verify.cjs','theory/NATIVE_PRIMITIVE_ORDER.md','theory/NATIVE_LAURENT_JET_REPAIR.md','audit/LINEAGE_RECONCILIATION.json'];
const report={protocol:'NATIVE_OPERATOR_LAURENT_JET_V0_2',status:'PASS_EXACT_FINITE_CHECKS',arithmetic:'Exact rational cut pairs with BigInt; central formal continuation and integer sheet labels',runtime:process.version,check_count:checks.length,checks,details,scope:{primitive_hilbert_space:false,native_positive_pairing_required_by_new_jet_module:false,native_scalar_source:'MP NR7/NR8; predecessor finite arithmetic realization retained',historical_python_suites_rerun:false,formal_series_general_proofs_machine_verified:false,all_repositories_migrated:false,physical_quantum_gravity_proved:false,source_snapshot_recertified:false},source_sha256:Object.fromEntries(binding.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]))};
function sorted(x){if(x===null||typeof x!=='object')return x;if(x instanceof F||x instanceof Cut)return x.toJSON();if(x instanceof Map)return sorted(Object.fromEntries(x));if(Array.isArray(x))return x.map(sorted);return Object.fromEntries(Object.keys(x).sort().map(k=>[k,sorted(x[k])]));}
const content=JSON.stringify(sorted(report),null,2)+'\n',hash=crypto.createHash('sha256').update(content).digest('hex'),file=path.join(root,'audit/FINITE_CERTIFICATE.json'),pin=path.join(root,'audit/EXPECTED.sha256');
if(process.argv.includes('--write')){fs.writeFileSync(file,content);fs.writeFileSync(pin,hash+'\n');console.log('WROTE_EXACT_FINITE_EVIDENCE',checks.length,hash);}else if(process.argv.includes('--check')){assert.equal(fs.readFileSync(pin,'utf8').trim(),hash,'Pin mismatch');console.log('PASS_EXACT_FINITE_CHECKS',checks.length,hash);}else console.log('PASS_EXACT_FINITE_CHECKS_UNPINNED',checks.length,hash);
