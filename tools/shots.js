// Makes the chooser screenshots: node tools/shots.js (with the site served on :8765)
const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const out=path.join(__dirname,'..','site','img','shots');
for(let n=1;n<=5;n++){const p=await b.newPage({viewport:{width:1280,height:800},colorScheme:'light'});
 await p.goto(`http://localhost:8765/designs/${n}.html`,{waitUntil:'networkidle'});
 await p.screenshot({path:`${out}/d${n}.png`});await p.close();}
await b.close();})();
