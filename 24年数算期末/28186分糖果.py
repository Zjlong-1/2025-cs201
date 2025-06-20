from collections import deque
n,m=map(int,input().split())
l=list(map(int,input().split()))
q=deque([(i+1,l[i]) for i in range(n)])
cnt=n
while cnt>1:
    id,x=q.popleft()
    if m<x:
        q.append((id,x-m))
    else:
        cnt-=1
print(q[0][0])
