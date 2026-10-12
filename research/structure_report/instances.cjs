'use strict';
/** Named finite instances for the structure report. Every entry is exact; names describe content. */
const iota=[0,1];
const R=[[0,-1],[1,0]],K=[[0,1],[1,0]];
function E(n,i,j,v=1){const m=Array.from({length:n},()=>Array(n).fill(0));m[i][j]=v;return m;}
function addM(a,b){return a.map((r,i)=>r.map((x,j)=>typeof x==='number'&&typeof b[i][j]==='number'?x+b[i][j]:[x,b[i][j]]));}
function blockDiag(a,b){const n=a.length+b.length;const m=Array.from({length:n},()=>Array(n).fill(0));a.forEach((r,i)=>r.forEach((x,j)=>m[i][j]=x));b.forEach((r,i)=>r.forEach((x,j)=>m[a.length+i][a.length+j]=x));return m;}

module.exports={
  // N03 control: observing e1 under the EMK pair needs exactly one more channel; nothing returns (R^dagger=-R, K^dagger=K in span).
  emk_pair_observer_e1:{catalogue:{R,K},observer:[[1,0]],thresholds:['1/2','1','2'],expect:{verdict:'HIDDEN_LOCAL',forward_extra:1,dagger_extra:0,rank_K:0}},
  // Full observer: nothing hidden, nothing returns.
  emk_pair_full_observer:{catalogue:{R,K},observer:[[1,0],[0,1]],expect:{verdict:'VISIBLE_LOCAL',forward_extra:0,dagger_extra:0,rank_K:0}},
  // N03 control: a block action mixing only components 1,2; observing component 1 completes to rank 2, decomposes (no leak).
  block_local_3:{catalogue:{A:[[1,1,0],[0,1,0],[0,0,2]]},observer:[[1,0,0]],expect:{verdict:'HIDDEN_LOCAL',forward_extra:1,dagger_extra:0,rank_K:0}},
  // One-way flow e2 -> e1 observed at e2: forward-complete with one channel, the reversed path returns (energy 1).
  one_way_flow_2:{catalogue:{S:E(2,0,1)},observer:[[0,1]],thresholds:['1/2','1','3/2'],expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:1,rank_K:1,weights:['1']}},
  // Same flow with a quarter turn: leak iota E_12, N(iota)=1. Coordinate transpose would give the wrong sign here.
  iota_one_way_flow_2:{catalogue:{S:E(2,0,1,iota)},observer:[[0,1]],thresholds:['1/2','1','3/2'],expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:1,rank_K:1,weights:['1']}},
  // Two faces J=diag(1,1,-1,-1); even generator R+R inside the faces, odd directed coupling Y=E_31+E_42 face1 -> face2; observer = face 1.
  cut_faces_directed_4:{catalogue:{RR:blockDiag(R,R),Y:addM(E(4,2,0),E(4,3,1))},observer:[[1,0,0,0],[0,1,0,0]],cut:[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]],thresholds:['1/2','1','2'],
    expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:2,rank_K:2,weights:['1','1'],cut_aligned:true,odd_only:true,seam_counts:[2,0,0]}},
  // Two faces, two odd couplings of different strength (2 and 3) and one even swap inside face 1: two returning channels with weights 4 and 9.
  cut_faces_two_strengths_4:{catalogue:{G:addM(E(4,0,1),E(4,1,0)),A:E(4,2,0,2),B:E(4,3,1,3)},observer:[[1,0,0,0],[0,1,0,0]],cut:[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]],thresholds:['1','4','6','9','10'],
    expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:2,rank_K:2,weights:['4','9'],cut_aligned:true,odd_only:true,seam_counts:[2,1,1,0,0]}},
  // Observer not aligned with the cut J=diag(1,1,-1): observes e1 only; the even flow e1 -> e2 (strength 2) leaks as well as the odd flow e1 -> e3 (strength 3).
  cut_misaligned_observer_3:{catalogue:{A:E(3,1,0,2),B:E(3,2,0,3)},observer:[[1,0,0]],cut:[[1,0,0],[0,1,0],[0,0,-1]],thresholds:['12','13','14'],
    expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:2,rank_K:1,weights:['13'],cut_aligned:false,even_leak:true,seam_counts:[1,0,0]}},
  // Observer with a turn component, C=(1,1+iota); the generator maps e1 onto ker C. The retained projector has turn entries,
  // so self-dagger (native reversal) and coordinate transpose differ; leak energy exactly 1, returning form of rank 1.
  // Here K equals P exactly, so the pencil reading flips at threshold 1 while the T53 weights are (1/3, 0): weights are not pencil thresholds (T53: weights = eigenvalues NOT CLAIMED).
  turn_observer_2:{catalogue:{N:[[[-1,-1],0],[1,0]]},observer:[[1,[1,1]]],thresholds:['1/2','1','2'],
    expect:{verdict:'GLOBAL_RETURNING_MEMORY',forward_extra:0,dagger_extra:1,rank_K:1,weights:['1/3','0'],seam_counts:[1,0,0]}}
};
