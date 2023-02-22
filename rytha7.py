# a=[[1,3],[0],[5,7],[9,11],[13,15,17]]
# i=0
# max=0
# min=10
# while i<len(a):
#     b=a[i]
#     c=len(b)
#     if c>max:
#         max=c
#         d=a[i]
#     elif c<min:
#         min=c
#         e=a[i]
#     i=i+1
# print(min,e)
# print(max,d)




# a=[12,67,98,34]
# i=0
# rem=0
# b=[]
# sum=0
# while i<len(a):
#     j=0
#     while j<=i:
#         x=a[i]%10
#         rem=rem+x
#         sum=sum+rem
#         y=a[j]%10
#         b.append(sum)
#     i+=1
#     print(b)




a=int(input("enter the number"))
i=a
while i>=10:
   sum=0
   while i>0:
    b=i%10
    sum=sum+b**2
    i=i//10
    while sum>a:
     c=i%10
     sum=sum+c**2
     i=i//10
i=sum
if sum==1:
    print("happy number")
else:
    print("no")        

