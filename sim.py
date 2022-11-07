import re
i=input
r=re.compile(r"[a-z0-9\s]+|<+|\[+|\]+")
for _ in range(int(i())):
 s="";n=0
 for c in r.findall(i()):
  if']'==c[0]:n=len(s)
  elif'['==c[0]:n=0
  elif'<'==c[0]:
   if n>0:s=s[:max(0,n-len(c))]+s[n:];n=max(0,n-len(c))
  else:s=s[:n]+c+s[n:];n+=len(c)
 print(s)