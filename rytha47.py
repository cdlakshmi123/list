a=['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

i=0
c=[]
while i<len(a):
    b=a[i]
    j=0
    while j<len(b):
        c.append (a[i][j])
        j=j+1
    i=i+1
print(c)
        