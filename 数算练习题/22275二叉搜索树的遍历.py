class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
n=int(input())
l=list(map(int,input().split()))
def build(l1):
    m=len(l1)
    if not l1:
        return None
    if m==1:
        return Node(l1[0])
    t=m
    for i in range(m):
        if l1[i]>l1[0]:
            t=i
            break
    root=Node(l1[0])
    root.left=build(l1[1:t])
    root.right=build(l1[t:])
    return root
tree=build(l)
def hou(node):
    if not node:
        return
    hou(node.left)
    hou(node.right)
    print(node.v,end=' ')
hou(tree)
