# a=[[1, 2], [2, 4]]
# i=0
# c=[]
# while i<len(a):
#     b=a[i]
#     j=0
#     while j<len(b):
#         j=j+1
#     i=i+1
# print("(",i,j,")")


a=[3,5,8,3,6,5]
c=[]
i=0
while i<len(a):
    d=a.count(a[i])
    if d>1:
        c.append(a[i])
    i=i+1
print(c)

