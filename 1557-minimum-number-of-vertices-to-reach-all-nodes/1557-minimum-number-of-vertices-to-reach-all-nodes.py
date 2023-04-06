class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(int)
        
        for edge in edges:
            graph[edge[1]] += 1
            
        res = []
        for i in range(n):
            if i not in graph:
                res.append(i)
          
        # visited = set()
#         res = []
#         queue = deque()
        
#         while queue:
#             cur = queue.popleft()
            
#             if i not in visited:
#                 res.append(i)
#             for num in graph[cur]:
#                 visited.add(num)
                
        return res