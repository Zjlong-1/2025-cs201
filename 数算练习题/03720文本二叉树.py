class Node:
    def __init__(self,v,d):
        self.d=d
        self.v=v
        self.left=None
        self.right=None
def q(node):
    if not node:
        return ''
    if node.v=='*':
        return ''
    return node.v+q(node.left)+q(node.right)
def h(node):
    if not node:
        return ''
    if node.v=='*':
        return ''
    return h(node.left)+h(node.right)+node.v
def z(node):
    if not node:
        return ''
    if node.v=='*':
        return ''
    return z(node.left)+node.v+z(node.right)
n=int(input())
for _ in range(n):
    l=[]
    stack=[]
    while True:
        s=input()
        if s=='0':
            break
        d=len(s)-1
        node=Node(s[-1],d)
        l.append(node)
        while stack and l[stack[-1]].d>=d:
            stack.pop()
        if stack:
            parent=l[stack[-1]]
            if not parent.left:
                parent.left=node
            else:
                parent.right=node
        stack.append(len(l)-1)
    print(q(l[0]))
    print(h(l[0]))
    print(z(l[0]))
    print()


