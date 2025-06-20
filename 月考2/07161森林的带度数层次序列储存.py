from collections import deque
class TreeNode:
    def __init__(self,name):
        self.name=name
        self.l=[]
def hou(root):
    if root is None:
        return
    for i in root.l:
        hou(i)
    print(root.name,end=' ')
n=int(input())
for _ in range(n):
    s=input().split()
    q=deque()
    root=TreeNode(s[0])
    q.append((root,int(s[1])))
    idx=2
    while q and idx<len(s):
        r,x=q.popleft()
        for i in range(x):
            childn,childl=s[idx],int(s[idx+1])
            child=TreeNode(childn)
            r.l.append(child)
            q.append((child,childl))
            idx+=2
    hou(root)
