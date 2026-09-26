'use strict';
/** Negative-control executions on temporary copies; source and pins stay intact. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const faults=[
 {name:'iota_square_wrong_sign',file:'core/native_operator.cjs',from:'this.rad.mul(x.rad).sub(this.turn.mul(x.turn))',to:'this.rad.mul(x.rad).add(this.turn.mul(x.turn))'},
 {name:'derivative_multiplicity_dropped',file:'core/native_laurent.cjs',from:'[k-1,scale(x,k)]',to:'[k-1,scale(x,1)]'},
 {name:'integer_sheet_wrongly_reduced_mod_two',file:'core/native_paths.cjs',from:'sheet(k).toString()',to:'(sheet(k)%2n).toString()'}
];
const result=[];
for(const f of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'native-mutation-'));try{fs.cpSync(root,tmp,{recursive:true});const target=path.join(tmp,f.file),src=fs.readFileSync(target,'utf8');assert.equal(src.split(f.from).length,2,'Mutation anchor must occur exactly once');fs.writeFileSync(target,src.replace(f.from,f.to));const r=cp.spawnSync(process.execPath,[path.join(tmp,'tests/verify.cjs'),'--write'],{encoding:'utf8',timeout:30000});assert.notEqual(r.status,0,'Mathematical tests must reject '+f.name);assert(r.status!==null,'Mutation execution must finish');result.push({mutation:f.name,rejected:true,exit_status:r.status,reason:'Mathematical assertion or identity check failed before evidence write'});}finally{fs.rmSync(tmp,{recursive:true,force:true});}}
console.log(JSON.stringify({protocol:'NATIVE_OPERATOR_MUTATION_CONTROLS_V0_2',status:'PASS',controls:result,original_files_modified:false},null,2));
