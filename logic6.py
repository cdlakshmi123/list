a=["lakshmi"]
i=0
c=[]
b=[]
while i<len(a):
    v=a[i]
    j=0
    while j<len(v):
        if v[j] in ("a,e,i,o,u") or v[j] in ("A","E","I","O","U"):
            c.append (v[j])
        else:
            b.append (v[j])
        j=j+1
    i=i+1
print(c)
print(b)