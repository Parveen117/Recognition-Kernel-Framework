'use strict';
/** Sparse typed residue paths. Arrow (to,from,k) retains an integer seam label.
 * The finite support is a submodel of the source's countable residue groupoid;
 * equal endpoint/color is not typed path equality. k is not complete word history.
 */
const {Cut,F,ZERO,ONE,zeros}=require('./native_operator.cjs');
function label(x){if(typeof x!=='string'||!x.length)throw new TypeError('Nonempty object label required');return x;}
function sheet(x){if(typeof x==='bigint')return x;if(typeof x==='number'&&Number.isSafeInteger(x))return BigInt(x);if(typeof x==='string'&&/^[-+]?\d+$/.test(x))return BigInt(x);throw new TypeError('Exact integer residue required');}
function key(t,f,k){return JSON.stringify([label(t),label(f),sheet(k).toString()]);}
class Paths{
  constructor(entries=[]){this.terms=new Map();for(const [t,f,k,v] of entries){const id=key(t,f,k),z=(this.terms.get(id)||ZERO).add(Cut.of(v));if(z.zero())this.terms.delete(id);else this.terms.set(id,z);}}
  entries(){return [...this.terms].map(([k,v])=>[...JSON.parse(k),v]);}
  coeff(t,f,k){return this.terms.get(key(t,f,k))||ZERO;}
  add(b){return new Paths(this.entries().concat(b.entries()));}
  neg(){return new Paths(this.entries().map(([t,f,k,v])=>[t,f,k,v.neg()]));}
  sub(b){return this.add(b.neg());}
  mul(b){const out=[];for(const [t,f,k,v] of this.entries())for(const [u,s,l,w] of b.entries())if(f===u)out.push([t,s,BigInt(k)+BigInt(l),v.mul(w)]);return new Paths(out);}
  dagger(){return new Paths(this.entries().map(([t,f,k,v])=>[f,t,-BigInt(k),v.dagger()]));}
  eq(b){return this.sub(b).terms.size===0;}
  mass(){return this.entries().reduce((s,[,,,v])=>s.add(v.gauge()),new F());}
  identityCoefficientSum(){return this.entries().reduce((s,[t,f,k,v])=>t===f&&BigInt(k)===0n?s.add(v):s,ZERO);}
  coefficientEnergy(){return this.entries().reduce((s,[,,,v])=>s.add(v.norm2()),new F());}
  endpointShadow(labels){if(new Set(labels).size!==labels.length)throw new TypeError('Distinct object labels required');labels.forEach(label);const a=zeros(labels.length);for(const [t,f,k,v] of this.entries()){const i=labels.indexOf(t),j=labels.indexOf(f);if(i<0||j<0)throw new RangeError('Undeclared object in endpoint chart');a[i][j]=a[i][j].add(v);}return a;}
  toJSON(){return this.entries().sort((a,b)=>JSON.stringify(a.slice(0,3)).localeCompare(JSON.stringify(b.slice(0,3)))).map(([t,f,k,v])=>({to:t,from:f,sheet:k,coefficient:v.toJSON()}));}
}
function arrow(to,from,k=0,coefficient=ONE){return new Paths([[to,from,k,coefficient]]);}
function unit(labels){if(new Set(labels).size!==labels.length)throw new TypeError('Distinct object labels required');return new Paths(labels.map(x=>[x,x,0,ONE]));}
module.exports={Paths,arrow,unit};
