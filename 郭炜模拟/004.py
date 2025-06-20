from collections import defaultdict
n,m=map(int,input().split())
s=[i for i in range(n+1)]
def f(x):
    if s[x]!=x:
        s[x]=f(s[x])
    return s[x]
for _ in range(m):
    x,y=map(int,input().split())
    x1,y1=f(x),f(y)
    if x1!=y1:
        s[x1]=y1
di=defaultdict(int)
ans=[]
for i in range(1,n+1):
    k=f(i)
    di[k]+=1
    ans.append(k)
print(len(di))
for k in ans[:min(100,n)]:
    print(di[k],end=' ')

