import heapq
n,m,s,t=map(int,input().split())
di=[float('inf')]*n
l=[[] for _ in range(n)]
for _ in range(m):
    u,v,w=map(int,input().split())
    l[u].append((v,w))
    l[v].append((u,w))
di[s]=0
visit=[False]*n
heap=[(0,s)]
while heap:
    d,u=heapq.heappop(heap)
    if visit[u]:
        continue
    visit[u]=True
    for v,w in l[u]:
        if not visit[v] and d+w<di[v]:
            di[v]=d+w
            heapq.heappush(heap,(di[v],v))
print(di[t] if di[t]!=float('inf') else -1)