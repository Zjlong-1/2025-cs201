n,m=map(int,input().split())
l=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
s=set()
flag=False
def dfs(x,pre):
    global  flag
    s.add(x)
    for i in l[x]:
        if i not in s:
            dfs(i,x)
        elif i!=pre:
            flag=True
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




