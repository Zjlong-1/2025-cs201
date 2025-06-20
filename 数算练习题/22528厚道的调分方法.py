from math import ceil
l=list(map(float,input().split()))
def can(b):
    a=b/(10**9)
    l1=[a*x+1.1**(a*x) for x in l]
    l1.sort(reverse=True)
    n=len(l1)
    return l1[ceil(n*0.6)-1]>=85
left=0
right=10**9
while left<right:
    mid=(left+right)//2
    if can(mid):
        right=mid
    else:
        left=mid+1
print(left)