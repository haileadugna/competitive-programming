# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        dictt = {0:1}
        summ = 0
        res = 0
        def dfs(root):
            nonlocal summ, res
            if not root:
                return 
            summ += root.val
            if summ - targetSum in dictt:
                res += dictt[summ - targetSum]
            dictt[summ] = dictt.get(summ, 0) + 1
            
            dfs(root.left)
            dfs(root.right)
            
            dictt[summ] -= 1
            summ -= root.val
            
        dfs(root)
        return res
            