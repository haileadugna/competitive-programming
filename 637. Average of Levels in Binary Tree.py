# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans =[]
        queue= deque([root]) 
        while queue:
            temp = 0
            
            for i in range(len(queue)):
                temp += queue[i].val
            avr = temp/len(queue)
            ans.append(avr)
            for j in range(len(queue)):
                n = queue.popleft()
                if  n.left :
                    queue.append(n.left)
                
                if n.right:
                    queue.append(n.right)
        return ans