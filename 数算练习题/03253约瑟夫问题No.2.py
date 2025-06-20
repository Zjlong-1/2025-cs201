from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    ans=[]
    q=deque()
    for i in range(p,n+1):
        q.append(i)
    for i in range(1,p):
        q.append(i)
    while q:
        for _ in range(m-1):
            q.append(q.popleft())
        ans.append(q.popleft())
    print(','.join(map(str,ans)))
