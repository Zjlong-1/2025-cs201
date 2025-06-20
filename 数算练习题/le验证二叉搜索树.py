# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#要检查子树的每一个点！！
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def can(node,low=-float('inf'),higth=float('inf')):
            if not node:
                return True
            if not (low<node.val<higth):
                return False
            return can(node.left,low,node.val) and can(node.right,node.val,higth)
        return can(root)
#还可以用stack:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = root
        tmp = float('-inf')
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.val<=tmp:
                    return False
                tmp = current.val
                current = current.right
        return True