n,m=map(int,input().split())
l=list(map(int,input().split()))
s=[[i,l[i]] for i in range(n)]
def f(x):
    if x!=s[x][0]:
        s[x][0]=f(s[x][0])
    return s[x][0]
for _ in range(m):
    x,y=map(int,input().split())
    x1,y1=f(x-1),f(y-1)
    if x1!=y1:
        s[y1][0]=x1
        s[x1][1]=min(s[x1][1],s[y1][1])
s1=set()
ans=0
for i in range(n):
    t=f(i)
    if t not in s1:
        s1.add(t)
        ans+=s[t][1]
print(ans)
