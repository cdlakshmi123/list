l=[[1,3,12,5],[2,5],[10,9,7,6,5,17]]
i=0
max=len(l[0])
b=[]
r=[]
while i<len(l):
    g=l[i]
    j=0
    sum=0
    c=0
    while j<len(g):
        sum=sum+g[j]
        c=c+1
        j=j+1
    b.append(sum)
    if c>max:
        max=c
        v=[max,l[i]]
        # r.append(v)
    i=i+1
print(b)
print(v)

   