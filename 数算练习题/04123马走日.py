#虽然一看就会，知道就是DFS。但是估计一下这个时间复杂度是不是会太高，仔细一想发现是自己变成小丑了。也就是每次8个方向而已
# pylint: skip-file
def dfs(a,b,cnt):
    global ans
    if cnt==m*n:
        ans+=1
        return
    for dx,dy in di:
        nx,ny=dx+a,dy+b
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
            visit[nx][ny]=True
            dfs(nx,ny,cnt+1)
            visit[nx][ny]=False

di=[(2,1),(2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(-2,1),(-2,-1)]
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    visit = [[False] * m for _ in range(n)]
    ans=0
    visit[x][y]=True
    dfs(x,y,1)
    print(ans)
#好久没有敲代码又忘记了静态检测，全局变量要在一开始声明