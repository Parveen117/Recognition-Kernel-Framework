'use strict';
/** Exact finite checks for R4: the repair step on every R3 instance, basis covariance of the declared-pairing verdicts, and the YM-37 pencil encoding. */
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const o=require('../../../operator_foundation/core/native_operator.cjs'),s=require('../structure_report.cjs'),r4=require('./repair.cjs'),instances=require('../instances.cjs');
const {F,matrix:M,identity:I,mul,dagger,equal,inverse,rank}=o;
const checks=[],data={repairs:{},ym37:{}},counts={repairs:0,minimality_probes:0,covariance_instances:0};
function check(name,fn){fn();checks.push(name);}

// 1. Repair on every named instance: one step, mark gone, idempotent, cost = dagger_extra, finite minimality probes pass.
for(const [name,inst] of Object.entries(instances)){check('repair_'+name,()=>{const {expect,...job}=inst;const r=r4.repairReport(job);
  assert.equal(r.after.verdict,'VISIBLE_LOCAL');assert.equal(r.after.returning_rank,0);assert.equal(r.cost_channels,r.before.dagger_extra);assert.equal(r.before.verdict,expect.verdict);
  counts.repairs++;counts.minimality_probes+=r.minimality_probe.length;
  data.repairs[name]={before:r.before.verdict,forward_rank:r.before.forward_rank,repaired_rank:r.before.dagger_rank,cost_channels:r.cost_channels,after:r.after.verdict,probes:r.minimality_probe.map(p=>[p.removed_row,p.forward_rank,p.mark])};});}

// 2. Basis covariance: a change of basis x -> G x carries (S, C, L, B) to (G S G^-1, C G^-1, L G^-1, G^-dagger B G^-1); every native verdict is unchanged under the declared pairing.
check('declared_pairing_verdicts_are_basis_covariant',()=>{const G3=M([[1,2,0],[0,1,[0,1]],[1,0,1]]),G4=M([[1,1,0,0],[0,1,0,[1,1]],[2,0,1,0],[0,0,1,1]]),G2=M([[1,[0,1]],[0,1]]);
  for(const name of ['one_way_flow_2','turn_observer_2','cut_misaligned_observer_3','cut_faces_two_strengths_4','block_local_3']){const {expect,...job}=instances[name];const n=M(job.observer)[0].length;const G={2:G2,3:G3,4:G4}[n],Gi=inverse(G),Bp=mul(mul(dagger(Gi),I(n)),Gi);
    const moved={catalogue:Object.fromEntries(Object.entries(job.catalogue).map(([k,v])=>[k,mul(mul(G,M(v)),Gi)])),observer:mul(M(job.observer),Gi),pairing:Bp,thresholds:job.thresholds};
    if(job.target)moved.target=mul(M(job.target),Gi);if(job.cut)moved.cut=mul(mul(G,M(job.cut)),Gi);
    const a=s.structureReport(job),b=s.structureReport(moved);
    assert.equal(a.verdict,b.verdict);assert.equal(a.observer.forward_rank,b.observer.forward_rank);assert.equal(a.observer.dagger_rank,b.observer.dagger_rank);assert.equal(a.returning_memory_form.rank,b.returning_memory_form.rank);
    assert(a.returning_memory_form.sum_of_leak_energies.eq(b.returning_memory_form.sum_of_leak_energies));
    for(const g of Object.keys(job.catalogue))assert(a.returning_memory.generators[g].leak_energy.eq(b.returning_memory.generators[g].leak_energy));
    if(a.seam_count_reading)assert.deepEqual(a.seam_count_reading.map(x=>x.n_plus),b.seam_count_reading.map(x=>x.n_plus));
    counts.covariance_instances++;}});
check('coordinate_dagger_is_not_basis_covariant',()=>{const {expect,...job}=instances.one_way_flow_2;const G=M([[2,1],[1,1]]),Gi=inverse(G);
  const moved={catalogue:{S:mul(mul(G,M(job.catalogue.S)),Gi)},observer:mul(M(job.observer),Gi),thresholds:job.thresholds};const a=s.structureReport(job),b=s.structureReport(moved);
  assert(!a.returning_memory_form.sum_of_leak_energies.eq(b.returning_memory_form.sum_of_leak_energies));assert.notDeepEqual(a.seam_count_reading.map(x=>x.n_plus),b.seam_count_reading.map(x=>x.n_plus));
  const c=s.structureReport({...moved,pairing:mul(dagger(Gi),Gi)});assert(c.returning_memory_form.sum_of_leak_energies.eq(a.returning_memory_form.sum_of_leak_energies));assert.deepEqual(c.seam_count_reading.map(x=>x.n_plus),a.seam_count_reading.map(x=>x.n_plus));
  data.coordinate_dagger_moved={original_energy:a.returning_memory_form.sum_of_leak_energies.toString(),moved_without_pairing_energy:b.returning_memory_form.sum_of_leak_energies.toString(),moved_with_transported_pairing_energy:c.returning_memory_form.sum_of_leak_energies.toString(),original_seam:a.seam_count_reading.map(x=>x.n_plus),moved_without_pairing_seam:b.seam_count_reading.map(x=>x.n_plus)};});

// 3. YM-37 pencil: declared data integrity, self-sharp transfer, local verdict under the Haar pairing, spurious mark under the coordinate dagger.
check('ym37_declared_data_is_a_symmetric_pencil_with_positive_pairing',()=>{const {data:d}=r4.ym37Job();assert.equal(d.dimension,8);assert(equal(d.M,dagger(d.M)));assert(equal(d.B,dagger(d.B)));assert(equal(d.N,dagger(d.N)));
  const p=s.declaredPairing(d.B,8);assert(p.weights.every(w=>w.rad.n>0n));const raw=r4.loadYm37();assert.deepEqual(raw.basis_monomials[raw.constant_index],{'(0, 0, 0, 0, 0, 0, 0, 0)':'1'});data.ym37.pairing_weights=p.weights.map(w=>w.rad.toString());});
check('ym37_transfer_is_self_sharp_but_not_self_dagger',()=>{const {data:d}=r4.ym37Job();const Binv=inverse(d.B);assert(equal(d.tau,mul(mul(Binv,dagger(d.tau)),d.B)));assert(!equal(d.tau,dagger(d.tau)));});
check('ym37_boundary_with_insertion_under_declared_pairing',()=>{const {job}=r4.ym37Job({pairing:true});const r=s.structureReport(job);
  assert.equal(r.verdict,'HIDDEN_LOCAL');assert.deepEqual(r.observer.forward_ladder,[2,4,6]);assert.equal(r.observer.forward_rank,6);assert.equal(r.observer.dagger_extra,0);assert.equal(r.returning_memory_form.rank,0);
  data.ym37.boundary_with_insertion={verdict:r.verdict,seed_rank:r.observer.seed_rank,forward_ladder:r.observer.forward_ladder,forward_rank:r.observer.forward_rank,invisible_directions:8-r.observer.forward_rank,dagger_extra:r.observer.dagger_extra,returning_rank:r.returning_memory_form.rank};});
check('ym37_constant_coefficient_readout_under_declared_pairing',()=>{const {job}=r4.ym37Job({pairing:true,readout:'constant_coefficient'});const r=s.structureReport(job);
  assert.equal(r.verdict,'HIDDEN_LOCAL');assert.equal(r.observer.forward_rank,7);assert.equal(r.observer.dagger_extra,0);data.ym37.constant_coefficient={verdict:r.verdict,forward_rank:r.observer.forward_rank,invisible_directions:8-r.observer.forward_rank};});
check('ym37_coordinate_dagger_shadow_is_a_spurious_mark',()=>{const {job}=r4.ym37Job({pairing:false});const r=r4.repairReport(job);
  assert.equal(r.before.verdict,'GLOBAL_RETURNING_MEMORY');assert.equal(r.before.dagger_extra,1);assert.equal(r.before.returning_rank,1);assert(r.before.returning_energy.eq(new F('1618373069/1180672000000')));assert.equal(r.after.verdict,'VISIBLE_LOCAL');assert.equal(r.cost_channels,1);
  data.ym37.coordinate_dagger_shadow={verdict:r.before.verdict,dagger_extra:r.before.dagger_extra,spurious_mark_energy:r.before.returning_energy.toString(),repair_cost:r.cost_channels,label:'CONTROL: coordinate transpose on a non-label basis, not a Yang-Mills statement'};});
check('ym37_native_repair_costs_nothing',()=>{const {job}=r4.ym37Job({pairing:true});const r=r4.repairReport(job);assert.equal(r.cost_channels,0);assert.equal(r.after.verdict,'VISIBLE_LOCAL');});

const root=__dirname,inputs=['repair.cjs','verify.cjs','mutate.cjs','THEOREM.md','README.md','LINEAGE.json','ym37_pencil_t2.json','../structure_report.cjs','../instances.cjs','../../../operator_foundation/core/native_operator.cjs'];
const hashes=Object.fromEntries(inputs.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]));
const result={protocol:'RKF_STRUCTURE_REPAIR_R4',status:'PASS_EXACT_FINITE_CHECKS',check_count:checks.length,checks,counts,results:data,source_sha256:hashes,scope:{general_theorems:'THEOREM.md',finite_declared_carrier:true,encoding_is_supplied_data:true,ym37_pencil_consumed_by_pin_not_rederived:true,yang_mills_gap_or_continuum_claim:false,primitive_hilbert_space:false,pairing_used_only_as_declared_cut_square:true,infinite_limit_invoked:false,exact_finite_tests_are_not_universal_proofs:true,runtime_string_pinned:false}};
const text=JSON.stringify(result,null,2)+'\n',hash=crypto.createHash('sha256').update(text).digest('hex'),file=path.join(root,'RESULT.json'),pin=path.join(root,'EXPECTED.sha256');
if(process.argv.includes('--write')){fs.writeFileSync(file,text);fs.writeFileSync(pin,hash+'\n');}else if(process.argv.includes('--check')){assert.equal(fs.readFileSync(file,'utf8'),text,'Source/evidence drift');assert.equal(fs.readFileSync(pin,'utf8').trim(),hash,'Pin mismatch');}
console.log(JSON.stringify({protocol:result.protocol,status:result.status,check_count:checks.length,counts,ym37:data.ym37,certificate_sha256:hash,runtime:process.version},null,2));
