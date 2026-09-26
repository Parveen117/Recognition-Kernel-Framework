'use strict';
/** Reject network access during an isolated verification run. */
const Module=require('node:module'),load=Module._load;
const blocked=new Set(['http','https','http2','net','tls','dns','dgram','undici']);
Module._load=function(name,...args){if(blocked.has(name.replace(/^node:/,'')))throw new Error('Network use is forbidden in offline verification: '+name);return load.call(this,name,...args);};
globalThis.fetch=()=>{throw new Error('fetch is forbidden in offline verification');};
