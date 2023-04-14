# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res =0
        def dfs(node, num):
            nonlocal res
            if not node:
                return 0

            num = num * 10 + node.val

            if not node.left and not node.right:
                res += num
                return num

            left = dfs(node.left, num)
            right = dfs(node.right, num)

            return left + right

        dfs(root, 0)

        return res