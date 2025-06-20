# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,cur):#不中途换起点的dfs
            if not node:
                return 0
            cnt=0
            if node.val+cur==targetSum:
                cnt+=1
            cnt+=dfs(node.left,cur+node.val)
            cnt+=dfs(node.right,cur+node.val)
            return cnt
        if not root :
            return 0
        return dfs(root,0)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)
#时间优化：（用哈希表）和前缀和的思想一样。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        cnt=defaultdict(int)
        cnt[0]=1
        def dfs(node,s):
            if node is None:return
            nonlocal ans
            s+=node.val
            ans+=cnt[s-targetSum]
            cnt[s]+=1
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s]-=1
        dfs(root,0)
        return ans
