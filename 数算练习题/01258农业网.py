import heapq
while True:
    try:
        n=int(input())
    except EOFError:
        break
    l=[list(map(int,input().split())) for _ in range(n)]
    heap=[(0,0)]
    dist=[float('inf')]*n
    ans=0
    vi=[False]*n
    cnt=0
    while heap and cnt<n:
        w,u=heapq.heappop(heap)
        if vi[u]:
            continue
        ans+=w
        cnt+=1
        vi[u]=True
        for i in range(n):
            if not vi[i] and l[u][i]<dist[i]:
                dist[i]=l[u][i]
                heapq.heappush(heap,(l[u][i],i))
    print(ans)
