#直接暴力模拟
n=int(input())
m=int(input())
l=[[0]*(2*m+1) for _ in range(2*n+1)]
for i in range(1,2*n+1,2):
    l1=list(map(int,input().split()))
    for j in range(m):
        k=bin(l1[j])[2:].zfill(4)
        if k[0]=='1':
            l[i+1][2*j+1]=l[i+1][2*j]=l[i+1][2*j+2]=1
        if k[1]==1:
            l[i+1][2*j+2]=l[i][2*j+2]=l[i-1][2*j+2]=1
        if k[2]=='1':
            l[i - 1][2 * j + 1] = l[i - 1][2 * j] = l[i - 1][2 * j + 2] = 1
        if k[3]=='1':
            l[i + 1][2 * j ] = l[i][2 * j] = l[i - 1][2 * j] = 1
ans=[]
di=[(0,2),(0,-2),(2,0),(-2,0)]

def dfs(x,y):
    global cnt
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<nx<2*n and 0<ny<2*m:
            mx,my=(x+nx)//2,(y+ny)//2
            if l[mx][my]==l[nx][ny]==0:
                cnt+=1
                l[nx][ny]=2
                dfs(nx,ny)
for i in range(1,2*n,2):
    for j in range(1,2*m,2):
        if l[i][j]==0:
            l[i][j]=2
            cnt=1
            dfs(i,j)
            ans.append(cnt)
print(len(ans))
print(max(ans))
