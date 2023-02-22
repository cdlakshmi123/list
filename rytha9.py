a=[4,6,4,3,3,4,3,4,3]
i=0
c=[]
e=[]
while i<len(a):
    d=a.count(a[i])
    if d>=3:
        c.append(a[i])
        if a[i] not in e:
            e.append(a[i])
    i=i+1
print(e)