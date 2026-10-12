'use strict';
/**
 * R4: the repair step and the first real encoding.
 *
 * repairReport: run the structure report, then re-run it with the reversed-catalogue completion D^# as observer.
 * By R3-B the mark of D^# vanishes; by N03 on the catalogue S ∪ S^sharp, D^# is the minimum-rank observer refining the
 * seed with no returning memory (R4-B). One step suffices: repairing D^# adds nothing (R4-C). The price of the repair is
 * dagger_extra channels, exactly the channels named by the mark.
 *
 * ym37Job: the YM-37 column pencil (Publications papers/yang-mills-certified-benchmark, build_pencil(2,u0,k0), t = 2 even
 * invariant sector, dim 8) as a declared encoding: catalogue {tau = B^-1 M}, observer = boundary readout e0^T M,
 * target = insertion readout e0^T N, pairing B (Haar pairing of the sector). Consumed by pin, not rederived.
 */
const fs=require('node:fs'),path=require('node:path');
const o=require('../../../operator_foundation/core/native_operator.cjs'),s=require('../structure_report.cjs');
const {matrix,identity,mul,inverse,rank,rref}=o;

function summary(r){return {verdict:r.verdict,initial_rank:r.observer.initial_rank,forward_rank:r.observer.forward_rank,forward_extra:r.observer.forward_extra,dagger_rank:r.observer.dagger_rank,dagger_extra:r.observer.dagger_extra,returning_rank:r.returning_memory_form.rank,returning_energy:r.returning_memory_form.sum_of_leak_energies,pairing_declared:r.carrier.pairing_declared};}

function repairReport(job){
  const before=s.structureReport(job);
  const Dsharp=before.observer.completed_observer_sharp;
  const repaired={...job,observer:Dsharp};delete repaired.target; // the seed rows already lie in row(D^#)
  const after=s.structureReport(repaired);
  if(after.verdict!=='VISIBLE_LOCAL')throw new Error('R4-A failed: repaired observer must be visible and local');
  if(after.returning_memory_form.rank!==0||after.returning_memory.any)throw new Error('R4-A failed: repaired observer must carry no mark');
  if(after.observer.forward_extra!==0||after.observer.dagger_extra!==0)throw new Error('R4-C failed: repair must be idempotent');
  if(rank(Dsharp)!==before.observer.dagger_rank)throw new Error('Repaired observer rank must equal the reversed completion rank');
  // Finite minimality probe (R4-B): remove one basis row of D^# (keeping the seed); the reduced observer either regrows to rank(D^#) or carries a mark.
  const seed=matrix(job.observer).concat(job.target===undefined?[]:matrix(job.target));const probes=[];
  for(let i=0;i<Dsharp.length;i++){const reduced=rref(Dsharp.filter((_,k)=>k!==i).concat(seed)).basis;if(!reduced.length||reduced.length>=Dsharp.length)continue;
    const r=s.structureReport({...job,observer:reduced,target:undefined});const ok=r.observer.forward_rank>=Dsharp.length||r.returning_memory.any;if(!ok)throw new Error('R4-B probe failed: a smaller mark-free descending observer exists');probes.push({removed_row:i,reduced_rank:reduced.length,forward_rank:r.observer.forward_rank,mark:r.returning_memory.any});}
  return {protocol:'RKF_STRUCTURE_REPAIR_R4',before:summary(before),after:summary(after),cost_channels:before.observer.dagger_extra,repaired_observer:Dsharp,idempotent:true,minimality_probe:probes,reports:{before,after}};
}

function loadYm37(){return JSON.parse(fs.readFileSync(path.join(__dirname,'ym37_pencil_t2.json'),'utf8'));}
function ym37Job({pairing=true,readout='boundary_with_insertion',thresholds=['1/100','1/10','1']}={}){
  const d=loadYm37();const M=matrix(d.M),B=matrix(d.B),N=matrix(d.N),e0=d.constant_index;const tau=mul(inverse(B),M);
  const row=A=>[A[e0].slice()];const job={catalogue:{tau},thresholds};
  if(readout==='boundary_with_insertion'){job.observer=row(M);job.target=row(N);}
  else if(readout==='constant_coefficient'){job.observer=[identity(M.length)[e0]];}
  else throw new RangeError('Unknown readout');
  if(pairing)job.pairing=B;
  return {job,data:{dimension:M.length,constant_index:e0,M,B,N,tau}};
}

module.exports={repairReport,summary,ym37Job,loadYm37};
