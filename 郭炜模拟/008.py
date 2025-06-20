from collections import deque
class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
l=list(map(int,input().split()))
n=len(l)
m=int(input())
root=Node(l[0])
q=deque([root])
cnt=1
while q:
    t=q.popleft()
    if cnt==n:
        break
    if l[cnt]==-1:
        cnt+=1
    else:
        t.left=Node(l[cnt])
        q.append(t.left)
        cnt+=1
    if cnt==n:
        break
    if l[cnt]==-1:
        cnt+=1
    else:
        t.right=Node(l[cnt])
        cnt+=1
        q.append(t.right)
def d(node):
    if not node.left and not node.right:
        return 0
    ans=1
    if node.left:
        ans=1+d(node.left)
    if node.right:
        ans=max(ans,1+d(node.right))
    return ans
def f(node):
    if not node:
        return None
    if node.v==m:
        return node
    if f(node.left):
        return f(node.left)
    if f(node.right):
        return f(node.right)
    return None
k=f(root)
left=d(root.left)
right=d(root.right)
d1=d(k)


