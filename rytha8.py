a=[1,2,3,1,2,2]
i=0
d=[]
while i<len(a):
    b=a[i]
    if b not in d:
        d.append(b)
    i=i+1
print(d)

    


