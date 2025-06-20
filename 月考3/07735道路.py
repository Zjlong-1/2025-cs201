#这里用最原始的Dijkstra会有非常严重的逻辑错误，就是会覆盖隐藏的可能值,第一个为错误解法
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
def p(k1):
    di = [float('inf')] * (n + 1)
    vi = [False] * (n + 1)
    di[1] = 0
    cost = di[:]
    heap = [(0, 1, 0)]
    while heap:
        len1, u, c = heapq.heappop(heap)
        if vi[u]:
            continue
        vi[u] = True
        for v, le, t in l[u]:
            if v==n:
                if not vi[v] and di[v] > len1 + le and t + c <= k:
                    di[v] = len1 + le
                    cost[v] = t + c
                    heapq.heappush(heap, (di[v], v, cost[v]))
                elif di[v] == len1 + le and cost[v] > t + c and t + c <= k:
                    cost[v] = t + c
                    heapq.heappush(heap, (di[v], v, cost[v]))
            else:
                if not vi[v] and di[v] > len1 + le and t + c <= k1:
                    di[v] = len1 + le
                    cost[v] = t + c
                    heapq.heappush(heap, (di[v], v, cost[v]))
                elif di[v] == len1 + le and cost[v] > t + c and t + c <= k1:
                    cost[v] = t + c
                    heapq.heappush(heap, (di[v], v, cost[v]))
    return di[n] if di[-1]!=float('inf') else -1
ans=float('inf')
for i in range(1,k):
    ans1=p(i)
    if ans1!=-1:
        if ans1<ans:
            ans=ans1
print(ans if ans!=float('inf') else -1)
#要么将visit条件放宽，加一个cost或者直接去掉visit，在循环里面结束。为了不掩盖可能的解，要把di去掉
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
def solve():
    vi = set()
    heap = [(0, 1, 0)]
    while heap:
        len1, u, c = heapq.heappop(heap)
        if u == n:
            return len1
        vi.add((u, c))
        for v, le, t in l[u]:
            if (v,t+c) not in vi and t + c <=k:
                heapq.heappush(heap, (len1+le, v, t+c))
    return -1
print(solve())
#感觉好用一点的vi列表：
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
def solve():
    vi =[float('inf')]*(n+1)
    heap = [(0, 1, 0)]
    while heap:
        len1, u, c = heapq.heappop(heap)
        if u == n:
            return len1
        if  c>vi[u]:
            continue
        vi[u]=c
        for v, le, t in l[u]:
            if t + c <=k:
                heapq.heappush(heap, (len1+le, v, t+c))
    return -1
print(solve())
#也可以去掉vi只是时间会比较长。而且当len1和cost都是0的时候会形成闭合的圈导致死循环（其余的不会，因为只要cost或者len1中的一个增加就一定会超过ans,从而不会死循环）
#10
#4
#4
#1 2 1 1
#2 3 0 0
#3 2 0 0
#3 4 1 2
#如何没有visit就会死循环。
#下面的代码也不行，很好得说明了bfs仅仅只在跨度为一（或者相等的情况下）成立，二位多跨度要么松弛Dijkstra要么dp
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
dist=[float('inf')]*(n+1)
dist[1]=0
heap=[(0,0,1)]
while heap:
    cost,way,u=heapq.heappop(heap)
    for v,len1,t in l[u]:
        if len1+way<dist[v] and t+cost<=k:
            dist[v]=len1+way
            heapq.heappush(heap,(t+cost,len1+way,v))
print(dist[n] if dist[-1]!=float('inf') else -1)

