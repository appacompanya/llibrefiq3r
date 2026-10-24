/* Llegeix un literal JS (const NOM = {...}) d’un fitxer HTML/JS sense executar la pàgina. */
const fs=require('fs');
function grab(file,name){
  const s=fs.readFileSync(file,'utf8');
  const re=new RegExp('^const '+name+' = ','m'); const m=re.exec(s); if(!m) return null;
  let i=m.index+m[0].length; // find end: balanced braces/brackets respecting strings
  let depth=0,st=null,j=i;
  for(;j<s.length;j++){const c=s[j];
    if(st){ if(c==='\\'){j++;continue;} if(c===st) st=null; continue;}
    if(c==='"'||c==="'"||c==='`'){st=c;continue;}
    if(c==='{'||c==='['||c==='(') depth++;
    else if(c==='}'||c===']'||c===')'){depth--; if(depth===0){j++;break;}}
  }
  const src=s.slice(i,j);
  return {src, start:m.index, end:j, val:eval('('+src+')')};
}
module.exports=grab;
if(require.main===module){
  const f=process.argv[2];
  for(const n of ['D','L','SDAS','EVAL','CRIT_NAMES']){const g=grab(f,n); console.log(n, g? (Array.isArray(g.val)?g.val.length:Object.keys(g.val).length):null, g&&g.src.length);}
}
