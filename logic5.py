
a=[[56,9],[34,3],[3,78],[98,100]]
i=0
c=[]
while i<len(a):
    sum=0
    b=a[i]
    j=0
    while j<len(b):
        sum=sum+b[j]
        j=j+1
    c.append(sum)    
    i=i+1
print(c)

# a=[1,2,3,4,5,6]
# i=-1
# c=[]
# while i>=-len(a):
#     c.append(a[i])
#     i=i-1
# print(c)
