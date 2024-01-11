# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        # record the required maximum difference
        res = 0

        def helper(node, cur_max, cur_min):
            nonlocal res
            
            if not node:
                return
            # update `result`
            res = max(res, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return res
#         _MAX = float('inf')
#         _MIN = float('-inf')
        
#         def dfs(node, res):
#             if not node:
#                 return _MIN, res
            
#             if not node.left and not node.right:
#                 return node.val, res
            
#             left_min, res = dfs(node.left, res)
#             right_min, res = dfs(node.right, res)
            
#             node_min = min(left_min, right_min)
            
#             res = max(res, node.val - node_min)
            
#             return min(node_min, node.val), res
        
#         res = _MIN
#         _, ans = dfs(root, res)
        
#         return ans
