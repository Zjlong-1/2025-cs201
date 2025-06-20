#一看就是bfs，但不是一个一个pop，而是一层一层的处理。
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            for _ in range(n-1):
                t=q.popleft()
                t.next=q[0]
                if t.left:
                    q.append(t.left)
                    q.append(t.right)
            t=q.popleft()
            if t.left:
                q.append(t.left)
                q.append(t.right)

        return root