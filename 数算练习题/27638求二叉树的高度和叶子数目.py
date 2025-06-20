class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
n=int(input())
l=[Node(i) for i in range(n)]
l.append(None)
s=set()
for i in range(n):
    x,y=map(int,input().split())
    s.add(x)
    s.add(y)
    l[i].left=l[x]
    l[i].right=l[y]
for i in range(n):
    if i not in s:
        root=l[i]
l1=[]
cnt=0
def dfs(node):
    global cnt
    if not node:
        return -1
    if not node.left and not node.right:
        cnt+=1
        return 0
    ans=0
    ans=max(ans,1+dfs(node.left))
    ans=max(ans,1+dfs(node.right))
    return ans
print(dfs(root),cnt)


