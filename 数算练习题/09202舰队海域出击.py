t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l = [[]  for _ in range(n + 1)]
    for i in range(m):
        x,y=map(int,input().split())
        l[x].append(y)
    def dfs(a,visit):
        if visit[a]==1:
            return True
        if visit[a]==2:
            return False
        visit[a]=1
        for k in l[a]:
            if dfs(k,visit):
                return True
        visit[a]=2
        return False
    visit=[0]*(n+1)#1表示在递归的过程中，2表示dfs完了之后没有，0即为没处理
    flag = False
    for i in range(1,n+1):
        if visit[i]==0:
            if dfs(i,visit):
                flag=True
                break
    print('Yes'if flag else 'No')
#另外一种方法，用优先队列实现，入度：
from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l = [[]  for _ in range(n + 1)]
    ind=[0]*(n+1)
    for i in range(m):
        x,y=map(int,input().split())
        l[x].append(y)
        ind[y]+=1
    q=deque([i for i in range(1,n+1) if ind[i]==0])
    s=set()
    while q:
        k=q.popleft()
        s.add(k)
        for i in l[k]:
            if i not in s:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
    if len(s)==n:
        print('No')
    else:
        print('Yes')