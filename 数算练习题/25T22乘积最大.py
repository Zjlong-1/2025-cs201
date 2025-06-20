n,k=map(int,input().split())
la=[[0]*(k+1) for _ in range(n)]
s=input()
for i in range(n):
    la[i][0]=int(s[:i+1])
for i in range(1,k+1):
    for j in range(i,n):
        la[j][i]=max(la[t][i-1]*int(s[t+1:j+1]) for  t in range(i-1,j))
print(la[-1][-1])