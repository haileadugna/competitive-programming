# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def run(root):
            if not root :
                return
            run(root.left)
            res.append(root.val)
            run(root.right)
        run(root)
      
        return res
        