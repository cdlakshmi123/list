# a=[78,76,94,86,88]
# b=[91,71,98,65,76]
# c=[95,45,78,52,49]
# t=0
# i=0
# while i<len(a):
#     t=t+a[i]+b[i]+c[i]
#     i=i+1
# print(t)

# a=["pynative",[4,8,12,16]]
# print(a[0][1])
# print(a[1][3])

a=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# ce=0
# co=0
# while i<len(a):
#     v=a[i]
#     if a[i]%2==0:
#         ce=ce+1
#     else:
#         co=co+1
#     i=i+1
# print("even",ce)
# print("odd",co)
# i=0
# odd=0
# even=0
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         odd=odd+a[i]
#     else:
#         even=even+a[i]
#     i=i+1
# print(odd)
# print(even)    

a=[1,2,3],[2,3,4]
i=0
c=[]
while i<len(a):
    j=0
    b=a[i]
    while j<len(b):
        c.append(b+a[j])
        i=i+1