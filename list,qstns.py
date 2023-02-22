# L=['a',['bb','cc'],'d',]
# L[1].append('xx')
# print(L)
# print(L)

# a=[3,4,5,20,5,25,1,3]
# print (a.count(5))

# a=[50,40,23,70,56,12,5,10,7]
# count=0
# while count<len(a):
#     count=count+1
# print(count)

# a=[50,40,23,70,56,12,5,10,7]
# c=0
# i=0
# while c<len(a):
#     if a[c]>=20 and a[c]<=40:
#         i=i+1
#     c=c+1
# print(i)


# n=int(input("enter the num"))
# total=0
# while n>0:
#     sum=n%10
#     total=sum+total
#     n=n//10
# print(total)

# a=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# c=0
# while i<len(a):
#     b=a[i]
#     if b>max:
#         max=b
#     i=i+1
# print(max)

# a=[50,40,23,70,56,12,5,10,7]
# max=0
# i=0
# c=0
# while i<len(a):
#     b=a[i]
#     if b>max:
#         max=b
#     elif b>c:
#         c=b
#     i=i+1
# print(c)

# a=["delhi","rajastan","punjab","kerala"]
# i=-1
# while i>=-len(a):
#     print(a[i])
#     i=i-1

# a=[-2,1,5,-8,10,60]
# max=0
# min=100
# i=0
# while i<len(a):
#     b=a[i]
#     if b>max:
#         max=b
#     elif b<min:
#         min=b
#     i=i+1
# print(max)
# print(min)

# a=[70,80,65,52,10,25,86,30,40]
# count=0
# i=0
# while count<len(a):
#     if a[count]>50:
#         i=i+1
#     count=count+1
# print(i)

# a=[1,2,3,4,5,6,7,8,9,10]
# even=0
# odd=0
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     i=i+1
# print(even)
# print(odd)

# list=[2,-7,5,-64,-14]
# count1=0
# count2=0
# i=0
# while i<len(list):
#     if list[i]>0:
#         count1=count1+1
#     else:
#         count2=count2+1
#     i+=1
# print("positive:",count1)
# print("negative:",count2)


# a=[2,3,4,5,6,7,8]
# print(a[0],a[1])
# print(a[1],a[2])
# print(a[2],a[4])
# print(a[3],a[6])
# print(a[4],a[5],a[2])
# print(a[5],a[3],a[0])
# print(a[6],a[0],a[1])

# age=int(input("enter the age"))
# if age>18 and age<=60:
#     print("person can vote")
# elif age>=0 and age<18:
#     print("cannot vote")
# else:
#     print("invalid age")

# a=[3,5,8,3,6,5]
# c=[]
# i=0
# while i<len(a):
#     d=a.count(a[i])
#     if d>1:
#       if c.count(a[i])==0:
#         c.append(a[i])
#     i=i+1
# print(c)

# a=[23,2.3,12,1.2,22]
# i=0
# c=[]
# s1=0
# s2=0
# while i<len(a):
#     s1=s1+a[i]
#     if type (a[i])==float:
#         v=int(a[i])
#     c.append(s1+v)
#     i=i+1
# print(c)


a=[1,2,3,4,5,6]
i=0
j=-1
c=[]
while i<len(a)-3:
    b=a[j],a[i]
    c.append(b)
    j=j-1
    i=i+1
print(c)






    



