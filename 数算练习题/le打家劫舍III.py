# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def f(node):#包含自己
            if not node:
                return 0
            return g(node.left)+g(node.right)+node.val
        @cache
        def g(node):
            if not node:
                return 0
            return max(f(node.left),g(node.left))+max(f(node.right),g(node.right))
        return max(f(root),g(root))
#还可以一个函数解决：
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,0
            lrob,lnot= dfs(node.left)
            rrob,rnot= dfs(node.right)
            rob,notrob=node.val+lnot+rnot,max(lrob,lnot)+max(rrob,rnot)
            return rob,notrob
        return max(dfs(root))