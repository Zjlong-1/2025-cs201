#可惜了，有bug:inq 访问记录可能会导致漏算最短路径
#不同路径可能会以相同步数到达某点，此时这个点已经在 inq 里面了，导致 另一条最短路径不会被统计。
#所以这种多路径的一定要用dfs
from collections import deque
start1,start2=map(int,input().split())
end1,end2=map(int,input().split())
s={tuple(map(int,input().split())) for _ in range(int(input()))}
def bfs():
    q = deque()
    inq = set()
    q.append((start1,start2,0,[(start1,start2)]))
    inq.add((start1,start2))
    flag=False
    t=0
    ans=1
    w=[]
    di=[(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(-1,2),(2,-1),(-2,1)]
    while q:
        x,y,step,way=q.popleft()
        if flag:
            if step==t and x==end1 and y==end2:
                ans+=1
            elif step>t:
                break
        else:
            if x==end1 and y==end2:
                flag=True
                t=step
                w=way[:]
                continue
            for dx,dy in di:
                nx,ny=dx+x,dy+y
                nx1,ny1=(nx+x)//2,(ny+y)//2
                if (nx1,ny1) not in s and 0<=nx<11 and 0<=ny<11 and (nx,ny) not in inq and (nx,ny) not in s:
                    q.append((nx,ny,step+1,way+[(nx,ny)]))
                    inq.add((nx,ny))
    if ans>1:
        print(ans)
    else:
        print('-'.join([str(k) for k in w]))
bfs()
#正解：
import sys
sys.setrecursionlimit(10000)
start1, start2 = map(int, input().split())
end1, end2 = map(int, input().split())
num_obstacles = int(input())
obstacles = {tuple(map(int, input().split())) for _ in range(num_obstacles)}
directions = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-1, 2), (2, -1), (-2, 1)]
best_steps = float('inf')
best_path = []
path_count = 0
def dfs(x, y, steps, path, visited):
    global best_steps, best_path, path_count
    if steps > best_steps:
        return
    if (x, y) == (end1, end2):
        if steps < best_steps:
            best_steps = steps
            best_path = path[:]
            path_count = 1
        elif steps == best_steps:
            path_count += 1
        return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx <= 10 and 0 <= ny <= 10):
            continue
        mx, my = (x + nx) // 2, (y + ny) // 2
        if (mx,my) in obstacles or (nx, ny) in obstacles:
            continue
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            dfs(nx, ny, steps + 1, path + [(nx, ny)], visited)
            visited.remove((nx, ny))
visited = {(start1, start2)}
dfs(start1, start2, 0, [(start1, start2)], visited)
if path_count == 1:
    print('-'.join(f"({r},{c})" for r, c in  best_path))
else:
    print(str(path_count))
#最后还要注意这个元组中的空格，很容易多打导致PE
