# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        
        def bfs(graph):
            queue = deque([graph])
            while queue:
                summ = 0
                n = len(queue)
                for i in range(n):
                    node = queue.popleft()
                    summ += node.val
                    if node.left:
                        left = node.left
                        queue.append(left)
                    if node.right:
                        right = node.right
                        queue.append(right)
                res.append(summ/n)
        bfs(root)       
        return res
                    
                    