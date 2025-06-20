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
n=int(input())
root=Node(float('inf'))
for _ in range(n):
    l=input().split()
    if len(l)==2:
        new=Node(int(l[-1]))
        solve(root,new)
    else:
        node=root
        parent=None
        while node.left:
            parent=node
            node=node.left
        print(node.v)
        parent.left=node.right
#要注意把去掉的点的右子树保留

