// Enllaç iònic, covalent i metàl·lic amb el model de capes
const EIN="#9aa3ad", EOUT="#2f6db5";
function electron(x,y,c,al=1){ctx.save();ctx.globalAlpha*=al;ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,7,0,7);ctx.fill();ctx.strokeStyle="rgba(0,0,0,.35)";ctx.lineWidth=1;ctx.stroke();ctx.restore();}
function shell(x,y,r,al=1,dash){ctx.save();ctx.globalAlpha*=al;ctx.strokeStyle=C.muted;ctx.lineWidth=1.3;if(dash)ctx.setLineDash([5,5]);ctx.beginPath();ctx.arc(x,y,r,0,7);ctx.stroke();ctx.restore();}
function nucleus(x,y,sym,r=22,col="#C9621C"){BALL(x,y,r,col,"#7a3a10",{l:sym,ls:.8});}
const RS=[38,64,92];
// àtom amb capes; o.skip: angles buits a la capa externa; o.outerAl: opacitat de la capa externa
function bohr(x,y,sym,sh,o={}){nucleus(x,y,sym);const n=sh.length;
  sh.forEach((k,s)=>{const r=RS[s],ext=s===n-1;const al=ext&&o.outerAl!=null?o.outerAl:1;shell(x,y,r,al);
    const slots=ext&&o.slots?o.slots:k;const a0=ext&&o.a0!=null?o.a0:-Math.PI/2;
    for(let j=0,m=0;j<slots&&m<k;j++){if(ext&&o.skip&&o.skip.includes(j))continue;const a=a0+j*2*Math.PI/slots;electron(x+r*Math.cos(a),y+r*Math.sin(a),ext?EOUT:EIN,al);m++;}});}
function ion(x,y,r,col,edge,sgn,sc=1){BALL(x,y,r*sc,col,edge,{l:sgn,ls:1.1});}
function caption(s,x,y,al=1){T(s,x,y,{s:17,w:700,al});}
function sub(s,x,y,al=1){T(s,x,y,{s:14,w:600,c:C.muted,al});}
// estat per a l'enllaç metàl·lic
let EL=[],rnd=mulberry(7);
const MX0=150,MX1=810,MY0=95,MY1=335;
function initMetal(){rnd=mulberry(7);EL=[];for(let k=0;k<34;k++){const a=rnd()*6.283,v=50+rnd()*60;EL.push({x:lerp(MX0,MX1,rnd()),y:lerp(MY0,MY1,rnd()),vx:Math.cos(a)*v,vy:Math.sin(a)*v});}}
function metal(sec,dt,drift,t){const cols=10,rows=4,dx=(MX1-MX0)/(cols-1)*0.94,dy=(MY1-MY0)/(rows-1)*0.9,ox=480-dx*(cols-1)/2,oy=215-dy*(rows-1)/2;
  ctx.save();ctx.fillStyle=C.chip;RR(MX0-40,MY0-35,MX1-MX0+80,MY1-MY0+70,18);ctx.fill();ctx.restore();
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){const j=r*cols+c;const x=ox+c*dx+Math.sin(sec*6+j)*1.6,y=oy+r*dy+Math.cos(sec*5+j*1.3)*1.6;BALL(x,y,21*pop(clamp(t*1.6-j/60)),"#b9c0c8","#6b737c",{l:"+",lc:"#1f2328",ls:1.1});}
  for(const e of EL){e.vx+=(rnd()-.5)*260*dt;e.vy+=(rnd()-.5)*260*dt;const sp=Math.hypot(e.vx,e.vy),tg=95;e.vx*=tg/sp;e.vy*=tg/sp;
    e.x+=(e.vx+drift)*dt;e.y+=e.vy*dt;
    if(drift){if(e.x>MX1+30)e.x=MX0-30;if(e.x<MX0-30)e.x=MX1+30;}else{if(e.x<MX0-25||e.x>MX1+25)e.vx*=-1;e.x=clamp(e.x,MX0-25,MX1+25);}
    if(e.y<MY0-22||e.y>MY1+22)e.vy*=-1;e.y=clamp(e.y,MY0-22,MY1+22);
    electron(e.x,e.y,EOUT,seg(t,.3,.7));}}
function battery(al){ctx.save();ctx.globalAlpha*=al;ctx.strokeStyle=C.fg;ctx.lineWidth=3;
  ctx.beginPath();ctx.moveTo(MX0-42,215);ctx.lineTo(70,215);ctx.lineTo(70,395);ctx.lineTo(455,395);ctx.moveTo(505,395);ctx.lineTo(890,395);ctx.lineTo(890,215);ctx.lineTo(MX1+42,215);ctx.stroke();
  ctx.lineWidth=8;ctx.beginPath();ctx.moveTo(462,383);ctx.lineTo(462,407);ctx.stroke();ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(498,373);ctx.lineTo(498,417);ctx.stroke();ctx.restore();
  T("pila",480,365,{s:14,w:700,c:C.muted,al});T("−",445,422,{s:22,w:800,al});T("+",516,422,{s:22,w:800,al});
  T("electrons cap al pol +",480,40,{s:15,w:700,c:EOUT,al});ARROW(380,58,580,58,{c:EOUT,lw:3,al});}
const NA=[250,190],CL=[710,190];
const SIM={W:960,H:440,steps:[
  {t:"Per què s'uneixen els àtoms?",d:1400,x:"<p>Els àtoms s'uneixen perquè així queden més estables. Una regla útil: tendeixen a tenir <b>8 electrons a la capa externa</b> (regla de l'octet).</p><p>Mirem dos àtoms: el sodi (Na: 2, 8, 1) i el clor (Cl: 2, 8, 7). En blau, els electrons de la capa externa.</p>",
    draw(t){const a=ease(t);bohr(NA[0],NA[1],"Na",[2,8,1],{a0:0,outerAl:a});bohr(CL[0],CL[1],"Cl",[2,8,7],{slots:8,a0:Math.PI,skip:[0],outerAl:a});
      caption("Sodi (Na)",NA[0],318);sub("2, 8, 1 → 1 electró extern",NA[0],346,a);caption("Clor (Cl)",CL[0],318);sub("2, 8, 7 → 7 electrons externs",CL[0],346,a);}},
  {t:"Enllaç iònic: un àtom cedeix electrons",d:2600,x:"<p>L'enllaç iònic es forma entre un <b>metall</b> i un <b>no metall</b>.</p><p>Al sodi li és més fàcil perdre 1 electró que guanyar-ne 7, i al clor li és més fàcil guanyar-ne 1. El sodi <b>cedeix</b> el seu electró extern al clor.</p>",
    draw(t){const p=ease(seg(t,.15,.85));bohr(NA[0],NA[1],"Na",[2,8,0],{});shell(NA[0],NA[1],RS[2],1-.6*p,true);bohr(CL[0],CL[1],"Cl",[2,8,7],{slots:8,a0:Math.PI,skip:[0]});
      const x0=NA[0]+RS[2],x1=CL[0]-RS[2],y=NA[1];const x=lerp(x0,x1,p),yy=y-Math.sin(Math.PI*p)*90;electron(x,yy,EOUT);
      if(p>0&&p<1){ctx.save();ctx.setLineDash([4,6]);ctx.strokeStyle=EOUT;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x0,y);ctx.quadraticCurveTo(480,y-180,x,yy);ctx.stroke();ctx.restore();}
      caption("Na",NA[0],318);caption("Cl",CL[0],318);}},
  {t:"Ions de càrrega contrària s'atrauen",d:2200,x:"<p>El sodi queda amb un electró menys: és un ió positiu, <b>Na⁺</b> (2, 8). El clor en té un de més: és un ió negatiu, <b>Cl⁻</b> (2, 8, 8). Tots dos tenen ara la capa externa completa.</p><p>Les càrregues de signe contrari s'atrauen: això és l'<b>enllaç iònic</b>.</p>",
    draw(t){const p=ease(seg(t,.3,1));const xa=lerp(NA[0],320,p),xb=lerp(CL[0],640,p);
      bohr(xa,NA[1],"Na",[2,8],{});bohr(xb,CL[1],"Cl",[2,8,8],{slots:8,a0:Math.PI});
      T("+",xa+60,NA[1]-70,{s:30,w:800,c:C.hot,al:seg(t,0,.3)});T("−",xb+100,CL[1]-90,{s:34,w:800,c:C.cold,al:seg(t,0,.3)});
      caption("Na⁺",xa,318);sub("2, 8",xa,346);caption("Cl⁻",xb,318);sub("2, 8, 8",xb,346);
      if(p>.5){ARROW(xa+80,NA[1],xb-110,CL[1],{c:C.acc,lw:3,al:seg(p,.5,1)});ARROW(xb-110,CL[1],xa+80,NA[1],{c:C.acc,lw:3,al:seg(p,.5,1)});T("atracció",480,NA[1]-22,{s:14,w:700,c:C.acc,al:seg(p,.5,1)});}}},
  {t:"Una xarxa cristal·lina d'ions",d:2600,x:"<p>Els ions no van en parelles: milions d'ions s'ordenen en una <b>xarxa cristal·lina</b>. La fórmula NaCl només indica la proporció: 1 Na⁺ per cada Cl⁻.</p><p>Per això la sal és dura i trencadissa, es fon a temperatura alta i condueix el corrent quan és fosa o dissolta en aigua, perquè llavors els ions es poden moure.</p>",
    draw(t){const cols=11,rows=6,s=56,ox=480-s*(cols-1)/2,oy=200-s*(rows-1)/2;const L=[];
      for(let r=0;r<rows;r++)for(let c=0;c<cols;c++)L.push({c,r,d:Math.hypot(c-(cols-1)/2,r-(rows-1)/2)});L.sort((a,b)=>a.d-b.d);
      L.forEach((q,k)=>{const sc=pop(clamp(t*1.3*L.length/ (L.length) - k/L.length)*3);const na=(q.c+q.r)%2===0;
        if(na)ion(ox+q.c*s,oy+q.r*s,14,"#9a7ad8","#5a3a9a","+",sc);else ion(ox+q.c*s,oy+q.r*s,25,"#4fbf7a","#1f7a44","−",sc);});
      ctx.save();ctx.globalAlpha=seg(t,.7,1);ctx.fillStyle=C.surface;RR(300,388,360,40,10);ctx.fill();ctx.restore();
      T("Na⁺: petit, lila  ·  Cl⁻: gran, verd",480,408,{s:15,w:700,al:seg(t,.7,1)});}},
  {t:"Enllaç covalent: compartir electrons",d:2800,x:"<p>L'enllaç covalent es forma entre <b>no metalls</b>. Dos àtoms d'hidrogen tenen 1 electró cadascun i cap no el vol cedir: el <b>comparteixen</b>.</p><p>El parell d'electrons compartit, entre els dos nuclis, els manté units: es forma una <b>molècula</b>, H₂.</p>",
    draw(t){const p=ease(seg(t,0,.6)),q=ease(seg(t,.5,1));const y=190,r=62;const xa=lerp(270,442,p),xb=lerp(690,518,p);
      shell(xa,y,r,1,true);shell(xb,y,r,1,true);nucleus(xa,y,"H",18,"#8a9099");nucleus(xb,y,"H",18,"#8a9099");
      electron(lerp(xa-r,480,q),lerp(y,y-9,q),EOUT);electron(lerp(xb+r,480,q),lerp(y,y+9,q),EOUT);
      if(q>.9){T("parell compartit",480,y-95,{s:15,w:700,c:EOUT,al:seg(q,.9,1)});ARROW(480,y-80,480,y-22,{c:EOUT,lw:2,h:10,al:seg(q,.9,1)});}
      caption(q>.95?"Molècula d'hidrogen, H₂ (H–H)":"Dos àtoms d'hidrogen",480,330);}},
  {t:"La molècula d'aigua",d:3000,x:"<p>Només dibuixem la capa externa. L'oxigen hi té 6 electrons i en necessita 2 més: en comparteix <b>un parell amb cada hidrogen</b>.</p><p>Així l'oxigen arriba a 8 electrons i cada hidrogen a 2 (la seva única capa només n'admet 2). Resultat: H₂O. Les substàncies covalents solen formar molècules.</p>",
    draw(t){const O=[480,150],R=74,rh=52,ang=52.25*Math.PI/180,p=ease(seg(t,0,.55)),q=ease(seg(t,.5,1));
      shell(O[0],O[1],R,1,true);nucleus(O[0],O[1],"O",24,"#d8483d");
      for(const sg of [-1,1]){const dx=Math.sin(ang)*sg,dy=Math.cos(ang);const d=lerp(280,112,p);const hx=O[0]+dx*d,hy=O[1]+dy*d;
        shell(hx,hy,rh,1,true);nucleus(hx,hy,"H",18,"#8a9099");
        const mx=O[0]+dx*72,my=O[1]+dy*72,px=-dy*9,py=dx*9;
        electron(lerp(O[0]+dx*R,mx+px,q),lerp(O[1]+dy*R,my+py,q),EOUT);electron(lerp(hx+dx*rh,mx-px,q),lerp(hy+dy*rh,my-py,q),EOUT);}
      for(const a of [-Math.PI/2-.55,-Math.PI/2+.55])for(const da of [-.14,.14])electron(O[0]+R*Math.cos(a+da),O[1]+R*Math.sin(a+da),EOUT);
      caption(q>.95?"Molècula d'aigua, H₂O":"Un oxigen i dos hidrògens",480,395);
      if(q>.95){sub("8 electrons al voltant de l'O · 2 al voltant de cada H",480,420);}}},
  {t:"Enllaç metàl·lic: un núvol d'electrons",loop:true,d:1600,init:initMetal,x:"<p>L'enllaç metàl·lic es forma entre àtoms de <b>metalls</b>. Cada àtom deixa anar els seus electrons externs, que queden lliures i es mouen per tot el metall: un <b>núvol d'electrons</b>.</p><p>Els ions positius queden ordenats en una xarxa i el núvol d'electrons, negatiu, els manté units.</p>",
    draw(t,sec,dt){metal(sec,dt,0,t);caption("Ions positius + núvol d'electrons lliures",480,410);}},
  {t:"Per què el coure condueix?",loop:true,d:1600,init:initMetal,x:"<p>Si connectem el metall a una pila, els electrons lliures avancen tots cap al pol positiu: és el <b>corrent elèctric</b>. Per això els cables del mòbil són de <b>coure</b>.</p><p>Al plàstic del separador de la bateria (enllaç covalent) els electrons no estan lliures: no condueix. Els metalls també es poden doblegar i estirar sense trencar-se, perquè els ions llisquen dins el núvol.</p>",
    draw(t,sec,dt){metal(sec,dt,70,1);battery(seg(t,0,.5));}},
  {t:"Resum dels tres enllaços",d:1800,x:"<p>Per saber quin enllaç hi ha, mira de quins elements es tracta: <b>metall + no metall</b> → iònic; <b>no metall + no metall</b> → covalent; <b>metall + metall</b> → metàl·lic.</p>",
    draw(t){const cards=[["Iònic",C.hot,"metall + no metall","un àtom cedeix electrons i l'altre els capta: ions + i −","xarxa cristal·lina d'ions","NaCl (sal), LiCoO₂ (bateria)"],["Covalent",C.cold,"no metall + no metall","els àtoms comparteixen parells d'electrons","sobretot molècules","H₂O, CO₂, O₂, plàstics"],["Metàl·lic",C.ok,"metall + metall","els electrons externs queden lliures","ions + en un núvol d'electrons","Cu (cables), Al, Fe, Li"]];
      cards.forEach((c,k)=>{const al=seg(t,k*.25,k*.25+.4),x=24+k*312,y=24;ctx.save();ctx.globalAlpha=al;ctx.fillStyle=C.surface;ctx.strokeStyle=c[1];ctx.lineWidth=3;RR(x,y+(1-al)*20,288,392,14);ctx.fill();ctx.stroke();ctx.restore();
        const yy=y+(1-al)*20;T(c[0],x+144,yy+34,{s:24,w:800,f:DFONT,c:c[1],al});
        let z=yy+70;[["Entre",c[2]],["Electrons",c[3]],["Forma",c[4]],["Exemples",c[5]]].forEach(([h,v])=>{T(h.toUpperCase(),x+18,z,{s:13,w:700,c:C.muted,a:"left",al});z=WR(v,x+18,z+14,256,24,{s:18,al})+10;});});}}
]};
