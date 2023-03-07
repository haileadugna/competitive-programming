# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                
        return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ans =0
        # queue= deque([root])
        # if not root:
        #     return 0
        # while queue:
        #     for i in range(len(queue)):
        #         n = queue.popleft()               
        #         if  n.left :
        #             queue.append(n.left)
        #         if n.right:
        #             queue.append(n.right)
        #     ans += 1
        # return ans