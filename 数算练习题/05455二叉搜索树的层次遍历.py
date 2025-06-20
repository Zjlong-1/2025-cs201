from collections import deque
class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
def solve(node,new):
    if node.v<new.v:
        if not node.right:
            node.right=new
            return
        solve(node.right,new)
    else:
        if not node.left:
            node.left=new
            return
        solve(node.left,new)
l=list(map(int,input().split()))
s=set()
s.add(l[0])
root=Node(l[0])
for i in l[1:]:
    if i in s:
        continue
    s.add(i)
    new=Node(i)
    solve(root,new)
q=deque()
q.append(root)
while q:
    for _ in range(len(q)):
        node=q.popleft()
        print(node.v,end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)





