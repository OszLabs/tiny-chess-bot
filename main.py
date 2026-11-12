import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
N=[-33,-31,-18,-14,14,18,31,33]
D=[-17,-15,15,17,-16,-1,1,16]
C=[0]
X=StopIteration
Y=["KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKK","ACEECGKLELMNEKNOELNOEKMNCGKKACEE"]
W=[[(ord(Y[t][28-(q>>4)*4+int("01233210"[q&7])])-75)*5 if not q&136 else 0 for q in range(128)]for t in range(2)]
def gv(z,q):return W[abs(z)-1][q^112*(z<0)]*z//abs(z)if abs(z)<3 else 0
def p(a,b):return json.load(u.urlopen(u.Request(E+a,json.dumps(b).encode())))
def at(b,s,w):
 for d in N+D:
  q=s+d
  if not q&136 and b[q]==(2+4*(d in D))*(2*w-1):return 1
 for d in D:
  q=s+d;g=abs(d)in(15,17)
  while not q&136:
   z=b[q]
   if z:
    if(z>0)==w and(abs(z)in((3,5)if g else(4,5))or(abs(z)==1 and q==s+d and g and(d<0)==w)):return 1
    break
   q+=d
 return 0
def gn(b,w,c,e):
 m=[];ks=0
 for f in range(128):
  if f&136:continue
  z=b[f]
  if not z or(z>0)!=w:continue
  t=abs(z);d=16*(2*w-1)
  if t==6:ks=f
  if t==1:
   q=f+d
   if not q&136 and not b[q]:
    m.append((f,q,5 if(q>>4)==7*w else 0))
    if(f>>4)==6-5*w and not b[f+2*d]:m.append((f,f+2*d,0))
   for q in(f+d-1,f+d+1):
    if q&136:continue
    if b[q] and(b[q]>0)!=w:m.append((f,q,5 if(q>>4)==7*w else 0))
    elif q==e:m.append((f,q,0))
  elif t==6:
   k=4+112*(1-w)
   for j in(0,1):
    to=k+2-4*j;rf=k+3-7*j;rt=k+1-2*j;bt=(4-3*w)<<j
    if c&bt and not b[rt]and not b[to]and b[rf]==4*(2*w-1)and not any(at(b,sq,not w)for sq in(k,rt,to))and(j==0 or not b[k-3]):m.append((k,to,0))
   for s in D:
    q=f+s
    if not q&136 and(not b[q]or(b[q]>0)!=w):m.append((f,q,0))
  else:
   O=[N,D[:4],D[4:],D][t-2]
   for s in O:
    q=f+s
    while not q&136:
     if b[q]:
      if(b[q]>0)!=w:m.append((f,q,0))
      break
     m.append((f,q,0))
     if t==2:break
     q+=s
 o=[]
 for mv in m:
  if abs(b[mv[1]])==6:continue
  nb,nc,ne,ns=mk(b,mv,w,c,e,None)
  nk=mv[1] if abs(b[mv[0]])==6 else ks
  if not at(nb,nk,not w):o.append(mv)
 return o
def mk(b,mv,w,c,e,s):
 f,t,pr=mv;n=b[:];z=n[f];n[f]=0
 if s is not None:s-=gv(z,f)
 cp=n[t]
 if abs(z)==1 and t==e and not cp:
  r=t-16*(2*w-1)
  if s is not None:s-=gv(n[r],r)
  n[r]=0
 elif cp and s is not None:s-=gv(cp,t)
 if abs(z)==6 and abs(t-f)==2:
  rf=t+1 if t>f else t-2;r=n[rf]
  if s is not None:s-=gv(r,rf)
  n[rf]=0;rt=(f+t)//2;n[rt]=r
  if s is not None:s+=gv(r,rt)
 n[t]=pr*(2*w-1)if pr else z
 if s is not None:s+=gv(n[t],t)
 if abs(z)==6:c&=~(3+9*(1-w))
 for j,bt in zip((0,7,112,119),(2,1,8,4)):
  if f==j or t==j:c&=~bt
 return n,c,(f+t)//2 if abs(z)==1 and abs(t-f)==32 else-1,s
def ps(fen):
 b=[0]*128;x=fen.split();c=0;s=0;q=112
 for ch in x[0]:
  if ch=="/":q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   z="pnbrqkPNBRQK".index(ch);z=-(z%6+1)if z<6 else z%6+1;b[q]=z;s+=gv(z,q);q+=1
 for ch in x[2]:c|={"K":1,"Q":2,"k":4,"q":8}.get(ch,0)
 e=(int(x[3][1])-1)*16+ord(x[3][0])-97 if x[3]!="-"else-1
 return b,x[1]=="w",c,e,s
def om(b,ms):return sorted(ms,key=lambda m:-abs(b[m[1]]))
def sr(b,w,c,e,s,dep,a,be):
 C[0]+=1
 if C[0]>45e3:raise X
 if dep<1:
  ck=at(b,b.index(6*(2*w-1)),not w);st=s*(2*w-1)
  if not ck:
   if st>=be:return be
   a=max(a,st)
  ms=gn(b,w,c,e)
  if not ck:ms=[mv for mv in ms if b[mv[1]]or mv[2]]
  for mv in om(b,ms):
   nb,nc,ne,ns=mk(b,mv,w,c,e,s)
   sc=-sr(nb,not w,nc,ne,ns,-1,-be,-a)
   if sc>=be:return be
   a=max(a,sc)
  return a
 ms=om(b,gn(b,w,c,e))
 if not ms:return-100000 if at(b,b.index(6*(2*w-1)),not w)else 0
 for mv in ms:
  nb,nc,ne,ns=mk(b,mv,w,c,e,s)
  sc=-sr(nb,not w,nc,ne,ns,dep-1,-be,-a)
  a=max(a,sc)
  if a>=be:break
 return a
def ch(fen,lg):
 b,w,c,e,s=ps(fen);C[0]=0;ms=gn(b,w,c,e);bt=ms[0]
 for dep in range(1,8):
  try:
   ba=-1e6;cu=None
   for mv in[bt]+[m for m in ms if m!=bt]:
    nb,nc,ne,ns=mk(b,mv,w,c,e,s)
    sc=-sr(nb,not w,nc,ne,ns,dep-1,-1e6,-ba)
    if sc>ba:ba=sc;cu=mv
   if cu:bt=cu
  except:break
 mv="".join(chr(x%8+97)+str(x//16+1)for x in bt[:2])
 if bt[2]:mv+="q"
 return mv if mv in lg else lg[0]
while 1:
 g=p("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=p("/move",{"game":g["game"],"move":ch(g["fen"],g["legal_moves"])})
