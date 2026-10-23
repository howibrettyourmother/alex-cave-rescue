import os,re
D=os.path.dirname(os.path.abspath(__file__))
t=open(f'{D}/template.html').read().replace('/*GAME*/',open(f'{D}/game.js').read())
s=open('/workspace/kids-hubs/home.js').read().strip().replace('%OWN%','alex').replace('%POS%','left:0;top:50%;margin-top:-26px;width:calc(44px + env(safe-area-inset-left));height:52px;border-radius:0 18px 18px 0;padding-left:env(safe-area-inset-left)')
i=t.rfind('</body>');t=t[:i]+s+'\n'+t[i:]
open(f'{D}/../index.html','w').write(t);print(len(t))
