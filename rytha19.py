a=[1234, 122, 1984, 19372, 100]
i=0
j=True
while i<len(a):
    b=str(a[i])
    if b[0]!=1:
        j=False
    i=i+1
print(j)
