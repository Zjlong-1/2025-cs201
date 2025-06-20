# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 每一层的最右边的数，直接deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            stack = []
            for _ in range(n):
                node = q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                stack.append(node.val)
            if stack:
                ans.append(stack[-1])

        return ans
