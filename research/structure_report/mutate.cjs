'use strict';
/** Mathematical fault controls in temporary copies of structure_report.cjs; the live source is never edited. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..'),out=[];
const faults=[
 ['transpose_instead_of_native_dagger_in_mark','const sq=mul(mul(dagger(leak),B),leak);','const sq=mul(mul(transposeOnly(leak),B),leak);'],
 ['skip_observer_completion_use_raw_observer','const {P,gram}=retainedProjector(D,pairing)','const {P,gram}=retainedProjector(C,pairing)'],
 ['transpose_projector_is_not_self_dagger','const Dd=dagger(D),G=mul(mul(D,pairing.Binv),Dd);','const Dd=transposeOnly(D),G=mul(mul(D,pairing.Binv),Dd);'],
 ['forward_leak_mistaken_for_the_mark','const leak=mul(mul(Q,g.m),P);','const leak=mul(mul(P,g.m),Q);'],
 ['accept_negative_weights_as_a_square',"if(f.inertia.n_minus>0)return {status:'NOT_A_CUT_SQUARE',...f};","if(false)return {status:'NOT_A_CUT_SQUARE',...f};"],
 ['odd_part_defined_as_even_part',"odd:scale(sub(s,c),'1/2')","odd:scale(add(s,c),'1/2')"],
 ['pivot_repair_with_daggered_coefficient','const c=A[k][t];applyRowOp','const c=A[k][t].dagger();applyRowOp']
];
for(const [name,from,to] of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-structure-fault-'));try{
 const target=path.join(tmp,'research/structure_report');fs.mkdirSync(path.join(tmp,'operator_foundation/core'),{recursive:true});fs.cpSync(__dirname,target,{recursive:true});
 fs.copyFileSync(path.join(root,'operator_foundation/core/native_operator.cjs'),path.join(tmp,'operator_foundation/core/native_operator.cjs'));
 const file=path.join(target,'structure_report.cjs'),text=fs.readFileSync(file,'utf8');assert.equal(text.split(from).length,2,'Unique mutation anchor required: '+name);fs.writeFileSync(file,text.replace(from,to));
 const r=cp.spawnSync(process.execPath,[path.join(target,'verify.cjs'),'--write'],{cwd:tmp,encoding:'utf8',timeout:60000});assert(r.status!==null,'Control must finish');assert.notEqual(r.status,0,'Mathematical fault escaped: '+name);
 const reason=(r.stderr.match(/Error: ([^\n]*)|AssertionError[^\n]*\n?([^\n]*)/)||[])[1]||'assertion';out.push({fault:name,rejected:true,exit_code:r.status,first_failure:reason.slice(0,160)});
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}}
const report={protocol:'RKF_STRUCTURE_REPORT_MUTATIONS_R3',controls:out,live_files_modified:false};
if(process.argv.includes('--write'))fs.writeFileSync(path.join(__dirname,'MUTATIONS.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
