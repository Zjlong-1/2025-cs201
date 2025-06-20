# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        head = postorder[-1]
        leftlen = inorder.index(head)
        rightlen = len(inorder) - 1 - leftlen
        return TreeNode(head, self.buildTree(inorder[:leftlen], postorder[:leftlen]),
                        self.buildTree(inorder[leftlen + 1:], postorder[leftlen:len(inorder) - 1]))
#每次都要index时间复杂度有一点高，可以先用一个哈希表储存：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {element: i for i, element in enumerate(inorder)}
        def build(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            root_pos = index[root_val]
            left_size = root_pos - in_left
            root.left = build(in_left, root_pos - 1, post_left, post_left + left_size - 1)
            root.right = build(root_pos + 1, in_right, post_left + left_size, post_right - 1)
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)