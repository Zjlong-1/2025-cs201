#只有缝里面的才是轨道，边界不是
while True:
    n, m = map(int, input().split())
    if n==m==0:
        break
    l = [list(map(int, input().split())) for _ in range(n)]
    x1, y1, x2, y2, d1 = input().split()
    di=[(0,0),(0,-1),(0,1),(-1,-1)]
    s={'south':(-1,0),'north':(1,0),'west':(0,-1),'east':(0,1)}
    turn={'south':('east','west'),'north':('east','west'),'west':('north','south'),'east':('north','south')}
    l1=[[[True,True,True,True] for i in range(m)] for _ in range(n)]
    s1= {'south':0, 'north': 1, 'west':2, 'east':3}
    def pan(x,y):
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if l[nx][ny]==1:
                return False
        return True
    def dfs(x,y,d,l2):
        ans=float('inf')
        l2[x][y][s1[d]] = False
        if (x,y)==(int(x2),int(y2)):
            return 0
        for i in range(1,4):
            nx,ny=i*s[d][0]+x,i*s[d][1]+y
            if 0<nx<n and 0<ny<m and l2[nx][ny][s1[d]]:
                if pan(nx,ny):
                    l2[nx][ny][s1[d]]=False
                    cur=dfs(nx,ny,d,l2)
                    if cur!=-1:
                        ans = min(cur + 1, ans)
                    l2[nx][ny][s1[d]]=True
        if l2[x][y][s1[turn[d][0]]]:
            cur = dfs(x,y,turn[d][0],l2)
            if cur != -1:
                ans = min(cur + 1, ans)
        if l2[x][y][s1[turn[d][1]]]:
            cur = dfs(x, y, turn[d][1], l2)
            if cur != -1:
                ans = min(cur + 1, ans)
        if ans==float('inf'):
            return -1
        else:
            return ans
    print(dfs(int(x1),int(y1),d1,l1))
#无限制的最短路径，还是要用bfs:
from collections import deque

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    l = [list(map(int, input().split())) for _ in range(n)]
    x1, y1, x2, y2, d1 = input().split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    dir_map = {'south': 0, 'east': 1, 'north': 2, 'west': 3}
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def can_move(x, y):
        if not (0 <= x < n - 1 and 0 <= y < m - 1):
            return False
        for i in range(2):
            for j in range(2):
                if l[x + i][y + j] == 1:
                    return False
        return True
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    q = deque()
    dir_idx = dir_map[d1]
    if can_move(x1 - 1, y1 - 1):
        q.append((x1 - 1, y1 - 1, dir_idx, 0))
        visited[x1 - 1][y1 - 1][dir_idx] = True
    ans = -1
    while q:
        x, y, d, step = q.popleft()
        if (x, y) == (x2 - 1, y2 - 1):
            ans = step
            break
        for k in range(1, 4):
            nx = x + dx[d] * k
            ny = y + dy[d] * k
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if not can_move(nx, ny):
                break
            if not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                q.append((nx, ny, d, step + 1))
        nd = (d + 3) % 4
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, step + 1))
        nd = (d + 1) % 4
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x, y, nd, step + 1))
    print(ans)







