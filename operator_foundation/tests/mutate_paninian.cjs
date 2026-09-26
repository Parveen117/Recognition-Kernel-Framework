'use strict';
/** Mathematical mutation controls run on temporary copies, never the source tree. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const faults=[
 {name:'commutator_sign',from:'function bracket(a,b){return a.times(b).minus(b.times(a));}',to:'function bracket(a,b){return a.times(b).plus(b.times(a));}'},
 {name:'priority_false_confluence',from:'provesConfluence:false',to:'provesConfluence:true',all:true},
 {name:'lopa_drops_memory',from:"ledger=state.ledger.concat(markersToErase.map(m=>({kind:'lopa-memory',marker:m})))",to:'ledger=state.ledger'},
 {name:'wrong_exponential_factorials',from:'factor*=BigInt(k);',to:'factor*=1n;'}
];
const result=[];
for(const f of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'paninian-fault-'));try{
 fs.cpSync(root,tmp,{recursive:true});const p=path.join(tmp,'core/paninian_operator.cjs'),src=fs.readFileSync(p,'utf8');assert(src.includes(f.from));if(!f.all)assert.equal(src.split(f.from).length,2);
 fs.writeFileSync(p,f.all?src.split(f.from).join(f.to):src.replace(f.from,f.to));
 const r=cp.spawnSync(process.execPath,[path.join(tmp,'tests/verify_paninian.cjs')],{encoding:'utf8',timeout:45000});
 assert(r.status!==null,'Mutation must complete');assert.notEqual(r.status,0,'A mathematical assertion must reject '+f.name);
 result.push({mutation:f.name,rejected:true,exit_status:r.status});
}finally{fs.rmSync(tmp,{recursive:true,force:true});}}
console.log(JSON.stringify({protocol:'NATIVE_PANINIAN_MUTATIONS_V0_3',status:'PASS',controls:result,source_tree_modified:false},null,2));
