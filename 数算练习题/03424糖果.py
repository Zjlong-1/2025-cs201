#自己的判断还是对的，实际上就是找最短路径（在相邻的边取max）
import heapq
n,m=map(int,input().split())
l=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    l[a].append((b,c))
def d(start,end):
    dist=[float('inf')]*(1+n)
    heap=[(0,start)]
    dist[start]=0
    while heap:
        w,u=heapq.heappop(heap)
        if dist[u]<w:
            continue
        for v,len1 in l[u]:
            if dist[v]>len1+w:
                dist[v]=len1+w
                heapq.heappush(heap,(len1+w,v))
    return dist[end]
print(d(1,n))
