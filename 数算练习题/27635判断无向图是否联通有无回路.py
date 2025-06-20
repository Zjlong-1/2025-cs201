#无向图：建立双边联系再用dfs搜索
n,m=map(int,input().split())
l=[[]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
def dfs(x,y):
    global s,flag
    s.add(x)
    for i in l[x]:
        if i not in s:
            dfs(i,x)
        elif i!=y:
            flag=True
s=set()
flag=False
for j in range(n):
    s.clear()
    dfs(j,-1)
    if len(s)==n:
        break
    if flag:
        break
if len(s)==n:
    print('connected:yes')
else:
    print('connected:no')
if flag:
    print('loop:yes')
else:
    print('loop:no')

