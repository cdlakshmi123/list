a=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
c=" "
while i<len(a):
    j=0
    while j<len(a[i]):
        b=a[i][j]
        c=c+a[i][j]
        j=j+1
    i=i+1
print(c)