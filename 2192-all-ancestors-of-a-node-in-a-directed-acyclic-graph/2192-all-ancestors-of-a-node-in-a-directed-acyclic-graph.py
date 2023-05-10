class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        incoming = [0] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            incoming[edge[1]] += 1
            
        todo = deque()
        for i in range(n):
            if incoming[i] == 0:
                todo.append(i)
       
        res = [set() for i in range(n)]
        while todo:
            node = todo.popleft()
            
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    todo.append(neighbor)
                res[neighbor].add(node)
                for i in res[node]:
                    res[neighbor].add(i)
                
          
        
        return map(sorted, res)
                
            