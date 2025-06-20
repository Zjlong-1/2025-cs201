# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#以某个点为起点的最大路径值，但好像又不行，这个是求联通图的最大路径数。由于只能确定下面的是什么，无法回溯知道下面的，以最上方的点为依据，左子树和右子树分别的max。还不够，要起点和最高点都递归
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def f(start):
            if not start:
                return 0
            return start.val+max(f(start.left),f(start.right),0)
        def dfs(node):
            if not node:
                return 0
            x=node.val
            x1=f(node.left)
            x2=f(node.right)
            if x1>0:
                x+=x1
            if x2>0:
                x+=x2
            return x
        if root.left and root.right:
            return max(dfs(root),self.maxPathSum(root.left),self.maxPathSum(root.right))
        elif root.left:
            return max(dfs(root),self.maxPathSum(root.left))
        elif root.right:
            return max(dfs(root),self.maxPathSum(root.right))
        return root.val
#复杂了一点，其实可以将dfs遍历，不断取max:
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum

#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.return_biggest(root)
        return self.result

    def return_biggest(self, root):
        if root.left is None and root.right is None:
            if root.val > self.result:
                self.result = root.val
            return root.val
        left = 0
        right = 0
        if root.left is not None:
            left = max(self.return_biggest(root.left), 0)
        if root.right is not None:
            right = max(0, self.return_biggest(root.right))
        if left + right + root.val > self.result:
            self.result = left + right + root.val
        return max(left, right) + root.val
