n=int(input())
l=[[] for _ in range(n)]
l1=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    l1.append((a,b))
s=set(map(int,input().split()))
for a,b in l1:
    if a in s or b in s:
        continue
    l[a].append(b)
    l[b].append(a)
vi=set()
def dfs(x):
    vi.add(x)
    for i in l[x]:
        if i not in vi:
            dfs(i)
dfs(0)
print(len(vi))


