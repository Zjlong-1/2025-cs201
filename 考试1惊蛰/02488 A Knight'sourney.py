di = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]
def can(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and (x, y) not in visited
def solve(n,m):
    all_positions = []
    for i in range(n):
        for j in range(m):
            all_positions.append((i, j))
    for start in all_positions:
        path = [start]
        visited = {start}
        def dfs(x, y):
            if len(path) == n *m:
                return True
            moves = []
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if can(nx, ny, n, m, visited):
                    moves.append((nx, ny))
            moves.sort(key=lambda x: (chr(x[0] + ord('A')),x[1] + 1))
            for nx, ny in moves:
                visited.add((nx, ny))
                path.append((nx, ny))
                if dfs(nx, ny):
                    return True
                path.pop()
                visited.remove((nx, ny))
            return False

        if dfs(start[0], start[1]):
            return ''.join(f"{chr(x + ord('A'))}{y + 1}" for x, y in path)
    return "impossible"
t = int(input())
for i in range(t):
    m,n = map(int, input().split())
    result = solve(n, m)
    print(f"Scenario #{i+1}:")
    print(result)
    print()
