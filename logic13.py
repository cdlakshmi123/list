# a="this is string"
# i=0
# while i<len(a):
#     b=a[i]
#     if b!=" ":

#       i=i+1
# print(b)



# a=[4,6,4,3,3,4,3,4,3,8]
# i=0
# c=[]
# d=[]
# while i<len(a):
#   b=a.count(a[i])
#   if b>=3:
#     c.append(b)
#     if a[i]not in d:
#       d.append(a[i])
#   i=i+1
# print(d)

a=[1,2,3]
for i in range (3):
  for j in range (3):
    for k in range (3):
      if i!=j and j!=k and k!=i:
        print(a[i],a[j],a[k])
        