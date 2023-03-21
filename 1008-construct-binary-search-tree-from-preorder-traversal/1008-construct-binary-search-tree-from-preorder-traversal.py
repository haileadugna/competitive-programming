# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            self.insertt(root, num)
        return root
    def insertt(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertt(root.left, val)
        if val > root.val:
            root.right = self.insertt(root.right, val)
        return root
        