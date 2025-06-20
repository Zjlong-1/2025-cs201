from collections import deque
t=int(input())
di=[(0,-1),(0,1),(1,0),(-1,0)]
def bfs(start,end):
    q=deque()
    inq=set()
    q.append((start,0))
    inq.add(start)
    while q:
        (x,y),length=q.popleft()
        if (x,y)==end:
            return length
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<r and 0<=ny<c and (nx,ny) not in inq and maze[nx][ny]!='#':
                inq.add((nx,ny))
                q.append(((nx,ny,),length+1))
    return 'oop!'
for _ in range(t):
    r, c = map(int, input().split())
    maze = []
    start = end = (0, 0)
    for i in range(r):
        s = list(input())
        for j in range(c):
            if s[j] == 'S':
                start = (i, j)
            elif s[j] == 'E':
                end = (i, j)
        maze.append(s)
    print(bfs(start,end))


