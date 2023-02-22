a=[6,1,3,5,6,3,1]
i=0
c=[]
p=1
while i<len(a):
    b=a[i]
    if b not in c:
        c.append(b)
        p=p*b
    i=i+1
print(p)

    