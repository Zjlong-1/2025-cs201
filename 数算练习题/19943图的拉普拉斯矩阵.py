n,m=map(int,input().split())
A=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    A[a][b]=-1
    A[b][a]=-1
    A[a][a]+=1
    A[b][b]+=1
for i in range(n):
    print(*A[i])


