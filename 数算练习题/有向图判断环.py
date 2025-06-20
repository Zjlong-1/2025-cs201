#初始时，我们把所有入度 0 的顶点入队并删去它们及其出边。
#删掉这些入度 0 的顶点后，剩余子图仍然是 DAG（去掉节点和出边，不会产生新环）。
#因为子图也是 DAG，所以它又有至少一个入度 0 的顶点，可继续删。
from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
indeg=[0]*n
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indeg[v]+=1
q=deque([u for u in range(n) if  indeg[u]==0])
cnt=0
while q:
    u=q.popleft()
    cnt+=1
    for v in graph[u]:
        indeg[v]-=1
        if indeg[v]==0:
            q.append(v)
if cnt!=n:
    print('Yes')
else:
    print('No')