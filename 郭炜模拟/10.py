#题目自相矛盾，就是不能选0
import heapq
a,n=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if l[i][j]>a:
            l[i][j]=a
        if l[i][j]==0:
            l[i][j]=a
def f():
    visited = [False] * n
    min_edge = [(a,0)]
    total_cost =0
    while min_edge:
        cost, u = heapq.heappop(min_edge)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        for v in range(n):
            if not visited[v] :
                heapq.heappush(min_edge, (l[u][v], v))
    return total_cost
print(f())