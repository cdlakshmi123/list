a=[1,3,9,6,5]
max=0
i=0
c=0
d=0
while i<len(a):
    b=a[i]
    if b>max:
        max=b
    elif b>c:
        c=b
    elif b>d:
        d=b
    i=i+1
print(max)
print(c)
print(d)
