# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def nextval(node):
            while node.right:
                node = node.right
            return node.val
        def preval(node):
            while node.left:
                node = node.left
            return node.val
                
        def search(node, key):
            if not node:
                return
            if key < node.val:
                node.left = search(node.left, key)
            elif key > node.val:
                node.right = search(node.right, key)
            elif key == node.val:
                if node.right:
                    node.val = preval(node.right)
                    key = node.val
                    node.right = search(node.right, key)
                elif node.left:
                    node.val = nextval(node.left)
                    key = node.val
                    node.left = search(node.left, key)
                else:
                    node = None
            return node
        return search(root, key)
        
            