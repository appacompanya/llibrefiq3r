// MRU i MRUA: el patinet i les gràfiques v–t i x–t alhora
const PX=x=>60+x*24, ROAD=150, TMAX=8;
const MOV={
  mru:{f:t=>({x:4*t,v:4,a:0})},
  mrua:{f:t=>({x:.5*t*t,v:t,a:1})},
  fren:{f:t=>t<=4?{x:8*t-t*t,v:8-2*t,a:-2}:{x:16,v:0,a:0}}
};
const GV={x:70,y:225,w:380,h:230,ym:10,ys:2,yl:"v (m/s)"}, GX={x:550,y:225,w:380,h:230,ym:40,ys:10,yl:"x (m)"};
const gx=(g,t)=>g.x+t/TMAX*g.w, gy=(g,v)=>g.y+g.h-v/g.ym*g.h;
function axes(g,title){ctx.save();ctx.strokeStyle=C.line;ctx.lineWidth=1;ctx.font="600 13px "+FONT;ctx.fillStyle=C.muted;ctx.textAlign="right";ctx.textBaseline="middle";
  for(let v=0;v<=g.ym;v+=g.ys){const y=gy(g,v);ctx.beginPath();ctx.moveTo(g.x,y);ctx.lineTo(g.x+g.w,y);ctx.stroke();ctx.fillText(String(v),g.x-8,y);}
  ctx.textAlign="center";ctx.textBaseline="top";for(let t=0;t<=TMAX;t++){const x=gx(g,t);ctx.beginPath();ctx.moveTo(x,g.y);ctx.lineTo(x,g.y+g.h);ctx.stroke();ctx.fillText(String(t),x,g.y+g.h+6);}
  ctx.strokeStyle=C.fg;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(g.x,g.y-6);ctx.lineTo(g.x,g.y+g.h);ctx.lineTo(g.x+g.w+6,g.y+g.h);ctx.stroke();ctx.restore();
  T(g.yl,g.x,g.y-18,{s:14,w:700,a:"left"});T("t (s)",g.x+g.w+4,g.y+g.h+24,{s:14,w:700,a:"right"});T(title,g.x+g.w/2,g.y-18,{s:15,w:700,c:C.muted});}
function curve(g,f,key,t1,col,lw=3.5,dash){ctx.save();ctx.strokeStyle=col;ctx.lineWidth=lw;ctx.lineJoin="round";if(dash)ctx.setLineDash(dash);ctx.beginPath();
  for(let k=0;k<=120;k++){const t=t1*k/120;const p=f(t);const x=gx(g,t),y=gy(g,p[key]);k?ctx.lineTo(x,y):ctx.moveTo(x,y);}ctx.stroke();ctx.restore();}
function dot(g,t,val,col){ctx.save();ctx.fillStyle=col;ctx.beginPath();ctx.arc(gx(g,t),gy(g,val),6,0,7);ctx.fill();ctx.restore();}
function road(){ctx.save();ctx.strokeStyle=C.muted;ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(40,ROAD);ctx.lineTo(930,ROAD);ctx.stroke();ctx.lineWidth=1.5;
  for(let m=0;m<=36;m+=2){const x=PX(m);ctx.beginPath();ctx.moveTo(x,ROAD);ctx.lineTo(x,ROAD+(m%4?6:11));ctx.stroke();if(m%4===0)T(m+" m",x,ROAD+22,{s:12,w:600,c:C.muted});}ctx.restore();}
function scooter(x,col){const y=ROAD;ctx.save();ctx.strokeStyle=C.fg;ctx.lineWidth=3;ctx.lineCap="round";
  ctx.fillStyle=col;ctx.beginPath();ctx.arc(x-22,y-9,9,0,7);ctx.arc(x+22,y-9,9,0,7);ctx.fill();
  ctx.beginPath();ctx.moveTo(x-26,y-18);ctx.lineTo(x+16,y-18);ctx.lineTo(x+22,y-9);ctx.moveTo(x+16,y-18);ctx.lineTo(x+20,y-66);ctx.lineTo(x+12,y-68);ctx.stroke();
  // persona
  ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x-6,y-20);ctx.lineTo(x-2,y-48);ctx.lineTo(x+2,y-76);ctx.moveTo(x+2,y-20);ctx.lineTo(x-2,y-48);ctx.moveTo(x+2,y-70);ctx.lineTo(x+14,y-64);ctx.stroke();
  ctx.fillStyle=C.fg;ctx.beginPath();ctx.arc(x+3,y-87,9,0,7);ctx.fill();ctx.restore();}
function marks(f,t1,col){let lastX=-99;for(let k=0;k<=Math.floor(t1+1e-9);k++){const x=PX(f(k).x);ctx.save();ctx.fillStyle=col;ctx.beginPath();ctx.arc(x,ROAD,5,0,7);ctx.fill();ctx.restore();
  if(x-lastX>26){T(k+" s",x,ROAD-112,{s:12,w:700,c:col});lastX=x;}}}
let READ={t:0,x:0,v:0,a:0};
function scene(m,t1,o={}){const f=MOV[m].f;road();
  if(o.ghost){curve(GV,MOV[o.ghost].f,"v",TMAX,"#9aa3ad",2.5,[6,5]);curve(GX,MOV[o.ghost].f,"x",TMAX,"#9aa3ad",2.5,[6,5]);}
  axes(GV,"Gràfica velocitat–temps");axes(GX,"Gràfica posició–temps");
  if(o.under)o.under();
  marks(f,t1,C.acc);curve(GV,f,"v",t1,C.acc);curve(GX,f,"x",t1,C.acc);const p=f(t1);dot(GV,t1,p.v,C.acc);dot(GX,t1,p.x,C.acc);scooter(PX(p.x),C.acc);
  READ={t:t1,...p};}
const SIM={W:960,H:500,steps:[
  {t:"Moviment uniforme (MRU)",d:8000,x:"<p>El patinet va sempre a <b>4 m/s</b>. Els punts marquen on és cada segon: estan <b>igual de separats</b>, 4 m.</p><p>A la gràfica v–t, la velocitat és una <b>recta horitzontal</b>. A la gràfica x–t, una recta inclinada.</p>",
    draw(t){scene("mru",TMAX*t);}},
  {t:"Moviment accelerat (MRUA)",d:8000,x:"<p>Ara el patinet surt <b>del repòs</b> i guanya 1 m/s cada segon: la seva acceleració és <b>a = 1 m/s²</b>.</p><p>Els punts cada vegada estan <b>més separats</b>. A la gràfica v–t surt una <b>recta que puja</b>. En gris, el MRU d'abans per comparar.</p>",
    draw(t){scene("mrua",TMAX*t,{ghost:"mru"});}},
  {t:"El pendent és l'acceleració",d:2200,x:"<p>El <b>pendent</b> de la recta v–t és l'acceleració:</p><p><b>a = Δv / Δt</b> = (6 − 2) m/s ÷ (6 − 2) s = <b>1 m/s²</b></p><p>Com més inclinada és la recta, més acceleració.</p>",
    draw(t){scene("mrua",TMAX,{under(){const p=ease(t);ctx.save();ctx.strokeStyle=C.cold;ctx.lineWidth=3;ctx.setLineDash([7,5]);
      ctx.beginPath();ctx.moveTo(gx(GV,2),gy(GV,2));ctx.lineTo(gx(GV,lerp(2,6,p)),gy(GV,2));if(p>.5){ctx.lineTo(gx(GV,6),gy(GV,lerp(2,6,seg(p,.5,1))));}ctx.stroke();ctx.restore();
      T("Δt = 4 s",gx(GV,4),gy(GV,2)+18,{s:14,w:700,c:C.cold,al:seg(t,.3,.5)});T("Δv = 4 m/s",gx(GV,6)+12,gy(GV,4),{s:14,w:700,c:C.cold,a:"left",al:seg(t,.8,1)});}});}},
  {t:"L'àrea és la distància",d:6000,x:"<p>L'<b>àrea sota la gràfica v–t</b> és la distància recorreguda. Aquí és un triangle:</p><p>x = (base × altura) ÷ 2 = (8 s × 8 m/s) ÷ 2 = <b>32 m</b></p><p>Coincideix amb x = ½ · a · t². Al MRU, el rectangle 8 s × 4 m/s també dona 32 m.</p>",
    draw(t){const t1=TMAX*t;scene("mrua",t1,{under(){ctx.save();ctx.fillStyle=C["acc-soft"];ctx.globalAlpha=.9;ctx.beginPath();ctx.moveTo(gx(GV,0),gy(GV,0));ctx.lineTo(gx(GV,t1),gy(GV,t1));ctx.lineTo(gx(GV,t1),gy(GV,0));ctx.closePath();ctx.fill();ctx.restore();
      T("àrea = "+fmt(.5*t1*t1,1)+" m",gx(GV,t1*.66),gy(GV,t1*.2),{s:15,w:800,c:C.acc,al:t>.05?1:0});}});}},
  {t:"Una frenada",d:8000,x:"<p>El patinet va a 8 m/s i <b>frena</b> amb a = −2 m/s². Perd 2 m/s cada segon i s'atura als <b>4 s</b>. Els punts cada vegada estan <b>més junts</b>.</p><p>Distància de frenada = àrea del triangle = (4 s × 8 m/s) ÷ 2 = <b>16 m</b>.</p>",
    draw(t){scene("fren",TMAX*t,{ghost:"mrua"});}},
  {t:"Les equacions del MRUA",d:1500,x:"<p><b>v = v₀ + a · t</b></p><p><b>x = x₀ + v₀ · t + ½ · a · t²</b></p><p>Gràfica v–t: una <b>recta</b> (el pendent és a). Gràfica x–t: una <b>paràbola</b>. Exemple, l'arrencada del pas 2 als 5 s: v = 0 + 1 · 5 = 5 m/s; x = ½ · 1 · 5² = 12,5 m.</p>",
    draw(t){scene("mrua",5*ease(t),{ghost:"mrua"});if(t>=1){T("t = 5 s → v = 5 m/s",gx(GV,5)+10,gy(GV,5)-16,{s:14,w:700,c:C.acc,a:"left"});T("x = 12,5 m",gx(GX,5)+10,gy(GX,12.5)-16,{s:14,w:700,c:C.acc,a:"left"});}}}
],
panel(){const r=READ;const h=`<div class="read"><div><span>Temps</span><b>${fmt(r.t,1)} s</b></div><div><span>Posició</span><b>${fmt(r.x,1)} m</b></div><div><span>Velocitat</span><b>${fmt(r.v,1)} m/s</b></div><div><span>Acceleració</span><b>${fmt(r.a,0)} m/s²</b></div></div>`;$("#extra").innerHTML=h;}
};
