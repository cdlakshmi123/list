# a=[34.67, 12, -94.89, 'Python', 0, 'C#']
# i=0
# c=[]
# while i<len(a):
#     if type(a[i])!=float and type(a[i])!=str:
#         c.append (a[i])
#     i=i+1
# print(c)
a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
c=[]
while i<len(a):
    if type(a[i])==int:
        c.append (a[i])
    i=i+1
print(c)
