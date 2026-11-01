'use strict';
/** Exact finite checks for the structure report R3: named instances, planted controls, and the T53-shape factorization. */
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const o=require('../../operator_foundation/core/native_operator.cjs'),s=require('./structure_report.cjs'),instances=require('./instances.cjs');
const {F,Cut,ONE,IOTA,matrix:M,identity:I,mul,dagger,equal,isZero,rank,sub,scale}=o;
const checks=[],data={instances:{}},counts={instances:0,forward_word_pairs:0,random_cut_squares:0,seam_count_readings:0};
function check(name,fn){fn();checks.push(name);}
const str=x=>x instanceof F?x.toString():Array.isArray(x)?x.map(str):x;

// 1. Named instances against their declared expectations.
for(const [name,job] of Object.entries(instances)){check('instance_'+name,()=>{const r=s.structureReport(job),e=job.expect;
  assert.equal(r.verdict,e.verdict);assert.equal(r.observer.forward_extra,e.forward_extra);assert.equal(r.observer.dagger_extra,e.dagger_extra);
  if(e.rank_K!==undefined)assert.equal(r.returning_memory_form.rank,e.rank_K);
  if(e.weights)assert.deepEqual(r.returning_memory_form.weights.filter(w=>!w.zero()).map(w=>w.rad.toString()),e.weights.filter(w=>w!=='0'));
  if(e.cut_aligned!==undefined)assert.equal(r.returning_memory.cut_aligned_observer,e.cut_aligned);
  if(e.odd_only)for(const g of Object.values(r.returning_memory.generators))assert(g.even_leak_mass.zero());
  if(e.even_leak)assert(Object.values(r.returning_memory.generators).some(g=>!g.even_leak_mass.zero()));
  if(e.seam_counts){assert.deepEqual(r.seam_count_reading.map(x=>x.n_plus),e.seam_counts);counts.seam_count_readings+=e.seam_counts.length;}
  // R3-B as a reported fact: returning memory is present exactly when the reversed catalogue adds channels.
  assert.equal(r.returning_memory.any,r.observer.dagger_extra>0);
  counts.instances++;counts.forward_word_pairs+=r.census.forward_word_pairs_multiplicative;
  data.instances[name]={verdict:r.verdict,forward_extra:r.observer.forward_extra,dagger_extra:r.observer.dagger_extra,rank_returning_form:r.returning_memory_form.rank,weights:str(r.returning_memory_form.weights.map(w=>w.rad)),leak_energy:Object.fromEntries(Object.entries(r.returning_memory.generators).map(([k,v])=>[k,v.leak_energy.toString()])),odd_leak_mass:r.cut?Object.fromEntries(Object.entries(r.returning_memory.generators).map(([k,v])=>[k,v.odd_leak_mass.toString()])):undefined,cut_aligned_observer:r.returning_memory.cut_aligned_observer,seam_count:r.seam_count_reading?r.seam_count_reading.map(x=>({threshold:x.threshold.toString(),n_plus:x.n_plus})):undefined};});}

// 2. The mark is square-sourced only under the native reversal: the coordinate transpose gives the wrong sign on the turn instance.
check('coordinate_transpose_is_not_the_mark',()=>{const leak=M([[0,IOTA],[0,0]]);const native=mul(dagger(leak),leak),transposed=mul(s.transposeOnly(leak),leak);assert(equal(native,M([[0,0],[0,1]])));assert(equal(transposed,M([[0,0],[0,-1]])));assert(!equal(native,transposed));data.transpose_control={native_square:'E_22',transpose_product:'-E_22'};});

// 3. Non-admitted cut refused; rank-zero observer refused; carrier mismatch refused.
check('non_admitted_cut_refused',()=>{assert.throws(()=>s.admittedCut([[1,1],[0,1]]),/self-dagger/);assert.throws(()=>s.admittedCut([[2,0],[0,2]]),/square to the identity/);});
check('empty_observer_refused',()=>assert.throws(()=>s.structureReport({catalogue:{R:[[0,-1],[1,0]]},observer:[[0,0]]}),/rank zero/));
check('carrier_mismatch_refused',()=>assert.throws(()=>s.structureReport({catalogue:{A:[[1]],B:[[1,0],[0,1]]},observer:[[1]]}),/carrier mismatch/));

// 4. T53 shape on planted forms: indefinite form refused as a square with an exact negative witness; zero-diagonal form handled by the exact pivot repair.
check('indefinite_form_has_negative_witness_and_is_not_a_square',()=>{const T=M([[1,0],[0,-2]]),f=s.congruenceDiagonalize(T);assert.deepEqual(f.inertia,{n_plus:1,n_zero:0,n_minus:1});assert(f.witness.value.eq(new Cut(-2)));assert.equal(s.cutSquareFactorization(T).status,'NOT_A_CUT_SQUARE');});
check('zero_diagonal_form_pivot_repair_and_determinant_channel',()=>{const T=M([[0,[1,1]],[[1,-1],0]]),f=s.congruenceDiagonalize(T);assert.deepEqual(f.inertia,{n_plus:1,n_zero:0,n_minus:1});assert(f.weight_product.eq(new Cut(-2)));assert(s.determinant(T).eq(new Cut(-2)));assert(f.weights.every(w=>w.turn.zero()));});
check('random_cut_squares_factor_with_nonnegative_weights',()=>{let seed=12345n;const rnd=()=>{seed=(seed*6364136223846793005n+1442695040888963407n)%(2n**64n);return Number(seed%7n)-3;};
  for(let t=0;t<24;t++){const n=2+(t%3);const X=Array.from({length:n},()=>Array.from({length:n},()=>[rnd(),rnd()]));const S=mul(dagger(M(X)),M(X));const f=s.cutSquareFactorization(S);assert.equal(f.status,'CUT_SQUARE');assert.equal(f.rank,rank(M(X)));assert(f.weight_product.eq(s.determinant(S)));counts.random_cut_squares++;}});

// 5. Seam-count reading is a pencil statement: on the turn instance K equals P exactly, so the count flips at 1 although the weights are (1/3,0).
check('weights_are_not_pencil_thresholds',()=>{const r=s.structureReport({...instances.turn_observer_2,thresholds:['1/3','1/2','1','3/2']});assert.deepEqual(r.returning_memory_form.weights.map(w=>w.rad.toString()),['1/3','0']);assert.deepEqual(r.seam_count_reading.map(x=>x.n_plus),[1,1,0,0]);});

// 6. Forward multiplicativity (R3-A) is a theorem of the completed observer, not of the raw observer: the raw projector of the EMK instance leaks forward.
check('raw_observer_is_not_forward_closed',()=>{const C=M([[1,0]]),{P}=s.retainedProjector(C),Q=sub(I(2),P),R=M([[0,-1],[1,0]]);assert(!isZero(mul(mul(P,R),Q)));});

const root=__dirname,inputs=['structure_report.cjs','instances.cjs','verify.cjs','mutate.cjs','THEOREM.md','README.md','LINEAGE.json','../../operator_foundation/core/native_operator.cjs'];
const hashes=Object.fromEntries(inputs.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]));
const result={protocol:'RKF_STRUCTURE_REPORT_R3',status:'PASS_EXACT_FINITE_CHECKS',check_count:checks.length,checks,counts,results:data,source_sha256:hashes,scope:{general_theorems:'THEOREM.md',finite_declared_carrier:true,encoding_is_supplied_data:true,primitive_hilbert_space:false,dagger_is_native_reversal_not_transpose:true,infinite_limit_invoked:false,exact_finite_tests_are_not_universal_proofs:true,runtime_string_pinned:false}};
const text=JSON.stringify(result,null,2)+'\n',hash=crypto.createHash('sha256').update(text).digest('hex'),file=path.join(root,'RESULT.json'),pin=path.join(root,'EXPECTED.sha256');
if(process.argv.includes('--write')){fs.writeFileSync(file,text);fs.writeFileSync(pin,hash+'\n');}else if(process.argv.includes('--check')){assert.equal(fs.readFileSync(file,'utf8'),text,'Source/evidence drift');assert.equal(fs.readFileSync(pin,'utf8').trim(),hash,'Pin mismatch');}
console.log(JSON.stringify({protocol:result.protocol,status:result.status,check_count:checks.length,counts,verdicts:Object.fromEntries(Object.entries(data.instances).map(([k,v])=>[k,v.verdict])),certificate_sha256:hash,runtime:process.version},null,2));
