import heapq

a, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = 0
        else:
            if l[i][j] > a:
                l[i][j] = a

def prim_dense():
    used = [False] * n
    dist = [a] * n
    dist[0] = 0
    total = 0
    for _ in range(n):
        u = -1
        best = a + 1
        for v in range(n):
            if not used[v] and dist[v] < best:
                best = dist[v]
                u = v
        used[u] = True
        total += dist[u]
        for v in range(n):
            if not used[v] and l[u][v] < dist[v]:
                dist[v] = l[u][v]
    return total
print(prim_dense() + a)
