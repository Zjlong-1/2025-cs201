#注意：每一个只能走一次
#Warnsdorff 规则,有序的走
n=int(input())
r,c=map(int,input().split())
di=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
l1=[[0]*n for _ in range(n)]
def rule(x,y):
    m=0
    for dx,dy in di:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<n and l1[nx][ny]==0:
            m+=1
    return m
def dfs(x,y,cnt,l):
    if cnt==n*n:
        return True
    rulel=[]
    for dx,dy in di:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<n and l[nx][ny]==0:
            rulel.append((rule(nx,ny,),nx,ny))
    rulel.sort()
    for t,nx,ny in rulel:
        l[nx][ny]=1
        if dfs(nx,ny,cnt+1,l):
            return True
        l[nx][ny]=0
    return False
l1[c][r]=1
if dfs(c,r,1,l1):
    print('success')
else:
    print('fail')

