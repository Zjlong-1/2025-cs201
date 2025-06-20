from collections import deque
n=int(input())
di=[(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]
for _ in range(n):
    m,n=map(int,input().split())
    def bfs(i,j):
        q=deque()
        inq=set()
        inq.add((i,j))
        q.append((i,j,1,[(i,j)]))
        while q:
            x,y,length,way=q.popleft()
            if length==n*m:
                return way
            for dx,dy in di:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in inq:
                    inq.add((nx,ny))
                    q.append((nx,ny,length+1,way+[(nx,ny)]))
        return False
    for i in range(n):
        for j in range(m):
            l=bfs(i,j)
            if l:
                for x,y in l:
                    print(f'{chr(x+ord('A'))}{y+1}',end='')
                break
    if not l:
        print('impossible')
#bfs无法实现，要用dfs