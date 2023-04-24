# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(root):
            nonlocal res
            if not root :
                return
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left :
                        res += root.left.left.val
                    if root.left.right:
                        res += root.left.right.val
                        
                if root.right:
                    if root.right.left:
                        res += root.right.left.val
                    if root.right.right:
                        res += root.right.right.val
            dfs(root.left)
            dfs(root.right)
            # return res
            
        dfs(root)
        return res
        
                        