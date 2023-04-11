class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        graph1 = defaultdict(list)
        
        for i in range(n):
            for j in graph[i]:
                graph1[i].append(j) 
        res  = []
        temp = [0]
        
        def dfs(k):
            if k == n - 1:
                res.append(temp[:])
                return
            
            
            for i in graph1[k]:
                temp.append(i)
                dfs(i)
                temp.pop()
        dfs(0)   
        return res
       