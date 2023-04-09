"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_depth = 0
        
        def getdepth(node, depth):
            nonlocal max_depth
            if not node:
                return 0
            max_depth = max(depth, max_depth)
            for child in node.children:
                getdepth(child, depth + 1)
                
        getdepth(root, 1)       
        return max_depth
        
            