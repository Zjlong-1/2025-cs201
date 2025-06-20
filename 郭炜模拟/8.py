from collections import deque, defaultdict
vals = list(map(int,input().split()))
start = int(input())
adj = defaultdict(list)

n = len(vals)
q = deque()
q.append(vals[0])
i = 1
while q and i < n:
    u = q.popleft()
    if i < n:
        v = vals[i]
        i += 1
        if v != -1:
            adj[u].append(v)
            adj[v].append(u)
            q.append(v)
    if i < n:
        v = vals[i]
        i += 1
        if v != -1:
            adj[u].append(v)
            adj[v].append(u)
            q.append(v)
dist = {start: 0}
q = deque([start])
max_dist = 0
while q:
    u = q.popleft()
    d = dist[u]
    max_dist = max(max_dist, d)
    for w in adj[u]:
        if w not in dist:
            dist[w] = d + 1
            q.append(w)
print(max_dist)


