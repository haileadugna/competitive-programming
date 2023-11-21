# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total =0
        def check(node, left):
            if not node:
                return 
            check(node.left, True)
            check(node.right, False)
            if not node.left and not node.right and left:
                self.total += node.val
        check(root, False)
        return self.total