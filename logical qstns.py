a=["gangothri","madhili"]
# i=0
# c=""
# while i<len(a):
#         v=a[i][0].upper()
#         c=c+v+"."
#         i=i+1
# print(c[0:-1])


# i=0
# while i<len(a):
#     print(a[i][i].capitalize(),".",a[i+1][i].capitalize())
#     break

i=0
string=""
while i<len(a):
    b=a[i][0].upper()
    string=string+b
    i=i+1
c=".".join(string)
print(c)