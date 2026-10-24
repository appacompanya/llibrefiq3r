// Pila de combustible d'hidrogen (membrana d'intercanvi de protons)
const XA0=318,XA1=352,XM1=608,XC1=642,Y0=140,Y1=430,WY=66,BX0=480;
const EPATH=(y)=>[[335,y],[335,WY],[625,WY],[625,y]];
function along(pts,f){let L=0;const seg2=[];for(let k=1;k<pts.length;k++){const d=Math.hypot(pts[k][0]-pts[k-1][0],pts[k][1]-pts[k-1][1]);seg2.push(d);L+=d;}
  let r=f*L;for(let k=0;k<seg2.length;k++){if(r<=seg2[k]){const u=r/seg2[k];return [lerp(pts[k][0],pts[k+1][0],u),lerp(pts[k][1],pts[k+1][1],u)];}r-=seg2[k];}return pts[pts.length-1];}
function H2(x,y,al=1,sep=0){BALL(x-9-sep,y,11,"#ffffff","#c9d0d7",{l:"H",lc:"#1f2328",al});BALL(x+9+sep,y,11,"#ffffff","#c9d0d7",{l:"H",lc:"#1f2328",al});}
function O2(x,y,al=1){BALL(x-13,y,16,"#ee5a4e","#a8251b",{l:"O",al});BALL(x+13,y,16,"#ee5a4e","#a8251b",{l:"O",al});}
function H2O(x,y,al=1,sc=1){BALL(x-15*sc,y+9*sc,11*sc,"#ffffff","#c9d0d7",{l:"H",lc:"#1f2328",al});BALL(x+15*sc,y+9*sc,11*sc,"#ffffff","#c9d0d7",{l:"H",lc:"#1f2328",al});BALL(x,y-4*sc,16*sc,"#ee5a4e","#a8251b",{l:"O",al});}
function Hp(x,y,al=1){BALL(x,y,10.5,"#b44fd6","#6a1f86",{l:"+",ls:1.3,al});}
function El(x,y,al=1){BALL(x,y,7.5,"#4a8ad8","#1d4f91",{l:"−",ls:1.3,al});}
function cell(glow,hl){ctx.save();
  ctx.fillStyle="rgba(120,170,230,.16)";ctx.fillRect(28,Y0+10,XA0-28,Y1-Y0-20);
  ctx.fillStyle="rgba(230,120,110,.14)";ctx.fillRect(XC1,Y0+10,930-XC1,Y1-Y0-20);
  ctx.fillStyle=hl==="m"?"rgba(240,200,90,.55)":"rgba(240,200,90,.32)";ctx.fillRect(XA1,Y0,XM1-XA1,Y1-Y0);
  ctx.fillStyle="#5d636c";ctx.fillRect(XA0,Y0,XA1-XA0,Y1-Y0);ctx.fillRect(XM1,Y0,XC1-XM1,Y1-Y0);
  if(hl==="a"||hl==="c"){ctx.strokeStyle=C.acc;ctx.lineWidth=4;const x=hl==="a"?XA0:XM1;ctx.strokeRect(x-4,Y0-4,XA1-XA0+8,Y1-Y0+8);}
  // aigua que surt
  ctx.fillStyle="rgba(230,120,110,.14)";ctx.fillRect(760,Y1-10,52,50);
  // circuit exterior
  ctx.strokeStyle=C.fg;ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(335,Y0);ctx.lineTo(335,WY);ctx.lineTo(BX0-20,WY);ctx.moveTo(BX0+20,WY);ctx.lineTo(625,WY);ctx.lineTo(625,Y0);ctx.stroke();
  if(glow>0){const g=ctx.createRadialGradient(BX0,WY,4,BX0,WY,70);g.addColorStop(0,`rgba(255,214,90,${.85*glow})`);g.addColorStop(1,"rgba(255,214,90,0)");ctx.fillStyle=g;ctx.beginPath();ctx.arc(BX0,WY,70,0,7);ctx.fill();}
  ctx.fillStyle=glow>0?`rgba(255,${200+40*glow|0},90,1)`:C.surface;ctx.strokeStyle=C.fg;ctx.lineWidth=2.5;ctx.beginPath();ctx.arc(BX0,WY,20,0,7);ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(BX0-12,WY-12);ctx.lineTo(BX0+12,WY+12);ctx.moveTo(BX0+12,WY-12);ctx.lineTo(BX0-12,WY+12);ctx.stroke();ctx.restore();
  T("Ànode (−)",XA0+17,Y1+20,{s:15,w:700});T("Càtode (+)",XC1-17,Y1+20,{s:15,w:700});
  T("Membrana",480,Y0+18,{s:15,w:700});T("només hi passen ions H⁺",480,Y0+38,{s:13,w:600,c:C.muted});
  T("Entra hidrogen (H₂)",170,Y0+30,{s:15,w:700,c:C.cold});T("Entra aire (O₂)",790,Y0+30,{s:15,w:700,c:C.hot});
  T("Surt aigua",870,Y1+18,{s:15,w:700,c:C.hot});T("Circuit exterior (al bus, el motor)",BX0,WY-38,{s:14,w:700,c:C.muted});}
// un cicle: 2 H₂ + O₂ → 2 H₂O; ph de 0 a 1; dy desplaça el carril
function cycle(ph,dy,al=1){const ys=[205+dy,320+dy];let wire=0;
  // H₂ arriba a l'ànode
  if(ph<.36){const p=ease(seg(ph,0,.25)),s=seg(ph,.25,.36);for(const y of ys){if(s<.5)H2(lerp(40,XA0-16,p),y,al*(ph>0?1:0),s*16);}}
  if(ph>=.25&&ph<.36){const s=seg(ph,.25,.36);if(s>=.5)for(const y of ys){Hp(XA0-8,y-12,al);Hp(XA0-8,y+12,al);El(XA0+8,y-12,al);El(XA0+8,y+12,al);}}
  // H⁺ travessen la membrana; e⁻ fan la volta pel circuit
  if(ph>=.36&&ph<.74){const p=ease(seg(ph,.36,.7));for(const y of ys)for(const d of [-12,12]){Hp(lerp(XA1+10,XM1-10,p),y+d,al);}
    ys.forEach((y,m)=>[-12,12].forEach((d,k)=>{const f=clamp(seg(ph,.36+.02*(2*m+k),.66+.02*(2*m+k)));const [x,yy]=along(EPATH(y+d),ease(f));El(x,yy,al);if(f>0&&f<1)wire=1;}));}
  // O₂ arriba al càtode
  if(ph>=.28&&ph<.76){const p=ease(seg(ph,.28,.7));O2(lerp(930,XC1+30,p),(ys[0]+ys[1])/2,al);}
  // es forma aigua i surt
  if(ph>=.72){const f=pop(seg(ph,.72,.8)),m=ease(seg(ph,.8,1));ys.forEach((y,k)=>{H2O(lerp(XC1+30,786,m),lerp(y,Y1+30,m),al*(1-seg(ph,.95,1)),f);});}
  return wire;}
let CY=0;
const SIM={W:960,H:510,steps:[
  {t:"Les parts de la pila",d:1000,eq:"",x:"<p>El bus d'hidrogen no crema l'hidrogen: el fa reaccionar dins una <b>pila de combustible</b>, que transforma energia química en <b>energia elèctrica</b>.</p><p>Té dos elèctrodes, l'<b>ànode</b> i el <b>càtode</b>, separats per una <b>membrana</b> que només deixa passar ions H⁺. Els elèctrodes estan units per un <b>circuit exterior</b>: aquí una bombeta, al bus el motor elèctric.</p>",
    draw(t){cell(0,"m");}},
  {t:"Entra l'hidrogen",d:2200,x:"<p>Per l'esquerra arriba <b>hidrogen gas (H₂)</b> del dipòsit fins a l'ànode.</p>",
    draw(t){cell(0);cycle(t*.25,0);}},
  {t:"A l'ànode: H₂ → 2 H⁺ + 2 e⁻",d:2200,hl:"a",x:"<p>A l'ànode, un catalitzador de platí separa cada molècula d'hidrogen en <b>2 ions H⁺</b> i <b>2 electrons</b>:</p><p><b>H₂ → 2 H⁺ + 2 e⁻</b></p><p>L'hidrogen perd electrons: és una <b>oxidació</b>.</p>",
    draw(t){cell(0,"a");cycle(lerp(.2,.35,t),0);}},
  {t:"Dos camins diferents",d:3800,x:"<p>Els ions H⁺ <b>travessen la membrana</b>. Els electrons no hi poden passar: han de fer la volta pel <b>circuit exterior</b>, i pel camí encenen la bombeta.</p><p>Aquest flux d'electrons és el <b>corrent elèctric</b> que mou el bus.</p>",
    draw(t){const ph=lerp(.35,.7,t);cell(ph>.38&&ph<.69?1:0,"m");cycle(ph,0);}},
  {t:"Al càtode es forma aigua",d:3600,hl:"c",x:"<p>Per la dreta arriba <b>oxigen (O₂)</b> de l'aire. Al càtode, l'oxigen s'uneix als ions H⁺ i als electrons i es forma <b>aigua</b>:</p><p><b>O₂ + 4 H⁺ + 4 e⁻ → 2 H₂O</b></p><p>L'oxigen guanya electrons: és una <b>reducció</b>.</p>",
    draw(t){cell(0,"c");cycle(lerp(.6,1,t),0);}},
  {t:"La pila funciona sense parar",loop:true,x:"<p>Mentre arribin hidrogen i oxigen, la pila funciona contínuament. Reacció global:</p><p><b>2 H₂ + O₂ → 2 H₂O</b> + energia elèctrica (i una mica de calor)</p><p>Pel tub d'escapament només surt <b>vapor d'aigua</b>.</p>",
    draw(t,sec){const ph=sec/5;const a=ph%1,b=(ph+.5)%1;cell(1,"");cycle(a,-22);cycle(b,22);
      T("2 H₂ + O₂ → 2 H₂O + energia elèctrica",400,486,{s:20,w:800,c:C.acc});}},
  {t:"I d'on surt l'hidrogen?",loop:true,x:"<p>Aquesta reacció és la <b>inversa de l'electròlisi</b> de l'aigua que vas fer al laboratori (2 H₂O → 2 H₂ + O₂), que gasta energia elèctrica.</p><p>L'hidrogen només és «<b>verd</b>» si l'electròlisi es fa amb electricitat renovable. Si s'obté del gas natural, en fabricar-lo s'emet CO₂.</p>",
    draw(t,sec){const ph=sec/5;cell(1,"");cycle(ph%1,-22);cycle((ph+.5)%1,22);
      T("Pila: 2 H₂ + O₂ → 2 H₂O  ·  Electròlisi: 2 H₂O → 2 H₂ + O₂",440,486,{s:17,w:700,c:C.muted});}}
],
panel0(s,i){const on=[null,null,"a","a","c","g","g"][i];const r=(k,lab,eq)=>`<div class="${on===k?"on":""}"><span>${lab}</span>${eq}</div>`;
  $("#extra").innerHTML='<div class="eqs">'+r("a","Ànode (oxidació)","H₂ → 2 H⁺ + 2 e⁻")+r("c","Càtode (reducció)","O₂ + 4 H⁺ + 4 e⁻ → 2 H₂O")+r("g","Reacció global","2 H₂ + O₂ → 2 H₂O")+"</div>";}
};
