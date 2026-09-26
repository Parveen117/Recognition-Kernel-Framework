'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const o=require('../core/native_operator.cjs'),m=require('../core/paninian_operator.cjs'),paths=require('../core/native_paths.cjs');
const {Cut,F,matrix:M,identity:I,zeros:Z,mul,add,scale,equal,rank,flatten}=o;
const {Presentation,Expr,Budget,bracket,star,daggerGate,derivationGate,polynomialDerivative,formalExp,formalLog,seriesMultiply,matrixValue,representationGate,ledgerBeforeLopa,resolvePriority,replayCompletion,digest,stable}=m;
const checks=[],details={};let wordCount=0;
function check(name,fn){fn();checks.push(name);}function eq(a,b){assert(a.equals(b));}function meq(a,b){assert(equal(a,b));}
const clone=x=>JSON.parse(JSON.stringify(x));
const emkSpec={tokens:['R','K'],rules:[{id:'RR',lhs:['R','R'],rhs:[[[],-1]],source:'RKF T48: R^2=-I'},{id:'KK',lhs:['K','K'],rhs:[[[],1]],source:'RKF T48: K^2=I'},{id:'KR',lhs:['K','R'],rhs:[[['R','K'],-1]],source:'RKF T48: KR=-RK'}]};
const s=new Presentation(emkSpec),r=s.word(['R']),k=s.word(['K']),unit=s.one(),nf=e=>s.reduce(e).normal;
const repr={R:M([[0,-1],[1,0]]),K:M([[0,1],[1,0]])};
check('EMK_all_critical_pairs_close',()=>{const a=s.audit();assert.equal(a.status,'CONFLUENT_BY_CHECKED_DIAMONDS');assert.equal(a.criticalPairs,4);for(const d of a.resolutions){s.replay(d.left);s.replay(d.right);}details.EMK={critical_pairs:a.criticalPairs,normal_basis:[[],['R'],['K'],['R','K']],audit_status:a.status};});
check('EMK_faithful_finite_realization',()=>{const g=representationGate(s,repr,2,[[],['R'],['K'],['R','K']]);assert.equal(g.status,'REPRESENTATION_RESPECTS_RELATIONS');assert.equal(g.independentProvidedImages,4);});
check('matrix_backend_rejects_wrong_representation',()=>assert.equal(representationGate(s,{R:I(2),K:repr.K},2).status,'RELATION_VIOLATION'));
check('KRKR_reduces_to_identity_with_replay',()=>{const a=s.reduce(s.word(['K','R','K','R']),{witness:true});eq(a.normal,unit);assert(s.replay(a.certificate));details.KRKR={result:a.normal.toJSON(),proof_steps:a.steps};});
check('commutator_is_signed_not_erased',()=>eq(nf(bracket(r,k)),r.times(k).scale(2)));
function* words(alphabet,depth,prefix=[]){yield prefix;if(depth)for(const t of alphabet)yield* words(alphabet,depth-1,prefix.concat(t));}
for(let length=0;length<=9;length++)check('EMK_all_words_exact_length_'+length,()=>{
  for(const w of words(['R','K'],length)){if(w.length!==length)continue;const x=s.word(w),a=s.reduce(x,{strategy:'first',witness:true}),b=s.reduce(x,{strategy:'last'});eq(a.normal,b.normal);assert(s.replay(a.certificate));meq(matrixValue(x,repr,2),matrixValue(a.normal,repr,2));assert(a.normal.entries().every(([v])=>v.length<=2));wordCount++;}
});
const dg={R:r.scale(-1),K:k};
check('source_dagger_descends',()=>assert.equal(daggerGate(s,dg).status,'DAGGER_DESCENDS'));
check('wrong_dagger_rejected_by_relation',()=>assert.equal(daggerGate(s,{R:k,K:r}).status,'DAGGER_NOT_RELATION_STABLE'));
for(let i=0;i<16;i++){
 const x=r.scale(new Cut(i-4,'1/3')).plus(k.scale(new Cut('2/5',1))),y=r.times(k).plus(unit.scale(i+1));
 check('exact_polynomial_and_dagger_'+i,()=>{eq(nf(x.times(y)),nf(nf(x).times(nf(y))));eq(nf(star(x.times(y),dg)),nf(star(y,dg).times(star(x,dg))));eq(nf(star(star(x,dg),dg)),nf(x));meq(matrixValue(x.times(y),repr,2),matrixValue(nf(x.times(y)),repr,2));});
}
const deriv={R:bracket(k,r),K:bracket(k,k)};
check('inner_derivation_preserves_defining_relations',()=>assert.equal(derivationGate(s,deriv).status,'DERIVATION_DESCENDS'));
check('arbitrary_generator_derivative_is_not_automatically_lawful',()=>assert.equal(derivationGate(s,{R:unit,K:s.zero()}).status,'RELATION_NOT_PRESERVED'));
check('symbolic_Leibniz',()=>{const x=r.plus(k),y=r.times(k).plus(unit);eq(nf(polynomialDerivative(x.times(y),deriv)),nf(polynomialDerivative(x,deriv).times(y).plus(x.times(polynomialDerivative(y,deriv)))));});
check('symbolic_Jacobi',()=>eq(nf(bracket(r,bracket(k,r.times(k))).plus(bracket(k,bracket(r.times(k),r))).plus(bracket(r.times(k),bracket(r,k)))),s.zero()));
const forkSpec={tokens:['C','D','A','B'],rules:[{id:'AB',lhs:['A','B'],rhs:[[['C'],1]],source:'declared overlap fixture'},{id:'BC',lhs:['B','C'],rhs:[[['D'],1]],source:'declared overlap fixture'}]};
const f=new Presentation(forkSpec),x=f.word(['A','B','C']);
check('priority_is_not_a_confluence_proof',()=>{assert(!f.reduce(x,{strategy:'first'}).normal.equals(f.reduce(x,{strategy:'last'}).normal));assert.equal(f.audit().status,'OPEN_CRITICAL_PAIRS');assert.equal(resolvePriority([{id:'AB',priority:2},{id:'BC',priority:1}]).provesConfluence,false);});
check('strict_priority_ties_stay_open',()=>assert.equal(resolvePriority([{id:'AB',priority:2},{id:'BC',priority:2}]).status,'OPEN_TIE'));
check('completion_budget_is_not_false_PASS',()=>assert.equal(new Presentation(forkSpec).complete({maxNewRules:0}).status,'COMPLETION_BUDGET_EXHAUSTED'));
let completion;
check('derived_critical_pair_completion',()=>{completion=f.complete();assert.equal(completion.status,'CONFLUENT_BY_CHECKED_DIAMONDS');assert.equal(completion.derivations.length,1);assert.equal(replayCompletion(forkSpec,completion).hash(),f.hash());eq(f.reduce(x,{strategy:'first'}).normal,f.reduce(x,{strategy:'last'}).normal);details.completion={added_relations:completion.derivations.map(a=>a.rule),status:completion.status};});
check('completion_proof_rejects_tampered_new_relation',()=>{const q=clone(completion);q.derivations[0].rule.rhs[0][1]=['2','0'];assert.throws(()=>replayCompletion(forkSpec,q),/not derived/);});
check('completion_proof_rejects_fake_fork',()=>{const q=clone(completion);q.derivations[0].pair.word=['A','A'];assert.throws(()=>replayCompletion(forkSpec,q),/Fabricated/);});
check('completion_rejects_nonzero_local_unit_collapse',()=>{const a=new Presentation({tokens:['X'],rules:[{id:'one',lhs:['X'],rhs:[[[],1]],source:'fixture'},{id:'zero',lhs:['X'],rhs:[],source:'fixture'}]});assert.equal(a.complete().status,'LOCAL_UNIT_COLLAPSE');});
check('inclusion_ambiguity_checked',()=>{const a=new Presentation({tokens:['X','Y'],rules:[{id:'X',lhs:['X'],rhs:[[[],1]],source:'fixture'},{id:'XX',lhs:['X','X'],rhs:[[['Y'],1]],source:'fixture'}]});assert(a.ambiguities().some(x=>x.kind==='inclusion'));assert.equal(a.audit().status,'OPEN_CRITICAL_PAIRS');});
check('no-rule_free_algebra_is_not_forced_commutative',()=>{const a=new Presentation({tokens:['A','B']});assert.equal(a.audit().status,'CONFLUENT_BY_CHECKED_DIAMONDS');assert(a.reduce(bracket(a.word(['A']),a.word(['B']))).normal.terms.size===2);});
check('reduction_budget_fails_closed',()=>assert.throws(()=>s.reduce(r.times(r),{maxSteps:0}),Budget));
check('audit_budget_is_incomplete_not_PASS',()=>assert.equal(s.audit({maxSteps:0}).status,'INCOMPLETE'));
check('term_budget_fails_closed',()=>assert.throws(()=>s.reduce(r.plus(k),{maxTerms:1}),Budget));
check('reject_length_increasing_rule',()=>assert.throws(()=>new Presentation({tokens:['R'],rules:[{id:'bad',lhs:['R'],rhs:[[['R','R'],1]],source:'fixture'}]}),/decreasing/));
check('reject_same_word_loop',()=>assert.throws(()=>new Presentation({tokens:['R'],rules:[{id:'bad',lhs:['R'],rhs:[[['R'],1]],source:'fixture'}]}),/decreasing/));
check('reject_unbound_rule_source',()=>assert.throws(()=>new Presentation({tokens:['R'],rules:[{id:'bad',lhs:['R'],rhs:[]}]}),/source/));
check('reject_float_coefficient',()=>assert.throws(()=>s.word(['R'],0.1),TypeError));
check('reject_unknown_token',()=>assert.throws(()=>s.word(['MISSING']),TypeError));
check('reject_empty_leading_word',()=>assert.throws(()=>s.addRule({id:'empty',lhs:[],rhs:[],source:'fixture'}),TypeError));
check('reject_duplicate_rule_ID',()=>assert.throws(()=>s.addRule(emkSpec.rules[0]),TypeError));
const good=s.reduce(s.word(['K','R','R','K']),{witness:true}).certificate;
check('proof_rejects_wrong_final_output',()=>{const q=clone(good);q.output.terms=[[[],['123','0']]];assert.throws(()=>s.replay(q),/claimed normal form/);});
check('proof_rejects_wrong_applied_coefficient',()=>{const q=clone(good);q.steps[0].coefficient=['2','0'];assert.throws(()=>s.replay(q),/coefficient/);});
check('proof_rejects_wrong_source_hash',()=>{const q=clone(good);q.presentation='0'.repeat(64);assert.throws(()=>s.replay(q),/source hash/);});
check('proof_rejects_missing_step',()=>{const q=clone(good);q.steps=[];assert.throws(()=>s.replay(q),/claimed normal form/);});
const typed=new Presentation({objects:['a','b'],tokens:[{name:'u',from:'a',to:'b',charge:1},{name:'du',from:'b',to:'a',charge:-1},{name:'v',from:'a',to:'b',charge:0}],rules:[{id:'du_u',lhs:['du','u'],rhs:[[[],1]],source:'native typed bridge'},{id:'u_du',lhs:['u','du'],rhs:[[[],1]],source:'native typed bridge'}]});
check('typed_bridge_normalizer_confluence',()=>assert.equal(typed.audit().status,'CONFLUENT_BY_CHECKED_DIAMONDS'));
check('typed_two_local_identities_distinct',()=>{assert(!typed.one('a').equals(typed.one('b')));eq(typed.reduce(typed.word(['du','u'])).normal,typed.one('a'));eq(typed.reduce(typed.word(['u','du'])).normal,typed.one('b'));});
check('typed_mismatched_middle_object_rejected',()=>assert.throws(()=>typed.word(['u','u']),/Noncomposable/));
check('typed_product_rejects_unmatched_middle',()=>assert.throws(()=>typed.word(['u']).times(typed.word(['v'])),/middle/));
check('typed_sum_rejects_incompatible_carriers',()=>assert.throws(()=>typed.word(['u']).plus(typed.word(['du'])),/sum/));
check('typed_dagger_reverses_arrows',()=>eq(star(typed.word(['u']),{u:typed.word(['du'])}),typed.word(['du'])));
check('native_sheet_erasure_rule_rejected',()=>assert.throws(()=>typed.addRule({id:'erase',lhs:['u','du','u'],rhs:[[['v'],1]],source:'planted wrong erasure'}),/integer residue/));
check('same_endpoints_do_not_imply_same_native_word',()=>assert(!typed.reduce(typed.word(['u'])).normal.equals(typed.reduce(typed.word(['v'])).normal)));
check('sparse_path_backend_retains_sheet_difference',()=>{const a=paths.arrow('b','a',1),b=paths.arrow('b','a',0);assert(!a.eq(b));assert(o.isZero(a.sub(b).endpointShadow(['a','b'])));assert(a.sub(b).coefficientEnergy().eq(2));});
const state={surface:'affix',markers:['it_A','it_B'],ledger:[]};
check('lopa_records_memory_before_surface_erasure',()=>{const t=ledgerBeforeLopa(state,['it_A']);assert.deepEqual(t.markers,['it_B']);assert.deepEqual(t.ledger,[{kind:'lopa-memory',marker:'it_A'}]);assert.deepEqual(state.markers,['it_A','it_B']);});
check('same_lopa_surface_can_have_different_memory',()=>{const a=ledgerBeforeLopa({surface:'x',markers:['A'],ledger:[]},['A']),b=ledgerBeforeLopa({surface:'x',markers:['B'],ledger:[]},['B']);assert.equal(a.surface,b.surface);assert.notDeepEqual(a.ledger,b.ledger);});
check('lopa_cannot_invent_missing_marker',()=>assert.throws(()=>ledgerBeforeLopa(state,['absent']),/absent/));
check('lopa_rejects_duplicate_erasure',()=>assert.throws(()=>ledgerBeforeLopa(state,['it_A','it_A']),/duplicate/));
const cut=new Presentation({tokens:['E','O','J'],rules:[{id:'JJ',lhs:['J','J'],rhs:[[[],1]],source:'native cut J^2=I'},{id:'JE',lhs:['J','E'],rhs:[[['E','J'],1]],source:'cut-even E'},{id:'JO',lhs:['J','O'],rhs:[[['O','J'],-1]],source:'cut-odd O'}]});
const E=cut.word(['E']),O=cut.word(['O']),J=cut.word(['J']),G=E.plus(O),degree=4;
check('cut_grading_word_presentation_is_confluent',()=>assert.equal(cut.audit().status,'CONFLUENT_BY_CHECKED_DIAMONDS'));
const exp=formalExp(G,degree),jexp=exp.map(a=>cut.reduce(J.times(a).times(J)).normal),loop=seriesMultiply(jexp,exp,degree),log=formalLog(loop,degree);
check('formal_cut_loop_degree_one',()=>eq(log[1],E.scale(2)));
check('formal_cut_loop_degree_two',()=>eq(log[2],bracket(E,O)));
check('formal_cut_loop_degree_three',()=>eq(log[3],bracket(O,bracket(E,O)).scale(new Cut(new F(-1,3)))));
check('formal_cut_loop_formula_is_matrix_free',()=>{assert(log.slice(0,4).every(a=>a.entries().every(([w])=>!w.includes('J'))));details.formal_cut_loop={modulus:'t^5',coefficients:log.map(x=>x.toJSON()),h1:'2 E',h2:'[E,O]',h3:'-[O,[E,O]]/3'};});
check('odd_only_formal_cut_loop_closes',()=>{const b=formalExp(O,degree),j=b.map(a=>cut.reduce(J.times(a).times(J)).normal),l=seriesMultiply(j,b,degree);eq(l[0],cut.one());assert(l.slice(1).every(e=>e.terms.size===0));});
check('formal_log_rejects_nonidentity_constant',()=>assert.throws(()=>formalLog([E],2),/constant identity/));
check('formal_exp_rejects_noncorner',()=>assert.throws(()=>formalExp(typed.word(['u']),2),/corner/));
const nil=new Presentation({tokens:['N'],rules:[{id:'N2',lhs:['N','N'],rhs:[],source:'v0.2 scalar t^2 jet action'}]});
check('v02_jet_nilpotent_normalization_adapter',()=>{const n=nil.word(['N']),exp=formalExp(n,6);eq(exp[0],nil.one());eq(exp[1],n);assert(exp.slice(2).every(e=>e.terms.size===0));const l=require('../core/native_laurent.cjs'),q=l.localPacket(l.monomial([[1]],2));assert.equal(representationGate(nil,{N:q.action},2).status,'REPRESENTATION_RESPECTS_RELATIONS');});
check('symbolic_equality_carries_a_replayable_proof',()=>{const v=m.proveEquality(bracket(r,k),r.times(k).scale(2));assert.equal(v.status,'EQUAL_IN_DECLARED_QUOTIENT');assert(s.replay(v.certificate));});
check('distinct_normal_forms_are_not_declared_equal',()=>assert.equal(m.proveEquality(r,k).status,'DISTINCT_IN_DECLARED_QUOTIENT'));
check('open_presentation_cannot_certify_equality',()=>{const a=new Presentation(forkSpec);assert.equal(m.proveEquality(a.one(),a.one()).status,'PRESENTATION_NOT_CERTIFIED');});
check('solve_unknown_EMK_commutator_coefficients',()=>{const v=m.solveCoefficients(bracket(r,k),[unit,r,k,r.times(k)]);assert.equal(v.status,'UNIQUE_SOLUTION');assert.deepEqual(v.particular,[['0','0'],['0','0'],['0','0'],['2','0']]);details.symbolic_commutator_coefficients=v.particular;});
check('native_commutant_template_recovers_I_and_K',()=>{const b=[unit,r,k,r.times(k)],v=m.solveCoefficients(s.zero(),b.map(x=>bracket(k,x)));assert.equal(v.status,'AFFINE_SOLUTION_FAMILY');assert.equal(v.nullspace.length,2);for(const row of v.nullspace){let x=s.zero();b.forEach((e,i)=>x=x.plus(e.scale(Cut.of(row[i]))));eq(nf(bracket(k,x)),s.zero());}details.K_commutant_dimension=2;});
check('missing_template_direction_is_not_invented',()=>assert.equal(m.solveCoefficients(r,[unit,k]).status,'NO_SOLUTION_IN_TEMPLATE'));
check('zero_template_retains_affine_freedom',()=>{const v=m.solveCoefficients(s.zero(),[s.zero(),s.zero()]);assert.equal(v.nullspace.length,2);});
const root=path.resolve(__dirname,'..');
const files=['core/paninian_operator.cjs','tests/verify_paninian.cjs','PANINIAN_EXTENSION.md','theory/PANINIAN_OPERATOR_COMPILER.md','audit/PANINIAN_SOURCE_REGISTER.json','audit/PUBLICATIONS_MORPHIC_AUDIT.md','tests/mutate_paninian.cjs','examples/paninian_demo.cjs'];
const report={protocol:'NATIVE_PANINIAN_OPERATOR_V0_3',status:'PASS_EXACT_FINITE_CHECKS',check_count:checks.length,exhaustive_EMK_words:wordCount,checks,details,
  scope:{primitive_Hilbert_space:false,full_Sanskrit_engine:false,unrestricted_completion_termination_claimed:false,finite_matrix_test_is_universal_proof:false,general_written_result:'degree-lex terminating typed monic presentations with all critical ambiguities resolved',v02_architecture_retained_under_canonical_migration:true},
  source_sha256:Object.fromEntries(files.filter(f=>fs.existsSync(path.join(root,f))).map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex')]))};
const text=JSON.stringify(stable(report),null,2)+'\n',hash=crypto.createHash('sha256').update(text).digest('hex');
if(process.argv.includes('--write')){if(report.source_sha256&&Object.keys(report.source_sha256).length!==files.length)throw new Error('Incomplete source manifest');fs.writeFileSync(path.join(root,'audit/PANINIAN_CERTIFICATE.json'),text);fs.writeFileSync(path.join(root,'audit/PANINIAN_EXPECTED.sha256'),hash+'\n');}
if(process.argv.includes('--check')){assert.equal(fs.readFileSync(path.join(root,'audit/PANINIAN_EXPECTED.sha256'),'utf8').trim(),hash);}
console.log('PASS_EXACT_PANINIAN_OPERATOR',checks.length,'CHECKS',wordCount,'EXHAUSTIVE_WORDS',hash);
