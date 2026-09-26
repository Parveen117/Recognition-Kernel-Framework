'use strict';
/** Mathematical fault controls in temporary copies; never edit the live source. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..'),out=[];
const faults=[
 ['erase_negative_feedback','new F(1).add(q.mul(x))','new F(1).sub(q.mul(x))'],
 ['invent_even_order_returns','if(n%2===0)return p.zero();','if(n%2===0)return p.one();'],
 ['omit_cutoff_from_joint_limit_bound','toStrongCouplingAperture:q.div(k).add(new F(1).div(q.mul(4)))','toStrongCouplingAperture:new F(1).div(q.mul(4))'],
 ['reverse_native_orientation_without_updating_feedback','L=normal(K.times(R))','L=normal(R.times(K))']
];
for(const [name,from,to] of faults){const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-return-fault-'));try{
 const target=path.join(tmp,'research/recognition_return');fs.mkdirSync(path.join(tmp,'operator_foundation/core'),{recursive:true});fs.cpSync(__dirname,target,{recursive:true});
 for(const f of ['native_operator.cjs','paninian_operator.cjs'])fs.copyFileSync(path.join(root,'operator_foundation/core',f),path.join(tmp,'operator_foundation/core',f));
 const file=path.join(target,'return_solver.cjs'),text=fs.readFileSync(file,'utf8');assert.equal(text.split(from).length,2,'Unique mutation anchor required');fs.writeFileSync(file,text.replace(from,to));
 const r=cp.spawnSync(process.execPath,[path.join(target,'verify.cjs'),'--write'],{cwd:tmp,encoding:'utf8',timeout:45000});assert(r.status!==null,'Control must finish');assert.notEqual(r.status,0,'Mathematical fault escaped: '+name);out.push({fault:name,rejected:true,exit_code:r.status});
 }finally{fs.rmSync(tmp,{recursive:true,force:true});}}
console.log(JSON.stringify({protocol:'RKF_GRADED_APERTURE_MUTATIONS_R1',controls:out,live_files_modified:false},null,2));
