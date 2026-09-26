'use strict';
const {Presentation,bracket,solveCoefficients,formalExp,formalLog,seriesMultiply}=require('../core/paninian_operator.cjs');
const p=new Presentation({tokens:['R','K'],rules:[
 {id:'RR',lhs:['R','R'],rhs:[[[],-1]],source:'RKF T48'},
 {id:'KK',lhs:['K','K'],rhs:[[[],1]],source:'RKF T48'},
 {id:'KR',lhs:['K','R'],rhs:[[['R','K'],-1]],source:'RKF T48'}]});
const r=p.word(['R']),k=p.word(['K']),proof=p.reduce(p.word(['K','R','K','R']),{witness:true});
const solution=solveCoefficients(bracket(r,k),[p.one(),r,k,r.times(k)]);
console.log(JSON.stringify({presentation:p.audit().status,critical_pairs:p.audit().criticalPairs,
 expression:'K R K R',normal:proof.normal,proof_replayed:p.replay(proof.certificate),
 commutator_template:['I','R','K','RK'],commutator_coefficients:solution.particular},null,2));
