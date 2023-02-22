a=[1,2,3,4,5,6,7]
i=0
c=[]
while i<len(a)-1:
    n=a[i],a[i+1]
    c.append (list(n))

    i=i+1
print(c)