const fs=require('fs'); const s=fs.readFileSync('template.html','utf8');
function grab(name, open, close){ const i=s.indexOf('const '+name+' = '); let j=s.indexOf(open,i); let d=0,k=j; for(;k<s.length;k++){ if(s[k]===open)d++; else if(s[k]===close){d--; if(!d)break;} } return s.slice(j,k+1); }
const D=eval('('+grab('D','{','}')+')'), L=eval('('+grab('L','{','}')+')'), SDAS=eval('('+grab('SDAS','[',']')+')');
fs.writeFileSync('links.json', JSON.stringify({D,L,SDAS:SDAS.map(x=>({n:x.n,title:x.title,sessions:x.sessions.map(z=>({t:z.t,d:z.d||[],dt:z.dt||[],l:z.l||[]})),teacher:(x.teacher||[]).map(z=>({b:z.b,d:z.d||[]}))}))},null,1));
console.log(Object.keys(D).length, SDAS.length);
