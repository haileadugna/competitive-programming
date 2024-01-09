# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root.left is None and root.right is None:
                return [root.val]
            if root.right is not None and root.left is not None:
                return dfs(root.left) + dfs(root.right)
            if root.right is not None:
                return dfs(root.right)
            if root.left is not None:
                return dfs(root.left) 
        return dfs(root1) == dfs(root2)