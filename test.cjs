const t=require('node:test'),a=require('assert/strict'),{execFileSync}=require('child_process'),s=require('./site/scaffold'),templates=require('./site/templates.json');
t('valid names',()=>{for(const n of ['demo','My-site_2','a'.repeat(40)])a.equal(s.validate(n),n);});
t('reject paths/reserved/unsafe',()=>{for(const n of ['', '../x','/tmp/x','a/b','a\\b','.','..','con','LPT9','COM1','a'.repeat(41),'🙂','1site','a b','<img>'])a.throws(()=>s.validate(n));});
t('three starter files',()=>a.deepEqual(Object.keys(s.build('demo',templates)),['index.html','css/style.css','js/main.js']));
t('Python parity',()=>{for(const n of ['demo','My-site_2','a'.repeat(40)]){const x=JSON.parse(execFileSync('python3',['-c',`import json; from T_C0D3 import scaffold; print(json.dumps(scaffold('${n}')))`],{encoding:'utf8'}));a.deepEqual(s.build(n,templates),x);}});
t('no mutation',()=>{const x=JSON.stringify(templates);s.build('demo',templates);a.equal(JSON.stringify(templates),x);});
t('linked paths',()=>{const x=s.build('demo',templates)['index.html'];a.ok(x.includes('href="css/style.css"'));a.ok(x.includes('src="js/main.js"'));});
t('no placeholders left',()=>{for(const v of Object.values(s.build('demo',templates)))a.ok(!v.includes('PROJECT_NAME'));});
t('main only workflow',()=>{const x=require('fs').readFileSync('.github/workflows/pages.yml','utf8');a.ok(x.includes('branches: [main]'));a.ok(!x.includes('workflow_dispatch'));});
