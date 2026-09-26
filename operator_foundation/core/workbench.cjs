'use strict';
/** Finite algebra discovery and a self-contained job/replay interface.
 * Native inputs: typed cut-field generators and declared relations.
 * The regular action is constructed from normal forms, not assumed as a metric.
 */
const o = require('./native_operator.cjs');
const p = require('./paninian_operator.cjs');
const l = require('./native_laurent.cjs');
const {Presentation, Expr, Budget, bracket, digest, stable} = p;
const {Cut, ZERO, ONE, matrix, zeros, identity, mul, equal, rank, rowClosure, descendedAction} = o;
const ENGINE = 'RKF_NATIVE_WORKBENCH_V0_4';
const DEFAULTS = Object.freeze({maxBasis:32,maxAutomatonStates:1024,maxSteps:100000,maxTerms:100000});
function limits(raw={}) {
  if(!raw || typeof raw!=='object' || Array.isArray(raw)) throw new TypeError('Limits must be an object');
  const out={...DEFAULTS};
  for(const [k,v] of Object.entries(raw)) {
    if(!Object.hasOwn(out,k)||!Number.isSafeInteger(v)||v<1||v>1000000) throw new RangeError('Invalid resource bound: '+k);
    out[k]=v;
  }
  if(out.maxBasis>256) throw new RangeError('Finite matrix backend limit is 256 basis words');
  return out;
}
function presentation(spec) {
  if(!spec || !Array.isArray(spec.tokens) || spec.tokens.length>32 || !Array.isArray(spec.rules||[]) || (spec.rules||[]).length>256) throw new TypeError('A bounded explicit presentation is required');
  for(const r of spec.rules||[]) if(!Array.isArray(r.lhs)||r.lhs.length>128) throw new RangeError('Leading words must have at most 128 tokens');
  return new Presentation(spec);
}
const wk = w => JSON.stringify(w);
const suffix = (word,tail) => tail.length<=word.length && tail.every((t,i)=>word[word.length-tail.length+i]===t);

function finiteBasis(s, options={}) {
  const cap=limits(options);
  if(s.objects.length!==1) return {status:'MULTI_OBJECT_BACKEND_NOT_IMPLEMENTED'};
  const audit=s.audit(cap);
  if(audit.status!=='CONFLUENT_BY_CHECKED_DIAMONDS') return {status:'PRESENTATION_NOT_CERTIFIED',audit};
  const forbidden=s.rules.map(r=>r.lhs), prefixes=new Map([[wk([]),[]]]);
  for(const w of forbidden) for(let i=1;i<w.length;i++) prefixes.set(wk(w.slice(0,i)),w.slice(0,i));
  const prefixList=[...prefixes.values()].sort((a,b)=>b.length-a.length);
  const alphabet=[...s.order.keys()], states=[[]], transitions=[], access=[[]], index=new Map([[wk([]),0]]);
  for(let at=0;at<states.length;at++) {
    if(states.length>cap.maxAutomatonStates) return {status:'AUTOMATON_BUDGET_EXHAUSTED',audit};
    const edges=[];
    for(const token of alphabet) {
      const candidate=states[at].concat(token);
      if(forbidden.some(w=>suffix(candidate,w))) continue;
      const next=prefixList.find(w=>suffix(candidate,w))||[], k=wk(next);
      if(!index.has(k)) { index.set(k,states.length);states.push(next);access.push(access[at].concat(token)); }
      edges.push({token,to:index.get(k)});
    }
    transitions.push(edges);
  }
  const color=Array(states.length).fill(0), stack=[], edgePath=[];let cycle=null;
  function visit(u) {
    color[u]=1;stack.push(u);
    for(const e of transitions[u]) {
      if(color[e.to]===1) { const i=stack.indexOf(e.to);cycle={access:access[e.to],loop:edgePath.slice(i).concat(e.token)};return true; }
      if(color[e.to]===0) {edgePath.push(e.token);if(visit(e.to))return true;edgePath.pop();}
    }
    stack.pop();color[u]=2;return false;
  }
  visit(0);
  const automaton={states,transitions};
  if(cycle) return {status:'INFINITE_IRREDUCIBLE_LANGUAGE',audit,automaton,cycle};
  const counts=new Map();function count(u){if(counts.has(u))return counts.get(u);const n=1n+transitions[u].reduce((a,e)=>a+count(e.to),0n);counts.set(u,n);return n;}
  const dimension=count(0);
  if(dimension>BigInt(cap.maxBasis))return {status:'FINITE_BASIS_BUDGET_EXHAUSTED',dimension:dimension.toString(),audit,automaton};
  const words=[],queue=[{state:0,word:[]}];
  for(let i=0;i<queue.length;i++){const a=queue[i];words.push(a.word);for(const e of transitions[a.state])queue.push({state:e.to,word:a.word.concat(e.token)});}
  words.sort((a,b)=>s.compare(a,b));
  if(BigInt(words.length)!==dimension)throw new Error('Automaton dimension/enumeration mismatch');
  return {status:'COMPLETE_FINITE_NORMAL_BASIS',dimension:words.length,words,audit,automaton};
}
function buildModel(spec,options={}) {
  const s=presentation(spec),cap=limits(options),basis=finiteBasis(s,cap);
  if(basis.status!=='COMPLETE_FINITE_NORMAL_BASIS')return {presentation:s,basis};
  const words=basis.words,expressions=words.map(w=>s.word(w)),ix=new Map(words.map((w,i)=>[wk(w),i]));
  function coefficients(e) {
    const v=Array(words.length).fill(ZERO),n=s.reduce(e,cap).normal;
    for(const [w,c] of n.entries()){const i=ix.get(wk(w));if(i===undefined)throw new Error('Normal form outside certified basis');v[i]=c;}return v;
  }
  function leftAction(e){const columns=expressions.map(b=>coefficients(e.times(b)));return matrix(Array.from({length:words.length},(_,i)=>columns.map(c=>c[i])));}
  const actions=Object.fromEntries([...s.order.keys()].map(t=>[t,leftAction(s.word([t]))]));
  const gate=p.representationGate(s,actions,words.length);
  if(gate.status!=='REPRESENTATION_RESPECTS_RELATIONS')throw new Error('Constructed action violates source relations');
  const unitIndex=ix.get(wk([]));
  for(let j=0;j<words.length;j++){const a=leftAction(expressions[j]);for(let i=0;i<words.length;i++)if(!a[i][unitIndex].eq(Number(i===j)))throw new Error('Regular-action faithfulness witness failed');}
  return {presentation:s,basis,expressions,coefficients,leftAction,actions,unitIndex};
}
function parseExpression(s,ast,depth=0,counter={count:0}) {
  if(depth>64 || ++counter.count>10000)throw new RangeError('Expression resource limit');
  if(!ast || typeof ast!=='object' || Array.isArray(ast))throw new TypeError('Use a JSON expression object, not executable text');
  if(Object.hasOwn(ast,'word')) {
    if(!Array.isArray(ast.word)||ast.word.length>512)throw new RangeError('Invalid word length');
    return s.word(ast.word,ast.coefficient===undefined?ONE:Cut.of(ast.coefficient));
  }
  const recur=x=>parseExpression(s,x,depth+1,counter);
  if(ast.op==='scale')return recur(ast.value).scale(Cut.of(ast.coefficient));
  if(ast.op==='commutator')return bracket(recur(ast.left),recur(ast.right));
  if(ast.op==='subtract')return recur(ast.left).minus(recur(ast.right));
  if(['add','multiply'].includes(ast.op)) {
    if(!Array.isArray(ast.args)||ast.args.length>512)throw new RangeError('Explicit bounded expression arguments required');
    return ast.args.reduce((a,x)=>ast.op==='add'?a.plus(recur(x)):a.times(recur(x)),ast.op==='add'?s.zero():s.one());
  }
  throw new TypeError('Unknown expression operation');
}
function expressionFromVector(model,v) {return model.expressions.reduce((a,b,i)=>a.plus(b.scale(v[i])),model.presentation.zero());}
function commutant(model,targets) {
  const d=model.basis.dimension, rows=[];
  for(const a of targets){const cols=model.expressions.map(b=>model.coefficients(bracket(a,b)));for(let i=0;i<d;i++)rows.push(cols.map(c=>c[i]));}
  const kernel=rows.length?l.nullspaceRows(rows):identity(d);
  const polynomials=kernel.map(v=>expressionFromVector(model,v));
  const proofs=polynomials.map(x=>targets.map(a=>p.proveEquality(bracket(a,x),model.presentation.zero())));
  if(proofs.flat().some(v=>v.status!=='EQUAL_IN_DECLARED_QUOTIENT'))throw new Error('Commutant reconstruction failed');
  return {dimension:kernel.length,coordinates:kernel,expressions:polynomials.map(x=>x.toJSON()),proofs};
}
function runJob(job) {
  if(!job||job.schema!=='rkf.operator-job.v1'||!Array.isArray(job.tasks)||job.tasks.length>64)throw new TypeError('Expected a bounded rkf.operator-job.v1 object');
  const cap=limits(job.limits),model=buildModel(job.presentation,cap),s=model.presentation;
  const report={protocol:ENGINE,input:job,input_sha256:digest(job),presentation_sha256:s.hash(),carrier:model.basis,results:[],scope:{native_cut_field:true,primitive_Hilbert_space:false,physical_model_selected:false,regular_action_is_a_derived_coordinate_model:true}};
  if(model.basis.status!=='COMPLETE_FINITE_NORMAL_BASIS'){report.status=model.basis.status;return stable(report);}
  report.regular_representation={actions:model.actions,unit_index:model.unitIndex,faithfulness:'complete irreducible basis and L_a(1)=a',dagger_is_not_assumed_to_be_coordinate_transpose:true};
  for(const task of job.tasks) {
    if(!task||typeof task.kind!=='string')throw new TypeError('Named task required');
    const read=x=>parseExpression(s,x);let result;
    switch(task.kind) {
      case 'normalize': {const r=s.reduce(read(task.expression),{...cap,witness:true});s.replay(r.certificate);result={normal:r.normal.toJSON(),proof:r.certificate};break;}
      case 'equality': result=p.proveEquality(read(task.left),read(task.right));break;
      case 'solve_coefficients': result=p.solveCoefficients(read(task.target),task.templates?task.templates.map(read):model.expressions);break;
      case 'centralizer': if(!Array.isArray(task.targets))throw new TypeError('Explicit centralizer targets required');result=commutant(model,task.targets.map(read));break;
      case 'center': result=commutant(model,[...s.order.keys()].map(t=>s.word([t])));break;
      case 'inverse': {
        const a=read(task.expression),sol=p.solveCoefficients(s.one(),model.expressions.map(b=>a.times(b)));
        if(sol.status==='NO_SOLUTION_IN_TEMPLATE'){result={status:'NOT_INVERTIBLE_IN_DECLARED_FINITE_ALGEBRA'};break;}
        const b=expressionFromVector(model,sol.particular.map(Cut.of)),left=p.proveEquality(a.times(b),s.one()),right=p.proveEquality(b.times(a),s.one());
        if(left.status!=='EQUAL_IN_DECLARED_QUOTIENT'||right.status!=='EQUAL_IN_DECLARED_QUOTIENT')throw new Error('Two-sided inverse check failed');
        result={status:'TWO_SIDED_INVERSE',inverse:b.toJSON(),coefficients:sol.particular,left,right};break;
      }
      case 'future_observer': {
        const c=matrix(task.observer),target=task.target===undefined?[]:matrix(task.target),d=model.basis.dimension;
        if(c[0].length!==d||(target.length&&target[0].length!==d))throw new RangeError('Observer/target must act on the certified regular carrier');
        const actions=Object.values(model.actions),r=rowClosure(c.concat(target),actions),D=r.observer;
        const descended=r.rank?actions.map(a=>descendedAction(a,D)):[];
        if(r.rank && descended.some(a=>a===null))throw new Error('Future action did not descend');
        result={initial_rank:rank(c),seed_rank:rank(c.concat(target)),completed_rank:r.rank,extra_channels:r.rank-rank(c),observer:D,actions:r.rank?descended:[],field:'cut-complex',native_dagger_closure_requested:false};break;
      }
      default:throw new TypeError('Unknown task kind: '+task.kind);
    }
    report.results.push({kind:task.kind,result});
  }
  report.status='VERIFIED_FINITE_JOB';return stable(report);
}
function replayJob(packet,expectedInputHash) {
  if(!packet||packet.protocol!==ENGINE||typeof expectedInputHash!=='string'||expectedInputHash.length!==64)throw new TypeError('An externally trusted expected input SHA-256 is required');
  if(digest(packet.input)!==expectedInputHash||packet.input_sha256!==expectedInputHash)throw new Error('Job source/contract mismatch');
  const fresh=runJob(packet.input);
  if(digest(fresh)!==digest(packet))throw new Error('Recomputed job does not match the supplied result/proof packet');
  return {status:'REPLAY_MATCH',input_sha256:expectedInputHash,result_sha256:digest(fresh),verified_job:fresh.status==='VERIFIED_FINITE_JOB'};
}
module.exports={ENGINE,limits,presentation,finiteBasis,buildModel,parseExpression,commutant,runJob,replayJob};
