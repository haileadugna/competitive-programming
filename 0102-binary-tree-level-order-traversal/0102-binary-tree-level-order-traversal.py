# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dictt = {}
        self.vertical(root, 0, 0)
        # print(self.dictt)
     
        return self.dictt.values()

    def vertical(self, node, x, y):
        # If the node is None, return
        if not node:
            return 1
        
        if x in self.dictt:
            self.dictt[x].append(node.val)
        else:
            self.dictt[x] = [node.val]
 
        self.vertical(node.left, x + 1, y - 1)
        self.vertical(node.right, x + 1, y + 1)