n=input("enter the no whose sum of digits to be calculated")
n=str(n)
lis=[]
length=len(n)
while length:
    lis.append(n[0])
    n=n[1:]
    length=length-1
newlis=list(map(int,lis))
print("sum of digits is ",sum(newlis))
