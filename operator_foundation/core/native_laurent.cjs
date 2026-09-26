'use strict';
/** Finite exact Laurent and jet operations over the native rational cut field.
 * The central continuation variable is formal, not physical time. Algebraic
 * coefficient extraction does not assume a contour, a metric, or a pairing.
 */
const o=require('./native_operator.cjs');
const {Cut,F,ZERO,ONE,matrix,zeros,identity,add,sub,scale,mul,equal,isZero,rref,inverse,rank}=o;
function integer(k,minimum=0){if(!Number.isSafeInteger(k)||k<minimum)throw new RangeError('Invalid exact finite index');}
function square(a){a=matrix(a);if(a.length!==a[0].length)throw new RangeError('Square coefficient matrix required');return a;}
function series(entries,n){integer(n,1);const out=new Map();for(const [k,raw] of entries){if(!Number.isSafeInteger(k))throw new RangeError('Integral Laurent exponent required');const a=square(raw);if(a.length!==n)throw new RangeError('Coefficient carrier mismatch');const b=out.has(k)?add(out.get(k),a):a;if(isZero(b))out.delete(k);else out.set(k,b);}return {n,terms:new Map([...out].sort((a,b)=>a[0]-b[0]))};}
function coefficient(s,k){return s.terms.has(k)?s.terms.get(k):zeros(s.n);}
function constant(a){a=square(a);return series([[0,a]],a.length);}
function monomial(a,k){a=square(a);return series([[k,a]],a.length);}
function plus(a,b){if(a.n!==b.n)throw new RangeError('Series carrier mismatch');return series([...a.terms,...b.terms],a.n);}
function times(a,b){if(a.n!==b.n)throw new RangeError('Series carrier mismatch');const entries=[];for(const [i,x] of a.terms)for(const [j,y] of b.terms)entries.push([i+j,mul(x,y)]);return series(entries,a.n);}
function derivative(a){return series([...a.terms].filter(([k])=>k!==0).map(([k,x])=>[k-1,scale(x,k)]),a.n);}
function equalSeries(a,b){if(a.n!==b.n)return false;const keys=new Set([...a.terms.keys(),...b.terms.keys()]);return [...keys].every(k=>equal(coefficient(a,k),coefficient(b,k)));}
function requirePolynomial(a){if([...a.terms.keys()].some(k=>k<0))throw new RangeError('Nonnegative pencil exponents required');}
function verifyInverse(a,b){const unit=constant(identity(a.n));if(!equalSeries(times(a,b),unit)||!equalSeries(times(b,a),unit))throw new RangeError('Not a verified two-sided finite Laurent inverse');}
function trace(a){a=square(a);return a.reduce((s,r,i)=>s.add(r[i]),ZERO);}
function idempotenceDefect(a){return sub(mul(a,a),a);}
function poleOrder(b){return Math.max(0,...[...b.terms.keys()].map(k=>-k));}
function logarithmicResidues(a,b){requirePolynomial(a);verifyInverse(a,b);const d=derivative(a);const right=coefficient(times(b,d),-1),left=coefficient(times(d,b),-1);let r=zeros(a.n),l=zeros(a.n);const q=poleOrder(b);for(let j=1;j<=q;j++){r=add(r,scale(mul(coefficient(b,-j),coefficient(a,j)),j));l=add(l,scale(mul(coefficient(a,j),coefficient(b,-j)),j));}
  if(!equal(r,right)||!equal(l,left))throw new Error('Principal coefficient identity failed');
  return {right,left,rightDefect:idempotenceDefect(right),leftDefect:idempotenceDefect(left),rightIsIdempotent:isZero(idempotenceDefect(right)),leftIsIdempotent:isZero(idempotenceDefect(left)),trace:trace(right),poleOrder:q};
}
function transpose(a){a=matrix(a);return a[0].map((_,j)=>a.map(r=>r[j]));}
function nullspaceRows(a){const r=rref(a),n=r.matrix[0].length;const free=Array.from({length:n},(_,i)=>i).filter(i=>!r.pivots.includes(i));return free.map(j=>{const v=Array(n).fill(ZERO);v[j]=ONE;r.pivots.forEach((p,i)=>v[p]=r.matrix[i][j].neg());return v;});}
function rightInverse(c){c=matrix(c);const r=rref(c),n=c[0].length,m=c.length;if(r.rank!==m)throw new RangeError('Independent quotient rows required');const inv=inverse(c.map(row=>r.pivots.map(j=>row[j]))),out=zeros(n,m);r.pivots.forEach((j,i)=>out[j]=inv[i]);return out;}
function toeplitz(a,depth){requirePolynomial(a);integer(depth,1);const n=a.n,d=n*depth,t=zeros(d);for(let i=0;i<depth;i++)for(let j=0;j<=i;j++){const c=coefficient(a,i-j);for(let r=0;r<n;r++)for(let s=0;s<n;s++)t[i*n+r][j*n+s]=c[r][s];}return t;}
function shift(n,depth){integer(n,1);integer(depth,1);const t=zeros(n*depth);for(let k=0;k<depth-1;k++)for(let j=0;j<n;j++)t[(k+1)*n+j][k*n+j]=ONE;return t;}
function jetQuotient(a,depth){const t=toeplitz(a,depth),s=shift(a.n,depth);if(!equal(mul(t,s),mul(s,t)))throw new Error('Continuation must preserve relation module');const c=nullspaceRows(transpose(t)),d=c.length;
  if(!d)return {depth,ambient:a.n*depth,dimension:0,observer:[],action:[],relation:t,rankSequence:[0],nilpotenceIndex:0,chainLengths:[]};
  const n=mul(mul(c,s),rightInverse(c));if(!isZero(mul(c,t))||!equal(mul(c,s),mul(n,c)))throw new Error('Quotient action did not descend');
  let p=identity(d);const ranks=[d];for(let k=1;k<=depth;k++){p=mul(p,n);ranks.push(rank(p));}
  if(ranks.at(-1)!==0)throw new Error('Truncated continuation must be nilpotent');
  const lengths=[];for(let k=1;k<=depth;k++){const atLeast=ranks[k-1]-ranks[k],next=k<depth?ranks[k]-ranks[k+1]:0;if(atLeast<next)throw new Error('Invalid nilpotent rank ladder');for(let j=0;j<atLeast-next;j++)lengths.push(k);}
  return {depth,ambient:a.n*depth,dimension:d,observer:c,action:n,relation:t,rankSequence:ranks,nilpotenceIndex:ranks.findIndex(x=>x===0),chainLengths:lengths.sort((a,b)=>b-a)};
}
function scalarPolyMultiply(a,b){const out=new Map();for(const [i,x] of a)for(const [j,y] of b){const k=i+j,v=(out.get(k)||ZERO).add(x.mul(y));if(v.zero())out.delete(k);else out.set(k,v);}return out;}
function determinantPolynomial(a){requirePolynomial(a);if(a.n>5)throw new RangeError('Exact permutation determinant is restricted to at most 5 coordinates');let det=new Map();const n=a.n;function rec(row,cols,poly,sign){if(row===n){for(const [k,x] of poly){const v=(det.get(k)||ZERO).add(x.mul(sign));if(v.zero())det.delete(k);else det.set(k,v);}return;}
  for(let j=0;j<n;j++)if(!cols.includes(j)){const p=new Map([...a.terms].map(([k,c])=>[k,c[row][j]]).filter(([,v])=>!v.zero()));if(!p.size)continue;const inversions=cols.filter(c=>c>j).length;rec(row+1,cols.concat(j),scalarPolyMultiply(poly,p),inversions%2?-sign:sign);}}
  rec(0,[],new Map([[0,ONE]]),1);return new Map([...det].sort((a,b)=>a[0]-b[0]));
}
function localPacket(a,{depth}={}){const det=determinantPolynomial(a);if(!det.size)throw new RangeError('Identically singular pencil requires a different module contract');const delta=Math.min(...det.keys());const l=depth===undefined?Math.max(1,delta):depth;const q=jetQuotient(a,l);
  const full=q.dimension===delta; // O^n/AO^n -> its t^l quotient is onto; equal finite lengths make it an isomorphism.
  if(q.dimension>delta)throw new Error('Truncated quotient cannot exceed determinant order');
  return {...q,determinant:det,determinantOrder:delta,fullLocalModule:full,unseenJetDimensions:delta-q.dimension,classification:full?'COMPLETE_LOCAL_JET_MODULE':'TRUNCATED_JET_MEMORY'};
}
function markerValues(a,markers){a=square(a);return markers.map(m=>trace(mul(square(m),a)));}
function matrixUnitMarkers(n){integer(n,1);const out=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++){const e=zeros(n);e[j][i]=ONE;out.push(e);}return out;}
function recoverCompleteMarkers(values,n){integer(n,1);if(values.length!==n*n)throw new RangeError('Complete coordinate marker bank required');return matrix(Array.from({length:n},(_,i)=>values.slice(i*n,(i+1)*n)));}
module.exports={series,coefficient,constant,monomial,plus,times,derivative,equalSeries,verifyInverse,trace,poleOrder,logarithmicResidues,transpose,nullspaceRows,rightInverse,toeplitz,shift,jetQuotient,determinantPolynomial,localPacket,markerValues,matrixUnitMarkers,recoverCompleteMarkers};
