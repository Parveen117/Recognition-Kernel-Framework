'use strict';
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const faults=[
 {name:'fake_finite_language',from:"status:'INFINITE_IRREDUCIBLE_LANGUAGE'",to:"status:'COMPLETE_FINITE_NORMAL_BASIS'"},
 {name:'invent_centralizer_dimension',from:'dimension:kernel.length,coordinates:kernel',to:'dimension:kernel.length+1,coordinates:kernel'},
 {name:'accept_tampered_result',from:'if(digest(fresh)!==digest(packet))',to:'if(false && digest(fresh)!==digest(packet))'}
];
const results=[];
for(const f of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-workbench-mutation-'));try{
 fs.cpSync(root,tmp,{recursive:true,filter:src=>!src.includes(path.sep+'sources'+path.sep)});
 const file=path.join(tmp,'core/workbench.cjs'),text=fs.readFileSync(file,'utf8');assert.equal(text.split(f.from).length,2,'Unique mutation anchor');fs.writeFileSync(file,text.replace(f.from,f.to));
 const r=cp.spawnSync(process.execPath,[path.join(tmp,'tests/verify_workbench.cjs')],{encoding:'utf8',timeout:30000});
 assert(r.status!==null,'Mutation must finish, not time out');assert.notEqual(r.status,0,'Tests must reject '+f.name);results.push({mutation:f.name,rejected:true,exit_status:r.status});
}finally{fs.rmSync(tmp,{recursive:true,force:true});}}
console.log(JSON.stringify({protocol:'NATIVE_WORKBENCH_MUTATIONS_V0_4',status:'PASS',controls:results,original_sources_modified:false}));
