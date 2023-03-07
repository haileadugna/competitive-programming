# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def run(root):
            if not root :
                return
            run(root.left)
            run(root.right)
            res.append(root.val)
        run(root)
      
        return res