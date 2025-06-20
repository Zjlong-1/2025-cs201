m=int(input())
s=input()
n=len(s)//m
t=len(s)
l=[[' ']*m for _ in range(n)]
for i in range(n):
    if i%2==1:
        for j in range(m):
            l[i][m-1-j]=s[i*m+j]
    else:
        for j in range(m):
            l[i][j]=s[i*m+j]
print(''.join(l[i][j] for j in range(m) for i in range(n)))