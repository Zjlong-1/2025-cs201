import heapq
import heapq
while True:
    try:
        n=int(input())
    except EOFError:
        break
    l = [list(map(int, input().split())) for _ in range(n)]
    heap = [(0, 0)]
    vi = [False] * n
    dist = [float('inf')] * n
    dist[0] = 0
    ans = 0
    cnt = 0
    while heap and cnt < n:
        w, u = heapq.heappop(heap)
        if vi[u]:
            continue
        ans += w
        cnt += 1
        vi[u] = True
        for i in range(n):
            if not vi[i]:
                if dist[i] > l[i][u]:
                    heapq.heappush(heap, (l[i][u], i))
                    dist[i] = l[i][u]
    print(ans)