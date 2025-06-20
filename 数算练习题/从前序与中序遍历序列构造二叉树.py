# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        head=preorder[0]
        leftlen=inorder.index(head)
        return TreeNode(head,self.buildTree(preorder[1:leftlen+1],inorder[:leftlen]),self.buildTree(preorder[leftlen+1:],inorder[leftlen+1:]))
#同样加哈希表会快很多：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {}
        for i in range(len(inorder)):
            val_to_index[inorder[i]] = i

        def build(preorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            index = val_to_index[root_val]
            left_size = index - in_start

            root.left = build(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, index - 1)
            root.right = build(preorder, pre_start + left_size + 1, pre_end, inorder, index + 1, in_end)

            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)