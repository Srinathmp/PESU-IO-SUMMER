n=input("enter the arrray").split(',')
n=list(map(int,n))
k=int(input("enter the key to be found"))
low=0
high=len(n)
import math
def compute(x,y):
    if x==y:
        return 0
    elif x>y:
        return 1
    else :
        return -1

while low<=high:
    mid=math.floor((low+high)/2)
    if compute(k,n[mid])==0:
        print("key is found at position ",mid)
        break
    elif compute(k,n[mid])==1:
        low=mid+1
    else:
        high=mid-1

