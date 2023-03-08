# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        res = []
        def run(root, k):
            if not root :
                return 0
            run(root.left, k)
            self.ans += 1
            if self.ans == k:
                res.append(root.val)
            run(root.right, k)
        run(root, k)
        return res[0]