from collections import deque
n,k=map(int,input().split())
q=deque()
for i in range(1,n+1):
    q.append(i)
cnt=0
ans=[]
while q:
    t=q.popleft()
    cnt+=1
    if cnt==k:
        ans.append(t)
        cnt=0
        continue
    q.append(t)
for i in range(n-1):
    print(ans[i],end=' ')