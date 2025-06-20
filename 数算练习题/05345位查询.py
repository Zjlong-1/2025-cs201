n,m=map(int,input().split())
l=list(map(int,input().split()))
def solve(l,x):
    cnt=0
    for i in l:
        if i&1<<x!=0:
            cnt+=1
    return cnt
for _ in range(m):
    a,b=input().split()
    b=int(b)
    if a=='C':
        for i in range(n):
            l[i]=(l[i]+b)%65536
    else:
        print(solve(l,b))
