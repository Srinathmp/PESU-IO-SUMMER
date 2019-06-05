r=input("enter string")
l=0
for i in range(len(r)):
    if(r[i].isdigit()):
        g+=1

if(g==len(r)):
    print("string is numeric")
else:
    print("the string is not numeric")
