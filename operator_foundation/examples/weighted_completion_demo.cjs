'use strict';
/** Exact finite certificates for a genuinely infinite noncommutative algebra. */
const {WeightedCompletion}=require('../core/weighted_completion.cjs');
const {finiteBasis}=require('../core/workbench.cjs');
const A=new WeightedCompletion({tokens:['X','Y'],rules:[{
  id:'YX',lhs:['Y','X'],rhs:[[['X','Y'],'1/2']],
  source:'Declared demonstration algebra YX=(1/2)XY; not physical input'
}]},{X:1,Y:1});
const s=A.presentation,b=s.word(['X']).plus(s.word(['Y'])).scale('1/4');
const inverse=A.geometric(b,8),exp=A.exponential(b,6);
console.log(JSON.stringify({
  presentation:s.spec(),weighted_contract:A.contract(),
  algebra_size:finiteBasis(s).status,
  inverse_of:'I-(X+Y)/4',retained_monomials:inverse.approximation.terms.size,
  geometric_order:inverse.order,prior_tail:inverse.a_priori_tail,
  residual_certified_tail:inverse.certified_tail,
  inverse_norm_bound:inverse.inverse_certificate.inverse_bound,
  exponential_order:6,exponential_tail:exp.tail,
  meaning:'Finite polynomials with proved norm error to infinite completed-algebra objects',
  physical_identification:false
},null,2));
