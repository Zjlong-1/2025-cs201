class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
s=input()
def build(idx):
    if s[idx]=='.':
        return None,idx+1
    node=Node(s[idx])
    idx+=1
    node.left,idx=build(idx)
    node.right,idx=build(idx)
    return node,idx
root,t=build(0)
def z(node):
    if not node:
        return ''
    return z(node.left)+node.v+z(node.right)
def h(node):
    if not node:
        return ''
    return h(node.left)+h(node.right)+node.v
print(z(root))
print(h(root))

