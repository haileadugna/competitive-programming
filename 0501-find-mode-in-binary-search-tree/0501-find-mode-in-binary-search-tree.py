# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.temp = defaultdict(int)
        def run(node):
            if not node:
                return
            run(node.left)
            self.temp[node.val] += 1
            run(node.right)
        run(root)
        res = self.temp
        ans = [[0, -1]]
        cnt = 0
        for key, val in res.items():
           
            while ans and val > ans[-1][1]:
                ans.pop()
            if not ans or ans[-1][1] == val :
                ans.append([key, val])
            
        result = []
        for num in ans:
            result.append(num[0])
        return result