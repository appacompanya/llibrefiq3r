import sys
s=open('template.html',encoding='utf-8').read()
if '.aval{' not in s:
    css=open('aval.css',encoding='utf-8').read()
    s=s.replace('@media (max-width:620px){', css + '@media (max-width:620px){\n  .avgrid{grid-template-columns:1fr}\n  .stulist{position:static}',1)
    old='''    ${MODE==="profe" ? `<h3 class="sec">Material del professorat</h3><div class="teacher">${teach}</div>` : ""}</div>`;'''
    new='''    ${MODE==="profe" ? `<h3 class="sec">Material del professorat</h3><div class="teacher">${teach}</div><section class="aval" id="aval"></section>` : ""}</div>`;
  if (MODE==="profe") { AV.sda = s.n; renderAval(); }'''
    assert old in s; s=s.replace(old,new)
    js=open('aval.js',encoding='utf-8').read()
    assert 'select(current);\n</script>' in s
    s=s.replace('select(current);\n</script>', js + '\nselect(current);\nif (MODE==="profe") initStore();\n</script>')
    open('template.html','w',encoding='utf-8').write(s)
import os, json
AUTHOR="Macià Esteve Pallarès Pallarès"
def covers():
    c={}
    for key in ["portada","portada-profe"]+[f"sda{n}" for n in range(1,7)]:
        base="portada" if key.startswith("portada") else "coberta"
        name=key if key.startswith("portada") else f"coberta-{key}"
        for ext in ("webp","jpg","png"):
            if os.path.exists(f"img/{name}.{ext}"): c[key]=f"img/{name}.{ext}"; break
    return c
def build(mode,out,title,eyebrow,h1,lead):
    src=s.replace('__AUTHOR__',AUTHOR).replace('__COVERS__',json.dumps(covers()))
    if mode=='alumne':
        a=src.index('/* ===== Avaluació'); b=src.index('\nroute();', a)
        src=src[:a]+src[b:]
        src=src.replace('\nif (MODE==="profe") initStore();','')
    t=src.replace('__MODE__',mode).replace('__TITLE__',title).replace('__EYEBROW__',eyebrow).replace('__H1__',h1).replace('__LEAD__',lead)
    open(out,'w',encoding='utf-8').write(t)
build('alumne','index.html',"Física i química 3r ESO","3r d'ESO","Física i química per entendre el món",
      "Sis reptes per entendre la física i la química del dia a dia. Aquí tens, sessió a sessió, què farem, els fulls que necessites i les simulacions.")
build('profe','profe.html',"Zona del professorat FQ","Física i química · 3r d'ESO · Professorat","Zona del professorat",
      "El llibre de l'alumnat amb la prova, els solucionaris, les rúbriques, els documents de programació i l'avaluació de cada alumne per criteris. No la comparteixis amb l'alumnat.")
print('built')
