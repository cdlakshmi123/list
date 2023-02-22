a=[1,7,3,9,5,15,7,8,9,20]
i=0
b=[]
while i<len(a)-1:
    n=a[i+1]-a[i]
    b.append(n)
    i=i+1
print(b)

