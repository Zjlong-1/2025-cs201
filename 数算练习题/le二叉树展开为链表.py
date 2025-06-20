# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if root.left and root.right:
            self.flatten(root.left)
            self.flatten(root.right)
            left,right=root.left,root.right
            root.left=None
            root.right=left
            while left.right:
                left=left.right
            left.right=right
        elif root.left:
            self.flatten(root.left)
            left,right=root.left,root.right
            root.left=None
            root.right=left
        elif root.right:
            self.flatten(root.right)