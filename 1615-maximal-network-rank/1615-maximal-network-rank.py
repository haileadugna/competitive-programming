class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
            
         
        res = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                cur_i = graph[i]
                cur_j = graph[j]
                if i in cur_j or j in cur_i:
                    res = max(res, len(cur_i) + len(cur_j ) - 1)
                else:
                    res = max(res, len(cur_i) + len(cur_j ))
    
        # print(graph)
        return res