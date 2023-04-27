class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i].append(key)
                
        def bfs(graph):
            visited = set()
            queue = deque()
            visited.add(0)
            queue.append(0)
            
            while queue:
                node = queue.popleft()
                for key in graph[node]:
                    if key not in visited:
                        queue.append(key)
                        visited.add(key)
                
            return visited
        res = bfs(graph)
        if len(res) == len(rooms) :
            return True
        return False
                    
                
                    
#         keys = set()
#         keys.add(0)
#         for i in range(len(rooms)):
#             if i in keys:
#                 for j in range(len(rooms[i])):
#                     keys.add(rooms[i][j])
                    
#             else:
#                 return False
        # return True