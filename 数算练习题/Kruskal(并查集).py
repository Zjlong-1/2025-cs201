#给出一个二位表，表示每两个点之间的距离，找出最小生成树
def solve(dist):
    n=len(dist)
    s=[i for i in range(n)]
    size=[1]*n
    def f(x):
        if f(x)!=s[x]:
            s[x]=f(s[x])
        return s[x]
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            edges.append((dist[i][j],i,j))
    edges.sort()
    ans=0
    for lens,x,y in edges:
        x1,y1=f(x),f(y)
        if x1==y1:
            continue
        ans+=lens
        size[x1]+=size[y1]
        s[y1]=x1
        if size[x1]==n:
            break
    return ans
#使用堆优化：prim算法
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0
        count = 0

        while count < n:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            in_mst[u] = True
            total_cost += cost
            count += 1
            for v in range(n):
                if not in_mst[v]:
                    new_dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if new_dist < min_dist[v]:
                        min_dist[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))
        return total_cost

