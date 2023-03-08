# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
    
        left = root.left
        right = root.right
        def run(left, right):
            if not left and not right:
                return True
            if not left and right:
                return False
            if not right and left:
                return False
            if left.val == right.val:
                return run(left.left, right.right) and run(left.right, right.left)
            
        return run(left, right)
