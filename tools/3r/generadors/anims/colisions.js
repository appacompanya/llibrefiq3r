// Teoria de col·lisions: partícules A i B en caixes; un xoc A–B és eficaç si té prou energia
const COLS={A:["#4a8ad8","#1d4f91"],B:["#f0a04a","#a85a10"],S:["#e08a2c","#8a4a0a"],P:["#3fbf75","#1d7a45"]};
function Box(x,y,w,h,o){Object.assign(this,{x,y,w,h,o,P:[],fx:[],n:{x:0,e:0,p:0},title:o.title||""});const rnd=mulberry(o.seed||1);this.rnd=rnd;
  const g=()=>{let u=0,v=0;while(!u)u=rnd();while(!v)v=rnd();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);};
  if(o.blocks)for(const [bx,by,nc] of o.blocks)for(let i=0;i<nc;i++)for(let j=0;j<nc;j++)this.P.push({x:x+bx+i*19,y:y+by+j*19,vx:0,vy:0,k:"S",r:9.5,fix:true});
  const add=(k,n)=>{for(let c=0;c<n;c++){let px,py,ok,tries=0;do{px=x+16+rnd()*(w-32);py=y+16+rnd()*(h-32);ok=this.P.every(q=>Math.hypot(q.x-px,q.y-py)>q.r+12);}while(!ok&&++tries<200);
    this.P.push({x:px,y:py,vx:g()*o.sig,vy:g()*o.sig,k,r:10});}};
  add("A",o.nA||0);add("B",o.nB||0);}
Box.prototype.step=function(dt,showReb){const P=this.P,o=this.o;
  for(const p of P){if(p.fix)continue;p.x+=p.vx*dt;p.y+=p.vy*dt;
    if(p.x<this.x+p.r){p.x=this.x+p.r;p.vx=Math.abs(p.vx);}if(p.x>this.x+this.w-p.r){p.x=this.x+this.w-p.r;p.vx=-Math.abs(p.vx);}
    if(p.y<this.y+p.r){p.y=this.y+p.r;p.vy=Math.abs(p.vy);}if(p.y>this.y+this.h-p.r){p.y=this.y+this.h-p.r;p.vy=-Math.abs(p.vy);}}
  for(let i=0;i<P.length;i++){const a=P[i];if(a.dead)continue;for(let j=i+1;j<P.length;j++){const b=P[j];if(b.dead||(a.fix&&b.fix))continue;if(a.k==="P"||b.k==="P")continue;if(a.k===b.k)continue; // dues partícules del mateix reactiu no reaccionen: aquí es travessen
    const dx=b.x-a.x,dy=b.y-a.y,d2=dx*dx+dy*dy,rr=a.r+b.r;if(d2>=rr*rr||d2===0)continue;const d=Math.sqrt(d2),nx=dx/d,ny=dy/d;
    const rvx=b.vx-a.vx,rvy=b.vy-a.vy,vn=rvx*nx+rvy*ny;if(vn>=0)continue;
    const ab=(a.k==="A"&&(b.k==="B"||b.k==="S"))||(b.k==="A"&&(a.k==="B"||a.k==="S"));
    const mx=a.x+nx*a.r,my=a.y+ny*a.r;
    if(ab){this.n.x++;const A=a.k==="A"?a:b,B=a.k==="A"?b:a;const en=B.fix?Math.hypot(A.vx,A.vy):Math.hypot(rvx,rvy);
      if(en>o.vth){this.n.e++;this.n.p++;B.dead=true;A.k="P";A.r=12;if(!B.fix){A.vx=(A.vx+B.vx)/2;A.vy=(A.vy+B.vy)/2;A.x=(A.x+B.x)/2;A.y=(A.y+B.y)/2;}else{const s=A===a?1:-1;const v=A.vx*nx*s+A.vy*ny*s;if(v>0){A.vx-=2*v*nx*s;A.vy-=2*v*ny*s;}}
        this.fx.push({x:mx,y:my,a:0,ok:true});continue;}
      if(showReb)this.fx.push({x:mx,y:my,a:0,ok:false});}
    if(a.fix||b.fix){const m=a.fix?b:a,s=a.fix?-1:1;const v=(m.vx*nx+m.vy*ny)*s;if(v>0){m.vx-=2*v*nx*s;m.vy-=2*v*ny*s;}const ov=rr-d;m.x-=nx*ov*s;m.y-=ny*ov*s;}
    else{const imp=-vn;a.vx-=imp*nx;a.vy-=imp*ny;b.vx+=imp*nx;b.vy+=imp*ny;const ov=(rr-d)/2;a.x-=nx*ov;a.y-=ny*ov;b.x+=nx*ov;b.y+=ny*ov;}}}
  // termòstat: la temperatura de la caixa es manté constant
  let e2=0,nm=0;for(const p of P)if(!p.fix&&!p.dead&&p.k!=="P"){e2+=p.vx*p.vx+p.vy*p.vy;nm++;}
  if(nm>1){const f=1+(Math.sqrt(2*o.sig*o.sig/(e2/nm))-1)*.02;for(const p of P)if(!p.fix&&p.k!=="P"){p.vx*=f;p.vy*=f;}}
  this.P=P.filter(p=>!p.dead);for(const f of this.fx)f.a+=dt;this.fx=this.fx.filter(f=>f.a<.7);};
Box.prototype.draw=function(){ctx.save();ctx.fillStyle=C.surface;ctx.strokeStyle=C.muted;ctx.lineWidth=2;RR(this.x-2,this.y-2,this.w+4,this.h+4,12);ctx.fill();ctx.stroke();ctx.restore();
  if(this.title)T(this.title,this.x+this.w/2,this.y-20,{s:17,w:700});
  for(const p of this.P){const c=COLS[p.k];BALL(p.x,p.y,p.r,c[0],c[1]);}
  for(const f of this.fx){const k=f.a/.7;ctx.save();ctx.globalAlpha=1-k;if(f.ok){ctx.fillStyle="#f5c242";ctx.strokeStyle="#a87a00";ctx.lineWidth=1.5;star(f.x,f.y,10+22*k);ctx.fill();ctx.stroke();}
    else{ctx.strokeStyle=C.muted;ctx.lineWidth=2.5;ctx.setLineDash([4,3]);ctx.beginPath();ctx.arc(f.x,f.y,10+14*k,0,7);ctx.stroke();ctx.setLineDash([]);ctx.font="700 12px "+FONT;ctx.fillStyle=C.muted;ctx.textAlign="center";ctx.fillText("rebot",f.x,f.y-30);}ctx.restore();}
  const lbl=`Producte format: ${this.n.p}`;T(lbl,this.x+this.w/2,this.y+this.h+22,{s:16,w:700,c:"#2e9d5b"});};
function star(x,y,r){ctx.beginPath();for(let k=0;k<10;k++){const a=-Math.PI/2+k*Math.PI/5,rr=k%2?r*.45:r;ctx.lineTo(x+rr*Math.cos(a),y+rr*Math.sin(a));}ctx.closePath();}
let BX=[];
function run(dt,reb){const sub=3;for(let s=0;s<sub;s++)for(const b of BX)b.step(dt/sub,reb);for(const b of BX)b.draw();}
const one=()=>[new Box(40,40,880,330,{seed:3,nA:14,nB:14,sig:90,vth:300})];
const SIM={W:960,H:430,steps:[
  {t:"Per reaccionar, cal xocar",loop:true,init(){BX=one();},x:"<p>Les partícules dels reactius es mouen sense parar. Perquè reaccionin, s'han de <b>trobar i xocar</b>.</p><p>Aquí hi ha dos reactius: partícules blaves (A) i taronges (B). Quan un xoc entre A i B funciona, es forma una partícula de <b>producte</b> (verda).</p>",
    draw(t,sec,dt){run(dt,false);}},
  {t:"No tots els xocs són eficaços",loop:true,init(){BX=one();},x:"<p>La majoria de xocs no fan res: les partícules <b>reboten</b> (cercle gris). Només reaccionen si xoquen amb prou energia per trencar enllaços: l'<b>energia d'activació</b>. També cal que xoquin amb l'orientació adequada.</p><p>Compara els xocs A–B totals amb els xocs eficaços (estrella groga). Dues partícules del mateix reactiu (A amb A, o B amb B) no poden reaccionar: en aquest model es travessen i no compten.</p>",
    draw(t,sec,dt){run(dt,true);}},
  {t:"Factor 1: la temperatura",loop:true,init(){BX=[new Box(30,50,430,320,{seed:5,nA:12,nB:12,sig:60,vth:280,title:"Freda"}),new Box(500,50,430,320,{seed:5,nA:12,nB:12,sig:125,vth:280,title:"Calenta"})];},
    x:"<p>A més temperatura, les partícules es mouen <b>més de pressa</b>: xoquen més sovint i, sobretot, amb <b>més energia</b>. Molts més xocs superen l'energia d'activació.</p><p>Per això els aliments es conserven millor a la nevera: les reaccions que els fan malbé van més a poc a poc.</p>",
    draw(t,sec,dt){run(dt,true);}},
  {t:"Factor 2: la concentració",loop:true,init(){BX=[new Box(30,50,430,320,{seed:8,nA:7,nB:7,sig:95,vth:280,title:"Diluïda"}),new Box(500,50,430,320,{seed:8,nA:24,nB:24,sig:95,vth:280,title:"Concentrada"})];},
    x:"<p>Amb més partícules en el mateix volum (<b>més concentració</b>), es troben més sovint: hi ha més xocs cada segon i, per tant, més xocs eficaços.</p><p>Per exemple, un tros de fusta encès crema molt més de pressa en oxigen pur que a l'aire, que només en té un 21 %.</p>",
    draw(t,sec,dt){run(dt,true);}},
  {t:"Factor 3: la superfície de contacte",loop:true,init(){const b1=[[168,112,6]],b2=[];for(const bx of [60,196,332])for(const by of [45,141,237])b2.push([bx,by,2]);
      BX=[new Box(30,50,430,320,{seed:11,nA:60,sig:70,vth:140,blocks:b1,title:"Un tros sencer"}),new Box(500,50,430,320,{seed:11,nA:60,sig:70,vth:140,blocks:b2,title:"El mateix, a trossets"})];},
    x:"<p>Un sòlid només reacciona per la <b>superfície</b>: les partícules de dins no poden xocar amb les de l'altre reactiu. Si el trossegem, amb la mateixa quantitat hi ha <b>molta més superfície</b> exposada.</p><p>Per això un comprimit triturat reacciona abans que un de sencer, i les encenalls de fusta cremen més de pressa que un tronc.</p>",
    draw(t,sec,dt){run(dt,true);}},
  {t:"Resum",d:1800,x:"<p>La velocitat d'una reacció augmenta si hi ha <b>més xocs</b> i <b>xocs amb més energia</b>.</p><p>També hi ha els <b>catalitzadors</b>, com el platí de la pila de combustible: fan que la reacció necessiti menys energia d'activació i no es gasten.</p>",
    draw(t){const it=[["Temperatura ↑","xocs més freqüents i amb més energia",C.hot],["Concentració ↑","més partícules → més xocs per segon",C.cold],["Superfície de contacte ↑","més partícules exposades als xocs","#c46f12"],["Catalitzador","cal menys energia d'activació",C.ok]];
      T("Què fa anar més de pressa una reacció?",480,40,{s:22,w:800,f:DFONT});
      it.forEach(([a,b,c],k)=>{const al=seg(t,k*.18,k*.18+.4),y=80+k*84+(1-al)*14;ctx.save();ctx.globalAlpha=al;ctx.fillStyle=C.surface;ctx.strokeStyle=c;ctx.lineWidth=3;RR(110,y,740,70,14);ctx.fill();ctx.stroke();ctx.restore();
        T(a,140,y+35,{s:21,w:800,c,a:"left",al});T(b,440,y+35,{s:18,w:600,a:"left",al});});}}
],
panel(s,t){if(!BX.length||!s.loop){$("#extra").innerHTML="";return;}const now=performance.now();if(this._l&&now-this._l<200)return;this._l=now;
  if(BX.length===1){$("#extra").innerHTML='<table class="cnt"><tr><th>Xocs A–B</th><th>Eficaços</th><th>% eficaços</th></tr>'+BX.map(b=>`<tr><td>${b.n.x}</td><td>${b.n.e}</td><td>${b.n.x?Math.round(100*b.n.e/b.n.x):0} %</td></tr>`).join("")+"</table>";return;}
  $("#extra").innerHTML=`<table class="cnt"><tr><th></th><th>Producte format</th><th>${BX[0].o.blocks?"Sòlid que queda":"Reactiu A que queda"}</th></tr>`+BX.map(b=>`<tr><td>${b.title}</td><td>${b.n.p}</td><td>${b.P.filter(p=>p.k===(b.o.blocks?"S":"A")).length}</td></tr>`).join("")+"</table>";}
};
