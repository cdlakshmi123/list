a=[(123456789)]
b=str(a)
i=1
while i<len(b):
    c=int(b[i]+b[i+1]+b[i+2])
    d=int(b[i+3]+b[i+4]+b[i+5])
    e=int(b[i+6]+b[i+7]+b[i+8])

    if c>=100 and c<=999:
        if d>=100 and d>=999:
            if e>=1000 and e<=9999:
                print("(",c,")",d,"-",e)
                break


    i=i+1
                