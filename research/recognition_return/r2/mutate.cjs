'use strict';
/** Mathematical mutation controls run before certificate hashing; originals stay intact. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../../..');
const faults=[
 ['wrong_native_pair_sign','r=p.sub(q.mul(u))','r=p.add(q.mul(u))'],
 ['reverse_depth_composition','for(let j=xs.length-1;j>=0;j--)x=step(xs[j],x)','for(let j=0;j<xs.length;j++)x=step(xs[j],x)'],
 ['false_tail_width','width.eq(one().div(P.C.mul(P.D)))','width.eq(new F(2).div(P.C.mul(P.D)))'],
 ['drop_quadratic_design_term','A=x.add(B.mul(x.pow(2)))','A=x.add(B.mul(x))'],
 ['declare_every_response_a_cut','exactNativeCut:x.eq(1)','exactNativeCut:true'],
 ['ignore_pair_balance','if(!products[j].eq(products[j+1]))','if(false)']
];
const controls=[];
for(const [name,from,to] of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-r2-mutation-'));try{
 for(const rel of ['operator_foundation/core/native_operator.cjs','operator_foundation/core/paninian_operator.cjs','research/recognition_return/return_solver.cjs']){fs.mkdirSync(path.dirname(path.join(tmp,rel)),{recursive:true});fs.copyFileSync(path.join(root,rel),path.join(tmp,rel));}
 const dest=path.join(tmp,'research/recognition_return/r2');fs.cpSync(__dirname,dest,{recursive:true});const file=path.join(dest,'variable_return.cjs'),src=fs.readFileSync(file,'utf8');assert.equal(src.split(from).length,2,'Unique mutation anchor required');fs.writeFileSync(file,src.replace(from,to));
 const r=cp.spawnSync(process.execPath,[path.join(dest,'verify.cjs'),'--assert-only'],{encoding:'utf8',timeout:40000});assert(r.status!==null,'Mutation execution must finish');assert.notEqual(r.status,0,'Fault escaped: '+name);assert(/AssertionError|Error:/.test(r.stderr),'Expected a mathematical failure');controls.push({fault:name,rejected:true,exit_code:r.status,hash_check_used:false});
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}}
console.log(JSON.stringify({protocol:'RKF_VARIABLE_APERTURE_MUTATIONS_R2',controls,live_files_modified:false},null,2));
