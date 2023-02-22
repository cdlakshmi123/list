a=[1,2,2,5,8,4,4,8]
c=0
i=0
d=[]
while i<len(a):
    b=a[i]
    if b not in d:
        d.append(b)
        c=c+1
    i=i+1
    
# print(d)
print(c)


