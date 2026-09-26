'use strict';
/** One read-only verification command for the entire standalone engine. */
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),cp=require('node:child_process'),assert=require('node:assert/strict');
const root=__dirname,sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const write=process.argv.includes('--write');
if(!write&&!process.argv.includes('--check')){console.error('Usage: node verify_all.cjs --check  (or reviewed --write)');process.exit(64);}
const sources={};
function walk(dir){for(const e of fs.readdirSync(path.join(root,dir),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){const rel=path.posix.join(dir,e.name);if(['sources','node_modules','.git'].includes(rel)||rel.startsWith('audit/generated/'))continue;if(e.isDirectory()){walk(rel);continue;}if(e.isSymbolicLink())throw new Error('Active source symlinks are not admitted');if(['audit/MASTER_CERTIFICATE.json','audit/MASTER_EXPECTED.sha256','audit/FINITE_CERTIFICATE.json','audit/PANINIAN_CERTIFICATE.json'].includes(rel))continue;sources[rel]=sha(fs.readFileSync(path.join(root,rel)));}}
walk('');
const commands=[
 ['tests/verify_core.cjs'],['tests/verify.cjs','--check'],['tests/verify_paninian.cjs','--check'],['tests/verify_workbench.cjs','--json'],
 ['tests/verify_weighted.cjs','--check','--json'],
 ['tests/mutation_controls.cjs'],['tests/mutate_paninian.cjs'],['tests/mutate_workbench.cjs'],['tests/mutate_weighted.cjs']
];
const runs=[];
for(const args of commands){const r=cp.spawnSync(process.execPath,['--require',path.join(root,'tests/offline_guard.cjs'),...args],{cwd:root,encoding:'utf8',timeout:90000});if(r.status!==0)throw new Error('Verification failed: '+args.join(' ')+'\n'+r.stdout+'\n'+r.stderr);let parsed=null;try{parsed=JSON.parse(r.stdout);}catch{}const count=parsed?.check_count??Number((r.stdout.match(/(?:UNPINNED|CHECKS|OPERATOR) (\d+)/)||[])[1]||0);runs.push({command:['node',...args],exit_status:r.status,stdout_sha256:sha(r.stdout.trim()),check_count:count,mutation_controls:parsed?.controls?.length||0});}
const jobPins={};for(const name of ['emk','jet','infinite']){const j=JSON.parse(fs.readFileSync(path.join(root,'examples',name+'_job.json'),'utf8'));jobPins[name]=require('./core/paninian_operator.cjs').digest(j);}
assert.deepEqual(jobPins,JSON.parse(fs.readFileSync(path.join(root,'audit/EXAMPLE_INPUTS.json'),'utf8')));
const report={protocol:'RKF_CANONICAL_OPERATOR_V0_5',status:'PASS_LOCAL_OFFLINE_VERIFICATION',canonical_home:JSON.parse(fs.readFileSync(path.join(root,'CANONICAL_HOME.json'),'utf8')),source_sha256:Object.fromEntries(Object.entries(sources).sort()),runs,example_input_sha256:jobPins,scope:{primitive_hilbert_space:false,independent_proof_assistant:false,private_patent_sources_included:false,historical_python_tests_rerun:false,remote_ci_pass_claimed:false}};
const text=JSON.stringify(report,null,2)+'\n',hash=sha(text),file=path.join(root,'audit/MASTER_CERTIFICATE.json'),pin=path.join(root,'audit/MASTER_EXPECTED.sha256');
if(write){fs.writeFileSync(file,text);fs.writeFileSync(pin,hash+'\n');}else{assert.equal(fs.readFileSync(file,'utf8'),text,'Source or result drift');assert.equal(fs.readFileSync(pin,'utf8').trim(),hash,'Master pin mismatch');}
console.log('PASS_CANONICAL_OPERATOR_V0_5',Object.keys(sources).length,'SOURCE_FILES',hash);
