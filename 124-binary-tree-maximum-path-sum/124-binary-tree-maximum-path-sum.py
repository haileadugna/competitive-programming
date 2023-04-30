# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            maxleft = max(left, 0)
            maxright = max(right, 0)
            
            res = max(res, maxleft + maxright + root.val)
            return root.val + max(maxleft, maxright)
        
        dfs(root)
        return res
            
            
            
            