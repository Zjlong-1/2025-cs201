n,k=map(int,input().split())
l=[]
for _ in range(n):
    x=float(input())
    l.append(int(x*100))
def p(t):
    cnt=0
    for i in l:
        cnt+=i//t
    return cnt>=k
left=1
right=max(l)
if not p(left):
    print(f'{0.00:.2f}')
else:
    while left < right:
        mid = (left + right + 1) // 2
        if p(mid):
            left = mid
        else:
            right = mid - 1
    print(f'{left / 100:.2f}')