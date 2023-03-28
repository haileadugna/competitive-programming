# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        nums = []
        def dfs(root, cur):
            if not root:
                return res.append(cur)
                return
            
            dfs(root.left, cur + str(root.val) + "->")
            dfs(root.right, cur + str(root.val) + "->")
            
        dfs(root, "")
        dictt = Counter(res)
        for string in list(dictt.keys()):
            if dictt[string] == 2:
                nums.append(string[:-2])
        return nums