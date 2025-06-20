import heapq
n,m=map(int,input().split())
l=[[]for _ in range(n+1)]
for _ in range(m):
    u,v,z=map(int,input().split())
    l[u].append((v,(100-z)/100))
    l[v].append((u,(100-z)/100))
a,b=map(int,input().split())
def d():
    di = [0] * (n + 1)
    vi = [False] * (n + 1)
    heap = [(-1,a)]
    di[a]=1
    while heap:
        d1,u1 = heapq.heappop(heap)
        d1=-d1
        if vi[u1]:
            continue
        vi[u1] = True
        for v1, le in l[u1]:
            if not vi[v1] and di[v1]<le*d1:
                di[v1] =le*d1
                heapq.heappush(heap, (-di[v1],v1))
    return di[b]
print(int(100/d()))