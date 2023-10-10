# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(_sum, temp, root):
            
            if not root:
                return 
            
            if not root.right and not root.left and _sum  == root.val:    
                temp.append(root.val)
                res.append(temp[:])


            temp.append(root.val)
            # print(temp)
            dfs(_sum - root.val, temp[:], root.left)

            # temp.append(root.val)
            # print(temp)
            dfs(_sum - root.val, temp[:], root.right)
            # temp.pop()

        
        dfs(targetSum, [], root)
        return res
            
            