import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[] for _ in range(n+1)]
for _ in range(r):
    s,d,w,t=map(int,input().split())
    l[s].append((d,w,t))
def solve():
    time = [float('inf')] * (n+1)
    heap=[(0,1,0)]
    while heap:
        w,u,t=heapq.heappop(heap)
        if u==n:
            return w
        if t>time[u]:
            continue
        time[u]=t
        for v,len1,t1 in l[u]:
            if t1+t<=k:
                heapq.heappush(heap,(len1+w,v,t1+t))
    return -1
print(solve())