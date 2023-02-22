a=[9119]
i=0
b=[]
while i<len(a):
    n=a[i]
    j=0
    while j<n:
        r=n%10
        c=r*r
        n=n//10
        print(c,end="")
        j=j+1
    i=i+1