a=[2,3,5,9]
i=0
max1=0
max2=0
while i<len(a):
    if a[i]>max1:
        max1=a[i]
    i=i+1
j=0
while j<len(a):
    if a[j]>max2 and a[j]!=max1:
        max2=a[j]
    j=j+1
print(max2)                

# a=[1,5]
# b=[]
# c=a[0]
# while c<=a[-1]:
#     b.append(c)
#     c=c+1
# print(b)





