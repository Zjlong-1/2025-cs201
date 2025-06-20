n=int(input())
l=list(map(int,input().split()))
ans=[]
flag=-1
if l[0]>l[1]:
    flag=1
else:
    flag=2
def dfs(x,s):
    global flag
    if s and s[-1]>l[x]:
        if flag!=1:
            flag=-1
    if s and s[-1]<l[x]:
        if flag!=2:
            flag=-1
    s.append(l[x])
    if 2*x+2<n:
        dfs(2*x+2,s[:])
    if 2*x+1<n:
        dfs(2*x+1,s[:])
    else:
        ans.append(s[:])
        return
dfs(0,[])
for i in ans:
    print(*i)
if flag==1:
    print('Max Heap')
elif flag==2:
    print('Min Heap')
else:
    print('Not Heap')