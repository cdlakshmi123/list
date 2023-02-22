a="https://www.w3resource.com/python-exercises/list/"
b=['.com', '.edu', '.tv']
i=0
c=0
while i<len(b):
    v=b[i]
    if v in a:
        c=c+1
    i=i+1
if c>=1:
    print("True")
else:
    print("False")

