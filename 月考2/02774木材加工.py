n,k=map(int,input().split())
l=[int(input()) for _ in range(n)]
right=sum(l)//k
left=0
def can(x):
    cnt=0
    for i in l:
        cnt+=i//x
    return cnt>=k
mid=0
if sum(l)<k:
    print(0)
else:
    while left < right:
        mid = (left + right + 1) // 2
        if can(mid):
            left = mid
        else:
            right = mid - 1
    print(left)
