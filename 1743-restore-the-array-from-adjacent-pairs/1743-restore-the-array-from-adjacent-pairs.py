class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        res = []
        visited = set()
        
        graph = defaultdict(list)
        for edge in adjacentPairs:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        for i in list(graph.keys()):
            if len(graph[i]) == 1:
                start = i
        # print(start)        
        def dfs(node):
            visited.add(node)
            res.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    
                    dfs(neighbor)
              
        dfs(start)
        return res