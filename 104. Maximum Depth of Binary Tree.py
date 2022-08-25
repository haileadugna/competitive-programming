# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans =0
        queue= deque([root])
        if not root:
            return 0
        while queue:
            for i in range(len(queue)):
                n = queue.popleft()               
                if  n.left :
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            ans += 1
        return ans
        # queue = deque([root])
        # visited = set()
        # print(visited)
        # print(queue)
        # while queue:
        #     current = queue.popleft()
        #     print(current)
        #     for neighbour in queue[current]:
        #         if neighbour not in visited:
        #             visited.add(neighbour)
        #             queue.apped(neighbour)
        #     print(queue)
        # # print(queue)