'use strict';
/** Check declared source dependency roles, not correctness of the proofs. */
function nativeDependencies(id,nodes){const forbidden=new Set(['HILBERT_PRIMITIVE','EXTERNAL_ANALYTIC_IMPORT','PHYSICAL_ADAPTER','REPRESENTATION_SHADOW']);const seen=new Set(),active=new Set(),order=[];
  function visit(k){if(active.has(k))throw new Error('Cyclic theorem dependency: '+k);if(seen.has(k))return;const n=nodes[k];if(!n)throw new Error('Unbound dependency: '+k);if(forbidden.has(n.role))throw new Error('Non-native premise on this derivation route: '+k);if(!Array.isArray(n.requires))throw new Error('Missing declared dependency list: '+k);active.add(k);n.requires.forEach(visit);active.delete(k);seen.add(k);order.push(k);}visit(id);return order;}
module.exports={nativeDependencies};
