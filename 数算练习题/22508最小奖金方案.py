from functools import lru_cache
n,m=map(int,input().split())
l=[[] for _ in range(n)]
ind=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    ind[b]+=1
ans=0
l1=[i for i in range(n) if ind[i]==0]
s=set()
@lru_cache(maxsize=None)
def depth(i):
    global ans
    if i in s:
        return
    s.add(i)
    t=0
    for j in l[i]:
        t=max(depth(j)+1,t)
    ans+=t
    return t

for i in l1:
    depth(i)
print(ans+n*100)

