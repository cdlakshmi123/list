a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
i=0
while i<len(a):
    if a[i]=="f":
        b=i
    if a[i]=="c":
        r=i
    if a[i]=="k":
        e=i
    if a[i]=="w":
        v=i
    i=i+1
print("Last occurance of f",b)
print("last occurance of c",r)
print("last occurance of k",e)
print("last occurance of w",v)
