'use strict';
// SE30 application: positive token counts precede the later cut adapter.
// Coefficient arithmetic and all polynomial products use the canonical engine.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const o=require('../operator_foundation/core/native_operator.cjs');
const l=require('../operator_foundation/core/native_laurent.cjs');
const {F,Cut}=o;
const root=path.resolve(__dirname,'..');
const resultPath=path.join(__dirname,'ENDPOINT_LAMBDA_COUNTING_RESULT.json');
const dev=path.join(root,'papers/rkf_completed_weil_endpoint/development');
const pinsPath=path.join(dev,'SE30_SOURCE_PINS.json');
const parentPins=path.join(dev,'SE29_SOURCE_PINS.json');

class Count {
  constructor(n,unit='lambda'){this.n=BigInt(n);if(this.n<1n)throw new RangeError('A count is a nonempty token string');this.unit=unit;Object.freeze(this);}
  same(b){if(!(b instanceof Count)||this.unit!==b.unit)throw new TypeError('Explicit unit relabeling required');}
  plus(b){this.same(b);return new Count(this.n+b.n,this.unit);}
  groups(b){this.same(b);return new Count(this.n*b.n,this.unit);}
  relabel(unit){return new Count(this.n,unit);}
  divides(b){this.same(b);return b.n%this.n===0n;}
  toJSON(){return {count:String(this.n),unit:this.unit};}
}
function factors(count){let n=count.n;const out=[];for(let p=2n;p*p<=n;p++)while(n%p===0n){out.push(p);n/=p;}if(n>1n)out.push(n);return out;}
function prime(n){n=BigInt(n);return n>1n&&factors(new Count(n)).length===1;}
const eqPair=(a,b)=>a[0]+b[1]===b[0]+a[1];
const plusPair=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const timesPair=(a,b)=>[a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]];

// Canonical scalar Laurent series are polynomials in whichever variable the
// caller declares. No second polynomial multiplication engine is implemented.
const mono=(c,k)=>l.monomial([[Cut.of(c)]],k);
const constant=c=>mono(c,0);
const scalar=c=>Cut.of(c);
const scale=(p,c)=>l.times(p,constant(c));
const subtract=(p,q)=>l.plus(p,scale(q,-1));
const equal=l.equalSeries;
const zero=()=>l.series([],1); // additive-neutral representation, not CutOperator
function power(p,n){let q=constant(1);for(let i=0;i<n;i++)q=l.times(q,p);return q;}
function evaluate(p,x){x=F.of(x);let s=scalar(0);for(const [k,a]of p.terms){assert(k>=0);s=s.add(a[0][0].mul(x.pow(k)));}return s;}
function coeff(p,k){return l.coefficient(p,k)[0][0];}
function choose(n,k){if(k<0||k>n)return 0n;let a=1n;for(let j=1;j<=k;j++)a=a*BigInt(n-j+1)/BigInt(j);return a;}
function factorial(n){let v=1n;for(let j=1;j<=n;j++)v*=BigInt(j);return v;}
function shift(p,h){h=F.of(h);const terms=[];for(const [k,a]of p.terms)for(let j=0;j<=k;j++)terms.push([j,[[a[0][0].mul(choose(k,j)).mul(h.pow(k-j))]]]);return l.series(terms,1);}
function delta(p,h){
  // The polynomial factor-removal formula is regular at the coefficient cut.
  h=F.of(h);const terms=[];
  for(const [k,a]of p.terms)for(let j=1;j<=k;j++)terms.push([k-j,[[a[0][0].mul(choose(k,j)).mul(h.pow(j-1))]]]);
  return l.series(terms,1);
}
const raise=(p,h)=>l.times(mono(1,1),shift(p,F.of(h).neg()));
function falling(n,h){h=F.of(h);let p=constant(1);for(let j=0;j<n;j++)p=l.times(p,l.plus(mono(1,1),constant(h.mul(-j))));return p;}
function transform(p,h){let out=zero();for(const [k,a]of p.terms)out=l.plus(out,scale(falling(k,h),a[0][0]));return out;}
function untransform(p,h){let out=zero(),rem=p;while(rem.terms.size){const degree=Math.max(...rem.terms.keys()),c=coeff(rem,degree);out=l.plus(out,mono(c,degree));rem=subtract(rem,scale(falling(degree,h),c));}return out;}
const bullet=(p,q,h)=>transform(l.times(untransform(p,h),untransform(q,h)),h);
const truncate=(p,n)=>l.series([...p.terms].filter(([k])=>k<=n),1);
function exponentialJet(x,h,n){return l.series(Array.from({length:n+1},(_,k)=>[k,[[evaluate(falling(k,h),x).div(factorial(k))]]]),1);}
function composeJet(p,q,n){let out=zero(),powerQ=constant(1);for(let j=0;j<=Math.max(0,...p.terms.keys());j++){out=truncate(l.plus(out,scale(powerQ,coeff(p,j))),n);powerQ=truncate(l.times(powerQ,q),n);}return out;}

function quantity(degree,body){if(!Number.isSafeInteger(degree)||degree<0)throw new RangeError('Nonnegative unit degree required');if([...body.terms.keys()].some(k=>k<degree))throw new RangeError('Family has terms below its declared cut degree');return {degree,body};}
const quantityProduct=(a,b)=>quantity(a.degree+b.degree,l.times(a.body,b.body));
const CutOperator=Object.freeze({
  apply(packet){return {degree:packet.degree,retained:coeff(packet.body,packet.degree),unitSymbol:'u'};},
  project(packet){return quantity(packet.degree,mono(coeff(packet.body,packet.degree),packet.degree));}
});
function cutCount(n){const packet=quantity(1,mono(n.n,1)),v=CutOperator.apply(packet);return new Count(v.retained.rad.n,'u');}
function pinCheck(file){const pins=JSON.parse(fs.readFileSync(file,'utf8')).sha256;for(const [p,h]of Object.entries(pins))assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex'),h,'Source pin: '+p);return Object.keys(pins).length;}
function verify(){
  const inheritedPins=pinCheck(parentPins),checks=[],controls=[];
  const check=(name,body,negative=false)=>{body();checks.push({name,status:'PASS'});if(negative)controls.push(name);};
  const counts=Array.from({length:9},(_,i)=>new Count(i+1));
  check('positive_count_layer_has_no_empty_or_negative_count',()=>{assert.throws(()=>new Count(0),RangeError);assert.throws(()=>new Count(-1),RangeError);},true);
  check('token_concatenation_and_grouping_obey_arithmetic_laws',()=>{for(const a of counts)for(const b of counts)for(const c of counts){assert.deepEqual(a.plus(b).plus(c),a.plus(b.plus(c)));assert.deepEqual(a.groups(b).groups(c),a.groups(b.groups(c)));assert.deepEqual(a.groups(b.plus(c)),a.groups(b).plus(a.groups(c)));assert.deepEqual(a.groups(b),b.groups(a));assert.deepEqual(a.plus(b),b.plus(a));}});
  check('unit_relabeling_transports_both_count_operations',()=>{for(const a of counts)for(const b of counts){assert.deepEqual(a.plus(b).relabel('mu'),a.relabel('mu').plus(b.relabel('mu')));assert.deepEqual(a.groups(b).relabel('mu'),a.relabel('mu').groups(b.relabel('mu')));}});
  check('mixed_units_require_explicit_transport',()=>assert.throws(()=>counts[0].plus(counts[0].relabel('mu')),TypeError),true);
  check('count_product_and_quantity_product_have_different_unit_degree',()=>{const a=new Count(3),b=new Count(5),unit=F.of(2);assert(a.groups(b).n===15n);assert(F.of(a.groups(b).n).mul(unit).eq(30));assert(F.of(a.n).mul(unit).mul(F.of(b.n).mul(unit)).eq(60));},true);
  check('difference_completion_derives_its_neutral_class',()=>{for(let a=1n;a<=8n;a++)for(let b=1n;b<=8n;b++){const p=[a,b];assert(eqPair([a,a],[1n,1n]));assert(eqPair(plusPair(p,[7n,7n]),p));assert(eqPair(plusPair(p,[b,a]),[1n,1n]));assert(eqPair(timesPair(p,[2n,1n]),p));}});
  check('completion_products_do_not_depend_on_pair_representative',()=>{for(let a=1n;a<=6n;a++)for(let b=1n;b<=6n;b++){const p=[a,b],q=[a+3n,b+3n],r=[7n,2n];assert(eqPair(timesPair(p,r),timesPair(q,r)));assert(eqPair(plusPair(p,r),plusPair(q,r)));}});
  const primeList=[];
  check('factorization_and_primes_are_preserved_by_the_unit_cut',()=>{for(let n=1;n<=512;n++){const a=new Count(n),b=cutCount(a),f=factors(a);assert.equal(f.reduce((x,y)=>x*y,1n),a.n);assert.deepEqual(f,factors(b));assert(f.every(prime));if(prime(n))primeList.push(n);}});
  check('divisibility_survives_the_cut',()=>{for(const a of counts)for(let n=1;n<=80;n++){const b=new Count(n);assert.equal(a.divides(b),cutCount(a).divides(cutCount(b)));}});
  check('cut_retains_distinct_nonempty_counts',()=>{const a=cutCount(new Count(3)),b=cutCount(new Count(5));assert.equal(a.n,3n);assert.equal(b.n,5n);assert.notDeepEqual(a,b);});
  check('raw_scalar_evaluation_is_not_the_cut_operator',()=>{const a=mono(3,1),b=mono(5,1);assert(evaluate(a,0).eq(evaluate(b,0)));assert(!CutOperator.apply(quantity(1,a)).retained.eq(CutOperator.apply(quantity(1,b)).retained));},true);
  check('cut_projector_is_idempotent_and_fixes_the_marked_unit',()=>{for(let d=0;d<=5;d++){const q=quantity(d,l.plus(mono(3,d),mono(7,d+2))),p=CutOperator.project(q);assert(equal(CutOperator.project(p).body,p.body));assert(coeff(p.body,d).eq(3));}assert(coeff(CutOperator.project(quantity(1,mono(1,1))).body,1).eq(1));});
  check('cut_is_additive_and_quantity_products_use_the_sum_degree',()=>{for(let d=0;d<=4;d++)for(let e=0;e<=4;e++){const a=quantity(d,l.plus(mono(3,d),mono(7,d+1))),b=quantity(e,l.plus(mono(5,e),mono(-2,e+2)));const ca=CutOperator.apply(a),cb=CutOperator.apply(b),cp=CutOperator.apply(quantityProduct(a,b));assert.equal(cp.degree,d+e);assert(cp.retained.eq(ca.retained.mul(cb.retained)));const a2=quantity(d,l.plus(a.body,a.body));assert(CutOperator.apply(a2).retained.eq(ca.retained.mul(2)));}});
  check('one_untyped_cut_cannot_preserve_all_quantity_products',()=>{const product=l.times(mono(3,1),mono(5,1));assert(CutOperator.apply(quantity(1,product)).retained.zero());assert(CutOperator.apply(quantity(2,product)).retained.eq(15));},true);
  check('below_degree_packets_are_rejected',()=>assert.throws(()=>quantity(2,l.plus(mono(1,1),mono(1,2))),RangeError),true);
  const steps=['1/3',1,2,'-2/5'],polys=[mono(1,0),mono(1,1),mono(1,7),l.plus(mono('3/7',5),l.plus(mono(-2,2),constant(4)))];
  check('formal_factor_removal_matches_step_differences',()=>{for(const h of steps)for(const p of polys)assert(equal(subtract(shift(p,h),p),scale(delta(p,h),h)));});
  check('falling_basis_counts_ordered_choices',()=>{for(const h of steps)for(let k=1;k<=12;k++)for(let n=1;n<=k;n++){let choices=1n;for(let j=0;j<n;j++)choices*=BigInt(k-j);assert(evaluate(falling(n,h),F.of(h).mul(k)).eq(F.of(choices).mul(F.of(h).pow(n))));assert(CutOperator.apply(quantity(n,mono(choices,n))).retained.eq(choices));}});
  check('lowering_and_raising_are_exact_on_the_counting_basis',()=>{for(const h of steps)for(let n=1;n<=10;n++){assert(equal(delta(falling(n,h),h),scale(falling(n-1,h),n)));assert(equal(raise(falling(n,h),h),falling(n+1,h)));}});
  check('operator_commutator_is_identity_before_specialization',()=>{for(const h of steps)for(const p of polys)assert(equal(subtract(delta(raise(p,h),h),raise(delta(p,h),h)),p));});
  check('polynomial_formula_transport_is_invertible',()=>{for(const h of steps)for(const p of polys){assert(equal(untransform(transform(p,h),h),p));assert(equal(transform(untransform(p,h),h),p));assert(equal(delta(transform(p,h),h),transform(l.derivative(p),h)));}});
  check('transported_formula_product_is_associative_and_differentiates',()=>{const p=l.plus(mono(1,2),constant(1)),q=l.plus(mono(2,1),constant(3)),r=mono(1,1);for(const h of steps){assert(equal(bullet(bullet(p,q,h),r,h),bullet(p,bullet(q,r,h),h)));assert(equal(delta(bullet(p,q,h),h),l.plus(bullet(delta(p,h),q,h),bullet(p,delta(q,h),h))));assert(equal(bullet(r,r,h),falling(2,h)));}});
  check('ordinary_product_retains_its_shifted_Leibniz_rule',()=>{for(const h of steps)for(const p of polys)for(const q of polys)assert(equal(delta(l.times(p,q),h),l.plus(l.times(delta(p,h),q),l.times(shift(p,h),delta(q,h)))));});
  check('ordinary_unshifted_product_rule_is_rejected',()=>{const x=mono(1,1);assert(!equal(delta(l.times(x,x),1),scale(x,2)));assert(equal(delta(l.times(x,x),1),l.plus(scale(x,2),constant(1))));},true);
  check('coefficient_cut_recovers_derivative_and_power_basis',()=>{for(const p of polys){assert(equal(delta(p,0),l.derivative(p)));assert(equal(transform(p,0),p));}for(let n=0;n<=10;n++)assert(equal(falling(n,0),mono(1,n)));});
  check('cutting_the_step_numerator_first_loses_the_response',()=>{const numerator=l.plus(mono(4,1),mono(1,2));assert(CutOperator.apply(quantity(0,numerator)).retained.zero());assert(CutOperator.apply(quantity(1,numerator)).retained.eq(4));},true);
  const jetOrder=10;
  check('exponential_jet_satisfies_the_counting_recurrence',()=>{for(const h of steps)for(const x of ['2/3',3]){const E=exponentialJet(x,h,jetOrder);for(let n=0;n<jetOrder;n++){const lhs=coeff(E,n+1).mul(n+1).add(coeff(E,n).mul(F.of(h).mul(n)));assert(lhs.eq(coeff(E,n).mul(x)));}}});
  check('exponential_addition_law_holds_through_the_declared_jet_order',()=>{for(const h of steps){const a=exponentialJet('2/3',h,jetOrder),b=exponentialJet('7/5',h,jetOrder),c=exponentialJet(F.of('2/3').add('7/5'),h,jetOrder);assert(equal(truncate(l.times(a,b),jetOrder),c));}});
  check('deformed_frequency_composition_holds_in_exact_jets',()=>{for(const h of steps){const E=exponentialJet('7/3',h,jetOrder),a=F.of('2/5'),b=F.of('3/7');const left=truncate(l.times(composeJet(E,mono(a,1),jetOrder),composeJet(E,mono(b,1),jetOrder)),jetOrder);const w=l.plus(mono(a.add(b),1),mono(F.of(h).mul(a).mul(b),2));assert(equal(left,composeJet(E,w,jetOrder)));}});
  check('frequency_composition_is_associative',()=>{for(const h of steps){const join=(a,b)=>F.of(a).add(b).add(F.of(h).mul(a).mul(b));assert(join(join('2/5','3/7'),'4/9').eq(join('2/5',join('3/7','4/9'))));}});
  check('exponential_at_the_coefficient_cut_retains_all_declared_coefficients',()=>{const x=F.of('7/3'),E=exponentialJet(x,0,jetOrder);for(let n=0;n<=jetOrder;n++)assert(coeff(E,n).eq(x.pow(n).div(factorial(n))));});
  const inherited=JSON.parse(fs.readFileSync(path.join(__dirname,'ENDPOINT_CONNECTED_CUT_RESULT.json'),'utf8'));
  check('historical_RH_source_bound_is_unchanged',()=>{assert.equal(inherited.global_source.eta,'1079/2000');assert.equal(inherited.global_source.shifted_native_floor,'1/492000');});
  return {schema:'rkf.constant-lambda-counting.v1',date:'2026-10-12',status:'PASS_LAMBDA_COUNTING_AND_TYPED_CUT',
    foundation:{primitive:'One marked unit and nonempty repetition',primitive_empty_count:false,geometric_cut_required_for_counting:false,
      zero_meaning:'Typed graded cut operator; not an annihilating scalar',cut:'C_d(f)=[Lambda^d]f*u^d on f in (Lambda^d)',
      count_product:'[m] odot [n]=[mn] in one marked unit',quantity_product:'(m Lambda^d)(n Lambda^e)=mn Lambda^(d+e)',curvature_developed:false},
    theorem_count:5,checks,controls,check_count:checks.length,negative_control_count:controls.length,inherited_source_pins_checked:inheritedPins,
    arithmetic:{factorization_max:512,prime_count:primeList.length,primes:primeList,positive_counts_at_cut:[cutCount(new Count(3)),cutCount(new Count(5))]},
    polynomial_controls:{steps,basis_degree_through:10,ordered_choice_count_through:12,formal_series_jet_order:jetOrder,
      at_cut:'D becomes d/dx; p_n becomes x^n; the exponential family becomes exp(x*t)',universal_claim_basis:'Written proofs, not finite sampling'},
    RH:{eta:'1079/2000',native_floor:'1/492000',global_replay_rerun:false,eta_zero_certified:false,RH_proved:false},
    not_claimed:['a new prime distribution','all mathematical definitions replaced','a ring with inverses and no additive neutral class','all analytic equations transported without domain conditions','a universal physical lambda constant','curvature or RH completion','whole-engine PASS','formal proof-assistant or external review']};
}
module.exports={Count,CutOperator,quantity,quantityProduct,falling,delta,raise,transform,untransform,bullet,verify};
if(require.main===module){const args=process.argv.slice(2);if(args.some(x=>!['--write','--check'].includes(x))||args.length>1)throw new Error('Choose --write or --check');const r=verify(),data=JSON.stringify(r,null,2)+'\n';if(args.includes('--write'))fs.writeFileSync(resultPath,data,{flag:'wx'});if(args.includes('--check')){assert.equal(fs.readFileSync(resultPath,'utf8'),data,'Read-only archive mismatch');console.log('Source pins checked:',pinCheck(pinsPath));}console.log(JSON.stringify({status:r.status,checks:r.check_count,negative_controls:r.negative_control_count,foundation:r.foundation,RH:r.RH},null,2));}
