#!/usr/bin/env node
'use strict';
const fs=require('node:fs');const {runJob,replayJob}=require('./core/workbench.cjs');
function read(path){const stat=fs.statSync(path);if(!stat.isFile()||stat.size>8*1024*1024)throw new Error('Input must be a JSON file of at most 8 MiB');return JSON.parse(fs.readFileSync(path,'utf8'));}
try {
  const [mode,file,...args]=process.argv.slice(2);
  if(mode==='solve'&&file&&args.length<=1){const result=runJob(read(file));const out=JSON.stringify(result,null,2)+'\n';if(args[0])fs.writeFileSync(args[0],out,{flag:'wx'});else process.stdout.write(out);if(result.status!=='VERIFIED_FINITE_JOB')process.exitCode=2;}
  else if(mode==='replay'&&file&&args.length===1)console.log(JSON.stringify(replayJob(read(file),args[0]),null,2));
  else {console.error('Usage: node cli.cjs solve job.json [new-output.json]\n       node cli.cjs replay result.json EXPECTED_INPUT_SHA256');process.exitCode=64;}
} catch(e) {console.error(JSON.stringify({status:'REFUSED',error:e.message}));process.exitCode=1;}
