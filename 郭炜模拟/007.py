n,m=map(int,input().split())
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,input().split())
    l[x].append(y)
stack=[m]
ans=0
while stack:
    t=stack.pop()
    stack+=l[t][:]
    ans+=1
print(ans)


