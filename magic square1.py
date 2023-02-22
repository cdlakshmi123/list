a=[
[8 ,2, 3],
[6, 3 ,5],
[5 ,7, 5]]
i=0
while i<len(a):
    row=0
    col=0
    j=0
    while j<len(a):
        row=row+a[i][j]
        col=col+a[i][j]
        d=0
        while d<len(a):
            d1=0
            d2=0
            c=0
            while c<len(a):
                d1=d1+d+c
                d2=d2+d+c
                d1=d2
                c+=1
            d+=1
        j+=1
    i+=1
print(row)
print(col)
print(d1)
if row==col==d1:
    print("magic square")
else:
    print("no")




















# a="aaabbbccaaeefgb"
# i=0
# c=[]
# while i<len(a):
#     b=a[i]
#     if b not in c:
#         c.append(b)
#     i=i+1
# print(c)
