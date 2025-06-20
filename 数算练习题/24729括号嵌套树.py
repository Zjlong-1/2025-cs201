class TreeNode:
    def __init__(self,val):
        self.l=[val]
s=input()
stack=[]
node=None
for i in s:
    if i!='(' and i!=')' and i!=',':
        node=TreeNode(i)
        if stack:
            stack[-1].l.append(node)
    elif i=='(':
        if node:
            stack.append(node)
            node=None
    elif i==')':
        if stack:
            node=stack.pop()
def q(root):
    ans=root.l[0]
    for i in root.l[1:]:
        ans+=q(i)
    return ans
def h(root):
    ans=''
    for i in root.l[1:]:
        ans+=h(i)
    ans+=root.l[0]
    return ans
print(q(node))
print(h(node))


