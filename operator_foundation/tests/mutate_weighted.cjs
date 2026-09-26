'use strict';
/** Re-run mathematical checks on temporary mutations, without consulting pins. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const cp=require('node:child_process'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const faults=[
  {name:'one_sided_inverse_promoted',from:'if (!qL.le(1) || qL.eq(1) || !qR.le(1) || qR.eq(1))',
    to:'if (!qL.le(1) || qL.eq(1))'},
  {name:'hidden_source_dressing_erased',from:'const fhat = this.sub(f, this.mul(bx, g));',
    to:'const fhat = this.normal(f);'},
  {name:'quadratic_lipschitz_factor_dropped',from:'const kappa = ell.add(q.mul(r).mul(2));',
    to:'const kappa = ell.add(q.mul(r));'}
];
const controls=[];
for(const fault of faults){
  const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'rkf-weighted-'));
  try{
    fs.cpSync(root,tmp,{recursive:true,filter:p=>!p.includes(path.sep+'sources'+path.sep)});
    const file=path.join(tmp,'core/weighted_completion.cjs'),src=fs.readFileSync(file,'utf8');
    assert.equal(src.split(fault.from).length,2,'One mutation location required');
    fs.writeFileSync(file,src.replace(fault.from,fault.to));
    const r=cp.spawnSync(process.execPath,[path.join(tmp,'tests/verify_weighted.cjs'),'--json'],{encoding:'utf8',timeout:90000});
    assert.notEqual(r.status,0,'Mathematical tests accepted '+fault.name);
    assert.notEqual(r.status,null,'Mutation runner did not finish');
    controls.push({name:fault.name,rejected:true,exit_status:r.status,source_pins_not_used:true});
  }finally{fs.rmSync(tmp,{recursive:true,force:true});}
}
console.log(JSON.stringify({protocol:'RKF_WEIGHTED_MUTATIONS_V0_5',status:'PASS',controls},null,2));
