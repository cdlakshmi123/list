a=[4,5,5,5,3,8]
a=[1,1,1,64,23,64,22,22,22]
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