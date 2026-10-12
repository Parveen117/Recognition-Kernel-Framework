'use strict';
/** Mathematical fault controls for R4 in temporary copies of repair.cjs; the live source is never edited. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../../..'),out=[];
const faults=[
 ['repair_with_forward_completion_instead_of_reversed','const Dsharp=before.observer.completed_observer_sharp;','const Dsharp=before.observer.completed_observer;'],
 ['ym37_pairing_silently_dropped','if(pairing)job.pairing=B;','if(false)job.pairing=B;'],
 ['ym37_transfer_on_the_wrong_side','const tau=mul(inverse(B),M);','const tau=mul(M,inverse(B));']
];
for(const [name,from,to] of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-repair-fault-'));try{
 const target=path.join(tmp,'research/structure_report/r4');fs.mkdirSync(path.join(tmp,'operator_foundation/core'),{recursive:true});fs.mkdirSync(path.join(tmp,'research/structure_report'),{recursive:true});
 fs.cpSync(__dirname,target,{recursive:true});for(const f of ['structure_report.cjs','instances.cjs'])fs.copyFileSync(path.join(root,'research/structure_report',f),path.join(tmp,'research/structure_report',f));
 fs.copyFileSync(path.join(root,'operator_foundation/core/native_operator.cjs'),path.join(tmp,'operator_foundation/core/native_operator.cjs'));
 const file=path.join(target,'repair.cjs'),text=fs.readFileSync(file,'utf8');assert.equal(text.split(from).length,2,'Unique mutation anchor required: '+name);fs.writeFileSync(file,text.replace(from,to));
 const r=cp.spawnSync(process.execPath,[path.join(target,'verify.cjs'),'--write'],{cwd:tmp,encoding:'utf8',timeout:120000});assert(r.status!==null,'Control must finish');assert.notEqual(r.status,0,'Mathematical fault escaped: '+name);
 const reason=(r.stderr.match(/Error: ([^\n]*)|AssertionError[^\n]*\n?([^\n]*)/)||[])[1]||'assertion';out.push({fault:name,rejected:true,exit_code:r.status,first_failure:reason.slice(0,160)});
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}}
const report={protocol:'RKF_STRUCTURE_REPAIR_MUTATIONS_R4',controls:out,live_files_modified:false};
if(process.argv.includes('--write'))fs.writeFileSync(path.join(__dirname,'MUTATIONS.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
