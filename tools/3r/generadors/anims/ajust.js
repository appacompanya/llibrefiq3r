// Ajust d'equacions químiques amb models de boles
const K=1.45;
const ATOM={H:{r:13*K,f:"#ffffff",e:"#c9d0d7",lc:"#1f2328"},O:{r:21*K,f:"#ee5a4e",e:"#a8251b",lc:"#fff"},C:{r:21*K,f:"#5b616b",e:"#24282e",lc:"#fff"}};
const MOL={
  H2:[["H",-11,0],["H",11,0]],
  O2:[["O",-17,0],["O",17,0]],
  H2O:[["H",-21,11],["H",21,11],["O",0,-5]],
  H2O2:[["H",-38,-17],["H",38,17],["O",-15,0],["O",15,0]],
  CH4:[["H",0,-27],["H",0,27],["H",-27,0],["H",27,0],["C",0,0]],
  CO2:[["O",-36,0],["O",36,0],["C",0,0]]
};
for(const k in MOL)MOL[k]=MOL[k].map(([e,x,y])=>[e,x*K,y*K]);
const NAME={H2:"H₂",O2:"O₂",H2O:"H₂O",H2O2:"H₂O₂",CH4:"CH₄",CO2:"CO₂"};
const CY=185, ZL=[24,420], ZR=[540,936];
function layout(side,z){const n=side.length,pw=40,cw=(z[1]-z[0]-pw*(n-1))/n;const mols=[],plus=[];
  side.forEach(([sp,k],c)=>{const cx=z[0]+c*(cw+pw)+cw/2,gap=124,y0=CY-(k-1)*gap/2;for(let j=0;j<k;j++)mols.push({sp,j,c,x:cx,y:y0+j*gap});if(c<n-1)plus.push(cx+cw/2+pw/2);});
  return {mols,plus};}
function atomsOf(lay){const out=[];for(const m of lay.mols)for(const [el,dx,dy] of MOL[m.sp])out.push({el,x:m.x+dx,y:m.y+dy,cx:m.x,cy:m.y});return out;}
function drawAtom(a,sc,al,hl,sec){const A=ATOM[a.el];BALL(a.x,a.y,A.r*sc,A.f,A.e,{l:a.el,lc:A.lc,al});
  if(hl&&sc>.5){ctx.save();ctx.globalAlpha=.55+.45*Math.sin(sec*5);ctx.strokeStyle=C.acc;ctx.lineWidth=3;ctx.beginPath();ctx.arc(a.x,a.y,A.r*sc+5,0,7);ctx.stroke();ctx.restore();}}
function drawMol(m,sc,al,hl,sec){for(const [el,dx,dy] of MOL[m.sp])drawAtom({el,x:m.x+dx*sc,y:m.y+dy*sc},sc,al,hl===el,sec);}
function count(scene){const r={L:{H:0,O:0,C:0},R:{H:0,O:0,C:0}};for(const s of ["L","R"])for(const [sp,k] of scene[s])for(const [el] of MOL[sp])r[s][el]+=k;return r;}
function arrow(){ARROW(448,CY,512,CY,{c:C.fg,lw:4,h:16});}
function plusSigns(lay){for(const x of lay.plus)T("+",x,CY,{s:34,w:700,c:C.muted});}
function equation(scene,al=1){const segs=[];const side=(arr)=>arr.forEach(([sp,k],c)=>{if(c)segs.push([" + ",0]);if(k>1)segs.push([k+" ",1]);segs.push([NAME[sp],0]);});
  side(scene.L);segs.push(["  →  ",0]);side(scene.R);
  ctx.save();ctx.font="700 32px "+FONT;let w=0;for(const [s] of segs)w+=ctx.measureText(s).width;let x=480-w/2;ctx.textBaseline="middle";ctx.globalAlpha=al;
  for(const [s,a] of segs){ctx.fillStyle=a?C.acc:C.fg;ctx.fillText(s,x,372);x+=ctx.measureText(s).width;}ctx.restore();}
function labels(){T("REACTIUS",222,40,{s:13,w:700,c:C.muted});T("PRODUCTES",738,40,{s:13,w:700,c:C.muted});}
function prevScene(){const k=SIM.steps.indexOf(SIM.cur);for(let j=k-1;j>=0;j--){const s=SIM.steps[j];if(s.sc)return s.sc;}return null;}
function drawScene(s,t,sec){const sc=s.sc,show=s.show||sc,pv=s.fresh?null:prevScene();
  labels();arrow();
  for(const side of ["L","R"]){const lay=layout(show[side],side==="L"?ZL:ZR);plusSigns(lay);
    for(const m of lay.mols){const had=pv&&pv[side].some(([sp,k])=>sp===m.sp&&k>m.j)&&!(s.show&&side==="R");
      const p=had?1:pop(ease(clamp(t*1.25)));drawMol(m,p,1,s.hl,sec);}}
  if(s.show){ctx.save();ctx.strokeStyle=C.hot;ctx.lineWidth=7;ctx.lineCap="round";const k=ease(seg(t,.35,.75));
    ctx.beginPath();ctx.moveTo(680,130);ctx.lineTo(lerp(680,800,k),lerp(130,270,k));ctx.stroke();
    if(k>=1){ctx.beginPath();ctx.moveTo(800,130);ctx.lineTo(680,270);ctx.stroke();}ctx.restore();
    T("H₂O₂ és aigua oxigenada: una altra substància!",738,306,{s:16,w:700,c:C.hot,al:seg(t,.6,1)});}
  equation(show);}
function drawReact(s,t,sec){const sc=s.sc;labels();arrow();
  const la=layout(sc.L,ZL),ra=layout(sc.R,ZR);const A=atomsOf(la),B=atomsOf(ra);
  const pairs=[];for(const el of ["C","O","H"]){const a=A.filter(z=>z.el===el).sort((p,q)=>p.y-q.y||p.x-q.x),b=B.filter(z=>z.el===el).sort((p,q)=>p.y-q.y||p.x-q.x);a.forEach((z,k)=>pairs.push([z,b[k]]));}
  const s1=ease(seg(t,0,.18)),p=ease(seg(t,.22,.86));
  if(t<.2)plusSigns(la);
  if(t>.86)plusSigns(ra);
  // les boles es dibuixen H primer perquè quedin darrere
  const pos=pairs.map(([a,b])=>{let x=a.x+(a.x-a.cx)*.7*s1,y=a.y+(a.y-a.cy)*.7*s1+Math.sin(sec*30+a.x)*1.5*s1*(1-p);
    if(p>0){x=lerp(x,b.x,p);y=lerp(y,b.y,p)-Math.sin(Math.PI*p)*46;}return {el:a.el,x,y};}).sort((u,v)=>(u.el==="H"?0:1)-(v.el==="H"?0:1));
  for(const a of pos)drawAtom(a,1,1,null,sec);
  T("Es trenquen enllaços…",222,320,{s:15,w:700,c:C.muted,al:seg(t,.05,.2)*(1-seg(t,.5,.7))});
  T("…i els àtoms es reorganitzen",738,320,{s:15,w:700,c:C.muted,al:seg(t,.75,.95)});
  equation(sc,seg(t,.8,1));}
const H2O_1={L:[["H2",1],["O2",1]],R:[["H2O",1]]};
const H2O_2={L:[["H2",1],["O2",1]],R:[["H2O",2]]};
const H2O_3={L:[["H2",2],["O2",1]],R:[["H2O",2]]};
const CH_1={L:[["CH4",1],["O2",1]],R:[["CO2",1],["H2O",1]]};
const CH_2={L:[["CH4",1],["O2",1]],R:[["CO2",1],["H2O",2]]};
const CH_3={L:[["CH4",1],["O2",2]],R:[["CO2",1],["H2O",2]]};
const st=(o)=>Object.assign({d:1300,draw(t,sec){SIM.cur=this;(this.react?drawReact:drawScene)(this,t,sec);}},o);
const SIM={W:960,H:420,cur:null,steps:[
  st({t:"Hidrogen + oxigen → aigua",sc:H2O_1,fresh:true,x:"<p>Als autobusos d'hidrogen, dins la pila de combustible, l'hidrogen reacciona amb l'oxigen i es forma aigua. Primer escrivim les fórmules de reactius i productes: <b>H₂ + O₂ → H₂O</b>.</p><p>Cada bola és un àtom: blanca, hidrogen; vermella, oxigen.</p>"}),
  st({t:"Comptem els àtoms",sc:H2O_1,hl:"O",loop:true,x:"<p>Comptem els àtoms de cada element a banda i banda (taula de sota). Hidrogen: 2 i 2. Oxigen: 2 a l'esquerra però només 1 a la dreta.</p><p>En una reacció els àtoms no es creen ni es destrueixen (<b>llei de Lavoisier</b>). L'equació encara <b>no està ajustada</b>.</p>"}),
  st({t:"Error típic: canviar la fórmula",sc:H2O_1,show:{L:H2O_1.L,R:[["H2O2",1]]},d:1800,x:"<p>Si escrivíssim H₂O₂ els comptes quadrarien… però H₂O₂ és <b>aigua oxigenada</b>, una substància diferent!</p><p>Mai no canviem els subíndexs d'una fórmula. Només podem canviar <b>quantes molècules</b> hi ha: els <b>coeficients</b>.</p>"}),
  st({t:"Coeficient 2 davant de l'aigua",sc:H2O_2,hl:"H",loop:true,x:"<p>Hi posem una molècula d'aigua més: <b>2 H₂O</b>. Ara l'oxigen quadra (2 i 2), però l'hidrogen no: 2 a l'esquerra i 4 a la dreta.</p>"}),
  st({t:"Coeficient 2 davant de l'hidrogen",sc:H2O_3,x:"<p>Hi posem una molècula d'hidrogen més: <b>2 H₂</b>. Hidrogen: 4 i 4. Oxigen: 2 i 2. Ja està ajustada:</p><p><b>2 H₂ + O₂ → 2 H₂O</b></p><p>El coeficient 1 no s'escriu.</p>"}),
  st({t:"Què passa de debò?",sc:H2O_3,react:true,d:3400,x:"<p>Es trenquen els enllaços de les molècules de reactius i els àtoms es <b>reorganitzen</b> per formar les molècules de producte.</p><p>Són els mateixos 6 àtoms abans i després: per això la massa es conserva.</p>"}),
  st({t:"Un altre: la combustió del metà",sc:CH_1,fresh:true,x:"<p>El metà (CH₄) és el gas natural. Quan crema amb oxigen es formen diòxid de carboni i aigua: <b>CH₄ + O₂ → CO₂ + H₂O</b>. La bola gris és el carboni.</p><p>Carboni: 1 i 1. Hidrogen: 4 i 2. Oxigen: 2 i 3. Truc: deixem per al final l'element que surt en més substàncies (aquí, l'oxigen).</p>"}),
  st({t:"Primer, l'hidrogen",sc:CH_2,hl:"O",loop:true,x:"<p>Per tenir 4 hidrògens a la dreta calen <b>2 H₂O</b>. Hidrogen: 4 i 4.</p><p>Ara l'oxigen: 2 a l'esquerra; a la dreta, 2 (del CO₂) + 2 (de les dues H₂O) = 4.</p>"}),
  st({t:"Per acabar, l'oxigen",sc:CH_3,x:"<p>Per tenir 4 oxígens a l'esquerra calen <b>2 O₂</b>. Ara tot quadra:</p><p><b>CH₄ + 2 O₂ → CO₂ + 2 H₂O</b></p>"}),
  st({t:"Els àtoms es reorganitzen",sc:CH_3,react:true,d:3600,x:"<p>Compta les boles de cada color abans i després: 1 de carboni, 4 d'hidrogen i 4 d'oxigen a cada banda.</p>"}),
  st({t:"Com s'ajusta una equació",sc:CH_3,x:"<p>1. Escriu bé les fórmules de reactius i productes.</p><p>2. Compta els àtoms de cada element a cada banda.</p><p>3. Canvia només els <b>coeficients</b>, mai els subíndexs.</p><p>4. Comença pels elements que surten en una sola substància a cada banda; deixa per al final els que surten en moltes (sovint O i H).</p><p>5. Torna-ho a comptar tot.</p>"})
],
panel0(s){const c=count(s.show||s.sc);const els=["H","O","C"].filter(e=>c.L[e]||c.R[e]);const nm={H:"Hidrogen (H)",O:"Oxigen (O)",C:"Carboni (C)"};
  $("#extra").innerHTML='<table class="cnt"><tr><th>Element</th><th>Reactius</th><th>Productes</th><th></th></tr>'+els.map(e=>`<tr><td>${nm[e]}</td><td>${c.L[e]}</td><td>${c.R[e]}</td><td>${c.L[e]===c.R[e]?'<span class="si">✓</span>':'<span class="no">✗</span>'}</td></tr>`).join("")+"</table>";}
};
