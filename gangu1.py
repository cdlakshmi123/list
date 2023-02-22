a=[[10,1,10,7],[4,3,7,1,0],[17,1,4,3,9,7]]
# i=0
# d=[]
# max=0
# while i<len(a):
#     b=a[i]
#     v=len(b)
#     d.append(b[-1])
#     if v>=max:
#         max=v
#         b=max,b
#     i=i+1
# print(d)
# print(b)
i=0
max=0
while i<len(a):
    b=a[i]
    v=len(b)
    d=[]
    if v>max:
        max=v
        d.append(a[i])
    i=i+1
print(v,d)