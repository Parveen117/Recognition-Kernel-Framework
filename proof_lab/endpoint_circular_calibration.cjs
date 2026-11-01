'use strict';
// SE28 application adapter. The unchanged canonical engine owns all arithmetic.
const assert=require('node:assert/strict');
const o=require('../operator_foundation/core/native_operator.cjs');
const {arrow}=require('../operator_foundation/core/native_paths.cjs');
const {F,Cut,matrix,identity,equal,mul,dagger,energy}=o;
const f=x=>F.of(x);
function floor(x){x=f(x);let q=x.n/x.d;if(x.n<0n&&x.n%x.d)q--;return q;}
function positive(x){x=f(x);if(x.le(0))throw new RangeError('Positive calibration required');return x;}
function encode(value,unit=1,cut=0){
  unit=positive(unit);cut=f(cut);const relative=f(value).div(unit).sub(cut),sheet=floor(relative),phase=relative.sub(new F(sheet));
  const side=Number(floor(phase.mul(2))),halfPhase=phase.mul(2).sub(side);
  return {unit,cut,sheet,phase,side,halfPhase};
}
function reading(p){return new F(p.sheet).add(p.phase).add(p.cut);}
function decode(p){return p.unit.mul(reading(p));}
function translate(p,amount){return encode(decode(p).add(amount),p.unit,p.cut);}
function rechart(p,newUnit){return encode(decode(p),newUnit,p.cut);}
function recut(p,newCut){return encode(decode(p),p.unit,newCut);}
function resolved(p,unit){unit=f(unit);if(unit.n<0n)throw new RangeError('Nonnegative scale required');return {unit,reading:reading(p),raw:unit.mul(reading(p))};}
function tvsp(values){
  const [p,v,s,t]=values.map(f);if([p,v,s,t].some(x=>x.zero()))throw new RangeError('Regular nonzero response channels required');
  const invariant=p.div(v).mul(t.div(s));positive(invariant);
  const defect=invariant.sub(1).div(invariant.add(1));
  const phase=new Cut(1,defect).div(new Cut(1,defect.neg()));
  return {invariant,defect,phase};
}
function cutPower(z,n){let out=new Cut(1);for(let j=0;j<n;j++)out=out.mul(z);return out;}
function primes(N){const out=[];for(let p=2;p<=N;p++)if(out.every(q=>p%q))out.push(p);return out;}
function omega(n){let count=0;for(let p=2;p*p<=n;p++)while(n%p===0){n/=p;count++;}return count+(n>1?1:0);}
function eulerCoefficients(N,z){
  let a=Array.from({length:N+1},()=>new Cut());a[1]=new Cut(1);
  for(const p of primes(N)){const b=Array.from({length:N+1},()=>new Cut());for(let n=1;n<=N;n++)if(!a[n].zero()){
    let q=1,power=new Cut(1);while(n*q<=N){b[n*q]=b[n*q].add(a[n].mul(power));q*=p;power=power.mul(z);}
  }a=b;}return a;
}
function verify(){
  const checks=[],controls=[];function check(name,test,negative=false){test();checks.push({name,status:'PASS'});if(negative)controls.push(name);}
  const units=['1/3',1,'7/2'],values=['-19/4',-2,'-1/2',0,'1/2',1,'9/4',7];
  check('exact_cut_field_and_integer_floor',()=>{assert(new Cut(0,1).mul(new Cut(0,1)).eq(-1));assert.equal(floor('-1/3'),-1n);});
  check('circle_sheet_round_trips',()=>{for(const u of units)for(const x of values){const p=encode(x,u);assert(decode(p).eq(x));assert(f(0).le(p.phase)&&!f(1).le(p.phase));}});
  check('whole_line_cut_retains_both_half_circle_labels',()=>{for(const x of values){const p=encode(x);assert(new F(2n*p.sheet).add(p.side).add(p.halfPhase).div(2).eq(x));}});
  check('translation_carry_is_associative',()=>{for(const x of values)for(const a of values)for(const b of ['-4/3','7/5']){const p=encode(x,'7/2');assert.deepEqual(translate(translate(p,a),b),translate(p,f(a).add(b)));}});
  check('calibration_changes_preserve_the_physical_reading',()=>{for(const x of values)for(const u of units)assert(decode(rechart(encode(x),u)).eq(x));});
  check('recalibration_cocycle',()=>{for(const x of values)assert.deepEqual(rechart(rechart(encode(x),3),7),rechart(encode(x),7));});
  check('moving_the_whole_cut_line_preserves_readings_and_memory',()=>{for(const x of values)for(const cut of ['-3/2','1/3','7/4'])assert(decode(recut(encode(x),cut)).eq(x));});
  check('moving_cut_transitions_satisfy_the_cocycle',()=>{for(const x of values)assert.deepEqual(recut(recut(encode(x),'1/3'),'5/4'),recut(encode(x),'5/4'));});
  check('native_paths_preserve_completed_turns',()=>{const one=arrow('cut','cut',1),two=arrow('cut','cut',2);assert(one.mul(one).eq(two));assert(!one.eq(two));assert(equal(one.endpointShadow(['cut']),two.endpointShadow(['cut'])));});
  check('path_dagger_reverses_turn_memory',()=>{assert(arrow('b','a',3).dagger().eq(arrow('a','b',-3)));});
  check('full_turns_return_phase_but_retain_count',()=>{assert(encode(1).phase.eq(encode(2).phase));assert(!reading(encode(1)).eq(reading(encode(2))));});
  check('normalized_zero_scale_keeps_the_reading',()=>{for(const x of values){const p=encode(x);for(const u of [0,'1/1000',1]){const z=resolved(p,u);assert(z.reading.eq(x));if(!f(u).zero())assert(z.raw.div(u).eq(x));else assert(z.raw.zero());}}});
  check('zero_unit_is_not_a_division_operation',()=>{assert.throws(()=>encode(1,0),RangeError);},true);
  check('phase_only_erases_integer_information',()=>{assert(encode('1/4').phase.eq(encode('9/4').phase));assert(!decode(encode('1/4')).eq(decode(encode('9/4'))));},true);
  check('erasing_the_line_side_aliases_half_turns',()=>{assert(encode('1/4').halfPhase.eq(encode('3/4').halfPhase));assert.notEqual(encode('1/4').side,encode('3/4').side);},true);
  const shapes=[[1,1,1,1],[2,1,1,1],[1,2,1,1],[-2,-4,-3,-6]];
  check('TVSP_ratio_and_Cayley_phase_from_the_same_tetrad',()=>{for(const s of shapes){const t=tvsp(s);assert(t.phase.norm2().eq(1));assert.equal(t.phase.eq(1),t.invariant.eq(1));assert.equal(t.defect.zero(),t.invariant.eq(1));}});
  check('TVSP_common_unit_cancels',()=>{for(const s of shapes)for(const c of units)assert.deepEqual(tvsp(s.map(x=>f(x).mul(c))),tvsp(s));});
  check('response_pair_reversal_conjugates_phase',()=>{for(const [p,v,s,t]of shapes)assert(tvsp([v,p,t,s]).phase.eq(tvsp([p,v,s,t]).phase.dagger()));});
  check('flat_ratio_does_not_require_zero_response_coordinates',()=>{assert(tvsp([-2,-4,-3,-6]).defect.zero());});
  check('collapsed_raw_tetrad_does_not_select_a_flat_direction',()=>{assert(!tvsp(shapes[0]).phase.eq(tvsp(shapes[1]).phase));assert.deepEqual(shapes[0].map(x=>f(x).mul(0)),shapes[1].map(x=>f(x).mul(0)));},true);
  check('singular_zero_tetrad_is_rejected',()=>{assert.throws(()=>tvsp([0,0,0,0]),RangeError);},true);
  const N=256,flat=tvsp(shapes[0]).phase,twist=tvsp(shapes[1]).phase;
  check('flat_Euler_coefficients_are_exactly_one',()=>{assert(eulerCoefficients(N,flat).slice(1).every(x=>x.eq(1)));});
  check('twisted_Euler_coefficients_retain_prime_multiplicity',()=>{const a=eulerCoefficients(N,twist);for(let n=1;n<=N;n++)assert(a[n].eq(cutPower(twist,omega(n))));});
  check('log_derivative_recovers_each_prime_power_with_its_log_prime_weight',()=>{
    const a=eulerCoefficients(N,twist);
    for(let n=2;n<=N;n++)for(const p of primes(N))if(n%p===0){
      let convolution=new Cut(),power=1,k=0,multiplicity=0,remainder=n;
      while(remainder%p===0){multiplicity++;remainder/=p;}
      while(n%(power*p)===0){power*=p;k++;convolution=convolution.add(a[n/power].mul(cutPower(twist,k)));}
      assert(convolution.eq(a[n].mul(multiplicity)));
    }
  });
  let sum=new Cut(),product=new Cut(1);for(let n=1;n<=N;n++)sum=sum.add(cutPower(twist,omega(n)).div(n*n));for(const p of primes(N))product=product.div(new Cut(1).sub(twist.div(p*p)));
  check('finite_Euler_product_and_Dirichlet_head_obey_analytic_tail_cap',()=>{assert(product.sub(sum).norm2().le(new F(1,N*N)));});
  check('twisting_is_not_a_source_preserving_relabeling',()=>{assert(!eulerCoefficients(4,twist)[2].eq(1));},true);
  check('flat_connection_need_not_have_trivial_holonomy',()=>{const halfTurn=new Cut(-1);assert(!halfTurn.eq(1));assert(halfTurn.norm2().eq(1));},true);
  check('flat_reference_does_not_force_positive_source',()=>{const U=matrix([[0,-1],[1,0]]),S=matrix([[1,0],[0,-1]]),h=matrix([[0],[1]]);assert(equal(mul(dagger(U),U),identity(2)));const y=mul(U,h),Sp=mul(mul(U,S),dagger(U));assert(mul(mul(dagger(y),Sp),y)[0][0].eq(-1));assert(energy(y).eq(energy(h)));},true);
  return {schema:'rkf.circular-calibration-controls.v1',status:'PASS_EXACT_CIRCULAR_CALIBRATION',check_count:checks.length,negative_control_count:controls.length,
    TVSP_shapes:shapes.map(s=>({values:s.map(String),...tvsp(s)})),Euler_control:{integer_cutoff:N,prime_count:primes(N).length,half_plane:'Re(s)>1',tail_disk_at_s_2:'1/256',twist},
    cut_reference:'Entire line section with both side labels and integer sheet memory',checks,controls};
}
module.exports={floor,encode,decode,reading,translate,rechart,recut,resolved,tvsp,verify};
if(require.main===module)console.log(JSON.stringify(verify(),null,2));
